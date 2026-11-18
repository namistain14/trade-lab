# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 18.11.2026 11:38 (İstanbul)

## Bot A — Kripto 1 saatlik trend (x1)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 4,999.12 $** (başlangıç 5,000 $, -0.88 $ / %-0.02)

Açık pozisyonlar: SOLUSDT short @ 74.79 (TP 70.82 / SL 76.77)

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +315.19 $ | -195.51 $ |
| İşlem sayısı | 10 | 124 |
| Kazanma oranı | %70.0 | %43.5 |
| Ödenen komisyon/spread | 119.80 $ | 1474.41 $ |

**Hesap değeri: 4,798.49 $** (başlangıç 5,000 $, -201.51 $ / %-4.03)

Açık pozisyonlar: PAXGUSDT short @ 3758.61 (TP 3747.33 / SL 3766.13)

Son haber analizi (18.11 11:31): Claude puan **-0.60**, güven 0.70 — Altın 3.800 doların altına inip yılın en düşük seviyelerini gördü; dolar endeksi 19 aylık zirveye yakın ve piyasada Fed'in faiz artırımı ihtimali tartışılıyor, bu da 1-4 saatlik görünümde altın için baskılayıcı. Jeopolitik riskler (İran savaşı, Ukrayna, Kerç köprüsü) sürse de altın bu gerilimlere güvenli liman tepkisi vermiyor; FOMC tutanakları öncesi belirsizlik ise kısa vadede yön değişimi riskini artırıyor.

GPT (gpt-6-luna): puan **-0.55**, güven 0.68 — Doların 19 ayın zirvesine yakın seyretmesi ve Fed tutanakları öncesi faiz artışı beklentilerinin güçlenmesi, altın üzerinde kısa vadede baskın biçimde negatif. Kerç Köprüsü’ne yönelik saldırı güvenli liman talebini destekleyebilir; ancak mevcut fiyat düşüşü ve jeopolitik haberlerin sınırlı etkisi bu

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 18.11 11:31 | PAXGUSDT | short | -56.01 $ | stop |
| 18.11 11:14 | PAXGUSDT | short | +69.02 $ | take profit |
| 18.11 10:04 | PAXGUSDT | short | +69.02 $ | take profit |
| 18.11 08:32 | PAXGUSDT | short | -56.00 $ | stop |
| 18.11 07:19 | PAXGUSDT | short | -56.00 $ | stop |

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
| Net kâr/zarar | +0.00 $ | +9928.18 $ |
| İşlem sayısı | 0 | 51 |
| Kazanma oranı | %0.0 | %49.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 112,386.68 $** (başlangıç 100,000 $, +12386.68 $ / %+12.39)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 17.11 23:46 | TSLA | long | -435.97 $ | seans sonu |
| 17.11 23:46 | QQQ | long | -307.07 $ | seans sonu |
| 17.11 22:51 | NVDA | long | -1161.25 $ | stop |
| 13.11 23:33 | AAPL | long | -1154.98 $ | stop |
| 13.11 20:09 | TSLA | short | -1169.49 $ | stop |

## Son olaylar

```
18.11 10:31 N  GPT  score -0.35 conf 0.67: Fed faiz artırımı beklentilerinin güçlenmesi ve altındaki sert düşüş eğilimi kısa vadede baskın biçimde aşağı yönlü. ABD’nin İran’a yeniden saldırdığı haberi güvenli liman talebini artırabilir, ancak bu etki şimdilik düşüş baskısını dengelemekle sınırlı kalabilir.
18.11 10:43 N  NEWS (16 new) score -0.70 conf 0.70: Altın, Orta Doğu savaşına rağmen güvenli liman talebinin zayıf kaldığı, faiz artırımı beklentilerinin ve güçlenen doların baskı yarattığı bir ortamda 3.800 doların altına inip yıllık dibe yakın seviyelere geriledi. Dolar endeksinin 19 aylık zirveye yakın seyretmesi ve ABD'de faiz artırımı yönünde verilerin güçlenmesi kısa vadede altı aşağı çekmeye devam edebilir; buna karşın aşırı satış sonrası teknik tepki riski ve bazı analistlerin yukarı hedefleri güveni biraz sınırlıyor.
18.11 10:43 N  GPT  score -0.74 conf 0.78: Doların 19 ayın zirvesine yakın seyretmesi ve Fed’in sıkılaşma beklentilerinin güçlenmesi, kısa vadede altın üzerinde belirgin baskı yaratıyor; fiyatın 3.800 doların altına gerilemesi de düşüş eğilimini teyit ediyor. Orta Doğu’daki savaş güvenli liman talebi sağlasa da şu an bu baskıyı dengeleyemiyo
18.11 10:55 N  NEWS (13 new) score -0.70 conf 0.75: Altın 3.800 doların altına inerek Eylül 2025'ten bu yana en düşük seviyeye geriledi; Fed faiz artırımı beklentileri güçleniyor, dolar endeksi 19 aylık zirveye yakın ve ABD verileri faiz artırımını destekliyor. Bu makroekonomik baskı, savaş kaynaklı jeopolitik risk primini (İran savaşı, Ukrayna) büyük ölçüde bastırdığı için kısa vadede altın üzerinde ağırlıklı olarak düşüş yönlü bir etki bekleniyor.
18.11 10:55 N  GPT  score -0.62 conf 0.72: Altının 3.800 doların altına gerilemesi, doların 19 ayın zirvesine yakın seyretmesi ve Fed faiz artırımı beklentilerinin güçlenmesi kısa vadede baskının sürebileceğine işaret ediyor. Yeni jeopolitik başlıklar belirgin bir tırmanış göstermediğinden güvenli liman desteği sınırlı; haberlerin bir kısmı 
18.11 11:07 N  NEWS (7 new) score -0.60 conf 0.70: Altın 3.800 doların altına düştü ve yıllık dip seviyesine geriledi; DXY 19 aylık zirveye yakın seyrediyor ve veriler Fed'in faiz artırımı ihtimalini güçlendiriyor. Yeni İran savaşı gelişmeleri (ABD saldırıları, Bahreyn ve Kuveyt'te İHA saldırıları) jeopolitik risk primi sağlasa da, güçlü dolar ve artan faiz beklentileri bu güvenli liman etkisini baskılıyor.
18.11 11:07 N  GPT  score -0.68 conf 0.78: Güçlü dolar ve Fed faiz artırımı beklentilerinin derinleşmesi, altının 3.800 doların altına sert düşüşünü destekleyen başlıca kısa vadeli etkenler. Körfez’deki yeni drone saldırıları güvenli liman talebini artırabilir, ancak şu an bu baskıyı dengelemiyor.
18.11 11:16 B5  CLOSE short take profit: +69.02 USD
18.11 11:19 N  NEWS (10 new) score -0.70 conf 0.60: Altın 3.800 doların altına düştü; Fed faiz artırımı beklentileri ve doların 19 aylık zirveye yakın seyri altını baskılıyor. Yakın vadede FOMC tutanakları önemli bir risk olarak bekleniyor, İran savaşı gibi güvenli liman haberleri ise fiyatı desteklemeye yetmiyor.
18.11 11:19 N  GPT  score -0.68 conf 0.78: Dolar endeksindeki yükseliş ve Fed tutanakları öncesinde güçlenen şahin faiz beklentileri, kısa vadede altın üzerinde belirgin baskı oluşturuyor. Bölgesel çatışma haberleri güvenli liman talebini desteklese de yeni ve güçlü bir tırmanış sinyali vermiyor; altındaki sert düşüş de mevcut olumsuz moment
18.11 11:19 B5  SHORT gold 25000 USD x10 @ 3756.69 (TP 3745.42, SL 3764.20; news -0.69)
18.11 11:31 B5  CLOSE short stop: -56.01 USD
18.11 11:31 N  NEWS (4 new) score -0.60 conf 0.70: Altın 3.800 doların altına inip yılın en düşük seviyelerini gördü; dolar endeksi 19 aylık zirveye yakın ve piyasada Fed'in faiz artırımı ihtimali tartışılıyor, bu da 1-4 saatlik görünümde altın için baskılayıcı. Jeopolitik riskler (İran savaşı, Ukrayna, Kerç köprüsü) sürse de altın bu gerilimlere güvenli liman tepkisi vermiyor; FOMC tutanakları öncesi belirsizlik ise kısa vadede yön değişimi riskini artırıyor.
18.11 11:31 N  GPT  score -0.55 conf 0.68: Doların 19 ayın zirvesine yakın seyretmesi ve Fed tutanakları öncesi faiz artışı beklentilerinin güçlenmesi, altın üzerinde kısa vadede baskın biçimde negatif. Kerç Köprüsü’ne yönelik saldırı güvenli liman talebini destekleyebilir; ancak mevcut fiyat düşüşü ve jeopolitik haberlerin sınırlı etkisi bu
18.11 11:38 B5  SHORT gold 25000 USD x10 @ 3758.61 (TP 3747.33, SL 3766.13; news -0.57)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
