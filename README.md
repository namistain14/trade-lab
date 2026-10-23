# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 16:30 (İstanbul)

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

**Hesap değeri: 4,967.24 $** (başlangıç 5,000 $, -32.76 $ / %-0.66)

Açık pozisyonlar: PAXGUSDT short @ 4038.70 (TP 4034.66 / SL 4041.13)

Son haber analizi (23.10 16:30): Claude puan **-0.30**, güven 0.50 — Altın haftalık bazda Haziran'dan bu yana en büyük kaybını yaşıyor ve fiyat 4.000 doları test ediyor; likidasyon paniği ve ABD tahvil toparlanması altını baskılıyor. Petrol kaynaklı enflasyon endişeleri, FOMC öncesi doların dirençli seyri ve Kanada'da olası faiz artırımı beklentisi sıkı para politikası algısını güçlendirdiği için kısa vadede düşüş yönlü risk var; buna karşılık İran savaşının sürmesi ve Ürdün/Paris'teki şiddet olayları güvenli liman talebini destekleyebilir, bu yüzden sinyal orta düzeyde negatif ve güven sınırlı.

GPT (gpt-6-luna): puan **+0.08**, güven 0.35 — Batı Şeria’daki saldırı, Ürdün’deki toplu ölüm ve İran savaşının bölgeye yayılma riski kısa vadede güvenli liman talebini destekleyebilir. Ancak altındaki sert düşüş ve doların Fed öncesi dirençli seyri bu etkiyi sınırlıyor; net yön sinyali zayıf.

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

**Hesap değeri: 5,001.79 $** (başlangıç 5,000 $, +1.79 $ / %+0.04)

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

## Bot B5 — Altın: Claude + GPT hemfikir (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Son olaylar

```
23.10 15:33 N  NEWS (5 new) score -0.35 conf 0.50: Altın, enflasyon endişeleri ve petrol fiyatlarındaki yükselişle üç aylık dip seviyelerine geriledi; Fed beklentilerindeki sıkılık ve yeniden güçlenen dolar/getiri avantajı kısa vadede baskı oluşturuyor. İran savaşı ve jeopolitik gerilim güvenli liman talebini destekliyor olsa da bu etki, mevcut satış momentumu ve enflasyon kaynaklı hawkish algı tarafından büyük ölçüde gölgeleniyor.
23.10 15:33 N  GPT  score -0.28 conf 0.45: Altının sert satış ve üç aylık dip haberleri kısa vadeli aşağı yönlü momentuma işaret ediyor; yükselen enerji fiyatlarının enflasyon ve faiz beklentilerini artırması da baskı yaratabilir. Rus dizel tankerine yönelik yaptırım gevşemesi bu baskıyı hafifletebilir, ancak etkisi belirsiz ve çatışma haber
23.10 15:42 N  NEWS (8 new) score -0.45 conf 0.60: Altın, petrol kaynaklı enflasyon endişeleri ve FOMC öncesi dolar direnci nedeniyle baskı altında; haberlerde altın %2,31 düştü ve üç aylık dip seviyelerinde açıldı. İran savaşı güvenli liman talebini destekliyor olsa da, piyasanın faiz beklentilerini sıkılaştırma yönünde fiyatlaması bu etkiyi ağır basıyor, bu yüzden kısa vadeli görünüm negatif.
23.10 15:42 N  GPT  score -0.35 conf 0.56: Doların FOMC öncesinde dirençli kalması ve enflasyon endişelerinin faizleri yüksek tutabileceği algısı altın için kısa vadede baskı oluşturuyor. Sudan’daki kötüleşme güvenli liman talebini destekleyebilir; ancak altındaki sert düşüşe ilişkin haberler büyük ölçüde mevcut fiyatlamayı yansıtıyor.
23.10 15:51 N  NEWS (12 new) score -0.30 conf 0.50: Altın, petrol kaynaklı enflasyon endişeleri ve sıkılaşma beklentileri nedeniyle üç aylık dipte açıldı ve haftalık düşüş eğiliminde; güçlü dolar ve FOMC öncesi temkin fiyatı aşağı çekiyor. Yeni gelen İsrail'de asker ölümleri ve İran savaşının yayılma riski gibi jeopolitik haberler güvenli liman talebini bir miktar destekleyebilir, ancak bu etki mevcut düşüş trendini tersine çevirmeye yetmeyebilir.
23.10 15:51 N  GPT  score +0.08 conf 0.34: Batı Şeria’da iki İsrail askerinin öldürülmesi kısa vadede sınırlı güvenli liman talebi yaratabilir. Rusya-Ukrayna esir takası gerilimi azaltıcı yönde; yeni başlıklarda altını güçlü biçimde yönlendirecek faiz veya dolar sinyali yok.
23.10 16:00 N  NEWS (8 new) score -0.40 conf 0.60: Altın 3 aylık dibe yakın seyrediyor ve haftalık en büyük kayıplardan birini yaşıyor; petrol fiyatlarındaki yükseliş enflasyon endişelerini artırıp sıkı para politikası beklentisini güçlendiriyor, dolar ise FOMC öncesi dirençli. İran savaşı jeopolitik risk yaratsa da bu korku altını desteklemiyor, bu yüzden genel etki negatif; yine de FOMC öncesi kısa vadeli tepki ve ABD'deki seçim riski yönünü değiştirebileceği için güven orta düzeyde tutuldu.
23.10 16:00 N  GPT  score -0.32 conf 0.48: Petrol fiyatlarındaki yükselişin enflasyon ve faiz beklentilerini yukarı çekmesi, altındaki sert satışlarla birlikte kısa vadede baskın biçimde olumsuz. Ürdün’deki saldırı güvenli liman talebini destekleyebilir; ancak etkisi belirsiz ve haberlerin bir kısmı zaten fiyatlanmış olabilir.
23.10 16:12 N  NEWS (7 new) score -0.35 conf 0.50: Altın, petrol kaynaklı enflasyon endişeleri ve FOMC öncesi dayanıklı doların etkisiyle sert düşüşte; bu da faiz beklentilerinin gold için olumsuz olduğunu gösteriyor. İran savaşı ve İsrail'deki saldırılar güvenli liman talebini destekleyebilir, ancak piyasanın şu an bu etkiyi faiz kanalının gerisinde bıraktığı görülüyor. Haftalık kayıp ve yüksek belirsizlik nedeniyle güven orta düzeyde.
23.10 16:12 N  GPT  score -0.20 conf 0.38: Ortadoğu’daki saldırılar güvenli liman talebini destekleyebilir; ancak petrol kaynaklı enflasyon endişeleri ve güçlü dolar/Fed beklentileri altın üzerinde baskı yaratıyor. Haber akışı karışık ve büyük ölçüde yeni bir makro veri sürprizi içermediğinden kısa vadeli yön sinyali zayıf.
23.10 16:21 N  NEWS (11 new) score -0.35 conf 0.50: Altın haftalık en büyük kaybını yaşıyor, 23 Ekim'de yaklaşık %2,3 düştü ve tasfiye paniği fiyatı 4.000 dolar eşiğine yaklaştırdı. Petrol kaynaklı enflasyon endişeleri, FOMC öncesi dolardaki dayanıklılık ve Kanada'da olası faiz artırımı tabloyu şahin tarafa çekiyor; İran savaşının sürmesi ise sınırlı da olsa güvenli liman talebini destekliyor.
23.10 16:21 N  GPT  score -0.30 conf 0.55: Altın ve gümüşteki sert düşüş, doların dirençli seyri ve savaş kaynaklı enerji fiyatlarının enflasyon/faiz beklentilerini yükseltme riski kısa vadede baskın ve altın için hafif negatif. Jeopolitik riskler güvenli liman talebini desteklese de yeni, belirleyici bir tırmanış haberi yok; haber akışı kar
23.10 16:30 N  NEWS (6 new) score -0.30 conf 0.50: Altın haftalık bazda Haziran'dan bu yana en büyük kaybını yaşıyor ve fiyat 4.000 doları test ediyor; likidasyon paniği ve ABD tahvil toparlanması altını baskılıyor. Petrol kaynaklı enflasyon endişeleri, FOMC öncesi doların dirençli seyri ve Kanada'da olası faiz artırımı beklentisi sıkı para politikası algısını güçlendirdiği için kısa vadede düşüş yönlü risk var; buna karşılık İran savaşının sürmesi ve Ürdün/Paris'teki şiddet olayları güvenli liman talebini destekleyebilir, bu yüzden sinyal orta düzeyde negatif ve güven sınırlı.
23.10 16:30 N  GPT  score +0.08 conf 0.35: Batı Şeria’daki saldırı, Ürdün’deki toplu ölüm ve İran savaşının bölgeye yayılma riski kısa vadede güvenli liman talebini destekleyebilir. Ancak altındaki sert düşüş ve doların Fed öncesi dirençli seyri bu etkiyi sınırlıyor; net yön sinyali zayıf.
23.10 16:30 B1  SHORT gold 5000 USD x10 @ 4038.70 (TP 4034.66, SL 4041.13; news -0.30)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
