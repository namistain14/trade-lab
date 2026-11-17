# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 17.11.2026 18:50 (İstanbul)

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

Son haber analizi (17.11 18:50): Claude puan **-0.50**, güven 0.60 — Altın, dolar 19 aylık zirvesi ve 10 yıllık tahvil getirisinin %5'e yaklaşması nedeniyle baskı altında; ABD enflasyonunun beklentinin üzerinde gelmesi de Fed'in sıkı kalacağı beklentisini güçlendiriyor. Jeopolitik gerilim (İran savaşı, Kırım Köprüsü) güvenli liman talebini destekleyebilir, ancak Vance'in "sonsuz savaş olmayacak" açıklaması bu etkiyi sınırlıyor; sonuç olarak kısa vadede net negatif görünüm, orta düzeyde güven.

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
17.11 18:07 B6  karar turu: Claude «Piyasa hafif negatif, teknoloji baskı altında; şirkete özgü haberler ve göreceli güç ön planda.» / GPT «-»
17.11 18:13 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 18:13 N  NEWS (20 new) score -0.40 conf 0.60: Altının bir yıllık dip seviyelerine yakın olması, doların 19 aylık zirvede olması, faiz artırımı beklentilerinin sertleşmesi ve ABD enflasyonunun beklentileri aşması altın için baskı oluşturuyor. Jeopolitik tarafta İran savaşına ilişkin "sonsuz savaş olmayacak" açıklamaları güvenli liman talebini sınırlıyor; yalnızca hisse senedi skandallarına bağlı kısa süreli bir yükseliş görülmesi bu tabloyu tam tersine çevirmiyor.
17.11 18:19 B6  GPT cevap vermedi: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the A
17.11 18:19 B6  karar turu: Claude «Piyasa çip hisselerinin baskısıyla hafif negatif seyrediyor; teknolojide zayıflık öne çıkıyor.» / GPT «-»
17.11 18:25 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 18:25 N  NEWS (12 new) score -0.60 conf 0.65: Altın bir yıllık dibe yakın seyrediyor; dolar 19 aylık zirvede, ABD enflasyonu beklentileri aştı, faiz artırımı beklentileri sertleşiyor ve 10 yıllık getiri %5'e yaklaşıyor. Iran savaşı güvenli liman talebini destekleyecek bir etki yaratmıyor, bu nedenle baskı sürecek gibi görünüyor; eski ve çelişkili 'altın yükseldi' haberi ise güveni biraz düşürüyor.
17.11 18:32 B6  GPT cevap vermedi: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the A
17.11 18:32 B6  karar turu: Claude «Teknoloji ağırlıklı satış baskısıyla endeksler gün içi düşüş eğiliminde, çip hisseleri en zayıf grup.» / GPT «-»
17.11 18:38 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 18:38 N  NEWS (13 new) score -0.40 conf 0.50: Altın, dolar 19 aylık zirvesi ve 10 yıllık tahvil getirisinin %5'e yaklaşması nedeniyle baskı altında; ABD enflasyonunun beklentinin üzerinde gelmesi de Fed'in sıkı kalacağı beklentisini güçlendiriyor. Jeopolitik gerilim (İran savaşı, Kırım Köprüsü) güvenli liman talebini destekleyebilir, ancak Vance'in "sonsuz savaş olmayacak" açıklaması bu etkiyi sınırlıyor; sonuç olarak kısa vadede net negatif görünüm, orta düzeyde güven.
17.11 18:44 B6  GPT cevap vermedi: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the A
17.11 18:44 B6  karar turu: Claude «Piyasada son bir saatte teknoloji öncülüğünde sert satış var; zayıf hisselerde kısa pozisyon tercih edilir ancak aşırı satım sonrası tepki riski göz önünde tutulmalı.» / GPT «-»
17.11 18:50 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 18:50 N  NEWS (8 new) score -0.50 conf 0.60: 
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
