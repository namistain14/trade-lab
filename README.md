# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 01.11.2026 00:02 (İstanbul)

## Bot A — Kripto TERS (alım sinyalinde satış, x3)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -539.09 $ |
| İşlem sayısı | 0 | 35 |
| Kazanma oranı | %0.0 | %20.0 |
| Ödenen komisyon/spread | 0.00 $ | 158.79 $ |

**Hesap değeri: 4,488.66 $** (başlangıç 5,000 $, -511.34 $ / %-10.23)

Açık pozisyonlar: BTCUSDT short @ 77575.88 (TP 77110.42 / SL 77886.18); SOLUSDT short @ 95.94 (TP 95.37 / SL 96.32); XRPUSDT short @ 1.25 (TP 1.24 / SL 1.26)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 31.10 08:47 | ETHUSDT | long | -4.52 $ | time limit |
| 31.10 08:47 | BTCUSDT | long | -4.46 $ | time limit |
| 31.10 07:13 | BNBUSDT | long | -19.18 $ | time limit |
| 31.10 06:10 | DOGEUSDT | long | -14.40 $ | stop |
| 31.10 06:44 | XRPUSDT | long | -28.81 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +78.66 $ |
| İşlem sayısı | 0 | 12 |
| Kazanma oranı | %0.0 | %50.0 |
| Ödenen komisyon/spread | 0.00 $ | 142.76 $ |

**Hesap değeri: 5,078.66 $** (başlangıç 5,000 $, +78.66 $ / %+1.57)

Son haber analizi (30.10 23:56): Claude puan **-0.65**, güven 0.70 — Fed yetkililerinin (Logan dahil) ek faiz artışı sinyalleri ve "hawkish hold" havası, reel faiz beklentilerini yükselterek altı baskılıyor; altın yıllık dibe inmiş durumda. Iran savaşının sonlanabileceği yönündeki Trump açıklamaları da güvenli liman talebini zayıflatıyor. Bu haberlerin bir kısmı zaten fiyatlanmış olabileceği için güveni sınırlı tutuyorum.

GPT (gpt-6-luna): puan **-0.72**, güven 0.78 — Fed yetkililerinin iki faiz artışı beklentisini dile getirmesi ve enflasyon kaygıları, altının faiz getirisi olmayan varlık olarak cazibesini azaltıyor; fiyatın yeni yıl dibine gerilemesi de aşağı yönlü momentumu destekliyor. İran savaşının yakında bitebileceği açıklaması güvenli liman talebini sını

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 31.10 00:48 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 23:07 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 20:35 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 18:48 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 17:39 | PAXGUSDT | short | -55.97 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 101,128.90 $** (başlangıç 100,000 $, +1128.90 $ / %+1.13)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
30.10 23:56 B5  SHORT gold 25000 USD x10 @ 3891.96 (TP 3880.29, SL 3899.75; news -0.69)
31.10 01:15 B5  CLOSE short stop: -55.97 USD
31.10 05:11 A  BUY BNBUSDT 5439 USD x3 @ 705.00 (RSI 36)
31.10 05:11 A  BUY XRPUSDT 5439 USD x3 @ 1.26 (RSI 39)
31.10 05:11 A  BUY DOGEUSDT 2719 USD x3 @ 0.08 (RSI 43)
31.10 06:45 A  CLOSE XRPUSDT stop: -28.81 USD
31.10 06:45 A  CLOSE DOGEUSDT stop: -14.40 USD
31.10 06:45 A  BUY BTCUSDT 5387 USD x3 @ 77257.17 (RSI 39)
31.10 06:45 A  BUY ETHUSDT 2642 USD x3 @ 2243.39 (RSI 41)
31.10 07:27 A  CLOSE BNBUSDT time limit: -19.18 USD
31.10 08:58 A  CLOSE BTCUSDT time limit: -4.46 USD
31.10 08:58 A  CLOSE ETHUSDT time limit: -4.52 USD
31.10 22:31 A  SHORT BTCUSDT 5353 USD x3 @ 77575.88 (ters sinyal, RSI 40)
31.10 22:31 A  SHORT SOLUSDT 5353 USD x3 @ 95.94 (ters sinyal, RSI 43)
31.10 23:23 A  SHORT XRPUSDT 2677 USD x3 @ 1.25 (ters sinyal, RSI 42)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
