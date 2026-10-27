# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 27.10.2026 13:42 (İstanbul)

## Bot A — Kripto kurallar (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -5.00 $ |
| İşlem sayısı | 0 | 3 |
| Kazanma oranı | %0.0 | %66.7 |
| Ödenen komisyon/spread | 0.00 $ | 6.00 $ |

**Hesap değeri: 4,995.00 $** (başlangıç 5,000 $, -5.00 $ / %-0.10)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 25.10 17:28 | BTCUSDT | long | +0.99 $ | time limit |
| 25.10 09:51 | SOLUSDT | long | -6.29 $ | stop |
| 23.10 09:46 | ETHUSDT | long | +0.30 $ | time limit |

## Bot A2 — Kripto: sert düşüş sonrası toparlanma (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +5.69 $ |
| İşlem sayısı | 0 | 1 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 2.01 $ |

**Hesap değeri: 5,005.69 $** (başlangıç 5,000 $, +5.69 $ / %+0.11)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 24.10 19:51 | ETHUSDT | long | +5.69 $ | take profit |

## Bot B1 — Altın + haber (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -10.97 $ | -93.01 $ |
| İşlem sayısı | 3 | 38 |
| Kazanma oranı | %0.0 | %21.1 |
| Ödenen komisyon/spread | 7.12 $ | 90.19 $ |

**Hesap değeri: 4,906.99 $** (başlangıç 5,000 $, -93.01 $ / %-1.86)

Son haber analizi (27.10 13:42): Claude puan **-0.20**, güven 0.40 — Fed kararı öncesinde dolar güçleniyor ve altın 4.000 dolar desteğini test ediyor; bu, kısa vadede altın için baskı yaratıyor. İran savaşı ve petrolün nisan zirvelerine yakın seyretmesi enflasyon kaynaklı sıkı para politikası beklentisini güçlendirip altını olumsuz etkileyebilir, ancak jeopolitik güvenli liman talebi bunu kısmen dengeliyor. Fed'in sonucunun belirsiz olması ve haberlerin çoğunun eski ya da fiyatlanmış olması nedeniyle güven düşük tutuldu.

GPT (gpt-6-luna): puan **-0.25**, güven 0.42 — Fed kararı öncesinde doların güçlenmesi ve altının önemli desteği sınaması kısa vadede aşağı yönlü baskı yaratıyor. İran ve Yemen kaynaklı riskler güvenli liman talebini desteklese de belirgin yeni bir tırmanış yok; haber akışı bu nedenle karışık.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 27.10 12:19 | PAXGUSDT | short | -3.00 $ | stop |
| 27.10 11:31 | PAXGUSDT | short | -4.97 $ | stop (gap) |
| 27.10 06:06 | PAXGUSDT | short | -3.00 $ | stop |
| 26.10 14:24 | PAXGUSDT | short | -3.00 $ | stop |
| 26.10 10:21 | PAXGUSDT | short | -3.00 $ | stop |

## Bot B2 — Altın: sıkı haber eşiği (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -3.00 $ | -38.22 $ |
| İşlem sayısı | 1 | 7 |
| Kazanma oranı | %0.0 | %14.3 |
| Ödenen komisyon/spread | 2.37 $ | 16.61 $ |

**Hesap değeri: 4,961.78 $** (başlangıç 5,000 $, -38.22 $ / %-0.76)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 27.10 12:19 | PAXGUSDT | short | -3.00 $ | stop |
| 23.10 18:03 | PAXGUSDT | short | -4.28 $ | stop (gap) |
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 08:32 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 05:27 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B4 — Altın: haberin TERSİ (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -11.18 $ | -33.55 $ |
| İşlem sayısı | 1 | 3 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 2.37 $ | 7.12 $ |

**Hesap değeri: 4,966.45 $** (başlangıç 5,000 $, -33.55 $ / %-0.67)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 27.10 13:18 | PAXGUSDT | long | -11.18 $ | stop |
| 26.10 16:25 | PAXGUSDT | long | -11.18 $ | stop |
| 23.10 17:08 | PAXGUSDT | long | -11.18 $ | stop |

## Bot B3 — Altın: B2 + seans filtresi + momentum (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -26.82 $ |
| İşlem sayısı | 0 | 3 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 7.12 $ |

**Hesap değeri: 4,973.18 $** (başlangıç 5,000 $, -26.82 $ / %-0.54)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 18:22 | PAXGUSDT | short | -11.35 $ | stop (gap) |
| 23.10 18:03 | PAXGUSDT | short | -4.28 $ | stop (gap) |
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -11.19 $ | +10.69 $ |
| İşlem sayısı | 1 | 3 |
| Kazanma oranı | %0.0 | %66.7 |
| Ödenen komisyon/spread | 2.37 $ | 7.12 $ |

**Hesap değeri: 5,010.69 $** (başlangıç 5,000 $, +10.69 $ / %+0.21)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 27.10 13:42 | PAXGUSDT | short | -11.19 $ | stop |
| 24.10 00:03 | PAXGUSDT | short | +8.06 $ | time limit |
| 23.10 17:11 | PAXGUSDT | short | +13.82 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:2

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 99,842.81 $** (başlangıç 100,000 $, -157.19 $ / %-0.16)

## Son olaylar

```
27.10 12:16 B1  CLOSE short stop (gap): -4.97 USD
27.10 12:16 N  NEWS (38 new) score -0.40 conf 0.60: Güçlenen dolar (DXY 102 üzerinde), Fed'in faiz artırımı ihtimali konuşmaları ve altının 4.000 dolar civarında zayıflaması altın için baskı yaratıyor. Jeopolitik haberler (Ukrayna'ya füze saldırıları, İran savaşının sonuçları) güvenli liman talebini destekleyebilir, ancak bunlar büyük ölçüde fiyatlanmış ve eski haberler olduğu için etkisi sınırlı kalır.
27.10 12:16 N  GPT  score -0.30 conf 0.66: Daha güçlü dolar ve Fed’in faizleri yüksek tutacağı beklentisi, altının 4.000 dolar civarında gerilemesiyle de uyumlu biçimde kısa vadede baskın ve aşağı yönlü. Rusya’nın Kyiv saldırısı ve Çinli hanehalkının altın alımları destek sağlasa da Fed kararı öncesi yön belirsizliği sürüyor.
27.10 12:16 B1  SHORT gold 5000 USD x10 @ 4006.57 (TP 4004.02, SL 4008.02; news -0.40)
27.10 12:16 B2  SHORT gold 5000 USD x10 @ 4006.56 (TP 4004.01, SL 4008.01; news -0.40)
27.10 12:16 B5  SHORT gold 5000 USD x10 @ 4006.56 (TP 3994.54, SL 4014.57; news -0.35)
27.10 13:02 B1  CLOSE short stop: -3.00 USD
27.10 13:02 N  NEWS (15 new) score -0.35 conf 0.50: Dolar endeksi 102 üzerinde güçleniyor, FOMC öncesi dolar alımları ve "faiz artırımı" endişeleri altını baskılıyor; altın 4.000 doları yakın tutarken gümüş yıllık düşük seviyeleri kırdı. Jeopolitik (İran savaşı, Ukrayna) güvenli liman talebini destekleyebilir, ancak bu etki dolar ve Fed beklentilerinin gerisinde kalıyor; "4.000 kırıldı" gibi haberlerin tarihi/kaynağı belirsiz olduğu için güven orta düzeyde.
27.10 13:02 N  GPT  score -0.22 conf 0.56: FOMC öncesi dolar alımlarının geri dönmesi ve Fed görünümünün altını baskılaması kısa vadede hafif aşağı yönlü. Getirilerin yatay seyri ve altının 4.000 dolar üzerinde kalması ise düşüşü sınırlayabilir; haber akışı karışık ve karar öncesi temkinli olmak gerekir.
27.10 13:02 B2  CLOSE short stop: -3.00 USD
27.10 13:02 B4  LONG gold 5000 USD x10 @ 4014.42 (TP 4026.47, SL 4006.39; news +0.35)
27.10 13:42 N  NEWS (29 new) score -0.20 conf 0.40: Fed kararı öncesinde dolar güçleniyor ve altın 4.000 dolar desteğini test ediyor; bu, kısa vadede altın için baskı yaratıyor. İran savaşı ve petrolün nisan zirvelerine yakın seyretmesi enflasyon kaynaklı sıkı para politikası beklentisini güçlendirip altını olumsuz etkileyebilir, ancak jeopolitik güvenli liman talebi bunu kısmen dengeliyor. Fed'in sonucunun belirsiz olması ve haberlerin çoğunun eski ya da fiyatlanmış olması nedeniyle güven düşük tutuldu.
27.10 13:42 N  GPT  score -0.25 conf 0.42: Fed kararı öncesinde doların güçlenmesi ve altının önemli desteği sınaması kısa vadede aşağı yönlü baskı yaratıyor. İran ve Yemen kaynaklı riskler güvenli liman talebini desteklese de belirgin yeni bir tırmanış yok; haber akışı bu nedenle karışık.
27.10 13:42 B4  CLOSE long stop: -11.18 USD
27.10 13:42 B5  CLOSE short stop: -11.19 USD
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
