# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 06.11.2026 13:40 (İstanbul)

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
| Net kâr/zarar | -335.82 $ | -369.77 $ |
| İşlem sayısı | 6 | 58 |
| Kazanma oranı | %0.0 | %39.7 |
| Ödenen komisyon/spread | 71.06 $ | 688.52 $ |

**Hesap değeri: 4,630.23 $** (başlangıç 5,000 $, -369.77 $ / %-7.40)

Son haber analizi (06.11 13:40): Claude puan **-0.25**, güven 0.40 — Fed'in Williams'ın enflasyonun hâlâ çok yüksek olduğu yönündeki açıklaması ve dolar ile tahvil faizlerindeki toparlanma, altın üzerinde kısa vadede baskı yaratıyor. İran'a yönelik üçüncü ABD uçak gemisi görevi jeopolitik risk kaynaklı güvenli liman talebini destekleyebilir, ancak petrolün gerilim azalması sinyalleriyle düşmesi bu etkiyi dengeliyor; ayrıca NFP öncesi piyasa belirsizliği nedeniyle sinyal karışık.

GPT (gpt-6-luna): puan **-0.30**, güven 0.56 — Fed Williams’ın enflasyonun hâlâ fazla yüksek olduğunu vurgulaması, dolar ve faiz beklentileri üzerinden altını kısa vadede baskılayabilir; NFP öncesi güçlü dolar ve düşen altın da bu yönü destekliyor. İran çevresindeki askerî gerilim güvenli liman talebi yaratabilir, ancak haberler çelişkili ve yak

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 10:57 | PAXGUSDT | short | -55.94 $ | stop |
| 06.11 09:25 | PAXGUSDT | short | -55.94 $ | stop |
| 06.11 08:11 | PAXGUSDT | short | -56.23 $ | stop (gap) |
| 06.11 04:01 | PAXGUSDT | long | -55.91 $ | stop |
| 06.11 03:47 | PAXGUSDT | long | -55.90 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -58.75 $ | +7.68 $ |
| İşlem sayısı | 1 | 2 |
| Kazanma oranı | %0.0 | %50.0 |
| Ödenen komisyon/spread | 17.52 $ | 34.69 $ |

**Hesap değeri: 5,007.68 $** (başlangıç 5,000 $, +7.68 $ / %+0.15)

Son haber analizi (06.11 07:59): Claude puan **+0.35**, güven 0.50 — Hormuz'daki yeni tanker saldırıları ve Rusya'daki rafineri patlamaları/Ukrayna saldırıları arz riskini artırıp Brent'i 100 doların üzerine itti; ancak İran'ın Katar üzerinden nükleer öneri göndermesi, Orta Doğu barış beklentileri ve haftalık yaklaşık %12-13'lük düşüş yukarı yönlü hareketi sınırlayabilir, bu yüzden güven orta düzeyde.

GPT (gpt-6-luna): puan **+0.55**, güven 0.66 — Hürmüz Boğazı’nda yeni tanker saldırısı haberleri ve Rusya’daki rafinerilere yönelik saldırı bildirimleri yakın vadeli arz riskini artırarak Brent’i destekliyor. İran’ın ABD’ye ilettiği bildirilen nükleer öneri ve daha geniş barış beklentileri bu etkiyi sınırlıyor; haberlerin bir kısmı doğrulanmamış

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 08:11 | BZ=F | long | -58.75 $ | stop |
| 02.11 23:09 | BZ=F | short | +66.43 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +5879.74 $ |
| İşlem sayısı | 0 | 21 |
| Kazanma oranı | %0.0 | %52.4 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 108,259.60 $** (başlangıç 100,000 $, +8259.60 $ / %+8.26)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 05.11 23:46 | SPY | short | +582.01 $ | seans sonu |
| 05.11 23:46 | QQQ | short | +576.72 $ | seans sonu |
| 05.11 23:46 | NVDA | short | +1215.36 $ | seans sonu |
| 05.11 23:46 | AAPL | long | +93.44 $ | seans sonu |
| 05.11 20:37 | QQQ | short | -1070.92 $ | stop |

## Son olaylar

```
06.11 12:15 N  GPT  score -0.58 conf 0.70: Doların istihdam verisi öncesi toparlanması ve altının 4.050 doların altına düşmesi, kısa vadede altın üzerinde belirgin baskı yaratıyor; şahin Fed beklentileri de bu eğilimi destekliyor. İran’dan gelen müzakere haberi jeopolitik risk primini azaltabilir, ancak savaşla ilgili çelişkili haberler ve y
06.11 12:27 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
06.11 12:27 N  NEWS (8 new) score -0.30 conf 0.50: Kısa vadede altın için baskı ağırlıklı: Goldman'ın Fed'in şahin dönüşü nedeniyle yıl sonu altın tahminini düşürmesi, doların toparlanması ve altının 4.050 doların altına inmesi negatif. Buna karşılık İran savaşı, Trump'ın savaşı yeniden başlatma kararı ve küresel teknoloji satışı güvenli liman talebini destekleyebilir; ancak bu gelişmelerin büyük kısmı zaten fiyatlanmış görünüyor ve ABD tarım dışı istihdam (NFP) verisi öncesi belirsizlik yüksek.
06.11 12:39 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
06.11 12:39 N  NEWS (9 new) score -0.20 conf 0.45: Dolar toparlanıyor ve NFP öncesi güç kazanıyor, Goldman da Fed'in şahin kaymasını gerekçe göstererek yıl sonu altın tahminini düşürdü; bu kısa vadede altın için baskılayıcı. İran savaşı belirsizliği ve petrolün 90 doların üzerinde seyretmesi güvenli liman talebini destekliyor, ancak bu etki dolar ve faiz beklentileri kadar güçlü görünmüyor.
06.11 12:51 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
06.11 12:51 N  NEWS (5 new) score -0.35 conf 0.50: 
06.11 13:04 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
06.11 13:04 N  NEWS (4 new) score -0.30 conf 0.50: 
06.11 13:16 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
06.11 13:16 N  NEWS (6 new) score -0.40 conf 0.55: Altın, güçlenen doların ve beklenen güçlü ABD tarım dışı istihdam (NFP) verisi öncesinde yaklaşık %1 düşüyor; Goldman'ın Fed'in sertleşme yönlü değişimi nedeniyle yıl sonu altın tahminini düşürmesi de kısa vadede baskı yaratıyor. Öte yandan İran'daki gerilimin azalmasına dair işaretler petrol fiyatlarını düşürse de WTI hâlâ 90 doların üzerinde olduğundan enflasyon ve faiz beklentileri altın için olumsuz kalıyor; NFP sonucunun belirsizliği nedeniyle güven sınırlı.
06.11 13:28 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
06.11 13:28 N  NEWS (17 new) score -0.30 conf 0.50: Faiz artırımı beklentileri, güçlenen dolar ve tahvil getirilerindeki toparlanma altın üzerinde baskı yaratıyor; Goldman'ın Fed'in sert duruşu nedeniyle yıl sonu altın tahminini düşürmesi de olumsuz. İran savaşına ilişkin jeopolitik riskler ise güvenli liman talebi yaratabilir, ancak petrol fiyatlarındaki düşüş gerilimin azalabileceğine işaret ettiği için bu destek sınırlı kalabilir.
06.11 13:40 N  NEWS (18 new) score -0.25 conf 0.40: Fed'in Williams'ın enflasyonun hâlâ çok yüksek olduğu yönündeki açıklaması ve dolar ile tahvil faizlerindeki toparlanma, altın üzerinde kısa vadede baskı yaratıyor. İran'a yönelik üçüncü ABD uçak gemisi görevi jeopolitik risk kaynaklı güvenli liman talebini destekleyebilir, ancak petrolün gerilim azalması sinyalleriyle düşmesi bu etkiyi dengeliyor; ayrıca NFP öncesi piyasa belirsizliği nedeniyle sinyal karışık.
06.11 13:40 N  GPT  score -0.30 conf 0.56: Fed Williams’ın enflasyonun hâlâ fazla yüksek olduğunu vurgulaması, dolar ve faiz beklentileri üzerinden altını kısa vadede baskılayabilir; NFP öncesi güçlü dolar ve düşen altın da bu yönü destekliyor. İran çevresindeki askerî gerilim güvenli liman talebi yaratabilir, ancak haberler çelişkili ve yak
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
