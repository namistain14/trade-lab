# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 06.11.2026 03:25 (İstanbul)

## Bot A — Kripto 1 saatlik trend (x1)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -55.91 $ | -89.85 $ |
| İşlem sayısı | 1 | 53 |
| Kazanma oranı | %0.0 | %43.4 |
| Ödenen komisyon/spread | 11.83 $ | 629.29 $ |

**Hesap değeri: 4,910.15 $** (başlangıç 5,000 $, -89.85 $ / %-1.80)

Son haber analizi (06.11 03:19): Claude puan **+0.02**, güven 0.35 — Haberler birbiriyle çelişiyor: İran savaşı ve Hormuz patlamaları güvenli liman talebini destekliyor, Polonya'nın altın alımına açık kapı tutumu da olumlu. Buna karşılık doların güçlü kalması, Fed'in şahin duruşu ve Goldman'ın altın tahminlerini düşürmesi baskı yaratıyor; NFP verisi öncesi belirsizlik de yüksek. Net etki nötre yakın olduğu için düşük güven ile hafif pozitif skor veriyorum.

GPT (gpt-6-luna): puan **+0.18**, güven 0.38 — İran savaşı ve Hürmüz Boğazı’na ilişkin belirsizlik güvenli liman talebini destekleyebilir; altın da son haberlerde yükseliş momentumunda. Ancak doların güçlü seyri, Fed’in şahin beklentileri ve yaklaşan istihdam verisi yükselişi sınırlıyor; haberlerin bir kısmı zaten fiyatlanmış olabilir.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 02:52 | PAXGUSDT | long | -55.91 $ | stop |
| 05.11 19:13 | PAXGUSDT | short | -55.93 $ | stop |
| 05.11 19:03 | PAXGUSDT | short | -55.93 $ | stop |
| 05.11 18:54 | PAXGUSDT | short | +69.10 $ | take profit |
| 05.11 18:18 | PAXGUSDT | short | -55.93 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +66.43 $ |
| İşlem sayısı | 0 | 1 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 17.17 $ |

**Hesap değeri: 5,066.43 $** (başlangıç 5,000 $, +66.43 $ / %+1.33)

Son haber analizi (05.11 07:59): Claude puan **-0.05**, güven 0.40 — Haberler çelişkili: İran'ın Hürmüz'de dört tankerin mayınlarla vurulduğunu öne sürmesi ve petrol fiyatlarındaki Hürmüz arz riskleri fiyatı yukarı iter; buna karşılık Brent'in İran müzakereleri nedeniyle 4 haftalık dibe inmesi ve ABD-İran arasında anlaşmanın hâlâ uzak olması aşağı yönlü baskı yaratır. Tanker iddiası doğrulanmamış olduğu için net etki hafif pozitif, güven düşük.

GPT (gpt-6-luna): puan **+0.28**, güven 0.55 — Hürmüz’de iki tanker ve bir römorkörün alev aldığı haberi, doğrulanması hâlinde yakın vadeli arz ve taşımacılık risk primini artırarak Brent’i yukarı destekleyebilir. Ancak İran geriliminin azalacağı beklentileriyle süren sert satış ve haberin nedeni hakkındaki belirsizlik yükseliş etkisini sınırlıy

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 23:09 | BZ=F | short | +66.43 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +5879.74 $ |
| İşlem sayısı | 0 | 21 |
| Kazanma oranı | %0.0 | %52.4 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 108,278.00 $** (başlangıç 100,000 $, +8278.00 $ / %+8.28)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 05.11 23:46 | SPY | short | +582.01 $ | seans sonu |
| 05.11 23:46 | QQQ | short | +576.72 $ | seans sonu |
| 05.11 23:46 | NVDA | short | +1215.36 $ | seans sonu |
| 05.11 23:46 | AAPL | long | +93.44 $ | seans sonu |
| 05.11 20:37 | QQQ | short | -1070.92 $ | stop |

## Son olaylar

```
06.11 02:06 N  GPT  score -0.15 conf 0.30: Doların güvenli liman talebiyle yükseldiğine dair haberler ve şahin Fed beklentisi altın üzerinde hafif baskı yaratabilir. Ancak İran savaşıyla ilgili başlıklar yeni bir tırmanış göstermiyor; altın görünümüne ilişkin haberler de çelişkili olduğundan etki sınırlı ve belirsiz.
06.11 02:18 N  NEWS (5 new) score -0.10 conf 0.30: Başlıkların çoğu siyasi ve yerel haberler; yeni gelen haberlerin altın fiyatına doğrudan etkisi zayıf. Goldman'ın şahin Fed nedeniyle altın hedeflerini düşürmesi ve dolara güvenli liman talebinin yansıması hafif baskılayıcı, İran savaşının sürmesi ise sınırlı destek sağlıyor; bu nedenle net etki hafif negatif ve düşük güvenli.
06.11 02:18 N  GPT  score -0.15 conf 0.34: Doların güvenli liman talebiyle güçlenmesi ve Fed’e ilişkin şahin beklentiler altın üzerinde kısa vadeli baskı yaratabilir. İran savaşı ve Sudan’daki çatışmalar güvenli liman talebini desteklese de başlıklar çelişkili ve çoğu yeni bir piyasa katalizörü sunmuyor.
06.11 02:31 N  NEWS (12 new) score +0.10 conf 0.30: 
06.11 02:31 N  GPT  score +0.35 conf 0.48: Trump’ın İran konusunda yakında karar vereceğini söylemesi ve Hürmüz’de patlama iddiaları kısa vadede güvenli liman talebini destekleyebilir. Ancak doların güçlenmesi altını baskılayabilir; haberler belirsiz ve çelişkili olduğundan etki sınırlı, güven düşük-orta düzeyde.
06.11 02:43 N  NEWS (5 new) score +0.40 conf 0.50: Altın, İran savaşındaki tırmanış ve Hürmüz'deki patlama iddialarıyla güvenli liman talebinden, Polonya Merkez Bankası'nın ek altın alımı sinyalinden ve iki haftalık zirve tazelemesinden destek görüyor. Buna karşılık güvenli liman kaynaklı dolar gücü, NFP öncesi bekleme ve olası Fed beklentisi değişimleri kısa vadeli riskleri artırıyor; bu nedenle sinyal orta düzeyde pozitif ama güven sınırlı.
06.11 02:43 N  GPT  score +0.35 conf 0.43: Altın fiyatının iki haftanın zirvesine çıkması ve Polonya Merkez Bankası’nın ek alımlara açık olması kısa vadede destekleyici; İran kararına ilişkin belirsizlik de güvenli liman talebini artırabilir. Ancak doların güçlenmesi ve yaklaşan ABD istihdam verisi yönü sınırlıyor, bu nedenle görünüm temkinl
06.11 02:45 B5  LONG gold 25000 USD x10 @ 4091.00 (TP 4103.27, SL 4082.82; news +0.38)
06.11 02:51 B5  CLOSE long stop: -55.91 USD
06.11 02:55 N  NEWS (4 new) score +0.15 conf 0.40: 
06.11 02:55 N  GPT  score +0.25 conf 0.36: İran savaşı ve Hürmüz’deki patlama iddiaları güvenli liman talebini destekleyebilir; ancak görüşmelerin sürmesi ve doların güçlenmesi yükselişi sınırlıyor. NFP öncesinde altının zaten iki haftanın zirvesine yaklaşmış olması kısa vadeli yön konusunda temkini gerektiriyor.
06.11 03:07 N  NEWS (7 new) score -0.10 conf 0.40: Yeni haberlerde net bir yön yok: Goldman'ın altın tahminlerini Fed'in şahin duruşu nedeniyle düşürmesi ve ABD doları güvenli liman talebinin artması kısa vadede baskı yaratıyor. Buna karşılık İran savaşı ve Hürmüz'deki patlama iddiaları ile teknoloji hisselerindeki sert düşüş jeopolitik ve risk-off talebini destekleyerek altını kısmen dengeliyor; NFP öncesi fiyat zaten ~4.100 seviyesinde olduğu için etki sınırlı kalabilir.
06.11 03:07 N  GPT  score +0.18 conf 0.31: İran savaşıyla ilgili belirsizlik ve olası gerilim güvenli liman talebini destekleyebilir; ancak doların güvenli liman alımlarıyla yükselmesi altını baskılıyor. Altının zaten yükselmiş olması ve yeni başlıkların çoğunun fiyatlanmış ya da kısa vadede doğrudan etkisiz görünmesi nedeniyle görünüm hafif
06.11 03:19 N  NEWS (5 new) score +0.02 conf 0.35: Haberler birbiriyle çelişiyor: İran savaşı ve Hormuz patlamaları güvenli liman talebini destekliyor, Polonya'nın altın alımına açık kapı tutumu da olumlu. Buna karşılık doların güçlü kalması, Fed'in şahin duruşu ve Goldman'ın altın tahminlerini düşürmesi baskı yaratıyor; NFP verisi öncesi belirsizlik de yüksek. Net etki nötre yakın olduğu için düşük güven ile hafif pozitif skor veriyorum.
06.11 03:19 N  GPT  score +0.18 conf 0.38: İran savaşı ve Hürmüz Boğazı’na ilişkin belirsizlik güvenli liman talebini destekleyebilir; altın da son haberlerde yükseliş momentumunda. Ancak doların güçlü seyri, Fed’in şahin beklentileri ve yaklaşan istihdam verisi yükselişi sınırlıyor; haberlerin bir kısmı zaten fiyatlanmış olabilir.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
