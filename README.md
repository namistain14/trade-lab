# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 18:40 (İstanbul)

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
| Net kâr/zarar | -61.83 $ | -58.01 $ |
| İşlem sayısı | 25 | 26 |
| Kazanma oranı | %24.0 | %26.9 |
| Ödenen komisyon/spread | 59.33 $ | 61.70 $ |

**Hesap değeri: 4,940.58 $** (başlangıç 5,000 $, -59.42 $ / %-1.19)

Açık pozisyonlar: PAXGUSDT short @ 4010.30 (TP 4006.29 / SL 4012.70)

Son haber analizi (23.10 18:40): Claude puan **-0.30**, güven 0.50 — Petrol kaynaklı enflasyon endişeleri, Fed'in Aralık'ta faiz artırma olasılığını yükseltmesi ve reel faizlerin yüksek seyretmesi altın için baskı yaratıyor; İran'da savaş tırmanışı hazırlıkları ise sınırlı bir güvenli liman desteği sağlıyor. Net etki hafif negatif, ancak jeopolitik risk ve olası ani haber akışı nedeniyle güven orta düzeyde.

GPT (gpt-6-luna): puan **-0.20**, güven 0.53 — İran geriliminin tırmanma ihtimali ve tanker saldırısı güvenli liman talebini destekleyebilir; ancak petrol kaynaklı enflasyon ve yüksek reel faiz baskısı altını kısa vadede aşağı çekiyor. Altının 4.000 doların altına inmiş olması, yakın vadede düşüş baskısının ağır bastığına işaret ediyor; jeopolit

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 18:21 | PAXGUSDT | short | -6.96 $ | stop (gap) |
| 23.10 18:03 | PAXGUSDT | short | -6.25 $ | stop (gap) |
| 23.10 17:50 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 17:26 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 17:11 | PAXGUSDT | short | +3.81 $ | take profit |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -30.94 $ | -30.94 $ |
| İşlem sayısı | 5 | 5 |
| Kazanma oranı | %20.0 | %20.0 |
| Ödenen komisyon/spread | 11.86 $ | 11.86 $ |

**Hesap değeri: 4,974.39 $** (başlangıç 5,000 $, -25.61 $ / %-0.51)

Açık pozisyonlar: PAXGUSDT short @ 4015.71 (TP 4003.66 / SL 4023.74)

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
| Net kâr/zarar | -26.82 $ | -26.82 $ |
| İşlem sayısı | 3 | 3 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 7.12 $ | 7.12 $ |

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
| Net kâr/zarar | +13.82 $ | +13.82 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %100.0 | %100.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 5,019.14 $** (başlangıç 5,000 $, +19.14 $ / %+0.38)

Açık pozisyonlar: PAXGUSDT short @ 4015.71 (TP 4003.66 / SL 4023.74)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
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
23.10 18:08 N  GPT  score -0.30 conf 0.48: ABD faaliyet verilerindeki fiyat baskısı ve güçlü PMI’lar Fed’in daha şahin kalabileceği beklentisini destekleyerek altını kısa vadede baskılıyor; yüksek reel getiriler ve 4.000 dolar altındaki zayıf fiyat hareketi de bu görünümle uyumlu. Sudan ve Ukrayna kaynaklı riskler güvenli liman talebi sağlay
23.10 18:08 B6  karar turu: Claude «Piyasa jeopolitik ve makro haberler arasında yatay-hafif pozitif seyrediyor; net bir avantaj olmadığından beklemek en doğru tercih.» / GPT «Endekslerdeki sınırlı toparlanmaya rağmen haber ve fiyat teyidi birlikte güçlü değil; yüzde 1,5 hedef ve yüzde 1 stop koşullarında kaldıraçlı yeni pozisyon açmamak daha disiplinli.»
23.10 18:19 N  NEWS (11 new) score -0.50 conf 0.60: Fed'in Ekim'de faizi sabit tutması ve Aralık'ta faiz artırımı ihtimalinin yükselmesi, güçlü PMI verileri ve artan enflasyon beklentileri altın için baskı yaratıyor. Trump'ın İran savaşını hızlı bitirme olasılığını tartması ve Ukrayna'da ateşkes haberleri ise güvenli liman talebini azaltarak altını ek olarak aşağı çekiyor; altın zaten 4.000 doların altına düşmüş durumda.
23.10 18:19 N  GPT  score -0.48 conf 0.67: Fed’in daha şahin kalabileceği beklentisi, güçlü ABD PMI verileri ve yükselen enflasyon baskısı altın için olumsuz; fiyatın 4.000 doların altına inmesi de satış baskısına işaret ediyor. İran savaşının hızlı sona ermesi ihtimali ve Ukrayna’daki ateşkes haberi güvenli liman talebini sınırlayabilir; an
23.10 18:19 B1  SHORT gold 5000 USD x10 @ 4011.03 (TP 4007.02, SL 4013.43; news -0.50)
23.10 18:19 B3  CLOSE short stop (gap): -4.28 USD
23.10 18:19 B3  SHORT gold 5000 USD x10 @ 4011.13 (TP 3999.09, SL 4019.15; news -0.50)
23.10 18:28 B1  CLOSE short stop (gap): -6.96 USD
23.10 18:28 N  NEWS (7 new) score -0.45 conf 0.60: Altın, Fed'in kararı öncesinde enflasyon beklentileri yükselirken ve Fed'in Aralık'ta faiz artırımı olasılığı arttığı için baskı altında; reel faizler yüksek kalmaya devam ediyor. İran savaşı ve Ukrayna haberleri güvenli liman talebini destekleyebilir, ancak altın son haberlerde 4.000 doların altına inerken güvenli liman varlığının da satıldığı görüldü, bu da jeopolitik primin şu an zayıf olduğunu gösteriyor.
23.10 18:28 N  GPT  score -0.35 conf 0.58: Altının 4.000 doların altına gerilemesi ve yüksek reel getirilerin fırsat maliyetini artırması kısa vadede baskıyı destekliyor; enflasyon baskılarının sürmesi Fed’in gevşeme beklentilerini de sınırlayabilir. PMI verileri karışık, jeopolitik haberler ise çelişkili olduğundan düşüş yönündeki kanaat te
23.10 18:28 B3  CLOSE short stop (gap): -11.35 USD
23.10 18:28 B6  karar turu: Claude «Piyasa jeopolitik ve makro başlıklar arasında yatay-karışık seyrediyor; net bir avantaj olmadığından beklemek en doğrusu.» / GPT «Endekslerde toparlanma görülse de önümüzdeki 1–3 saatte yüzde 1,5 hedefi destekleyen haber ve fiyat uyumu bulunmadığından kaldıraçlı işlem açmamak daha disiplinli.»
23.10 18:40 N  NEWS (10 new) score -0.30 conf 0.50: Petrol kaynaklı enflasyon endişeleri, Fed'in Aralık'ta faiz artırma olasılığını yükseltmesi ve reel faizlerin yüksek seyretmesi altın için baskı yaratıyor; İran'da savaş tırmanışı hazırlıkları ise sınırlı bir güvenli liman desteği sağlıyor. Net etki hafif negatif, ancak jeopolitik risk ve olası ani haber akışı nedeniyle güven orta düzeyde.
23.10 18:40 N  GPT  score -0.20 conf 0.53: İran geriliminin tırmanma ihtimali ve tanker saldırısı güvenli liman talebini destekleyebilir; ancak petrol kaynaklı enflasyon ve yüksek reel faiz baskısı altını kısa vadede aşağı çekiyor. Altının 4.000 doların altına inmiş olması, yakın vadede düşüş baskısının ağır bastığına işaret ediyor; jeopolit
23.10 18:40 B1  SHORT gold 5000 USD x10 @ 4010.30 (TP 4006.29, SL 4012.70; news -0.30)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
