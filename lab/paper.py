"""Paper account: realistic fills (fees, spread, slippage, gaps), leverage, take-profit / stop-loss,
time stop and daily risk limits. Everything is simulated; no orders ever reach an exchange."""
import datetime as dt
import uuid

IST = dt.timezone(dt.timedelta(hours=3))


def today() -> str:
    return dt.datetime.now(IST).date().isoformat()


def new_account(start: float) -> dict:
    return {"balance": start, "start": start, "positions": [], "trades": [], "day": {"date": today(),
            "trades": 0, "pnl": 0.0, "stopped": False}, "last_check_ms": 0}


def roll_day(acc: dict) -> None:
    if acc["day"]["date"] != today():
        acc["day"] = {"date": today(), "trades": 0, "pnl": 0.0, "stopped": False}


def can_open(acc: dict, max_trades: int, loss_limit_usd: float) -> tuple[bool, str]:
    roll_day(acc)
    d = acc["day"]
    if d["stopped"]:
        return False, "daily loss limit reached"
    if d["pnl"] <= -abs(loss_limit_usd):
        d["stopped"] = True
        return False, "daily loss limit reached"
    if d["trades"] >= max_trades:
        return False, "max trades for today"
    return True, ""


def open_position(acc: dict, *, symbol: str, side: str, price: float, qty: float, tp: float, sl: float,
                  t_ms: int, entry_cost: float, max_hold_min: int, margin: float, note: str = "") -> dict:
    """price = fill price already including spread/slippage. entry_cost = fees paid at entry (USD)."""
    pos = {"id": uuid.uuid4().hex[:8], "symbol": symbol, "side": side, "qty": qty, "entry": price,
           "tp": tp, "sl": sl, "opened_ms": t_ms, "entry_cost": entry_cost, "max_hold_min": max_hold_min,
           "margin": margin, "note": note}
    acc["positions"].append(pos)
    acc["day"]["trades"] += 1
    return pos


def _close(acc: dict, pos: dict, exit_price: float, t_ms: int, reason: str, exit_cost: float) -> dict:
    sign = 1 if pos["side"] == "long" else -1
    gross = (exit_price - pos["entry"]) * pos["qty"] * sign
    pnl = gross - pos["entry_cost"] - exit_cost
    acc["balance"] += pnl
    acc["positions"].remove(pos)
    roll_day(acc)
    acc["day"]["pnl"] += pnl
    tr = {**pos, "exit": exit_price, "closed_ms": t_ms, "reason": reason, "gross": round(gross, 4),
          "costs": round(pos["entry_cost"] + exit_cost, 4), "pnl": round(pnl, 4)}
    acc["trades"].append(tr)
    acc["trades"] = acc["trades"][-3000:]
    return tr


def check_exits(acc: dict, symbol: str, candles_1m: list[dict], exit_fill, exit_fee) -> list[dict]:
    """Walks 1-minute candles since each position opened. If TP and SL are both inside one candle, the
    STOP is assumed first (conservative). A candle opening beyond the stop fills at the open (gap).
    exit_fill(side, level) -> realistic fill price; exit_fee(price, qty) -> USD fee."""
    closed = []
    for pos in [p for p in acc["positions"] if p["symbol"] == symbol]:
        long_ = pos["side"] == "long"
        for c in candles_1m:
            if c["t"] < pos["opened_ms"]:  # only candles that started after the entry
                continue
            level, reason = None, None
            if long_:
                if c["o"] <= pos["sl"]:
                    level, reason = c["o"], "stop (gap)"
                elif c["l"] <= pos["sl"]:
                    level, reason = pos["sl"], "stop"
                elif c["h"] >= pos["tp"]:
                    level, reason = pos["tp"], "take profit"
            else:
                if c["o"] >= pos["sl"]:
                    level, reason = c["o"], "stop (gap)"
                elif c["h"] >= pos["sl"]:
                    level, reason = pos["sl"], "stop"
                elif c["l"] <= pos["tp"]:
                    level, reason = pos["tp"], "take profit"
            # protect profit: once price has moved far enough our way, the stop moves to break-even
            # (checked after the stop test of the same candle, so it never helps a losing candle)
            if level is None and pos.get("be_trigger") is not None:
                hit = c["h"] >= pos["be_trigger"] if long_ else c["l"] <= pos["be_trigger"]
                if hit:
                    pos["sl"] = max(pos["sl"], pos["be_level"]) if long_ else min(pos["sl"], pos["be_level"])
                    pos["be_trigger"] = None
            if level is None and c["t"] - pos["opened_ms"] >= pos["max_hold_min"] * 60_000 and c["closed"]:
                level, reason = c["c"], "time limit"
            if level is not None:
                fill = exit_fill(pos["side"], level)
                closed.append(_close(acc, pos, fill, c["t"] + 60_000, reason, exit_fee(fill, pos["qty"])))
                break
    return closed


def equity(acc: dict, prices: dict) -> float:
    e = acc["balance"]
    for p in acc["positions"]:
        px = prices.get(p["symbol"], p["entry"])
        e += (px - p["entry"]) * p["qty"] * (1 if p["side"] == "long" else -1) - p["entry_cost"]
    return e


def stats(acc: dict, since_ms: int = 0) -> dict:
    tr = [t for t in acc["trades"] if t["closed_ms"] >= since_ms]
    wins = [t for t in tr if t["pnl"] > 0]
    return {"trades": len(tr), "wins": len(wins), "win_rate": round(100 * len(wins) / len(tr), 1) if tr else 0.0,
            "net": round(sum(t["pnl"] for t in tr), 2),
            "costs": round(sum(t["costs"] + t.get("friction", 0) for t in tr), 2),
            "avg_win": round(sum(t["pnl"] for t in wins) / len(wins), 2) if wins else 0.0,
            "avg_loss": round(sum(t["pnl"] for t in tr if t["pnl"] <= 0) / max(1, len(tr) - len(wins)), 2)}
