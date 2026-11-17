# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 17.11.2026 13:33 (İstanbul)

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

Son haber analizi (17.11 13:33): Claude puan **-0.35**, güven 0.50 — Güçlü dolar (DXY 19 aylık zirveye yakın, 103.5 direnci) ve yüksek reel faiz beklentileri altın üzerinde baskı oluşturuyor; altın 3830-3870 bandında ve sert satış sonrası kısmi toparlanma sinyali veriyor. Iran savaşı ve Ukrayna'daki gelişmeler güvenli liman talebini artırmadığı için jeopolitik etkisi sınırlı; yakın vadede Fed tutanakları ve ABD piyasa verileri belirleyici olacak.

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
17.11 12:09 N  NEWS (7 new) score -0.20 conf 0.40: Dolar endeksi 19 aylık zirveden geri çekilse de güçlü dolar momentumu ve ING'nin "güçlü momentum" değerlendirmesi altın için baskı oluşturuyor. İran savaşı ve Ukrayna'daki saldırılar güvenli liman talebini destekliyor, ancak Vance'in "sonsuz savaş olmayacak" açıklaması jeopolitik primi sınırlıyor; altın ise yıllık dip yakınında değer bölgesini test ediyor. Haberlerin büyük kısmı zaten fiyatlanmış veya karışık olduğu için sinyal zayıf.
17.11 12:21 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 12:21 N  NEWS (6 new) score -0.35 conf 0.50: Altın yıllık en düşük seviyeye yakın konsolide oluyor ve güçlü ABD doları (DXY 19 aylık zirvesine yakın) yukarı yönlü hareketi sınırlıyor; Fed tutanakları öncesi bu baskı sürebilir. Jeopolitik gerilim (İran savaşı, Ukrayna-Kırım köprü saldırıları) güvenli liman talebi yaratmadığı için destek sağlamıyor, bu nedenle sinyal ağırlıklı olarak negatif; ancak haberlerin çoğu tekrar niteliğinde ve fiyatlanmış olabileceğinden güven orta düzeyde.
17.11 12:33 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 12:33 N  NEWS (9 new) score -0.35 conf 0.50: Altın yıllık dip yakınında ve güçlü dolar (DXY 19 aylık zirveye yakın) altını baskılıyor; sıcak CPI verisi Fed'in sıkı kalacağı beklentisini güçlendirip reel faizleri yukarı itiyor. Ukrayna-Rusya ve İran savaşına dair jeopolitik gerilim güvenli liman talebi yaratabilir, ancak bu etki dolar ve faiz baskısının gerisinde kalıyor; ayrıca bu haberlerin çoğu zaten fiyatlanmış durumda.
17.11 12:45 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 12:45 N  NEWS (4 new) score -0.40 conf 0.60: Dolar endeksi 19 aylık zirveye yakın ve sıcak CPI sonrası güçleniyor; bu, faiz beklentileri ve güçlü dolar nedeniyle altın için baskı yaratıyor. Ukrayna'nın Kırım köprüsüne saldırısı ve İran savaşı jeopolitik risk üretse de altının jeopolitik talebi bu haberlerde belirgin bir yükseliş göstermiyor, bu yüzden etki sınırlı kalabilir.
17.11 12:57 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 12:57 N  NEWS (10 new) score -0.40 conf 0.50: Dolar 19 aylık zirvesine yakın (DXY ~103,5) ve yüksek faizler altını baskılıyor; altın yaklaşık 3.830-3.870 dolarda yıllık dip bölgesinde. Jeopolitik tarafta İran savaşının sona yaklaştığına dair haberler (Vance, petrol fiyatlarında düşüş) güvenli liman talebini zayıflatıyor, Ukrayna-Kırım köprüsü saldırısı ise etkisi sınırlı kalabilir; Fed tutanakları öncesi hawkish risk de sürüyor.
17.11 13:09 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 13:09 N  NEWS (14 new) score -0.25 conf 0.50: Dolar endeksi 19 aylık zirveye yakın seyrediyor ve altın 3.830-3.870 dolar bandında baskı altında; yüksek faiz ve güçlü dolar altını aşağı çekiyor. Yeni jeopolitik haberler (Ukrayna'nın Kırım köprüsüne saldırısı, İran savaşı) güvenli liman talebini destekliyor olsa da, Vance'in İran savaşının uzamayacağı yönündeki açıklaması ve petrol fiyatlarındaki düşüş enflasyon ve faiz beklentileri açısından nötr-dovish bir sinyal olarak okunabilir; bu nedenle etki sınırlı ve karışık.
17.11 13:21 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 13:21 N  NEWS (8 new) score -0.30 conf 0.50: Güçlü dolar (DXY 19 aylık zirveye yakın, 103.5 direnci) ve yüksek reel faiz beklentileri altın üzerinde baskı oluşturuyor; altın 3830-3870 bandında ve sert satış sonrası kısmi toparlanma sinyali veriyor. Iran savaşı ve Ukrayna'daki gelişmeler güvenli liman talebini artırmadığı için jeopolitik etkisi sınırlı; yakın vadede Fed tutanakları ve ABD piyasa verileri belirleyici olacak.
17.11 13:33 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 13:33 N  NEWS (15 new) score -0.35 conf 0.50: 
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
