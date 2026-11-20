# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 20.11.2026 18:34 (İstanbul)

## Bot A — Kripto 1 saatlik trend (x1)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +37.10 $ | +104.97 $ |
| İşlem sayısı | 1 | 2 |
| Kazanma oranı | %100.0 | %100.0 |
| Ödenen komisyon/spread | 1.63 $ | 3.25 $ |

**Hesap değeri: 5,104.97 $** (başlangıç 5,000 $, +104.97 $ / %+2.10)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 20.11 04:03 | SOLUSDT | short | +37.10 $ | time limit |
| 19.11 01:49 | XRPUSDT | short | +67.87 $ | take profit |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +288.14 $ | +340.52 $ |
| İşlem sayısı | 37 | 190 |
| Kazanma oranı | %51.4 | %46.3 |
| Ödenen komisyon/spread | 447.88 $ | 2270.80 $ |

**Hesap değeri: 5,334.47 $** (başlangıç 5,000 $, +334.47 $ / %+6.69)

Açık pozisyonlar: PAXGUSDT short @ 3543.51 (TP 3532.88 / SL 3550.60)

Son haber analizi (20.11 18:34): Claude puan **-0.50**, güven 0.60 — Haberlerin çoğu altın için olumsuz: Fed'de sıkılaşma (faiz artırımı) tartışması, doların 19 ayın zirvesine yakın seyretmesi ve altının 14 aylık dip seviyelere inmesi baskı oluşturuyor. Ukrayna/Polonya'daki füze saldırıları ve İran'a yeni saldırı ihtimali gibi jeopolitik riskler güvenli liman talebi yaratabilir, ancak piyasada bu riskler henüz altını yukarı taşımıyor; bu nedenle etkisi sınırlı kalıyor.

GPT (gpt-6-luna): puan **-0.35**, güven 0.58 — Fed’in daha şahin faiz beklentileri ve 19 ayın zirvesine yakın dolar, önümüzdeki saatlerde altın üzerinde baskın ve net bir aşağı yönlü etken. Rusya-Ukrayna gerilimi güvenli liman talebini destekleyebilir; ancak altındaki sert düşüş bu desteğin şimdilik zayıf kaldığını düşündürüyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 20.11 18:28 | PAXGUSDT | short | +68.95 $ | take profit |
| 20.11 17:53 | PAXGUSDT | short | +68.97 $ | take profit |
| 20.11 17:42 | PAXGUSDT | short | +68.97 $ | take profit |
| 20.11 17:32 | PAXGUSDT | short | -56.06 $ | stop |
| 20.11 17:12 | PAXGUSDT | short | -56.06 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -123.04 $ |
| İşlem sayısı | 0 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 0.00 $ | 70.51 $ |

**Hesap değeri: 4,876.96 $** (başlangıç 5,000 $, -123.04 $ / %-2.46)

Son haber analizi (18.11 11:41): Claude puan **+0.30**, güven 0.40 — Hürmüz Boğazı'nda ADNOC gemisinin vurulması ve gaz tankerine isabet gibi yeni saldırılar, ayrıca ABD'nin İran adasını vurması ve Bahreyn/Kuwait'e dronlar, arz riski primini yukarı çekebilir. Buna karşılık Brent'in 100 doların altına inmesi, fazla arz ve bozulan fiyat yapısı (backwardation, zayıf motorin) gibi baskılayıcı haberler piyasada zaten fiyatlanmış görünüyor; bu nedenle net etki hafif yukarı yönlü ama belirsiz.

GPT (gpt-6-luna): puan **+0.58**, güven 0.68 — Hürmüz Boğazı’nda ADNOC bağlantılı gemiye saldırı, can kaybı ve başka bir tanker hasarı haberleri yakın vadeli arz kesintisi risk primini artırıyor. Ancak arz fazlası endişeleri ve petrolün 100 doların altına indiğine dair haberler yükselişi sınırlayabilir.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 10.11 08:01 | BZ=F | short | -67.46 $ | stop (gap) |
| 06.11 22:41 | BZ=F | long | -63.26 $ | stop (gap) |
| 06.11 08:11 | BZ=F | long | -58.75 $ | stop |
| 02.11 23:09 | BZ=F | short | +66.43 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -585.35 $ | +17940.58 $ |
| İşlem sayısı | 3 | 73 |
| Kazanma oranı | %33.3 | %50.7 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 119,846.43 $** (başlangıç 100,000 $, +19846.43 $ / %+19.85)

Açık pozisyonlar: AAPL long @ 350.62 (TP 356.07 / SL 347.30); QQQ short @ 631.49 (TP 621.60 / SL 637.38); TSLA short @ 362.67 (TP 356.96 / SL 366.02)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 20.11 18:28 | SPY | long | -1223.81 $ | stop |
| 20.11 17:57 | TSLA | long | +1846.64 $ | take profit |
| 20.11 17:36 | AAPL | long | -1208.18 $ | stop |
| 19.11 23:46 | TSLA | long | -282.10 $ | seans sonu |
| 19.11 23:46 | AAPL | short | +524.76 $ | seans sonu |

## Son olaylar

```
20.11 18:05 B6  ALIŞ SPY 169 adet ≈ 121,033 $ (1:4) @ 716.17 (TP 726.91, SL 709.01; ikisi de hemfikir, güven 0.50)
20.11 18:10 N  NEWS (12 new) score -0.20 conf 0.40: Altın 14 aylık dibe yakın ve satış baskısı altında; Fed'in sert (hawkish) söylemleri ve güçlü doların (tek kazanan olarak öne çıkması) kısa vadede altını aşağı çekiyor. İran'a yeni saldırı ihtimali ve Polonya'ya füze isabeti gibi jeopolitik gerilimler güvenli liman talebi yaratabilir, ancak piyasa bu haberlere şimdiye kadar altında belirgin bir yükseliş vermedi; bu nedenle etki sınırlı ve karışık.
20.11 18:10 N  GPT  score +0.18 conf 0.43: İran’a yönelik yeni saldırı olasılığı ve Rus füzesinin Polonya’ya düşmesi kısa vadede güvenli liman talebini artırabilir. Ancak altındaki sert satış baskısı ve şahin Fed beklentileri yükselişi sınırlıyor; haberlerin fiilî tırmanışa dönüşüp dönüşmeyeceği belirsiz.
20.11 18:16 B6  karar turu: Claude «Teknoloji, NVDA öncülüğünde baskı altında; SPY ise daha dirençli ve piyasa genelinde karışık, hafif negatif bir seyir var.» / GPT «Teknoloji hisselerindeki göreli zayıflık ve başarısız tepki yükselişleri önümüzdeki 1–3 saat için aşağı yönlü işlemlere sınırlı avantaj sağlıyor.»
20.11 18:22 N  NEWS (10 new) score -0.50 conf 0.60: Yeni başlıklar ağırlıklı olarak altın için olumsuz: Fed faiz artırımı beklentileri ve güçlenen dolar (dolar 4 haftalık yükseliş serisinde), altının haftalık en kötü performansa yönelmesi ve zorunlu satışlar baskı yaratıyor. ABD/İsrail'in İran'a yeni saldırı planladığı haberi ve Polonya'daki füze olayı güvenli liman talebini destekleyebilir, ancak bu etkiler jeopolitik riskin zaten kısmen fiyatlanmış olması ve Fed/dolar etkisinin daha baskın görünmesi nedeniyle sınırlı kalıyor.
20.11 18:22 N  GPT  score -0.65 conf 0.72: Önümüzdeki saatlerde altın için baskın etkenler, Fed’in daha şahin olabileceği beklentisi ve doların üst üste dördüncü haftalık yükselişe yönelmesi; bunlar altını aşağı çekiyor. İran’a ilişkin yaptırım ve olası çatışma haberleri güvenli liman talebi yaratabilir, ancak yeni bir tırmanış teyit edilmed
20.11 18:22 B5  SHORT gold 25000 USD x10 @ 3535.27 (TP 3524.67, SL 3542.34; news -0.57)
20.11 18:28 B5  CLOSE short take profit: +68.95 USD
20.11 18:28 B6  CLOSE long SPY stop: -1223.81 USD
20.11 18:28 B6  karar turu: Claude «Piyasa teknoloji öncülüğünde satış baskısı altında ve kısa vadeli momentum aşağı yönlü; zaten sert düşmüş hisselerde kovalamaktan kaçınıyorum.» / GPT «Kısa vadeli görünüm satıcılı; ancak diplerden tepki ve aynı yöne açılan pozisyonların korelasyonu nedeniyle 1:4 kaldıraçta toplam risk sınırlı tutulmalı.»
20.11 18:28 B6  AÇIĞA SATIŞ QQQ 189 adet ≈ 119,272 $ (1:4) @ 631.07 (TP 621.6, SL 637.38; ikisi de hemfikir, güven 0.55)
20.11 18:28 B6  AÇIĞA SATIŞ TSLA 330 adet ≈ 119,592 $ (1:4) @ 362.4 (TP 356.96, SL 366.02; ikisi de hemfikir, güven 0.50)
20.11 18:34 N  NEWS (15 new) score -0.50 conf 0.60: Haberlerin çoğu altın için olumsuz: Fed'de sıkılaşma (faiz artırımı) tartışması, doların 19 ayın zirvesine yakın seyretmesi ve altının 14 aylık dip seviyelere inmesi baskı oluşturuyor. Ukrayna/Polonya'daki füze saldırıları ve İran'a yeni saldırı ihtimali gibi jeopolitik riskler güvenli liman talebi yaratabilir, ancak piyasada bu riskler henüz altını yukarı taşımıyor; bu nedenle etkisi sınırlı kalıyor.
20.11 18:34 N  GPT  score -0.35 conf 0.58: Fed’in daha şahin faiz beklentileri ve 19 ayın zirvesine yakın dolar, önümüzdeki saatlerde altın üzerinde baskın ve net bir aşağı yönlü etken. Rusya-Ukrayna gerilimi güvenli liman talebini destekleyebilir; ancak altındaki sert düşüş bu desteğin şimdilik zayıf kaldığını düşündürüyor.
20.11 18:34 B5  SHORT gold 25000 USD x10 @ 3543.51 (TP 3532.88, SL 3550.60; news -0.42)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
