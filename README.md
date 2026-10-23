# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 05:10 (İstanbul)

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
| Net kâr/zarar | -5.30 $ | -1.49 $ |
| İşlem sayısı | 7 | 8 |
| Kazanma oranı | %42.9 | %50.0 |
| Ödenen komisyon/spread | 16.61 $ | 18.98 $ |

**Hesap değeri: 4,997.31 $** (başlangıç 5,000 $, -2.69 $ / %-0.05)

Açık pozisyonlar: PAXGUSDT short @ 4023.90 (TP 4019.87 / SL 4026.31)

Son haber analizi (23.10 05:10): puan **-0.50**, güven 0.60 — Petrol fiyatlarındaki yükseliş enflasyon ve faiz indirimi beklentilerini baskılayarak altın üzerinde baskı yaratıyor; altın 3 aylık dip seviyesine geriledi ve haftalık düşüş yönünde. Dolar endeksindeki zayıflama ve Orta Doğu'daki jeopolitik risk (Houthi füzesi) destekleyici olsa da bu etkiler faiz kaynaklı satış baskısının gerisinde kalıyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 04:57 | PAXGUSDT | short | +3.81 $ | take profit |
| 23.10 04:37 | PAXGUSDT | short | +3.81 $ | take profit |
| 23.10 04:17 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 03:47 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 03:11 | PAXGUSDT | short | -4.19 $ | stop |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +2.63 $ | +2.63 $ |
| İşlem sayısı | 2 | 2 |
| Kazanma oranı | %50.0 | %50.0 |
| Ödenen komisyon/spread | 4.74 $ | 4.74 $ |

**Hesap değeri: 5,001.44 $** (başlangıç 5,000 $, +1.44 $ / %+0.03)

Açık pozisyonlar: PAXGUSDT short @ 4023.91 (TP 4011.83 / SL 4031.95)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
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
23.10 04:24 B1  CLOSE short stop: -4.19 USD
23.10 04:24 N  NEWS (10 new) score -0.30 conf 0.50: Petrol fiyatlarının yükselmesi enflasyon ve sıkı para politikası beklentilerini güçlendirip altın üzerinde baskı yaratıyor; altın son saatlerde iki aylık dibe inmiş durumda. Yeni gelen haberler karışık: Houthi saldırıları ve İran savaşının yeniden başlayabileceği ihtimali jeopolitik risk primi getirse de, Hürmüz çevresinden daha fazla petrol çıkışı ve ABD'nin üretimi artırma adımları petrol baskısını azaltabilir.
23.10 04:31 N  NEWS (10 new) score -0.45 conf 0.60: Petrol fiyatlarındaki sert yükseliş (Suudi saldırısı sonrası 113 doların üzerinde) enflasyon ve sıkı para politikası beklentilerini artırarak altın üzerinde baskı yaratıyor; altın zaten iki aylık dip olan 4.050 doların altına indi. Jeopolitik güvenli liman talebi bu baskıyı kısmen dengeliyor, ayrıca Basra Körfezi'nden çıkan petrol miktarının arttığına dair haber fiyat baskısını azaltabilir, bu yüzden güven orta düzeyde.
23.10 04:31 B1  SHORT gold 5000 USD x10 @ 4029.52 (TP 4025.49, SL 4031.94; news -0.45)
23.10 04:31 B2  SHORT gold 5000 USD x10 @ 4029.41 (TP 4017.33, SL 4037.47; news -0.45)
23.10 04:42 B1  CLOSE short take profit: +3.81 USD
23.10 04:42 N  NEWS (3 new) score -0.40 conf 0.55: Altın, petrol fiyatlarındaki sert yükselişin enflasyon ve sıkı para politikası beklentilerini güçlendirmesi nedeniyle iki aylık dibe geriledi; bu, savaş kaynaklı güvenli liman talebinin etkisini bastırıyor. Yeni başlıklardaki İran savaşının yeniden başlayabileceği ihtimali ve Ukrayna gelişmeleri jeopolitik riski sürdürse de piyasa şu an bu riski petrol/faiz kanalı üzerinden fiyatlıyor, bu yüzden kısa vadeli eğilim aşağı yönlü.
23.10 04:54 N  NEWS (13 new) score -0.30 conf 0.45: Petrol fiyatlarındaki sert yükseliş enflasyon ve sıkı para politikası beklentilerini güçlendirip altın üzerinde baskı yaratıyor; tahvil getirilerinin yükselişi ve altının iki aylık dibe inmesi de bu yönü destekliyor. Ancak Orta Doğu jeopolitik riski güvenli liman talebini artırabilir ve dolar zayıflığı altını destekleyebilir, bu yüzden güven orta düzeyde tutuldu.
23.10 04:54 B1  SHORT gold 5000 USD x10 @ 4014.84 (TP 4010.82, SL 4017.25; news -0.30)
23.10 04:54 B2  CLOSE short take profit: +13.82 USD
23.10 05:04 B1  CLOSE short take profit: +3.81 USD
23.10 05:04 N  NEWS (8 new) score +0.10 conf 0.35: 
23.10 05:10 N  NEWS (7 new) score -0.50 conf 0.60: Petrol fiyatlarındaki yükseliş enflasyon ve faiz indirimi beklentilerini baskılayarak altın üzerinde baskı yaratıyor; altın 3 aylık dip seviyesine geriledi ve haftalık düşüş yönünde. Dolar endeksindeki zayıflama ve Orta Doğu'daki jeopolitik risk (Houthi füzesi) destekleyici olsa da bu etkiler faiz kaynaklı satış baskısının gerisinde kalıyor.
23.10 05:10 B1  SHORT gold 5000 USD x10 @ 4023.90 (TP 4019.87, SL 4026.31; news -0.50)
23.10 05:10 B2  SHORT gold 5000 USD x10 @ 4023.91 (TP 4011.83, SL 4031.95; news -0.50)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
