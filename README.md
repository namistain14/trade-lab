# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 01.11.2026 07:24 (İstanbul)

## Bot A — Kripto TERS (alım sinyalinde satış, x3)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -81.85 $ | -620.93 $ |
| İşlem sayısı | 8 | 43 |
| Kazanma oranı | %12.5 | %18.6 |
| Ödenen komisyon/spread | 37.32 $ | 196.11 $ |

**Hesap değeri: 4,353.04 $** (başlangıç 5,000 $, -646.96 $ / %-12.94)

Açık pozisyonlar: XRPUSDT short @ 1.25 (TP 1.24 / SL 1.26); BNBUSDT short @ 703.16 (TP 698.94 / SL 705.97); SOLUSDT short @ 95.48 (TP 94.91 / SL 95.86)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 01.11 07:02 | DOGEUSDT | short | -1.46 $ | time limit |
| 01.11 04:54 | BTCUSDT | short | -17.54 $ | time limit |
| 01.11 04:15 | SOLUSDT | short | -8.71 $ | time limit |
| 01.11 03:54 | ETHUSDT | short | -28.31 $ | stop |
| 01.11 02:50 | BNBUSDT | short | -14.05 $ | time limit |

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
01.11 02:52 A  CLOSE BNBUSDT time limit: -14.05 USD
01.11 02:52 A  SHORT BTCUSDT 5307 USD x3 @ 77514.74 (ters sinyal, RSI 43)
01.11 03:56 A  CLOSE ETHUSDT stop: -28.31 USD
01.11 04:17 A  CLOSE SOLUSDT time limit: -8.71 USD
01.11 04:54 A  CLOSE BTCUSDT time limit: -17.54 USD
01.11 05:00 A  SHORT DOGEUSDT 5257 USD x3 @ 0.08 (ters sinyal, RSI 44)
01.11 05:23 A  SHORT XRPUSDT 5257 USD x3 @ 1.25 (ters sinyal, RSI 42)
01.11 05:47 A  SHORT BNBUSDT 2628 USD x3 @ 703.16 (ters sinyal, RSI 44)
01.11 07:13 A  CLOSE DOGEUSDT time limit: -1.46 USD
01.11 07:13 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
01.11 07:16 A  SHORT SOLUSDT 5252 USD x3 @ 95.48 (ters sinyal, RSI 43)
01.11 07:16 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
01.11 07:18 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
01.11 07:21 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
01.11 07:24 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
