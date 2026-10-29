# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 01:17 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -60.38 $ | -310.66 $ |
| İşlem sayısı | 2 | 18 |
| Kazanma oranı | %0.0 | %22.2 |
| Ödenen komisyon/spread | 11.37 $ | 81.05 $ |

**Hesap değeri: 4,678.08 $** (başlangıç 5,000 $, -321.92 $ / %-6.44)

Açık pozisyonlar: BTCUSDT long @ 78738.42 (TP 79210.85 / SL 78423.47); ETHUSDT long @ 2262.36 (TP 2275.93 / SL 2253.31); SOLUSDT long @ 96.92 (TP 97.50 / SL 96.53)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 00:43 | DOGEUSDT | long | -30.19 $ | stop |
| 30.10 00:41 | BNBUSDT | long | -30.19 $ | stop |
| 29.10 23:57 | BNBUSDT | long | +13.51 $ | take profit |
| 29.10 23:58 | ETHUSDT | long | -30.49 $ | stop |
| 29.10 23:58 | BTCUSDT | long | -30.49 $ | stop |

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

**Hesap değeri: 99,623.79 $** (başlangıç 100,000 $, -376.21 $ / %-0.38)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
29.10 23:54 N  NEWS (33 new) score +0.12 conf 0.35: Jeopolitik risk (İran savaşının yeniden başlatılma planı, ABD askeri kayıpları, Ukrayna-Rusya gerilimi) ve doların zayıflaması altını hafifçe destekliyor. Buna karşılık, güçlü GDP büyümesi ve yeniden hızlanan enflasyon, Warsh'ın Fed faiz yaklaşımındaki değişiklik belirsizliği nedeniyle gerçek faiz beklentilerini yukarı çekebilir; bu da altı baskılayabilir. Haberler karışık ve büyük bölümü zaten fiyatlanmış olduğu için güven düşük.
30.10 00:34 A  CLOSE BTCUSDT stop: -30.49 USD
30.10 00:34 A  CLOSE ETHUSDT stop: -30.49 USD
30.10 00:34 A  CLOSE BNBUSDT take profit: +13.51 USD
30.10 00:34 A  BUY BNBUSDT 5700 USD x3 @ 711.89 (RSI 42)
30.10 00:34 A  BUY DOGEUSDT 5700 USD x3 @ 0.08 (RSI 41)
30.10 00:34 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 00:34 N  NEWS (22 new) score -0.60 conf 0.60: Yeni başlıklar ağırlıklı olarak altın için negatif: sıcak enflasyon ve güçlü ABD GSYH verisi Fed sıkılaştırma beklentilerini artırıyor, gold ve gümüş düşüşte, ve piyasa çöküşü güvenli liman talebi yaratmadı. İran savaşı ve jeopolitik riskler ise destekleyici olabilir, ama bu haberler kısmen fiyatlanmış ve yeni bir tırmanış sinyali net değil; bu nedenle güven orta düzeyde.
30.10 01:17 A  CLOSE BNBUSDT stop: -30.19 USD
30.10 01:17 A  CLOSE DOGEUSDT stop: -30.19 USD
30.10 01:17 A  BUY BTCUSDT 5627 USD x3 @ 78738.42 (RSI 34)
30.10 01:17 A  BUY ETHUSDT 5627 USD x3 @ 2262.36 (RSI 40)
30.10 01:17 A  BUY SOLUSDT 2814 USD x3 @ 96.92 (RSI 41)
30.10 01:17 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 01:17 N  NEWS (26 new) score -0.50 conf 0.60: Güçlü ABD büyüme verisi (Q3 %3,4) ve enflasyon verisi Fed'in sıkılaşma beklentilerini artırıyor; bu reel faiz ve dolar tarafından altı baskılıyor ve altın zaten düşüşte. İran savaşıyla ilgili jeopolitik haberler (Patriot sistemi kayması, olası saldırı) güvenli liman talebini destekleyebilir, ancak bu etki kısa vadede hawkish veriyi dengeleyecek kadar güçlü görünmüyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
