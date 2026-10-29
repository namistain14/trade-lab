"""One 5-minute tick: both paper bots, state saved, dashboard (README) refreshed."""
import datetime as dt
import json
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bots  # noqa: E402
import market  # noqa: E402
import paper  # noqa: E402
import stocks  # noqa: E402

STATE = os.path.join(ROOT, "state", "state.json")
IST = dt.timezone(dt.timedelta(hours=3))


def load() -> tuple[dict, dict]:
    with open(os.path.join(ROOT, "config.yaml")) as f:
        cfg = yaml.safe_load(f)
    try:
        with open(STATE) as f:
            st = json.load(f)
    except (FileNotFoundError, ValueError):
        st = {}
    for name in cfg["bots"]:
        start = 100000 if cfg["bots"][name].get("type") == "stocks_alpaca" else cfg["start_equity_usd"]
        st.setdefault(name, {"account": paper.new_account(start), "equity_curve": []})
    st.setdefault("log", [])
    return cfg, st


def save(st: dict) -> None:
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    tmp = STATE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(st, f, indent=1)
    os.replace(tmp, STATE)


def fmt_ms(ms: int) -> str:
    return dt.datetime.fromtimestamp(ms / 1000, IST).strftime("%d.%m %H:%M")


def dashboard(cfg: dict, st: dict, prices: dict) -> None:
    now = dt.datetime.now(IST)
    day_start = int(dt.datetime.combine(now.date(), dt.time(), IST).timestamp() * 1000)
    names = {n: b.get("label", n) for n, b in cfg["bots"].items()}
    out = ["# trade-lab — SANAL işlem denemesi",
           "",
           "> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.",
           f"> Son güncelleme: {now.strftime('%d.%m.%Y %H:%M')} (İstanbul)",
           ""]
    for name, b in cfg["bots"].items():
        if not b.get("enabled"):
            continue  # Erdem 29.10: switched-off bots are no longer listed
        acc = st[name]["account"]
        eq = paper.equity(acc, prices)
        all_s, day_s = paper.stats(acc), paper.stats(acc, day_start)
        chg = eq - acc["start"]
        out += [f"## {names.get(name, name)}",
                "",
                "| | Bugün | Toplam |",
                "|---|---|---|",
                f"| Net kâr/zarar | {day_s['net']:+.2f} $ | {all_s['net']:+.2f} $ |",
                f"| İşlem sayısı | {day_s['trades']} | {all_s['trades']} |",
                f"| Kazanma oranı | %{day_s['win_rate']} | %{all_s['win_rate']} |",
                f"| Ödenen komisyon/spread | {day_s['costs']:.2f} $ | {all_s['costs']:.2f} $ |",
                "",
                f"**Hesap değeri: {eq:,.2f} $** (başlangıç {acc['start']:,.0f} $, {chg:+.2f} $ / %{100 * chg / acc['start']:+.2f})",
                ""]
        if acc["positions"]:
            out.append("Açık pozisyonlar: " + "; ".join(
                f"{p['symbol']} {p['side']} @ {p['entry']:.2f} (TP {p['tp']:.2f} / SL {p['sl']:.2f})"
                for p in acc["positions"]))
            out.append("")
        if name == "gold_news" and st.get(name, {}).get("news"):  # the shared news view lives with B1
            n = st[name]["news"]
            out += [f"Son haber analizi ({fmt_ms(n.get('ts', 0))}): Claude puan **{n.get('score', 0):+.2f}**, "
                    f"güven {n.get('confidence', 0):.2f} — {n.get('reason', '')}", ""]
            g = n.get("gpt") or {}
            if g:
                out += [f"GPT ({g.get('model', '')}): puan **{g.get('score', 0):+.2f}**, güven {g.get('confidence', 0):.2f}"
                        f" — {g.get('reason', '')}", ""]
        last = acc["trades"][-5:][::-1]
        if last:
            out += ["Son işlemler:", "", "| Kapanış | Parite | Yön | Sonuç | Neden |", "|---|---|---|---|---|"]
            out += [f"| {fmt_ms(t['closed_ms'])} | {t['symbol']} | {t['side']} | {t['pnl']:+.2f} $ | {t['reason']} |"
                    for t in last]
            out.append("")
    out += ["## Son olaylar", "", "```"] + st["log"][-15:] + ["```", "",
            "Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`."]
    with open(os.path.join(ROOT, "README.md"), "w") as f:
        f.write("\n".join(out) + "\n")


def main() -> None:
    cfg, st = load()
    log: list[str] = []
    prices: dict = {}
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip() or None
    b = cfg["bots"]
    errors = []
    # Erdem's one-off paper orders (config "manual_orders"): opened once at the market price, held for N hours
    done = st.setdefault("manual_done", [])
    for mo in cfg.get("manual_orders") or []:
        if mo["id"] in done:
            continue
        try:
            bc = b[mo["bot"]]
            acc = st[mo["bot"]]["account"]
            px = market.klines(mo["symbol"], "1m", 5)[-1]["c"] * (1 + bc["slippage_rate"])
            usd = float(mo["usd"])
            paper.open_position(acc, symbol=mo["symbol"], side="long", price=px, qty=usd / px, tp=px * 100, sl=0.0,
                                t_ms=int(dt.datetime.now().timestamp() * 1000), entry_cost=usd * bc["fee_rate"],
                                max_hold_min=int(float(mo["hold_hours"]) * 60), margin=usd,
                                note=mo.get("note", "Erdem'in elle verdiği alım"))
            log.append(f"{bc.get('tag', mo['bot'])}  BUY {mo['symbol']} {usd:.0f} USD @ {px:.2f} (elle, {mo['hold_hours']} saat tut)")
        except Exception as e:  # noqa: BLE001
            errors.append(f"manual {mo['id']}: {e}")
        done.append(mo["id"])
    # Erdem's one-off balance resets (config "resets"): the bot starts again from a clean account, old trades kept aside
    rdone = st.setdefault("resets_done", [])
    for rs in cfg.get("resets") or []:
        if rs["id"] in rdone or rs["bot"] not in st:
            continue
        old = st[rs["bot"]]["account"]
        st[rs["bot"]].setdefault("archive", []).append({"until_ms": int(dt.datetime.now().timestamp() * 1000),
                                                      "balance": round(old["balance"], 2), "start": old["start"],
                                                      "trades": old["trades"]})
        st[rs["bot"]]["account"] = paper.new_account(float(rs["balance"]))
        st[rs["bot"]]["equity_curve"] = []
        log.append(f"{b[rs['bot']].get('tag', rs['bot'])}  bakiye {float(rs['balance']):,.0f} $ olarak yeniden başlatıldı")
        rdone.append(rs["id"])
    # switched-off bots: any position still open is closed once at the market price
    for name, bc in b.items():
        acc = st[name]["account"]
        if bc.get("enabled") or not acc["positions"] or bc.get("type") == "stocks_alpaca":
            continue
        for pos in list(acc["positions"]):
            try:
                px = market.klines(pos["symbol"], "1m", 5)[-1]["c"]
                half = bc.get("spread_usd_per_oz", 0) / 2
                slip = bc.get("slippage_rate", 0)
                fill = px - half - px * slip if pos["side"] == "long" else px + half + px * slip
                tr = paper._close(acc, pos, fill, int(dt.datetime.now().timestamp() * 1000), "bot kapatıldı",
                                  fill * pos["qty"] * bc.get("fee_rate", 0))
                log.append(f"{bc.get('tag', name)}  CLOSE {pos['symbol']} bot kapatıldı: {tr['pnl']:+.2f} USD")
            except Exception as e:  # noqa: BLE001
                errors.append(f"{bc.get('tag', name)} kapatma: {e}")
    # one gold bot reads the news and the others share its view. The view always lives with "gold_news";
    # if B1 itself is switched off, the first gold bot still running reads the news in its place.
    gold_on = [n for n in b if b[n].get("enabled") and b[n].get("type") == "gold_news"]
    news_owner = "gold_news" if "gold_news" in gold_on else (gold_on[0] if gold_on else None)
    order = sorted(b, key=lambda n: (b[n].get("type", n) != "crypto_rules", n != news_owner))
    for name in order:
        bc = b[name]
        if not bc.get("enabled"):
            continue
        kind = bc.get("type", name)
        tag = bc.get("tag", name)
        try:
            if kind == "crypto_rules":
                prices.update(bots.crypto_tick(st[name]["account"], bc, log))
            elif kind == "gold_news":
                shared = None if name == news_owner else st["gold_news"].setdefault("news", {})
                prices.update(bots.gold_tick(st[name]["account"], bc, cfg["news"], st["gold_news"] if name == news_owner else st[name], log, key,
                                             shared_news=shared, tag=tag))
            elif kind == "stocks_alpaca":
                prices.update(stocks.stocks_tick(st[name], bc, cfg["news"], log, key, tag=tag))
        except Exception as e:  # noqa: BLE001
            errors.append(f"{tag}: {e}")

    stamp = dt.datetime.now(IST).strftime("%d.%m %H:%M")
    for name in cfg["bots"]:
        acc = st[name]["account"]
        curve = st[name]["equity_curve"]
        curve.append([int(dt.datetime.now().timestamp()), round(paper.equity(acc, prices), 2)])
        st[name]["equity_curve"] = curve[-3000:]
    st["log"] = (st["log"] + [f"{stamp} {line}" for line in log + [f"ERROR {e}" for e in errors]])[-300:]
    save(st)
    dashboard(cfg, st, prices)
    for line in log:
        print(line)
    for e in errors:
        print(f"::warning::{e}")


if __name__ == "__main__":
    main()
