# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 02:39 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -69.89 $ | -320.17 $ |
| İşlem sayısı | 8 | 24 |
| Kazanma oranı | %37.5 | %29.2 |
| Ödenen komisyon/spread | 39.72 $ | 109.40 $ |

**Hesap değeri: 4,668.60 $** (başlangıç 5,000 $, -331.40 $ / %-6.63)

Açık pozisyonlar: BTCUSDT long @ 78592.87 (TP 79064.43 / SL 78278.50); SOLUSDT long @ 96.37 (TP 96.95 / SL 95.98); XRPUSDT long @ 1.24 (TP 1.25 / SL 1.24)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 02:03 | DOGEUSDT | long | -15.11 $ | stop |
| 30.10 02:02 | XRPUSDT | long | -30.23 $ | stop |
| 30.10 02:03 | SOLUSDT | long | -30.23 $ | stop |
| 30.10 01:27 | SOLUSDT | long | +13.21 $ | take profit |
| 30.10 01:24 | ETHUSDT | long | +26.42 $ | take profit |

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

**Hesap değeri: 100,151.28 $** (başlangıç 100,000 $, +151.28 $ / %+0.15)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
30.10 02:00 A  CLOSE ETHUSDT take profit: +26.42 USD
30.10 02:00 A  CLOSE SOLUSDT take profit: +13.21 USD
30.10 02:00 A  BUY SOLUSDT 5706 USD x3 @ 97.11 (RSI 42)
30.10 02:00 A  BUY XRPUSDT 5706 USD x3 @ 1.25 (RSI 38)
30.10 02:00 A  BUY DOGEUSDT 2853 USD x3 @ 0.08 (RSI 43)
30.10 02:00 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 02:00 N  NEWS (17 new) score -0.15 conf 0.35: Fed faizini %3.75-4 bandında sabit tuttu (beklenen duruş), enflasyonun yeniden yükselmesi ve güçlü ABD büyümesi faiz artırımı beklentilerini canlı tutarak altı baskılıyor. Buna karşılık İran savaşındaki ölümler ve Asya'da güvenli liman talebi altı destekliyor; bu nedenle net etki hafif negatif ve düşük güvenilirlikli.
30.10 02:39 A  CLOSE SOLUSDT stop: -30.23 USD
30.10 02:39 A  CLOSE XRPUSDT stop: -30.23 USD
30.10 02:39 A  CLOSE DOGEUSDT stop: -15.11 USD
30.10 02:39 A  BUY BTCUSDT 5616 USD x3 @ 78592.87 (RSI 39)
30.10 02:39 A  BUY SOLUSDT 5616 USD x3 @ 96.37 (RSI 42)
30.10 02:39 A  BUY XRPUSDT 2808 USD x3 @ 1.24 (RSI 44)
30.10 02:39 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 02:39 N  NEWS (17 new) score -0.60 conf 0.70: Yeni başlıklar ağırlıklı olarak altın için baskılayıcı: PCE verisi Aralık faiz artırımı ihtimalini güçlendirdi, Lacker Fed'in enflasyon eğrisinin gerisinde kaldığını söylüyor ve GSYH 3,4% ile beklentileri aştı. Jeopolitik (İran savaşı, Rusya-Avrupa gerilimi) güvenli liman talebini destekliyor, ancak bu etki faiz beklentilerinin gölgesinde kalıyor; ayrıca bazı başlıklar eski veya çelişkili (dolar ve tahvil getirilerinin düşmesi).
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
