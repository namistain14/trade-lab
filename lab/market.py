"""Public market data (no account, no keys) + simple indicators."""
import time

import requests

HOSTS = ["https://data-api.binance.vision", "https://api.binance.com", "https://api1.binance.com",
         "https://api-gcp.binance.com"]


def klines(symbol: str, interval: str, limit: int = 300) -> list[dict]:
    """Returns candles oldest -> newest: {t, o, h, l, c, closed}."""
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
