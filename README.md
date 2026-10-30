# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 20:09 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -217.43 $ | -467.72 $ |
| İşlem sayısı | 14 | 30 |
| Kazanma oranı | %21.4 | %23.3 |
| Ödenen komisyon/spread | 67.51 $ | 137.19 $ |

**Hesap değeri: 4,532.28 $** (başlangıç 5,000 $, -467.72 $ / %-9.35)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 03:19 | SOLUSDT | long | -14.64 $ | stop |
| 30.10 03:19 | ETHUSDT | long | -29.27 $ | stop |
| 30.10 03:19 | BTCUSDT | long | -29.27 $ | stop |
| 30.10 02:47 | XRPUSDT | long | -14.87 $ | stop |
| 30.10 02:47 | SOLUSDT | long | -29.74 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +164.35 $ | +121.55 $ |
| İşlem sayısı | 6 | 9 |
| Kazanma oranı | %66.7 | %55.6 |
| Ödenen komisyon/spread | 71.39 $ | 106.98 $ |

**Hesap değeri: 5,149.01 $** (başlangıç 5,000 $, +149.01 $ / %+2.98)

Açık pozisyonlar: PAXGUSDT short @ 3912.45 (TP 3900.71 / SL 3920.27)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 18:48 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 17:39 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 16:51 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 15:43 | PAXGUSDT | short | +69.07 $ | take profit |
| 30.10 14:25 | PAXGUSDT | short | +69.08 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 102,062.99 $** (başlangıç 100,000 $, +2062.99 $ / %+2.06)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
30.10 18:26 N  NEWS (36 new) score -0.20 conf 0.40: 
30.10 18:26 N  GPT  score -0.65 conf 0.72: Altının yüzde 3 düşerek 3.900 doların altına inmesi ve satışların likidasyonla derinleşmesi kısa vadeli aşağı yönlü momentumu güçlendiriyor; Trump’ın İran savaşının yakında bitebileceği açıklaması da güvenli liman talebini azaltabilir. Dolar ve tahvil getirilerindeki gerileme düşüşü sınırlasa da enf
30.10 18:26 B5  SHORT gold 25000 USD x10 @ 3924.06 (TP 3912.28, SL 3931.90; news -0.43)
30.10 18:26 B6  karar turu: Claude «Büyüme ve teknoloji hisseleri AI harcama endişeleri ve zayıf bilançolarla baskı altında, savunma sektörleri öne çıkıyor; Cuma günü trend gününün kapanışa kadar sürme olasılığı var.» / GPT «Büyüme hisselerinde baskı sürerken tepki alımları zayıf; ancak yataylaşan piyasada 1:4 kaldıraç ve mevcut teknoloji pozisyonları toplam riski artırıyor.»
30.10 18:26 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"104520.13","message":"insufficient buying power"}
30.10 19:20 B5  CLOSE short take profit: +69.06 USD
30.10 19:20 N  NEWS (27 new) score -0.45 conf 0.60: 
30.10 19:20 N  GPT  score -0.55 conf 0.62: Altının 3.900 doların altına sert düşmesi kısa vadeli satış momentumuna işaret ediyor; PCE enflasyonunun %3,6’ya çıkması ve bildirilen TIPS getiri sıçraması da faizlerin yüksek kalacağı beklentisini güçlendirerek altını baskılayabilir. Jeopolitik risk başlıkları destekleyici olsa da çoğu belirsiz ve
30.10 19:20 B5  SHORT gold 25000 USD x10 @ 3912.45 (TP 3900.71, SL 3920.27; news -0.50)
30.10 19:20 B6  karar turu: Claude «Teknoloji ağırlıklı satış baskısı, defansif rotasyon ve Hürmüz kaynaklı jeopolitik risk nedeniyle piyasa hafta sonu öncesi zayıf seyrini koruyor.» / GPT «Piyasa satış ağırlıklı; teknoloji daha zayıf görünürken 1:4 kaldıraçta mevcut pozisyonlarla toplam risk birikimine dikkat edilmeli.»
30.10 19:20 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"104827.21","message":"insufficient buying power"}
30.10 20:09 N  NEWS (31 new) score -0.70 conf 0.70: Fed yetkilileri (Musalem, Barkin) yakında faiz artırımı gerektiğini söyleyerek şahin bir tutum sergiledi; bu reel faiz ve dolar beklentilerini yükselterek altı baskılıyor. Altın bir yıllık dibe inmiş ve sert düşüş yaşanıyor; Orta Doğu gerilimi ise güvenli liman talebini destekleyecek yönde olsa da bu etki şu an fiyatlanmış görünmüyor. Güvenli liman sinyali yerine faiz kaynaklı satış baskın olduğundan skor negatif, güven ise İran diplomasisinin belirsizliği nedeniyle orta düzeyde.
30.10 20:09 N  GPT  score -0.55 conf 0.69: Musalem’in yakında faiz artırımı gerektiğini yinelemesi, dolar ve reel faizleri destekleyerek altın üzerinde kısa vadeli baskı yaratabilir. Suudi Arabistan yakınındaki füze ve İHA önlemeleri güvenli liman talebini artırsa da bu etki, belirgin şahin Fed mesajını muhtemelen dengeleyemiyor; ayrıca habe
30.10 20:09 B6  karar turu: Claude «Şahin Fed açıklamaları ve çip hisselerindeki çöküş Cuma öğleden sonrasında teknoloji ağırlıklı satış baskısını sürdürüyor; ancak gün içi düşüş zaten büyük olduğu için pozisyonlar temkinli tutuluyor.» / GPT «Şahin Fed açıklamaları ve teknoloji hisselerindeki zayıflık kısa yönü destekliyor; iki endeksin yüksek korelasyonu nedeniyle toplam kaldıraçlı risk sınırlı tutulmalı.»
30.10 20:09 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"105073.85","message":"insufficient buying power"}
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
