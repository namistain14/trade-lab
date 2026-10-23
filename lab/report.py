"""Daily review: Claude studies today's paper trades and writes an honest report (Turkish) in reports/."""
import datetime as dt
import json
import os
import sys

import anthropic

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import paper  # noqa: E402
from run import IST, load  # noqa: E402

PROMPT = """Sen dürüst ve temkinli bir kantitatif analistsin. Aşağıda iki SANAL (paper) trading botunun verileri var.
Bot A: kripto, kurallara dayalı (RSI + EMA200 trend filtresi), spot, kaldıraçsız. A2: kripto, %2+ düşüş sonrası ilk yeşil mumda alım (trend filtresi yok), spot. B1/B2/B3: altın (PAXG ile XAU/USD simülasyonu),
haberleri Claude puanlıyor, 1:10 kaldıraç. B1 gözlem ayarları (TP 5$/SL 3$), B2 sıkı eşik ve büyük hedef (TP 15$/SL 10$),
B3 = B2 + Londra/New York seans filtresi + momentum + kârı koruma. B4 = haberin TERSİNE işlem (fiyat da haberi dinlemiyorsa), TP 15$/SL 10$. B5 = sadece Claude ve GPT haberleri aynı yönde okuduğunda işlem (iki model kontrolü), TP 15$/SL 10$; haber kayıtlarında gpt_score Claude'un puanının yanında. Botları özellikle işlem başına ortalama net kazanç
(expectancy) ve başa baş kazanma oranı açısından karşılaştır.

Ayarlar:
{config}

Bugünün ve toplamın istatistikleri:
{stats}

Bugünkü işlemler (en fazla 60):
{trades}

Bugünkü haber puanları (Bot B):
{news}

Türkçe, sade bir rapor yaz (markdown, en fazla ~350 kelime):
1. Bugün ne oldu (her bot için 2-3 cümle, rakamlarla).
2. Komisyon/spread'in kâra etkisi.
3. Neyin işe yaradığı / yaramadığı (örnekleme yetersizse açıkça söyle; birkaç günlük veri anlamlı değildir).
4. En fazla 2 somut ayar önerisi (config.yaml'daki isimlerle) ve neden. Emin değilsen "henüz değiştirme" de.
5. Tek satırlık genel durum: "Gerçek paraya hazır değil" ya da kanıt çok güçlüyse daha olumlu bir ifade.
Asla kesin kazanç vaadi verme; bunun yatırım tavsiyesi olmadığını sonda kısaca belirt."""


def main() -> None:
    cfg, st = load()
    now = dt.datetime.now(IST)
    day_start = int(dt.datetime.combine(now.date(), dt.time(), IST).timestamp() * 1000)
    stats, trades = {}, []
    for name in cfg["bots"]:
        acc = st[name]["account"]
        stats[name] = {"today": paper.stats(acc, day_start), "total": paper.stats(acc),
                       "equity_now": st[name]["equity_curve"][-1][1] if st[name]["equity_curve"] else acc["balance"]}
        trades += [{k: t.get(k) for k in ("symbol", "side", "entry", "exit", "pnl", "costs", "friction",
                                         "reason", "note")} | {"bot": name}
                   for t in acc["trades"] if t["closed_ms"] >= day_start]
    news = [n for n in st.get("gold_news", {}).get("news_history", []) if n["ts"] >= day_start]
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    body = "(Claude anahtarı yok, sadece rakamlar)"
    if key:
        client = anthropic.Anthropic(api_key=key)
        msg = client.messages.create(model=cfg["report"]["model"], max_tokens=1500, messages=[{
            "role": "user", "content": PROMPT.format(
                config=json.dumps(cfg["bots"], ensure_ascii=False), stats=json.dumps(stats, ensure_ascii=False),
                trades=json.dumps(trades[-60:], ensure_ascii=False), news=json.dumps(news, ensure_ascii=False))}])
        body = "".join(getattr(b, "text", "") for b in msg.content)
    second = ""
    if os.environ.get("OPENAI_API_KEY", "").strip():  # independent second opinion from GPT
        try:
            import gpt
            out, used = gpt.ask_json(
                "Sen bağımsız ikinci bir kantitatif analistsin (raporu yazan modelden farklı bir yapay zekâ). "
                "Tek bir JSON nesnesi döndür.",
                "Aşağıda SANAL trading botlarının bugünkü verileri ve başka bir modelin yazdığı rapor var.\n\n"
                f"Ayarlar: {json.dumps(cfg['bots'], ensure_ascii=False)}\n\nİstatistikler: "
                f"{json.dumps(stats, ensure_ascii=False)}\n\nİşlemler: {json.dumps(trades[-60:], ensure_ascii=False)}"
                f"\n\nHaber puanları (Claude ve GPT): {json.dumps(news, ensure_ascii=False)}\n\nRapor:\n{body}\n\n"
                "Raporu bağımsız olarak değerlendir. JSON: {\"katiliyor_mu\": \"evet|kısmen|hayır\", "
                "\"itirazlar\": [\"en fazla 3 madde, Türkçe, rakamlarla\"], \"claude_vs_gpt_haber\": \"iki modelin "
                "haber puanlarının bugün nasıl ayrıştığı/örtüştüğü, 1-2 cümle\", \"oneri\": \"tek cümle\"}",
                cfg["report"].get("gpt_models", ["gpt-6.1-sol"]), max_tokens=1200)
            items = "\n".join(f"- {x}" for x in out.get("itirazlar", []) if x)
            second = (f"\n\n## İkinci görüş (GPT · {used})\n\n**Rapora katılıyor mu:** {out.get('katiliyor_mu', '?')}\n\n"
                      + (f"{items}\n\n" if items else "")
                      + f"**Claude ve GPT haber okuması:** {out.get('claude_vs_gpt_haber', '')}\n\n"
                      f"**Öneri:** {out.get('oneri', '')}\n")
        except Exception as e:  # noqa: BLE001
            second = f"\n\n_(GPT ikinci görüşü alınamadı: {str(e)[:150]})_\n"
    os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
    path = os.path.join(ROOT, "reports", f"{now.date().isoformat()}.md")
    with open(path, "w") as f:
        f.write(f"# Günlük rapor — {now.strftime('%d.%m.%Y')}\n\n")
        for name, s in stats.items():
            f.write(f"- **{name}**: bugün {s['today']['net']:+.2f} $ ({s['today']['trades']} işlem, "
                    f"%{s['today']['win_rate']} kazanma), toplam {s['total']['net']:+.2f} $, "
                    f"hesap {s['equity_now']:,.2f} $\n")
        f.write("\n" + body.strip() + "\n" + second)
    print(f"::notice::Report written: {path}")


if __name__ == "__main__":
    main()
