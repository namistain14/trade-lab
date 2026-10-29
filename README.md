# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 29.10.2026 21:17 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -67.15 $ | -78.44 $ |
| İşlem sayısı | 4 | 8 |
| Kazanma oranı | %25.0 | %37.5 |
| Ödenen komisyon/spread | 23.88 $ | 31.87 $ |

**Hesap değeri: 4,909.75 $** (başlangıç 5,000 $, -90.25 $ / %-1.80)

Açık pozisyonlar: BTCUSDT long @ 80866.25 (TP 81351.45 / SL 80542.79); ETHUSDT long @ 2341.30 (TP 2355.35 / SL 2331.94); SOLUSDT long @ 101.12 (TP 101.73 / SL 100.72)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 29.10 20:42 | XRPUSDT | long | -31.68 $ | stop |
| 29.10 20:48 | BTCUSDT | long | -31.68 $ | stop |
| 29.10 16:31 | BNBUSDT | long | +27.93 $ | take profit |
| 29.10 14:24 | BNBUSDT | long | -31.71 $ | stop |
| 28.10 16:31 | BTCUSDT | long | -6.29 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +13.14 $ | +13.14 $ |
| İşlem sayısı | 2 | 2 |
| Kazanma oranı | %50.0 | %50.0 |
| Ödenen komisyon/spread | 23.73 $ | 23.73 $ |

**Hesap değeri: 5,007.21 $** (başlangıç 5,000 $, +7.21 $ / %+0.14)

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

**Hesap değeri: 100,257.88 $** (başlangıç 100,000 $, +257.88 $ / %+0.26)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
29.10 20:27 A  BUY BTCUSDT 5982 USD x3 @ 81120.97 (RSI 43)
29.10 20:27 A  BUY XRPUSDT 5982 USD x3 @ 1.30 (RSI 42)
29.10 20:27 N  NEWS (36 new) score -0.30 conf 0.50: 
29.10 20:27 N  GPT  score -0.25 conf 0.56: Eylül enflasyonunun ve çekirdek PCE’nin hızlandığı haberleri Fed’in daha temkinli kalacağı beklentisini güçlendirerek altın üzerinde baskı yaratabilir. İran ve Ukrayna kaynaklı riskler güvenli liman talebini desteklese de haberler büyük ölçüde süregelen gelişmeler ve kısa vadeli yön net değil.
29.10 20:27 B6  karar turu: Claude «Piyasa, Alphabet'in sert düşüşü nedeniyle teknoloji ağırlıklı zayıf seyrediyor ancak güçlü GDP verisiyle öğleden sonra yatay konsolide oluyor; İran gelişmeleri aşağı yönlü risk taşıyor.» / GPT «Piyasa yatay sıkışırken teknoloji hisseleri görece zayıf; dar saatlik bantlar yüzde 1,5 hedefe ulaşmayı zorlaştırıyor ve 1:4 kaldıraç riski büyütüyor.»
29.10 21:17 A  CLOSE BTCUSDT stop: -31.68 USD
29.10 21:17 A  CLOSE XRPUSDT stop: -31.68 USD
29.10 21:17 A  BUY BTCUSDT 5906 USD x3 @ 80866.25 (RSI 41)
29.10 21:17 A  BUY ETHUSDT 5906 USD x3 @ 2341.30 (RSI 41)
29.10 21:17 A  BUY SOLUSDT 2953 USD x3 @ 101.12 (RSI 38)
29.10 21:17 B5  CLOSE short take profit: +69.08 USD
29.10 21:17 N  NEWS (30 new) score -0.50 conf 0.60: Fed faizleri sabit tutup şahin duruş sergiledi, güçlü ABD GSYH verisi ve enflasyonun yükselişi faiz artırımı beklentilerini güçlendirdi; bu da altın için negatif. İran savaşı ile ilgili haberler jeopolitik risk primi sağlasa da bu etki zaten fiyatlanmış görünüyor ve faiz/dolar etkisini dengeleyemiyor.
29.10 21:17 N  GPT  score -0.55 conf 0.65: Güçlü büyüme ve hızlanan enflasyon, Fed’in faizleri daha uzun süre yüksek tutabileceği beklentisini destekleyerek altın üzerinde baskı yaratıyor; haberlerde altının zaten gerilediği de belirtiliyor. Savaş başlıkları yeni bir tırmanış göstermediğinden güvenli liman desteği sınırlı, ayrıca bazı haberl
29.10 21:17 B5  SHORT gold 25000 USD x10 @ 4015.17 (TP 4003.12, SL 4023.20; news -0.53)
29.10 21:17 B6  karar turu: Claude «Alphabet kaynaklı teknoloji satışı ve İran-ABD gerginliği Nasdaq'ı baskılarken, güçlü GDP verisi defansif hisseleri ve küçük ölçekli şirketleri destekliyor.» / GPT «Teknoloji hisselerinde baskı sürerken endekslerde momentum zayıf; QQQ kısa pozisyonu mevcut NVDA pozisyonuyla birlikte yoğunlaşma riski açısından değerlendirilmelidir.»
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
