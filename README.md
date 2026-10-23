# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 04:12 (İstanbul)

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
| Net kâr/zarar | -8.74 $ | -4.93 $ |
| İşlem sayısı | 4 | 5 |
| Kazanma oranı | %25.0 | %40.0 |
| Ödenen komisyon/spread | 9.49 $ | 11.86 $ |

**Hesap değeri: 4,993.88 $** (başlangıç 5,000 $, -6.12 $ / %-0.12)

Açık pozisyonlar: PAXGUSDT short @ 4026.32 (TP 4022.30 / SL 4028.74)

Son haber analizi (23.10 04:12): puan **-0.30**, güven 0.45 — Petrol fiyatlarındaki yükseliş enflasyon ve sert Fed beklentisi üzerinden altını baskılayıp iki aylık dibe çektiği için kısa vadede negatif görünüyor. Ancak Körfez'den çıkan petrol arzının artması ve bu haberin zaten fiyatlanmış olması, düşüşün bir kısmının tersine dönebileceğini gösterdiği için güven sınırlı kalıyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 03:47 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 03:11 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 02:03 | PAXGUSDT | short | +3.82 $ | take profit |
| 23.10 00:03 | PAXGUSDT | short | -4.19 $ | stop |
| 22.10 23:16 | PAXGUSDT | short | +3.82 $ | take profit |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -11.19 $ | -11.19 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 4,988.81 $** (başlangıç 5,000 $, -11.19 $ / %-0.22)

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
23.10 02:48 N  NEWS (9 new) score -0.40 conf 0.60: Petrol fiyatlarının yükselmesi (Suudi saldırısı, Hürmüz'de tanker saldırıları, Petrol 113$ üzerinde) enflasyon ve sıkı Fed beklentilerini besleyerek altın için baskı yaratıyor; altın iki aylık/11 haftalık dibe geriledi. Jeopolitik risk güvenli liman talebi getirse de piyasa tepkisi şu an satış yönünde, bu nedenle kısa vadede hafif-orta düzeyde negatif görünüm var.
23.10 02:48 B2  SHORT gold 5000 USD x10 @ 4034.81 (TP 4022.71, SL 4042.88; news -0.40)
23.10 02:58 N  NEWS (5 new) score -0.50 conf 0.60: Petrol fiyatlarının 113 doların üzerine çıkması enflasyon ve sıkı para politikası beklentilerini canlandırarak altı baskılıyor; altın 4.050 doların altına inip iki aylık dip görmüş durumda. Iran savaşı ve Hürmüz'deki tanker saldırıları güvenli liman talebini artırması gereken bir unsur olsa da, piyasada şu an bu etki görülmüyor; bu yüzden düşüş eğilimi baskın kabul edildi ve güven orta düzeyde tutuldu.
23.10 03:03 N  NEWS (3 new) score -0.45 conf 0.60: Petrol 113 doların üzerine fırladı ve bu enflasyon ile sıkı para politikası beklentilerini canlandırarak altı baskılıyor; altın iki aylık ve 11 haftalık dip seviyelerine geriledi. Jeopolitik risk (İran, Hürmüz) güvenli liman talebini desteklemesi gerektiği halde piyasa tepkisi altın aleyhine çalışıyor; Putin'in barış görüşmelerine hazır olduğu haberi de jeopolitik primi biraz zayıflatıyor.
23.10 03:14 B1  CLOSE short stop: -4.19 USD
23.10 03:14 N  NEWS (10 new) score -0.30 conf 0.50: 
23.10 03:26 N  NEWS (6 new) score -0.45 conf 0.60: Petrol fiyatlarının 113 doların üzerine fırlaması enflasyon ve sıkı para politikası beklentilerini canlandırarak altı baskılıyor; altın iki aylık dip olan 4.050 doların altına indi ve satış baskısı sürüyor. Rusya'nın yeni füze saldırıları ve İran savaşına ilişkin jeopolitik gerilim güvenli liman talebini destekleyebilir, ancak bu etki mevcut satışı dengelemekte yetersiz kalıyor; tahvil getirilerindeki yükseliş de bu tabloyu destekliyor.
23.10 03:26 B1  SHORT gold 5000 USD x10 @ 4032.75 (TP 4028.72, SL 4035.17; news -0.45)
23.10 03:36 N  NEWS (6 new) score -0.45 conf 0.60: Petrol fiyatlarının sert yükselişi (Suudi saldırısı sonrası 113 doların üzerine) enflasyon ve sıkı para politikası beklentilerini artırıyor; bu da güvenli liman talebine rağmen altın üzerinde baskı yaratıyor. Altın 2 aylık dibe inerek 4.050 doların altına düştü, momentum belirgin şekilde negatif, ancak düşüş büyük ölçüde zaten fiyatlanmış olabilir.
23.10 03:48 B1  CLOSE short stop: -4.19 USD
23.10 03:48 N  NEWS (7 new) score -0.40 conf 0.60: Petrol fiyatlarındaki sert yükseliş enflasyon ve sıkılaşan Fed beklentileri üzerinden altını baskılıyor; piyasada güvenli liman talebinden çok bu kanal öne çıkıyor ve altın 2 aylık dibe indi. Yeni gelen haberlerde Basra Körfezi'nden daha fazla petrol çıktığı bilgisi petrol baskısını biraz hafifletebileceği için etkisi sınırlı kalıyor; ayrıca bu bilgi çelişkili olduğundan güven orta seviyede tutuldu.
23.10 04:02 N  NEWS (4 new) score -0.20 conf 0.40: Petrol fiyatlarındaki yükseliş enflasyon ve sıkılaşan Fed beklentilerini besleyerek altın üzerinde baskı oluşturuyor; altın iki aylık en düşük seviyeye (4.050 doları altına) geriledi. Yeni gelen haberlerde Basra Körfezi'nden çıkan petrol miktarının savaş öncesinden fazla olması ise petrol baskısını azaltabilir, bu da karışık bir tablo yaratıyor; bu nedenle güven düşük tutuldu.
23.10 04:02 B2  CLOSE short stop: -11.19 USD
23.10 04:12 N  NEWS (2 new) score -0.30 conf 0.45: Petrol fiyatlarındaki yükseliş enflasyon ve sert Fed beklentisi üzerinden altını baskılayıp iki aylık dibe çektiği için kısa vadede negatif görünüyor. Ancak Körfez'den çıkan petrol arzının artması ve bu haberin zaten fiyatlanmış olması, düşüşün bir kısmının tersine dönebileceğini gösterdiği için güven sınırlı kalıyor.
23.10 04:12 B1  SHORT gold 5000 USD x10 @ 4026.32 (TP 4022.30, SL 4028.74; news -0.30)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
