# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 16:33 (İstanbul)

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
| Net kâr/zarar | +82.20 $ | +39.40 $ |
| İşlem sayısı | 3 | 6 |
| Kazanma oranı | %66.7 | %50.0 |
| Ödenen komisyon/spread | 35.65 $ | 71.25 $ |

**Hesap değeri: 5,033.45 $** (başlangıç 5,000 $, +33.45 $ / %+0.67)

Açık pozisyonlar: PAXGUSDT short @ 3944.48 (TP 3932.65 / SL 3952.37)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 15:43 | PAXGUSDT | short | +69.07 $ | take profit |
| 30.10 14:25 | PAXGUSDT | short | +69.08 $ | take profit |
| 30.10 11:54 | PAXGUSDT | short | -55.95 $ | stop |
| 29.10 22:31 | PAXGUSDT | short | -55.94 $ | stop |
| 29.10 20:48 | PAXGUSDT | short | +69.08 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 98,098.09 $** (başlangıç 100,000 $, -1901.91 $ / %-1.90)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
30.10 13:17 B5  SHORT gold 25000 USD x10 @ 3990.55 (TP 3978.58, SL 3998.53; news -0.23)
30.10 14:03 N  NEWS (22 new) score -0.30 conf 0.50: Yeni haberlerde Fed'in "çok sıcak olmayan" görüşünü sınayan veriler ve faiz artırımı beklentilerini destekleyen büyüme sinyalleri altın için baskı yaratıyor; gold fiyatı da 4.000 doların altına düştü. Iran savaşı ve olası yeni saldırılar güvenli liman talebini destekleyebilir, ancak altın bu jeopolitik gerilime rağmen yükselmiyor, zorunlu tasfiyeler sürüyor ve bu yüzden etki sınırlı kalıyor.
30.10 14:03 N  GPT  score -0.35 conf 0.66: ABD verilerinin Fed’in enflasyon değerlendirmesini sorgulatması ve faiz artışı beklentilerinin güçlenmesi altın üzerinde kısa vadeli baskı yaratıyor; 4.000 doların altına iniş de bu zayıflığı teyit ediyor. İran çevresindeki gerilim güvenli liman talebini destekleyebilir, ancak haber akışı savaşın sü
30.10 14:44 B5  CLOSE short take profit: +69.08 USD
30.10 14:44 N  NEWS (35 new) score -0.30 conf 0.50: Altın 4.000 doların altına kaydı; piyasada Fed'e yönelik şahin beklentiler (petrol ve ABD enflasyonuna bağlı faiz artırımı bahisleri) ve güçlenen dolar baskı yaratıyor. İran savaşı nedeniyle güvenli liman talebi destekleyici olsa da, faiz beklentileri bu desteği baskılıyor; haber akışının çoğu savaş ve enerji ile ilgili olduğundan etki karışık ve güven orta düzeyde.
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
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
