# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 03.11.2026 13:15 (İstanbul)

## Bot A — Kripto TERS (alım sinyalinde satış, x3)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -142.81 $ | -1165.56 $ |
| İşlem sayısı | 12 | 91 |
| Kazanma oranı | %8.3 | %17.6 |
| Ödenen komisyon/spread | 47.29 $ | 397.49 $ |

**Hesap değeri: 3,834.44 $** (başlangıç 5,000 $, -1165.56 $ / %-23.31)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 03.11 12:07 | DOGEUSDT | short | -12.40 $ | stop |
| 03.11 12:07 | XRPUSDT | short | -24.80 $ | stop |
| 03.11 12:07 | BNBUSDT | short | -24.80 $ | stop |
| 03.11 10:23 | XRPUSDT | short | -12.67 $ | stop |
| 03.11 10:23 | ETHUSDT | short | -24.99 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -279.74 $ | -424.88 $ |
| İşlem sayısı | 5 | 21 |
| Kazanma oranı | %0.0 | %28.6 |
| Ödenen komisyon/spread | 59.50 $ | 249.86 $ |

**Hesap değeri: 4,579.31 $** (başlangıç 5,000 $, -420.69 $ / %-8.41)

Açık pozisyonlar: PAXGUSDT short @ 3916.57 (TP 3904.82 / SL 3924.40)

Son haber analizi (03.11 13:12): Claude puan **-0.05**, güven 0.35 — İran'ın Qeshm Adası'na ABD saldırısı ve petrol fiyatlarındaki yükseliş güvenli liman talebini destekliyor, ancak enflasyon kaygısı, Fed Başkanı Warsh'un sert açıklamaları ve yükselen dolar/Fed beklentileri altını aşağı çekiyor. Altın zaten son saatlerde geriliyor, bu nedenle net etki hafif negatif ve belirsiz.

GPT (gpt-6-luna): puan **+0.20**, güven 0.43 — İran’ın Qeşm Adası’na yönelik yeni ABD saldırısı kısa vadede güvenli liman talebini artırabilir. Ancak petrol kaynaklı enflasyon ve faiz endişeleriyle altının zaten gerilemesi, olası yükselişi sınırlıyor; net etki hafif pozitif görünüyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 03.11 12:36 | PAXGUSDT | short | -55.97 $ | stop |
| 03.11 06:16 | PAXGUSDT | long | -55.94 $ | stop |
| 03.11 05:04 | PAXGUSDT | long | -55.94 $ | stop |
| 03.11 03:43 | PAXGUSDT | long | -55.94 $ | stop |
| 03.11 03:18 | PAXGUSDT | short | -55.96 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +66.43 $ |
| İşlem sayısı | 0 | 1 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 17.17 $ |

**Hesap değeri: 5,066.43 $** (başlangıç 5,000 $, +66.43 $ / %+1.33)

Son haber analizi (02.11 23:07): Claude puan **-0.50**, güven 0.60 — Baskın haber akışı İran ile barış görüşmelerine ve Hürmüz Boğazı'nın iki gün içinde yeniden açılabileceği ihtimaline işaret ediyor; bu, savaş primini hızla eritip Brent'i aşağı çekiyor (piyasada %7'ye varan düşüş bildirildi). Kazakistan'ın Samara hattındaki taşımayı durdurması ve Hindistan'daki rafineri yangını gibi arz kaynaklı yukarı yönlü riskler var, ancak bunlar müzakere iyimserliğinin gerisinde kalıyor; Goldman'ın hedef artışı ise uzun vadeli bir sinyal.

GPT (gpt-6-luna): puan **-0.78**, güven 0.82 — ABD-İran ateşkes görüşmeleri ve İran’ın anlaşma kapsamında Hürmüz Boğazı’nı yeniden açabileceği haberleri yakın vadeli arz kesintisi riskini azaltıyor; petrolün %7’den fazla düşmesi bu beklentinin fiyatlandığını gösteriyor. Kazakistan’ın petrol transitini durdurması sınırlı bir karşı unsur, ancak kı

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 23:09 | BZ=F | short | +66.43 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 100,746.25 $** (başlangıç 100,000 $, +746.25 $ / %+0.75)

## Son olaylar

```
03.11 12:07 A  CLOSE XRPUSDT stop: -24.80 USD
03.11 12:07 A  CLOSE DOGEUSDT stop: -12.40 USD
03.11 12:16 N  NEWS (10 new) score -0.20 conf 0.40: Altın birkaç saatlik görünümde hafif negatif: fiyat son haberlerde yaklaşık %1 geriledi, ABD ara seçim öncesi zayıf seyir ve petrol kaynaklı enflasyon endişeleri faiz beklentilerini sertleştirerek altına baskı yapabilir. Buna karşılık merkez bankalarının Q3'te 321 ton alımı ve İran savaşının sürmesi destek unsuru; ayrıca Hindistan talebindeki %29'luk düşüş ve Cuma günkü NFP verisi belirsizliği artırıyor, bu çelişkiler güveni sınırlıyor.
03.11 12:16 N  GPT  score -0.25 conf 0.42: Altın fiyatındaki yakın dönem düşüş ve seçim öncesi temkinli görünüm kısa vadede aşağı yönlü baskıya işaret ediyor. İran gerilimi ve güçlü merkez bankası alımları destek sağlasa da bunlar kısa vadeli fiyat zayıflığını dengeleyebilir; haber akışı karışık ve bir kısmı zaten fiyatlanmış olabilir.
03.11 12:16 B5  SHORT gold 25000 USD x10 @ 3908.44 (TP 3896.71, SL 3916.26; news -0.23)
03.11 12:28 N  NEWS (17 new) score -0.20 conf 0.40: İran savaşının petrol fiyatlarını (WTI 96 doları üzerinde) yukarı itmesi enflasyon ve sıkılaşma beklentilerini besleyerek altın için kısa vadede baskı yaratıyor; Avrupa Merkez Bankası'nın şahin tonu ve doların ABD ara seçimleri öncesinde dengeli seyretmesi de desteklemiyor. Buna karşılık savaş riskinin sürmesi ve merkez bankalarının güçlü altın alımları (3. çeyrekte 321 ton) yapısal olarak destekleyici, bu yüzden etki sınırlı ve belirsiz.
03.11 12:28 N  GPT  score +0.18 conf 0.43: İran’a yönelik ABD saldırısı ve Tahran’dan gelen daha geniş karşılık uyarısı kısa vadede güvenli liman talebini destekleyebilir; Rusya’nın Harkiv’deki hastaneye saldırısı da bu riski artırıyor. Ancak altının yaklaşık %1 gerilediğine dair haberler ve yüksek petrolün enflasyon/faiz beklentileri üzerin
03.11 12:48 B5  CLOSE short stop: -55.97 USD
03.11 12:48 N  NEWS (20 new) score -0.20 conf 0.40: Altın için karışık tablo var: ABD-İran diplomasi umutları ve Fed Başkanı Warsh'un sert açıklamaları (faiz beklentileri ve dolar tarafında) kısa vadede baskı yaratabilir; buna karşılık Qeshm Adası saldırıları ve savaş riski güvenli liman talebini destekliyor. Merkez bankası alımları yapısal olarak destekleyici olsa da kısa vadeli etkisi sınırlı.
03.11 12:48 N  GPT  score -0.25 conf 0.38: Altın son haberlerde yaklaşık %1 gerilemiş; İran konusunda diplomasi umudu güvenli liman talebini sınırlayabilir. Ancak olası savaş tırmanışına dair haberler ve çelişkili sinyaller nedeniyle kısa vadeli yön belirsiz, merkez bankası alımları ise 1-4 saatlik görünüm için daha az belirleyici.
03.11 12:48 B5  SHORT gold 25000 USD x10 @ 3916.57 (TP 3904.82, SL 3924.40; news -0.23)
03.11 13:00 N  NEWS (13 new) score -0.25 conf 0.40: 
03.11 13:00 N  GPT  score -0.25 conf 0.56: Altın fiyatındaki düşüş ve petrol kaynaklı enflasyon kaygılarının faiz beklentilerini desteklemesi kısa vadede baskı yaratıyor. İran’la anlaşmanın uzak görünmesi güvenli liman talebini artırabilir; merkez bankası alımları ise daha çok uzun vadeli ve kısa vadeli etkiyi sınırlı ölçüde dengeliyor.
03.11 13:12 N  NEWS (11 new) score -0.05 conf 0.35: İran'ın Qeshm Adası'na ABD saldırısı ve petrol fiyatlarındaki yükseliş güvenli liman talebini destekliyor, ancak enflasyon kaygısı, Fed Başkanı Warsh'un sert açıklamaları ve yükselen dolar/Fed beklentileri altını aşağı çekiyor. Altın zaten son saatlerde geriliyor, bu nedenle net etki hafif negatif ve belirsiz.
03.11 13:12 N  GPT  score +0.20 conf 0.43: İran’ın Qeşm Adası’na yönelik yeni ABD saldırısı kısa vadede güvenli liman talebini artırabilir. Ancak petrol kaynaklı enflasyon ve faiz endişeleriyle altının zaten gerilemesi, olası yükselişi sınırlıyor; net etki hafif pozitif görünüyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
