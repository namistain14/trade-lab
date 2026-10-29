"""Bot B6: US stocks on Alpaca's PAPER account (fake money, real market and real order flow).

Every tick while the US market is open:
  1. sync the Alpaca paper account (equity, positions) and notice positions that closed (take profit / stop),
  2. at most every `decide_minutes`, Claude and GPT each read prices + fresh news for the watch list
     independently; a position opens only when BOTH pick the same direction with enough confidence,
  3. every order is a bracket order (take profit + stop loss sit at Alpaca),
  4. near the close everything is flattened (no overnight risk).
Keys come from GitHub Secrets (ALPACA_KEY_ID / ALPACA_SECRET). The base URL is pinned to the PAPER endpoint.
"""
import datetime as dt
import json
import math
import os

import requests

STYLE = 'Only trade when price action AND news give a clear edge; "none" is the right answer most of the time.'
PAPER = "https://paper-api.alpaca.markets"   # paper only: real-money endpoint is never used
DATA = "https://data.alpaca.markets"

PROMPT = """You are a disciplined US equities intraday trader. It is {now} New York time.
For each symbol decide whether to open a position NOW for the next 1-3 hours, or do nothing.
Leverage is 1:{lev}. Each trade uses a take profit of +{tp}% and a stop loss of -{sl}% (bracket order).
{style}
Avoid chasing big moves that already happened; weigh fresh, company-specific news most.

Market data (price, change vs yesterday's close, change over the last hour, last 12 five-minute closes):
{prices}

Recent headlines (newest first):
{news}

Already open (do not decide these): {open}

Answer with JSON only:
{{"decisions": [{{"symbol": "...", "action": "long" | "short" | "none", "confidence": 0..1,
                 "reason": "one short sentence in TURKISH"}}],
  "market_view": "one sentence in TURKISH"}}"""


class Alpaca:
    def __init__(self, key: str, secret: str):
        self.h = {"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret}

    def _req(self, method, base, path, **kw):
        r = requests.request(method, base + path, headers=self.h, timeout=30, **kw)
        if r.status_code >= 400:
            raise RuntimeError(f"Alpaca {method} {path}: {r.status_code} {r.text[:200]}")
        return r.json() if r.text else {}

    def get(self, path, **params):
        return self._req("GET", PAPER, path, params=params)

    def data(self, path, **params):
        return self._req("GET", DATA, path, params=params)

    def post(self, path, body):
        return self._req("POST", PAPER, path, json=body)

    def delete(self, path):
        return self._req("DELETE", PAPER, path)


def _now_ms() -> int:
    return int(dt.datetime.now(dt.timezone.utc).timestamp() * 1000)


def _iso(ms_ago_min: int) -> str:
    return (dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=ms_ago_min)).strftime("%Y-%m-%dT%H:%M:%SZ")


def market_snapshot(api: Alpaca, symbols: list[str]) -> dict:
    snaps = api.data("/v2/stocks/snapshots", symbols=",".join(symbols), feed="iex")
    bars = api.data("/v2/stocks/bars", symbols=",".join(symbols), timeframe="5Min", start=_iso(240),
                    limit=5000, feed="iex").get("bars", {})
    out = {}
    for s in symbols:
        sn = snaps.get(s) or {}
        px = (sn.get("latestTrade") or {}).get("p") or (sn.get("minuteBar") or {}).get("c")
        prev = (sn.get("prevDailyBar") or {}).get("c")
        closes = [b["c"] for b in bars.get(s, [])][-12:]
        if not px:
            continue
        hour = closes[-12] if len(closes) >= 12 else (closes[0] if closes else px)
        out[s] = {"price": round(px, 2), "day_pct": round(100 * (px / prev - 1), 2) if prev else None,
                  "hour_pct": round(100 * (px / hour - 1), 2), "last_closes": [round(c, 2) for c in closes]}
    return out


def headlines(api: Alpaca, symbols: list[str], hours: int = 6) -> list[str]:
    try:
        news = api.data("/v1beta1/news", symbols=",".join(symbols), start=_iso(hours * 60), limit=40,
                        sort="desc").get("news", [])
    except RuntimeError:
        return []
    return [f"[{n['created_at'][11:16]} UTC] ({','.join(n.get('symbols', [])[:4])}) {n['headline']}" for n in news]


def ask_claude(key: str, models: list[str], prompt: str) -> tuple[dict, str]:
    """Strongest model first; falls back to the next one if a model is not available on this account."""
    import anthropic
    client, last = anthropic.Anthropic(api_key=key), None
    for m in models:
        try:
            msg = client.messages.create(model=m, max_tokens=2000, messages=[{"role": "user", "content": prompt}])
        except (anthropic.NotFoundError, anthropic.PermissionDeniedError, anthropic.BadRequestError) as e:
            last = e
            continue
        text = "".join(getattr(b, "text", "") for b in msg.content)
        return json.loads(text[text.find("{"): text.rfind("}") + 1]), m
    raise RuntimeError(f"no Claude model available: {last}")


def _by_symbol(ans: dict) -> dict:
    return {d.get("symbol", "").upper(): d for d in ans.get("decisions", []) if d.get("symbol")}


def _record_close(acc: dict, tr: dict, exit_px: float, reason: str, log: list, tag: str) -> None:
    d = 1 if tr["side"] == "long" else -1
    pnl = (exit_px - tr["entry"]) * tr["qty"] * d
    acc["trades"].append({**{k: tr[k] for k in ("id", "symbol", "side", "qty", "entry", "tp", "sl", "opened_ms")},
                          "note": tr.get("note", ""), "exit": exit_px, "closed_ms": _now_ms(), "reason": reason,
                          "gross": round(pnl, 2), "costs": 0.0, "pnl": round(pnl, 2), "entry_cost": 0.0})
    acc["trades"] = acc["trades"][-500:]
    log.append(f"{tag}  CLOSE {tr['side']} {tr['symbol']} {reason}: {pnl:+.2f} USD")


def _exit_of(api: Alpaca, order_id: str) -> tuple[float | None, str]:
    """(exit price, reason); reason "pending" = entry not filled yet, "never" = entry never filled."""
    try:
        o = api.get(f"/v2/orders/{order_id}", nested="true")
    except RuntimeError:
        return None, "kapandı"
    if o.get("status") in ("new", "accepted", "pending_new", "partially_filled", "accepted_for_bidding"):
        return None, "pending"
    if o.get("status") in ("canceled", "expired", "rejected") and not float(o.get("filled_qty") or 0):
        return None, "never"
    for leg in o.get("legs") or []:
        if leg.get("status") == "filled" and leg.get("filled_avg_price"):
            kind = "take profit" if leg.get("type") == "limit" else "stop"
            return float(leg["filled_avg_price"]), kind
    return None, "kapandı"


def stocks_tick(st_bot: dict, bc: dict, news_cfg: dict, log: list, claude_key: str | None, tag: str = "B6") -> dict:
    key, secret = os.environ.get("ALPACA_KEY_ID", "").strip(), os.environ.get("ALPACA_SECRET", "").strip()
    if not key or not secret:
        missing = [n for n, v in (("ALPACA_KEY_ID", key), ("ALPACA_SECRET", secret)) if not v]
        st_bot["error"] = "GitHub Secrets'ta yok: " + ", ".join(missing)
        print(f"::warning::B6: missing secrets {missing}")
        return {}
    st_bot.pop("error", None)
    api = Alpaca(key, secret)
    acc = st_bot["account"]
    track = st_bot.setdefault("open", {})
    symbols = [s.upper() for s in bc["symbols"]]

    account = api.get("/v2/account")
    equity, last_eq = float(account["equity"]), float(account["last_equity"])
    if not st_bot.get("started"):
        acc["start"] = round(last_eq or equity, 2)
        st_bot["started"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    pos = {p["symbol"]: p for p in api.get("/v2/positions")}

    # positions that disappeared since the last tick -> record the result
    for sym in [s for s in track if s not in pos]:
        px, why = _exit_of(api, track[sym]["order_id"])
        if why == "pending":
            continue
        tr = track.pop(sym)
        if why == "never":
            log.append(f"{tag}  {sym} emri dolmadı, iptal")
            continue
        _record_close(acc, tr, px if px else tr["entry"], why, log, tag)

    prices, mapped = {}, []
    for sym, p in pos.items():
        cur, entry, qty = float(p["current_price"]), float(p["avg_entry_price"]), abs(float(p["qty"]))
        side = "long" if p["side"] == "long" else "short"
        t = track.get(sym) or {}
        prices[sym] = cur
        mapped.append({"id": t.get("order_id", sym), "symbol": sym, "side": side, "qty": qty, "entry": entry,
                       "tp": t.get("tp", entry), "sl": t.get("sl", entry), "opened_ms": t.get("opened_ms", _now_ms()),
                       "entry_cost": 0.0, "friction": 0.0, "note": t.get("note", ""), "cur": cur})
    acc["positions"] = mapped
    unreal = sum((m["cur"] - m["entry"]) * m["qty"] * (1 if m["side"] == "long" else -1) for m in mapped)
    acc["balance"] = equity - unreal     # so that balance + open P/L == Alpaca equity
    acc["equity"] = equity
    acc["day"] = {"date": dt.date.today().isoformat(), "pnl": round(equity - last_eq, 2),
                  "trades": len([t for t in acc["trades"] if t["closed_ms"] > _now_ms() - 86400000]), "stopped": False}

    clock = api.get("/v2/clock")
    st_bot["market_open"] = bool(clock.get("is_open"))
    if not clock.get("is_open"):
        # asleep until 1 hour before the bell; then one pre-market view (no orders), trading starts at the open
        nxt = dt.datetime.fromisoformat(clock["next_open"].replace("Z", "+00:00"))
        mins = (nxt - dt.datetime.now(nxt.tzinfo)).total_seconds() / 60
        st_bot["next_open"] = clock["next_open"]
        st_bot["state"] = "hazırlık (seans öncesi)" if mins <= 60 else "uyku (piyasa kapalı)"
        day = nxt.date().isoformat()
        if mins <= bc.get("warmup_minutes", 60) and st_bot.get("premarket_day") != day and claude_key:
            st_bot["premarket_day"] = day
            try:
                market = market_snapshot(api, symbols)
                news = headlines(api, symbols)
                prompt = PROMPT.format(now="pre-market, the bell rings in about an hour", lev=bc["leverage"], style=bc.get("style", STYLE),
                                       tp=bc["take_profit_pct"], sl=bc["stop_loss_pct"],
                                       prices=json.dumps(market, ensure_ascii=False), news="\n".join(news) or "(none)",
                                       open="none")
                c_ans, c_model = ask_claude(claude_key, bc["claude_models"], prompt)
                st_bot["view"] = {"ts": _now_ms(), "claude": c_ans.get("market_view", ""), "claude_model": c_model,
                                  "gpt": "", "premarket": True}
                log.append(f"{tag}  seans öncesi görüş: {c_ans.get('market_view', '-')}"[:400])
            except Exception as e:  # noqa: BLE001
                log.append(f"{tag}  seans öncesi görüş alınamadı: {str(e)[:120]}")
        return prices
    st_bot["state"] = "aktif (seans açık)"
    close_at = dt.datetime.fromisoformat(clock["next_close"].replace("Z", "+00:00"))
    to_close = (close_at - dt.datetime.now(close_at.tzinfo)).total_seconds() / 60

    # flatten before the bell
    if to_close <= bc.get("flatten_minutes_before_close", 15):
        if pos:
            api.delete("/v2/orders")              # cancel the bracket legs first
            for sym in list(pos):
                tr = track.pop(sym, None)
                api.delete(f"/v2/positions/{sym}")
                if tr:
                    _record_close(acc, tr, prices.get(sym, tr["entry"]), "seans sonu", log, tag)
            log.append(f"{tag}  seans kapanışı: tüm pozisyonlar kapatıldı")
        return prices

    # stop for the day after a large loss
    if equity - last_eq <= -bc.get("daily_loss_limit_pct", 0.02) * last_eq:
        acc["day"]["stopped"] = True
        return prices

    now = _now_ms()
    if now - st_bot.get("last_decision_ms", 0) < bc.get("decide_minutes", 15) * 60000:
        return prices
    if len(pos) >= bc.get("max_open", 5) or to_close < bc.get("no_new_minutes_before_close", 45):
        return prices
    st_bot["last_decision_ms"] = now

    market = market_snapshot(api, symbols)
    news = headlines(api, symbols)
    ny = dt.datetime.now(dt.timezone(dt.timedelta(hours=-4))).strftime("%H:%M")
    prompt = PROMPT.format(now=ny, lev=bc["leverage"], style=bc.get("style", STYLE), tp=bc["take_profit_pct"], sl=bc["stop_loss_pct"],
                           prices=json.dumps(market, ensure_ascii=False), news="\n".join(news) or "(none)",
                           open=", ".join(pos) or "none")
    c_ans, g_ans, g_model, c_model = {}, {}, None, None
    if claude_key:
        try:
            c_ans, c_model = ask_claude(claude_key, bc["claude_models"], prompt)
        except Exception as e:  # noqa: BLE001
            log.append(f"{tag}  Claude cevap vermedi: {str(e)[:120]}")
    try:
        import gpt
        g_ans, g_model = gpt.ask_json("You are a disciplined US equities intraday trader. Answer with one JSON object.",
                                      prompt, bc["gpt_models"], max_tokens=2000, timeout=120)
    except Exception as e:  # noqa: BLE001
        log.append(f"{tag}  GPT cevap vermedi: {str(e)[:120]}")
    c, g = _by_symbol(c_ans), _by_symbol(g_ans)
    st_bot["view"] = {"ts": now, "claude": c_ans.get("market_view", ""), "gpt": g_ans.get("market_view", ""),
                      "gpt_model": g_model, "claude_model": c_model,
                      "picks": {s: {"claude": [c.get(s, {}).get("action"), c.get(s, {}).get("confidence")],
                                    "gpt": [g.get(s, {}).get("action"), g.get(s, {}).get("confidence")]}
                                for s in symbols}}
    log.append(f"{tag}  karar turu: Claude «{c_ans.get('market_view', '-')}» / GPT «{g_ans.get('market_view', '-')}»"[:400])

    min_conf = bc.get("min_confidence", 0.55)
    slots = bc.get("max_open", 5) - len(pos)
    lev = bc["leverage"]
    for sym in symbols:
        if slots <= 0 or sym in pos or sym not in market:
            continue
        a, b = c.get(sym, {}), g.get(sym, {})
        act = a.get("action")
        if act not in ("long", "short") or b.get("action") != act:
            continue
        conf = min(float(a.get("confidence", 0)), float(b.get("confidence", 0)))
        if conf < min_conf:
            continue
        px = market[sym]["price"]
        notional = equity * bc.get("position_pct", 0.2) * lev
        qty = math.floor(notional / px)
        if qty < 1:
            continue
        d = 1 if act == "long" else -1
        tp = round(px * (1 + d * bc["take_profit_pct"] / 100), 2)
        sl = round(px * (1 - d * bc["stop_loss_pct"] / 100), 2)
        try:
            o = api.post("/v2/orders", {"symbol": sym, "qty": str(qty), "side": "buy" if d > 0 else "sell",
                                        "type": "market", "time_in_force": "day", "order_class": "bracket",
                                        "take_profit": {"limit_price": str(tp)}, "stop_loss": {"stop_price": str(sl)}})
        except RuntimeError as e:
            log.append(f"{tag}  {sym} emir reddedildi: {str(e)[:150]}")
            continue
        note = f"Claude {a.get('confidence')}: {a.get('reason', '')} | GPT {b.get('confidence')}: {b.get('reason', '')}"
        track[sym] = {"order_id": o["id"], "symbol": sym, "side": act, "qty": qty, "entry": px, "tp": tp, "sl": sl,
                      "opened_ms": now, "note": note[:300]}
        slots -= 1
        log.append(f"{tag}  {'ALIŞ' if d > 0 else 'AÇIĞA SATIŞ'} {sym} {qty} adet ≈ {qty * px:,.0f} $ "
                   f"(1:{lev}) @ {px} (TP {tp}, SL {sl}; ikisi de hemfikir, güven {conf:.2f})")
    return prices
