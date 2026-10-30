# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 18:26 (İstanbul)

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
| Net kâr/zarar | +95.29 $ | +52.49 $ |
| İşlem sayısı | 5 | 8 |
| Kazanma oranı | %60.0 | %50.0 |
| Ödenen komisyon/spread | 59.47 $ | 95.07 $ |

**Hesap değeri: 5,046.54 $** (başlangıç 5,000 $, +46.54 $ / %+0.93)

Açık pozisyonlar: PAXGUSDT short @ 3924.06 (TP 3912.28 / SL 3931.90)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 17:39 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 16:51 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 15:43 | PAXGUSDT | short | +69.07 $ | take profit |
| 30.10 14:25 | PAXGUSDT | short | +69.08 $ | take profit |
| 30.10 11:54 | PAXGUSDT | short | -55.95 $ | stop |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 101,762.29 $** (başlangıç 100,000 $, +1762.29 $ / %+1.76)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
30.10 16:33 N  GPT  score -0.30 conf 0.42: Altının sert düşüşü ve Trump’ın İran savaşının yakında biteceği yönündeki açıklamaları kısa vadede güvenli liman talebini zayıflatabilir. Ancak savaşın yeniden tırmanabileceğine dair haberler ve doların gerilemesi düşüşü sınırlıyor; yön sinyali bu nedenle temkinli ve hafif negatif.
30.10 16:33 B5  SHORT gold 25000 USD x10 @ 3944.48 (TP 3932.65, SL 3952.37; news -0.35)
30.10 16:33 B6  karar turu: Claude «Büyük teknoloji ve çip tarafındaki satış baskısı ile Fed'in şahin tonu piyasayı aşağı çekiyor; trend aşağı yönlü ancak açılışta tepki riski yüksek.» / GPT «Açılışta teknoloji öncülüğünde satış baskısı baskın; 1:4 kaldıraç ve mevcut pozisyonlar nedeniyle toplam riski sınırlamak önemli.»
30.10 16:33 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"100976.98","message":"insufficient buying power"}
30.10 17:32 B5  CLOSE short take profit: +69.06 USD
30.10 17:32 N  NEWS (32 new) score -0.60 conf 0.60: Haberlerin çoğu altın için baskı yaratıyor: Fed'de faiz artırımı beklentileri (Barkin'in kademeli artırımları desteklemesi, enflasyon endişeleri, Warsh uyarısı) ve altının 4 aylık dibe inmesi kısa vadede düşüşü destekliyor. Trump'ın İran savaşının yakında biteceğini söylemesi de güvenli liman talebini azaltıyor. Buna karşılık yavaşlayan ücret artışı ve UBS'nin fiyat hedefini koruması sınırlı bir destek sağlıyor; piyasada fiyatlanmış haberler olduğu için güven orta düzeyde.
30.10 17:32 N  GPT  score -0.58 conf 0.69: Altının 4 ayın dibine gerilemesi ve 4.000 doların altına düşmesi, enflasyonun Fed faiz artırımı beklentilerini güçlendirdiğine işaret ederek kısa vadede baskıyı artırıyor. Barkin’in kademeli faiz artışlarına desteği düşüş yönünü desteklerken, yavaşlayan ücret artışı ve İran çevresindeki çelişkili ha
30.10 17:32 B5  SHORT gold 25000 USD x10 @ 3912.39 (TP 3900.65, SL 3920.21; news -0.59)
30.10 17:32 B6  karar turu: Claude «Yapay zeka harcama endişeleri ve zayıf çip haberleriyle teknoloji ağırlıklı satış baskısı sürüyor, ancak düşüşün büyük kısmı fiyatlandığı için kısa yönlü işlemlerde temkinli olunmalı.» / GPT «Piyasa görünümü negatif; teknoloji hisselerindeki tepki alımları nedeniyle agresif satış yerine seçici kısa pozisyon tercih ediyorum.»
30.10 18:26 B5  CLOSE short stop: -55.97 USD
30.10 18:26 N  NEWS (36 new) score -0.20 conf 0.40: 
30.10 18:26 N  GPT  score -0.65 conf 0.72: Altının yüzde 3 düşerek 3.900 doların altına inmesi ve satışların likidasyonla derinleşmesi kısa vadeli aşağı yönlü momentumu güçlendiriyor; Trump’ın İran savaşının yakında bitebileceği açıklaması da güvenli liman talebini azaltabilir. Dolar ve tahvil getirilerindeki gerileme düşüşü sınırlasa da enf
30.10 18:26 B5  SHORT gold 25000 USD x10 @ 3924.06 (TP 3912.28, SL 3931.90; news -0.43)
30.10 18:26 B6  karar turu: Claude «Büyüme ve teknoloji hisseleri AI harcama endişeleri ve zayıf bilançolarla baskı altında, savunma sektörleri öne çıkıyor; Cuma günü trend gününün kapanışa kadar sürme olasılığı var.» / GPT «Büyüme hisselerinde baskı sürerken tepki alımları zayıf; ancak yataylaşan piyasada 1:4 kaldıraç ve mevcut teknoloji pozisyonları toplam riski artırıyor.»
30.10 18:26 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"104520.13","message":"insufficient buying power"}
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
