# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 04.11.2026 01:01 (İstanbul)

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
| Net kâr/zarar | +0.00 $ | -342.75 $ |
| İşlem sayısı | 0 | 24 |
| Kazanma oranı | %0.0 | %33.3 |
| Ödenen komisyon/spread | 0.00 $ | 285.59 $ |

**Hesap değeri: 4,618.78 $** (başlangıç 5,000 $, -381.22 $ / %-7.62)

Açık pozisyonlar: PAXGUSDT short @ 3928.84 (TP 3917.06 / SL 3936.70)

Son haber analizi (04.11 00:55): Claude puan **+0.10**, güven 0.30 — İran savaşı ve müzakere belirsizliği jeopolitik güvenli liman talebini hafif destekliyor; ancak dolar endeksinin yükselişi ve enflasyon kaynaklı faiz beklentilerinin sertleşme ihtimali altın için dengeleyici bir baskı oluşturuyor. Başlıkların çoğu gürültü niteliğinde ve eski/fiyatlanmış haberler olduğu için sinyal zayıf.

GPT (gpt-6-luna): puan **+0.12**, güven 0.32 — İran’la çatışmanın yeniden tırmanabileceğine dair haberler güvenli liman talebini destekleyebilir; ancak yeni ve doğrulanmış bir gelişme yok. Enflasyon ve yükselen mortgage faizleri ile doların güçlenmesi altın üzerindeki baskıyı artırarak görünümü dengeliyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 03.11 23:04 | PAXGUSDT | short | +69.06 $ | take profit |
| 03.11 15:57 | PAXGUSDT | long | +69.03 $ | take profit |
| 03.11 15:26 | PAXGUSDT | short | -55.97 $ | stop |
| 03.11 12:36 | PAXGUSDT | short | -55.97 $ | stop |
| 03.11 06:16 | PAXGUSDT | long | -55.94 $ | stop |

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
03.11 23:45 ERROR B6: Alpaca DELETE /v2/positions/NVDA: 403 {"available":"0","code":40310000,"existing_qty":"484","held_for_orders":"484","message":"insufficient qty available for order (requested: 484, available: 0)","symbol":"NVDA"}
03.11 23:48 B6  CLOSE long QQQ seans sonu: -62.06 USD
03.11 23:48 B6  seans kapanışı: tüm pozisyonlar kapatıldı
03.11 23:51 N  NEWS (10 new) score +0.10 conf 0.35: İran savaşının yeniden başlayabileceğine dair haberler ve İsrail'in kimyasal silah uyarısı altın için hafif yukarı yönlü bir jeopolitik destek sağlıyor. Ancak bu haberlerin somut bir tırmanışa dönüşmediği, ABD tahvil faizlerindeki yükseliş ve Fed'in sıkılaştırma beklentilerinin altını baskılayan eski haberler ise bu desteği dengeliyor; net etki sınırlı ve belirsiz.
03.11 23:51 N  GPT  score +0.12 conf 0.32: İran’la yeniden savaş ihtimali ve Avrupa’daki şüpheli bomba tehditleri kısa vadede güvenli liman talebini destekleyebilir; ancak haberlerin bir kısmı spekülatif ve El-Sayed’in savaşın azaltılması çağrısı bu etkiyi sınırlıyor. Dolar ve yükselen tahvil getirilerinin altın üzerindeki baskısı daha somut
04.11 00:07 N  NEWS (15 new) score +0.10 conf 0.30: Yeni başlıkların çoğu jeopolitik arka plan ya da alakasız haberler; altın için doğrudan yeni bir şok yok. İran savaşının yeniden başlayabileceği ve kimyasal silah iddiaları güvenli liman talebini hafifçe destekliyor, ancak "altın fiyatları yüksek seviyelerden stabilize oluyor" ve ABD doları tarafında ara seçim/NFP beklentisi kaynaklı yükseliş riski altını baskılayabilir; bu nedenle etki sınırlı ve karışık.
04.11 00:07 N  GPT  score +0.18 conf 0.27: İran savaşının yeniden tırmanabileceğine dair haberler ve savaşın Suudi bütçesine etkisi güvenli liman talebini sınırlı ölçüde destekleyebilir. Ancak yeni ve doğrulanmış bir askerî gelişme ya da altın fiyatını kısa vadede yönlendirecek faiz/dolar verisi yok; başlıkların çoğu yorum niteliğinde.
04.11 00:19 N  NEWS (9 new) score +0.20 conf 0.35: İran savaşına ilişkin yeni başlıklar (tam ölçekli çatışma riskinin zirvede olması, Trump'ın yeniden saldırı olasılığı) güvenli liman talebini destekliyor ve altın için hafif pozitif. Ancak dolar endeksinin hafif yükselişi ve savaş haberlerinin büyük bölümünün zaten fiyatlanmış ve karışık olması güveni sınırlıyor.
04.11 00:19 N  GPT  score +0.25 conf 0.43: İran’la görüşmelerin karamsar seyri ve geniş çaplı çatışma riskine ilişkin haberler kısa vadede güvenli liman talebini destekleyebilir. Ancak dolar endeksindeki yükseliş altını baskılıyor; somut yeni bir askerî gelişme olmadığından net etki sınırlı ve belirsiz.
04.11 00:31 N  NEWS (8 new) score +0.20 conf 0.30: İran savaşına ilişkin tırmanma riski ve "tam ölçekli çatışma" uyarıları altın için güvenli liman talebini hafif destekliyor. Ancak dolar endeksinin yükselişi, altının rekor seviyelerden sonra istikrar bulduğuna dair haberler ve Fed bağımsızlığına dair belirsizlik etkiyi sınırlıyor; haber akışı büyük ölçüde tekrarlayan ve fiyatlanmış nitelikte.
04.11 00:31 N  GPT  score +0.20 conf 0.36: İran’la çatışmanın tırmanma riskine ve görüşmelerdeki kötümserliğe dair haberler güvenli liman talebini destekleyebilir. Ancak doların güçlenmesi altının yükselişini sınırlıyor; yeni başlıkların çoğu kısa vadede etkisiz veya doğrudan ilgili değil.
04.11 00:43 N  NEWS (6 new) score +0.12 conf 0.30: İran savaşına ilişkin jeopolitik gerilim (tam ölçekli çatışma riski, son dakika müzakereleri) altın için hafif güvenli liman desteği sağlıyor. Ancak dolar endeksinin yükselmesi ve altının rekor zirvelerden sonra yatay seyretmesi bu etkiyi sınırlıyor; Fed'e dair yeni bir sinyal yok ve haberlerin çoğu gürültü niteliğinde.
04.11 00:43 N  GPT  score +0.15 conf 0.34: İran savaşı ve görüşmelere yönelik kötümserlik güvenli liman talebini destekleyebilir; ancak bunlar büyük ölçüde önceden bilinen gelişmeler ve doların hafif güçlenmesi altını sınırlıyor. Yakın vadede net yön sinyali zayıf, hafif pozitif eğilim beklenebilir.
04.11 00:55 N  NEWS (10 new) score +0.10 conf 0.30: İran savaşı ve müzakere belirsizliği jeopolitik güvenli liman talebini hafif destekliyor; ancak dolar endeksinin yükselişi ve enflasyon kaynaklı faiz beklentilerinin sertleşme ihtimali altın için dengeleyici bir baskı oluşturuyor. Başlıkların çoğu gürültü niteliğinde ve eski/fiyatlanmış haberler olduğu için sinyal zayıf.
04.11 00:55 N  GPT  score +0.12 conf 0.32: İran’la çatışmanın yeniden tırmanabileceğine dair haberler güvenli liman talebini destekleyebilir; ancak yeni ve doğrulanmış bir gelişme yok. Enflasyon ve yükselen mortgage faizleri ile doların güçlenmesi altın üzerindeki baskıyı artırarak görünümü dengeliyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
