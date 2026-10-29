# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 29.10.2026 23:08 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -191.53 $ | -202.82 $ |
| İşlem sayısı | 9 | 13 |
| Kazanma oranı | %11.1 | %23.1 |
| Ödenen komisyon/spread | 47.31 $ | 55.30 $ |

**Hesap değeri: 4,797.18 $** (başlangıç 5,000 $, -202.82 $ / %-4.06)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 29.10 23:03 | XRPUSDT | long | -15.19 $ | stop |
| 29.10 23:04 | BNBUSDT | long | -30.98 $ | stop |
| 29.10 23:04 | BTCUSDT | long | -31.28 $ | stop |
| 29.10 21:32 | SOLUSDT | long | -15.64 $ | stop |
| 29.10 21:32 | ETHUSDT | long | -31.28 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -42.80 $ | -42.80 $ |
| İşlem sayısı | 3 | 3 |
| Kazanma oranı | %33.3 | %33.3 |
| Ödenen komisyon/spread | 35.60 $ | 35.60 $ |

**Hesap değeri: 4,957.20 $** (başlangıç 5,000 $, -42.80 $ / %-0.86)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
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

**Hesap değeri: 100,251.45 $** (başlangıç 100,000 $, +251.45 $ / %+0.25)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
29.10 21:17 N  GPT  score -0.55 conf 0.65: Güçlü büyüme ve hızlanan enflasyon, Fed’in faizleri daha uzun süre yüksek tutabileceği beklentisini destekleyerek altın üzerinde baskı yaratıyor; haberlerde altının zaten gerilediği de belirtiliyor. Savaş başlıkları yeni bir tırmanış göstermediğinden güvenli liman desteği sınırlı, ayrıca bazı haberl
29.10 21:17 B5  SHORT gold 25000 USD x10 @ 4015.17 (TP 4003.12, SL 4023.20; news -0.53)
29.10 21:17 B6  karar turu: Claude «Alphabet kaynaklı teknoloji satışı ve İran-ABD gerginliği Nasdaq'ı baskılarken, güçlü GDP verisi defansif hisseleri ve küçük ölçekli şirketleri destekliyor.» / GPT «Teknoloji hisselerinde baskı sürerken endekslerde momentum zayıf; QQQ kısa pozisyonu mevcut NVDA pozisyonuyla birlikte yoğunlaşma riski açısından değerlendirilmelidir.»
29.10 22:18 A  CLOSE ETHUSDT stop: -31.28 USD
29.10 22:18 A  CLOSE SOLUSDT stop: -15.64 USD
29.10 22:18 A  BUY BNBUSDT 5850 USD x3 @ 744.08 (RSI 41)
29.10 22:18 A  BUY XRPUSDT 2868 USD x3 @ 1.28 (RSI 33)
29.10 22:18 N  NEWS (26 new) score -0.45 conf 0.60: Fed'in 10-2 ile faizleri sabit tutup enflasyonun yüksek kaldığını belirtmesi, Core PCE'nin %3,1'e çıkması ve Hassett'in Ekim enflasyonu sıcak gelirse faiz artırımına açık olduğunu söylemesi, sıkılaşma beklentilerini artırarak altın için baskılayıcı. İran savaşı riski altın için sınırlı destek sağlasa da, haberlerin çoğu zaten fiyatlanmış görünüyor.
29.10 22:18 N  GPT  score -0.45 conf 0.67: Beklentileri aşan ABD büyümesi, yüksek çekirdek PCE ve Fed’in enflasyon nedeniyle temkinli duruşu faizlerin yüksek kalacağı beklentisini destekleyerek altını kısa vadede baskılıyor. İran ve Ukrayna kaynaklı riskler güvenli liman talebiyle bu baskıyı kısmen dengeliyor.
29.10 23:08 A  CLOSE BTCUSDT stop: -31.28 USD
29.10 23:08 A  CLOSE BNBUSDT stop: -30.98 USD
29.10 23:08 A  CLOSE XRPUSDT stop: -15.19 USD
29.10 23:08 B5  CLOSE short stop: -55.94 USD
29.10 23:08 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
29.10 23:08 N  NEWS (26 new) score -0.35 conf 0.60: Güçlü ABD büyümesi (%3.4 GSYH), 3,1% çekirdek PCE ve Fed'in faizi sabit tutması (10-2) ile sıkı para politikası beklentisi altını baskılıyor. İran ve Ukrayna'daki savaş haberleri güvenli liman talebini destekliyor, ancak bunların büyük kısmı zaten fiyatlanmış durumda; ayrıca Warsh'ın Fed yaklaşımındaki değişiklik yönü belirsiz.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
