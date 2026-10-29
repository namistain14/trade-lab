# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 29.10.2026 15:41 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -31.71 $ | -43.00 $ |
| İşlem sayısı | 1 | 5 |
| Kazanma oranı | %0.0 | %40.0 |
| Ödenen komisyon/spread | 5.97 $ | 13.97 $ |

**Hesap değeri: 4,961.64 $** (başlangıç 5,000 $, -38.36 $ / %-0.77)

Açık pozisyonlar: BNBUSDT long @ 740.20 (TP 744.64 / SL 737.24)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 29.10 14:24 | BNBUSDT | long | -31.71 $ | stop |
| 28.10 16:31 | BTCUSDT | long | -6.29 $ | stop |
| 25.10 17:28 | BTCUSDT | long | +0.99 $ | time limit |
| 25.10 09:51 | SOLUSDT | long | -6.29 $ | stop |
| 23.10 09:46 | ETHUSDT | long | +0.30 $ | time limit |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 4,981.79 $** (başlangıç 5,000 $, -18.21 $ / %-0.36)

Açık pozisyonlar: PAXGUSDT short @ 4030.45 (TP 4018.36 / SL 4038.51)

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
29.10 13:53 B5  bakiye 5,000 $ olarak yeniden başlatıldı
29.10 13:53 B4  CLOSE PAXGUSDT bot kapatıldı: -7.24 USD
29.10 13:53 A  BUY BNBUSDT 5986 USD x3 @ 742.85 (RSI 34)
29.10 13:53 N  NEWS (20 new) score +0.15 conf 0.40: Fed faiz oranlarını sabit tuttu ve tahvil getirileri ile dolar Fed kararının ardından geriledi; bu, altın için hafif olumlu bir sinyal. Ancak enflasyon endişeleri ve Bank of Canada'nın faiz artırımı altın üzerinde baskı yaratabilir, ayrıca savaş haberleri büyük ölçüde fiyatlanmış durumda.
29.10 13:53 N  GPT  score +0.25 conf 0.42: Kuzey Kore’nin füze atışları ve Karadeniz’de savaşın ticari gemi trafiğine taşma riski güvenli liman talebini destekleyebilir; Fed sonrası tahvil faizlerinin gerilemesi ve dolar görünümünün zayıflaması da altın için hafif olumlu. Ancak faiz kararı büyük ölçüde bekleniyordu ve altının yatay/gerileyen
29.10 14:07 N  NEWS (19 new) score +0.15 conf 0.40: Fed'in faizi sabit tutması ve sonrasında Treasury getirilerinin ve doların gerilemesi altın için hafif destekleyici. Buna karşın Iran savaşına dair Katar arabuluculuk teklifi ve Kanada Merkez Bankası'nın faiz artırımı gibi haberler karışık sinyal veriyor, altın ve gümüş fiyatlarında kısa süreli düşüşler de görüldü; bu nedenle etki sınırlı ve güven düşük.
29.10 14:07 N  GPT  score +0.32 conf 0.43: Fed’in faizleri sabit tutmasının ardından tahvil getirilerinin gevşemesi ve İran çevresindeki gerilim ile Kuzey Kore füze haberleri altına kısa vadeli destek sağlayabilir. Ancak haber akışı karışık ve altının gerilediğini bildiren başlıklar da var; bu nedenle yükseliş etkisi sınırlı ve belirsiz.
29.10 14:53 A  CLOSE BNBUSDT stop: -31.71 USD
29.10 14:53 A  BUY BNBUSDT 5948 USD x3 @ 740.20 (RSI 39)
29.10 14:53 N  NEWS (33 new) score -0.30 conf 0.50: Fed faizleri sabit tuttu ama iki yetkili faiz artırımı için oy kullandı; bu şahin tonu altın için olumsuz. Gold ayrıca PCE öncesi zayıfladı ve dolar sabit kaldı. Öte yandan İran savaşı için yeni diplomatik girişimler jeopolitik risk primini azaltarak sınırlı bir baskı yaratıyor; sonuç olarak hafif negatif bir görünüm var, ancak PCE ve GDP verileri belirsizliği yüksek tutuyor.
29.10 14:53 N  GPT  score -0.30 conf 0.56: Fed’in faizi sabit tutmasına rağmen iki üyenin artış yönünde oy vermesi ve yüksek enflasyon kaygıları, PCE öncesinde altın üzerinde baskı yaratıyor; doların güçlenmesi de aşağı yönlü. İran savaşı güvenli liman talebini desteklese de çatışma haberleri yeni bir tırmanış göstermiyor ve getirilerdeki ge
29.10 14:53 B5  SHORT gold 25000 USD x10 @ 4030.45 (TP 4018.36, SL 4038.51; news -0.30)
29.10 15:41 N  NEWS (31 new) score -0.30 conf 0.50: Fed faizleri sabit tuttu ama iki yetkili faiz artırımı için oy verdi ve PCE enflasyonu yükseldi; bu, faiz indirimi beklentilerini zayıflatarak altın için baskı oluşturuyor. Altın fiyatı haber sonrası hafifçe geriledi ve dolar sabit kaldı; İran savaşı gibi jeopolitik riskler ise büyük ölçüde fiyatlanmış olduğundan destekleyici etkisi sınırlı kalıyor.
29.10 15:41 N  GPT  score -0.35 conf 0.65: Yükselen PCE ve Fed’in daha uzun süre sıkı kalabileceği beklentisi, doların güçlü seyriyle birlikte kısa vadede altın üzerinde baskı yaratıyor; haberlerde altının Fed kararının ardından gerilediği de belirtiliyor. Jeopolitik riskler sınırlı bir güvenli liman desteği sağlasa da yakın vadeli faiz etki
29.10 15:41 B6  seans öncesi görüş: Makro veriler büyük ölçüde beklentiye paralel, GDP güçlü ve fiyat endeksi düşük geldi; ancak GOOGL kaynaklı teknoloji zayıflığı Nasdaq'ı baskılıyor, bu yüzden seçici ve temkinli işlem uygun.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
