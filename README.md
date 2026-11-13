# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 13.11.2026 06:30 (İstanbul)

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
| Net kâr/zarar | -55.98 $ | -331.66 $ |
| İşlem sayısı | 1 | 102 |
| Kazanma oranı | %0.0 | %42.2 |
| Ödenen komisyon/spread | 11.94 $ | 1211.39 $ |

**Hesap değeri: 4,668.34 $** (başlangıç 5,000 $, -331.66 $ / %-6.63)

Son haber analizi (13.11 06:29): Claude puan **-0.30**, güven 0.45 — Dolar 19 aylık zirvesinde ve Fed faiz artırım beklentileri yükselirken ABD tahvil getirileri de artıyor; bu, altın için baskı oluşturuyor. Öte yandan İran'ın ABD radar üssünü hedef aldığı haberi jeopolitik risk kaynaklı güvenli liman talebini destekleyebilir, ancak haberler çelişkili (dolar düşüşü haberi, savaş haberleri) ve altın 3 günde yaklaşık %6 düştükten sonra stabilize oluyor, bu yüzden güven düşük.

GPT (gpt-6-luna): puan **+0.15**, güven 0.36 — İran’ın Bahreyn’deki ABD radar tesisini hedef aldığını açıklaması kısa vadeli güvenli liman talebini artırabilir. Ancak güçlü dolar ve yükselen ABD tahvil getirileri altını baskılıyor; genel etki sınırlı ve belirsiz görünüyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 13.11 03:05 | PAXGUSDT | short | -55.98 $ | stop |
| 12.11 21:37 | PAXGUSDT | short | -56.18 $ | stop (gap) |
| 12.11 19:56 | PAXGUSDT | short | -55.98 $ | stop |
| 12.11 19:06 | PAXGUSDT | short | -55.98 $ | stop |
| 12.11 18:46 | PAXGUSDT | short | -55.98 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -123.04 $ |
| İşlem sayısı | 0 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 0.00 $ | 70.51 $ |

**Hesap değeri: 4,876.96 $** (başlangıç 5,000 $, -123.04 $ / %-2.46)

Son haber analizi (12.11 07:59): Claude puan **-0.15**, güven 0.40 — Başlıklar karışık: ABD-İran barış görüşmesi umutları, Brent'in 92 doların altına inmesi ve Suudi üretim artışı fiyatı aşağı çekiyor, ancak Hormuz'da mayına çarpan tanker, İran'ın misilleme tehditleri ve barış görüşmelerinin tıkanması ciddi bir yukarı risk oluşturuyor. Bu çelişkiler ve bazı haberlerin eski veya zaten fiyatlanmış olması nedeniyle yön sinyali zayıf ve güven düşük.

GPT (gpt-6-luna): puan **-0.35**, güven 0.56 — Barış görüşmesi umutları, Suudi üretimindeki artış ve OPEC+ ihracatının savaş öncesi seviyelere yaklaşması yakın vadede arz endişelerini azaltıp Brent üzerinde baskı kuruyor. Hürmüz’deki mayın/tanker haberleri ve İran’ın misilleme tehdidi düşüşü sınırlıyor; haber akışının bir kısmı doğrulanmamış vey

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
| Net kâr/zarar | +0.00 $ | +10683.69 $ |
| İşlem sayısı | 0 | 44 |
| Kazanma oranı | %0.0 | %52.3 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 113,945.80 $** (başlangıç 100,000 $, +13945.80 $ / %+13.95)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 12.11 23:46 | SPY | long | -466.64 $ | seans sonu |
| 12.11 23:46 | QQQ | long | +93.52 $ | seans sonu |
| 12.11 23:21 | TSLA | long | +774.55 $ | take profit |
| 12.11 21:50 | NVDA | long | -834.20 $ | stop |
| 12.11 20:38 | AAPL | long | -1155.20 $ | stop |

## Son olaylar

```
13.11 05:05 N  GPT  score -0.62 conf 0.68: Doların 19 ayın zirvesine yaklaşması, yükselen ABD tahvil getirileri ve Fed’in daha sıkı politika beklentileri altın üzerinde belirgin kısa vadeli baskı yaratıyor. Ukrayna görüşmeleri güvenli liman talebini sınırlayabilir; ancak haberlerin önemli bir kısmı mevcut düşüşü zaten yansıtıyor ve jeopoliti
13.11 05:17 N  NEWS (10 new) score -0.60 conf 0.70: Haberlerin ağırlığı şahin Fed beklentilerine ve güçlenen dolara işaret ediyor: dolar 19 aylık zirveye yakın, faiz artırımı bahisleri yükseliyor ve altın 13 aylık dibe yakın seyrediyor. İran savaşı ve Ukrayna görüşmeleri gibi jeopolitik gelişmeler sınırlı güvenli liman talebi yaratıyor ama reel faiz ve dolar etkisini dengeleyemiyor; ayrıca bazı başlıklar eski veya tekrar eden nitelikte olduğu için güven orta düzeyde tutuldu.
13.11 05:17 N  GPT  score -0.68 conf 0.75: Fed’in enflasyon konusunda hawkish mesajları ve faiz artışı beklentileri doları 19 ayın zirvesine taşırken yükselen getiriler altın üzerinde belirgin baskı yaratıyor. İran savaşıyla ilgili belirsizlik güvenli liman talebini destekleyebilir, ancak kısa vadede dolar ve faiz etkisinin ağır basması olas
13.11 05:29 N  NEWS (8 new) score -0.60 conf 0.70: Güçlü dolar (19 aylık zirve), Fed faiz artırımı beklentilerinin yükselmesi ve 96 dolarlık petrol enflasyon endişelerini artırarak altı baskılıyor; altın 13 aylık dip yakınında. İran savaşı ve jeopolitik risk safe-haven talebini sınırlı destekliyor ancak baskın etki negatif.
13.11 05:29 N  GPT  score -0.55 conf 0.68: Güçlü dolar, yükselen tahvil getirileri ve Fed’in faiz artıracağı beklentisi altın üzerinde baskı yaratıyor. İran ve Rusya-Ukrayna savaşlarını sona erdirme çabaları güvenli liman talebini de sınırlayabilir; ancak bu gelişmelerin bir kısmı zaten fiyatlanmış olabilir.
13.11 05:41 N  NEWS (16 new) score -0.65 conf 0.60: Dolar 19 aylık zirvesine yakın ve Fed faiz artırımı beklentileri yükseliyor; petrol 96 dolar civarında enflasyon kaygısını besliyor. Altın 3.900 doların altına inip 13 aylık dibe yakın işlem görüyor. Trump'ın İran anlaşmasına gerek olmadığı yönündeki açıklaması jeopolitik güvenli liman talebini zayıflatıyor. Bekleyen ABD PPI verisi kısa vadede sürpriz yaratabileceğinden güven orta düzeyde tutuldu.
13.11 05:41 N  GPT  score -0.70 conf 0.78: Doların 19 ayın zirvesine çıkması, ABD tahvil getirileri ve Fed faiz artırımı beklentilerinin güçlenmesi altını önümüzdeki saatlerde baskılıyor; fiyatın 3.900 doların altına gerilemesi de bu görünümü destekliyor. İran kaynaklı jeopolitik risk ve dipten toparlanma olasılığı düşüşü sınırlayabilir.
13.11 05:53 N  NEWS (7 new) score -0.60 conf 0.60: Faiz artışı beklentileri nedeniyle dolar 19 ayın zirvesine yakın seyrediyor ve altın 3.900 doların altına düştü; bu, altın için belirgin bir baskı. Trump'ın İran anlaşmasına ihtiyaç duyulmadığını söylemesi jeopolitik risk primini sınırlıyor, ancak İran savaşının sürmesi güvenli liman talebini tamamen silmiyor. Yakın vadede ABD PPI verisi ana belirleyici olacak; sıcak bir enflasyon sürprizi baskıyı artırır, yumuşak veri ise tepkiyi tersine çevirebilir.
13.11 05:53 N  GPT  score -0.68 conf 0.76: Doların 19 ayın zirvesine yaklaşması ve Fed faiz artırımı beklentilerinin güçlenmesi altın üzerinde belirgin baskı yaratıyor. İran ve Ukrayna başlıklarının piyasa yorumu kısmen belirsiz olsa da, altındaki sert düşüş ve PPI öncesi temkin kısa vadeli görünümü aşağı yönlü kılıyor.
13.11 06:06 N  NEWS (6 new) score +0.40 conf 0.50: Yeni gelen en önemli haber, ABD doları düşerken altın ve gümüşün yükseldiğini bildiriyor; bu, altın için kısa vadede olumlu bir sinyal. Ancak daha eski haberler doların 19 aylık zirvede olduğunu ve Fed faiz artırımı beklentilerinin güçlendiğini gösteriyor, bu da altına baskı yapabilir; bu nedenle güven orta düzeyde tutuldu.
13.11 06:06 N  GPT  score +0.15 conf 0.34: En yeni başlıkta doların gerilemesiyle altın ve gümüşün yükseldiği belirtiliyor; bu kısa vadede altını destekleyebilir. Ancak doların 19 ayın zirvesine yakın olduğu, faiz artışı beklentilerinin güçlendiği ve altının yakın zamanda sert düştüğü yönündeki çelişkili haberler etkiyi sınırlıyor.
13.11 06:18 N  NEWS (5 new) score -0.25 conf 0.40: Dolar 19 aylık zirvede ve Fed faiz artırımı beklentileri güçleniyor; bu, altın için net olarak baskı yaratıyor. Ukrayna barış görüşmelerinde Avrupa'nın dahil edilmesi ve Trump'ın İran anlaşmasına ihtiyaç olmadığını söylemesi güvenli liman talebini azaltıyor. Buna karşılık, eski ve kısmen fiyatlanmış haberler ile ABD PPI verisinin belirsizliği nedeniyle güven sınırlı kalıyor.
13.11 06:18 N  GPT  score -0.66 conf 0.72: Doların 19 ayın zirvesine yaklaşması, yükselen tahvil getirileri ve Fed faiz artırımı beklentileri altın üzerinde belirgin baskı yaratıyor; fiyatın 3.900 doların altına gerilemesi de bu görünümü destekliyor. İran anlaşmasına ihtiyaç olmadığı açıklaması ve Ukrayna’da barış/prisoner exchange girişimle
13.11 06:29 N  NEWS (5 new) score -0.30 conf 0.45: Dolar 19 aylık zirvesinde ve Fed faiz artırım beklentileri yükselirken ABD tahvil getirileri de artıyor; bu, altın için baskı oluşturuyor. Öte yandan İran'ın ABD radar üssünü hedef aldığı haberi jeopolitik risk kaynaklı güvenli liman talebini destekleyebilir, ancak haberler çelişkili (dolar düşüşü haberi, savaş haberleri) ve altın 3 günde yaklaşık %6 düştükten sonra stabilize oluyor, bu yüzden güven düşük.
13.11 06:29 N  GPT  score +0.15 conf 0.36: İran’ın Bahreyn’deki ABD radar tesisini hedef aldığını açıklaması kısa vadeli güvenli liman talebini artırabilir. Ancak güçlü dolar ve yükselen ABD tahvil getirileri altını baskılıyor; genel etki sınırlı ve belirsiz görünüyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
