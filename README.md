# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 13:05 (İstanbul)

## Bot A — Kripto kurallar (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.30 $ | +0.30 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %100.0 | %100.0 |
| Ödenen komisyon/spread | 2.00 $ | 2.00 $ |

**Hesap değeri: 5,000.30 $** (başlangıç 5,000 $, +0.30 $ / %+0.01)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 09:46 | ETHUSDT | long | +0.30 $ | time limit |

## Bot A2 — Kripto: sert düşüş sonrası toparlanma (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot B1 — Altın + haber (şimdiki ayarlar, TP 5$ / SL 3$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -35.35 $ | -31.54 $ |
| İşlem sayısı | 18 | 19 |
| Kazanma oranı | %27.8 | %31.6 |
| Ödenen komisyon/spread | 42.71 $ | 45.08 $ |

**Hesap değeri: 4,968.46 $** (başlangıç 5,000 $, -31.54 $ / %-0.63)

Son haber analizi (23.10 13:05): puan **-0.50**, güven 0.60 — Altın 4.000 dolar seviyesinin altına inmiş durumda; Fed faiz artırımı beklentileri, güçlü dolar ve yükselen Treasury getirileri altını baskılıyor. Petrol 113 doların üzerinde olduğu için enflasyon kaygısı sürüyor, İran savaşı ise güvenli liman talebini belirgin biçimde artırmadığı için bu baskıyı dengeleyemiyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 11:23 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 11:01 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 10:16 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 10:02 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 09:48 | PAXGUSDT | short | -4.19 $ | stop |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -30.94 $ | -30.94 $ |
| İşlem sayısı | 5 | 5 |
| Kazanma oranı | %20.0 | %20.0 |
| Ödenen komisyon/spread | 11.86 $ | 11.86 $ |

**Hesap değeri: 4,969.06 $** (başlangıç 5,000 $, -30.94 $ / %-0.62)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 08:32 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 05:27 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 04:52 | PAXGUSDT | short | +13.82 $ | take profit |
| 23.10 03:57 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B4 — Altın: haberin TERSİ (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 4,998.90 $** (başlangıç 5,000 $, -1.10 $ / %-0.02)

Açık pozisyonlar: PAXGUSDT long @ 4038.25 (TP 4050.36 / SL 4030.17)

## Bot B3 — Altın: B2 + seans filtresi + momentum + kârı koruma

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -11.19 $ | -11.19 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 4,988.81 $** (başlangıç 5,000 $, -11.19 $ / %-0.22)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |

## Son olaylar

```
23.10 11:18 B1  SHORT gold 5000 USD x10 @ 4029.04 (TP 4025.01, SL 4031.46; news -0.50)
23.10 11:27 B1  CLOSE short stop: -4.19 USD
23.10 11:27 N  NEWS (9 new) score -0.70 conf 0.70: Petrol fiyatlarındaki yükseliş enflasyon endişelerini ve Fed faiz artırımı beklentilerini besliyor, dolar güçleniyor ve altın üç aylık dipte. Jeopolitik risk (İran savaşı) var ama güvenli liman talebi bu baskıyı dengelemiyor; yine de veri/Fed açıklamaları sürpriz getirebileceğinden güven orta düzeyde.
23.10 11:36 N  NEWS (7 new) score -0.50 conf 0.60: Altın 3 aylık dibe yakın (~4.015$) işlem görüyor; petrol yükselişi enerji kaynaklı enflasyon ve Fed sıkılaştırma beklentilerini besliyor, Warsh'ın yeni faiz artışı sinyali verebileceği haberi ve güçlü dolar altın için baskılayıcı. Buna karşın İran savaşı ve jeopolitik risk, ayrıca 10 yıllık tahvil getirisinin sert düşüşü gibi karşıt unsurlar olduğundan güven orta düzeyde.
23.10 11:48 N  NEWS (5 new) score -0.60 conf 0.70: Petrol kaynaklı enflasyon endişeleri ve Fed'in faiz artırımı beklentileri (Warsh'ın daha fazla hikaye işaret etmesi, Fed'in yüksek enflasyon tahmini) altın için baskılayıcı; dolar ve getiriler de güçlü. Jeopolitik risk (İran, Ukrayna) güvenli liman talebini kısmen destekleyebilir ancak doların güvenli liman rolünü kaybettiği haberi bu etkiyi zayıflatıyor.
23.10 11:48 B2  CLOSE short stop: -11.19 USD
23.10 11:48 B3  CLOSE short stop: -11.19 USD
23.10 11:57 N  NEWS (7 new) score -0.45 conf 0.55: Petrol kaynaklı enflasyon ve Warsh'un ek faiz artırımı sinyali, altın için 3 aylık dip yakınında baskı yaratıyor; ABD doları da güvenli liman rolünü kaybettiği için altı destekleyen bir etken yok. Ancak 10 yıllık tahvil getirisindeki sert düşüş ve jeopolitik riskler (İran savaşı) kısa vadede dengeleyici olabileceğinden güven orta düzeyde tutuldu.
23.10 12:02 B4  LONG gold 5000 USD x10 @ 4038.25 (TP 4050.36, SL 4030.17; news +0.45)
23.10 12:11 N  NEWS (10 new) score -0.50 conf 0.60: Petrol 113 doların üzerine çıkarak enflasyon ve faiz artışı beklentilerini besliyor; Warsh'ın daha fazla faiz artırımına işaret etmesi ve altının 3 aylık dibe gelmesi baskıyı artırıyor. Savaş haberleri ve güvenli liman talebi ise sınırlı kalıyor, dolar da güvenli liman rolünü kaybetmiş görünüyor; bu nedenle beklenen etki negatif, ancak haberlerin bir kısmı zaten fiyatlanmış olabilir.
23.10 12:26 N  NEWS (13 new) score -0.50 conf 0.60: 
23.10 12:38 N  NEWS (8 new) score -0.55 conf 0.60: Altın 4.000 doların altına indi ve düşüş sürüyor. Faiz artışı beklentileri (BofA'nın 2026'da iki ek faiz artışı öngörüsü, Warsh'un daha fazla artış sinyali vermesi), yükselen tahvil getirileri ve petrolün 113 doların üzerine çıkmasından doğan enflasyon kaygısı altın için baskılayıcı. Savaş kaynaklı güvenli liman talebi zayıf kalıyor çünkü "dolar güvenli liman taclarını kaybetti" yorumu ve hisse senedi satışı önemli bir destek sağlamıyor. Teknik kırılma ve haber akışındaki çelişkiler nedeniyle güven orta düzeyde tutuldu.
23.10 12:47 N  NEWS (13 new) score -0.60 conf 0.60: Altın 4.000 dolar seviyesinin altına inmiş, üç aylık dibe yakın ve haftalık kayıplar sürüyor; Fed'in faiz artırma beklentileri (BofA iki ek artırım, Warsh'un sıkılaştırma sinyali), yükselen tahvil getirileri ve güçlü dolar altın üzerinde baskı oluşturuyor. Jeopolitik riskler (İran savaşı, Hürmüz) güvenli liman talebini destekleyebilir ancak bu etki şu an fiyatlarda görünmüyor; Goldman'ın 5.400 dolarlık uzun vadeli hedefi kısa vadeli etkisi olmayan eski bir haber.
23.10 12:55 N  NEWS (4 new) score -0.45 conf 0.60: Altın 4.000 doların altına inmiş durumda; Fed'in faiz artırımı beklentileri, güçlü dolar ve Warsh'un daha fazla sıkılaştırma sinyali vermesi beklentisi reel faiz baskısını artırıp altına negatif yansıyor. Yeni gelen haberlerin çoğu (Lockheed backlog, Batı Şeria saldırısı, peso rekor düşüşü) altın için doğrudan etkisi zayıf; jeopolitik risk-off talebi ise bu baskıyı tam dengeleyecek kadar güçlü görünmüyor.
23.10 13:05 N  NEWS (6 new) score -0.50 conf 0.60: Altın 4.000 dolar seviyesinin altına inmiş durumda; Fed faiz artırımı beklentileri, güçlü dolar ve yükselen Treasury getirileri altını baskılıyor. Petrol 113 doların üzerinde olduğu için enflasyon kaygısı sürüyor, İran savaşı ise güvenli liman talebini belirgin biçimde artırmadığı için bu baskıyı dengeleyemiyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
