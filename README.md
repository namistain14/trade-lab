# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 29.10.2026 18:36 (İstanbul)

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

**Hesap değeri: 4,938.13 $** (başlangıç 5,000 $, -61.87 $ / %-1.24)

Açık pozisyonlar: PAXGUSDT short @ 4029.87 (TP 4017.78 / SL 4037.93)

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

**Hesap değeri: 99,532.78 $** (başlangıç 100,000 $, -467.22 $ / %-0.47)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
29.10 16:43 A  CLOSE BNBUSDT take profit: +27.93 USD
29.10 16:43 B5  CLOSE short stop: -55.94 USD
29.10 16:43 N  NEWS (41 new) score -0.60 conf 0.70: Fed faizleri sabit tuttu ancak iki oy artırım yönünde çıktı, çekirdek PCE enflasyonu %3,6'ya yükseldi ve ABD GDP'si %3,4 ile beklentilerin üzerinde büyüdü. Bu tablo reel faiz ve dolar tarafında baskı yaratıyor; Kitco da altının 4.000 dolara doğru gerilediğini bildiriyor. Jeopolitik haberler (İran savaşı maliyeti, Rusya-Ukrayna) güvenli liman talebini bir miktar destekleyebilir, ancak etkisi bu sıkı para politikası sinyallerinin gerisinde kalıyor.
29.10 16:43 N  GPT  score -0.58 conf 0.72: Beklentileri aşan ABD büyümesi ve Fed’in tercih ettiği enflasyon göstergesinin %3,6’ya yükselmesi, faizlerin daha uzun süre yüksek kalacağı beklentisini destekleyerek altın üzerinde baskı yaratıyor. İran savaşı kaynaklı riskler güvenli liman talebini desteklese de kısa vadede makroekonomik baskın et
29.10 16:43 B6  karar turu: Claude «Alphabet çöküşü Nasdaq'ı aşağı çekerken makro veriler nötr; şirkete özel haberlerde seçici işlem yapmak en mantıklısı.» / GPT «Teknoloji endeksi baskı altında olduğundan geniş piyasadaki düşüşü kovalamak yerine AAPL'de haber destekli alım ve NVDA'da seçici satış tercih ediyorum.»
29.10 16:43 B6  AÇIĞA SATIŞ NVDA 467 adet ≈ 99,751 $ (1:4) @ 213.6 (TP 210.4, SL 215.74; ikisi de hemfikir, güven 0.55)
29.10 16:43 B6  ALIŞ AAPL 285 adet ≈ 99,608 $ (1:4) @ 349.5 (TP 354.74, SL 346.0; ikisi de hemfikir, güven 0.60)
29.10 17:39 N  NEWS (36 new) score -0.50 conf 0.60: Enflasyon ve büyüme verileri güçlü çıktı (Eylül PCE %3,6, Q3 büyüme beklentiyi aştı) ve Fed'in yıl sonu faiz artırımı beklentileri canlandı; bu reel faiz ve dolar tarafında altı baskılıyor. İran savaşı ve Ukrayna'daki saldırılar güvenli liman talebini destekleyebilir, ancak bu gelişmelerin büyük kısmı zaten fiyatlanmış durumda.
29.10 17:39 N  GPT  score -0.40 conf 0.73: Beklentilerle uyumlu olsa da yüksek PCE enflasyonu ve güçlü büyüme, Fed’in yıl sonuna doğru faiz artırımı beklentilerini besleyerek kısa vadede altın üzerinde baskı oluşturuyor. İran ve Ukrayna kaynaklı gerilimler güvenli liman talebiyle düşüşü sınırlayabilir.
29.10 17:39 B6  karar turu: Claude «Piyasa, Alphabet ve yazılım kaynaklı teknoloji satışının ardından açılış düşüşünü sindirip dengelenmeye çalışıyor; göreceli güçlü hisseler öne çıkıyor.» / GPT «Teknoloji endeksi zayıf olsa da satış baskısı son saatte hafifliyor; dört kat kaldıraç altında endekslerden ziyade göreli güç gösteren TSLA'da seçici alımı tercih ediyorum.»
29.10 17:39 B6  ALIŞ TSLA 245 adet ≈ 99,544 $ (1:4) @ 406.3 (TP 412.39, SL 402.24; ikisi de hemfikir, güven 0.56)
29.10 18:36 N  NEWS (37 new) score -0.30 conf 0.50: Fed faizleri sabit tuttu ancak Hassett, Ekim enflasyonu yüksek gelirse Fed'in harekete geçebileceğini söyledi; Eylül PCE enflasyonu yükseldi ve 6% tahvil getirisi tezi gerçek faizleri yukarı taşıyarak altı baskılıyor. İran savaşı ve olası yeni saldırı haberleri jeopolitik talebi destekliyor, ancak etkisi sınırlı kalıyor ve haberlerin büyük kısmı zaten fiyatlanmış durumda.
29.10 18:36 N  GPT  score -0.28 conf 0.58: Güçlü büyüme ve yükselen enflasyon verileri, Fed’in daha sıkı kalabileceği ve tahvil getirilerinin yükselebileceği beklentisini destekleyerek altını kısa vadede baskılıyor. İran savaşı ve olası yeni saldırılar güvenli liman talebi yaratsa da bu etki, faiz baskısıyla kısmen dengeleniyor.
29.10 18:36 B5  SHORT gold 25000 USD x10 @ 4029.87 (TP 4017.78, SL 4037.93; news -0.29)
29.10 18:36 B6  karar turu: Claude «Alphabet'in sert düşüşü Nasdaq'ı baskılasa da beklentiyle uyumlu PCE ve güçlü GDP verisi sonrası piyasa gün içi dipten kademeli olarak toparlanıyor.» / GPT «Endekslerde kısa vadeli toparlanma alımları öne çıkarken Alphabet kaynaklı teknoloji baskısı nedeniyle yükselişi güçlü trend değil, kırılgan tepki hareketi olarak değerlendiriyorum.»
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
