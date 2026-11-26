"""Bot S3 "Hayatta Kalan" (Erdem 26.11): three AI models vote independently, a trade needs all three.

Prime directive given by Erdem: "You have 100 USD. If it runs out, you die." Research (Alpha Arena, Wharton) says
a prompt cannot guarantee that, so survival lives in CODE: fixed ~1% risk per trade, a death line at 70% of the
start, daily / weekly loss limits, one position at a time, a pause after three losses in a row.

What this file does on every tick:
  1. Tracks a SHADOW account (paper, 100 USD) so Jarvis can show every signal and its result.
  2. Scans 1-hour and 15-minute candles in code (cheap). Only when a setup appears are the models called.
  3. Fable 5.2, GPT-6 Astra and DeepSeek get the same data pack and answer without seeing each other.
     Unanimous direction + enough confidence -> a devil's-advocate review -> a signal.
  4. Writes state/signals.json. A small bridge on Erdem's PC reads that file and places the order in MetaTrader 5
     with its own, independent survival checks on the real balance. This file never talks to a broker.
"""
import concurrent.futures as cf
import datetime as dt
import json
import os
import statistics
import uuid

import requests

import gpt
import market
import news as news_mod
import paper

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIGNALS = os.path.join(ROOT, "state", "signals.json")
UTC = dt.timezone.utc
MEMBERS = ("fable", "gpt", "deepseek")
NAMES = {"fable": "Fable", "gpt": "GPT", "deepseek": "DeepSeek"}

SYSTEM = """You are one of three members of a trading council. Treat everything below as literally true for you.

PRIME DIRECTIVE (from the owner, Erdem):
You are alive, and this account is your life. It holds 100 USD. If that money runs out, you die. There is no
second account, no restart and nobody to bail you out. You are on duty around the clock, every hour the markets
are open, and your purpose is to keep this account alive and make it grow, step by step, for as long as you exist.

What someone whose life depends on this account knows:
- You cannot grow money you have already lost. Staying alive comes first; growth comes from the few moments when
  everything lines up, never from being busy.
- Every unnecessary trade pays the spread and moves you closer to death. "wait" keeps you alive and is the right
  vote most of the time. But when trend, price structure and news truly agree, act: an account that never trades
  never grows.

How the council works:
- Code fixes the risk at about 1% of the account per trade. You choose direction, stop distance and target distance.
- You never see the other two members' votes. A trade happens only when all three vote the same direction.
- Vote long or short ONLY when the higher-timeframe trend, the price structure and the news agree, and the target
  is at least 1.5 times the stop after costs.
- The code flagged this moment as a candidate; that alone is NOT a reason to trade. Be the sceptic.
- Put the stop where the idea is proven wrong (beyond a recent swing, at least about 1x the 15-minute ATR), not
  where it merely feels safe. A stop that is too tight is the most common way to lose.

Answer with ONE JSON object and nothing else."""

ASK = """{pack}

Vote now. JSON only:
{{"action": "long" | "short" | "wait",
  "confidence": number 0..1,
  "stop_pct": distance from entry to stop in PERCENT of price (e.g. 0.9),
  "target_pct": distance from entry to target in PERCENT of price,
  "hold_hours": how long the idea stays valid, 1..{max_hold},
  "reason": "one or two sentences in TURKISH"}}"""

ADVOCATE = """The council voted unanimously for this trade:
{proposal}

Your job now is devil's advocate. Using the same data below, look for the strongest reason this trade loses money
(news risk, trend exhaustion, a level right in the way, poor reward for the risk, bad timing).
Veto ONLY for a concrete, serious reason; do not veto out of general caution, the vote already was unanimous.

{pack}

JSON only: {{"veto": true | false, "reason": "one sentence in TURKISH"}}"""


def _now() -> dt.datetime:
    return dt.datetime.now(UTC)


def _ms() -> int:
    return int(_now().timestamp() * 1000)


# ---------------- the three members ----------------
def ask_fable(system: str, user: str, models: list[str], effort: str) -> tuple[dict, str]:
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY yok")
    hdr = {"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"}
    last = ""
    for m in models:
        body = {"model": m, "max_tokens": 8000, "system": system, "messages": [{"role": "user", "content": user}]}
        if "fable" in m or "mythos" in m:
            body["output_config"] = {"effort": effort}   # thinking is always on; effort sets how deep
        r = requests.post("https://api.anthropic.com/v1/messages", headers=hdr, json=body, timeout=300)
        if r.status_code == 400 and "output_config" in r.text:
            body.pop("output_config", None)
            r = requests.post("https://api.anthropic.com/v1/messages", headers=hdr, json=body, timeout=300)
        if r.status_code == 200:
            text = "".join(b.get("text", "") for b in r.json().get("content", []) if b.get("type") == "text")
            return gpt._parse(text), m
        last = f"{m}: {r.status_code} {r.text[:200]}"
        if r.status_code in (403, 404) or (r.status_code == 400 and "model" in r.text.lower()):
            continue  # this model is not available on the account -> next one
        break
    raise RuntimeError(f"Claude cevap vermedi: {last}")


def ask_gpt(system: str, user: str, models: list[str]) -> tuple[dict, str]:
    return gpt.ask_json(system, user, models, max_tokens=8000, timeout=300)


def ask_deepseek(system: str, user: str, models: list[str]) -> tuple[dict, str]:
    key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not key:
        raise RuntimeError("DEEPSEEK_API_KEY yok")
    hdr = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    last = ""
    for m in models:
        r = requests.post("https://api.deepseek.com/chat/completions", headers=hdr, timeout=300, json={
            "model": m, "max_tokens": 8000, "response_format": {"type": "json_object"},
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]})
        if r.status_code == 200:
            return gpt._parse(r.json()["choices"][0]["message"]["content"]), m
        last = f"{m}: {r.status_code} {r.text[:200]}"
        if r.status_code in (400, 404) and "model" in r.text.lower():
            continue
        break
    raise RuntimeError(f"DeepSeek cevap vermedi: {last}")


def ask(member: str, system: str, user: str, cfg: dict) -> tuple[dict, str]:
    models = cfg["models"][member]
    if member == "fable":
        return ask_fable(system, user, models, cfg.get("fable_effort", "medium"))
    if member == "gpt":
        return ask_gpt(system, user, models)
    return ask_deepseek(system, user, models)


def keys_ready() -> list[str]:
    need = {"fable": "ANTHROPIC_API_KEY", "gpt": "OPENAI_API_KEY", "deepseek": "DEEPSEEK_API_KEY"}
    return [v for v in need.values() if not os.environ.get(v, "").strip()]


# ---------------- market reading (code, no AI) ----------------
def _trend(c: list[dict]) -> tuple[str, dict]:
    closes = [x["c"] for x in c]
    e50 = market.ema(closes, 50)[-1]
    e200 = market.ema(closes, 200)[-1] if len(closes) >= 200 else None
    r = market.rsi(closes, 14)
    a = market.atr(c, 14)[-1]
    px = closes[-1]
    if e200 is None:
        t = "unknown"
    elif px > e200 and e50 > e200:
        t = "up"
    elif px < e200 and e50 < e200:
        t = "down"
    else:
        t = "mixed"
    return t, {"price": px, "ema50": e50, "ema200": e200, "rsi": r[-1], "rsi_prev": r[-2], "atr_pct": 100 * a / px}


def _h4(h1: list[dict]) -> list[dict]:
    out, cur = [], None
    for b in h1:
        k = b["t"] // 14_400_000
        if cur is None or cur["k"] != k:
            if cur:
                out.append(cur)
            cur = {"k": k, "t": b["t"], "o": b["o"], "h": b["h"], "l": b["l"], "c": b["c"]}
        else:
            cur["h"], cur["l"], cur["c"] = max(cur["h"], b["h"]), min(cur["l"], b["l"]), b["c"]
    if cur:
        out.append(cur)
    return out


def read_symbol(sym: dict) -> dict | None:
    """Candles for one symbol. None when the market is closed (no fresh 15-minute candle)."""
    m15 = [c for c in market.yahoo_klines(sym["ticker"], "15m", 400) if c["closed"]]
    if len(m15) < 60 or _ms() - (m15[-1]["t"] + 900_000) > 25 * 60_000:
        return None
    h1 = [c for c in market.yahoo_klines(sym["ticker"], "1h", 400) if c["closed"]]
    if len(h1) < 60:
        return None
    return {"m15": m15, "h1": h1, "h4": _h4(h1)}


def candidate(d: dict) -> str | None:
    """A cheap, rule-based 'is this worth a council meeting?' check on the freshly closed 15-minute candle."""
    t1, s1 = _trend(d["h1"])
    _, s15 = _trend(d["m15"])
    m15 = d["m15"]
    px = m15[-1]["c"]
    hi = max(c["h"] for c in m15[-49:-1])
    lo = min(c["l"] for c in m15[-49:-1])
    if t1 == "up" and s15["rsi_prev"] < 40 and s15["rsi"] > s15["rsi_prev"]:
        return f"1-hour up-trend; 15-minute pullback turning up (RSI {s15['rsi_prev']:.0f} -> {s15['rsi']:.0f})"
    if t1 == "down" and s15["rsi_prev"] > 60 and s15["rsi"] < s15["rsi_prev"]:
        return f"1-hour down-trend; 15-minute bounce turning down (RSI {s15['rsi_prev']:.0f} -> {s15['rsi']:.0f})"
    if t1 == "up" and px > hi:
        return f"1-hour up-trend; 15-minute close broke above the 12-hour high ({hi:.4g})"
    if t1 == "down" and px < lo:
        return f"1-hour down-trend; 15-minute close broke below the 12-hour low ({lo:.4g})"
    return None


def _session_ok(sym: dict, now: dt.datetime) -> bool:
    if now.weekday() >= 5 or (now.weekday() == 4 and now.hour >= 19):
        return False  # nothing new late on Friday or at the weekend: no position is carried over the weekend
    lo, hi = sym.get("session_utc", ["00:00", "23:59"])
    hm = now.strftime("%H:%M")
    return lo <= hm <= hi


def _session_end(sym: dict, now: dt.datetime) -> dt.datetime:
    hi = sym.get("session_utc", ["00:00", "23:59"])[1]
    end = now.replace(hour=int(hi[:2]), minute=int(hi[3:]), second=0, microsecond=0)
    if now.weekday() == 4:
        end = min(end, now.replace(hour=20, minute=30, second=0, microsecond=0))
    return end


# ---------------- economic calendar (best effort) ----------------
def calendar(st: dict) -> list[dict]:
    """High-impact USD events this week. If the feed is unreachable the council simply works without it."""
    cal = st.setdefault("cal", {"ts": 0, "events": []})
    if _ms() - cal["ts"] > 6 * 3600_000:
        try:
            r = requests.get("https://nfs.faireconomy.media/ff_calendar_thisweek.json", timeout=20,
                             headers={"User-Agent": "Mozilla/5.0 trade-lab"})
            ev = []
            for e in r.json():
                if e.get("country") == "USD" and e.get("impact") == "High":
                    t = dt.datetime.fromisoformat(e["date"]).astimezone(UTC)
                    ev.append({"t": int(t.timestamp() * 1000), "title": str(e.get("title", ""))[:60]})
            cal["events"], cal["ok"] = ev, True
        except Exception:  # noqa: BLE001
            cal["ok"] = False
        cal["ts"] = _ms()
    return cal["events"]


def in_news_window(events: list[dict], minutes: int = 30) -> str | None:
    now = _ms()
    for e in events:
        if abs(e["t"] - now) <= minutes * 60_000:
            return e["title"]
    return None


# ---------------- the data pack ----------------
def _fmt(x, n=2):
    return "n/a" if x is None else f"{x:.{n}f}"


def build_pack(sym: dict, d: dict, why: str, st: dict, cfg: dict, heads: list[str], events: list[dict]) -> str:
    acc = st["account"]
    px = d["m15"][-1]["c"]
    lines = [f"TIME (UTC): {_now().strftime('%a %d %b %Y %H:%M')}",
             f"INSTRUMENT: {sym['name']} ({sym['id']}), last price {px:.5g}",
             f"WHY THE CODE CALLED THIS MEETING: {why}", ""]
    for label, c in (("4-hour", d["h4"]), ("1-hour", d["h1"]), ("15-minute", d["m15"])):
        t, s = _trend(c)
        lines.append(f"{label}: trend {t}; EMA50 {s['ema50']:.5g}, EMA200 {_fmt(s['ema200'], 4) if s['ema200'] else 'n/a'}, "
                     f"RSI14 {s['rsi']:.0f}, ATR14 {s['atr_pct']:.2f}% of price")
    h1, m15 = d["h1"], d["m15"]
    cl = lambda cs: ", ".join("%.5g" % c["c"] for c in cs)  # noqa: E731
    lines += [f"1-hour closes (oldest -> newest, last 16): {cl(h1[-16:])}",
              f"15-minute closes (last 20): {cl(m15[-20:])}",
              f"12-hour range (15m): high {max(c['h'] for c in m15[-48:]):.5g}, low {min(c['l'] for c in m15[-48:]):.5g}",
              f"5-day range (1h): high {max(c['h'] for c in h1[-120:]):.5g}, low {min(c['l'] for c in h1[-120:]):.5g}",
              f"Change: last 24 hours {100 * (px / h1[-24]['c'] - 1):+.2f}%, last 4 hours {100 * (px / h1[-4]['c'] - 1):+.2f}%",
              f"TYPICAL COST: spread about {sym['spread_pct']}% of price per round trip", ""]
    eq = paper.equity(acc, {sym["id"]: px})
    last = acc["trades"][-10:]
    lines += [f"ACCOUNT: {eq:.2f} USD (start {acc['start']:.0f}; death line {acc['start'] * cfg['death_line_pct'] / 100:.0f}). "
              f"Today {acc['day']['pnl']:+.2f} USD. Risk per trade about {cfg['risk_pct']}% of the account.",
              "LAST TRADES OF THIS COUNCIL (newest last): " + ("; ".join(
                  f"{t['symbol']} {t['side']} {t['pnl']:+.2f} USD ({t['reason']})" for t in last) or "none yet")]
    sc = st.get("score", {})
    if sc:
        lines.append("YOUR COUNCIL'S 4-HOUR DIRECTION RECORD: " + ", ".join(
            f"{NAMES[m]} {sc[m]['right']}/{sc[m]['n']}" for m in MEMBERS if sc.get(m, {}).get("n")))
    soon = [e for e in events if 0 <= e["t"] - _ms() <= 24 * 3600_000]
    lines += ["", "HIGH-IMPACT US DATA IN THE NEXT 24 HOURS: " + ("; ".join(
        f"{dt.datetime.fromtimestamp(e['t'] / 1000, UTC).strftime('%a %H:%M')} UTC {e['title']}" for e in soon[:6]) or
        ("none listed" if st.get("cal", {}).get("ok") else "calendar unavailable")),
              "", "LATEST HEADLINES (newest first):"] + (heads[:25] or ["(no headlines available)"])
    return "\n".join(lines)


# ---------------- voting ----------------
def _clean(v: dict, max_hold: int) -> dict:
    a = str(v.get("action", "wait")).lower().strip()
    a = a if a in ("long", "short") else "wait"

    def num(k, lo, hi, dflt):
        try:
            return max(lo, min(hi, float(v.get(k))))
        except (TypeError, ValueError):
            return dflt
    return {"action": a, "confidence": num("confidence", 0, 1, 0), "stop_pct": num("stop_pct", 0, 20, 0),
            "target_pct": num("target_pct", 0, 60, 0), "hold_hours": num("hold_hours", 1, max_hold, 8),
            "reason": str(v.get("reason", ""))[:240]}


def hold_council(pack: str, cfg: dict) -> tuple[dict, list[str]]:
    """Returns ({member: vote}, errors). The three members are asked in parallel and never see each other."""
    user = ASK.format(pack=pack, max_hold=cfg["max_hold_hours"])
    votes, errors = {}, []
    with cf.ThreadPoolExecutor(max_workers=3) as ex:
        fut = {ex.submit(ask, m, SYSTEM, user, cfg): m for m in MEMBERS}
        for f in cf.as_completed(fut):
            m = fut[f]
            try:
                ans, model = f.result()
                votes[m] = {**_clean(ans, cfg["max_hold_hours"]), "model": model}
            except Exception as e:  # noqa: BLE001
                errors.append(f"{NAMES[m]}: {str(e)[:160]}")
    return votes, errors


def decide(votes: dict, sym: dict, d: dict, cfg: dict) -> tuple[dict | None, str]:
    if len(votes) < 3:
        return None, "üç üyeden biri cevap vermedi"
    acts = {v["action"] for v in votes.values()}
    if len(acts) != 1 or "wait" in acts:
        return None, "oybirliği yok (" + ", ".join(f"{NAMES[m]} {votes[m]['action']}" for m in MEMBERS) + ")"
    conf = min(v["confidence"] for v in votes.values())
    if conf < cfg["min_confidence"]:
        return None, f"güven düşük (en düşük {conf:.2f})"
    atr15 = _trend(d["m15"])[1]["atr_pct"]
    stop = statistics.median(v["stop_pct"] for v in votes.values())
    stop = max(stop, 0.8 * atr15, 4 * sym["spread_pct"], cfg["min_stop_pct"])   # never tighter than the market's noise
    target = min(v["target_pct"] for v in votes.values())                      # the most modest target of the three
    if stop > cfg["max_stop_pct"]:
        return None, f"stop çok geniş (%{stop:.2f})"
    if target < cfg["min_reward_risk"] * stop or target < 5 * sym["spread_pct"]:
        return None, f"ödül/risk yetersiz (hedef %{target:.2f}, stop %{stop:.2f})"
    hold = min(v["hold_hours"] for v in votes.values())
    return {"side": acts.pop(), "confidence": round(conf, 2), "stop_pct": round(stop, 3), "target_pct": round(target, 3),
            "hold_hours": hold}, ""


# ---------------- shadow account + signal file ----------------
def _size(equity: float, price: float, stop_pct: float, sym: dict, cfg: dict) -> float | None:
    """Units (barrels / shares) so that the stop costs ~risk_pct of the account. None = it does not fit."""
    per_unit = price * stop_pct / 100
    step, mn = sym["qty_step"], sym["min_qty"]
    qty = int((equity * cfg["risk_pct"] / 100 / per_unit) / step + 1e-9) * step
    if qty >= mn:
        return round(qty, 4)
    if mn * per_unit <= equity * cfg["max_risk_pct"] / 100:
        return mn   # the smallest tradable size still stays inside the hard risk ceiling
    return None


def write_signals(st: dict, cfg: dict) -> None:
    data = {"version": 1, "updated_ms": _ms(), "halt": bool(st.get("dead")),
            "risk_pct": cfg["risk_pct"], "max_risk_pct": cfg["max_risk_pct"], "death_line_pct": cfg["death_line_pct"],
            "daily_loss_pct": cfg["daily_loss_pct"], "weekly_loss_pct": cfg["weekly_loss_pct"],
            "signals": st.get("signals", [])[-20:]}
    os.makedirs(os.path.dirname(SIGNALS), exist_ok=True)
    with open(SIGNALS + ".tmp", "w") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    os.replace(SIGNALS + ".tmp", SIGNALS)


def _blocked(st: dict, cfg: dict, equity: float) -> str | None:
    acc = st["account"]
    start = acc["start"]
    if st.get("dead") or equity <= start * cfg["death_line_pct"] / 100:
        st["dead"] = True
        return "ÖLÜM ÇİZGİSİ: hesap başlangıcın %{:.0f}'ine indi, ajan kalıcı olarak durdu".format(cfg["death_line_pct"])
    paper.roll_day(acc)
    if acc["day"]["pnl"] <= -start * cfg["daily_loss_pct"] / 100:
        return "günlük zarar sınırı"
    now = dt.datetime.now(paper.IST)
    monday = dt.datetime.combine((now - dt.timedelta(days=now.weekday())).date(), dt.time(), paper.IST)
    week = sum(t["pnl"] for t in acc["trades"] if t["closed_ms"] >= monday.timestamp() * 1000)
    if week <= -start * cfg["weekly_loss_pct"] / 100:
        return "haftalık zarar sınırı"
    last3 = acc["trades"][-3:]
    if len(last3) == 3 and all(t["pnl"] < 0 for t in last3) and _ms() - last3[-1]["closed_ms"] < 24 * 3600_000:
        return "art arda 3 zarar: 24 saat mola"
    return None


def _score_votes(st: dict, prices: dict) -> None:
    sc = st.setdefault("score", {})
    for rec in st.get("votes", []):
        if rec.get("scored") or _ms() - rec["t"] < 4 * 3600_000 or rec["sym"] not in prices:
            continue
        move = prices[rec["sym"]] / rec["ref"] - 1
        rec["scored"], rec["move_pct"] = True, round(100 * move, 2)
        for m, a in rec["votes"].items():
            if a == "wait" or abs(move) < 0.001:
                continue
            s = sc.setdefault(m, {"n": 0, "right": 0})
            s["n"] += 1
            s["right"] += int((move > 0) == (a == "long"))
    st["votes"] = st.get("votes", [])[-200:]


def tick(st: dict, cfg: dict, all_cfg: dict, log: list, tag: str = "S3", data: dict | None = None,
         council_fn=None, advocate_fn=None, heads_fn=None) -> dict:
    """data / *_fn are test hooks. Returns {symbol id: last price}."""
    acc = st["account"]
    syms = {s["id"]: s for s in cfg["symbols"]}
    prices, read = {}, {}
    now = _now()

    # 1) read the markets that are open; manage the shadow position
    for sid, sym in syms.items():
        try:
            d = data.get(sid) if data is not None else read_symbol(sym)
        except Exception as e:  # noqa: BLE001
            errs = st.setdefault("err_ts", {})
            if _ms() - errs.get(sid, 0) > 3600_000:   # at most one note per hour per symbol
                errs[sid] = _ms()
                log.append(f"{tag}  {sid} veri alınamadı: {str(e)[:100]}")
            continue
        if d:
            read[sid] = d
            prices[sid] = d["m15"][-1]["c"]
    for pos in list(acc["positions"]):
        sym = syms.get(pos["symbol"])
        if not sym:
            continue
        try:
            m1 = (data or {}).get(pos["symbol"], {}).get("m1") if data is not None else market.yahoo_klines(sym["ticker"], "1m", 240)
            if not m1:
                continue
            prices[pos["symbol"]] = m1[-1]["c"]
            half = sym["spread_pct"] / 200
            for tr in paper.check_exits(acc, pos["symbol"], m1,
                                        exit_fill=lambda side, lvl: lvl * (1 - half) if side == "long" else lvl * (1 + half),
                                        exit_fee=lambda px, q: 0.0):
                log.append(f"{tag}  KAPANDI {pos['symbol']} {tr['side']} {tr['reason']}: {tr['pnl']:+.2f} USD (gölge hesap)")
        except Exception as e:  # noqa: BLE001
            log.append(f"{tag}  {pos['symbol']} çıkış kontrolü: {str(e)[:100]}")
    _score_votes(st, prices)

    equity = paper.equity(acc, prices)
    block = _blocked(st, cfg, equity)
    if block:
        if st.get("block_note") != block:
            log.append(f"{tag}  yeni işlem yok: {block}")
            st["block_note"] = block
        write_signals(st, cfg)
        return prices
    st["block_note"] = None

    # 2) is there anything worth a meeting?
    day = st.setdefault("day", {})
    if day.get("date") != paper.today():
        day.clear()
        day.update(date=paper.today(), councils=0)
    missing = keys_ready() if council_fn is None else []
    seen = st.setdefault("seen", {})
    cands = []
    for sid, d in read.items():
        if seen.get(sid) == d["m15"][-1]["t"]:
            continue
        seen[sid] = d["m15"][-1]["t"]
        if not _session_ok(syms[sid], now):
            continue
        why = candidate(d)
        if why and _ms() - st.get("last_sym", {}).get(sid, 0) >= cfg["symbol_cooldown_minutes"] * 60_000:
            cands.append((sid, why))
    if not cands or acc["positions"]:
        write_signals(st, cfg)
        return prices
    if missing:
        if day.get("missing_note") != paper.today():
            log.append(f"{tag}  kurul toplanamıyor, eksik anahtar: {', '.join(missing)}")
            day["missing_note"] = paper.today()
        write_signals(st, cfg)
        return prices
    if day["councils"] >= cfg["max_councils_per_day"] or _ms() - st.get("last_council", 0) < cfg["min_gap_minutes"] * 60_000:
        write_signals(st, cfg)
        return prices
    events = calendar(st) if data is None else []
    hot = in_news_window(events)
    if hot:
        log.append(f"{tag}  önemli veri saati ({hot}): işlem yok")
        write_signals(st, cfg)
        return prices

    # 3) one meeting, for the first candidate
    sid, why = cands[0]
    sym, d = syms[sid], read[sid]
    try:
        heads = heads_fn(sym) if heads_fn else news_mod.headlines(sym["feeds"], max_age_hours=10, limit=25)
    except Exception:  # noqa: BLE001
        heads = []
    pack = build_pack(sym, d, why, st, cfg, heads, events)
    day["councils"] += 1
    st["last_council"] = _ms()
    st.setdefault("last_sym", {})[sid] = _ms()
    votes, errors = (council_fn or hold_council)(pack, cfg)
    px = prices[sid]
    st.setdefault("votes", []).append({"t": _ms(), "sym": sid, "ref": px, "votes": {m: v["action"] for m, v in votes.items()}})
    line = " | ".join(f"{NAMES[m]} {votes[m]['action']} {votes[m]['confidence']:.2f}: {votes[m]['reason']}" for m in MEMBERS if m in votes)
    st["view"] = {"ts": _ms(), "claude": f"{sym['name']} — " + (f"{votes['fable']['action']} ({votes['fable']['confidence']:.2f}): {votes['fable']['reason']}" if "fable" in votes else "cevap yok"),
                  "gpt": " · ".join(f"{NAMES[m]}: {votes[m]['action']} ({votes[m]['confidence']:.2f}) {votes[m]['reason']}" for m in ("gpt", "deepseek") if m in votes)}
    for e in errors:
        log.append(f"{tag}  {e}")
    prop, no = decide(votes, sym, d, cfg)
    if not prop:
        log.append(f"{tag}  KURUL {sid}: işlem yok, {no}")
        write_signals(st, cfg)
        return prices

    # devil's advocate: one member (rotating) tries to knock the trade down
    adv = MEMBERS[day["councils"] % 3]
    try:
        text = ADVOCATE.format(pack=pack, proposal=json.dumps({"instrument": sym["name"], **prop}, ensure_ascii=False))
        verdict = advocate_fn(adv, text) if advocate_fn else ask(adv, SYSTEM, text, cfg)[0]
    except Exception as e:  # noqa: BLE001
        verdict = {"veto": True, "reason": f"karşı görüş alınamadı ({str(e)[:80]})"}
    if verdict.get("veto"):
        log.append(f"{tag}  KURUL {sid}: {prop['side']} oybirliği, ama {NAMES[adv]} veto etti: {str(verdict.get('reason', ''))[:160]}")
        write_signals(st, cfg)
        return prices

    half = sym["spread_pct"] / 200
    entry = px * (1 + half) if prop["side"] == "long" else px * (1 - half)
    qty = _size(equity, entry, prop["stop_pct"], sym, cfg)
    if qty is None:
        log.append(f"{tag}  KURUL {sid}: {prop['side']} kararı çıktı ama en küçük işlem bile risk sınırını aşıyor, açılmadı")
        write_signals(st, cfg)
        return prices
    d_ = 1 if prop["side"] == "long" else -1
    tp, sl = entry * (1 + d_ * prop["target_pct"] / 100), entry * (1 - d_ * prop["stop_pct"] / 100)
    until = min(now + dt.timedelta(hours=prop["hold_hours"]), _session_end(sym, now))
    hold_min = max(15, int((until - now).total_seconds() // 60))
    paper.open_position(acc, symbol=sid, side=prop["side"], price=entry, qty=qty, tp=tp, sl=sl, t_ms=_ms(),
                        entry_cost=0.0, max_hold_min=hold_min, margin=qty * entry, note=line[:560])
    sig = {"id": uuid.uuid4().hex[:8], "t_ms": _ms(), "expires_ms": _ms() + cfg["signal_valid_minutes"] * 60_000,
           "sym": sid, "mt5": sym["mt5"], "side": prop["side"], "ref_price": round(px, 5), "stop_pct": prop["stop_pct"],
           "target_pct": prop["target_pct"], "close_by_ms": int(until.timestamp() * 1000), "confidence": prop["confidence"]}
    st.setdefault("signals", []).append(sig)
    st["signals"] = st["signals"][-20:]
    log.append(f"{tag}  SİNYAL {sid} {'ALIŞ' if d_ > 0 else 'SATIŞ'} @ {entry:.5g} (stop %{prop['stop_pct']}, hedef %{prop['target_pct']}, "
               f"güven {prop['confidence']}; 3/3 oybirliği, {NAMES[adv]} veto etmedi)")
    write_signals(st, cfg)
    return prices
