"""The two paper bots. Each call to tick() handles exits first, then looks for new entries."""
import datetime as dt
import os
import time

import market
import paper


def _now_ms() -> int:
    return int(time.time() * 1000)


# ---------------- Bot A: crypto rules (spot, long only) ----------------
def crypto_tick(acc: dict, cfg: dict, log: list, data=None) -> dict:
    fee, slip = cfg["fee_rate"], cfg["slippage_rate"]
    prices = {}
    for sym in cfg["symbols"]:
        m1 = data[sym]["1m"] if data else market.klines(sym, "1m", 240)
        prices[sym] = m1[-1]["c"]
        for tr in paper.check_exits(acc, sym, m1,
                                    exit_fill=lambda side, lvl: lvl * (1 - slip),
                                    exit_fee=lambda px, q: px * q * fee):
            log.append(f"{cfg.get('tag', 'A')}  CLOSE {sym} {tr['reason']}: {tr['pnl']:+.2f} USD")

    ok, why = paper.can_open(acc, cfg["max_trades_per_day"], acc["start"] * cfg["daily_loss_limit_pct"])
    if not ok:
        return prices
    for sym in cfg["symbols"]:
        if len(acc["positions"]) >= cfg["max_open"] or any(p["symbol"] == sym for p in acc["positions"]):
            continue
        recent = [t for t in acc["trades"] if t["symbol"] == sym and _now_ms() - t["closed_ms"] < 30 * 60_000]
        if recent:
            continue  # cool-down after a trade on the same coin
        m5 = data[sym]["5m"] if data else market.klines(sym, cfg["interval"], 300)
        closes = [c["c"] for c in m5 if c["closed"]]
        if len(closes) < 210:
            continue
        e200, r = market.ema(closes, 200)[-1], market.rsi(closes, 14)
        trend_ok = closes[-1] > e200 if cfg.get("trend_filter", True) else True
        # optional "bounce" rules: a real drop first, then the first green candle
        lookback = cfg.get("drop_lookback_candles", 24)
        dropped = ((max(closes[-lookback:]) - closes[-1]) / max(closes[-lookback:]) >= cfg["min_drop_pct"]
                   if cfg.get("min_drop_pct") else True)
        last_c = [c for c in m5 if c["closed"]][-1]
        green = last_c["c"] > last_c["o"] if cfg.get("require_green_candle") else True
        if trend_ok and dropped and green and r[-1] < cfg["rsi_buy_below"] and r[-1] > r[-2]:
            price = prices[sym] * (1 + slip)
            notional = min(acc["balance"] * cfg["position_pct"], acc["balance"] - sum(
                p["qty"] * p["entry"] for p in acc["positions"]))
            if notional < 10:
                continue
            qty = notional / price
            paper.open_position(acc, symbol=sym, side="long", price=price, qty=qty,
                                tp=price * (1 + cfg["take_profit_pct"]), sl=price * (1 - cfg["stop_loss_pct"]),
                                t_ms=_now_ms(), entry_cost=notional * fee, max_hold_min=cfg["max_hold_minutes"],
                                margin=notional, note=f"RSI {r[-1]:.0f}, above EMA200")
            log.append(f"{cfg.get('tag', 'A')}  BUY {sym} {notional:.0f} USD @ {price:.2f} (RSI {r[-1]:.0f})")
    return prices


# ---------------- Bot B: gold news (leveraged, long or short) ----------------
def gold_market_open(now: dt.datetime | None = None) -> bool:
    """Real gold (XAU/USD) closes from Friday 21:00 to Sunday 22:00 UTC; no new trades then."""
    n = now or dt.datetime.now(dt.timezone.utc)
    wd, h = n.weekday(), n.hour
    return not (wd == 5 or (wd == 4 and h >= 21) or (wd == 6 and h < 22))


def gold_tick(acc: dict, cfg: dict, news_cfg: dict, state: dict, log: list, api_key: str | None,
              data=None, sentiment_fn=None, shared_news: dict | None = None, tag: str = "B") -> dict:
    sym, slip = cfg["symbol"], cfg["slippage_rate"]
    m1 = data[sym]["1m"] if data else market.klines(sym, "1m", 240)
    price_now = m1[-1]["c"]
    half = cfg["spread_usd_per_oz"] / 2

    def exit_fill(side, lvl):  # closing a long sells at bid, closing a short buys at ask
        return lvl - half - lvl * slip if side == "long" else lvl + half + lvl * slip

    # targets changed in config.yaml -> open positions follow the new TP/SL too (measured from their own entry)
    for p in acc["positions"]:
        if p["symbol"] != sym:
            continue
        tp_d, sl_d = cfg["take_profit_usd"] / p["qty"], cfg["stop_loss_usd"] / p["qty"]
        tp, sl = ((p["entry"] + tp_d, p["entry"] - sl_d) if p["side"] == "long"
                  else (p["entry"] - tp_d, p["entry"] + sl_d))
        moved = "be_trigger" in p and p["be_trigger"] is None  # B3 already moved its stop to break-even
        if abs(tp - p["tp"]) > 1e-6 or (abs(sl - p["sl"]) > 1e-6 and not moved):
            p["tp"], p["sl"] = tp, (p["sl"] if moved else sl)
            log.append(f"{tag}  hedefler güncellendi: TP {tp:.2f} (+{cfg['take_profit_usd']}$), SL {p['sl']:.2f} (-{cfg['stop_loss_usd']}$)")
    for tr in paper.check_exits(acc, sym, m1, exit_fill=exit_fill, exit_fee=lambda px, q: 0.0):
        log.append(f"{tag}  CLOSE {tr['side']} {tr['reason']}: {tr['pnl']:+.2f} USD")

    # news: headlines are checked on EVERY tick (free); Claude is asked only when new headlines arrived
    # (at most every news_min_minutes), or anyway every news_max_minutes so the view never gets stale.
    news = shared_news if shared_news is not None else state.setdefault("news", {})
    age_min = (_now_ms() - news.get("ts", 0)) / 60_000
    min_m = cfg.get("news_min_minutes", cfg.get("news_every_minutes", 30))
    max_m = cfg.get("news_max_minutes", cfg.get("news_every_minutes", 60))
    calls = state.setdefault("news_calls", {"date": paper.today(), "n": 0})
    if calls["date"] != paper.today():
        calls.update({"date": paper.today(), "n": 0})
    if (shared_news is None and (api_key or sentiment_fn) and age_min >= min_m
            and calls["n"] < cfg.get("news_max_calls_per_day", 120)):
        try:
            import news as news_mod
            lines = [] if sentiment_fn else news_mod.headlines(news_cfg["feeds"])
            seen = set(state.get("news_seen", []))
            new_lines = [x for x in lines if x.split("] ", 1)[-1] not in seen]
            if sentiment_fn or (lines and (new_lines or age_min >= max_m)) or (not lines and age_min >= max_m):
                res = sentiment_fn() if sentiment_fn else news_mod.gold_sentiment(
                    api_key, news_cfg["model"], news_cfg["feeds"], lines=lines, new_lines=new_lines)
                calls["n"] += 1
                # second, independent opinion from GPT on the same headlines (used by the consensus bot B5)
                res["gpt"] = None
                if os.environ.get("OPENAI_API_KEY", "").strip() and not sentiment_fn:
                    try:
                        res["gpt"] = news_mod.gpt_sentiment(news_cfg.get("gpt_models", ["gpt-6-luna"]),
                                                            lines, new_lines)
                    except Exception as e:  # noqa: BLE001  GPT never blocks the bots
                        log.append(f"N  GPT news failed: {str(e)[:160]}")
                news.update(res)
                news["ts"] = _now_ms()
                news["new_headlines"] = len(new_lines)
                state["news_seen"] = [x.split("] ", 1)[-1] for x in lines][:200]
                hist = state.setdefault("news_history", [])
                g = res.get("gpt") or {}
                hist.append({"ts": news["ts"], "score": res["score"], "confidence": res["confidence"],
                             "reason": res.get("reason", ""), "new": len(new_lines),
                             "gpt_score": g.get("score"), "gpt_confidence": g.get("confidence")})
                state["news_history"] = hist[-300:]
                log.append(f"N  NEWS ({len(new_lines)} new) score {res['score']:+.2f} conf {res['confidence']:.2f}: "
                           f"{res.get('reason', '')}")
                if g:
                    log.append(f"N  GPT  score {g['score']:+.2f} conf {g['confidence']:.2f}: {g.get('reason', '')}")
        except Exception as e:  # noqa: BLE001
            log.append(f"B  NEWS failed: {e}")

    ok, why = paper.can_open(acc, cfg["max_trades_per_day"], cfg["daily_loss_limit_usd"])
    if not ok or acc["positions"] or not gold_market_open():
        return {sym: price_now}
    hours = cfg.get("session_hours_utc")  # e.g. [7, 16] = London + New York (10:00-19:00 Istanbul)
    if hours and not (hours[0] <= dt.datetime.now(dt.timezone.utc).hour < hours[1]):
        return {sym: price_now}
    fresh = (_now_ms() - news.get("ts", 0)) / 60_000 <= 2 * cfg.get("news_max_minutes", cfg.get("news_every_minutes", 60))
    score, conf = news.get("score", 0.0), news.get("confidence", 0.0)
    if cfg.get("contrarian"):  # fade the news: trade AGAINST it, only when price already moves against it too
        score = -score
    if cfg.get("consensus"):  # B5: Claude AND GPT must agree on the direction; the weaker view decides the size
        g = news.get("gpt") or {}
        gs, gc = g.get("score"), g.get("confidence")
        if gs is None or gc is None or gs * score <= 0:
            return {sym: price_now}
        score = (score + gs) / 2 if abs(gs) >= cfg["min_score"] and abs(score) >= cfg["min_score"] else 0.0
        conf = min(conf, gc)
    if not fresh or abs(score) < cfg["min_score"] or conf < cfg["min_confidence"]:
        return {sym: price_now}
    last = acc["trades"][-1] if acc["trades"] else None
    if last and _now_ms() - last["closed_ms"] < 10 * 60_000:
        return {sym: price_now}  # short pause after each trade

    m5 = data[sym]["5m"] if data else market.klines(sym, cfg["interval"], 120)
    closes = [c["c"] for c in m5 if c["closed"]]
    if len(closes) < 60:
        return {sym: price_now}
    e50 = market.ema(closes, 50)[-1]
    side = "long" if score > 0 else "short"
    if (side == "long" and closes[-1] <= e50) or (side == "short" and closes[-1] >= e50):
        return {sym: price_now}  # price trend disagrees with the news -> wait
    if cfg.get("momentum"):  # the move must already be under way: price beyond a rising/falling EMA20
        e20 = market.ema(closes, 20)
        if side == "long" and not (closes[-1] > e20[-1] > e20[-3]):
            return {sym: price_now}
        if side == "short" and not (closes[-1] < e20[-1] < e20[-3]):
            return {sym: price_now}

    entry = price_now + half + price_now * slip if side == "long" else price_now - half - price_now * slip
    qty = cfg["notional_usd"] / entry
    margin = cfg["notional_usd"] / cfg["leverage"]
    if acc["balance"] < margin:
        return {sym: price_now}
    tp_d, sl_d = cfg["take_profit_usd"] / qty, cfg["stop_loss_usd"] / qty
    tp, sl = (entry + tp_d, entry - sl_d) if side == "long" else (entry - tp_d, entry + sl_d)
    pos = paper.open_position(acc, symbol=sym, side=side, price=entry, qty=qty, tp=tp, sl=sl, t_ms=_now_ms(),
                              entry_cost=0.0, max_hold_min=cfg["max_hold_minutes"], margin=margin,
                              note=f"news {score:+.2f}/{conf:.2f}")
    pos["friction"] = round(qty * (2 * half + 2 * price_now * slip), 4)  # spread + slippage (already in fills)
    if cfg.get("breakeven_after_usd"):
        be_d = cfg["breakeven_after_usd"] / qty
        cost_d = pos["friction"] / qty  # stop at a level that still covers the exit costs
        pos["be_trigger"] = entry + be_d if side == "long" else entry - be_d
        pos["be_level"] = entry + cost_d if side == "long" else entry - cost_d
    log.append(f"{tag}  {side.upper()} gold {cfg['notional_usd']} USD x{cfg['leverage']} @ {entry:.2f} "
               f"(TP {tp:.2f}, SL {sl:.2f}; news {score:+.2f})")
    return {sym: price_now}
