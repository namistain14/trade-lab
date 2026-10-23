# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 19:22 (İstanbul)

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
| Net kâr/zarar | -66.01 $ | -62.20 $ |
| İşlem sayısı | 26 | 27 |
| Kazanma oranı | %23.1 | %25.9 |
| Ödenen komisyon/spread | 61.70 $ | 64.07 $ |

**Hesap değeri: 4,939.75 $** (başlangıç 5,000 $, -60.25 $ / %-1.21)

Açık pozisyonlar: PAXGUSDT short @ 4018.98 (TP 4014.96 / SL 4021.39)

Son haber analizi (23.10 19:22): Claude puan **-0.20**, güven 0.35 — Başlıklar karışık ama ağırlıklı olarak altın için hafif negatif: Trump'ın İran savaşını hızla bitirme ihtimali jeopolitik güvenli liman talebini azaltıyor, Fed'in aralık ayında faiz artırımı beklentisi ve yüksek reel getiriler fırsat maliyetini yükseltiyor. Eylül enflasyon baskısının gevşemesi ise sınırlı bir dengeleyici etki yaratıyor; Paris ve Ürdün'deki saldırılar ise kısa vadede güvenli liman talebini destekleyebilecek ama etkisi zayıf haberler. Birçok başlık eski veya tekrar eden olduğu için güven düşük.

GPT (gpt-6-luna): puan **-0.20**, güven 0.42 — Trump’ın İran savaşını hızla bitirme seçeneğini değerlendirmesi ve Ukrayna’daki olası ateşkes güvenli liman talebini azaltabilir; buna karşılık bölgedeki saldırılar jeopolitik riskleri canlı tutuyor. Yüksek reel getiriler ve Fed’in sıkı kalabileceği beklentisi altın için hafif olumsuz, ancak haber a

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 18:43 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 18:21 | PAXGUSDT | short | -6.96 $ | stop (gap) |
| 23.10 18:03 | PAXGUSDT | short | -6.25 $ | stop (gap) |
| 23.10 17:50 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 17:26 | PAXGUSDT | short | -4.19 $ | stop |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -30.94 $ | -30.94 $ |
| İşlem sayısı | 5 | 5 |
| Kazanma oranı | %20.0 | %20.0 |
| Ödenen komisyon/spread | 11.86 $ | 11.86 $ |

**Hesap değeri: 4,966.94 $** (başlangıç 5,000 $, -33.06 $ / %-0.66)

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

**Hesap değeri: 5,011.70 $** (başlangıç 5,000 $, +11.70 $ / %+0.23)

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
23.10 18:40 N  NEWS (10 new) score -0.30 conf 0.50: Petrol kaynaklı enflasyon endişeleri, Fed'in Aralık'ta faiz artırma olasılığını yükseltmesi ve reel faizlerin yüksek seyretmesi altın için baskı yaratıyor; İran'da savaş tırmanışı hazırlıkları ise sınırlı bir güvenli liman desteği sağlıyor. Net etki hafif negatif, ancak jeopolitik risk ve olası ani haber akışı nedeniyle güven orta düzeyde.
23.10 18:40 N  GPT  score -0.20 conf 0.53: İran geriliminin tırmanma ihtimali ve tanker saldırısı güvenli liman talebini destekleyebilir; ancak petrol kaynaklı enflasyon ve yüksek reel faiz baskısı altını kısa vadede aşağı çekiyor. Altının 4.000 doların altına inmiş olması, yakın vadede düşüş baskısının ağır bastığına işaret ediyor; jeopolit
23.10 18:40 B1  SHORT gold 5000 USD x10 @ 4010.30 (TP 4006.29, SL 4012.70; news -0.30)
23.10 18:49 B1  CLOSE short stop: -4.19 USD
23.10 18:49 N  NEWS (9 new) score -0.35 conf 0.50: 
23.10 18:49 N  GPT  score -0.25 conf 0.42: Faizlerin sıkı kalacağı ve enflasyon baskılarının sürdüğü yönündeki haberler, kısa vadede reel faizler ve dolar kanalıyla altın üzerinde baskı yaratabilir. Bölgesel çatışmalar güvenli liman talebini desteklese de haber akışı karışık ve altındaki düşüşün bir kısmı zaten fiyatlanmış görünüyor.
23.10 18:49 B6  karar turu: Claude «Piyasa enerji ve jeopolitik haber akışı altında dar bantta yön arıyor; net bir avantaj olmadığından kenarda kalmak en doğrusu.» / GPT «Endekslerde yön teyidi ve taze şirkete özgü katalizörler yetersiz olduğundan, önümüzdeki 1–3 saat için yüzde 1,5 hedefli kaldıraçlı işlemlerde beklemek daha disiplinli.»
23.10 19:01 N  NEWS (11 new) score -0.25 conf 0.40: Haberler karışık ama net eğilim hafif negatif: Trump'ın İran savaşını hızla bitirme ihtimali jeopolitik risk primini azaltıyor, kritik Fed toplantısı öncesi enflasyon kaygıları ve yüksek reel faizler sıkılaştırma beklentisini destekliyor. Buna karşılık ABD/İsrail'in olası İran saldırısına hazırlandığı haberi ve sürmekte olan savaş riskleri güvenli liman talebini sınırlı da olsa destekliyor; ayrıca bazı başlıklar eski veya zaten fiyatlanmış olabilir.
23.10 19:01 N  GPT  score -0.25 conf 0.48: İran savaşının hızlı sona erdirilmesi ihtimali güvenli liman talebini sınırlayabilir; ancak haber net bir karar değil ve çatışmanın seyri belirsiz. Altının 4.000 doların altına gerilemesi ve yüksek reel faizlerin fırsat maliyetini artırması kısa vadede hafif aşağı yönlü baskıyı destekliyor.
23.10 19:01 B1  SHORT gold 5000 USD x10 @ 4018.98 (TP 4014.96, SL 4021.39; news -0.25)
23.10 19:13 N  NEWS (11 new) score -0.30 conf 0.40: 
23.10 19:13 N  GPT  score -0.25 conf 0.48: Altının 4.000 doların altına gerilemesi ve yüksek reel faizlerin fırsat maliyetini artırması kısa vadede baskı yaratıyor. Yeni bölgesel saldırılar güvenli liman talebini destekleyebilir; ancak İran savaşının hızlı sona erebileceği haberleri ve karışık enflasyon sinyalleri düşüşü sınırlıyor.
23.10 19:13 B6  karar turu: Claude «Piyasa öğle saatlerinde yatay ve kararsız; enerji öne çıkarken teknoloji hafif pozitif, net bir işlem fırsatı görünmüyor.» / GPT «Endekslerde dar bant ve Tesla'da önceden gerçekleşmiş satış baskısı nedeniyle mevcut haber-fiyat uyumu yeni pozisyon açmak için yeterince güçlü değil.»
23.10 19:22 N  NEWS (10 new) score -0.20 conf 0.35: Başlıklar karışık ama ağırlıklı olarak altın için hafif negatif: Trump'ın İran savaşını hızla bitirme ihtimali jeopolitik güvenli liman talebini azaltıyor, Fed'in aralık ayında faiz artırımı beklentisi ve yüksek reel getiriler fırsat maliyetini yükseltiyor. Eylül enflasyon baskısının gevşemesi ise sınırlı bir dengeleyici etki yaratıyor; Paris ve Ürdün'deki saldırılar ise kısa vadede güvenli liman talebini destekleyebilecek ama etkisi zayıf haberler. Birçok başlık eski veya tekrar eden olduğu için güven düşük.
23.10 19:22 N  GPT  score -0.20 conf 0.42: Trump’ın İran savaşını hızla bitirme seçeneğini değerlendirmesi ve Ukrayna’daki olası ateşkes güvenli liman talebini azaltabilir; buna karşılık bölgedeki saldırılar jeopolitik riskleri canlı tutuyor. Yüksek reel getiriler ve Fed’in sıkı kalabileceği beklentisi altın için hafif olumsuz, ancak haber a
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
