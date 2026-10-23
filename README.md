# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 11:18 (İstanbul)

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
| Net kâr/zarar | -31.17 $ | -27.35 $ |
| İşlem sayısı | 17 | 18 |
| Kazanma oranı | %29.4 | %33.3 |
| Ödenen komisyon/spread | 40.34 $ | 42.71 $ |

**Hesap değeri: 4,972.55 $** (başlangıç 5,000 $, -27.45 $ / %-0.55)

Açık pozisyonlar: PAXGUSDT short @ 4029.04 (TP 4025.01 / SL 4031.46)

Son haber analizi (23.10 11:18): puan **-0.50**, güven 0.60 — Petrol kaynaklı enflasyon ve Fed faiz artırımı beklentileri altın üzerinde baskı yaratıyor; altın 3 aylık dibe yakın işlem görüyor ve haftalık düşüş bekleniyor. Yeniden alevlenen İran savaşı güvenli liman talebini destekleyebilir, ancak piyasa bunu şu an altın lehine fiyatlamıyor, dolar da güvenli liman rolünü kaybettiğini gösteriyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 11:01 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 10:16 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 10:02 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 09:48 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 08:08 | PAXGUSDT | short | -4.19 $ | stop |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -19.75 $ | -19.75 $ |
| İşlem sayısı | 4 | 4 |
| Kazanma oranı | %25.0 | %25.0 |
| Ödenen komisyon/spread | 9.49 $ | 9.49 $ |

**Hesap değeri: 4,979.43 $** (başlangıç 5,000 $, -20.57 $ / %-0.41)

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

**Hesap değeri: 4,999.12 $** (başlangıç 5,000 $, -0.88 $ / %-0.02)

Açık pozisyonlar: PAXGUSDT short @ 4028.41 (TP 4016.33 / SL 4036.47)

## Son olaylar

```
23.10 10:11 B1  CLOSE short stop: -4.19 USD
23.10 10:11 N  NEWS (8 new) score -0.45 conf 0.55: Altın 4.000 doların altına inip Temmuz'dan beri en düşük seviyeye yakın işlem görüyor; petrol şoku enflasyon ve Fed faiz artırımı beklentilerini canlandırıyor, dolar güçlü. Ancak 10 yıllık tahvil getirisinin sert düşüşü ve İran savaşı kaynaklı güvenli liman talebi kısmen destek sağlayabileceği için sinyal karışık ve güven sınırlı.
23.10 10:13 B1  SHORT gold 5000 USD x10 @ 4028.24 (TP 4024.22, SL 4030.66; news -0.45)
23.10 10:23 B1  CLOSE short stop: -4.19 USD
23.10 10:23 N  NEWS (5 new) score -0.60 conf 0.60: Altın 4.000 doların altına düşerek Temmuz'dan beri en düşük seviyeye geriledi; petrol kaynaklı enflasyon endişeleri Fed faiz artırımı beklentilerini canlandırıyor ve dolar (DXY ~101.5) güçlü seyrediyor. Bu tablo kısa vadede altın için baskılayıcı, ancak AI kaynaklı teknoloji satışı ve 10 yıllık tahvil getirisindeki sert düşüş (19 baz puan) güvenli liman talebi ve gevşeme beklentisi açısından karşıt sinyaller içerdiğinden güveni sınırlı tutuyorum.
23.10 10:23 B3  SHORT gold 5000 USD x10 @ 4028.41 (TP 4016.33, SL 4036.47; news -0.60)
23.10 10:33 N  NEWS (8 new) score -0.40 conf 0.55: Altın 4.000 doların altına düştü ve Temmuz'dan beri en düşük seviyelere yakın işlem görüyor; petrol şokunun Fed faiz artırımı beklentilerini canlandırması ve doların güçlü kalması baskı yaratıyor. Buna karşılık 10 yıllık tahvil getirisinin sert düşüşü ve teknoloji satışının güvenli liman talebini artırabilmesi çelişkili sinyaller olduğu için güven sınırlı.
23.10 10:44 N  NEWS (6 new) score -0.55 conf 0.70: Altın 3 aylık dip yakınında; Fed faiz artırımı beklentileri, güçlü dolar ve petrol şokunun faiz korkularını yeniden canlandırması altına baskı yapıyor. Orta Doğu saldırıları ve jeopolitik risk güvenli liman talebi yaratabilir, ancak bu etki mevcut sert satışı dengelemeye yetmiyor; 10 yıllık tahvil getirisindeki sert düşüş ise çelişkili bir sinyal olarak güveni biraz azaltıyor.
23.10 10:54 N  NEWS (9 new) score -0.35 conf 0.50: Altın 3 aylık dibe yakın ve 4.000 doların altında işlem görüyor; Fed faiz artırımı beklentileri, güçlü dolar ve petrol şokunun enflasyon/faiz korkularını yeniden canlandırması fiyatı baskılıyor. Buna karşılık ABD-İran savaşı ihtimali ve 10 yıllık tahvil getirisindeki sert düşüş gibi güvenli liman/gevşeme yönlü sinyaller çelişkili olduğu için güven orta düzeyde tutuldu.
23.10 10:59 N  NEWS (7 new) score -0.60 conf 0.60: Petrol kaynaklı enflasyon ve Fed faiz artırımı beklentileri altını baskılıyor; dolar güçlü ve altın 3 aylık dip bölgesinde seyrediyor. Jeopolitik risk (İran, Orta Doğu saldırıları) güvenli liman talebi yaratabilse de bu etki şu an fiyatlanmış görünmüyor; 10 yıllık tahvil getirisindeki sert düşüş ise çelişkili bir sinyal olduğu için güveni sınırlıyor.
23.10 10:59 B1  SHORT gold 5000 USD x10 @ 4025.04 (TP 4021.02, SL 4027.46; news -0.60)
23.10 11:09 B1  CLOSE short stop: -4.19 USD
23.10 11:09 N  NEWS (9 new) score -0.40 conf 0.50: Altın 3 aylık dibe yakın ve 4.000 doların altına inmiş durumda; Fed faiz artırımı beklentileri, güçlü dolar ve petrol kaynaklı enflasyon endişeleri baskı oluşturuyor. Buna karşılık ABD 10 yıllık tahvil getirisinin sert düşüşü ve yapay zeka yatırım kaygıları kısmen destekleyici olabileceğinden, güven seviyesi orta düzeyde tutuldu.
23.10 11:18 N  NEWS (13 new) score -0.50 conf 0.60: Petrol kaynaklı enflasyon ve Fed faiz artırımı beklentileri altın üzerinde baskı yaratıyor; altın 3 aylık dibe yakın işlem görüyor ve haftalık düşüş bekleniyor. Yeniden alevlenen İran savaşı güvenli liman talebini destekleyebilir, ancak piyasa bunu şu an altın lehine fiyatlamıyor, dolar da güvenli liman rolünü kaybettiğini gösteriyor.
23.10 11:18 B1  SHORT gold 5000 USD x10 @ 4029.04 (TP 4025.01, SL 4031.46; news -0.50)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
