# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 28.10.2026 18:18 (İstanbul)

## Bot A — Kripto kurallar (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -6.29 $ | -11.29 $ |
| İşlem sayısı | 1 | 4 |
| Kazanma oranı | %0.0 | %50.0 |
| Ödenen komisyon/spread | 1.99 $ | 7.99 $ |

**Hesap değeri: 4,988.71 $** (başlangıç 5,000 $, -11.29 $ / %-0.23)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 28.10 16:31 | BTCUSDT | long | -6.29 $ | stop |
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
| Net kâr/zarar | -2.08 $ | -95.09 $ |
| İşlem sayısı | 4 | 42 |
| Kazanma oranı | %50.0 | %23.8 |
| Ödenen komisyon/spread | 9.49 $ | 99.68 $ |

**Hesap değeri: 4,903.11 $** (başlangıç 5,000 $, -96.89 $ / %-1.94)

Açık pozisyonlar: PAXGUSDT short @ 4046.91 (TP 4044.33 / SL 4048.38)

Son haber analizi (28.10 18:18): Claude puan **-0.25**, güven 0.50 — Fed'in bugün faiz kararını bekleyen piyasada, Fed'in bekleneni (duraklamayı) koruyup Aralık'ta olası bir faiz artırımını canlı tutması ve enflasyonun %3,7 seviyesinde olması altın için baskı oluşturuyor. Buna karşılık İran savaşının sürmesi, Putin'in nükleer kapasiteli füze testi ve NATO gerginliği güvenli liman talebini destekliyor; bu nedenle etki hafif negatif, güven orta düzeyde.

GPT (gpt-6-luna): puan **+0.12**, güven 0.34 — İran savaşı çevresindeki tırmanma uyarıları ve Rusya’nın nükleer kapasiteli füze denemesi kısa vadede güvenli liman talebini sınırlı destekleyebilir. Ancak Fed kararı öncesi olası şahin beklentiler altını baskılayabilir; başlıklar karışık ve bazıları dolaylı olduğundan yön güveni düşük.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 28.10 10:24 | PAXGUSDT | short | -3.00 $ | stop |
| 28.10 09:13 | PAXGUSDT | short | -3.08 $ | stop (gap) |
| 28.10 08:56 | PAXGUSDT | short | +2.00 $ | take profit |
| 28.10 07:50 | PAXGUSDT | short | +2.00 $ | take profit |
| 27.10 12:19 | PAXGUSDT | short | -3.00 $ | stop |

## Bot B2 — Altın: sıkı haber eşiği (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -38.22 $ |
| İşlem sayısı | 0 | 7 |
| Kazanma oranı | %0.0 | %14.3 |
| Ödenen komisyon/spread | 0.00 $ | 16.61 $ |

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
| Net kâr/zarar | -5.91 $ | -11.84 $ |
| İşlem sayısı | 2 | 7 |
| Kazanma oranı | %0.0 | %28.6 |
| Ödenen komisyon/spread | 4.74 $ | 16.60 $ |

**Hesap değeri: 4,988.16 $** (başlangıç 5,000 $, -11.84 $ / %-0.24)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 28.10 17:17 | PAXGUSDT | long | -4.01 $ | time limit |
| 28.10 01:16 | PAXGUSDT | long | -1.90 $ | time limit |
| 27.10 17:05 | PAXGUSDT | long | +13.81 $ | take profit |
| 27.10 15:33 | PAXGUSDT | long | +13.81 $ | take profit |
| 27.10 13:18 | PAXGUSDT | long | -11.18 $ | stop |

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
| Net kâr/zarar | +0.00 $ | +10.69 $ |
| İşlem sayısı | 0 | 3 |
| Kazanma oranı | %0.0 | %66.7 |
| Ödenen komisyon/spread | 0.00 $ | 7.12 $ |

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
28.10 15:15 A  BUY BTCUSDT 999 USD @ 80946.07 (RSI 31)
28.10 15:15 N  NEWS (38 new) score -0.30 conf 0.50: Fed'in bu hafta faiz kararı öncesi sıkılaşma riskleri (Aralık'ta olası artış beklentisi) ve ABD dolarının iki haftalık zirveye yakın seyretmesi altın için baskı yaratıyor. İran savaşıyla ilgili jeopolitik haberler güvenli liman talebini destekleyebilir, ancak Katar arabuluculuğunda savaşı bitirme teklifi bu etkiyi dengeliyor; dolayısıyla net etki hafif negatif.
28.10 15:15 N  GPT  score -0.22 conf 0.56: Fed’in faizleri sabit tutması bekleniyor; ancak aralıkta faiz artırımı ihtimali ve doların güçlü seyri kısa vadede altını baskılıyor. İran savaşının maliyetindeki artış güvenli liman talebini desteklese de olası anlaşma görüşmeleri bu desteği sınırlıyor.
28.10 16:22 N  NEWS (45 new) score -0.15 conf 0.40: İran savaşı sürüyor ve petrol fiyatlarını yukarı iten Suudi rafineri saldırısı güvenli liman talebini destekliyor, ancak altın toparlanması durdu ve gümüş geriledi; petrol kaynaklı enflasyon, Fed'in sıkı duruşu ve güçlü dolar beklentisi altın üzerinde baskı yaratıyor. Fed'in faiz sabit tutması bekleniyor ve enflasyon endişesi baskın olduğu için kısa vadede hafif negatif, ancak sinyaller karışık olduğundan güven düşük.
28.10 16:22 N  GPT  score +0.12 conf 0.36: İran savaşı, Yemen’deki füze saldırıları ve petrol tesisine yönelik saldırı iddiaları güvenli liman talebini destekleyebilir. Ancak petrol kaynaklı enflasyonun Fed’i temkinli veya daha şahin tutabileceği beklentisi altın için baskı yaratıyor; haber akışı karışık ve etkisinin bir kısmı fiyatlanmış ol
28.10 16:22 B6  seans öncesi görüş: Vadeli işlemler Fed faiz kararı öncesi pozitif seyrediyor, ancak karar öncesi belirsizlik nedeniyle yeni pozisyon açmamak en disiplinli seçenek.
28.10 17:21 A  CLOSE BTCUSDT stop: -6.29 USD
28.10 17:21 N  NEWS (30 new) score -0.10 conf 0.30: Haberler karışık: İran'la barış görüşmeleri (Katar arabuluculuğu, Körfez planı) jeopolitik korku primini azaltıp altın için hafif olumsuz; öte yandan petrol kaynaklı enflasyon, Bank of Canada'nın faiz artırımı ve Fed'in faiz artırımını "şimdilik" ertelediği haberleri sıkı para politikası beklentisini canlı tutarak altını baskılıyor. Fed kararının tonu belirsiz olduğundan güven düşük.
28.10 17:21 N  GPT  score +0.18 conf 0.34: İran savaşının petrol ve enerji fiyatları üzerindeki etkisi güvenli liman talebini destekleyebilir; ancak yeni barış girişimleri bu desteği sınırlıyor. Fed’in faizi sabit tutmasının beklenmesi büyük ölçüde fiyatlanmış görünüyor; kısa vadeli etki bu nedenle hafif pozitif ve belirsiz.
28.10 17:21 B4  CLOSE long time limit: -4.01 USD
28.10 17:21 B6  karar turu: Claude «Fed kararı öncesinde piyasa temkinli ve yatay seyrediyor; net bir fırsat olmadığı için beklemek en doğrusu.» / GPT «Endeksler kararsız ve teknoloji hisseleri zayıf; Fed kararı öncesinde haber ile fiyatın birlikte doğruladığı net bir avantaj bulunmadığından yeni pozisyon açmıyorum.»
28.10 18:18 N  NEWS (42 new) score -0.25 conf 0.50: Fed'in bugün faiz kararını bekleyen piyasada, Fed'in bekleneni (duraklamayı) koruyup Aralık'ta olası bir faiz artırımını canlı tutması ve enflasyonun %3,7 seviyesinde olması altın için baskı oluşturuyor. Buna karşılık İran savaşının sürmesi, Putin'in nükleer kapasiteli füze testi ve NATO gerginliği güvenli liman talebini destekliyor; bu nedenle etki hafif negatif, güven orta düzeyde.
28.10 18:18 N  GPT  score +0.12 conf 0.34: İran savaşı çevresindeki tırmanma uyarıları ve Rusya’nın nükleer kapasiteli füze denemesi kısa vadede güvenli liman talebini sınırlı destekleyebilir. Ancak Fed kararı öncesi olası şahin beklentiler altını baskılayabilir; başlıklar karışık ve bazıları dolaylı olduğundan yön güveni düşük.
28.10 18:18 B1  SHORT gold 5000 USD x10 @ 4046.91 (TP 4044.33, SL 4048.38; news -0.25)
28.10 18:18 B6  karar turu: Claude «Piyasa Fed kararı öncesi düşük oynaklıkla yatay seyrediyor; net bir avantaj olmadığı için beklemek en doğrusu.» / GPT «Endekslerdeki dar bant ve güçlü yeni şirket katalizörlerinin eksikliği nedeniyle, kaldıraçla yüzde 1,5 hedefli işlem açmak yerine beklemek daha disiplinli.»
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
