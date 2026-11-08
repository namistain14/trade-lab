# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 08.11.2026 15:22 (İstanbul)

## Bot A — Kripto 1 saatlik trend (x1)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -455.77 $ |
| İşlem sayısı | 0 | 64 |
| Kazanma oranı | %0.0 | %39.1 |
| Ödenen komisyon/spread | 0.00 $ | 759.67 $ |

**Hesap değeri: 4,544.23 $** (başlangıç 5,000 $, -455.77 $ / %-9.12)

Son haber analizi (06.11 20:10): Claude puan **-0.50**, güven 0.60 — Yeni haberlerin ağırlıklı tonu şahin: beklentilerin üzerinde güçlü istihdam (165 bin), işsizlik oranının 4,1%'e gerilemesi, Fed'in Aralık'ta faiz artırımı beklentisinin güçlenmesi ve Fed yetkililerinin enflasyon uyarıları, doların yükselişiyle birlikte altın için baskı yaratıyor. İran savaşına ilişkin güvenli liman talebi destekleyici olsa da bu haberler büyük ölçüde fiyatlanmış ve eskidir; bu nedenle etkisi sınırlı kalır.

GPT (gpt-6-luna): puan **-0.45**, güven 0.64 — Beklentiyi aşan istihdam ve güçlenen Aralık faiz artırımı beklentisi, dolar ile reel faizleri destekleyerek altın üzerinde kısa vadeli baskı oluşturuyor. İran gerilimi ve tanker saldırısı güvenli liman talebini destekleyebilir, ancak şu anki makro sinyaller daha ağır basıyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 18:11 | PAXGUSDT | short | -55.94 $ | stop |
| 06.11 17:47 | PAXGUSDT | short | -55.94 $ | stop |
| 06.11 17:25 | PAXGUSDT | short | -55.94 $ | stop |
| 06.11 17:11 | PAXGUSDT | short | +69.09 $ | take profit |
| 06.11 16:31 | PAXGUSDT | short | +69.09 $ | take profit |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -55.58 $ |
| İşlem sayısı | 0 | 3 |
| Kazanma oranı | %0.0 | %33.3 |
| Ödenen komisyon/spread | 0.00 $ | 52.30 $ |

**Hesap değeri: 4,944.42 $** (başlangıç 5,000 $, -55.58 $ / %-1.11)

Son haber analizi (07.11 00:20): Claude puan **-0.15**, güven 0.40 — Haberler karışık: ABD-İran arasında anlaşmaya yakın olunduğu ve diplomasi umutlarının petrol vadeli işlemlerini düşürdüğü bildiriliyor, bu kısa vadede baskı yaratıyor. Buna karşılık Trump'ın savaşın yeniden başlatılmasına ilişkin kararının "yakında" açıklanacağı, Hürmüz Boğazı'ndaki aksamalar ve Citi'nin 150 dolara kadar tahmini ile UBS'in düşük envanter uyarısı fiyatı destekliyor; yeni İran yaptırımları ise büyük ölçüde rutin ve zaten fiyatlanmış.

GPT (gpt-6-luna): puan **-0.20**, güven 0.42 — İran’la görüşmelerde ilerleme ve diplomasi beklentisi, yakın vadede petrol fiyatları üzerinde hafif aşağı yönlü baskı yaratıyor. Ancak Hürmüz’deki kesinti riski ve tanker saldırısı olası düşüşü sınırlıyor; yeni yaptırımların kısa vadeli arz etkisi ise belirsiz.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 22:41 | BZ=F | long | -63.26 $ | stop (gap) |
| 06.11 08:11 | BZ=F | long | -58.75 $ | stop |
| 02.11 23:09 | BZ=F | short | +66.43 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +7633.95 $ |
| İşlem sayısı | 0 | 28 |
| Kazanma oranı | %0.0 | %46.4 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 109,993.83 $** (başlangıç 100,000 $, +9993.83 $ / %+9.99)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 23:47 | SPY | long | -268.92 $ | seans sonu |
| 06.11 23:47 | QQQ | long | -39.36 $ | seans sonu |
| 06.11 23:47 | NVDA | long | -26.55 $ | seans sonu |
| 06.11 23:47 | AAPL | long | -190.06 $ | seans sonu |
| 06.11 20:38 | NVDA | short | +1687.56 $ | take profit |

## Son olaylar

```
08.11 14:42 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 14:45 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 14:48 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 14:51 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 14:54 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 14:57 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 15:00 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 15:01 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 15:04 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 15:07 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 15:10 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 15:13 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 15:16 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 15:19 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
08.11 15:22 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
