# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 17:09 (İstanbul)

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
| Net kâr/zarar | -44.05 $ | -40.24 $ |
| İşlem sayısı | 20 | 21 |
| Kazanma oranı | %25.0 | %28.6 |
| Ödenen komisyon/spread | 47.46 $ | 49.83 $ |

**Hesap değeri: 4,959.79 $** (başlangıç 5,000 $, -40.21 $ / %-0.80)

Açık pozisyonlar: PAXGUSDT short @ 4028.28 (TP 4024.26 / SL 4030.70)

Son haber analizi (23.10 17:09): Claude puan **-0.35**, güven 0.50 — Altın gün içinde yaklaşık %2,3 düştü ve haftalık bazda Haziran'dan bu yana en büyük kaybını yaşıyor; Fed'in Ekim'de faiz sabit tutmasının Aralık'ta faiz artırımı olasılığını yükseltmesi ve ABD dolarının FOMC öncesi dirençli seyretmesi baskı oluşturuyor. İran savaşı ve olası ABD-İsrail saldırıları gibi jeopolitik riskler ise güvenli liman talebi yaratabilir, ancak haberlere göre güvenli liman işlemi şu an bozulmuş durumda, bu da bu desteği sınırlıyor.

GPT (gpt-6-luna): puan **-0.35**, güven 0.58 — Fed’in Aralıkta faiz artırma olasılığının yükseldiği yorumu ve doların dirençli seyri altın için kısa vadede baskı oluşturuyor; son sert düşüş haberleri de aşağı yönlü momentuma işaret ediyor. Orta Doğu’daki gerilim güvenli liman talebini destekleyebilir, ancak yeni ve belirleyici bir tırmanış haber

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 16:49 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 16:32 | PAXGUSDT | short | -4.51 $ | stop (gap) |
| 23.10 11:23 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 11:01 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 10:16 | PAXGUSDT | short | -4.19 $ | stop |

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
| Net kâr/zarar | -11.18 $ | -11.18 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 4,988.82 $** (başlangıç 5,000 $, -11.18 $ / %-0.22)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 17:08 | PAXGUSDT | long | -11.18 $ | stop |

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

**Hesap değeri: 5,010.16 $** (başlangıç 5,000 $, +10.16 $ / %+0.20)

Açık pozisyonlar: PAXGUSDT short @ 4036.46 (TP 4024.35 / SL 4044.54)

## Son olaylar

```
23.10 16:30 B1  SHORT gold 5000 USD x10 @ 4038.70 (TP 4034.66, SL 4041.13; news -0.30)
23.10 16:39 B1  CLOSE short stop (gap): -4.51 USD
23.10 16:39 N  NEWS (10 new) score -0.30 conf 0.45: Altın son haftada en büyük haftalık kayıplardan birini yaşıyor ve "haven" talebi zayıflarken dolar FOMC öncesi dirençli, petrol kaynaklı enflasyon endişeleri ise faiz artırımı beklentilerini besliyor; bu tablo kısa vadede altın için baskılayıcı. Buna karşılık İran savaşının tırmanış haberleri ve Ortadoğu saldırıları jeopolitik destek sağlayabileceği için sinyal karışık ve güven sınırlı.
23.10 16:39 N  GPT  score -0.35 conf 0.48: Altına ilişkin sert düşüş ve 4.000 dolar eşiğine yaklaşma haberleri, doların ve faiz avantajının güçlü kalmasıyla kısa vadede aşağı yönlü baskıyı destekliyor. Orta Doğu’daki saldırı ve tırmanma haberleri güvenli liman talebini artırabilir; ancak fiyat hareketi bu desteğin şimdilik baskın olmadığını 
23.10 16:39 B5  SHORT gold 5000 USD x10 @ 4036.46 (TP 4024.35, SL 4044.54; news -0.32)
23.10 16:45 N  NEWS (7 new) score -0.40 conf 0.50: Altın 3 aylık dibe yakın, haftalık en büyük kayıplardan birini yaşıyor ve haven talebi zayıflamış görünüyor; petrol kaynaklı enflasyon endişeleri ile FOMC öncesi dolar direnci ve olası BoC faiz artırımı beklentisi baskıyı artırıyor. Buna karşılık İran savaşı ve Orta Doğu saldırıları gibi jeopolitik riskler sürmekte, bu da kısa vadeli toparlanma ihtimalini sınırlı da olsa destekleyebilir; ayrıca çok sayıda fiyat hareketi zaten yansıtılmış olduğu için güven orta düzeyde tutuldu.
23.10 16:45 N  GPT  score -0.40 conf 0.65: Altın fiyatının 4.000 doların altına gerilemesi ve süregelen satış baskısı kısa vadede aşağı yönlü momentuma işaret ediyor; dirençli dolar ve petrol kaynaklı enflasyon/faiz endişeleri de baskıyı artırabilir. Orta Doğu’daki saldırılar güvenli liman talebini desteklese de yeni başlıklar güçlü bir tırm
23.10 16:45 B1  SHORT gold 5000 USD x10 @ 4032.96 (TP 4028.93, SL 4035.38; news -0.40)
23.10 16:57 B1  CLOSE short stop: -4.19 USD
23.10 16:57 N  NEWS (15 new) score +0.05 conf 0.20: Yeni başlıkların çoğu altın fiyatını doğrudan etkileyecek nitelikte değil; Fed, reel faiz, dolar veya merkez bankası alımlarına dair önemli bir haber yok. Ürdün, Batı Şeria ve Sudan'daki şiddet olayları küçük bir güvenli liman talebi yaratabilir, ancak bu etki büyük ihtimalle sınırlı ve kısa ömürlü olacaktır.
23.10 16:57 N  GPT  score +0.16 conf 0.28: Sudan’daki hastanelere yönelik saldırılar ve Ukrayna’daki Starlink belirsizliği güvenli liman talebini bir miktar destekleyebilir. Ancak haberlerin altın üzerindeki etkisi dolaylı; yeni faiz veya dolar sinyali bulunmadığından olası yükseliş sınırlı görünüyor.
23.10 17:09 N  NEWS (41 new) score -0.35 conf 0.50: Altın gün içinde yaklaşık %2,3 düştü ve haftalık bazda Haziran'dan bu yana en büyük kaybını yaşıyor; Fed'in Ekim'de faiz sabit tutmasının Aralık'ta faiz artırımı olasılığını yükseltmesi ve ABD dolarının FOMC öncesi dirençli seyretmesi baskı oluşturuyor. İran savaşı ve olası ABD-İsrail saldırıları gibi jeopolitik riskler ise güvenli liman talebi yaratabilir, ancak haberlere göre güvenli liman işlemi şu an bozulmuş durumda, bu da bu desteği sınırlıyor.
23.10 17:09 N  GPT  score -0.35 conf 0.58: Fed’in Aralıkta faiz artırma olasılığının yükseldiği yorumu ve doların dirençli seyri altın için kısa vadede baskı oluşturuyor; son sert düşüş haberleri de aşağı yönlü momentuma işaret ediyor. Orta Doğu’daki gerilim güvenli liman talebini destekleyebilir, ancak yeni ve belirleyici bir tırmanış haber
23.10 17:09 B1  SHORT gold 5000 USD x10 @ 4028.28 (TP 4024.26, SL 4030.70; news -0.35)
23.10 17:09 B4  CLOSE long stop: -11.18 USD
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
