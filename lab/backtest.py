"""Bot A research (Erdem 02.11): why does it lose, and which crypto rule set would have made money?

Downloads ~120 days of Binance 5-minute candles for A's six coins and replays several rule sets with the SAME
cost model as the paper bot (0.05% fee + 0.03% slippage per side, so ~0.16% of the position per round trip).
Every entry happens at the NEXT candle's open; if a candle touches both target and stop, the stop counts
(conservative, like paper.py). The first 60% of the days is "learning", the last 40% is the honest test
("out-of-sample"): a rule only counts as good if it also wins there.

Run: python lab/backtest.py   -> reports/backtest_A.md (+ .json)
"""
import datetime as dt
import json
import math
import os
import random
import time

import requests

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT", "DOGEUSDT"]
DAYS = int(os.environ.get("BT_DAYS", "120"))
NOTIONAL = 6000.0          # what A uses today: 40% of 5.000 $ x3
FEE, SLIP = 0.0005, 0.0003
HOSTS = ["https://data-api.binance.vision", "https://api.binance.com", "https://api1.binance.com"]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------- data ----------------
def fetch(sym: str, interval: str, days: int) -> list[dict]:
    step = {"5m": 300_000, "1h": 3_600_000}[interval]
    end = int(time.time() * 1000)
    start = end - days * 86_400_000
    out, t = [], start
    while t < end:
        for host in HOSTS:
            try:
                r = requests.get(f"{host}/api/v3/klines", timeout=30,
                                 params={"symbol": sym, "interval": interval, "startTime": t, "limit": 1000})
                if r.status_code == 200:
                    break
            except requests.RequestException:
                continue
        else:
            raise RuntimeError(f"no data {sym}")
        rows = r.json()
        if not rows:
            break
        for k in rows:
            if int(k[6]) < end:
                out.append({"t": int(k[0]), "o": float(k[1]), "h": float(k[2]), "l": float(k[3]), "c": float(k[4])})
        t = int(rows[-1][0]) + step
        time.sleep(0.15)
    return out


# ---------------- indicators ----------------
def ema(xs, n):
    k, out, e = 2 / (n + 1), [], None
    for x in xs:
        e = x if e is None else x * k + e * (1 - k)
        out.append(e)
    return out


def rsi(xs, n=14):
    out, ag, al = [50.0] * len(xs), 0.0, 0.0
    for i in range(1, len(xs)):
        d = xs[i] - xs[i - 1]
        g, l_ = max(d, 0), max(-d, 0)
        if i <= n:
            ag += g / n
            al += l_ / n
        else:
            ag = (ag * (n - 1) + g) / n
            al = (al * (n - 1) + l_) / n
        if i >= n:
            out[i] = 100.0 if al == 0 else 100 - 100 / (1 + ag / al)
    return out


def atr(c, n=14):
    out, a = [0.0] * len(c), None
    for i in range(1, len(c)):
        tr = max(c[i]["h"] - c[i]["l"], abs(c[i]["h"] - c[i - 1]["c"]), abs(c[i]["l"] - c[i - 1]["c"]))
        a = tr if a is None else (a * (n - 1) + tr) / n
        out[i] = a
    return out


# ---------------- replay ----------------
def replay(c, signal, tp_fn, sl_fn, hold_bars, cooldown_bars=2):
    """signal(i) -> 'long' | 'short' | None, judged on the CLOSED candle i; entry at candle i+1 open."""
    trades, i, n, free_at = [], 210, len(c), 0
    while i < n - 2:
        side = signal(i) if i >= free_at else None
        if not side:
            i += 1
            continue
        j = i + 1
        px = c[j]["o"]
        entry = px * (1 + SLIP) if side == "long" else px * (1 - SLIP)
        tp_d, sl_d = tp_fn(i, entry), sl_fn(i, entry)   # distances in price
        tp = entry + tp_d if side == "long" else entry - tp_d
        sl = entry - sl_d if side == "long" else entry + sl_d
        exit_px, reason, k = None, None, j
        for k in range(j, min(n, j + hold_bars)):
            b = c[k]
            if side == "long":
                if b["o"] <= sl: exit_px, reason = b["o"], "stop"; break
                if b["l"] <= sl: exit_px, reason = sl, "stop"; break
                if b["h"] >= tp: exit_px, reason = tp, "tp"; break
            else:
                if b["o"] >= sl: exit_px, reason = b["o"], "stop"; break
                if b["h"] >= sl: exit_px, reason = sl, "stop"; break
                if b["l"] <= tp: exit_px, reason = tp, "tp"; break
        if exit_px is None:
            exit_px, reason = c[k]["c"], "time"
        fill = exit_px * (1 - SLIP) if side == "long" else exit_px * (1 + SLIP)
        qty = NOTIONAL / entry
        gross = (fill - entry) * qty * (1 if side == "long" else -1)
        pnl = gross - NOTIONAL * FEE - fill * qty * FEE
        trades.append({"t": c[j]["t"], "side": side, "pnl": pnl, "gross": gross, "reason": reason})
        free_at = k + 1 + cooldown_bars
        i = k + 1
    return trades


def to_hourly(c5):
    out, cur = [], None
    for b in c5:
        h = b["t"] // 3_600_000 * 3_600_000
        if cur is None or cur["t"] != h:
            if cur:
                out.append(cur)
            cur = {"t": h, "o": b["o"], "h": b["h"], "l": b["l"], "c": b["c"]}
        else:
            cur["h"], cur["l"], cur["c"] = max(cur["h"], b["h"]), min(cur["l"], b["l"]), b["c"]
    if cur:
        out.append(cur)
    return out


def strategies(c5, c1h):
    cl5 = [b["c"] for b in c5]
    r5, e200_5, a5 = rsi(cl5), ema(cl5, 200), atr(c5)
    cl1 = [b["c"] for b in c1h]
    r1, e200_1, e50_1, a1 = rsi(cl1), ema(cl1, 200), ema(cl1, 50), atr(c1h)
    pct = lambda p: (lambda i, e: e * p)
    rnd = random.Random(7)

    def a_old(i):          # what A did until 31.10: buy RSI<45 turning up, no trend filter
        return "long" if r5[i] < 45 and r5[i] > r5[i - 1] else None

    def a_inverse(i):      # what A does now
        return "short" if a_old(i) else None

    def a_trend(i):        # original A: only buy the dip while price is above its 200 EMA
        return "long" if cl5[i] > e200_5[i] and r5[i] < 30 and r5[i] > r5[i - 1] else None

    def pullback_both(i):  # trade WITH the trend in both directions, only on deeper pullbacks
        if cl5[i] > e200_5[i] and r5[i] < 30 and r5[i] > r5[i - 1]:
            return "long"
        if cl5[i] < e200_5[i] and r5[i] > 70 and r5[i] < r5[i - 1]:
            return "short"
        return None

    def coin_flip(i):      # random direction every ~2 hours: shows what costs alone do
        return rnd.choice(["long", "short"]) if i % 24 == 0 else None

    hi = lambda i, n: max(b["h"] for b in c1h[i - n:i])
    lo = lambda i, n: min(b["l"] for b in c1h[i - n:i])

    def breakout_1h(i):    # 1-hour trend following: new 24h high above EMA50 -> long; new 24h low below -> short
        if i < 210:
            return None
        if cl1[i] > hi(i, 24) and cl1[i] > e50_1[i] > e200_1[i]:
            return "long"
        if cl1[i] < lo(i, 24) and cl1[i] < e50_1[i] < e200_1[i]:
            return "short"
        return None

    def pullback_1h(i):    # 1-hour: buy dips in an up-trend / sell rallies in a down-trend
        if cl1[i] > e200_1[i] and r1[i] < 35 and r1[i] > r1[i - 1]:
            return "long"
        if cl1[i] < e200_1[i] and r1[i] > 65 and r1[i] < r1[i - 1]:
            return "short"
        return None

    return {
        "A eski (RSI<45 alış, %0,6/%0,4)": (c5, a_old, pct(0.006), pct(0.004), 24, 2),
        "A şimdiki TERS (aynı sinyalde satış)": (c5, a_inverse, pct(0.006), pct(0.004), 24, 2),
        "Yazı-tura (rastgele yön, aynı hedef/stop)": (c5, coin_flip, pct(0.006), pct(0.004), 24, 2),
        "İlk A: trend filtresi + RSI<30 (5 dk)": (c5, a_trend, pct(0.006), pct(0.004), 24, 2),
        "Trend yönünde geri çekilme, iki yön (5 dk)": (c5, pullback_both, pct(0.006), pct(0.004), 24, 2),
        "Trend yönünde geri çekilme, ATR hedef 3x / stop 1,5x (5 dk)":
            (c5, pullback_both, lambda i, e: 3 * a5[i], lambda i, e: 1.5 * a5[i], 144, 2),
        "1 saatlik trend geri çekilme, ATR 3x / 1,5x":
            (c1h, pullback_1h, lambda i, e: 3 * a1[i], lambda i, e: 1.5 * a1[i], 48, 1),
        "1 saatlik kırılım (trend takibi), ATR 4x / 2x":
            (c1h, breakout_1h, lambda i, e: 4 * a1[i], lambda i, e: 2 * a1[i], 72, 1),
    }


def summarize(tr):
    if not tr:
        return {"n": 0, "win": 0, "net": 0.0, "avg_pct": 0.0, "pf": 0.0, "dd": 0.0, "stop": 0, "tp": 0, "time": 0}
    w = [t for t in tr if t["pnl"] > 0]
    gp, gl = sum(t["pnl"] for t in w), -sum(t["pnl"] for t in tr if t["pnl"] <= 0)
    eq = peak = dd = 0.0
    for t in sorted(tr, key=lambda x: x["t"]):
        eq += t["pnl"]
        peak = max(peak, eq)
        dd = max(dd, peak - eq)
    net = sum(t["pnl"] for t in tr)
    return {"n": len(tr), "win": round(100 * len(w) / len(tr), 1), "net": round(net, 2),
            "avg_pct": round(100 * net / len(tr) / NOTIONAL, 3), "pf": round(gp / gl, 2) if gl else 99.0,
            "dd": round(dd, 2), "gross": round(sum(t["gross"] for t in tr), 2),
            "stop": sum(t["reason"] == "stop" for t in tr), "tp": sum(t["reason"] == "tp" for t in tr),
            "time": sum(t["reason"] == "time" for t in tr)}


def main():
    data = {}
    for s in SYMBOLS:
        data[s] = fetch(s, "5m", DAYS)
        print(s, len(data[s]), "candles", flush=True)
    t0 = min(d[0]["t"] for d in data.values())
    t1 = max(d[-1]["t"] for d in data.values())
    split = t0 + int((t1 - t0) * 0.6)
    res = {}
    for s in SYMBOLS:
        c5 = data[s]
        c1h = to_hourly(c5)
        for name, (c, sig, tp, sl, hold, cd) in strategies(c5, c1h).items():
            tr = replay(c, sig, tp, sl, hold, cd)
            for t in tr:
                t["sym"] = s
            res.setdefault(name, []).extend(tr)
    first = dt.datetime.fromtimestamp(t0 / 1000).strftime("%d.%m.%Y")
    mid = dt.datetime.fromtimestamp(split / 1000).strftime("%d.%m.%Y")
    last = dt.datetime.fromtimestamp(t1 / 1000).strftime("%d.%m.%Y")
    out = {"period": [first, mid, last], "notional": NOTIONAL, "strategies": {}}
    for name, tr in res.items():
        out["strategies"][name] = {
            "all": summarize(tr),
            "learn": summarize([t for t in tr if t["t"] < split]),
            "test": summarize([t for t in tr if t["t"] >= split]),
            "by_coin": {s: summarize([t for t in tr if t["sym"] == s]) for s in SYMBOLS},
        }
    os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
    with open(os.path.join(ROOT, "reports", "backtest_A.json"), "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    md = [f"# Bot A — geçmiş veri testi ({first} – {last}, 6 coin, 5 dk mumlar)", "",
          f"Pozisyon {NOTIONAL:,.0f} $ (A'nın bugünkü büyüklüğü), masraf işlem başına ~%0,16 (komisyon + kayma).",
          f"Öğrenme dönemi {first}–{mid}, test dönemi {mid}–{last}.", "",
          "| Strateji | İşlem | Kazanma % | Net $ (tümü) | İşlem başı % | Kâr faktörü | En büyük düşüş $ | TEST dönemi net $ | TEST kâr faktörü |",
          "|---|---|---|---|---|---|---|---|---|"]
    for name, r in out["strategies"].items():
        a, t = r["all"], r["test"]
        md.append(f"| {name} | {a['n']} | {a['win']} | {a['net']:+,.0f} | {a['avg_pct']:+.3f} | {a['pf']} | {a['dd']:,.0f} | "
                  f"{t['net']:+,.0f} | {t['pf']} |")
    with open(os.path.join(ROOT, "reports", "backtest_A.md"), "w") as f:
        f.write("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
