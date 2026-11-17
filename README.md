# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 17.11.2026 12:15 (İstanbul)

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

Son haber analizi (17.11 12:09): Claude puan **-0.20**, güven 0.40 — Dolar endeksi 19 aylık zirveden geri çekilse de güçlü dolar momentumu ve ING'nin "güçlü momentum" değerlendirmesi altın için baskı oluşturuyor. İran savaşı ve Ukrayna'daki saldırılar güvenli liman talebini destekliyor, ancak Vance'in "sonsuz savaş olmayacak" açıklaması jeopolitik primi sınırlıyor; altın ise yıllık dip yakınında değer bölgesini test ediyor. Haberlerin büyük kısmı zaten fiyatlanmış veya karışık olduğu için sinyal zayıf.

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
17.11 10:44 N  NEWS (43 new) score -0.70 conf 0.75: Altın, Fed faiz artırımı beklentileri ve 19 aylık zirvedeki dolar nedeniyle 1 yıllık dibe yakın işlem görüyor; reel getiri ve enflasyon baskısı altını aşağı çekiyor. Ukrayna-Rusya saldırıları gibi jeopolitik haberler eski ve fiyatlanmış olduğundan güvenli liman talebini artırmıyor; yüksek belirsizlik nedeniyle güven sınırlı tutuldu.
17.11 10:56 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 10:56 N  NEWS (25 new) score -0.50 conf 0.60: Altın, Fed faiz artırımı beklentileri ve 19 aylık zirveye çıkan dolar nedeniyle yılın dibine yakın işlem görüyor; bu baskı jeopolitik haberlerdeki sınırlı güvenli liman talebinin önüne geçiyor. ABD tahvil getirilerindeki düşüş ve dolardaki hafif geri çekilme kısa vadede bir miktar destek sağlayabilir, bu yüzden güven orta düzeyde tutuldu.
17.11 11:08 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 11:08 N  NEWS (16 new) score -0.10 conf 0.35: Jeopolitik gerilim (Kırım köprüsü, Kiev saldırıları, Hürmüz'de tanker vurulması) güvenli liman talebini destekleyebilir, ancak altın son haberlerde savaş primi yerine Fed faiz artırımı beklentileri ve güçlü dolar nedeniyle bir yıllık dibe yakın işlem görüyor. Bu çelişki nedeniyle ve yeni haberlerin çoğunun doğrudan altın fiyatını hareket ettirecek nitelikte olmaması sebebiyle hafif negatif, düşük güvenli bir görünüm.
17.11 11:20 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 11:20 N  NEWS (19 new) score -0.60 conf 0.60: Altın, Fed faiz artırımı beklentileri ve dolardaki 19 aylık zirve nedeniyle yılın dibine yakın seyrediyor; bu, 1-4 saatlik vadede altın için baskılayıcı bir tablo. Jeopolitik gerilim (İran savaşı, Hürmüz, Ukrayna) güvenli liman talebi yaratsa da bu etki belirgin biçimde sınırlı kalıyor; ABD tahvil getirilerindeki bazı geri çekilmeler ve dolardaki kısmi gevşeme ise güveni azaltıyor.
17.11 11:32 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 11:32 N  NEWS (8 new) score -0.20 conf 0.35: Başlıklar karışık: Fed faiz artırımı beklentileri ve güçlü dolar altını yıllık dibe yakın tutarken, ABD tahvil getirilerindeki düşüş ve dolardaki geri çekilme kısmen destekliyor. İran ve Ukrayna çatışmalarındaki jeopolitik gerilim güvenli liman talebi yaratabilir, ancak bu haberlerin çoğu zaten fiyatlanmış ve yeni bir tırmanış sinyali zayıf; net etki hafif negatif, güven düşük.
17.11 11:44 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 11:44 N  NEWS (10 new) score +0.10 conf 0.40: Jeopolitik gerilim (İran savaşı, Ukrayna-Kırım saldırıları) altın için güvenli liman talebini destekliyor, ayrıca DXY 19 aylık zirveden geri çekilirken ABD tahvil getirilerinin düşmesi altın için olumlu. Buna karşılık ING'in güçlü dolar görüşü ve EUR/USD'nin 19 aylık dibe yakın seyretmesi ile dolar momentumu altın üzerinde baskı yaratabilir; haberlerin büyük kısmı zaten fiyatlanmış niteliğinde olduğundan güven düşük tutuldu.
17.11 11:56 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 11:56 N  NEWS (10 new) score -0.10 conf 0.35: Dolar tarafında güç (DXY 19 aylık zirvelerden geri çekilse de ING'nin güçlü momentum tespiti ve euro/dolarda 19 aylık dip) altın için baskı oluşturuyor; altın da bir yılı aşkın dip bölgesine yakın işlem görüyor. Ukrayna'daki Kerç köprüsü saldırısı ve İran savaşına dair jeopolitik gerilim jeopolitik risk primini destekliyor, ancak Vance'in "sonsuz savaş olmayacak" açıklaması bu riski sınırlıyor; kısa vadeli etki hafif negatif, çelişkili haberler nedeniyle güven düşük.
17.11 12:09 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
17.11 12:09 N  NEWS (7 new) score -0.20 conf 0.40: Dolar endeksi 19 aylık zirveden geri çekilse de güçlü dolar momentumu ve ING'nin "güçlü momentum" değerlendirmesi altın için baskı oluşturuyor. İran savaşı ve Ukrayna'daki saldırılar güvenli liman talebini destekliyor, ancak Vance'in "sonsuz savaş olmayacak" açıklaması jeopolitik primi sınırlıyor; altın ise yıllık dip yakınında değer bölgesini test ediyor. Haberlerin büyük kısmı zaten fiyatlanmış veya karışık olduğu için sinyal zayıf.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
