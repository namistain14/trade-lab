# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 10:23 (İstanbul)

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
| Net kâr/zarar | -26.98 $ | -23.17 $ |
| İşlem sayısı | 16 | 17 |
| Kazanma oranı | %31.2 | %35.3 |
| Ödenen komisyon/spread | 37.96 $ | 40.34 $ |

**Hesap değeri: 4,976.84 $** (başlangıç 5,000 $, -23.16 $ / %-0.46)

Son haber analizi (23.10 10:23): puan **-0.60**, güven 0.60 — Altın 4.000 doların altına düşerek Temmuz'dan beri en düşük seviyeye geriledi; petrol kaynaklı enflasyon endişeleri Fed faiz artırımı beklentilerini canlandırıyor ve dolar (DXY ~101.5) güçlü seyrediyor. Bu tablo kısa vadede altın için baskılayıcı, ancak AI kaynaklı teknoloji satışı ve 10 yıllık tahvil getirisindeki sert düşüş (19 baz puan) güvenli liman talebi ve gevşeme beklentisi açısından karşıt sinyaller içerdiğinden güveni sınırlı tutuyorum.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 10:16 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 10:02 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 09:48 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 08:08 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 07:47 | PAXGUSDT | short | +3.81 $ | take profit |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -19.75 $ | -19.75 $ |
| İşlem sayısı | 4 | 4 |
| Kazanma oranı | %25.0 | %25.0 |
| Ödenen komisyon/spread | 9.49 $ | 9.49 $ |

**Hesap değeri: 4,979.12 $** (başlangıç 5,000 $, -20.88 $ / %-0.42)

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

**Hesap değeri: 4,998.81 $** (başlangıç 5,000 $, -1.19 $ / %-0.02)

Açık pozisyonlar: PAXGUSDT short @ 4028.41 (TP 4016.33 / SL 4036.47)

## Son olaylar

```
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
23.10 10:23 B1  CLOSE short stop: -4.19 USD
23.10 10:23 N  NEWS (5 new) score -0.60 conf 0.60: Altın 4.000 doların altına düşerek Temmuz'dan beri en düşük seviyeye geriledi; petrol kaynaklı enflasyon endişeleri Fed faiz artırımı beklentilerini canlandırıyor ve dolar (DXY ~101.5) güçlü seyrediyor. Bu tablo kısa vadede altın için baskılayıcı, ancak AI kaynaklı teknoloji satışı ve 10 yıllık tahvil getirisindeki sert düşüş (19 baz puan) güvenli liman talebi ve gevşeme beklentisi açısından karşıt sinyaller içerdiğinden güveni sınırlı tutuyorum.
23.10 10:23 B3  SHORT gold 5000 USD x10 @ 4028.41 (TP 4016.33, SL 4036.47; news -0.60)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
