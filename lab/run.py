"""One 5-minute tick: both paper bots, state saved, dashboard (README) refreshed."""
import datetime as dt
import json
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bots  # noqa: E402
import paper  # noqa: E402

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
        st.setdefault(name, {"account": paper.new_account(cfg["start_equity_usd"]), "equity_curve": []})
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
    names = {"crypto_rules": "Bot A — Kripto kurallar (spot, kaldıraçsız)",
             "gold_news": "Bot B — Altın + haber (1:10 kaldıraç)"}
    out = ["# trade-lab — SANAL işlem denemesi",
           "",
           "> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.",
           f"> Son güncelleme: {now.strftime('%d.%m.%Y %H:%M')} (İstanbul)",
           ""]
    for name, b in cfg["bots"].items():
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
        if name == "gold_news" and st.get(name, {}).get("news"):
            n = st[name]["news"]
            out += [f"Son haber analizi ({fmt_ms(n.get('ts', 0))}): puan **{n.get('score', 0):+.2f}**, "
                    f"güven {n.get('confidence', 0):.2f} — {n.get('reason', '')}", ""]
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
    if b.get("crypto_rules", {}).get("enabled"):
        try:
            prices.update(bots.crypto_tick(st["crypto_rules"]["account"], b["crypto_rules"], log))
        except Exception as e:  # noqa: BLE001
            errors.append(f"Bot A: {e}")
    if b.get("gold_news", {}).get("enabled"):
        try:
            prices.update(bots.gold_tick(st["gold_news"]["account"], b["gold_news"], cfg["news"], st["gold_news"],
                                         log, key))
        except Exception as e:  # noqa: BLE001
            errors.append(f"Bot B: {e}")

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
