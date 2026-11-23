# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.11.2026 07:35 (İstanbul)

## Bot A — Kripto 1 saatlik trend (x1)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +104.97 $ |
| İşlem sayısı | 0 | 2 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 3.25 $ |

**Hesap değeri: 5,104.97 $** (başlangıç 5,000 $, +104.97 $ / %+2.10)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 20.11 04:03 | SOLUSDT | short | +37.10 $ | time limit |
| 19.11 01:49 | XRPUSDT | short | +67.87 $ | take profit |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +297.35 $ |
| İşlem sayısı | 0 | 193 |
| Kazanma oranı | %0.0 | %46.1 |
| Ödenen komisyon/spread | 0.00 $ | 2307.16 $ |

**Hesap değeri: 5,297.35 $** (başlangıç 5,000 $, +297.35 $ / %+5.95)

Son haber analizi (23.11 07:33): Claude puan **-0.10**, güven 0.40 — Fed Aralık ayında faiz artırımı olasılığının %90'ın üzerine çıkması ve dolar endeksinin 19 aylık zirveye yakın seyretmesi altın için baskı yaratıyor. Buna karşılık dolardaki gevşeme, 14 aylık dibinden toparlanma ve İran kaynaklı jeopolitik risklerin sürmesi kısa vadede destek sağlıyor; başlıklar çelişkili olduğu için sinyal zayıf ve güven düşük.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 20.11 19:13 | PAXGUSDT | short | -56.07 $ | stop |
| 20.11 19:02 | PAXGUSDT | short | +68.96 $ | take profit |
| 20.11 18:37 | PAXGUSDT | short | -56.07 $ | stop |
| 20.11 18:28 | PAXGUSDT | short | +68.95 $ | take profit |
| 20.11 17:53 | PAXGUSDT | short | +68.97 $ | take profit |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -123.04 $ |
| İşlem sayısı | 0 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 0.00 $ | 70.51 $ |

**Hesap değeri: 4,876.96 $** (başlangıç 5,000 $, -123.04 $ / %-2.46)

Son haber analizi (18.11 11:41): Claude puan **+0.30**, güven 0.40 — Hürmüz Boğazı'nda ADNOC gemisinin vurulması ve gaz tankerine isabet gibi yeni saldırılar, ayrıca ABD'nin İran adasını vurması ve Bahreyn/Kuwait'e dronlar, arz riski primini yukarı çekebilir. Buna karşılık Brent'in 100 doların altına inmesi, fazla arz ve bozulan fiyat yapısı (backwardation, zayıf motorin) gibi baskılayıcı haberler piyasada zaten fiyatlanmış görünüyor; bu nedenle net etki hafif yukarı yönlü ama belirsiz.

GPT (gpt-6-luna): puan **+0.58**, güven 0.68 — Hürmüz Boğazı’nda ADNOC bağlantılı gemiye saldırı, can kaybı ve başka bir tanker hasarı haberleri yakın vadeli arz kesintisi risk primini artırıyor. Ancak arz fazlası endişeleri ve petrolün 100 doların altına indiğine dair haberler yükselişi sınırlayabilir.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 10.11 08:01 | BZ=F | short | -67.46 $ | stop (gap) |
| 06.11 22:41 | BZ=F | long | -63.26 $ | stop (gap) |
| 06.11 08:11 | BZ=F | long | -58.75 $ | stop |
| 02.11 23:09 | BZ=F | short | +66.43 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +25414.95 $ |
| İşlem sayısı | 0 | 79 |
| Kazanma oranı | %0.0 | %53.2 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 128,183.18 $** (başlangıç 100,000 $, +28183.18 $ / %+28.18)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 20.11 23:45 | AAPL | short | +1408.47 $ | seans sonu |
| 20.11 23:32 | SPY | short | +1844.50 $ | take profit |
| 20.11 23:26 | QQQ | short | +1847.34 $ | take profit |
| 20.11 20:02 | QQQ | short | +1793.08 $ | take profit |
| 20.11 19:32 | TSLA | short | +1798.50 $ | take profit |

## Son olaylar

```
23.11 01:50 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
23.11 01:53 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
23.11 01:56 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
23.11 01:59 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
23.11 02:02 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
23.11 02:05 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
23.11 02:08 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
23.11 02:11 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
23.11 02:14 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
23.11 02:17 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
23.11 02:20 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
23.11 07:02 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 07:02 N  NEWS (11 new) score +0.05 conf 0.30: Yeni başlıkların çoğu altın fiyatını doğrudan etkileyecek nitelikte değil. Rusya-Ukrayna saldırıları ve Libya'daki Rus gemisi patlaması sürmekte olan, büyük ölçüde fiyatlanmış jeopolitik gerilimler; Fed, reel faiz veya doların hareketine dair yeni bir bilgi yok. Bu nedenle etki hafif pozitif (güvenli liman) yönlü ama çok zayıf ve güven düşük.
23.11 07:33 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 07:33 N  NEWS (44 new) score -0.10 conf 0.40: Fed Aralık ayında faiz artırımı olasılığının %90'ın üzerine çıkması ve dolar endeksinin 19 aylık zirveye yakın seyretmesi altın için baskı yaratıyor. Buna karşılık dolardaki gevşeme, 14 aylık dibinden toparlanma ve İran kaynaklı jeopolitik risklerin sürmesi kısa vadede destek sağlıyor; başlıklar çelişkili olduğu için sinyal zayıf ve güven düşük.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
