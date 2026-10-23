# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 06:19 (İstanbul)

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
| Net kâr/zarar | -17.86 $ | -14.05 $ |
| İşlem sayısı | 10 | 11 |
| Kazanma oranı | %30.0 | %36.4 |
| Ödenen komisyon/spread | 23.73 $ | 26.10 $ |

**Hesap değeri: 4,985.95 $** (başlangıç 5,000 $, -14.05 $ / %-0.28)

Son haber analizi (23.10 06:19): puan **-0.50**, güven 0.60 — Altın 3 aylık dip seviyesine geriledi ve haftalık düşüşe gidiyor; petrol fiyatlarındaki yükseliş faiz artırımı beklentilerini besleyerek reel faizler üzerinden altını baskılıyor. Jeopolitik risk-off (İran savaşı, Orta Doğu) bir miktar güvenli liman talebi yaratsa da, piyasada baskın etki hawkish Fed beklentisi ve güçlü dolar/tahvil getirisi yönünde olduğundan net etki negatif.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 06:14 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 05:34 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 05:12 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 04:57 | PAXGUSDT | short | +3.81 $ | take profit |
| 23.10 04:37 | PAXGUSDT | short | +3.81 $ | take profit |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -8.56 $ | -8.56 $ |
| İşlem sayısı | 3 | 3 |
| Kazanma oranı | %33.3 | %33.3 |
| Ödenen komisyon/spread | 7.12 $ | 7.12 $ |

**Hesap değeri: 4,990.25 $** (başlangıç 5,000 $, -9.75 $ / %-0.19)

Açık pozisyonlar: PAXGUSDT short @ 4027.22 (TP 4015.14 / SL 4035.28)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 05:27 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 04:52 | PAXGUSDT | short | +13.82 $ | take profit |
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
23.10 05:10 B2  SHORT gold 5000 USD x10 @ 4023.91 (TP 4011.83, SL 4031.95; news -0.50)
23.10 05:20 B1  CLOSE short stop: -4.19 USD
23.10 05:20 N  NEWS (2 new) score -0.45 conf 0.60: Petrol fiyatlarındaki yükseliş enflasyon ve faiz artışı beklentilerini besleyerek altın için baskı yaratıyor; altın 3 aylık dibe geriledi. Orta Doğu'daki Husi saldırıları jeopolitik risk primi sağlasa da, bu etki petrol kaynaklı faiz endişelerinin gerisinde kalıyor. ABD doları endeksindeki zayıflık (teknoloji kazançları) kısmen destekleyici olsa da, genel tablo negatif.
23.10 05:32 N  NEWS (8 new) score -0.35 conf 0.50: Petrol fiyatlarındaki yükseliş enflasyon ve faiz artırımı beklentilerini besleyerek altın için baskı oluşturuyor; altın 3 aylık dibe geriledi. Jeopolitik risk (İran savaşı, Husi füzesi) güvenli liman talebini destekliyor ama bu etki piyasada büyük ölçüde fiyatlanmış görünüyor. Yeni gelen haberlerin çoğu (Yemen, Murkowski, Dolly Parton vb.) altınla ilgisiz; zayıf ABD doları ise sınırlı destek sağlıyor.
23.10 05:32 B1  SHORT gold 5000 USD x10 @ 4032.37 (TP 4028.34, SL 4034.79; news -0.35)
23.10 05:32 B2  CLOSE short stop: -11.19 USD
23.10 05:42 B1  CLOSE short stop: -4.19 USD
23.10 05:42 N  NEWS (10 new) score -0.45 conf 0.60: Altın 3 aylık dibe geriledi ve haftalık düşüş bekleniyor; petrol fiyatlarındaki yükseliş enflasyon ve faiz artırımı beklentilerini besleyerek altın için baskı yaratıyor. Jeopolitik risk (İran savaşı, Husiler) güvenli liman talebi yaratsa da, piyasada etkili olan kanal petrol-faiz bağlantısı; ayrıca ABD doları teknoloji kazançlarının zayıflığıyla biraz zayıfladı, bu da kısmen destekleyici. Petrolün Basra Körfezi'nden çıkışının artması gibi çelişkili haberler petrol yükselişinin kalıcılığına dair belirsizlik yaratıyor, bu yüzden güveni sınırlı tutuyorum.
23.10 05:48 N  NEWS (11 new) score -0.35 conf 0.50: Petrol fiyatlarındaki yükseliş enflasyon ve faiz artışı beklentilerini besleyerek altın için baskı yaratıyor; altın 3 aylık dip seviyesine gerilemiş durumda. Yeni İran/Husi/Doğu Afrika gerilimi haberleri jeopolitik güvenli liman talebini artırabilir, ancak piyasa tepkisi şu an riskten çok faiz kaygısı yönünde; ABD dolarındaki zayıflık ise sınırlı destek sağlıyor.
23.10 05:58 N  NEWS (28 new) score -0.50 conf 0.60: Altın 3 aylık ve iki aylık dip seviyelerine geriledi; petrol fiyatlarındaki sert yükseliş (Suudi saldırısı, İran riski) enflasyon ve faiz artırımı beklentilerini besleyerek güvenli liman talebini baskılıyor. Dolar ve tahvil getirilerindeki zayıf hareketler kısmen destekleyici olsa da, Fed'in faiz artırımı ihtimali gibi baskın etki altın üzerinde negatif kalıyor.
23.10 06:08 N  NEWS (25 new) score -0.30 conf 0.45: Altın, petrol kaynaklı enflasyon ve Fed'in faiz artırımı/bekleme beklentileri nedeniyle üç aylık dibe yakın ve haftalık düşüş yolunda; bu baskı yeni haberlerle de sürüyor. Dolar endeksinin zayıflaması ve Orta Doğu'daki jeopolitik risk iştahı kısmen destekleyici olsa da, reel faiz ve sıkılaşma beklentileri ağırlıkta olduğu için genel etki hafif negatif.
23.10 06:08 B1  SHORT gold 5000 USD x10 @ 4028.04 (TP 4024.02, SL 4030.46; news -0.30)
23.10 06:19 B1  CLOSE short stop: -4.19 USD
23.10 06:19 N  NEWS (8 new) score -0.50 conf 0.60: Altın 3 aylık dip seviyesine geriledi ve haftalık düşüşe gidiyor; petrol fiyatlarındaki yükseliş faiz artırımı beklentilerini besleyerek reel faizler üzerinden altını baskılıyor. Jeopolitik risk-off (İran savaşı, Orta Doğu) bir miktar güvenli liman talebi yaratsa da, piyasada baskın etki hawkish Fed beklentisi ve güçlü dolar/tahvil getirisi yönünde olduğundan net etki negatif.
23.10 06:19 B2  SHORT gold 5000 USD x10 @ 4027.22 (TP 4015.14, SL 4035.28; news -0.50)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
