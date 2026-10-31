"""Public market data (no account, no keys) + simple indicators."""
import time

import requests

HOSTS = ["https://data-api.binance.vision", "https://api.binance.com", "https://api1.binance.com",
         "https://api-gcp.binance.com"]


def yahoo_klines(symbol: str, interval: str, limit: int = 300) -> list[dict]:
    """Futures such as Brent oil (BZ=F) from Yahoo Finance's public chart API. Same shape as klines()."""
    rng = {"1m": "1d", "5m": "5d", "15m": "5d"}.get(interval, "5d")
    step = {"1m": 60_000, "5m": 300_000, "15m": 900_000}.get(interval, 300_000)
    last = None
    for host in ("https://query1.finance.yahoo.com", "https://query2.finance.yahoo.com"):
        for _ in range(2):
            try:
                r = requests.get(f"{host}/v8/finance/chart/{symbol}", timeout=20,
                                 params={"interval": interval, "range": rng, "includePrePost": "true"},
                                 headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) trade-lab"})
                if r.status_code == 200:
                    res = r.json()["chart"]["result"][0]
                    q = res["indicators"]["quote"][0]
                    now = int(time.time() * 1000)
                    out = []
                    for i, ts in enumerate(res.get("timestamp") or []):
                        o, h, lo, c = q["open"][i], q["high"][i], q["low"][i], q["close"][i]
                        if None in (o, h, lo, c):
                            continue
                        t = int(ts) * 1000
                        out.append({"t": t, "o": float(o), "h": float(h), "l": float(lo), "c": float(c),
                                    "closed": t + step <= now})
                    if out:
                        return out[-limit:]
                last = f"{host}: HTTP {r.status_code} {r.text[:120]}"
            except (requests.RequestException, KeyError, IndexError, TypeError, ValueError) as e:
                last = f"{host}: {e}"
            time.sleep(1)
    raise RuntimeError(f"No market data for {symbol}: {last}")


def klines(symbol: str, interval: str, limit: int = 300) -> list[dict]:
    """Returns candles oldest -> newest: {t, o, h, l, c, closed}."""
    if "=" in symbol:  # futures tickers (BZ=F = Brent oil) come from Yahoo, crypto/PAXG from Binance
        return yahoo_klines(symbol, interval, limit)
    last = None
    for host in HOSTS:
        for _ in range(2):
            try:
                r = requests.get(f"{host}/api/v3/klines", timeout=20,
                                 params={"symbol": symbol, "interval": interval, "limit": limit})
                if r.status_code == 200:
                    now = int(time.time() * 1000)
                    return [{"t": int(k[0]), "o": float(k[1]), "h": float(k[2]), "l": float(k[3]),
                             "c": float(k[4]), "closed": int(k[6]) < now} for k in r.json()]
                last = f"{host}: HTTP {r.status_code} {r.text[:120]}"
            except requests.RequestException as e:
                last = f"{host}: {e}"
            time.sleep(1)
    raise RuntimeError(f"No market data for {symbol}: {last}")


def ema(values: list[float], n: int) -> list[float]:
    k, out = 2 / (n + 1), []
    for i, v in enumerate(values):
        out.append(v if i == 0 else v * k + out[-1] * (1 - k))
    return out


def rsi(values: list[float], n: int = 14) -> list[float]:
    out = [50.0] * len(values)
    gain = loss = 0.0
    for i in range(1, len(values)):
        d = values[i] - values[i - 1]
        g, l_ = max(d, 0), max(-d, 0)
        if i <= n:
            gain += g / n
            loss += l_ / n
        else:
            gain = (gain * (n - 1) + g) / n
            loss = (loss * (n - 1) + l_) / n
        if i >= n:
            out[i] = 100.0 if loss == 0 else 100 - 100 / (1 + gain / loss)
    return out
