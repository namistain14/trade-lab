# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 09:11 (İstanbul)

## Bot A — Kripto kurallar (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,001.46 $** (başlangıç 5,000 $, +1.46 $ / %+0.03)

Açık pozisyonlar: ETHUSDT long @ 2400.73 (TP 2415.13 / SL 2391.13)

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
| Net kâr/zarar | -14.42 $ | -10.60 $ |
| İşlem sayısı | 13 | 14 |
| Kazanma oranı | %38.5 | %42.9 |
| Ödenen komisyon/spread | 30.85 $ | 33.22 $ |

**Hesap değeri: 4,989.40 $** (başlangıç 5,000 $, -10.60 $ / %-0.21)

Son haber analizi (23.10 09:11): puan **-0.40**, güven 0.60 — Petrol kaynaklı enflasyon endişeleri ve Fed'in faiz artırımı beklentileri (BofA: 2026'da iki artış) altını baskılıyor; dolar da toparlanıyor. İran savaşı ve Hormuz saldırıları jeopolitik risk yaratsa da altın bu haberlere güvenli liman olarak tepki vermiyor, bu nedenle kısa vadede negatif eğilim baskın.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 08:08 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 07:47 | PAXGUSDT | short | +3.81 $ | take profit |
| 23.10 07:02 | PAXGUSDT | short | +3.81 $ | take profit |
| 23.10 06:14 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 05:34 | PAXGUSDT | short | -4.19 $ | stop |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -19.75 $ | -19.75 $ |
| İşlem sayısı | 4 | 4 |
| Kazanma oranı | %25.0 | %25.0 |
| Ödenen komisyon/spread | 9.49 $ | 9.49 $ |

**Hesap değeri: 4,980.25 $** (başlangıç 5,000 $, -19.75 $ / %-0.39)

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
23.10 07:44 A  BUY ETHUSDT 1000 USD @ 2400.73 (RSI 40)
23.10 07:44 N  NEWS (7 new) score -0.60 conf 0.65: Haberlerin ağırlığı altın için belirgin şekilde negatif: petrol fiyatlarının Fed faiz artırımı beklentilerini körüklemesi, altının üç aylık dibinin altında (4.000 doların altında) işlem görmesi ve haftalık sert düşüş beklentisi reel faiz/dolar kanalından baskı yaratıyor. İran savaşı gibi jeopolitik risk başlıkları güvenli liman talebi sağlasa da, bu etki hawkish Fed beklentilerinin gerisinde kalıyor; ayrıca birçok başlık genel nitelikli veya eski olduğu için güveni sınırlıyorum.
23.10 07:53 B1  CLOSE short take profit: +3.81 USD
23.10 07:53 N  NEWS (4 new) score -0.50 conf 0.60: Petrol fiyatlarının yükselmesi Fed faiz artırımı beklentilerini güçlendirdiği için altın üç aylık dip seviyelerine (4.000 doların altına) geriledi ve haftalık sert düşüş yaşıyor. Jeopolitik risk primi (İran savaşı, Brent prim) bu baskıyı kısmen dengeliyor, ancak faiz ve dolar etkisi baskın görünüyor; bir miktar toparlanma sinyali (üç aylık dipten tepki) belirsizliği artırıyor.
23.10 08:02 N  NEWS (10 new) score -0.55 conf 0.65: Altın 4.000 doların altına inip üç aylık dibe yakın seviyelere geriledi; petrol kaynaklı enflasyon endişeleri Fed faiz artırımı beklentilerini güçlendirerek reel faizleri ve doları destekliyor. Jeopolitik gerilim (İran/Körfez, Ukrayna) güvenli liman talebi yaratmaya devam etse de bu etki Fed'in sıkılaştırma beklentisinin gölgesinde kalıyor; bir miktar tepki alımı görülmesi ve bazı haberlerin çelişkili olması güveni sınırlıyor.
23.10 08:02 B1  SHORT gold 5000 USD x10 @ 4021.20 (TP 4017.17, SL 4023.61; news -0.55)
23.10 08:10 B1  CLOSE short stop: -4.19 USD
23.10 08:10 N  NEWS (9 new) score -0.50 conf 0.60: Petrol kaynaklı enflasyon endişeleri ve Fed'in 2026'da iki kez daha faiz artırabileceği beklentisi (BofA) reel faiz baskısını artırıp altı aşağı çekiyor; altın üç aylık dip seviyesinin (4.000 dolar altı) yakınında ve haftalık sert düşüş yolunda. Hürmüz'deki gemi saldırılarının artması güvenli liman talebi açısından destekleyici olsa da piyasa tepkisi şu an bu etkiyi bastırıyor; ayrıca Treasury getirilerindeki düşüş doların zayıflamasıyla altına kısmi destek sağlayabilir.
23.10 08:20 N  NEWS (7 new) score -0.60 conf 0.70: Petrol fiyatlarının yükselmesi enflasyon ve Fed faiz artırımı beklentilerini güçlendiriyor; bu da altın için baskılayıcı. Gold 4.000 doların altına inip üç aylık dibe geriledi ve haftalık sert düşüş yolunda. İran savaşındaki tırmanış güvenli liman talebini artırabilse de piyasa şu an bu etkiyi faiz ve dolar kanalının gerisinde bırakıyor.
23.10 08:29 N  NEWS (3 new) score -0.60 conf 0.70: Petrol fiyatlarının enflasyon kaygılarını artırması ve Fed'in faiz artırma beklentilerinin güçlenmesi altın üzerinde baskı yaratıyor; altın 4.000 doların altına inip üç aylık düşük seviyeye geriledi. İran savaşı ve Hürmüz'deki saldırılar jeopolitik talep yaratsa da bu etki, reel faiz ve dolar kaynaklı baskının gerisinde kalıyor.
23.10 08:41 N  NEWS (6 new) score -0.60 conf 0.65: Petrol fiyatlarındaki yükseliş enflasyon ve Fed faiz artırımı beklentilerini güçlendirdiği için altın üzerinde baskı sürüyor; altın üç aylık dibe yakın seviyelerde ve haftalık kayıp yaşıyor. İran savaşı ve Hürmüz'deki saldırılar jeopolitik talebi destekleyebilir, ancak bu etki şu an faiz ve dolar baskısının gerisinde kalıyor.
23.10 08:41 B2  CLOSE short stop: -11.19 USD
23.10 08:48 N  NEWS (5 new) score -0.50 conf 0.60: Petrol kaynaklı enflasyon endişeleri ve Fed'in 2026'da iki kez daha faiz artırabileceği beklentisi (BofA) altını baskılıyor; altın haftalık sert kayıp yolunda ve dolar toparlanıyor. İran savaşı ve Hürmüz'deki saldırılar jeopolitik güvenli liman talebi yaratmadığı için bu baskı baskın görünüyor, ancak tekrarlayan haberlerin büyük kısmı zaten fiyatlanmış olduğundan güven orta düzeyde tutuldu.
23.10 08:59 N  NEWS (7 new) score -0.45 conf 0.60: Petrol kaynaklı enflasyon endişeleri ve Fed'in 2026'da iki kez daha faiz artırabileceği beklentisi (BofA), reel faiz ve dolar tarafında altın için baskı yaratıyor; gold haftalık kayıp yaşıyor ve Fed kararı öncesi düşüş sürüyor. Hormuz'daki saldırıların artması ve İran savaşı güvenli liman talebini destekleyebilir, ancak piyasa bu riski şu an enflasyon kanalının gerisinde bırakıyor; bu nedenle güven orta düzeyde.
23.10 09:11 N  NEWS (11 new) score -0.40 conf 0.60: Petrol kaynaklı enflasyon endişeleri ve Fed'in faiz artırımı beklentileri (BofA: 2026'da iki artış) altını baskılıyor; dolar da toparlanıyor. İran savaşı ve Hormuz saldırıları jeopolitik risk yaratsa da altın bu haberlere güvenli liman olarak tepki vermiyor, bu nedenle kısa vadede negatif eğilim baskın.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
