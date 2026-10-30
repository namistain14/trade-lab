# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 15:24 (İstanbul)

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
| Net kâr/zarar | +13.13 $ | -29.67 $ |
| İşlem sayısı | 2 | 5 |
| Kazanma oranı | %50.0 | %40.0 |
| Ödenen komisyon/spread | 23.76 $ | 59.36 $ |

**Hesap değeri: 4,986.57 $** (başlangıç 5,000 $, -13.43 $ / %-0.27)

Açık pozisyonlar: PAXGUSDT short @ 3977.36 (TP 3965.43 / SL 3985.32)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 14:25 | PAXGUSDT | short | +69.08 $ | take profit |
| 30.10 11:54 | PAXGUSDT | short | -55.95 $ | stop |
| 29.10 22:31 | PAXGUSDT | short | -55.94 $ | stop |
| 29.10 20:48 | PAXGUSDT | short | +69.08 $ | take profit |
| 29.10 16:36 | PAXGUSDT | short | -55.94 $ | stop |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 98,240.08 $** (başlangıç 100,000 $, -1759.92 $ / %-1.76)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
30.10 11:25 B5  SHORT gold 25000 USD x10 @ 3994.28 (TP 3982.30, SL 4002.27; news -0.47)
30.10 12:21 B5  CLOSE short stop: -55.95 USD
30.10 12:21 N  NEWS (33 new) score -0.45 conf 0.60: Haberlerin çoğu altın için baskı yaratıyor: Fed faiz artırımı beklentileri, yüksek petrol ve ABD enflasyon verisi, altının 4.000 dolar altına inmesi ve spot talepteki zayıflık. Jeopolitik risk (İran savaşı, Asya'da risk-off ve tahvil talebi) kısmen destek sağlasa da, bu etki Fed beklentilerinin gerisinde kalıyor; DXY'deki gerileme ise sınırlı bir destek sunuyor.
30.10 12:21 N  GPT  score -0.58 conf 0.68: Altının 4.000 doların altına gerilemesi ve yüksek petrol/enflasyonun Fed faiz artırımı beklentilerini güçlendirmesi kısa vadede belirgin baskı yaratıyor. Düşen tahvil getirileri ve DXY’deki zorlanma ile jeopolitik riskler bu baskıyı kısmen sınırlıyor.
30.10 13:17 N  NEWS (24 new) score -0.25 conf 0.40: 
30.10 13:17 N  GPT  score -0.20 conf 0.36: Altın, Fed faiz artırımı beklentileri ve zorunlu satışlarla baskı altında; doların zorlanması ve düşen tahvil getirileri bu baskıyı kısmen dengeliyor. Yeni başlıklarda kısa vadede güvenli liman talebini belirgin artıracak net bir tırmanış görünmüyor.
30.10 13:17 B5  SHORT gold 25000 USD x10 @ 3990.55 (TP 3978.58, SL 3998.53; news -0.23)
30.10 14:03 N  NEWS (22 new) score -0.30 conf 0.50: Yeni haberlerde Fed'in "çok sıcak olmayan" görüşünü sınayan veriler ve faiz artırımı beklentilerini destekleyen büyüme sinyalleri altın için baskı yaratıyor; gold fiyatı da 4.000 doların altına düştü. Iran savaşı ve olası yeni saldırılar güvenli liman talebini destekleyebilir, ancak altın bu jeopolitik gerilime rağmen yükselmiyor, zorunlu tasfiyeler sürüyor ve bu yüzden etki sınırlı kalıyor.
30.10 14:03 N  GPT  score -0.35 conf 0.66: ABD verilerinin Fed’in enflasyon değerlendirmesini sorgulatması ve faiz artışı beklentilerinin güçlenmesi altın üzerinde kısa vadeli baskı yaratıyor; 4.000 doların altına iniş de bu zayıflığı teyit ediyor. İran çevresindeki gerilim güvenli liman talebini destekleyebilir, ancak haber akışı savaşın sü
30.10 14:44 B5  CLOSE short take profit: +69.08 USD
30.10 14:44 N  NEWS (35 new) score -0.30 conf 0.50: Altın 4.000 doların altına kaydı; piyasada Fed'e yönelik şahin beklentiler (petrol ve ABD enflasyonuna bağlı faiz artırımı bahisleri) ve güçlenen dolar baskı yaratıyor. İran savaşı nedeniyle güvenli liman talebi destekleyici olsa da, faiz beklentileri bu desteği baskılıyor; haber akışının çoğu savaş ve enerji ile ilgili olduğundan etki karışık ve güven orta düzeyde.
30.10 14:44 N  GPT  score -0.48 conf 0.68: İran savaşının petrol ve enflasyon baskısını artırdığı, Fed’in faiz artırımı beklentilerinin ve doların güçlendiği yönündeki haberler kısa vadede altın için baskın biçimde olumsuz. Savaş kaynaklı güvenli liman talebi düşüşü sınırlayabilir; ancak haberlerin bir kısmı tekrarlı ve riskler muhtemelen fi
30.10 14:44 B5  SHORT gold 25000 USD x10 @ 3977.36 (TP 3965.43, SL 3985.32; news -0.39)
30.10 15:24 N  NEWS (25 new) score -0.60 conf 0.60: Altın 4.000 doları altına sarkıyor ve gün içinde %2,19 düşüş görülüyor; bu düşüşü sahiplenen ana neden, savaşa bağlı enflasyon baskısının yarattığı sert Fed beklentileri ve Trump'ın İran savaşının "yakında bitecek" açıklamasıyla güvenli liman talebinin zayıflamasıdır. Dolar sabah erken saatlerde zayıfladığı için kısmen destekleyici olsa da, bu etki sınırlı kalıyor; fiziki altın talebinin Asya'da zayıf olması da yukarı yönlü baskıyı sınırlıyor.
30.10 15:24 N  GPT  score -0.48 conf 0.67: İran savaşının yakında sona erebileceği yönündeki açıklamalar güvenli liman talebini azaltabilir; altının %2,19 düşmesi ve Fed faiz beklentilerinin baskısı kısa vadede aşağı yönlü sinyal veriyor. Doların gerilemesi altına bir miktar destek sağlarken, savaşın yeniden alevlenebileceğine dair haberler 
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
