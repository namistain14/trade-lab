# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 17.11.2026 08:48 (İstanbul)

## Bot A — Kripto 1 saatlik trend (x1)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -454.74 $ |
| İşlem sayısı | 0 | 113 |
| Kazanma oranı | %0.0 | %41.6 |
| Ödenen komisyon/spread | 0.00 $ | 1342.67 $ |

**Hesap değeri: 4,545.26 $** (başlangıç 5,000 $, -454.74 $ / %-9.09)

Son haber analizi (17.11 08:42): Claude puan **-0.35**, güven 0.50 — Altın, güçlü dolar ve Fed faiz artırımı beklentileri nedeniyle yıllık dip seviyelere yakın işlem görüyor; bu baskı ana eğilimi aşağı yönlü tutuyor. Yeni gelen İran'da "sonsuz savaş" olasılığının reddi ve petrol fiyatlarındaki düşüş jeopolitik risk primini ve enflasyon korkusunu azaltarak kısmen destekleyici olabilir, ancak haberlerin çoğu eski veya fiyatlanmış olduğu için etkisi sınırlı.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 13.11 19:25 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 18:39 | PAXGUSDT | short | +69.05 $ | take profit |
| 13.11 17:32 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 16:56 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 16:31 | PAXGUSDT | short | -55.98 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -123.04 $ |
| İşlem sayısı | 0 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 0.00 $ | 70.51 $ |

**Hesap değeri: 4,876.96 $** (başlangıç 5,000 $, -123.04 $ / %-2.46)

Son haber analizi (17.11 08:00): Claude puan **-0.30**, güven 0.50 — Hormuz'daki tanker saldırıları ve mayın isabeti arz riskini artırıp fiyatı destekliyor, ancak piyasa bunu görmezden gelip Goldman'ın 2027'ye kadar büyük arz fazlası öngörüsü, Hormuz sevkiyatlarının iyileşmesi ve dolar güçlenmesi nedeniyle Brent'i 92 doların altına çekti. Haber akışı net olarak fiyatı aşağı çekiyor, ancak jeopolitik risk yüksek olduğundan güven orta düzeyde.

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
| Net kâr/zarar | +0.00 $ | +11832.47 $ |
| İşlem sayısı | 0 | 48 |
| Kazanma oranı | %0.0 | %52.1 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 114,145.15 $** (başlangıç 100,000 $, +14145.15 $ / %+14.15)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 13.11 23:33 | AAPL | long | -1154.98 $ | stop |
| 13.11 20:09 | TSLA | short | -1169.49 $ | stop |
| 13.11 18:11 | QQQ | short | +1751.13 $ | take profit |
| 13.11 17:37 | NVDA | short | +1722.12 $ | take profit |
| 12.11 23:46 | SPY | long | -466.64 $ | seans sonu |

## Son olaylar

```
17.11 07:53 N  NEWS (44 new) score -0.40 conf 0.60: Dolar endeksi 19 aylık zirveye yakın seyrediyor ve Fed'in faiz artırma beklentileri güçleniyor; bu, reel faiz ve dolar kanalıyla altın üzerinde baskı yaratıyor. İran savaşı ve jeopolitik gerilim güvenli liman talebini destekleyebilir, ancak haberler bu etkiyi sınırlı gösteriyor ve altının YTD dibinden toparlanması kazançları sınırlayan faktör olarak Fed/USD'yi işaret ediyor.
17.11 08:00 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 08:00 B5P  NEWS (45 new) score -0.30 conf 0.50: Hormuz'daki tanker saldırıları ve mayın isabeti arz riskini artırıp fiyatı destekliyor, ancak piyasa bunu görmezden gelip Goldman'ın 2027'ye kadar büyük arz fazlası öngörüsü, Hormuz sevkiyatlarının iyileşmesi ve dolar güçlenmesi nedeniyle Brent'i 92 doların altına çekti. Haber akışı net olarak fiyatı aşağı çekiyor, ancak jeopolitik risk yüksek olduğundan güven orta düzeyde.
17.11 08:02 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
17.11 08:06 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 08:06 N  NEWS (30 new) score -0.75 conf 0.80: Fed faiz artırımı beklentileri ve 19 aylık zirvedeki dolar altını yıllık dip seviyelerine çekiyor; güvenli liman talebini destekleyecek bir jeopolitik şok yok. Çin alımı ve $3,850 destek seviyesi kısa vadede sınırlı bir toparlanma ihtimali bırakıyor, ancak ana yön aşağı.
17.11 08:06 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
17.11 08:08 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
17.11 08:11 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
17.11 08:18 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 08:18 N  NEWS (28 new) score -0.35 conf 0.50: Altın yıllık dip yakınında ve piyasa Fed faiz artırımı beklentileri ile güçlü doların baskısı altında; İran'daki çatışma ve Hormuz'da tanker saldırısı gibi jeopolitik gelişmelere rağmen altın bu haberlere güvenli liman talebiyle tepki vermiyor. Bu nedenle kısa vadede (1-4 saat) hafif-orta düzeyde düşüş yönlü bir baskı bekliyorum; ancak haberlerin birçoğu tekrar eden ve fiyatlanmış nitelikte olduğundan güven sınırlı.
17.11 08:30 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 08:30 N  NEWS (4 new) score -0.30 conf 0.50: Altın, Fed faiz artırımı beklentileri ve güçlü doların baskısı altında yıllık dip seviyelerinde işlem görüyor; haberlerde jeopolitik gerilim (İran, Kiev köprüleri, üçüncü ABD uçak gemisi) artmasına rağmen güvenli liman talebinin fiyatı desteklediğine dair bir işaret yok. Bu nedenle kısa vadede hafif negatif bir görünüm var, ancak yeni gelen haberlerin çoğu zaten fiyatlanmış ve çelişkili olduğu için güven orta düzeyde.
17.11 08:42 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 08:42 N  NEWS (8 new) score -0.35 conf 0.50: Altın, güçlü dolar ve Fed faiz artırımı beklentileri nedeniyle yıllık dip seviyelere yakın işlem görüyor; bu baskı ana eğilimi aşağı yönlü tutuyor. Yeni gelen İran'da "sonsuz savaş" olasılığının reddi ve petrol fiyatlarındaki düşüş jeopolitik risk primini ve enflasyon korkusunu azaltarak kısmen destekleyici olabilir, ancak haberlerin çoğu eski veya fiyatlanmış olduğu için etkisi sınırlı.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
