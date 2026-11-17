# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 17.11.2026 16:27 (İstanbul)

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
| Net kâr/zarar | +0.00 $ | -454.74 $ |
| İşlem sayısı | 0 | 113 |
| Kazanma oranı | %0.0 | %41.6 |
| Ödenen komisyon/spread | 0.00 $ | 1342.67 $ |

**Hesap değeri: 4,545.26 $** (başlangıç 5,000 $, -454.74 $ / %-9.09)

Son haber analizi (17.11 16:24): Claude puan **-0.50**, güven 0.60 — Fed yetkilisi Musalem'in "birkaç faiz artırımı" gerekebileceği yönündeki sözleri ve buna bağlı dolar toparlanması altın için baskılayıcı. Jeopolitik gerilim (İran savaşı, Kırım köprüsü saldırısı) güvenli liman talebini destekleyebilir, ancak bu etki hawkish Fed ve güçlenen doların gerisinde kalıyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 13.11 19:25 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 18:39 | PAXGUSDT | short | +69.05 $ | take profit |
| 13.11 17:32 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 16:56 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 16:31 | PAXGUSDT | short | -55.98 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -123.04 $ |
| İşlem sayısı | 0 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 0.00 $ | 70.51 $ |

**Hesap değeri: 4,876.96 $** (başlangıç 5,000 $, -123.04 $ / %-2.46)

Son haber analizi (17.11 08:00): Claude puan **-0.30**, güven 0.50 — Hormuz'daki tanker saldırıları ve mayın isabeti arz riskini artırıp fiyatı destekliyor, ancak piyasa bunu görmezden gelip Goldman'ın 2027'ye kadar büyük arz fazlası öngörüsü, Hormuz sevkiyatlarının iyileşmesi ve dolar güçlenmesi nedeniyle Brent'i 92 doların altına çekti. Haber akışı net olarak fiyatı aşağı çekiyor, ancak jeopolitik risk yüksek olduğundan güven orta düzeyde.

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
| Net kâr/zarar | +0.00 $ | +11832.47 $ |
| İşlem sayısı | 0 | 48 |
| Kazanma oranı | %0.0 | %52.1 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 114,145.15 $** (başlangıç 100,000 $, +14145.15 $ / %+14.15)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 13.11 23:33 | AAPL | long | -1154.98 $ | stop |
| 13.11 20:09 | TSLA | short | -1169.49 $ | stop |
| 13.11 18:11 | QQQ | short | +1751.13 $ | take profit |
| 13.11 17:37 | NVDA | short | +1722.12 $ | take profit |
| 12.11 23:46 | SPY | long | -466.64 $ | seans sonu |

## Son olaylar

```
17.11 14:59 N  NEWS (9 new) score -0.35 conf 0.50: Piyasadaki en önemli sinyal, altının Fed'in art arda faiz artırımı beklentisiyle baskı altında olması ve doların güçlenmesi, bu da altı kısa vadede aşağı yönlü etkiler. Jeopolitik tarafta İran savaşının uzayabileceği yönündeki endişeler güvenli liman talebini destekleyebilir, ancak Vance'in savaşın sonsuz hale gelmeyeceğini söylemesi ve Rusya-Ukrayna barışının "çok yakın" olduğu haberleri bu desteği zayıflatıyor.
17.11 15:11 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 15:11 N  NEWS (14 new) score -0.40 conf 0.50: Altın için baskı ağırlıkta: piyasa art arda Fed faiz artışı bahis yapıyor (şahin beklenti) ve gümüş, doların güçlenmesiyle düşüyor. Trump'ın Rusya-Ukrayna savaşının "çok yakın" olduğu açıklaması güvenli liman talebini zayıflatıyor; İran savaşıyla ilgili jeopolitik haberler ise destek sağlasa da daha az yeni bir tırmanış içermiyor ve zaten fiyatlanmış olabilir.
17.11 15:23 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 15:23 N  NEWS (7 new) score -0.60 conf 0.60: Altın, güçlenen dolar, yüksek enflasyon ve Fed'in art arda faiz artırma beklentisi nedeniyle baskı altında; altın son bir yılın en düşük açılışını yaptı. İran savaşı ve Rusya-Ukrayna haberleri güvenli liman talebini destekleyebilir, ancak bu etki sınırlı kalıyor ve haberler çoğunlukla fiyatlanmış durumda.
17.11 15:35 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 15:35 N  NEWS (7 new) score -0.40 conf 0.50: Altının 17 Kasım'da Eylül 2025'ten bu yana en düşük seviyeden açılması, güçlenen dolar ve yüksek enflasyon başlıkları kısa vadede baskı yaratıyor. İran savaşında "sonsuz savaş olmayacak" açıklaması ise güvenli liman talebini sınırlıyor; ancak bu haberler kısmen fiyatlanmış ve genel jeopolitik gürültü ağırlıklı olduğu için güven orta düzeyde tutuldu.
17.11 15:47 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 15:47 N  NEWS (11 new) score -0.60 conf 0.70: Fed yetkililerinin (Musalem, Hammack) faiz artırımı mesajları, güçlenen dolar ve yüksek enflasyon birlikte altın üzerinde baskı yaratıyor; altın fiyatı 2025 Eylül'den bu yana en düşük seviyeden açıldı. İran savaşının "donmuş çatışmaya" dönüşmesi ve Vance'in savaşın sonsuz olmayacağını söylemesi jeopolitik güvenli liman talebini sınırlıyor; yine de Goldman'ın yüksek hedef tahmini uzun vadeli destek olabilir, bu yüzden güveni sınırlı tutuyorum.
17.11 15:59 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 15:59 N  NEWS (12 new) score -0.60 conf 0.70: Fed'in St. Louis Başkanı Musalem'in 2027 baharına kadar "birkaç faiz artışı" gerekebileceği yönündeki şahin açıklaması, reel faiz ve dolar beklentilerini yukarı çekerek altın için baskı oluşturuyor. Altının 17 Kasım'da Eylül 2025'ten bu yana en düşük seviyeden açılması ve dolar güçlenmesi de bu yönü destekliyor; jeopolitik risk (İran savaşı, Ukrayna/AB yaptırımları) ise "donmuş çatışma" haberleriyle sınırlı kalıp güvenli liman talebini zayıflatıyor.
17.11 16:12 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 16:12 N  NEWS (18 new) score -0.60 conf 0.70: Fed yetkilisi Musalem ve St. Louis Fed başkanı, enflasyon nedeniyle ilkbahara kadar birkaç faiz artırımı gerekebileceğini söyledi; bu da faiz beklentilerini yükseltip doların toparlanmasına yol açtı (FT: dolar 'liberation day' kayıplarını sildi). Altın bu nedenle baskı altında ve Yahoo'ya göre 29 Eylül 2025'ten bu yana en düşük seviyeden açıldı. Kırım köprüsü saldırısı gibi jeopolitik haberler sınırlı bir güvenli liman talebi yaratabilir, ancak baskın etki hawkish Fed ve güçlü dolar yönünde.
17.11 16:24 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 16:24 N  NEWS (12 new) score -0.50 conf 0.60: Fed yetkilisi Musalem'in "birkaç faiz artırımı" gerekebileceği yönündeki sözleri ve buna bağlı dolar toparlanması altın için baskılayıcı. Jeopolitik gerilim (İran savaşı, Kırım köprüsü saldırısı) güvenli liman talebini destekleyebilir, ancak bu etki hawkish Fed ve güçlenen doların gerisinde kalıyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
