# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 04.11.2026 04:37 (İstanbul)

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

Son haber analizi (04.11 04:31): Claude puan **-0.40**, güven 0.60 — Altın, dolar ve tahvil getirilerinin yükselmesi, İran ile gerilimin azalması (güvenli liman talebini zayıflatıyor) ve Fed'in enflasyon konusundaki endişeleri nedeniyle 1-4 saat içinde baskı altında görünüyor. Ancak altın zaten bir yılın en düşük seviyesine yakın işlem görüyor, petrol fiyatlarındaki düşüş ve ABD ara seçim sonuçlarının beklenmesi belirsizliği artırdığı için sinyal karışık ve güven orta düzeyde.

GPT (gpt-6-luna): puan **+0.05**, güven 0.32 — Yumuşayan petrol fiyatları altına hafif destek verirken, dolar ve tahvil getirilerindeki yükseliş baskı yaratıyor. İran geriliminin azalması ve çelişkili altın haberleri kısa vadeli yön sinyalini zayıflatıyor.

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
04.11 02:19 N  GPT  score -0.20 conf 0.36: İran ve Ukrayna kaynaklı riskler güvenli liman talebini destekleyebilir; ancak doların ve ABD getirilerinin yükseldiği haberleri kısa vadede altın için daha belirgin baskı oluşturuyor. Yeni başlıkların çoğu fiyatı etkileyecek nitelikte değil ve haber akışı zaten fiyatlanmış olabilir.
04.11 02:30 N  NEWS (4 new) score -0.10 conf 0.30: İran savaşının sürmesi ve Rusya-Ukrayna gerilimi jeopolitik talebi destekliyor, ancak dolar ve ABD tahvil getirilerinin yükselmesi, enflasyonun hızlanması ve altın fiyatlarındaki düşüş haberleri kısa vadede baskı yaratıyor. Genel etki hafif negatif, güven düşük çünkü haberlerin çoğu zaten fiyatlanmış ve karışık.
04.11 02:30 N  GPT  score +0.15 conf 0.38: İran-ABD gerilimi ve İsrail’in olası çatışmaya hazırlığı kısa vadede güvenli liman talebini destekleyebilir; ancak bunlar yeni bir çatışma haberi değil. Dolar ve ABD tahvil getirilerindeki yükseliş altını baskıladığı için net etki sınırlı ve karışık görünüyor.
04.11 02:42 N  NEWS (14 new) score -0.30 conf 0.50: Altın, güçlenen dolar ve yükselen ABD tahvil getirileri nedeniyle 3.950 doların altına geriledi; bu kısa vadede baskı yaratıyor. İran savaşı ve jeopolitik gerilim güvenli liman talebini destekleyici olsa da, piyasa tepkisi şu an dolar ve faiz kanalına odaklı görünüyor. Enflasyonun hızlanma sinyalleri de Fed'in sıkı duruşu beklentisini besleyerek altı olumsuz etkiliyor. Sinyaller karışık olduğu için güven orta düzeyde tutuldu.
04.11 02:42 N  GPT  score -0.38 conf 0.57: Altının 3.950 doların altına gerilemesi ve doların yükselen ABD getirileriyle güçlenmesi kısa vadede aşağı yönlü baskıyı öne çıkarıyor. İran kaynaklı riskler güvenli liman talebini destekleyebilir; ancak haberler çelişkili ve bu risklerin bir kısmı zaten fiyatlanmış olabilir.
04.11 02:54 N  NEWS (13 new) score -0.50 conf 0.60: Altın, güçlenen dolar ve yükselen ABD tahvil getirileri nedeniyle bir yıllık dibe geriledi; enflasyonun hızlanması faiz beklentilerini sertleştirip altın üzerinde baskı yaratıyor. İran savaşı ve Ukrayna haberleri güvenli liman talebini destekliyor olsa da bu etki şimdiden fiyatlanmış görünüyor, bu yüzden genel eğilim 1-4 saat için negatif.
04.11 02:54 N  GPT  score -0.48 conf 0.63: Altın yeni haber akışında sert düşüş ve bir yıllık dip vurgularıyla baskı altında; yükselen dolar ve ABD getirileri kısa vadede aşağı yönü destekliyor. İran ve Ukrayna kaynaklı gerilim güvenli liman talebi yaratabilir, ancak bu etki şimdilik dolar baskısını dengeleyecek kadar güçlü görünmüyor.
04.11 03:06 N  NEWS (13 new) score -0.45 conf 0.60: Altın, güçlenen dolar ve yükselen ABD tahvil getirilerine bağlı olarak bir yıllık dibe geriledi; Trump'ın İran'a karşı yakın vadede saldırı planı olmadığını söylemesi jeopolitik güvenli liman talebini azaltarak baskı yaratıyor. Haberlerin çoğu zaten fiyatlanmış olduğundan ve İran'da yeniden savaş riski hâlâ sürdüğünden güven orta seviyede.
04.11 03:06 N  GPT  score -0.48 conf 0.62: Altın bir yıllık dip seviyeye gerilerken güçlenen dolar ve yükselen ABD getirileri kısa vadede baskıyı artırıyor; ABD’nin İran’a yönelik yakın vadeli saldırı planı olmadığının açıklanması da güvenli liman talebini sınırlayabilir. İran haberleri çelişkili ve hareketin bir kısmı zaten fiyatlanmış olab
04.11 04:07 N  NEWS (28 new) score -0.40 conf 0.50: Altın, güçlenen dolar ve yükselen ABD tahvil getirileri nedeniyle düşüş eğilimindedir; "Gold Slides to a One-Year Low" ve "Gold declines below $3,950" başlıkları bu baskıyı teyit ediyor. İran'la gerilimin gevşemesi jeopolitik güvenli liman talebini azaltarak ek bir baskı yaratıyor, ancak İran savaşının yeniden başlama riski ve sürmekte olan çatışmalar (Ukrayna) yukarı yönlü riski sınırlı da olsa koruyor; ayrıca bazı başlıklar eski veya kısmen fiyatlanmış haberler.
04.11 04:07 N  GPT  score +0.18 conf 0.38: İran görüşmelerindeki karamsarlık ve Ukrayna’ya yönelik saldırılar güvenli liman talebini destekleyebilir; ABD-İran geriliminin hafiflemesi ve son dönemde yükselen dolar ile tahvil getirileri ise altını baskılıyor. Çelişkili sinyaller nedeniyle 1-4 saatlik etki hafif pozitif, ancak belirsiz.
04.11 04:19 N  NEWS (6 new) score -0.45 conf 0.60: Altın bir yıllık dibe yakın seyrediyor; dolar güçleniyor, tahvil getirileri yükseliyor ve İran-ABD gerilimindeki yumuşama güvenli liman talebini azaltıyor. Fed'in enflasyon konusunda endişeli olması da kısa vadede altın için olumsuz bir sinyal; ancak haberlerin çoğu zaten fiyatlanmış olduğundan ve ABD ara seçim sonuçları belirsiz olduğundan güven orta düzeyde.
04.11 04:19 N  GPT  score +0.18 conf 0.34: Altın fiyatının yumuşayan petrol fiyatlarıyla toparlandığı haberi ve Ukrayna’daki yeni saldırılar kısa vadede sınırlı destek sağlayabilir. Ancak Fed’in enflasyon kaygıları ve önceki dolar/getiri kaynaklı düşüş haberleri yönü belirsizleştiriyor; etkilerin bir kısmı önceden fiyatlanmış olabilir.
04.11 04:31 N  NEWS (8 new) score -0.40 conf 0.60: Altın, dolar ve tahvil getirilerinin yükselmesi, İran ile gerilimin azalması (güvenli liman talebini zayıflatıyor) ve Fed'in enflasyon konusundaki endişeleri nedeniyle 1-4 saat içinde baskı altında görünüyor. Ancak altın zaten bir yılın en düşük seviyesine yakın işlem görüyor, petrol fiyatlarındaki düşüş ve ABD ara seçim sonuçlarının beklenmesi belirsizliği artırdığı için sinyal karışık ve güven orta düzeyde.
04.11 04:31 N  GPT  score +0.05 conf 0.32: Yumuşayan petrol fiyatları altına hafif destek verirken, dolar ve tahvil getirilerindeki yükseliş baskı yaratıyor. İran geriliminin azalması ve çelişkili altın haberleri kısa vadeli yön sinyalini zayıflatıyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
