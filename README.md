# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 04:42 (İstanbul)

## Bot A — Kripto kurallar (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot A2 — Kripto: sert düşüş sonrası toparlanma (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot B1 — Altın + haber (şimdiki ayarlar, TP 5$ / SL 3$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -9.12 $ | -5.30 $ |
| İşlem sayısı | 6 | 7 |
| Kazanma oranı | %33.3 | %42.9 |
| Ödenen komisyon/spread | 14.23 $ | 16.61 $ |

**Hesap değeri: 4,994.70 $** (başlangıç 5,000 $, -5.30 $ / %-0.11)

Son haber analizi (23.10 04:42): puan **-0.40**, güven 0.55 — Altın, petrol fiyatlarındaki sert yükselişin enflasyon ve sıkı para politikası beklentilerini güçlendirmesi nedeniyle iki aylık dibe geriledi; bu, savaş kaynaklı güvenli liman talebinin etkisini bastırıyor. Yeni başlıklardaki İran savaşının yeniden başlayabileceği ihtimali ve Ukrayna gelişmeleri jeopolitik riski sürdürse de piyasa şu an bu riski petrol/faiz kanalı üzerinden fiyatlıyor, bu yüzden kısa vadeli eğilim aşağı yönlü.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 04:37 | PAXGUSDT | short | +3.81 $ | take profit |
| 23.10 04:17 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 03:47 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 03:11 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 02:03 | PAXGUSDT | short | +3.82 $ | take profit |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -11.19 $ | -11.19 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 4,993.05 $** (başlangıç 5,000 $, -6.95 $ / %-0.14)

Açık pozisyonlar: PAXGUSDT short @ 4029.41 (TP 4017.33 / SL 4037.47)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 03:57 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B3 — Altın: B2 + seans filtresi + momentum + kârı koruma

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Son olaylar

```
23.10 03:26 B1  SHORT gold 5000 USD x10 @ 4032.75 (TP 4028.72, SL 4035.17; news -0.45)
23.10 03:36 N  NEWS (6 new) score -0.45 conf 0.60: Petrol fiyatlarının sert yükselişi (Suudi saldırısı sonrası 113 doların üzerine) enflasyon ve sıkı para politikası beklentilerini artırıyor; bu da güvenli liman talebine rağmen altın üzerinde baskı yaratıyor. Altın 2 aylık dibe inerek 4.050 doların altına düştü, momentum belirgin şekilde negatif, ancak düşüş büyük ölçüde zaten fiyatlanmış olabilir.
23.10 03:48 B1  CLOSE short stop: -4.19 USD
23.10 03:48 N  NEWS (7 new) score -0.40 conf 0.60: Petrol fiyatlarındaki sert yükseliş enflasyon ve sıkılaşan Fed beklentileri üzerinden altını baskılıyor; piyasada güvenli liman talebinden çok bu kanal öne çıkıyor ve altın 2 aylık dibe indi. Yeni gelen haberlerde Basra Körfezi'nden daha fazla petrol çıktığı bilgisi petrol baskısını biraz hafifletebileceği için etkisi sınırlı kalıyor; ayrıca bu bilgi çelişkili olduğundan güven orta seviyede tutuldu.
23.10 04:02 N  NEWS (4 new) score -0.20 conf 0.40: Petrol fiyatlarındaki yükseliş enflasyon ve sıkılaşan Fed beklentilerini besleyerek altın üzerinde baskı oluşturuyor; altın iki aylık en düşük seviyeye (4.050 doları altına) geriledi. Yeni gelen haberlerde Basra Körfezi'nden çıkan petrol miktarının savaş öncesinden fazla olması ise petrol baskısını azaltabilir, bu da karışık bir tablo yaratıyor; bu nedenle güven düşük tutuldu.
23.10 04:02 B2  CLOSE short stop: -11.19 USD
23.10 04:12 N  NEWS (2 new) score -0.30 conf 0.45: Petrol fiyatlarındaki yükseliş enflasyon ve sert Fed beklentisi üzerinden altını baskılayıp iki aylık dibe çektiği için kısa vadede negatif görünüyor. Ancak Körfez'den çıkan petrol arzının artması ve bu haberin zaten fiyatlanmış olması, düşüşün bir kısmının tersine dönebileceğini gösterdiği için güven sınırlı kalıyor.
23.10 04:12 B1  SHORT gold 5000 USD x10 @ 4026.32 (TP 4022.30, SL 4028.74; news -0.30)
23.10 04:24 B1  CLOSE short stop: -4.19 USD
23.10 04:24 N  NEWS (10 new) score -0.30 conf 0.50: Petrol fiyatlarının yükselmesi enflasyon ve sıkı para politikası beklentilerini güçlendirip altın üzerinde baskı yaratıyor; altın son saatlerde iki aylık dibe inmiş durumda. Yeni gelen haberler karışık: Houthi saldırıları ve İran savaşının yeniden başlayabileceği ihtimali jeopolitik risk primi getirse de, Hürmüz çevresinden daha fazla petrol çıkışı ve ABD'nin üretimi artırma adımları petrol baskısını azaltabilir.
23.10 04:31 N  NEWS (10 new) score -0.45 conf 0.60: Petrol fiyatlarındaki sert yükseliş (Suudi saldırısı sonrası 113 doların üzerinde) enflasyon ve sıkı para politikası beklentilerini artırarak altın üzerinde baskı yaratıyor; altın zaten iki aylık dip olan 4.050 doların altına indi. Jeopolitik güvenli liman talebi bu baskıyı kısmen dengeliyor, ayrıca Basra Körfezi'nden çıkan petrol miktarının arttığına dair haber fiyat baskısını azaltabilir, bu yüzden güven orta düzeyde.
23.10 04:31 B1  SHORT gold 5000 USD x10 @ 4029.52 (TP 4025.49, SL 4031.94; news -0.45)
23.10 04:31 B2  SHORT gold 5000 USD x10 @ 4029.41 (TP 4017.33, SL 4037.47; news -0.45)
23.10 04:42 B1  CLOSE short take profit: +3.81 USD
23.10 04:42 N  NEWS (3 new) score -0.40 conf 0.55: Altın, petrol fiyatlarındaki sert yükselişin enflasyon ve sıkı para politikası beklentilerini güçlendirmesi nedeniyle iki aylık dibe geriledi; bu, savaş kaynaklı güvenli liman talebinin etkisini bastırıyor. Yeni başlıklardaki İran savaşının yeniden başlayabileceği ihtimali ve Ukrayna gelişmeleri jeopolitik riski sürdürse de piyasa şu an bu riski petrol/faiz kanalı üzerinden fiyatlıyor, bu yüzden kısa vadeli eğilim aşağı yönlü.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
