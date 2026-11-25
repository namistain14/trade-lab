# Hayatta Kalan - MT5 koprusu (Erdem'in bilgisayarinda calisir).
# trade-lab'daki 3 modelli kurulun sinyalini okur, hayatta kalma kurallarini GERCEK bakiyeye gore uygular
# ve emri zarar-durdur + hedef ile MetaTrader 5'e gonderir. Sifre ya da anahtar icermez, istemez.
import datetime
import json
import math
import os
import sys
import time
import urllib.error
import urllib.request

try:
    import MetaTrader5 as mt5
except Exception as e:  # noqa: BLE001
    print("MetaTrader5 paketi yuklenemedi:", e)
    sys.exit(1)

API_URL = "https://api.github.com/repos/namistain14/trade-lab/contents/state/signals.json"
RAW_URL = "https://raw.githubusercontent.com/namistain14/trade-lab/main/state/signals.json"
MAGIC = 7300126                      # bu koprunun actigi islemlerin kimligi
SYMBOLS = ["BRENTCash", "OILCash", "Nvidia", "Apple", "Tesla"]
POLL_SECONDS = 75
# Sert sinirlar: sinyal dosyasi bunlari GEVSETEMEZ, yalnizca sikilastirabilir.
RISK_PCT, MAX_RISK_PCT = 1.0, 1.5    # islem basina risk (hesabin yuzdesi)
DEATH_LINE_PCT = 70.0                # varlik baslangicin %70'ine inerse kalici dur
DAILY_LOSS_PCT, WEEKLY_LOSS_PCT = 3.0, 6.0
MAX_SIGNAL_AGE_MIN = 20

HERE = os.path.dirname(os.path.abspath(sys.argv[0]))
STATE_FILE = os.path.join(HERE, "kopru_durum.json")
LOG_FILE = os.path.join(HERE, "kopru_gunluk.txt")
LIVE = False


def log(*a):
    line = datetime.datetime.now().strftime("%d.%m %H:%M:%S ") + " ".join(str(x) for x in a)
    print(line, flush=True)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass


def load_state():
    try:
        with open(STATE_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {"start_equity": None, "done": [], "dead": False, "open": {}, "day": {}, "week": {}}


def save_state(st):
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(st, f, indent=1)
    os.replace(tmp, STATE_FILE)


# ---------------- sinyal dosyasi ----------------
_cache = {"etag": None, "data": None}


def fetch_signals():
    req = urllib.request.Request(API_URL, headers={"Accept": "application/vnd.github.raw+json",
                                                   "User-Agent": "hayatta-kalan-kopru"})
    if _cache["etag"]:
        req.add_header("If-None-Match", _cache["etag"])
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            _cache["data"] = json.loads(r.read().decode("utf-8"))
            _cache["etag"] = r.headers.get("ETag")
    except urllib.error.HTTPError as e:
        if e.code == 304:
            return _cache["data"]
        try:  # API siniri ya da gecici hata: yedek adres (birkac dakika gecikmeli olabilir)
            with urllib.request.urlopen(RAW_URL + "?t=%d" % int(time.time() // 60), timeout=20) as r:
                _cache["data"] = json.loads(r.read().decode("utf-8"))
        except Exception:  # noqa: BLE001
            return None
    except Exception:  # noqa: BLE001
        return None
    return _cache["data"]


# ---------------- MT5 yardimcilari ----------------
def connect():
    if mt5.terminal_info() is None and not mt5.initialize():
        return False
    return mt5.account_info() is not None


def fresh_tick(name, max_age=120):
    mt5.symbol_select(name, True)
    t = mt5.symbol_info_tick(name)
    if not t or not t.ask or not t.bid:
        return None
    ref = max((x.time for x in (mt5.symbol_info_tick(s) for s in SYMBOLS + ["EURUSD"]) if x), default=t.time)
    return t if ref - t.time <= max_age else None


def plan(name, side, stop_pct, target_pct, equity, free_margin):
    """Emrin tum sayilarini hesaplar. (istek, aciklama) ya da (None, neden) doner."""
    info = mt5.symbol_info(name)
    if info is None:
        return None, "sembol bulunamadi"
    if info.trade_mode != 4:
        return None, "sembol isleme kapali"
    tick = fresh_tick(name)
    if tick is None:
        return None, "piyasa kapali (taze fiyat yok)"
    long_ = side == "long"
    otype = mt5.ORDER_TYPE_BUY if long_ else mt5.ORDER_TYPE_SELL
    price = tick.ask if long_ else tick.bid
    d = 1 if long_ else -1
    sl = round(price * (1 - d * stop_pct / 100), info.digits)
    tp = round(price * (1 + d * target_pct / 100), info.digits)
    spread_pct = (tick.ask - tick.bid) / tick.bid * 100
    if target_pct < 5 * spread_pct or spread_pct > 0.25 * stop_pct:
        return None, "alis-satis farki cok genis (%%%.3f)" % spread_pct
    min_dist = info.trade_stops_level * info.point
    if abs(price - sl) <= min_dist or abs(tp - price) <= min_dist:
        return None, "stop/hedef araci kurumun en az mesafesinden yakin"
    loss1 = mt5.order_calc_profit(otype, name, 1.0, price, sl)
    if loss1 is None or loss1 >= 0:
        return None, "risk hesaplanamadi"
    per_lot = abs(loss1)
    step, vmin = info.volume_step, info.volume_min
    lots = math.floor(equity * RISK_PCT / 100 / per_lot / step + 1e-9) * step
    if lots < vmin:
        if vmin * per_lot <= equity * MAX_RISK_PCT / 100:
            lots = vmin
        else:
            return None, "en kucuk islem bile risk sinirini asiyor (%.2f $ > %.2f $)" % (vmin * per_lot, equity * MAX_RISK_PCT / 100)
    lots = round(min(lots, info.volume_max), 6)
    margin = mt5.order_calc_margin(otype, name, lots, price)
    if margin is None or margin > 0.5 * free_margin:
        return None, "teminat yetersiz"
    req = {"action": mt5.TRADE_ACTION_DEAL, "symbol": name, "volume": lots, "type": otype, "price": price, "sl": sl,
           "tp": tp, "deviation": 30, "magic": MAGIC, "comment": "HK", "type_time": mt5.ORDER_TIME_GTC}
    text = "%s %s %.2f lot @ %s, stop %s, hedef %s, risk %.2f $, teminat %.2f $, fark %%%.3f" % (
        name, "ALIS" if long_ else "SATIS", lots, price, sl, tp, lots * per_lot, margin, spread_pct)
    return req, text


def with_filling(req, fn):
    """Araci kurumun kabul ettigi dolum turunu bulur."""
    res = None
    for fill in (mt5.ORDER_FILLING_IOC, mt5.ORDER_FILLING_FOK, mt5.ORDER_FILLING_RETURN):
        res = fn({**req, "type_filling": fill})
        if res is None or res.retcode != 10030:   # 10030 = bu dolum turu desteklenmiyor
            break
    return res


def my_positions():
    return [p for p in (mt5.positions_get() or []) if p.magic == MAGIC]


def close_position(p, why):
    tick = mt5.symbol_info_tick(p.symbol)
    if not tick:
        return False
    is_buy = p.type == mt5.POSITION_TYPE_BUY
    req = {"action": mt5.TRADE_ACTION_DEAL, "symbol": p.symbol, "volume": p.volume, "position": p.ticket,
           "type": mt5.ORDER_TYPE_SELL if is_buy else mt5.ORDER_TYPE_BUY, "price": tick.bid if is_buy else tick.ask,
           "deviation": 30, "magic": MAGIC, "comment": "HK kapat", "type_time": mt5.ORDER_TIME_GTC}
    res = with_filling(req, mt5.order_send)
    ok = res is not None and res.retcode in (10008, 10009)
    log("KAPATMA", p.symbol, why, "->", "tamam" if ok else "BASARISIZ %s" % (res.comment if res else mt5.last_error(),))
    return ok


def recent_losses():
    """Bu koprunun son kapanan islemleri (en yeni sonda): [(sunucu_zamani, kar)]"""
    now = datetime.datetime.now() + datetime.timedelta(days=1)
    deals = mt5.history_deals_get(now - datetime.timedelta(days=15), now) or []
    out = [(d.time, d.profit + d.swap + d.commission) for d in deals if d.magic == MAGIC and d.entry == 1]
    return sorted(out)


def server_now():
    return max((x.time for x in (mt5.symbol_info_tick(s) for s in SYMBOLS + ["EURUSD"]) if x), default=int(time.time()))


def blocked(st, acc):
    """Hayatta kalma kurallari. Yeni islem acilamiyorsa nedenini doner."""
    eq, start = acc.equity, st["start_equity"]
    if st.get("dead") or eq <= start * DEATH_LINE_PCT / 100:
        if not st.get("dead"):
            st["dead"] = True
            log("OLUM CIZGISI: varlik %.2f $, baslangic %.2f $. Kopru kalici olarak durdu." % (eq, start))
        return "olum cizgisi (kalici durus)"
    today = datetime.date.today().isoformat()
    week = "%d-%02d" % datetime.date.today().isocalendar()[:2]
    if st["day"].get("date") != today:
        st["day"] = {"date": today, "equity": eq}
    if st["week"].get("id") != week:
        st["week"] = {"id": week, "equity": eq}
    if eq <= st["day"]["equity"] * (1 - DAILY_LOSS_PCT / 100):
        return "gunluk zarar siniri"
    if eq <= st["week"]["equity"] * (1 - WEEKLY_LOSS_PCT / 100):
        return "haftalik zarar siniri"
    last = recent_losses()[-3:]
    if len(last) == 3 and all(p < 0 for _, p in last) and server_now() - last[-1][0] < 24 * 3600:
        return "art arda 3 zarar: 24 saat mola"
    if my_positions():
        return "acik islem var"
    return None


def moved_since(name, t_ms):
    """Sinyal verildiginden beri fiyat yuzde kac oynadi (kendi fiyatina gore)."""
    age = int((time.time() * 1000 - t_ms) // 60000)
    rates = mt5.copy_rates_from_pos(name, mt5.TIMEFRAME_M1, 0, age + 3)
    if rates is None or len(rates) < 2:
        return 0.0
    return (rates[-1]["close"] / rates[0]["open"] - 1) * 100


def self_test(acc):
    log("--- KABLO TESTI (emir GONDERILMEZ, yalnizca sunucuya 'bu emir gecerli mi' diye sorulur) ---")
    for name in SYMBOLS:
        req, text = plan(name, "long", 1.0, 2.0, acc.equity, acc.margin_free)
        if req is None:
            log("  %-10s : %s" % (name, text))
            continue
        res = with_filling(req, mt5.order_check)
        verdict = "GECERLI" if res is not None and res.retcode == 0 else "RED: %s" % ((res.retcode, res.comment) if res else mt5.last_error(),)
        log("  %-10s : %s -> %s" % (name, text, verdict))
    log("--- test bitti ---")


def handle(sig, st, acc):
    sid = sig["id"]
    now_ms = time.time() * 1000
    st["done"] = (st["done"] + [sid])[-200:]
    if now_ms > sig["expires_ms"] or now_ms - sig["t_ms"] > MAX_SIGNAL_AGE_MIN * 60000:
        return log("sinyal", sid, sig["sym"], "gec kaldi, atlandi")
    name = sig["mt5"]
    if name not in SYMBOLS:
        return log("sinyal", sid, "bilinmeyen sembol", name)
    stop_pct, target_pct = float(sig["stop_pct"]), float(sig["target_pct"])
    if not (0.2 <= stop_pct <= 3.0) or target_pct < 1.5 * stop_pct:
        return log("sinyal", sid, "stop/hedef kural disi, atlandi")
    why = blocked(st, acc)
    if why:
        return log("sinyal", sid, sig["sym"], sig["side"], "ACILMADI:", why)
    drift = moved_since(name, sig["t_ms"])
    if abs(drift) > 0.4 * stop_pct:
        return log("sinyal", sid, "fiyat sinyalden beri %%%.2f oynadi, atlandi" % drift)
    req, text = plan(name, sig["side"], stop_pct, target_pct, acc.equity, acc.margin_free)
    if req is None:
        return log("sinyal", sid, sig["sym"], "ACILMADI:", text)
    req["comment"] = "HK " + sid
    if not LIVE:
        res = with_filling(req, mt5.order_check)
        return log("TEST MODU (emir gonderilmedi):", text, "| sunucu:", "gecerli" if res is not None and res.retcode == 0 else (res.comment if res else "?"))
    if not mt5.terminal_info().trade_allowed:
        return log("EMIR GONDERILEMEDI: MT5'te 'Algoritmik Ticaret' dugmesi kapali.", text)
    res = with_filling(req, mt5.order_send)
    if res is not None and res.retcode in (10008, 10009):
        st["open"][str(res.order)] = sig.get("close_by_ms") or (now_ms + 24 * 3600000)
        log("EMIR ACILDI:", text, "| fiyat", res.price, "| bilet", res.order)
    else:
        log("EMIR REDDEDILDI:", text, "|", (res.retcode, res.comment) if res else mt5.last_error())


def main():
    global LIVE, RISK_PCT, MAX_RISK_PCT
    if not mt5.initialize():
        print("MT5'e baglanilamadi:", mt5.last_error())
        print("MetaTrader 5 acik ve hesaba giris yapilmis olmali.")
        return
    acc, term = mt5.account_info(), mt5.terminal_info()
    st = load_state()
    if st.get("account") not in (None, acc.login):
        st = {"start_equity": None, "done": [], "dead": False, "open": {}, "day": {}, "week": {}}
    st["account"] = acc.login
    if not st.get("start_equity"):
        st["start_equity"] = acc.equity
    save_state(st)
    log("=== HAYATTA KALAN KOPRU ===")
    log("hesap ***%s | %s | %s | bakiye %.2f + bonus %.2f = varlik %.2f %s" % (
        str(acc.login)[-3:], acc.server, "GERCEK" if acc.trade_mode == 2 else "DEMO", acc.balance, acc.credit, acc.equity, acc.currency))
    log("baslangic %.2f | olum cizgisi %.2f | islem basina risk %%%.1f (en cok %%%.1f) | gunluk -%%%.0f, haftalik -%%%.0f" % (
        st["start_equity"], st["start_equity"] * DEATH_LINE_PCT / 100, RISK_PCT, MAX_RISK_PCT, DAILY_LOSS_PCT, WEEKLY_LOSS_PCT))
    log("'Algoritmik Ticaret' dugmesi:", "ACIK" if term.trade_allowed else "KAPALI (canli mod icin acilmali)")
    self_test(acc)
    if st.get("dead"):
        log("Bu hesap olum cizgisine inmis; kopru islem ACMAZ. (Sifirlamak icin Claude'a yaz.)")
    print()
    ans = input("CANLI islem icin EVET yaz ve Enter'a bas. Yalnizca test icin dogrudan Enter'a bas: ").strip().upper()
    LIVE = ans == "EVET"
    log("MOD:", "CANLI - gercek emir gonderilecek" if LIVE else "TEST - emir gonderilmeyecek")
    log("Sinyal bekleniyor. Bu pencere acik kalmali; kapatirsan kopru durur. (Acik islemlerin stop/hedefi araci kurumda durur.)")
    last_beat = 0
    while True:
        try:
            if not connect():
                log("MT5 baglantisi yok, tekrar denenecek")
                time.sleep(POLL_SECONDS)
                continue
            acc = mt5.account_info()
            # suresi dolan ya da kapanmis islemler
            mine = {str(p.ticket): p for p in my_positions()}
            for ticket, close_by in list(st["open"].items()):
                p = mine.get(ticket)
                if p is None:
                    st["open"].pop(ticket)
                    last = recent_losses()[-1:]
                    log("islem kapandi (stop/hedef):", "%+.2f $" % last[0][1] if last else "")
                elif time.time() * 1000 >= close_by and LIVE:
                    if close_position(p, "sure doldu"):
                        st["open"].pop(ticket)
            data = fetch_signals()
            if data:
                RISK_PCT = min(1.0, float(data.get("risk_pct", 1.0)))
                MAX_RISK_PCT = min(1.5, float(data.get("max_risk_pct", 1.5)))
                if data.get("halt") and not st.get("halt_note"):
                    log("Kurul 'dur' dedi (golge hesap olum cizgisinde). Yeni islem acilmayacak.")
                    st["halt_note"] = True
                for sig in data.get("signals", []):
                    if sig["id"] not in st["done"] and not data.get("halt"):
                        handle(sig, st, acc)
            blocked(st, acc)   # gun/hafta baslangiclarini ve olum cizgisini guncel tutar
            save_state(st)
            if time.time() - last_beat > 1800:
                last_beat = time.time()
                log("calisiyor | varlik %.2f | acik islem %d | mod %s" % (acc.equity, len(my_positions()), "CANLI" if LIVE else "TEST"))
        except KeyboardInterrupt:
            break
        except Exception as e:  # noqa: BLE001
            log("hata (devam ediliyor):", repr(e)[:200])
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
