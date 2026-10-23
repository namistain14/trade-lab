# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 18:01 (İstanbul)

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
| Net kâr/zarar | -48.61 $ | -44.80 $ |
| İşlem sayısı | 23 | 24 |
| Kazanma oranı | %26.1 | %29.2 |
| Ödenen komisyon/spread | 54.58 $ | 56.95 $ |

**Hesap değeri: 4,952.05 $** (başlangıç 5,000 $, -47.95 $ / %-0.96)

Açık pozisyonlar: PAXGUSDT short @ 4014.13 (TP 4010.11 / SL 4016.54)

Son haber analizi (23.10 18:01): Claude puan **-0.45**, güven 0.60 — Altın 4.000 doların altına indi ve "sığınak" varlık olarak da satış baskısı görülüyor; bu, jeopolitik riskin altına destek olmadığını gösteriyor. Fed'in Ekim'de faiz sabit tutması ama Aralık'ta artış ihtimalini yükseltmesi, güçlü ABD PMI verileri ve enflasyon baskısı reel faiz ve dolar tarafında altı aşağı çekiyor. Ukrayna ve İran'daki gerilim haberleri ise kısa vadede yukarı yönlü destek sağlayabilir, ancak mevcut fiyat hareketi bu etkiyi bastırıyor.

GPT (gpt-6-luna): puan **-0.35**, güven 0.62 — Altının 4.000 doların altına gerilemesi, yüksek reel getiriler ve güçlü PMI verilerinin Fed’in daha sıkı kalabileceği beklentisini desteklemesi kısa vadede baskı yaratıyor. Kyiv’e yeni saldırılar güvenli liman talebini artırabilir; bu nedenle düşüş yönündeki görünümün gücü sınırlı.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 17:50 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 17:26 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 17:11 | PAXGUSDT | short | +3.81 $ | take profit |
| 23.10 16:49 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 16:32 | PAXGUSDT | short | -4.51 $ | stop (gap) |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -30.94 $ | -30.94 $ |
| İşlem sayısı | 5 | 5 |
| Kazanma oranı | %20.0 | %20.0 |
| Ödenen komisyon/spread | 11.86 $ | 11.86 $ |

**Hesap değeri: 4,967.88 $** (başlangıç 5,000 $, -32.12 $ / %-0.64)

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
| Net kâr/zarar | -11.19 $ | -11.19 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 4,987.62 $** (başlangıç 5,000 $, -12.38 $ / %-0.25)

Açık pozisyonlar: PAXGUSDT short @ 4015.71 (TP 4003.66 / SL 4023.74)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +13.82 $ | +13.82 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %100.0 | %100.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 5,012.63 $** (başlangıç 5,000 $, +12.63 $ / %+0.25)

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
23.10 17:33 N  NEWS (6 new) score -0.12 conf 0.35: Fed'in Ekim'de faiz sabit tutmasının Aralık artırım olasılıklarını yükseltmesi ve "altın güvenli liman talebini kaybediyor" başlığı altın için kısa vadede baskı yaratıyor. İran savaşı ve jeopolitik gerilim riskleri destekleyici olsa da zaten fiyatlanmış görünüyor; enflasyon beklentilerinin yükselmesi ve ABD iş aktivitesindeki karışık veriler ise sinyalleri çelişkili kılıyor.
23.10 17:33 N  GPT  score -0.15 conf 0.34: ABD iş aktivitesindeki yavaşlama altını destekleyebilir; ancak talebin fiyat baskılarını artırması ve Aralık’ta faiz artırımı olasılığının yükselmesi kısa vadede daha güçlü dolar/faiz beklentisiyle baskı yaratabilir. Ukrayna’daki esir takası gerilimi bir miktar azaltırken, İran’a ilişkin haberler gü
23.10 17:40 N  NEWS (8 new) score -0.05 conf 0.35: 
23.10 17:40 N  GPT  score +0.15 conf 0.38: İran savaşının yeniden başlayabileceğine dair haberler ve saldırıların önlenmesi kısa vadede güvenli liman talebini destekleyebilir. Ancak artan enflasyon baskıları ve Fed’in faiz artırımı ihtimalinin yükselmesi altın için olumsuz; net etki bu nedenle sınırlı ve belirsiz.
23.10 17:48 N  NEWS (8 new) score -0.30 conf 0.50: Yeni başlıklar karışık: ABD-İsrail'in İran'a olası saldırı hazırlığı ve Trump'ın yeni saldırı tehdidi güvenli liman talebini destekliyor, ancak güçlü ABD PMI verileri ve Fed'in Aralık'ta faiz artırma olasılığını yükselten duruş, reel faizleri ve doları yukarı iterek altını baskılıyor. Ayrıca "Haven trade" çözülmesi ve reel faizlerin altın üzerindeki baskısı gibi haberler kısa vadede düşüş yönünü öne çıkarıyor; Kübü füze krizi haberi ise eski olduğu için dikkate alınmadı.
23.10 17:48 N  GPT  score -0.25 conf 0.55: Güçlü ABD PMI verileri ve yüksek reel getiriler altının fırsat maliyetini artırarak kısa vadede baskı yaratabilir. İran gerilimi ve Batı Şeria’daki saldırı güvenli liman talebini destekliyor; bu karşıt etkiler düşüşün sınırlı kalabileceğini düşündürüyor.
23.10 17:48 B1  SHORT gold 5000 USD x10 @ 4018.37 (TP 4014.35, SL 4020.78; news -0.30)
23.10 17:50 B1  CLOSE short stop: -4.19 USD
23.10 17:50 B6  karar turu: Claude «Piyasa karışık bir seyir izliyor: teknoloji önde, geniş endeks hafif ekside ve makro veriler nötr olduğundan beklemek en doğrusu.» / GPT «Endekslerde toparlanma görülse de mevcut haber ve fiyat birleşimi, kaldıraçlı ve sabit hedefli işlemler için yeterince net avantaj sunmuyor.»
23.10 18:01 N  NEWS (10 new) score -0.45 conf 0.60: Altın 4.000 doların altına indi ve "sığınak" varlık olarak da satış baskısı görülüyor; bu, jeopolitik riskin altına destek olmadığını gösteriyor. Fed'in Ekim'de faiz sabit tutması ama Aralık'ta artış ihtimalini yükseltmesi, güçlü ABD PMI verileri ve enflasyon baskısı reel faiz ve dolar tarafında altı aşağı çekiyor. Ukrayna ve İran'daki gerilim haberleri ise kısa vadede yukarı yönlü destek sağlayabilir, ancak mevcut fiyat hareketi bu etkiyi bastırıyor.
23.10 18:01 N  GPT  score -0.35 conf 0.62: Altının 4.000 doların altına gerilemesi, yüksek reel getiriler ve güçlü PMI verilerinin Fed’in daha sıkı kalabileceği beklentisini desteklemesi kısa vadede baskı yaratıyor. Kyiv’e yeni saldırılar güvenli liman talebini artırabilir; bu nedenle düşüş yönündeki görünümün gücü sınırlı.
23.10 18:01 B1  SHORT gold 5000 USD x10 @ 4014.13 (TP 4010.11, SL 4016.54; news -0.45)
23.10 18:01 B2  SHORT gold 5000 USD x10 @ 4015.71 (TP 4003.66, SL 4023.74; news -0.45)
23.10 18:01 B3  SHORT gold 5000 USD x10 @ 4015.71 (TP 4003.66, SL 4023.74; news -0.45)
23.10 18:01 B5  SHORT gold 5000 USD x10 @ 4015.71 (TP 4003.66, SL 4023.74; news -0.40)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
