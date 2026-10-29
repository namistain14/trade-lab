# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 00:34 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -250.29 $ |
| İşlem sayısı | 0 | 16 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 0.00 $ | 69.68 $ |

**Hesap değeri: 4,740.60 $** (başlangıç 5,000 $, -259.40 $ / %-5.19)

Açık pozisyonlar: BNBUSDT long @ 711.89 (TP 716.16 / SL 709.05); DOGEUSDT long @ 0.08 (TP 0.08 / SL 0.08)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 29.10 23:57 | BNBUSDT | long | +13.51 $ | take profit |
| 29.10 23:58 | ETHUSDT | long | -30.49 $ | stop |
| 29.10 23:58 | BTCUSDT | long | -30.49 $ | stop |
| 29.10 23:03 | XRPUSDT | long | -15.19 $ | stop |
| 29.10 23:04 | BNBUSDT | long | -30.98 $ | stop |

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

**Hesap değeri: 99,477.33 $** (başlangıç 100,000 $, -522.67 $ / %-0.52)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
29.10 23:08 B5  CLOSE short stop: -55.94 USD
29.10 23:08 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
29.10 23:08 N  NEWS (26 new) score -0.35 conf 0.60: Güçlü ABD büyümesi (%3.4 GSYH), 3,1% çekirdek PCE ve Fed'in faizi sabit tutması (10-2) ile sıkı para politikası beklentisi altını baskılıyor. İran ve Ukrayna'daki savaş haberleri güvenli liman talebini destekliyor, ancak bunların büyük kısmı zaten fiyatlanmış durumda; ayrıca Warsh'ın Fed yaklaşımındaki değişiklik yönü belirsiz.
29.10 23:54 A  BUY BTCUSDT 5757 USD x3 @ 79262.02 (RSI 16)
29.10 23:54 A  BUY ETHUSDT 5757 USD x3 @ 2267.56 (RSI 21)
29.10 23:54 A  BUY BNBUSDT 2878 USD x3 @ 698.37 (RSI 7)
29.10 23:54 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
29.10 23:54 N  NEWS (33 new) score +0.12 conf 0.35: Jeopolitik risk (İran savaşının yeniden başlatılma planı, ABD askeri kayıpları, Ukrayna-Rusya gerilimi) ve doların zayıflaması altını hafifçe destekliyor. Buna karşılık, güçlü GDP büyümesi ve yeniden hızlanan enflasyon, Warsh'ın Fed faiz yaklaşımındaki değişiklik belirsizliği nedeniyle gerçek faiz beklentilerini yukarı çekebilir; bu da altı baskılayabilir. Haberler karışık ve büyük bölümü zaten fiyatlanmış olduğu için güven düşük.
30.10 00:34 A  CLOSE BTCUSDT stop: -30.49 USD
30.10 00:34 A  CLOSE ETHUSDT stop: -30.49 USD
30.10 00:34 A  CLOSE BNBUSDT take profit: +13.51 USD
30.10 00:34 A  BUY BNBUSDT 5700 USD x3 @ 711.89 (RSI 42)
30.10 00:34 A  BUY DOGEUSDT 5700 USD x3 @ 0.08 (RSI 41)
30.10 00:34 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 00:34 N  NEWS (22 new) score -0.60 conf 0.60: Yeni başlıklar ağırlıklı olarak altın için negatif: sıcak enflasyon ve güçlü ABD GSYH verisi Fed sıkılaştırma beklentilerini artırıyor, gold ve gümüş düşüşte, ve piyasa çöküşü güvenli liman talebi yaratmadı. İran savaşı ve jeopolitik riskler ise destekleyici olabilir, ama bu haberler kısmen fiyatlanmış ve yeni bir tırmanış sinyali net değil; bu nedenle güven orta düzeyde.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
