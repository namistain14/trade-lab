# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 12.11.2026 07:53 (İstanbul)

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
| Net kâr/zarar | -42.83 $ | -212.29 $ |
| İşlem sayısı | 3 | 82 |
| Kazanma oranı | %33.3 | %42.7 |
| Ödenen komisyon/spread | 35.66 $ | 973.00 $ |

**Hesap değeri: 4,814.84 $** (başlangıç 5,000 $, -185.16 $ / %-3.70)

Açık pozisyonlar: PAXGUSDT short @ 3975.48 (TP 3963.56 / SL 3983.44)

Son haber analizi (12.11 07:50): Claude puan **-0.60**, güven 0.70 — Dolar 19 aylık zirvesine yükseldi ve Fed'in faiz artırımı beklentileri güçleniyor; bu, altın için net bir baskı unsuru. Jeopolitik (İran-İsrail gerilimi) ise güvenli liman talebi yaratıyor, ancak mevcut haber akışında dolar ve faiz etkisi baskın görünüyor.

GPT (gpt-6-luna): puan **-0.58**, güven 0.68 — Güçlenen dolar ve Fed’in daha şahin olacağı beklentileri altını baskılıyor; fiyatların sert düşüşü de kısa vadeli görünümü zayıflatıyor. İran kaynaklı gerilim güvenli liman talebi yaratabilir, ancak bu etki mevcut baskıyı şimdilik dengelemiyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 12.11 03:48 | PAXGUSDT | short | -55.95 $ | stop |
| 12.11 03:21 | PAXGUSDT | short | -55.95 $ | stop |
| 12.11 03:01 | PAXGUSDT | short | +69.07 $ | take profit |
| 11.11 21:04 | PAXGUSDT | short | +69.08 $ | take profit |
| 11.11 20:25 | PAXGUSDT | short | -55.95 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -123.04 $ |
| İşlem sayısı | 0 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 0.00 $ | 70.51 $ |

**Hesap değeri: 4,876.96 $** (başlangıç 5,000 $, -123.04 $ / %-2.46)

Son haber analizi (10.11 07:59): Claude puan **-0.25**, güven 0.50 — Trump'ın İran savaşının askeri olarak bittiğini söylemesi ve Brent'in %6,7 düşüp 91,70 dolara gerilemesi, barış beklentileri nedeniyle kısa vadede baskı yaratıyor. Ancak Hormuz'daki gemi saldırıları, Husilerin Suudi boru hattına yönelik saldırıları ve Çin'in ham petrol ithalatının artması arz riskini canlı tutuyor; bu çelişkili haberler güveni sınırlıyor.

GPT (gpt-6-luna): puan **-0.55**, güven 0.68 — İran savaşının askerî olarak sona erdiği açıklaması, saldırı risklerinin azaldığına dair haberler ve Brent’in %6,73 düşmesi kısa vadede güçlü aşağı yönlü baskıya işaret ediyor. Suudi petrol boru hattına yönelik saldırı ve Hürmüz’deki gemi iddiaları arz riskini canlı tutsa da haberler çelişkili ve dü

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
| Net kâr/zarar | +0.00 $ | +12271.66 $ |
| İşlem sayısı | 0 | 39 |
| Kazanma oranı | %0.0 | %53.8 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 115,261.43 $** (başlangıç 100,000 $, +15261.43 $ / %+15.26)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 11.11 23:45 | SPY | long | +21.86 $ | seans sonu |
| 11.11 23:45 | QQQ | long | +339.47 $ | seans sonu |
| 11.11 23:45 | NVDA | long | -45.71 $ | seans sonu |
| 11.11 23:45 | AAPL | long | +805.80 $ | seans sonu |
| 11.11 17:47 | NVDA | short | +1713.17 $ | take profit |

## Son olaylar

```
12.11 06:25 N  GPT  score -0.58 conf 0.67: Fed’in daha fazla faiz artıracağı beklentisi ve doların güçlenmesi, kısa vadede altın üzerinde baskı yaratıyor; yeni başlıklar da dolar yükselirken altının desteği test ettiğini gösteriyor. PBOC kaynaklı dolar geri çekilmesi sınırlı bir karşı unsur, ancak belirgin yeni bir güvenli liman katalizörü y
12.11 06:38 N  NEWS (5 new) score -0.60 conf 0.70: Güçlü dolar (19 aylık zirve), Fed'in faiz artırımı beklentilerinin yükselmesi ve enflasyon kaygıları altını 4.000 doların altına itti; yeni haberler ve 12 günlük dip ile tutarlı bir baskı görülüyor. Savaş haberleri (İran) güvenli liman talebini destekleyebilir ancak mevcut piyasada bu etki baskın değil.
12.11 06:38 N  GPT  score -0.75 conf 0.81: Doların 19 ayın zirvesine yükselmesi ve Fed’in daha büyük faiz artışı beklentilerinin güçlenmesi, getirisi olmayan altın üzerinde belirgin baskı yaratıyor; altının 12 günlük düşük seviyeye gerilemesi bu görünümü destekliyor. Doların kısa süreli geri çekildiğine dair haberler aşağı yönlü etkiyi bir m
12.11 06:50 N  NEWS (7 new) score -0.60 conf 0.70: Fed faiz artırımı beklentilerinin yükselmesi, güçlü dolar ve enflasyon kaynaklı baskı altçizilmiş altın fiyatı (4.000 doların altında) kısa vadede düşüş yönlü baskı altında. Savaş/jeopolitik haberleri (İran, Ukrayna barış görüşmeleri) güvenli liman talebini sınırlı destekliyor; bu nedenle genel etki negatif, ancak eski haberlerin çoğu zaten fiyatlanmış.
12.11 06:50 N  GPT  score -0.68 conf 0.78: Doların güçlenmesi ve daha şahin Fed faiz beklentileri altın üzerinde kısa vadeli baskı oluşturuyor; yeni başlıklarda güvenli liman talebini belirgin biçimde artıracak bir gelişme yok. Haberlerin çoğu aynı fiyat hareketini ve beklentileri tekrarladığı için düşüş yönündeki sinyal güçlü, ancak ek teyi
12.11 07:02 N  NEWS (12 new) score -0.70 conf 0.70: ABD enflasyon verisinin ardından Fed faiz artırımı beklentileri yükseldi ve dolar 19 aylık zirvesine çıktı; bu, altın için 1-4 saatlik görünümde güçlü bir baskı oluşturuyor. Savaş kaynaklı güvenli liman talebine dair yeni bir gelişme ise öne çıkmadığı için bu baskıyı dengeleyecek bir unsur zayıf.
12.11 07:02 N  GPT  score -0.68 conf 0.73: Doların 19 ayın zirvesine çıkması ve güçlü ABD enflasyonu sonrası Fed faiz artırımı beklentilerinin yükselmesi, önümüzdeki saatlerde altın üzerinde belirgin baskı yaratıyor. PPI öncesi belirsizlik ve bazı jeopolitik başlıklar düşüşü sınırlayabilir; ancak yeni bir tırmanış sinyali yok.
12.11 07:14 N  NEWS (8 new) score -0.60 conf 0.70: Dolar 19 aylık zirvesine çıkarken Fed faiz artırımı beklentileri güçleniyor; bu, reel faizler ve güçlü dolar nedeniyle altın için net olarak baskı yaratıyor. Ayrıca petrol, İran ve Ukrayna barış görüşmeleri umuduyla düşüyor, bu da jeopolitik güvenli liman talebini zayıflatıyor. Altın zaten haftalık en düşük seviyeye gerilemiş durumda; yine de PPI verisi ve yen müdahalesi riski kısa vadede oynaklık yaratabilir.
12.11 07:14 N  GPT  score -0.55 conf 0.68: Doların 19 ayın zirvesine çıkması ve Fed faiz artırımı beklentilerinin güçlenmesi, kısa vadede altın üzerinde belirgin baskı yaratıyor. İran’ın misilleme söylemi güvenli liman talebini destekleyebilir; ancak petrolün barış görüşmeleri umuduyla gerilemesi bu desteği sınırlıyor.
12.11 07:26 N  NEWS (7 new) score -0.60 conf 0.60: Dolar 19 aylık zirvesine çıkarken Fed faiz artırımı beklentileri güçleniyor ve altın bir haftanın en düşük seviyesine geriledi; bu, altın için net bir baskı sinyali. İran savaşı ve Orta Doğu gerilimi güvenli liman talebini destekleyebilir, ancak petrol fiyatlarının barış umutlarıyla düşmesi bu etkiyi zayıflatıyor. Yakın vadede PPI verisi ve dolar hareketi belirleyici olacak; bu nedenle güven orta düzeyde.
12.11 07:26 N  GPT  score -0.55 conf 0.72: Doların 19 ayın zirvesine çıkması ve Fed faiz artırımı beklentilerinin güçlenmesi, altındaki düşüşü kısa vadede destekliyor. İran’dan misilleme tehdidi ve Gazze’deki saldırı güvenli liman talebini artırabilir; bu nedenle düşüş görünümü kesin değil.
12.11 07:38 N  NEWS (6 new) score -0.40 conf 0.60: Doların 19 aylık zirveye yükselmesi ve Fed faiz artırımı beklentilerinin güçlenmesi altın için baskı oluşturuyor; altın bir haftanın en düşük seviyesine geriledi. İran–İsrail gerilimi jeopolitik güvenli liman talebini destekliyor ancak barış görüşmesi umutları ve petrol fiyatlarındaki düşüş bu etkiyi sınırlıyor.
12.11 07:38 N  GPT  score -0.35 conf 0.68: Güçlenen dolar ve artan Fed faiz artırımı beklentileri altın üzerinde kısa vadede baskın; altının haftanın en düşük seviyelerine gerilemesi bu görünümü destekliyor. İran’ın genişletilmiş misilleme uyarısı güvenli liman talebini artırabilir, ancak haber akışı çelişkili olduğundan düşüş beklentisinin 
12.11 07:50 N  NEWS (9 new) score -0.60 conf 0.70: Dolar 19 aylık zirvesine yükseldi ve Fed'in faiz artırımı beklentileri güçleniyor; bu, altın için net bir baskı unsuru. Jeopolitik (İran-İsrail gerilimi) ise güvenli liman talebi yaratıyor, ancak mevcut haber akışında dolar ve faiz etkisi baskın görünüyor.
12.11 07:50 N  GPT  score -0.58 conf 0.68: Güçlenen dolar ve Fed’in daha şahin olacağı beklentileri altını baskılıyor; fiyatların sert düşüşü de kısa vadeli görünümü zayıflatıyor. İran kaynaklı gerilim güvenli liman talebi yaratabilir, ancak bu etki mevcut baskıyı şimdilik dengelemiyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
