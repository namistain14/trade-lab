# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 26.10.2026 13:26 (İstanbul)

## Bot A — Kripto kurallar (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -5.00 $ |
| İşlem sayısı | 0 | 3 |
| Kazanma oranı | %0.0 | %66.7 |
| Ödenen komisyon/spread | 0.00 $ | 6.00 $ |

**Hesap değeri: 4,995.00 $** (başlangıç 5,000 $, -5.00 $ / %-0.10)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 25.10 17:28 | BTCUSDT | long | +0.99 $ | time limit |
| 25.10 09:51 | SOLUSDT | long | -6.29 $ | stop |
| 23.10 09:46 | ETHUSDT | long | +0.30 $ | time limit |

## Bot A2 — Kripto: sert düşüş sonrası toparlanma (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +5.69 $ |
| İşlem sayısı | 0 | 1 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 2.01 $ |

**Hesap değeri: 5,005.69 $** (başlangıç 5,000 $, +5.69 $ / %+0.11)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 24.10 19:51 | ETHUSDT | long | +5.69 $ | take profit |

## Bot B1 — Altın + haber (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -3.00 $ | -79.04 $ |
| İşlem sayısı | 1 | 34 |
| Kazanma oranı | %0.0 | %23.5 |
| Ödenen komisyon/spread | 2.37 $ | 80.69 $ |

**Hesap değeri: 4,920.96 $** (başlangıç 5,000 $, -79.04 $ / %-1.58)

Son haber analizi (26.10 13:26): Claude puan **-0.30**, güven 0.50 — Fed'in faizleri sabit tutması bekleniyor ancak başlıklar şahin bir tona işaret ediyor: Aralık'ta faiz artırımı ihtimali yükseldi, enflasyon yüksek ve dolar güçlü. Bu, altın için kısa vadede baskı oluşturuyor. Orta Doğu gerilimi ve enerji fiyatlarındaki artış güvenli liman talebini destekleyebilir, ama enflasyon ve faiz beklentisi üzerinden etkisi daha baskın görünüyor. Altın 4.000 dolar civarında dengelenmeye çalışıyor; bu nedenle etki hafif negatif, güven orta düzeyde.

GPT (gpt-6-luna): puan **+0.20**, güven 0.46 — Orta Doğu’daki gerilim ve Riyad’a yönelik füze saldırısı güvenli liman talebini destekleyebilir. Ancak doların güçlü seyri ve Fed’in ileride yeniden faiz artırabileceği beklentisi altının yükselişini sınırlıyor; kısa vadeli net etki hafif pozitif görünüyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 26.10 10:21 | PAXGUSDT | short | -3.00 $ | stop |
| 23.10 21:26 | PAXGUSDT | short | -3.00 $ | stop |
| 23.10 20:51 | PAXGUSDT | short | -3.00 $ | stop |
| 23.10 20:31 | PAXGUSDT | short | -3.00 $ | stop |
| 23.10 20:03 | PAXGUSDT | short | -4.19 $ | stop |

## Bot B2 — Altın: sıkı haber eşiği (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -35.22 $ |
| İşlem sayısı | 0 | 6 |
| Kazanma oranı | %0.0 | %16.7 |
| Ödenen komisyon/spread | 0.00 $ | 14.24 $ |

**Hesap değeri: 4,964.78 $** (başlangıç 5,000 $, -35.22 $ / %-0.70)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 18:03 | PAXGUSDT | short | -4.28 $ | stop (gap) |
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 08:32 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 05:27 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 04:52 | PAXGUSDT | short | +13.82 $ | take profit |

## Bot B4 — Altın: haberin TERSİ (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -11.18 $ |
| İşlem sayısı | 0 | 1 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 2.37 $ |

**Hesap değeri: 4,987.63 $** (başlangıç 5,000 $, -12.37 $ / %-0.25)

Açık pozisyonlar: PAXGUSDT long @ 4027.81 (TP 4039.89 / SL 4019.75)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 17:08 | PAXGUSDT | long | -11.18 $ | stop |

## Bot B3 — Altın: B2 + seans filtresi + momentum (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -26.82 $ |
| İşlem sayısı | 0 | 3 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 7.12 $ |

**Hesap değeri: 4,973.18 $** (başlangıç 5,000 $, -26.82 $ / %-0.54)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 18:22 | PAXGUSDT | short | -11.35 $ | stop (gap) |
| 23.10 18:03 | PAXGUSDT | short | -4.28 $ | stop (gap) |
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +21.88 $ |
| İşlem sayısı | 0 | 2 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 4.75 $ |

**Hesap değeri: 5,021.88 $** (başlangıç 5,000 $, +21.88 $ / %+0.44)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 24.10 00:03 | PAXGUSDT | short | +8.06 $ | time limit |
| 23.10 17:11 | PAXGUSDT | short | +13.82 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:2

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 100,000.00 $** (başlangıç 100,000 $, +0.00 $ / %+0.00)

## Son olaylar

```
26.10 09:14 N  NEWS (32 new) score +0.15 conf 0.40: Dolar endeksinin 101,50 civarına gerilemesi, petrol fiyatlarının düşmesi ve Fed'in bekleme beklentisi altına yatırımı hafifçe destekliyor. Buna karşın Fed'in çeyreklik faiz artırımlarını sürdürme ihtimali ve Aralık'ta artırım riski gibi şahin başlıklar ile sonuçların henüz netleşmemiş olması güveni sınırlıyor.
26.10 09:14 N  GPT  score +0.22 conf 0.46: Doların Fed’in faiz kararları öncesinde zayıflaması ve altının bu sabah yükseldiğine dair haberler kısa vadede destekleyici. Ancak Fed’in daha şahin kalabileceği beklentisi ve haber akışındaki belirsizlik yükseliş potansiyelini sınırlıyor.
26.10 10:16 N  NEWS (38 new) score -0.20 conf 0.40: Fed'in faiz artırımı olasılığının yükseldiğine dair haberler (Aralık hike ihtimali, %75 artırım olasılığı) ve güçlü dolar beklentisi altın için baskılayıcı. İran savaşı, Husi saldırıları ve Ukrayna'daki çatışmalar güvenli liman talebini destekliyor, ancak bu gerilimlerin büyük kısmı zaten fiyatlanmış ve haberler karışık; Fed toplantısı öncesi piyasa belirsizlik içinde.
26.10 10:16 N  GPT  score -0.12 conf 0.38: Fed’in faiz artırımı olasılığının yüksek gösterilmesi altın için kısa vadede baskı yaratabilir. Doların gerilemesi ve Yemen çevresindeki gerilimler bu etkiyi dengeliyor; haber akışı büyük ölçüde beklenti ve mevcut riskleri yansıtıyor.
26.10 10:16 B1  SHORT gold 5000 USD x10 @ 4014.07 (TP 4011.51, SL 4015.52; news -0.20)
26.10 11:10 B1  CLOSE short stop: -3.00 USD
26.10 11:10 N  NEWS (33 new) score -0.20 conf 0.40: Fed'in Aralık'ta faiz artırımı ihtimali ve güçlenen dolar altın için baskı oluşturuyor; buna karşılık İran ve Körfez'deki jeopolitik gerilim (Husi saldırısı, Suudi karşı saldırıları) güvenli liman talebini destekliyor. Arabulucu heyetlerin İran'a gitmesi gerilimin bir kısmının gevşediğine işaret ettiği için net etki hafif negatif, güven düşük.
26.10 11:10 N  GPT  score -0.15 conf 0.42: Fed’e ilişkin şahin beklentiler ve doların gücü altın üzerinde kısa vadeli baskı oluşturuyor. İran çevresindeki gerilim ve Riyad’a yönelik saldırı haberleri güvenli liman talebini destekleyebilir; ancak diplomatik temaslar ve çelişkili haber akışı bu desteği sınırlıyor.
26.10 12:00 N  NEWS (28 new) score -0.15 conf 0.40: Jeopolitik risk (İran'ın savaşa dönme tehdidi) altına güvenli liman talebi getiriyor, ancak Fed'in faiz artırımı ihtimali (Aralık hikâyesi), DXY'nin 101.50 üzerinde seyretmesi ve FOMC öncesi doların güçlü kalması altın için baskı oluşturuyor. Haberler karışık ve bir kısmı zaten fiyatlanmış olduğu için güven düşük.
26.10 12:00 N  GPT  score +0.20 conf 0.43: İran’ın yeniden savaşa hazır olduğu açıklaması ve Ukrayna’daki saldırılar kısa vadede güvenli liman talebini destekleyebilir; doların Fed duraklaması beklentisiyle gerilemesi de altın için olumlu. Ancak şahin Fed beklentileri ve doların genel gücü yükselişi sınırlayabilir; etkiler karışık olduğundan
26.10 12:45 N  NEWS (32 new) score -0.20 conf 0.40: Fed kararı öncesi haberler karışık ama hafif şahin ağırlıklı: TD Securities, Ekim'de faiz pauzası olasılığının Aralık'ta artış ihtimalini yükselttiğini, dolar ise Fed kararı öncesi dirençli kaldığını belirtiyor; bu altın için baskı oluşturur. Öte yandan İran savaşında diplomatik çabalar ve petrolün düşüşü jeopolitik risk primini azaltıyor, ancak altın 4.000 dolar civarında toparlanma sinyali veriyor ve güvenli liman talebi tamamen sönmüş değil. Sonuç olarak hafif negatif, düşük güvenli bir görünüm.
26.10 12:45 N  GPT  score +0.10 conf 0.35: Altın fiyatındaki toparlanma ve süren jeopolitik riskler kısa vadede hafif destekleyici. Ancak Fed kararı öncesi doların güçlü kalması ve gelecekte faiz artışı beklentilerinin yükselmesi bu desteği sınırlıyor.
26.10 13:26 N  NEWS (29 new) score -0.30 conf 0.50: Fed'in faizleri sabit tutması bekleniyor ancak başlıklar şahin bir tona işaret ediyor: Aralık'ta faiz artırımı ihtimali yükseldi, enflasyon yüksek ve dolar güçlü. Bu, altın için kısa vadede baskı oluşturuyor. Orta Doğu gerilimi ve enerji fiyatlarındaki artış güvenli liman talebini destekleyebilir, ama enflasyon ve faiz beklentisi üzerinden etkisi daha baskın görünüyor. Altın 4.000 dolar civarında dengelenmeye çalışıyor; bu nedenle etki hafif negatif, güven orta düzeyde.
26.10 13:26 N  GPT  score +0.20 conf 0.46: Orta Doğu’daki gerilim ve Riyad’a yönelik füze saldırısı güvenli liman talebini destekleyebilir. Ancak doların güçlü seyri ve Fed’in ileride yeniden faiz artırabileceği beklentisi altının yükselişini sınırlıyor; kısa vadeli net etki hafif pozitif görünüyor.
26.10 13:26 B4  LONG gold 5000 USD x10 @ 4027.81 (TP 4039.89, SL 4019.75; news +0.30)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
