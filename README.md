# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 10.11.2026 03:59 (İstanbul)

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
| Net kâr/zarar | -55.90 $ | -735.33 $ |
| İşlem sayısı | 1 | 69 |
| Kazanma oranı | %0.0 | %36.2 |
| Ödenen komisyon/spread | 11.82 $ | 818.80 $ |

**Hesap değeri: 4,264.67 $** (başlangıç 5,000 $, -735.33 $ / %-14.71)

Son haber analizi (10.11 03:50): Claude puan **+0.30**, güven 0.45 — Trump'ın İran savaşının askeri olarak "esasen bitti" demesi jeopolitik güvenli liman talebini azaltarak altı hafif olumsuz etkileyebilir; ancak petrol fiyatlarının düşmesi ve ABD enflasyonunun yavaşlayacağı yönündeki haberler faiz indirimi beklentilerini destekleyip dolar zayıfladığı için altı destekliyor. Gold'un zaten yaklaşık %2 yükselmiş olması ve haberlerin çelişkili olması nedeniyle güven sınırlı.

GPT (gpt-6-luna): puan **-0.18**, güven 0.38 — İran savaşının askeri açıdan sona erdiği yönündeki açıklamalar ve Ukrayna görüşmelerindeki ilerleme güvenli liman talebini azaltarak altını baskılayabilir. Ancak ABD enflasyon verisi öncesi bekleyiş ve altındaki önceki yükseliş görünümü belirsizleştiriyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 10.11 03:20 | PAXGUSDT | long | -55.90 $ | stop |
| 09.11 22:29 | PAXGUSDT | short | -55.93 $ | stop |
| 09.11 17:36 | PAXGUSDT | long | -55.90 $ | stop |
| 09.11 14:18 | PAXGUSDT | short | -55.93 $ | stop |
| 09.11 09:20 | PAXGUSDT | long | -55.90 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -55.58 $ |
| İşlem sayısı | 0 | 3 |
| Kazanma oranı | %0.0 | %33.3 |
| Ödenen komisyon/spread | 0.00 $ | 52.30 $ |

**Hesap değeri: 4,944.42 $** (başlangıç 5,000 $, -55.58 $ / %-1.11)

Son haber analizi (09.11 23:06): Claude puan **-0.10**, güven 0.40 — Brent yaklaşık %5 düşüşle 93,5 dolara geriledi; ABD-İran anlaşması umutları ana itici güç ve bu bearish etki kısmen fiyatlandı. Buna karşın Suudi Arabistan'ın Doğu-Batı boru hattına yönelik saldırısı ve Hürmüz Boğazı'ndaki patlama haberleri arz riskini canlı tutuyor, bu nedenle etki çelişkili ve sınırlı.

GPT (gpt-6-luna): puan **-0.18**, güven 0.42 — ABD-İran anlaşması umutlarıyla Brent’in yaklaşık %5 gerilemesi kısa vadede aşağı yönlü momentumu destekliyor. Ancak Hürmüz’de patlama haberleri ve Suudi Arabistan’ın Doğu-Batı petrol hattına yönelik sınırlı saldırı bu düşüşü sınırlayabilecek arz riskleri yaratıyor; haberler çelişkili ve bir kısmı fi

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 22:41 | BZ=F | long | -63.26 $ | stop (gap) |
| 06.11 08:11 | BZ=F | long | -58.75 $ | stop |
| 02.11 23:09 | BZ=F | short | +66.43 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +9437.07 $ |
| İşlem sayısı | 0 | 34 |
| Kazanma oranı | %0.0 | %50.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 111,691.09 $** (başlangıç 100,000 $, +11691.09 $ / %+11.69)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 09.11 23:48 | TSLA | long | +1105.07 $ | seans sonu |
| 09.11 23:48 | SPY | long | +281.01 $ | seans sonu |
| 09.11 23:48 | QQQ | long | +996.60 $ | seans sonu |
| 09.11 21:28 | NVDA | long | -1113.38 $ | stop |
| 09.11 19:06 | NVDA | long | -1115.17 $ | stop |

## Son olaylar

```
10.11 02:38 N  NEWS (12 new) score +0.10 conf 0.30: İran savaşının "esasen bitti" söylemi jeopolitik güvenli liman talebini azaltıp altı baskılayabilir; ancak petrol fiyatlarındaki düşüşün enflasyon endişelerini azaltması faiz beklentileri üzerinden altı destekliyor. Yaklaşan ABD TÜFE verisi nedeniyle net etki belirsiz, bu yüzden sinyal zayıf ve güven düşük.
10.11 02:38 N  GPT  score -0.40 conf 0.66: Trump’ın İran savaşının “fiilen bittiği” yönündeki yeni açıklaması ve Ukrayna’da ilerleme mesajları kısa vadede güvenli liman talebini azaltarak altını baskılayabilir. Petrolün düşmesi enflasyon ve faiz beklentileri üzerinden destek sağlayabilir; bu nedenle aşağı yönlü etki sınırlı ve belirsiz.
10.11 02:50 N  NEWS (4 new) score -0.05 conf 0.35: Trump'ın İran savaşının "esasen bitti" olduğunu söylemesi jeopolitik güvenli liman talebini azaltarak altı hafif baskılıyor. Buna karşılık petrol fiyatlarındaki düşüşün enflasyon endişelerini azaltması ve faiz beklentileri üzerindeki dovish etki altı destekliyor; yaklaşan ABD TÜFE verisi ise yönü belirsiz bırakıyor. Net etki sınırlı ve karışık olduğu için güven düşük.
10.11 02:50 N  GPT  score -0.28 conf 0.48: Trump’ın İran savaşının fiilen sona erdiği yönündeki yeni açıklaması ve Ukrayna’da barışa yönelik ilerleme haberleri, kısa vadede güvenli liman talebini azaltarak altını baskılayabilir. Ancak açıklamalar tekrarlanıyor ve petrol kaynaklı enflasyonun soğuması faiz beklentileri üzerinden altına destek 
10.11 03:02 N  NEWS (9 new) score +0.40 conf 0.50: Trump'ın İran savaşının "esasen bittiğini" söylemesi jeopolitik güvenli liman talebini azaltarak altın için olumsuz, ancak petrol fiyatlarının %4 düşmesi, enflasyon endişelerinin hafiflemesi ve doların zayıflaması faiz indirimi beklentilerini destekleyip altını yukarı itiyor. Net etki hafif pozitif; ancak ABD TÜFE verisi yaklaşırken volatilite yüksek ve haberler çelişkili olduğu için güven orta düzeyde.
10.11 03:02 N  GPT  score -0.12 conf 0.34: İran savaşının askerî açıdan sona yaklaştığı yönündeki açıklamalar güvenli liman talebini azaltabilir; petrolün düşmesi de enflasyon kaygılarını hafifletiyor. Doların gerilemesi altını desteklese de başlıklar çelişkili ve savaşın gerçekten sona erdiği net değil, bu nedenle net etki sınırlı ölçüde ne
10.11 03:14 N  NEWS (18 new) score +0.10 conf 0.35: Trump'ın İran savaşının "askeri olarak fiilen bitti" demesi ve Ukrayna barış görüşmelerindeki ilerleme güvenli liman talebini azaltarak altın için hafif olumsuz. Buna karşın petrol fiyatlarının düşmesi, ABD CPI'ının soğuyacağı beklentisi ve dolarda zayıflama, Fed'in daha yumuşak duruşu ihtimalini artırarak altı hafifçe destekliyor. Çoğu haber eski veya fiyatlanmış olduğu için net bir yön yok.
10.11 03:14 N  GPT  score -0.15 conf 0.36: İran savaşının fiilen sona erebileceği ve Ukrayna görüşmelerindeki esneklik güvenli liman talebini azaltarak altın için hafif negatif. Buna karşılık doların zayıfladığı ve altının yükseldiği haberleri etkiyi sınırlıyor; CPI verisi henüz açıklanmadığından yön konusunda güven düşük.
10.11 03:20 B5  CLOSE long stop: -55.90 USD
10.11 03:26 N  NEWS (8 new) score +0.25 conf 0.40: 
10.11 03:26 N  GPT  score +0.18 conf 0.36: Doların zayıflaması ve altındaki güçlü yükseliş kısa vadede destekleyici; ancak Trump’ın İran savaşının fiilen sona erdiğini söylemesi güvenli liman talebini azaltabilir. İran ve Ukrayna’daki barış haberleri ile enflasyon beklentileri çelişkili olduğundan yön sinyali sınırlı.
10.11 03:38 N  NEWS (6 new) score +0.20 conf 0.40: Trump'ın İran savaşının askeri olarak "esasen bitti" demesi jeopolitik güvenli liman talebini azaltarak altı hafif olumsuz etkileyebilir; ancak petrol fiyatlarının düşmesi ve ABD enflasyonunun yavaşlayacağı yönündeki haberler faiz indirimi beklentilerini destekleyip dolar zayıfladığı için altı destekliyor. Gold'un zaten yaklaşık %2 yükselmiş olması ve haberlerin çelişkili olması nedeniyle güven sınırlı.
10.11 03:38 N  GPT  score -0.20 conf 0.34: İran savaşının askerî açıdan fiilen sona erdiği yönündeki açıklamalar ve Ukrayna görüşmelerindeki esneklik güvenli liman talebini azaltarak altın için hafif negatif. Ancak bunlar doğrulanmış bir ateşkes değil; doların zayıfladığı ve altının yükseldiği haberleri aşağı yönlü etkiyi sınırlıyor.
10.11 03:50 N  NEWS (8 new) score +0.30 conf 0.45: 
10.11 03:50 N  GPT  score -0.18 conf 0.38: İran savaşının askeri açıdan sona erdiği yönündeki açıklamalar ve Ukrayna görüşmelerindeki ilerleme güvenli liman talebini azaltarak altını baskılayabilir. Ancak ABD enflasyon verisi öncesi bekleyiş ve altındaki önceki yükseliş görünümü belirsizleştiriyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
