# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 17.11.2026 10:19 (İstanbul)

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

Son haber analizi (17.11 10:19): Claude puan **-0.70**, güven 0.75 — Altın 1 yıllık dibe yakın seyrediyor; dolar 19 aylık zirvede ve Fed faiz artırımı beklentileri artıyor, bu da reel faizleri ve doları yukarı iterek altın için güçlü bir baskı oluşturuyor. İran savaşı ve Hürmüz'deki saldırılar güvenli liman talebini destekleyebilse de, bu etki Fed sıkılaştırma beklentilerinin gerisinde kalıyor.

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
17.11 08:54 N  NEWS (3 new) score -0.50 conf 0.60: Altın, güçlü dolar ve Fed faiz artırımı beklentileri nedeniyle yaklaşık bir yıllık dibe yakın seyrediyor; yeni haberlerde ABD'nin İran'da "sonsuz savaş" ihtimalini reddetmesi ve petrolün düşmesi jeopolitik güvenli liman talebini zayıflatıyor. Ukrayna ve İran'daki çatışma haberleri ise büyük ölçüde fiyatlanmış durumda olduğundan etkisi sınırlı kalabilir.
17.11 09:06 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 09:06 N  NEWS (18 new) score -0.40 conf 0.60: Faiz artırımı beklentileri ve güçlenen dolar altın için baskılayıcı; Warsh'ın inflasyon nedeniyle faiz artırımına yaklaştığına dair haberler ve doların 19 aylık zirvesi altını aşağı çekiyor. İran ve Ukrayna'daki gerilim güvenli liman talebi yaratabilir, ancak petrolün düşmesi ve ABD'nin "sonsuz savaş" ihtimalini reddetmesi bu etkiyi sınırlıyor; ayrıca Hazine tahvil satışıyla doların bir miktar zayıflaması karışık sinyal veriyor.
17.11 09:18 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 09:18 N  NEWS (6 new) score -0.30 conf 0.50: Haberler karışık ama ağırlıklı olarak altın için negatif: Fed faiz artırımı beklentileri, doların 19 aylık zirvesi ve 5% Hazine getirisi altın üzerinde baskı yaratıyor. Hormuz'daki tanker saldırısı ve İran gerilimi güvenli liman talebini destekleyebilir, ancak ABD'nin "sonsuz savaş" olmayacağını belirtmesi ve petrol fiyatlarının düşmesi bu etkiyi sınırlıyor. Bazı başlıklar eski veya çelişkili olduğu için güven düşük tutuldu.
17.11 09:30 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 09:30 N  NEWS (8 new) score -0.10 conf 0.35: İran'daki savaş ve Hürmüz'de tanker saldırısı gibi yeni jeopolitik gerilim unsurları güvenli liman talebini destekliyor. Ancak Fed faiz artırımı beklentileri, güçlenen dolar ve "aşırı satım" yorumları gibi baskılar altın üzerinde daha ağır basıyor; bu nedenle net etki hafif negatif ve düşük güvenle değerlendiriliyor.
17.11 09:43 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 09:43 N  NEWS (2 new) score -0.30 conf 0.40: Faiz artırımı beklentileri ve güçlü doların altın üzerindeki baskısı, İran gerilimi ve Hürmüz'deki tanker saldırısı gibi jeopolitik risklerin yarattığı güvenli liman talebinden daha ağır basıyor. Haberlerin çoğu zaten fiyatlanmış ve birbiriyle çelişiyor (ABD'nin "sonsuz savaş" yorumu, petrolün düşmesi), bu nedenle güven orta düzeyde tutuldu.
17.11 09:55 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 09:55 N  NEWS (17 new) score -0.70 conf 0.75: Altın 1 yılın dibine yakın seyrediyor; dolar 19 aylık zirvede ve Fed faiz artırımı beklentileri güçleniyor, bu da reel faizler ve dolar üzerinden altını baskılıyor. Jeopolitik haberler (İran savaşı, Ukrayna) güvenli liman talebini destekleyebilir, ancak bu etki faiz ve dolar baskısının gerisinde kalıyor ve petrol düşüşü enflasyon endişesini bir ölçüde hafifletiyor.
17.11 10:07 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 10:07 N  NEWS (23 new) score +0.12 conf 0.30: Haberlerin çoğu görüş yazısı, eski veya zaten fiyatlanmış jeopolitik gelişmeler; İran savaşı ve Ukrayna'daki çatışmalar güvenli liman talebini hafifçe destekliyor. Ancak Vance'in "sonsuz savaş olmayacak" açıklaması ve petrolün düşmesi, enflasyon beklentilerini yumuşatarak sınırlı bir dovish etki yaratabilir; bu karışık sinyaller nedeniyle güven düşük.
17.11 10:19 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 10:19 N  NEWS (17 new) score -0.70 conf 0.75: Altın 1 yıllık dibe yakın seyrediyor; dolar 19 aylık zirvede ve Fed faiz artırımı beklentileri artıyor, bu da reel faizleri ve doları yukarı iterek altın için güçlü bir baskı oluşturuyor. İran savaşı ve Hürmüz'deki saldırılar güvenli liman talebini destekleyebilse de, bu etki Fed sıkılaştırma beklentilerinin gerisinde kalıyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
