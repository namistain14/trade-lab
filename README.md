# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 14:03 (İstanbul)

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

**Hesap değeri: 4,917.05 $** (başlangıç 5,000 $, -82.95 $ / %-1.66)

Açık pozisyonlar: PAXGUSDT short @ 3990.55 (TP 3978.58 / SL 3998.53)

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

**Hesap değeri: 97,687.20 $** (başlangıç 100,000 $, -2312.80 $ / %-2.31)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
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
30.10 13:17 N  NEWS (24 new) score -0.25 conf 0.40: 
30.10 13:17 N  GPT  score -0.20 conf 0.36: Altın, Fed faiz artırımı beklentileri ve zorunlu satışlarla baskı altında; doların zorlanması ve düşen tahvil getirileri bu baskıyı kısmen dengeliyor. Yeni başlıklarda kısa vadede güvenli liman talebini belirgin artıracak net bir tırmanış görünmüyor.
30.10 13:17 B5  SHORT gold 25000 USD x10 @ 3990.55 (TP 3978.58, SL 3998.53; news -0.23)
30.10 14:03 N  NEWS (22 new) score -0.30 conf 0.50: Yeni haberlerde Fed'in "çok sıcak olmayan" görüşünü sınayan veriler ve faiz artırımı beklentilerini destekleyen büyüme sinyalleri altın için baskı yaratıyor; gold fiyatı da 4.000 doların altına düştü. Iran savaşı ve olası yeni saldırılar güvenli liman talebini destekleyebilir, ancak altın bu jeopolitik gerilime rağmen yükselmiyor, zorunlu tasfiyeler sürüyor ve bu yüzden etki sınırlı kalıyor.
30.10 14:03 N  GPT  score -0.35 conf 0.66: ABD verilerinin Fed’in enflasyon değerlendirmesini sorgulatması ve faiz artışı beklentilerinin güçlenmesi altın üzerinde kısa vadeli baskı yaratıyor; 4.000 doların altına iniş de bu zayıflığı teyit ediyor. İran çevresindeki gerilim güvenli liman talebini destekleyebilir, ancak haber akışı savaşın sü
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
