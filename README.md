# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 10:13 (İstanbul)

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
| Net kâr/zarar | -22.79 $ | -18.98 $ |
| İşlem sayısı | 15 | 16 |
| Kazanma oranı | %33.3 | %37.5 |
| Ödenen komisyon/spread | 35.59 $ | 37.96 $ |

**Hesap değeri: 4,979.84 $** (başlangıç 5,000 $, -20.16 $ / %-0.40)

Açık pozisyonlar: PAXGUSDT short @ 4028.24 (TP 4024.22 / SL 4030.66)

Son haber analizi (23.10 10:11): puan **-0.45**, güven 0.55 — Altın 4.000 doların altına inip Temmuz'dan beri en düşük seviyeye yakın işlem görüyor; petrol şoku enflasyon ve Fed faiz artırımı beklentilerini canlandırıyor, dolar güçlü. Ancak 10 yıllık tahvil getirisinin sert düşüşü ve İran savaşı kaynaklı güvenli liman talebi kısmen destek sağlayabileceği için sinyal karışık ve güven sınırlı.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 10:02 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 09:48 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 08:08 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 07:47 | PAXGUSDT | short | +3.81 $ | take profit |
| 23.10 07:02 | PAXGUSDT | short | +3.81 $ | take profit |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -19.75 $ | -19.75 $ |
| İşlem sayısı | 4 | 4 |
| Kazanma oranı | %25.0 | %25.0 |
| Ödenen komisyon/spread | 9.49 $ | 9.49 $ |

**Hesap değeri: 4,979.33 $** (başlangıç 5,000 $, -20.67 $ / %-0.41)

Açık pozisyonlar: PAXGUSDT short @ 4028.45 (TP 4016.37 / SL 4036.51)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 08:32 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 05:27 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 04:52 | PAXGUSDT | short | +13.82 $ | take profit |
| 23.10 03:57 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B3 — Altın: B2 + seans filtresi + momentum + kârı koruma

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Son olaylar

```
23.10 08:59 N  NEWS (7 new) score -0.45 conf 0.60: Petrol kaynaklı enflasyon endişeleri ve Fed'in 2026'da iki kez daha faiz artırabileceği beklentisi (BofA), reel faiz ve dolar tarafında altın için baskı yaratıyor; gold haftalık kayıp yaşıyor ve Fed kararı öncesi düşüş sürüyor. Hormuz'daki saldırıların artması ve İran savaşı güvenli liman talebini destekleyebilir, ancak piyasa bu riski şu an enflasyon kanalının gerisinde bırakıyor; bu nedenle güven orta düzeyde.
23.10 09:11 N  NEWS (11 new) score -0.40 conf 0.60: Petrol kaynaklı enflasyon endişeleri ve Fed'in faiz artırımı beklentileri (BofA: 2026'da iki artış) altını baskılıyor; dolar da toparlanıyor. İran savaşı ve Hormuz saldırıları jeopolitik risk yaratsa da altın bu haberlere güvenli liman olarak tepki vermiyor, bu nedenle kısa vadede negatif eğilim baskın.
23.10 09:18 N  NEWS (7 new) score -0.50 conf 0.60: Petrol kaynaklı enflasyon endişeleri Fed faiz artırımı beklentilerini güçlendiriyor ve dolar/reel faizler altını baskılıyor; altın haftalık kayıp yolunda. İran savaşı ve Hormuz'daki saldırılar güvenli liman talebini destekliyor olsa da piyasa şu an bu etkiyi faiz kanalının gerisinde bırakıyor.
23.10 09:29 N  NEWS (7 new) score -0.60 conf 0.70: Petrol fiyatlarının yükselmesi Fed faiz artırımı beklentilerini canlandırıyor ve dolar güçleniyor; altın 4.000 doların altına, Temmuz'dan bu yana en düşük seviyeye geriledi. Hormuz'daki saldırılar jeopolitik destek sağlasa da enflasyon/faiz kanalı baskın görünüyor.
23.10 09:41 N  NEWS (10 new) score -0.60 conf 0.60: Petrol kaynaklı enflasyon endişeleri Fed faiz artırımı beklentilerini canlandırıyor ve BofA'nın 2026'da iki kez daha artırım öngörüsü altın üzerinde baskı oluşturuyor. Altın 4.000 doların altına inip temmuzdan bu yana en düşük seviyeye geriledi; ancak düşüş zaten büyük ölçüde fiyatlanmış olabileceğinden ve yeni gelen ABD'nin 'karanlık filo' yaptırımlarını kaldırması gibi haberler petrol arzını gevşetip enflasyon baskısını azaltabileceğinden güven orta düzeyde tutuldu.
23.10 09:41 B1  SHORT gold 5000 USD x10 @ 4028.45 (TP 4024.43, SL 4030.87; news -0.60)
23.10 09:41 B2  SHORT gold 5000 USD x10 @ 4028.45 (TP 4016.37, SL 4036.51; news -0.60)
23.10 09:50 A  CLOSE ETHUSDT time limit: +0.30 USD
23.10 09:50 B1  CLOSE short stop: -4.19 USD
23.10 09:50 N  NEWS (9 new) score -0.60 conf 0.65: Altın 4.000 doların altına inip Temmuz'dan bu yana en düşük seviyeye geriledi; petrol kaynaklı enflasyon endişeleri Fed faiz artırımı beklentilerini canlandırıyor ve BofA 2026'da iki kez daha artırım öngörüyor. Bu hawkish beklentiler ve güçlü dolar 1-4 saatlik vadede altı baskılıyor, ancak İran savaşının sürmesi ve Hürmüz'deki saldırılar güvenli liman talebini destekleyerek düşüşü sınırlayabilir.
23.10 09:59 N  NEWS (3 new) score -0.60 conf 0.70: Altın 4.000 doların altına inip temmuzdan bu yana en düşük seviyeye geriledi; petrol fiyatlarındaki yükseliş enflasyon ve Fed faiz artırımı beklentilerini canlandırıyor, Fed'in 2026'da iki kez daha artırabileceği yönündeki tahminler reel faizleri ve doları destekleyerek altını baskılıyor. İran savaşı ve Hürmüz'deki saldırılar güvenli liman talebini destekliyor olsa da piyasa şu an bu etkiyi faiz kanalının gerisinde bırakıyor; Fed soruşturmasının kapatılması ise etkisi sınırlı bir haber.
23.10 09:59 B1  SHORT gold 5000 USD x10 @ 4026.67 (TP 4022.65, SL 4029.09; news -0.60)
23.10 10:11 B1  CLOSE short stop: -4.19 USD
23.10 10:11 N  NEWS (8 new) score -0.45 conf 0.55: Altın 4.000 doların altına inip Temmuz'dan beri en düşük seviyeye yakın işlem görüyor; petrol şoku enflasyon ve Fed faiz artırımı beklentilerini canlandırıyor, dolar güçlü. Ancak 10 yıllık tahvil getirisinin sert düşüşü ve İran savaşı kaynaklı güvenli liman talebi kısmen destek sağlayabileceği için sinyal karışık ve güven sınırlı.
23.10 10:13 B1  SHORT gold 5000 USD x10 @ 4028.24 (TP 4024.22, SL 4030.66; news -0.45)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
