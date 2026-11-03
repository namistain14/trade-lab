# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 04.11.2026 02:50 (İstanbul)

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
| Net kâr/zarar | -55.96 $ | -398.72 $ |
| İşlem sayısı | 1 | 25 |
| Kazanma oranı | %0.0 | %32.0 |
| Ödenen komisyon/spread | 11.91 $ | 297.50 $ |

**Hesap değeri: 4,601.28 $** (başlangıç 5,000 $, -398.72 $ / %-7.97)

Son haber analizi (04.11 02:42): Claude puan **-0.30**, güven 0.50 — Altın, güçlenen dolar ve yükselen ABD tahvil getirileri nedeniyle 3.950 doların altına geriledi; bu kısa vadede baskı yaratıyor. İran savaşı ve jeopolitik gerilim güvenli liman talebini destekleyici olsa da, piyasa tepkisi şu an dolar ve faiz kanalına odaklı görünüyor. Enflasyonun hızlanma sinyalleri de Fed'in sıkı duruşu beklentisini besleyerek altı olumsuz etkiliyor. Sinyaller karışık olduğu için güven orta düzeyde tutuldu.

GPT (gpt-6-luna): puan **-0.38**, güven 0.57 — Altının 3.950 doların altına gerilemesi ve doların yükselen ABD getirileriyle güçlenmesi kısa vadede aşağı yönlü baskıyı öne çıkarıyor. İran kaynaklı riskler güvenli liman talebini destekleyebilir; ancak haberler çelişkili ve bu risklerin bir kısmı zaten fiyatlanmış olabilir.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 04.11 01:49 | PAXGUSDT | short | -55.96 $ | stop |
| 03.11 23:04 | PAXGUSDT | short | +69.06 $ | take profit |
| 03.11 15:57 | PAXGUSDT | long | +69.03 $ | take profit |
| 03.11 15:26 | PAXGUSDT | short | -55.97 $ | stop |
| 03.11 12:36 | PAXGUSDT | short | -55.97 $ | stop |

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
| Net kâr/zarar | +0.00 $ | -167.93 $ |
| İşlem sayısı | 0 | 6 |
| Kazanma oranı | %0.0 | %16.7 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 102,500.90 $** (başlangıç 100,000 $, +2500.90 $ / %+2.50)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 03.11 23:48 | QQQ | long | -62.06 $ | seans sonu |
| 03.11 18:34 | AAPL | long | -859.05 $ | stop |
| 02.11 23:51 | TSLA | long | -1109.17 $ | seans sonu |
| 02.11 23:48 | NVDA | short | +5136.86 $ | seans sonu |
| 02.11 23:45 | AAPL | long | -3118.15 $ | seans sonu |

## Son olaylar

```
04.11 01:31 N  NEWS (8 new) score -0.15 conf 0.40: İran savaşına dair jeopolitik risk (tam ölçekli çatışma ihtimali, son dakika müzakereleri) altın için güvenli liman talebini destekliyor. Ancak "Dolar ABD tahvil getirileriyle birlikte yükseliyor" başlığı ve enflasyon ivmelenmesi, Fed'in sıkı kalabileceği beklentisini artırarak altın üzerinde baskı yaratıyor. Haberler karışık ve bir kısmı zaten fiyatlanmış olduğu için güven düşük.
04.11 01:31 N  GPT  score -0.15 conf 0.38: İran geriliminin tırmanma riski güvenli liman talebini destekleyebilir; ancak doların ABD tahvil getirileriyle birlikte yükselmesi kısa vadede altın üzerinde baskı oluşturuyor. Haberler çelişkili ve yeni fiyat etkisinin yönü belirsiz olduğundan görünüm hafif negatif.
04.11 01:43 N  NEWS (16 new) score -0.20 conf 0.40: Dolar ve ABD tahvil getirilerinin yükselmesi, enflasyonun hızlanmasına dair haberler ve FXEmpire'ın altının düşüş riskine dikkat çeken teknik yorumu altın için kısa vadede baskı yaratıyor. İran savaşı ve nükleer gerilim gibi güvenli liman talebini artıran unsurlar ise bu baskıyı kısmen dengeliyor; haberler karışık olduğu için güven düşük tutuldu.
04.11 01:43 N  GPT  score -0.20 conf 0.35: Doların ve ABD getirilerinin güçlenmesi ile altındaki aşağı yönlü teknik risk kısa vadede baskı yaratıyor. İran ve Ukrayna kaynaklı gerilim güvenli liman talebini desteklese de haberler karışık ve bir kısmı zaten fiyatlanmış olabilir.
04.11 01:49 B5  CLOSE short stop: -55.96 USD
04.11 01:55 N  NEWS (16 new) score +0.08 conf 0.30: İran'da ABD saldırılarının sürmesi ve Rusya'nın Ukrayna'ya enerji altyapısına yönelik büyük saldırısı güvenli liman talebini hafifçe destekliyor. Ancak dolar ve ABD tahvil getirilerinin yükselmesi, enflasyon kaynaklı faiz baskısı ve ABD ara seçim endişeleri altını baskılıyor. Gündemdeki birçok başlık da spor ve tarih haberi olduğundan sinyal zayıf, bu yüzden güven düşük.
04.11 01:55 N  GPT  score +0.18 conf 0.34: Ukrayna enerji şebekesine yönelik büyük saldırı ve İran’daki çatışmaların sürdüğüne dair haberler kısa vadeli güvenli liman talebini destekleyebilir. Ancak doların ve ABD tahvil getirilerinin yükselmesi altını baskılıyor; haberlerin bir kısmı tekrarlı veya belirsiz olduğundan net etki sınırlı.
04.11 02:07 N  NEWS (5 new) score -0.12 conf 0.40: İran savaşının yeniden alevlenme riski jeopolitik talebi destekliyor, ancak dolar ve ABD tahvil getirilerindeki yükseliş ile enflasyonun hızlanması (hawkish beklentiler) altın üzerinde baskı yaratıyor. Altın teknik analizlerde düşüş riski uyarısı alıyor ve haberler karışık olduğu için sinyal zayıf.
04.11 02:07 N  GPT  score -0.15 conf 0.36: İran çevresindeki çatışma riski güvenli liman talebini destekleyebilir; ancak doların ve ABD tahvil getirilerinin yükselmesi ile altındaki düşüş haberi kısa vadede baskın görünüyor. Başlıkların çoğu yeni veya doğrudan fiyatı etkileyen bir gelişme değil, bu yüzden yön sinyali zayıf.
04.11 02:19 N  NEWS (4 new) score -0.15 conf 0.40: İran'daki çatışmanın sürmesi ve yeniden savaş riski güvenli liman talebi açısından altını destekliyor. Ancak dolar ve ABD tahvil getirilerinin yükselmesi, enflasyonun hızlanma sinyalleri ve altın fiyatındaki "düşüş/geri dönüş" başlıkları baskıyı artırıyor. Haberler karışık ve büyük ölçüde fiyatlanmış olduğu için sinyal zayıf.
04.11 02:19 N  GPT  score -0.20 conf 0.36: İran ve Ukrayna kaynaklı riskler güvenli liman talebini destekleyebilir; ancak doların ve ABD getirilerinin yükseldiği haberleri kısa vadede altın için daha belirgin baskı oluşturuyor. Yeni başlıkların çoğu fiyatı etkileyecek nitelikte değil ve haber akışı zaten fiyatlanmış olabilir.
04.11 02:30 N  NEWS (4 new) score -0.10 conf 0.30: İran savaşının sürmesi ve Rusya-Ukrayna gerilimi jeopolitik talebi destekliyor, ancak dolar ve ABD tahvil getirilerinin yükselmesi, enflasyonun hızlanması ve altın fiyatlarındaki düşüş haberleri kısa vadede baskı yaratıyor. Genel etki hafif negatif, güven düşük çünkü haberlerin çoğu zaten fiyatlanmış ve karışık.
04.11 02:30 N  GPT  score +0.15 conf 0.38: İran-ABD gerilimi ve İsrail’in olası çatışmaya hazırlığı kısa vadede güvenli liman talebini destekleyebilir; ancak bunlar yeni bir çatışma haberi değil. Dolar ve ABD tahvil getirilerindeki yükseliş altını baskıladığı için net etki sınırlı ve karışık görünüyor.
04.11 02:42 N  NEWS (14 new) score -0.30 conf 0.50: Altın, güçlenen dolar ve yükselen ABD tahvil getirileri nedeniyle 3.950 doların altına geriledi; bu kısa vadede baskı yaratıyor. İran savaşı ve jeopolitik gerilim güvenli liman talebini destekleyici olsa da, piyasa tepkisi şu an dolar ve faiz kanalına odaklı görünüyor. Enflasyonun hızlanma sinyalleri de Fed'in sıkı duruşu beklentisini besleyerek altı olumsuz etkiliyor. Sinyaller karışık olduğu için güven orta düzeyde tutuldu.
04.11 02:42 N  GPT  score -0.38 conf 0.57: Altının 3.950 doların altına gerilemesi ve doların yükselen ABD getirileriyle güçlenmesi kısa vadede aşağı yönlü baskıyı öne çıkarıyor. İran kaynaklı riskler güvenli liman talebini destekleyebilir; ancak haberler çelişkili ve bu risklerin bir kısmı zaten fiyatlanmış olabilir.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
