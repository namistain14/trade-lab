# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 29.10.2026 22:18 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -114.07 $ | -125.36 $ |
| İşlem sayısı | 6 | 10 |
| Kazanma oranı | %16.7 | %30.0 |
| Ödenen komisyon/spread | 32.72 $ | 40.71 $ |

**Hesap değeri: 4,860.17 $** (başlangıç 5,000 $, -139.83 $ / %-2.80)

Açık pozisyonlar: BTCUSDT long @ 80866.25 (TP 81351.45 / SL 80542.79); BNBUSDT long @ 744.08 (TP 748.55 / SL 741.11); XRPUSDT long @ 1.28 (TP 1.29 / SL 1.28)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 29.10 21:32 | SOLUSDT | long | -15.64 $ | stop |
| 29.10 21:32 | ETHUSDT | long | -31.28 $ | stop |
| 29.10 20:42 | XRPUSDT | long | -31.68 $ | stop |
| 29.10 20:48 | BTCUSDT | long | -31.68 $ | stop |
| 29.10 16:31 | BNBUSDT | long | +27.93 $ | take profit |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +13.14 $ | +13.14 $ |
| İşlem sayısı | 2 | 2 |
| Kazanma oranı | %50.0 | %50.0 |
| Ödenen komisyon/spread | 23.73 $ | 23.73 $ |

**Hesap değeri: 4,993.45 $** (başlangıç 5,000 $, -6.55 $ / %-0.13)

Açık pozisyonlar: PAXGUSDT short @ 4015.17 (TP 4003.12 / SL 4023.20)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 29.10 20:48 | PAXGUSDT | short | +69.08 $ | take profit |
| 29.10 16:36 | PAXGUSDT | short | -55.94 $ | stop |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 100,236.74 $** (başlangıç 100,000 $, +236.74 $ / %+0.24)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
29.10 21:17 A  CLOSE XRPUSDT stop: -31.68 USD
29.10 21:17 A  BUY BTCUSDT 5906 USD x3 @ 80866.25 (RSI 41)
29.10 21:17 A  BUY ETHUSDT 5906 USD x3 @ 2341.30 (RSI 41)
29.10 21:17 A  BUY SOLUSDT 2953 USD x3 @ 101.12 (RSI 38)
29.10 21:17 B5  CLOSE short take profit: +69.08 USD
29.10 21:17 N  NEWS (30 new) score -0.50 conf 0.60: Fed faizleri sabit tutup şahin duruş sergiledi, güçlü ABD GSYH verisi ve enflasyonun yükselişi faiz artırımı beklentilerini güçlendirdi; bu da altın için negatif. İran savaşı ile ilgili haberler jeopolitik risk primi sağlasa da bu etki zaten fiyatlanmış görünüyor ve faiz/dolar etkisini dengeleyemiyor.
29.10 21:17 N  GPT  score -0.55 conf 0.65: Güçlü büyüme ve hızlanan enflasyon, Fed’in faizleri daha uzun süre yüksek tutabileceği beklentisini destekleyerek altın üzerinde baskı yaratıyor; haberlerde altının zaten gerilediği de belirtiliyor. Savaş başlıkları yeni bir tırmanış göstermediğinden güvenli liman desteği sınırlı, ayrıca bazı haberl
29.10 21:17 B5  SHORT gold 25000 USD x10 @ 4015.17 (TP 4003.12, SL 4023.20; news -0.53)
29.10 21:17 B6  karar turu: Claude «Alphabet kaynaklı teknoloji satışı ve İran-ABD gerginliği Nasdaq'ı baskılarken, güçlü GDP verisi defansif hisseleri ve küçük ölçekli şirketleri destekliyor.» / GPT «Teknoloji hisselerinde baskı sürerken endekslerde momentum zayıf; QQQ kısa pozisyonu mevcut NVDA pozisyonuyla birlikte yoğunlaşma riski açısından değerlendirilmelidir.»
29.10 22:18 A  CLOSE ETHUSDT stop: -31.28 USD
29.10 22:18 A  CLOSE SOLUSDT stop: -15.64 USD
29.10 22:18 A  BUY BNBUSDT 5850 USD x3 @ 744.08 (RSI 41)
29.10 22:18 A  BUY XRPUSDT 2868 USD x3 @ 1.28 (RSI 33)
29.10 22:18 N  NEWS (26 new) score -0.45 conf 0.60: Fed'in 10-2 ile faizleri sabit tutup enflasyonun yüksek kaldığını belirtmesi, Core PCE'nin %3,1'e çıkması ve Hassett'in Ekim enflasyonu sıcak gelirse faiz artırımına açık olduğunu söylemesi, sıkılaşma beklentilerini artırarak altın için baskılayıcı. İran savaşı riski altın için sınırlı destek sağlasa da, haberlerin çoğu zaten fiyatlanmış görünüyor.
29.10 22:18 N  GPT  score -0.45 conf 0.67: Beklentileri aşan ABD büyümesi, yüksek çekirdek PCE ve Fed’in enflasyon nedeniyle temkinli duruşu faizlerin yüksek kalacağı beklentisini destekleyerek altını kısa vadede baskılıyor. İran ve Ukrayna kaynaklı riskler güvenli liman talebiyle bu baskıyı kısmen dengeliyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
