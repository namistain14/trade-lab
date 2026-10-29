# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 02:00 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +5.68 $ | -244.61 $ |
| İşlem sayısı | 5 | 21 |
| Kazanma oranı | %60.0 | %33.3 |
| Ödenen komisyon/spread | 25.48 $ | 95.16 $ |

**Hesap değeri: 4,743.98 $** (başlangıç 5,000 $, -256.02 $ / %-5.12)

Açık pozisyonlar: SOLUSDT long @ 97.11 (TP 97.69 / SL 96.72); XRPUSDT long @ 1.25 (TP 1.25 / SL 1.24); DOGEUSDT long @ 0.08 (TP 0.08 / SL 0.08)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 01:27 | SOLUSDT | long | +13.21 $ | take profit |
| 30.10 01:24 | ETHUSDT | long | +26.42 $ | take profit |
| 30.10 01:25 | BTCUSDT | long | +26.42 $ | take profit |
| 30.10 00:43 | DOGEUSDT | long | -30.19 $ | stop |
| 30.10 00:41 | BNBUSDT | long | -30.19 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -42.80 $ |
| İşlem sayısı | 0 | 3 |
| Kazanma oranı | %0.0 | %33.3 |
| Ödenen komisyon/spread | 0.00 $ | 35.60 $ |

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

**Hesap değeri: 100,377.77 $** (başlangıç 100,000 $, +377.77 $ / %+0.38)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
30.10 01:17 A  CLOSE BNBUSDT stop: -30.19 USD
30.10 01:17 A  CLOSE DOGEUSDT stop: -30.19 USD
30.10 01:17 A  BUY BTCUSDT 5627 USD x3 @ 78738.42 (RSI 34)
30.10 01:17 A  BUY ETHUSDT 5627 USD x3 @ 2262.36 (RSI 40)
30.10 01:17 A  BUY SOLUSDT 2814 USD x3 @ 96.92 (RSI 41)
30.10 01:17 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 01:17 N  NEWS (26 new) score -0.50 conf 0.60: Güçlü ABD büyüme verisi (Q3 %3,4) ve enflasyon verisi Fed'in sıkılaşma beklentilerini artırıyor; bu reel faiz ve dolar tarafından altı baskılıyor ve altın zaten düşüşte. İran savaşıyla ilgili jeopolitik haberler (Patriot sistemi kayması, olası saldırı) güvenli liman talebini destekleyebilir, ancak bu etki kısa vadede hawkish veriyi dengeleyecek kadar güçlü görünmüyor.
30.10 02:00 A  CLOSE BTCUSDT take profit: +26.42 USD
30.10 02:00 A  CLOSE ETHUSDT take profit: +26.42 USD
30.10 02:00 A  CLOSE SOLUSDT take profit: +13.21 USD
30.10 02:00 A  BUY SOLUSDT 5706 USD x3 @ 97.11 (RSI 42)
30.10 02:00 A  BUY XRPUSDT 5706 USD x3 @ 1.25 (RSI 38)
30.10 02:00 A  BUY DOGEUSDT 2853 USD x3 @ 0.08 (RSI 43)
30.10 02:00 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 02:00 N  NEWS (17 new) score -0.15 conf 0.35: Fed faizini %3.75-4 bandında sabit tuttu (beklenen duruş), enflasyonun yeniden yükselmesi ve güçlü ABD büyümesi faiz artırımı beklentilerini canlı tutarak altı baskılıyor. Buna karşılık İran savaşındaki ölümler ve Asya'da güvenli liman talebi altı destekliyor; bu nedenle net etki hafif negatif ve düşük güvenilirlikli.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
