# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 17.11.2026 14:16 (İstanbul)

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

Son haber analizi (17.11 14:10): Claude puan **-0.40**, güven 0.60 — Piyasadaki baskın etki Fed'in art arda faiz artırımı beklentisi ve doların 19 aylık zirvesi nedeniyle altı aşağı yönlü baskılıyor. Orta Doğu'daki savaş ve İran'a bağlı gelişmeler (Bahreyn'de insansız hava aracı saldırısı) güvenli liman talebini destekliyor olsa da bu etki hawkish Fed ve güçlü dolar baskısının gerisinde kalıyor.

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
17.11 12:45 N  NEWS (4 new) score -0.40 conf 0.60: Dolar endeksi 19 aylık zirveye yakın ve sıcak CPI sonrası güçleniyor; bu, faiz beklentileri ve güçlü dolar nedeniyle altın için baskı yaratıyor. Ukrayna'nın Kırım köprüsüne saldırısı ve İran savaşı jeopolitik risk üretse de altının jeopolitik talebi bu haberlerde belirgin bir yükseliş göstermiyor, bu yüzden etki sınırlı kalabilir.
17.11 12:57 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 12:57 N  NEWS (10 new) score -0.40 conf 0.50: Dolar 19 aylık zirvesine yakın (DXY ~103,5) ve yüksek faizler altını baskılıyor; altın yaklaşık 3.830-3.870 dolarda yıllık dip bölgesinde. Jeopolitik tarafta İran savaşının sona yaklaştığına dair haberler (Vance, petrol fiyatlarında düşüş) güvenli liman talebini zayıflatıyor, Ukrayna-Kırım köprüsü saldırısı ise etkisi sınırlı kalabilir; Fed tutanakları öncesi hawkish risk de sürüyor.
17.11 13:09 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 13:09 N  NEWS (14 new) score -0.25 conf 0.50: Dolar endeksi 19 aylık zirveye yakın seyrediyor ve altın 3.830-3.870 dolar bandında baskı altında; yüksek faiz ve güçlü dolar altını aşağı çekiyor. Yeni jeopolitik haberler (Ukrayna'nın Kırım köprüsüne saldırısı, İran savaşı) güvenli liman talebini destekliyor olsa da, Vance'in İran savaşının uzamayacağı yönündeki açıklaması ve petrol fiyatlarındaki düşüş enflasyon ve faiz beklentileri açısından nötr-dovish bir sinyal olarak okunabilir; bu nedenle etki sınırlı ve karışık.
17.11 13:21 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 13:21 N  NEWS (8 new) score -0.30 conf 0.50: Güçlü dolar (DXY 19 aylık zirveye yakın, 103.5 direnci) ve yüksek reel faiz beklentileri altın üzerinde baskı oluşturuyor; altın 3830-3870 bandında ve sert satış sonrası kısmi toparlanma sinyali veriyor. Iran savaşı ve Ukrayna'daki gelişmeler güvenli liman talebini artırmadığı için jeopolitik etkisi sınırlı; yakın vadede Fed tutanakları ve ABD piyasa verileri belirleyici olacak.
17.11 13:33 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 13:33 N  NEWS (15 new) score -0.35 conf 0.50: 
17.11 13:46 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 13:46 N  NEWS (9 new) score -0.40 conf 0.60: Dolar 19 aylık zirvesine çıkıyor ve piyasalar Fed'in sıkı duruşuna dair bahisler yapıyor; bu, reel faiz beklentilerini yükselterek altın için baskı oluşturuyor. Kırım Köprüsü'ndeki saldırı ve İran savaşının sürmesi güvenli liman talebini bir miktar destekleyebilir, ancak bu haberlerin etkisi sınırlı ve Alman yatırımcı güveninin yükselmesi risk iştahını artırıyor. Genel tablo altın için olumsuz, ancak haber akışında çelişkili unsurlar olduğu için güven orta düzeyde.
17.11 13:58 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 13:58 N  NEWS (12 new) score -0.35 conf 0.50: Doların 19 aylık zirveye çıkması ve Fed'e yönelik şahin beklentiler altın için baskı oluşturuyor. İran savaşı ve jeopolitik gerilim başlıkları güvenli liman talebini destekleyebilir, ancak bu haberler büyük ölçüde fiyatlanmış görünüyor ve Almanya'da yatırımcı güveninin yükselmesi risk iştahını artırıyor.
17.11 14:10 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 14:10 N  NEWS (12 new) score -0.40 conf 0.60: Piyasadaki baskın etki Fed'in art arda faiz artırımı beklentisi ve doların 19 aylık zirvesi nedeniyle altı aşağı yönlü baskılıyor. Orta Doğu'daki savaş ve İran'a bağlı gelişmeler (Bahreyn'de insansız hava aracı saldırısı) güvenli liman talebini destekliyor olsa da bu etki hawkish Fed ve güçlü dolar baskısının gerisinde kalıyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
