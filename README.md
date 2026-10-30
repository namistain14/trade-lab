# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 04:28 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -217.43 $ | -467.72 $ |
| İşlem sayısı | 14 | 30 |
| Kazanma oranı | %21.4 | %23.3 |
| Ödenen komisyon/spread | 67.51 $ | 137.19 $ |

**Hesap değeri: 4,532.28 $** (başlangıç 5,000 $, -467.72 $ / %-9.35)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 03:19 | SOLUSDT | long | -14.64 $ | stop |
| 30.10 03:19 | ETHUSDT | long | -29.27 $ | stop |
| 30.10 03:19 | BTCUSDT | long | -29.27 $ | stop |
| 30.10 02:47 | XRPUSDT | long | -14.87 $ | stop |
| 30.10 02:47 | SOLUSDT | long | -29.74 $ | stop |

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

**Hesap değeri: 99,870.81 $** (başlangıç 100,000 $, -129.19 $ / %-0.13)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
30.10 02:39 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 02:39 N  NEWS (17 new) score -0.60 conf 0.70: Yeni başlıklar ağırlıklı olarak altın için baskılayıcı: PCE verisi Aralık faiz artırımı ihtimalini güçlendirdi, Lacker Fed'in enflasyon eğrisinin gerisinde kaldığını söylüyor ve GSYH 3,4% ile beklentileri aştı. Jeopolitik (İran savaşı, Rusya-Avrupa gerilimi) güvenli liman talebini destekliyor, ancak bu etki faiz beklentilerinin gölgesinde kalıyor; ayrıca bazı başlıklar eski veya çelişkili (dolar ve tahvil getirilerinin düşmesi).
30.10 03:16 A  CLOSE BTCUSDT stop: -29.74 USD
30.10 03:16 A  CLOSE SOLUSDT stop: -29.74 USD
30.10 03:16 A  CLOSE XRPUSDT stop: -14.87 USD
30.10 03:16 A  BUY BTCUSDT 5527 USD x3 @ 77803.93 (RSI 22)
30.10 03:16 A  BUY ETHUSDT 5527 USD x3 @ 2242.76 (RSI 32)
30.10 03:16 A  BUY SOLUSDT 2763 USD x3 @ 95.35 (RSI 32)
30.10 03:16 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 03:16 N  NEWS (18 new) score -0.50 conf 0.60: Fed faizleri sabit tuttu ancak Warsh'un mesajları ve sıcak PCE/enflasyon verisi Aralık faiz artırımı beklentisini güçlendirdi; bu, reel faizler ve doların tarafından gold üzerinde baskı yaratıyor. İran savaşı kaynaklı güvenli liman talebi var ama haberlerde altın yerine tahvillere yönelim görülüyor, bu nedenle net etki negatif.
30.10 04:28 A  CLOSE BTCUSDT stop: -29.27 USD
30.10 04:28 A  CLOSE ETHUSDT stop: -29.27 USD
30.10 04:28 A  CLOSE SOLUSDT stop: -14.64 USD
30.10 04:28 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 04:28 N  NEWS (26 new) score -0.50 conf 0.60: Sıcak ABD enflasyon verisi (çekirdek PCE %3.1), güçlü GSYH ve Aralık ayında Fed faiz artırımı beklentilerinin yükselmesi, dolar ve reel faizler üzerinden altı baskılıyor; haberlerde altının 4.000 dolar civarına gerilediği ve düşüş yönlü teknik görünüm de yer alıyor. İran savaşı ve jeopolitik gerilim güvenli liman talebi yaratarak kısmen destekleyici olsa da, bu etki şu an dominant hawkish Fed mesajının gerisinde kalıyor; bu nedenle 1-4 saatlik görünüm negatif.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
