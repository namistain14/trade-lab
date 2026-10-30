# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 17:32 (İstanbul)

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
| Net kâr/zarar | +151.26 $ | +108.46 $ |
| İşlem sayısı | 4 | 7 |
| Kazanma oranı | %75.0 | %57.1 |
| Ödenen komisyon/spread | 47.55 $ | 83.15 $ |

**Hesap değeri: 5,102.50 $** (başlangıç 5,000 $, +102.50 $ / %+2.05)

Açık pozisyonlar: PAXGUSDT short @ 3912.39 (TP 3900.65 / SL 3920.21)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 16:51 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 15:43 | PAXGUSDT | short | +69.07 $ | take profit |
| 30.10 14:25 | PAXGUSDT | short | +69.08 $ | take profit |
| 30.10 11:54 | PAXGUSDT | short | -55.95 $ | stop |
| 29.10 22:31 | PAXGUSDT | short | -55.94 $ | stop |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 100,534.20 $** (başlangıç 100,000 $, +534.20 $ / %+0.53)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
30.10 14:44 N  GPT  score -0.48 conf 0.68: İran savaşının petrol ve enflasyon baskısını artırdığı, Fed’in faiz artırımı beklentilerinin ve doların güçlendiği yönündeki haberler kısa vadede altın için baskın biçimde olumsuz. Savaş kaynaklı güvenli liman talebi düşüşü sınırlayabilir; ancak haberlerin bir kısmı tekrarlı ve riskler muhtemelen fi
30.10 14:44 B5  SHORT gold 25000 USD x10 @ 3977.36 (TP 3965.43, SL 3985.32; news -0.39)
30.10 15:24 N  NEWS (25 new) score -0.60 conf 0.60: Altın 4.000 doları altına sarkıyor ve gün içinde %2,19 düşüş görülüyor; bu düşüşü sahiplenen ana neden, savaşa bağlı enflasyon baskısının yarattığı sert Fed beklentileri ve Trump'ın İran savaşının "yakında bitecek" açıklamasıyla güvenli liman talebinin zayıflamasıdır. Dolar sabah erken saatlerde zayıfladığı için kısmen destekleyici olsa da, bu etki sınırlı kalıyor; fiziki altın talebinin Asya'da zayıf olması da yukarı yönlü baskıyı sınırlıyor.
30.10 15:24 N  GPT  score -0.48 conf 0.67: İran savaşının yakında sona erebileceği yönündeki açıklamalar güvenli liman talebini azaltabilir; altının %2,19 düşmesi ve Fed faiz beklentilerinin baskısı kısa vadede aşağı yönlü sinyal veriyor. Doların gerilemesi altına bir miktar destek sağlarken, savaşın yeniden alevlenebileceğine dair haberler 
30.10 16:33 B5  CLOSE short take profit: +69.07 USD
30.10 16:33 N  NEWS (35 new) score -0.40 conf 0.55: Altın, haberlerde görülen düşüşün ardından 4.000 doların altına indi ve güvenli liman talebi zayıflıyor. Trump'ın İran savaşının yakında biteceği yönündeki açıklamaları jeopolitik primi azaltıyor; Fed Başkanı Warsh'un enflasyon ve sıkı para politikası uyarıları ile yüksek petrol fiyatları da faiz beklentilerini baskılayarak altın için olumsuz. Buna karşın doların her zaman güçlenmemesi ve ABD enflasyon riskinin sürmesi kısmen destekleyici; bu çelişkiler güveni sınırlıyor.
30.10 16:33 N  GPT  score -0.30 conf 0.42: Altının sert düşüşü ve Trump’ın İran savaşının yakında biteceği yönündeki açıklamaları kısa vadede güvenli liman talebini zayıflatabilir. Ancak savaşın yeniden tırmanabileceğine dair haberler ve doların gerilemesi düşüşü sınırlıyor; yön sinyali bu nedenle temkinli ve hafif negatif.
30.10 16:33 B5  SHORT gold 25000 USD x10 @ 3944.48 (TP 3932.65, SL 3952.37; news -0.35)
30.10 16:33 B6  karar turu: Claude «Büyük teknoloji ve çip tarafındaki satış baskısı ile Fed'in şahin tonu piyasayı aşağı çekiyor; trend aşağı yönlü ancak açılışta tepki riski yüksek.» / GPT «Açılışta teknoloji öncülüğünde satış baskısı baskın; 1:4 kaldıraç ve mevcut pozisyonlar nedeniyle toplam riski sınırlamak önemli.»
30.10 16:33 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"100976.98","message":"insufficient buying power"}
30.10 17:32 B5  CLOSE short take profit: +69.06 USD
30.10 17:32 N  NEWS (32 new) score -0.60 conf 0.60: Haberlerin çoğu altın için baskı yaratıyor: Fed'de faiz artırımı beklentileri (Barkin'in kademeli artırımları desteklemesi, enflasyon endişeleri, Warsh uyarısı) ve altının 4 aylık dibe inmesi kısa vadede düşüşü destekliyor. Trump'ın İran savaşının yakında biteceğini söylemesi de güvenli liman talebini azaltıyor. Buna karşılık yavaşlayan ücret artışı ve UBS'nin fiyat hedefini koruması sınırlı bir destek sağlıyor; piyasada fiyatlanmış haberler olduğu için güven orta düzeyde.
30.10 17:32 N  GPT  score -0.58 conf 0.69: Altının 4 ayın dibine gerilemesi ve 4.000 doların altına düşmesi, enflasyonun Fed faiz artırımı beklentilerini güçlendirdiğine işaret ederek kısa vadede baskıyı artırıyor. Barkin’in kademeli faiz artışlarına desteği düşüş yönünü desteklerken, yavaşlayan ücret artışı ve İran çevresindeki çelişkili ha
30.10 17:32 B5  SHORT gold 25000 USD x10 @ 3912.39 (TP 3900.65, SL 3920.21; news -0.59)
30.10 17:32 B6  karar turu: Claude «Yapay zeka harcama endişeleri ve zayıf çip haberleriyle teknoloji ağırlıklı satış baskısı sürüyor, ancak düşüşün büyük kısmı fiyatlandığı için kısa yönlü işlemlerde temkinli olunmalı.» / GPT «Piyasa görünümü negatif; teknoloji hisselerindeki tepki alımları nedeniyle agresif satış yerine seçici kısa pozisyon tercih ediyorum.»
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
