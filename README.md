# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 12:21 (İstanbul)

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
| Net kâr/zarar | -55.95 $ | -98.75 $ |
| İşlem sayısı | 1 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 11.88 $ | 47.48 $ |

**Hesap değeri: 4,901.25 $** (başlangıç 5,000 $, -98.75 $ / %-1.97)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 11:54 | PAXGUSDT | short | -55.95 $ | stop |
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

**Hesap değeri: 99,559.20 $** (başlangıç 100,000 $, -440.80 $ / %-0.44)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
30.10 07:04 N  NEWS (20 new) score -0.60 conf 0.70: Yüksek ABD enflasyonu, güçlü GDP ve yükselen petrol fiyatları Fed faiz artırımı beklentilerini güçlendirerek altını baskılıyor; dolar da destek buluyor. İran savaşı ve Husi saldırıları güvenli liman talebi yaratsa da, bu etki haber akışında zayıf kalıyor ve ABD-İran müzakere umutları jeopolitik primi sınırlıyor.
30.10 07:51 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 07:51 N  NEWS (21 new) score -0.60 conf 0.70: Sıcak PCE enflasyonu, güçlü ABD GSYH verisi ve Aralık'ta Fed faiz artırımı bahisleri altını baskılıyor; altın 4.000 doların altına sarkmış durumda. İran savaşı kaynaklı güvenli liman talebi ve petrol fiyatlarındaki yükseliş bir miktar destek sağlasa da, faiz beklentilerinin etkisi bu desteği belirgin biçimde geride bırakıyor.
30.10 08:33 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 08:33 N  NEWS (24 new) score -0.50 conf 0.60: Sıcak PCE enflasyonu ve güçlü ABD verileri Aralık'ta Fed faiz artırımı beklentilerini güçlendirerek altın üzerinde baskı yaratıyor; altın 4.000 doların altına indi. İran savaşı ve Asya'daki güvenli liman talebi kısmen destek olsa da, bu etki haber akışında sınırlı kalıyor ve faiz beklentisinin gerisinde kalıyor.
30.10 09:18 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 09:18 N  NEWS (21 new) score -0.60 conf 0.70: Sıcak PCE enflasyonu ve yükselen petrol fiyatları, Fed faiz artırımı beklentilerini güçlendiriyor; güçlenen majör para birimleri ve Fed'in faizleri sabit tutması da altını baskılıyor. İran savaşı ve ABD askeri kayıpları güvenli liman talebi yaratabilir, ancak piyasada altın bu jeopolitik riske rağmen düşüyor, bu da baskının daha belirleyici olduğunu gösteriyor.
30.10 10:29 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
30.10 10:29 N  NEWS (23 new) score -0.50 conf 0.60: Sıcak PCE enflasyonu ve Fed'de faiz artırımı beklentilerinin güçlenmesi, reel faizleri ve doları destekleyerek altın üzerinde baskı yaratıyor; altın 4.000 doların altına sarkmış durumda. İran savaşı ve jeopolitik riskler güvenli liman talebini artırabilir, ancak bu etki şu an faiz beklentilerinin gerisinde kalıyor.
30.10 11:25 N  NEWS (33 new) score -0.60 conf 0.70: Yüksek enerji fiyatları ve ABD enflasyon verisi (PCE) Fed'in faiz artırma beklentilerini güçlendiriyor; altın 4.000 doların altına indi ve dolar/tahvil tarafında baskı sürüyor. Jeopolitik haberler (İran savaşı, Ukrayna) güvenli liman talebi yaratsa da, bu etki faiz beklentilerinin gerisinde kalıyor.
30.10 11:25 N  GPT  score -0.35 conf 0.66: Yükselen petrol ve güçlü enflasyon verilerinin Fed faiz artışı beklentilerini beslemesi, altını kısa vadede baskılıyor; fiyatın 4.000 doların altına gerilediğine dair başlıklar bu eğilimi destekliyor. Doların zayıflaması ve Rusya-Ukrayna kaynaklı güvenli liman talebi düşüşü sınırlayabilir.
30.10 11:25 B5  SHORT gold 25000 USD x10 @ 3994.28 (TP 3982.30, SL 4002.27; news -0.47)
30.10 12:21 B5  CLOSE short stop: -55.95 USD
30.10 12:21 N  NEWS (33 new) score -0.45 conf 0.60: Haberlerin çoğu altın için baskı yaratıyor: Fed faiz artırımı beklentileri, yüksek petrol ve ABD enflasyon verisi, altının 4.000 dolar altına inmesi ve spot talepteki zayıflık. Jeopolitik risk (İran savaşı, Asya'da risk-off ve tahvil talebi) kısmen destek sağlasa da, bu etki Fed beklentilerinin gerisinde kalıyor; DXY'deki gerileme ise sınırlı bir destek sunuyor.
30.10 12:21 N  GPT  score -0.58 conf 0.68: Altının 4.000 doların altına gerilemesi ve yüksek petrol/enflasyonun Fed faiz artırımı beklentilerini güçlendirmesi kısa vadede belirgin baskı yaratıyor. Düşen tahvil getirileri ve DXY’deki zorlanma ile jeopolitik riskler bu baskıyı kısmen sınırlıyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
