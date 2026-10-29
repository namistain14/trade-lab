# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 29.10.2026 16:43 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -3.78 $ | -15.07 $ |
| İşlem sayısı | 2 | 6 |
| Kazanma oranı | %50.0 | %50.0 |
| Ödenen komisyon/spread | 11.94 $ | 19.93 $ |

**Hesap değeri: 4,984.93 $** (başlangıç 5,000 $, -15.07 $ / %-0.30)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 29.10 16:31 | BNBUSDT | long | +27.93 $ | take profit |
| 29.10 14:24 | BNBUSDT | long | -31.71 $ | stop |
| 28.10 16:31 | BTCUSDT | long | -6.29 $ | stop |
| 25.10 17:28 | BTCUSDT | long | +0.99 $ | time limit |
| 25.10 09:51 | SOLUSDT | long | -6.29 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -55.94 $ | -55.94 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 11.86 $ | 11.86 $ |

**Hesap değeri: 4,944.06 $** (başlangıç 5,000 $, -55.94 $ / %-1.12)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 29.10 16:36 | PAXGUSDT | short | -55.94 $ | stop |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 99,842.81 $** (başlangıç 100,000 $, -157.19 $ / %-0.16)

## Son olaylar

```
29.10 14:53 A  CLOSE BNBUSDT stop: -31.71 USD
29.10 14:53 A  BUY BNBUSDT 5948 USD x3 @ 740.20 (RSI 39)
29.10 14:53 N  NEWS (33 new) score -0.30 conf 0.50: Fed faizleri sabit tuttu ama iki yetkili faiz artırımı için oy kullandı; bu şahin tonu altın için olumsuz. Gold ayrıca PCE öncesi zayıfladı ve dolar sabit kaldı. Öte yandan İran savaşı için yeni diplomatik girişimler jeopolitik risk primini azaltarak sınırlı bir baskı yaratıyor; sonuç olarak hafif negatif bir görünüm var, ancak PCE ve GDP verileri belirsizliği yüksek tutuyor.
29.10 14:53 N  GPT  score -0.30 conf 0.56: Fed’in faizi sabit tutmasına rağmen iki üyenin artış yönünde oy vermesi ve yüksek enflasyon kaygıları, PCE öncesinde altın üzerinde baskı yaratıyor; doların güçlenmesi de aşağı yönlü. İran savaşı güvenli liman talebini desteklese de çatışma haberleri yeni bir tırmanış göstermiyor ve getirilerdeki ge
29.10 14:53 B5  SHORT gold 25000 USD x10 @ 4030.45 (TP 4018.36, SL 4038.51; news -0.30)
29.10 15:41 N  NEWS (31 new) score -0.30 conf 0.50: Fed faizleri sabit tuttu ama iki yetkili faiz artırımı için oy verdi ve PCE enflasyonu yükseldi; bu, faiz indirimi beklentilerini zayıflatarak altın için baskı oluşturuyor. Altın fiyatı haber sonrası hafifçe geriledi ve dolar sabit kaldı; İran savaşı gibi jeopolitik riskler ise büyük ölçüde fiyatlanmış olduğundan destekleyici etkisi sınırlı kalıyor.
29.10 15:41 N  GPT  score -0.35 conf 0.65: Yükselen PCE ve Fed’in daha uzun süre sıkı kalabileceği beklentisi, doların güçlü seyriyle birlikte kısa vadede altın üzerinde baskı yaratıyor; haberlerde altının Fed kararının ardından gerilediği de belirtiliyor. Jeopolitik riskler sınırlı bir güvenli liman desteği sağlasa da yakın vadeli faiz etki
29.10 15:41 B6  seans öncesi görüş: Makro veriler büyük ölçüde beklentiye paralel, GDP güçlü ve fiyat endeksi düşük geldi; ancak GOOGL kaynaklı teknoloji zayıflığı Nasdaq'ı baskılıyor, bu yüzden seçici ve temkinli işlem uygun.
29.10 16:43 A  CLOSE BNBUSDT take profit: +27.93 USD
29.10 16:43 B5  CLOSE short stop: -55.94 USD
29.10 16:43 N  NEWS (41 new) score -0.60 conf 0.70: Fed faizleri sabit tuttu ancak iki oy artırım yönünde çıktı, çekirdek PCE enflasyonu %3,6'ya yükseldi ve ABD GDP'si %3,4 ile beklentilerin üzerinde büyüdü. Bu tablo reel faiz ve dolar tarafında baskı yaratıyor; Kitco da altının 4.000 dolara doğru gerilediğini bildiriyor. Jeopolitik haberler (İran savaşı maliyeti, Rusya-Ukrayna) güvenli liman talebini bir miktar destekleyebilir, ancak etkisi bu sıkı para politikası sinyallerinin gerisinde kalıyor.
29.10 16:43 N  GPT  score -0.58 conf 0.72: Beklentileri aşan ABD büyümesi ve Fed’in tercih ettiği enflasyon göstergesinin %3,6’ya yükselmesi, faizlerin daha uzun süre yüksek kalacağı beklentisini destekleyerek altın üzerinde baskı yaratıyor. İran savaşı kaynaklı riskler güvenli liman talebini desteklese de kısa vadede makroekonomik baskın et
29.10 16:43 B6  karar turu: Claude «Alphabet çöküşü Nasdaq'ı aşağı çekerken makro veriler nötr; şirkete özel haberlerde seçici işlem yapmak en mantıklısı.» / GPT «Teknoloji endeksi baskı altında olduğundan geniş piyasadaki düşüşü kovalamak yerine AAPL'de haber destekli alım ve NVDA'da seçici satış tercih ediyorum.»
29.10 16:43 B6  AÇIĞA SATIŞ NVDA 467 adet ≈ 99,751 $ (1:4) @ 213.6 (TP 210.4, SL 215.74; ikisi de hemfikir, güven 0.55)
29.10 16:43 B6  ALIŞ AAPL 285 adet ≈ 99,608 $ (1:4) @ 349.5 (TP 354.74, SL 346.0; ikisi de hemfikir, güven 0.60)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
