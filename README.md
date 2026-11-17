# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 18.11.2026 01:02 (İstanbul)

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
| Net kâr/zarar | +0.00 $ | -510.70 $ |
| İşlem sayısı | 0 | 114 |
| Kazanma oranı | %0.0 | %41.2 |
| Ödenen komisyon/spread | 0.00 $ | 1354.61 $ |

**Hesap değeri: 4,508.03 $** (başlangıç 5,000 $, -491.97 $ / %-9.84)

Açık pozisyonlar: PAXGUSDT short @ 3845.81 (TP 3834.27 / SL 3853.50)

Son haber analizi (18.11 01:02): Claude puan **-0.05**, güven 0.35 — İran ile ABD arasındaki çatışmanın tırmanması (Qeshm Adası'na ABD saldırıları ve Bahreyn üssüne yönelik hedefleme) jeopolitik risk ve güvenli liman talebini artırarak altı kısa vadede destekliyor. Ancak FXEmpire'ın güçlü dolar ve faiz artırımı beklentilerine dair notu ile Fed'in Williams'ın "ani faiz hamlesi gerekmiyor" açıklaması karışık sinyaller veriyor; bu nedenle etki sınırlı ve yönü belirsiz.

GPT (gpt-6-luna): puan **+0.12**, güven 0.39 — İran’daki çatışma ve ABD’nin füze tesisine yönelik saldırısı kısa vadede güvenli liman talebini destekleyebilir. Ancak daha güçlü ABD büyüme beklentisi ve Fed’den ek faiz artışı sinyalleri altını baskılayabilir; etkiler bu nedenle dengeli ve belirsiz.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 17.11 21:41 | PAXGUSDT | long | -55.96 $ | stop |
| 13.11 19:25 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 18:39 | PAXGUSDT | short | +69.05 $ | take profit |
| 13.11 17:32 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 16:56 | PAXGUSDT | short | -55.98 $ | stop |

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
| Net kâr/zarar | +0.00 $ | +9928.18 $ |
| İşlem sayısı | 0 | 51 |
| Kazanma oranı | %0.0 | %49.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 112,393.69 $** (başlangıç 100,000 $, +12393.69 $ / %+12.39)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 17.11 23:46 | TSLA | long | -435.97 $ | seans sonu |
| 17.11 23:46 | QQQ | long | -307.07 $ | seans sonu |
| 17.11 22:51 | NVDA | long | -1161.25 $ | stop |
| 13.11 23:33 | AAPL | long | -1154.98 $ | stop |
| 13.11 20:09 | TSLA | short | -1169.49 $ | stop |

## Son olaylar

```
17.11 23:46 B6  CLOSE long QQQ seans sonu: -307.07 USD
17.11 23:46 B6  CLOSE long TSLA seans sonu: -435.97 USD
17.11 23:46 B6  seans kapanışı: tüm pozisyonlar kapatıldı
18.11 00:01 N  NEWS (45 new) score -0.10 conf 0.40: İran'a yönelik ABD saldırıları jeopolitik risk primini destekleyerek altı hafif yukarı çekebilir, ancak İran savaşı zaten uzun süredir fiyatlanmış durumda. Fed'in Williams'ın sıkılaştırmadan yana olduğunu söylemesi ve doların güçlü seyri altın üzerinde baskı yaratabilir; bu nedenle net etki hafif negatif, güven düşük.
18.11 00:01 N  GPT  score +0.35 conf 0.58: İran’daki füze sahasına yönelik ABD saldırısı bölgesel gerilim ve güvenli liman talebini artırarak altını kısa vadede destekleyebilir. Ancak Fed’den gelen temkinli-şahin mesajlar ve doların güçlü seyri yükselişi sınırlıyor; yinelenen haberler ek etkiyi belirsiz kılıyor.
18.11 00:14 N  NEWS (10 new) score +0.05 conf 0.35: ABD'nin İran'ın Qeshm Adası'ndaki füze sahasına yönelik saldırısı güvenli liman talebini kısa vadede hafif destekliyor. Ancak Fed'in Williams'ın sıkılaştırmadan yana olduğunu, ama "dramatik adım" gerekmediğini söylemesi ve doların güçlü seyri altın üzerinde baskı yaratabileceği için etki sınırlı kalıyor; genel tablo nötre yakın.
18.11 00:14 N  GPT  score +0.45 conf 0.59: ABD’nin İran’daki IRGC füze sahasına saldırısı ve Netanyahu’nun tehdit açıklamaları kısa vadede güvenli liman talebini destekleyebilir. Fed’den Williams’ın sıkı politika yanlısı duruşu yükselişi sınırlarken, savaş haberlerinin bir kısmı zaten fiyatlanmış olabilir.
18.11 00:26 N  NEWS (13 new) score -0.05 conf 0.35: İran savaşının sürmesi ve ABD'nin Qeshm Adası'na yönelik yeni saldırıları jeopolitik risk nedeniyle altı destekliyor, ancak bu gelişmeler büyük ölçüde fiyatlanmış durumda. Buna karşılık 10 yıllık tahvil getirisinin %5'e yaklaşması ve Fed'li Williams'ın hâlâ sıkılaştırmayı savunması reel faiz ve dolar tarafında altı baskılıyor; bu nedenle net etki hafif negatif.
18.11 00:26 N  GPT  score -0.15 conf 0.46: ABD 10 yıllık tahvil getirisinin %5’in üzerine çıkma beklentisi ve Fed’den gelen sıkılaşmacı mesajlar altın üzerinde baskı yaratabilir. İran’daki çatışmanın sürmesi ve yeni İsrail yaptırımları güvenli liman talebini desteklese de kısa vadeli net etki hafif negatif görünüyor.
18.11 00:38 N  NEWS (12 new) score +0.15 conf 0.35: Yeni ABD saldırıları (Kum Adası/Qeshm'deki İran füze sahası) jeopolitik risk ve güvenli liman talebini artırarak altı hafif destekliyor. Ancak FXEmpire başlığındaki güçlü dolar ve faiz artırımı beklentileri altı baskılıyor; savaş haberlerinin büyük kısmı zaten fiyatlanmış olduğu için net etki sınırlı ve karışık.
18.11 00:38 N  GPT  score +0.35 conf 0.52: ABD’nin İran’daki füze tesisine saldırısı ve Bahreyn’deki üs tehdidi kısa vadede güvenli liman talebini artırabilir. Ancak güçlü dolar ve faiz artışı beklentilerine ilişkin haberler altını sınırlayabilir; saldırı haberlerinin tekrarlı olması da ek etkinin belirsizliğini artırıyor.
18.11 00:50 N  NEWS (10 new) score +0.30 conf 0.50: İran ile ABD arasındaki çatışmanın tırmanması (Qeshm Adası'na ABD saldırıları ve Bahreyn üssüne yönelik hedefleme) jeopolitik risk ve güvenli liman talebini artırarak altı kısa vadede destekliyor. Ancak FXEmpire'ın güçlü dolar ve faiz artırımı beklentilerine dair notu ile Fed'in Williams'ın "ani faiz hamlesi gerekmiyor" açıklaması karışık sinyaller veriyor; bu nedenle etki sınırlı ve yönü belirsiz.
18.11 00:50 N  GPT  score +0.42 conf 0.66: ABD’nin İran’daki füze sahasına düzenlediği yeni saldırı ve Bahreyn’deki üsse yönelik saldırı, kısa vadede güvenli liman talebini artırarak altını destekleyebilir. Fed’den Williams’ın «dramatik» bir faiz hamlesine gerek olmadığını söylemesi sınırlı destek sunarken, güçlü dolar ve faiz artışı beklent
18.11 01:02 N  NEWS (8 new) score -0.05 conf 0.35: 
18.11 01:02 N  GPT  score +0.12 conf 0.39: İran’daki çatışma ve ABD’nin füze tesisine yönelik saldırısı kısa vadede güvenli liman talebini destekleyebilir. Ancak daha güçlü ABD büyüme beklentisi ve Fed’den ek faiz artışı sinyalleri altını baskılayabilir; etkiler bu nedenle dengeli ve belirsiz.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
