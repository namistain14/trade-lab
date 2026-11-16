# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 17.11.2026 00:17 (İstanbul)

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

Son haber analizi (17.11 00:14): Claude puan **-0.60**, güven 0.70 — Sıcak ABD enflasyonu faiz artırımı beklentilerini besliyor, dolar güçleniyor ve altın bir yılın en düşük seviyesine geriledi; bu baskı jeopolitik (İran savaşı) kaynaklı güvenli liman talebinden daha belirleyici görünüyor. Fed'in Hammack'ten gelen sıkılaştırıcı açıklamaları tekrar eden haberler olduğu için etkisi kısmen fiyatlanmış olabilir.

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
16.11 23:00 B6  karar turu: Claude «Teknoloji ağırlıklı ve Nvidia kaynaklı risk-off bir gün kapandı; seans sonrası düşük likidite ve manşet riski nedeniyle yeni pozisyon açmak yerine yarının açılışını beklemek daha disiplinli.» / GPT «-»
16.11 23:13 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
16.11 23:13 N  NEWS (40 new) score -0.60 conf 0.60: Altın 13 aylık ve bir yıllık dip seviyelerinde, güçlenen dolar ve artan Fed faiz artırımı beklentileri nedeniyle baskı altında; bu reel faiz ve dolar kanalı kısa vadede altın için net negatif. Merkez bankası alımları ve Kırım köprüsü saldırısı gibi jeopolitik gelişmeler sınırlı destek sağlasa da fiyatlamaya yetmiyor; birçok başlık tekrar niteliğinde olduğu için güven orta düzeyde.
16.11 23:13 B6  GPT cevap vermedi: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the A
16.11 23:13 B6  karar turu: Claude «Nvidia liderlik krizi ve faiz artışı beklentileriyle teknoloji ağırlıklı sert bir satış günü yaşandı, ancak piyasa kapandığı için yeni intraday pozisyon açmak yerine yarının açılışı beklenmeli.» / GPT «-»
16.11 23:25 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
16.11 23:25 N  NEWS (35 new) score -0.60 conf 0.70: Altın yıllık en düşük seviyeye geriledi; Treasury getirilerindeki yükseliş ve güçlenen dolar baskı yaratıyor. Fed'in Hammack gibi isimlerinin faiz artırımını savunması ve enflasyonun yayılması reel faiz beklentilerini yükselterek altını olumsuz etkiliyor. İran savaşı ve üçüncü/beşinci uçak gemisi haberleri güvenli liman talebini destekliyor, ancak bu etki şu an fiyatlarda görülmüyor.
16.11 23:37 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
16.11 23:37 N  NEWS (31 new) score -0.60 conf 0.70: Fed'in Hammack gibi isimleri faiz artırımı çağrısı yapıyor, dolar 19 aylık zirveye yakın ve ABD tahvil getirileri yükseliyor; bu ortam altın için net olarak negatif. Jeopolitik güvenli liman talebini destekleyecek yeni bir kriz haberi yok. Altın zaten 1 yılın dibinde olduğundan bir kısmı fiyatlanmış olabilir, bu nedenle güveni sınırlı tuttum.
16.11 23:49 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
16.11 23:49 N  NEWS (36 new) score -0.60 conf 0.70: Altın 13 aylık/bir yıllık dip seviyelerine geriledi; güçlü dolar, artan Fed faiz artırımı beklentileri ve "hawkish Fed" görünümü altını baskılıyor. Merkez bankası alımları ve düşük fiyat kaynaklı alım ilgisi kısmen destek olsa da kısa vadede baskı ağır basıyor; savaş/jeopolitik haberler (Kırım köprüsü saldırısı) ise sınırlı güvenli liman etkisi yaratıyor.
17.11 00:02 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 00:02 N  NEWS (38 new) score -0.60 conf 0.70: Sıcak ABD enflasyonu faiz artırımı beklentilerini ve doları güçlendiriyor; Fed'in Hammack'in şahin açıklamaları da altın için olumsuz. İran savaşına dair jeopolitik risk altını destekleyebilir ancak haberler altının yıllık en düşük seviyeye gerilediğini gösteriyor, bu da güvenli liman talebinin şu an baskılanabildiğini gösteriyor.
17.11 00:14 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 00:14 N  NEWS (8 new) score -0.60 conf 0.70: Sıcak ABD enflasyonu faiz artırımı beklentilerini besliyor, dolar güçleniyor ve altın bir yılın en düşük seviyesine geriledi; bu baskı jeopolitik (İran savaşı) kaynaklı güvenli liman talebinden daha belirleyici görünüyor. Fed'in Hammack'ten gelen sıkılaştırıcı açıklamaları tekrar eden haberler olduğu için etkisi kısmen fiyatlanmış olabilir.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
