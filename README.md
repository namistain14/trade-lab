# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 18:19 (İstanbul)

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
| Net kâr/zarar | -54.86 $ | -51.05 $ |
| İşlem sayısı | 24 | 25 |
| Kazanma oranı | %25.0 | %28.0 |
| Ödenen komisyon/spread | 56.95 $ | 59.32 $ |

**Hesap değeri: 4,946.88 $** (başlangıç 5,000 $, -53.12 $ / %-1.06)

Açık pozisyonlar: PAXGUSDT short @ 4011.03 (TP 4007.02 / SL 4013.43)

Son haber analizi (23.10 18:19): Claude puan **-0.50**, güven 0.60 — Fed'in Ekim'de faizi sabit tutması ve Aralık'ta faiz artırımı ihtimalinin yükselmesi, güçlü PMI verileri ve artan enflasyon beklentileri altın için baskı yaratıyor. Trump'ın İran savaşını hızlı bitirme olasılığını tartması ve Ukrayna'da ateşkes haberleri ise güvenli liman talebini azaltarak altını ek olarak aşağı çekiyor; altın zaten 4.000 doların altına düşmüş durumda.

GPT (gpt-6-luna): puan **-0.48**, güven 0.67 — Fed’in daha şahin kalabileceği beklentisi, güçlü ABD PMI verileri ve yükselen enflasyon baskısı altın için olumsuz; fiyatın 4.000 doların altına inmesi de satış baskısına işaret ediyor. İran savaşının hızlı sona ermesi ihtimali ve Ukrayna’daki ateşkes haberi güvenli liman talebini sınırlayabilir; an

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 18:03 | PAXGUSDT | short | -6.25 $ | stop (gap) |
| 23.10 17:50 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 17:26 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 17:11 | PAXGUSDT | short | +3.81 $ | take profit |
| 23.10 16:49 | PAXGUSDT | short | -4.19 $ | stop |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -30.94 $ | -30.94 $ |
| İşlem sayısı | 5 | 5 |
| Kazanma oranı | %20.0 | %20.0 |
| Ödenen komisyon/spread | 11.86 $ | 11.86 $ |

**Hesap değeri: 4,972.82 $** (başlangıç 5,000 $, -27.18 $ / %-0.54)

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
| Net kâr/zarar | -15.47 $ | -15.47 $ |
| İşlem sayısı | 2 | 2 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 4.75 $ | 4.75 $ |

**Hesap değeri: 4,982.58 $** (başlangıç 5,000 $, -17.42 $ / %-0.35)

Açık pozisyonlar: PAXGUSDT short @ 4011.13 (TP 3999.09 / SL 4019.15)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 18:03 | PAXGUSDT | short | -4.28 $ | stop (gap) |
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +13.82 $ | +13.82 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %100.0 | %100.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 5,017.57 $** (başlangıç 5,000 $, +17.57 $ / %+0.35)

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
23.10 18:01 N  NEWS (10 new) score -0.45 conf 0.60: Altın 4.000 doların altına indi ve "sığınak" varlık olarak da satış baskısı görülüyor; bu, jeopolitik riskin altına destek olmadığını gösteriyor. Fed'in Ekim'de faiz sabit tutması ama Aralık'ta artış ihtimalini yükseltmesi, güçlü ABD PMI verileri ve enflasyon baskısı reel faiz ve dolar tarafında altı aşağı çekiyor. Ukrayna ve İran'daki gerilim haberleri ise kısa vadede yukarı yönlü destek sağlayabilir, ancak mevcut fiyat hareketi bu etkiyi bastırıyor.
23.10 18:01 N  GPT  score -0.35 conf 0.62: Altının 4.000 doların altına gerilemesi, yüksek reel getiriler ve güçlü PMI verilerinin Fed’in daha sıkı kalabileceği beklentisini desteklemesi kısa vadede baskı yaratıyor. Kyiv’e yeni saldırılar güvenli liman talebini artırabilir; bu nedenle düşüş yönündeki görünümün gücü sınırlı.
23.10 18:01 B1  SHORT gold 5000 USD x10 @ 4014.13 (TP 4010.11, SL 4016.54; news -0.45)
23.10 18:01 B2  SHORT gold 5000 USD x10 @ 4015.71 (TP 4003.66, SL 4023.74; news -0.45)
23.10 18:01 B3  SHORT gold 5000 USD x10 @ 4015.71 (TP 4003.66, SL 4023.74; news -0.45)
23.10 18:01 B5  SHORT gold 5000 USD x10 @ 4015.71 (TP 4003.66, SL 4023.74; news -0.40)
23.10 18:08 B1  CLOSE short stop (gap): -6.25 USD
23.10 18:08 N  NEWS (4 new) score -0.40 conf 0.50: Yeni başlıklar ağırlıklı olarak altı baskılıyor: Fed'in Ekim'de faiz sabit tutması Aralık'ta faiz artırımı olasılığını yükseltti, ABD imalat ve hizmet PMI'ları güçlü ve fiyat baskıları yüksek, tüketici enflasyon beklentileri arttı, altın ise 4.000 doların altına düşerek 'sığınak' talebinin de satışta olduğunu gösterdi. Buna karşın İran savaşı ve Ukrayna-Rusya gerilimi gibi jeopolitik riskler sürüyor, ancak bunlar fiyatta yeterli yansımadı; yakın Fed toplantısı ve veri sürprizleri yön belirleyebilir, bu yüzden güven orta düzeyde.
23.10 18:08 N  GPT  score -0.30 conf 0.48: ABD faaliyet verilerindeki fiyat baskısı ve güçlü PMI’lar Fed’in daha şahin kalabileceği beklentisini destekleyerek altını kısa vadede baskılıyor; yüksek reel getiriler ve 4.000 dolar altındaki zayıf fiyat hareketi de bu görünümle uyumlu. Sudan ve Ukrayna kaynaklı riskler güvenli liman talebi sağlay
23.10 18:08 B6  karar turu: Claude «Piyasa jeopolitik ve makro haberler arasında yatay-hafif pozitif seyrediyor; net bir avantaj olmadığından beklemek en doğru tercih.» / GPT «Endekslerdeki sınırlı toparlanmaya rağmen haber ve fiyat teyidi birlikte güçlü değil; yüzde 1,5 hedef ve yüzde 1 stop koşullarında kaldıraçlı yeni pozisyon açmamak daha disiplinli.»
23.10 18:19 N  NEWS (11 new) score -0.50 conf 0.60: Fed'in Ekim'de faizi sabit tutması ve Aralık'ta faiz artırımı ihtimalinin yükselmesi, güçlü PMI verileri ve artan enflasyon beklentileri altın için baskı yaratıyor. Trump'ın İran savaşını hızlı bitirme olasılığını tartması ve Ukrayna'da ateşkes haberleri ise güvenli liman talebini azaltarak altını ek olarak aşağı çekiyor; altın zaten 4.000 doların altına düşmüş durumda.
23.10 18:19 N  GPT  score -0.48 conf 0.67: Fed’in daha şahin kalabileceği beklentisi, güçlü ABD PMI verileri ve yükselen enflasyon baskısı altın için olumsuz; fiyatın 4.000 doların altına inmesi de satış baskısına işaret ediyor. İran savaşının hızlı sona ermesi ihtimali ve Ukrayna’daki ateşkes haberi güvenli liman talebini sınırlayabilir; an
23.10 18:19 B1  SHORT gold 5000 USD x10 @ 4011.03 (TP 4007.02, SL 4013.43; news -0.50)
23.10 18:19 B3  CLOSE short stop (gap): -4.28 USD
23.10 18:19 B3  SHORT gold 5000 USD x10 @ 4011.13 (TP 3999.09, SL 4019.15; news -0.50)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
