# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 17.11.2026 05:27 (İstanbul)

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

Son haber analizi (17.11 05:18): Claude puan **-0.70**, güven 0.70 — Dolar endeksi 19 aylık zirveye yükseldi ve Fed faiz artırımı beklentileri güçleniyor; bu, altın için güçlü bir baskı oluşturuyor. Altın 3.850 doların altına düştü ve yıllık en düşük seviyede; Iran'la ilgili güvenli liman talebini destekleyecek haberler ise yeni değil ve gerilimin azalmasına işaret eden sinyaller içeriyor.

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
17.11 03:53 N  NEWS (10 new) score -0.60 conf 0.70: Güçlenen dolar, Fed faiz artırımı beklentilerinin yükselmesi ve altının 1 yılın en düşüğüne (~3.850$) inmesi altın için net olarak negatif bir tablo çiziyor. Jeopolitik (İran savaşı) riski altına destek verebilse de bu etki şu an dolar ve faiz kanalının gerisinde kalıyor; güven, haberlerin bir kısmının zaten fiyatlanmış olması nedeniyle sınırlı.
17.11 04:05 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 04:05 N  NEWS (16 new) score -0.70 conf 0.70: Altın 1 yılın en düşük seviyesi olan yaklaşık 3.830 dolara geriledi. Güçlenen dolar, Fed faiz artırımı beklentileri ve yükselen tahviller reel faiz baskısını artırarak altını aşağı çekiyor. Ukrayna'daki tırmanış ve Orta Doğu gerilimi güvenli liman talebini destekleyebilir, ancak bu etki şu an hakim olan sıkı para politikası baskısının altında kalıyor.
17.11 04:17 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 04:17 N  NEWS (14 new) score -0.50 conf 0.60: Altın, güçlü doların ve artan Fed faiz artırımı beklentilerinin baskısıyla yaklaşık 3.850 dolarlık bir yıllık dibe geriledi; bu da kısa vadede ağırlıklı olarak negatif bir tablo çiziyor. Savaş ve jeopolitik gerilim haberleri (İran, Ukrayna, Tayvan) güvenli liman talebini destekleyebilse de piyasada bu etki görülmüyor, merkez bankası alımlarına dair Goldman tahmini ise 2027 perspektifli olduğu için kısa vadeli etkisi sınırlı.
17.11 04:29 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 04:29 N  NEWS (17 new) score -0.60 conf 0.70: Güçlü dolar, Fed'in faiz artırım beklentilerinin yükselmesi ve reel faizlerin baskısı altında altın 1 yılın dibine (~3.830$) geriledi; jeopolitik risk (Ukrayna, İran) güvenli liman talebi yaratmadığı için fiyatı destekleyemiyor. Haber akışı kısa vadede baskılı ama yoğun satış sonrası aşırı satım tepkisi riski nedeniyle güven orta.
17.11 04:41 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 04:41 N  NEWS (15 new) score -0.70 conf 0.72: Başlıklar altın için net ayı yönlüdür: altın 1 yılın en düşük seviyesi olan ~3.830-3.850 dolara geriledi, dolar güçleniyor ve Fed'de faiz artırımı beklentileri yükseliyor. Jeopolitik korku kaynaklı güvenli liman talebine dair yeni bir haber yok; Goldman'ın merkez bankası alımı tahmini ise 2027'ye yönelik olduğundan kısa vadeyi etkilemesi zayıf. Fiyatın zaten büyük ölçüde düşmüş olması kısa vadeli tepki riskini artırdığı için güven orta seviyede tutuldu.
17.11 04:54 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 04:54 N  NEWS (21 new) score -0.60 conf 0.70: Fed faiz artırımı beklentileri ve dolar endeksinin 19 ayın zirvesine yükselmesi altın üzerinde güçlü baskı yaratıyor; altın yıllık dip seviyesine (yaklaşık 3.830 dolar) yakın işlem görüyor. Orta Doğu ve Ukrayna'daki çatışma haberleri jeopolitik talep açısından bir miktar destek sunsa da, bu haberler büyük ölçüde fiyatlanmış ve bu güvenli liman etkisini dengeleyemiyor.
17.11 05:06 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 05:06 N  NEWS (18 new) score -0.70 conf 0.80: Dolar 19 aylık zirvede, Fed faiz artırımı beklentileri güçleniyor ve altın yıllık dip seviyelerine (~3.830-3.850$) geriledi; reel faiz ve güçlü dolar baskısı kısa vadede altı aşağı çekiyor. Güvenli liman talebini artıracak bir savaş/kriz haberi yok, bu yüzden düşüş eğilimi sürebilir; ancak aşırı satış sonrası teknik tepki riski nedeniyle güven tam değil.
17.11 05:18 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 05:18 N  NEWS (23 new) score -0.70 conf 0.70: Dolar endeksi 19 aylık zirveye yükseldi ve Fed faiz artırımı beklentileri güçleniyor; bu, altın için güçlü bir baskı oluşturuyor. Altın 3.850 doların altına düştü ve yıllık en düşük seviyede; Iran'la ilgili güvenli liman talebini destekleyecek haberler ise yeni değil ve gerilimin azalmasına işaret eden sinyaller içeriyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
