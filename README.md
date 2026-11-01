# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 02.11.2026 02:14 (İstanbul)

## Bot A — Kripto TERS (alım sinyalinde satış, x3)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -56.80 $ | -811.94 $ |
| İşlem sayısı | 3 | 64 |
| Kazanma oranı | %0.0 | %18.8 |
| Ödenen komisyon/spread | 12.71 $ | 288.30 $ |

**Hesap değeri: 4,181.54 $** (başlangıç 5,000 $, -818.46 $ / %-16.37)

Açık pozisyonlar: BNBUSDT short @ 708.05 (TP 703.80 / SL 710.88)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 02:14 | XRPUSDT | short | -13.35 $ | stop |
| 02.11 02:14 | SOLUSDT | short | -26.91 $ | stop |
| 02.11 01:04 | ETHUSDT | short | -16.55 $ | time limit |
| 01.11 23:42 | BNBUSDT | short | +1.80 $ | time limit |
| 01.11 23:39 | BTCUSDT | short | -1.11 $ | time limit |

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
02.11 01:04 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 01:07 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 01:10 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 01:53 A  SHORT SOLUSDT 5074 USD x3 @ 93.99 (ters sinyal, RSI 44)
02.11 01:53 A  SHORT XRPUSDT 2517 USD x3 @ 1.25 (ters sinyal, RSI 39)
02.11 01:53 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 01:56 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 01:59 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 02:02 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 02:05 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 02:08 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 02:11 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 02:14 A  CLOSE SOLUSDT stop: -26.91 USD
02.11 02:14 A  CLOSE XRPUSDT stop: -13.35 USD
02.11 02:14 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
