# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 06.11.2026 12:45 (İstanbul)

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

Son haber analizi (06.11 12:39): Claude puan **-0.20**, güven 0.45 — Dolar toparlanıyor ve NFP öncesi güç kazanıyor, Goldman da Fed'in şahin kaymasını gerekçe göstererek yıl sonu altın tahminini düşürdü; bu kısa vadede altın için baskılayıcı. İran savaşı belirsizliği ve petrolün 90 doların üzerinde seyretmesi güvenli liman talebini destekliyor, ancak bu etki dolar ve faiz beklentileri kadar güçlü görünmüyor.

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
06.11 11:14 N  GPT  score -0.30 conf 0.44: Doların güçlenmesiyle altının %1’den fazla düşmesi kısa vadede aşağı yönlü momentumu destekliyor; Fed faiz artırımı riskine ilişkin beklentiler de baskı yaratabilir. Buna karşılık yeni haberlerde güçlü ve doğrudan bir piyasa katalizörü yok, bu yüzden görünümün güveni sınırlı.
06.11 11:26 N  NEWS (6 new) score -0.30 conf 0.50: Fed'in sertleşme beklentisi, güçlenen dolar ve Goldman'ın hedef fiyat indirimi altın için baskı yaratıyor; İran savaşı ve teknoloji satışı kaynaklı güvenli liman talebi ise sınırlı bir destek sağlıyor. ABD istihdam verisi öncesi belirsizlik nedeniyle güven orta düzeyde tutuldu.
06.11 11:26 N  GPT  score -0.35 conf 0.62: Doların güçlenmesiyle altının %1’den fazla düşmesi ve Fed’in daha şahin kalabileceği beklentisi kısa vadede baskın, olumsuz etkenler. İran savaşı söylemi ve teknoloji satışlarının güvenli liman talebini artırma ihtimali düşüşü sınırlayabilir; yaklaşan ABD istihdam verisi belirsizliği yükseltiyor.
06.11 11:38 N  NEWS (7 new) score -0.35 conf 0.50: Dolar toparlanması ve altın fiyatının 4.050 doların altına düşmesi, Goldman'ın Fed'in şahin duruşu nedeniyle hedefi kırpması kısa vadede baskı yaratıyor. Ancak İran savaşı ve Ukrayna gibi jeopolitik riskler sürüyor, ayrıca ABD tarım dışı istihdam (NFP) verisi öncesi yön belirsiz olduğu için güven sınırlı.
06.11 11:38 N  GPT  score -0.45 conf 0.58: Doların istihdam verisi öncesinde güçlenmesiyle altının 4.050 doların altına gerilemesi, önümüzdeki saatler için aşağı yönlü baskıya işaret ediyor. Ukrayna savaşına ilişkin belirsizlik güvenli liman talebini destekleyebilir; ancak bu haberler yeni bir tırmanış göstermiyor ve yönü sınırlı ölçüde deng
06.11 11:50 N  NEWS (7 new) score -0.30 conf 0.50: Yeni haberlerin ağırlığı hafif negatif: Goldman'ın Fed'in şahin tutumu nedeniyle yıl sonu altın tahminini düşürmesi ve doların toparlanması altına baskı yapıyor. Buna karşılık İran savaşının yeniden başlayabileceğine dair haberler ve Kore borsasındaki sert düşüş güvenli liman talebini bir miktar destekliyor; bu yüzden güven orta düzeyde tutuldu.
06.11 11:50 N  GPT  score -0.55 conf 0.67: Kısa vadede doların toparlanması, altındaki sert düşüş ve Fed’in daha şahin olacağı beklentisi baskın; Goldman’ın tahmin indirimi de bu görünümü destekliyor. İran’da savaşın yeniden başlaması ihtimali güvenli liman talebini artırabilir, ancak haber belirsiz ve ilk piyasa tepkisi aşağı yönlü.
06.11 12:02 N  NEWS (12 new) score -0.40 conf 0.55: 
06.11 12:02 N  GPT  score -0.45 conf 0.62: Altının 4.050 doların altına düşmesi ve doların güçlenmesi, Fed’in daha şahin kalabileceği beklentisiyle önümüzdeki saatlerde baskının sürmesine işaret ediyor. İran’ın ABD’ye nükleer teklif gönderdiği haberi gerilimi azaltabilir; diğer jeopolitik riskler ise düşüşü sınırlayabilir.
06.11 12:15 N  NEWS (2 new) score -0.45 conf 0.60: Dolar toparlanması, Fed'de şahinleşme beklentisi ve Goldman'ın yıl sonu altın tahminini düşürmesi altın için baskılayıcı; altın $4.050'nin altına düştü. Kısa vadede İran savaşı ve jeopolitik gerilim gibi güvenli liman talebini destekleyebilecek haberler var ama bunların büyük kısmı zaten fiyatlanmış; ayrıca ABD tarım dışı istihdam (NFP) verisi öncesi oynaklık yüksek olduğu için güven sınırlı.
06.11 12:15 N  GPT  score -0.58 conf 0.70: Doların istihdam verisi öncesi toparlanması ve altının 4.050 doların altına düşmesi, kısa vadede altın üzerinde belirgin baskı yaratıyor; şahin Fed beklentileri de bu eğilimi destekliyor. İran’dan gelen müzakere haberi jeopolitik risk primini azaltabilir, ancak savaşla ilgili çelişkili haberler ve y
06.11 12:27 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
06.11 12:27 N  NEWS (8 new) score -0.30 conf 0.50: Kısa vadede altın için baskı ağırlıklı: Goldman'ın Fed'in şahin dönüşü nedeniyle yıl sonu altın tahminini düşürmesi, doların toparlanması ve altının 4.050 doların altına inmesi negatif. Buna karşılık İran savaşı, Trump'ın savaşı yeniden başlatma kararı ve küresel teknoloji satışı güvenli liman talebini destekleyebilir; ancak bu gelişmelerin büyük kısmı zaten fiyatlanmış görünüyor ve ABD tarım dışı istihdam (NFP) verisi öncesi belirsizlik yüksek.
06.11 12:39 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
06.11 12:39 N  NEWS (9 new) score -0.20 conf 0.45: Dolar toparlanıyor ve NFP öncesi güç kazanıyor, Goldman da Fed'in şahin kaymasını gerekçe göstererek yıl sonu altın tahminini düşürdü; bu kısa vadede altın için baskılayıcı. İran savaşı belirsizliği ve petrolün 90 doların üzerinde seyretmesi güvenli liman talebini destekliyor, ancak bu etki dolar ve faiz beklentileri kadar güçlü görünmüyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
