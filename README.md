# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 16:45 (İstanbul)

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
| Net kâr/zarar | -39.87 $ | -36.05 $ |
| İşlem sayısı | 19 | 20 |
| Kazanma oranı | %26.3 | %30.0 |
| Ödenen komisyon/spread | 45.08 $ | 47.45 $ |

**Hesap değeri: 4,962.76 $** (başlangıç 5,000 $, -37.24 $ / %-0.74)

Açık pozisyonlar: PAXGUSDT short @ 4032.96 (TP 4028.93 / SL 4035.38)

Son haber analizi (23.10 16:45): Claude puan **-0.40**, güven 0.50 — Altın 3 aylık dibe yakın, haftalık en büyük kayıplardan birini yaşıyor ve haven talebi zayıflamış görünüyor; petrol kaynaklı enflasyon endişeleri ile FOMC öncesi dolar direnci ve olası BoC faiz artırımı beklentisi baskıyı artırıyor. Buna karşılık İran savaşı ve Orta Doğu saldırıları gibi jeopolitik riskler sürmekte, bu da kısa vadeli toparlanma ihtimalini sınırlı da olsa destekleyebilir; ayrıca çok sayıda fiyat hareketi zaten yansıtılmış olduğu için güven orta düzeyde tutuldu.

GPT (gpt-6-luna): puan **-0.40**, güven 0.65 — Altın fiyatının 4.000 doların altına gerilemesi ve süregelen satış baskısı kısa vadede aşağı yönlü momentuma işaret ediyor; dirençli dolar ve petrol kaynaklı enflasyon/faiz endişeleri de baskıyı artırabilir. Orta Doğu’daki saldırılar güvenli liman talebini desteklese de yeni başlıklar güçlü bir tırm

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 16:32 | PAXGUSDT | short | -4.51 $ | stop (gap) |
| 23.10 11:23 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 11:01 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 10:16 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 10:02 | PAXGUSDT | short | -4.19 $ | stop |

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

**Hesap değeri: 4,994.64 $** (başlangıç 5,000 $, -5.36 $ / %-0.11)

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

**Hesap değeri: 5,003.15 $** (başlangıç 5,000 $, +3.15 $ / %+0.06)

Açık pozisyonlar: PAXGUSDT short @ 4036.46 (TP 4024.35 / SL 4044.54)

## Son olaylar

```
23.10 16:00 N  GPT  score -0.32 conf 0.48: Petrol fiyatlarındaki yükselişin enflasyon ve faiz beklentilerini yukarı çekmesi, altındaki sert satışlarla birlikte kısa vadede baskın biçimde olumsuz. Ürdün’deki saldırı güvenli liman talebini destekleyebilir; ancak etkisi belirsiz ve haberlerin bir kısmı zaten fiyatlanmış olabilir.
23.10 16:12 N  NEWS (7 new) score -0.35 conf 0.50: Altın, petrol kaynaklı enflasyon endişeleri ve FOMC öncesi dayanıklı doların etkisiyle sert düşüşte; bu da faiz beklentilerinin gold için olumsuz olduğunu gösteriyor. İran savaşı ve İsrail'deki saldırılar güvenli liman talebini destekleyebilir, ancak piyasanın şu an bu etkiyi faiz kanalının gerisinde bıraktığı görülüyor. Haftalık kayıp ve yüksek belirsizlik nedeniyle güven orta düzeyde.
23.10 16:12 N  GPT  score -0.20 conf 0.38: Ortadoğu’daki saldırılar güvenli liman talebini destekleyebilir; ancak petrol kaynaklı enflasyon endişeleri ve güçlü dolar/Fed beklentileri altın üzerinde baskı yaratıyor. Haber akışı karışık ve büyük ölçüde yeni bir makro veri sürprizi içermediğinden kısa vadeli yön sinyali zayıf.
23.10 16:21 N  NEWS (11 new) score -0.35 conf 0.50: Altın haftalık en büyük kaybını yaşıyor, 23 Ekim'de yaklaşık %2,3 düştü ve tasfiye paniği fiyatı 4.000 dolar eşiğine yaklaştırdı. Petrol kaynaklı enflasyon endişeleri, FOMC öncesi dolardaki dayanıklılık ve Kanada'da olası faiz artırımı tabloyu şahin tarafa çekiyor; İran savaşının sürmesi ise sınırlı da olsa güvenli liman talebini destekliyor.
23.10 16:21 N  GPT  score -0.30 conf 0.55: Altın ve gümüşteki sert düşüş, doların dirençli seyri ve savaş kaynaklı enerji fiyatlarının enflasyon/faiz beklentilerini yükseltme riski kısa vadede baskın ve altın için hafif negatif. Jeopolitik riskler güvenli liman talebini desteklese de yeni, belirleyici bir tırmanış haberi yok; haber akışı kar
23.10 16:30 N  NEWS (6 new) score -0.30 conf 0.50: Altın haftalık bazda Haziran'dan bu yana en büyük kaybını yaşıyor ve fiyat 4.000 doları test ediyor; likidasyon paniği ve ABD tahvil toparlanması altını baskılıyor. Petrol kaynaklı enflasyon endişeleri, FOMC öncesi doların dirençli seyri ve Kanada'da olası faiz artırımı beklentisi sıkı para politikası algısını güçlendirdiği için kısa vadede düşüş yönlü risk var; buna karşılık İran savaşının sürmesi ve Ürdün/Paris'teki şiddet olayları güvenli liman talebini destekleyebilir, bu yüzden sinyal orta düzeyde negatif ve güven sınırlı.
23.10 16:30 N  GPT  score +0.08 conf 0.35: Batı Şeria’daki saldırı, Ürdün’deki toplu ölüm ve İran savaşının bölgeye yayılma riski kısa vadede güvenli liman talebini destekleyebilir. Ancak altındaki sert düşüş ve doların Fed öncesi dirençli seyri bu etkiyi sınırlıyor; net yön sinyali zayıf.
23.10 16:30 B1  SHORT gold 5000 USD x10 @ 4038.70 (TP 4034.66, SL 4041.13; news -0.30)
23.10 16:39 B1  CLOSE short stop (gap): -4.51 USD
23.10 16:39 N  NEWS (10 new) score -0.30 conf 0.45: Altın son haftada en büyük haftalık kayıplardan birini yaşıyor ve "haven" talebi zayıflarken dolar FOMC öncesi dirençli, petrol kaynaklı enflasyon endişeleri ise faiz artırımı beklentilerini besliyor; bu tablo kısa vadede altın için baskılayıcı. Buna karşılık İran savaşının tırmanış haberleri ve Ortadoğu saldırıları jeopolitik destek sağlayabileceği için sinyal karışık ve güven sınırlı.
23.10 16:39 N  GPT  score -0.35 conf 0.48: Altına ilişkin sert düşüş ve 4.000 dolar eşiğine yaklaşma haberleri, doların ve faiz avantajının güçlü kalmasıyla kısa vadede aşağı yönlü baskıyı destekliyor. Orta Doğu’daki saldırı ve tırmanma haberleri güvenli liman talebini artırabilir; ancak fiyat hareketi bu desteğin şimdilik baskın olmadığını 
23.10 16:39 B5  SHORT gold 5000 USD x10 @ 4036.46 (TP 4024.35, SL 4044.54; news -0.32)
23.10 16:45 N  NEWS (7 new) score -0.40 conf 0.50: Altın 3 aylık dibe yakın, haftalık en büyük kayıplardan birini yaşıyor ve haven talebi zayıflamış görünüyor; petrol kaynaklı enflasyon endişeleri ile FOMC öncesi dolar direnci ve olası BoC faiz artırımı beklentisi baskıyı artırıyor. Buna karşılık İran savaşı ve Orta Doğu saldırıları gibi jeopolitik riskler sürmekte, bu da kısa vadeli toparlanma ihtimalini sınırlı da olsa destekleyebilir; ayrıca çok sayıda fiyat hareketi zaten yansıtılmış olduğu için güven orta düzeyde tutuldu.
23.10 16:45 N  GPT  score -0.40 conf 0.65: Altın fiyatının 4.000 doların altına gerilemesi ve süregelen satış baskısı kısa vadede aşağı yönlü momentuma işaret ediyor; dirençli dolar ve petrol kaynaklı enflasyon/faiz endişeleri de baskıyı artırabilir. Orta Doğu’daki saldırılar güvenli liman talebini desteklese de yeni başlıklar güçlü bir tırm
23.10 16:45 B1  SHORT gold 5000 USD x10 @ 4032.96 (TP 4028.93, SL 4035.38; news -0.40)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
