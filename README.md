# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 01.11.2026 05:06 (İstanbul)

## Bot A — Kripto TERS (alım sinyalinde satış, x3)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -80.39 $ | -619.48 $ |
| İşlem sayısı | 7 | 42 |
| Kazanma oranı | %14.3 | %19.0 |
| Ödenen komisyon/spread | 32.06 $ | 190.86 $ |

**Hesap değeri: 4,370.76 $** (başlangıç 5,000 $, -629.24 $ / %-12.58)

Açık pozisyonlar: DOGEUSDT short @ 0.08 (TP 0.08 / SL 0.08)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 01.11 04:54 | BTCUSDT | short | -17.54 $ | time limit |
| 01.11 04:15 | SOLUSDT | short | -8.71 $ | time limit |
| 01.11 03:54 | ETHUSDT | short | -28.31 $ | stop |
| 01.11 02:50 | BNBUSDT | short | -14.05 $ | time limit |
| 01.11 01:25 | XRPUSDT | short | -8.78 $ | time limit |

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
31.10 22:31 A  SHORT BTCUSDT 5353 USD x3 @ 77575.88 (ters sinyal, RSI 40)
31.10 22:31 A  SHORT SOLUSDT 5353 USD x3 @ 95.94 (ters sinyal, RSI 43)
31.10 23:23 A  SHORT XRPUSDT 2677 USD x3 @ 1.25 (ters sinyal, RSI 42)
01.11 00:48 A  CLOSE BTCUSDT time limit: -3.37 USD
01.11 00:48 A  CLOSE SOLUSDT time limit: +0.37 USD
01.11 00:48 A  SHORT BNBUSDT 5349 USD x3 @ 702.50 (ters sinyal, RSI 25)
01.11 01:27 A  CLOSE XRPUSDT time limit: -8.78 USD
01.11 02:13 A  SHORT ETHUSDT 5339 USD x3 @ 2253.72 (ters sinyal, RSI 45)
01.11 02:13 A  SHORT SOLUSDT 2659 USD x3 @ 95.61 (ters sinyal, RSI 44)
01.11 02:52 A  CLOSE BNBUSDT time limit: -14.05 USD
01.11 02:52 A  SHORT BTCUSDT 5307 USD x3 @ 77514.74 (ters sinyal, RSI 43)
01.11 03:56 A  CLOSE ETHUSDT stop: -28.31 USD
01.11 04:17 A  CLOSE SOLUSDT time limit: -8.71 USD
01.11 04:54 A  CLOSE BTCUSDT time limit: -17.54 USD
01.11 05:00 A  SHORT DOGEUSDT 5257 USD x3 @ 0.08 (ters sinyal, RSI 44)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
