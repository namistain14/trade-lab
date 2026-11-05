# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 05.11.2026 14:37 (İstanbul)

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
| Net kâr/zarar | +233.54 $ | +120.67 $ |
| İşlem sayısı | 7 | 47 |
| Kazanma oranı | %71.4 | %46.8 |
| Ödenen komisyon/spread | 82.79 $ | 558.27 $ |

**Hesap değeri: 5,120.67 $** (başlangıç 5,000 $, +120.67 $ / %+2.41)

Son haber analizi (05.11 14:37): Claude puan **+0.10**, güven 0.30 — Altın, ABD ara seçim sonrası yaklaşık %1,6 yükselerek 4.124,89 dolara çıktı ve toparlanma sürüyor; ancak haber akışının büyük kısmı jeopolitik gürültü ve eski haberlerden oluşuyor. Dolar toparlanması ve yaklaşan ABD NFP verisinin yönü belirsiz olduğu için sinyal zayıf, bu nedenle skor hafif pozitif ve güven düşük tutuldu.

GPT (gpt-6-luna): puan **+0.25**, güven 0.43 — Altın, seçim sonrası oynaklık ve zayıf dolar haberleriyle yükselmiş; bu kısa vadede yukarı yönlü momentumu destekliyor. Ancak doların toparlanması ve yaklaşan ABD istihdam verisi kazançları sınırlayabilir; yükselişin önemli kısmı zaten fiyatlanmış olabilir.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 05.11 14:18 | PAXGUSDT | long | +69.07 $ | take profit |
| 05.11 10:28 | PAXGUSDT | long | -55.90 $ | stop |
| 05.11 08:21 | PAXGUSDT | long | -55.90 $ | stop |
| 05.11 06:55 | PAXGUSDT | long | +69.07 $ | take profit |
| 05.11 04:12 | PAXGUSDT | long | +69.07 $ | take profit |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +66.43 $ |
| İşlem sayısı | 0 | 1 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 17.17 $ |

**Hesap değeri: 5,066.43 $** (başlangıç 5,000 $, +66.43 $ / %+1.33)

Son haber analizi (05.11 07:59): Claude puan **-0.05**, güven 0.40 — Haberler çelişkili: İran'ın Hürmüz'de dört tankerin mayınlarla vurulduğunu öne sürmesi ve petrol fiyatlarındaki Hürmüz arz riskleri fiyatı yukarı iter; buna karşılık Brent'in İran müzakereleri nedeniyle 4 haftalık dibe inmesi ve ABD-İran arasında anlaşmanın hâlâ uzak olması aşağı yönlü baskı yaratır. Tanker iddiası doğrulanmamış olduğu için net etki hafif pozitif, güven düşük.

GPT (gpt-6-luna): puan **+0.28**, güven 0.55 — Hürmüz’de iki tanker ve bir römorkörün alev aldığı haberi, doğrulanması hâlinde yakın vadeli arz ve taşımacılık risk primini artırarak Brent’i yukarı destekleyebilir. Ancak İran geriliminin azalacağı beklentileriyle süren sert satış ve haberin nedeni hakkındaki belirsizlik yükseliş etkisini sınırlıy

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 23:09 | BZ=F | short | +66.43 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +3307.54 $ |
| İşlem sayısı | 0 | 12 |
| Kazanma oranı | %0.0 | %41.7 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 105,876.17 $** (başlangıç 100,000 $, +5876.17 $ / %+5.88)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 04.11 23:45 | SPY | long | +485.08 $ | seans sonu |
| 04.11 23:45 | QQQ | long | -222.60 $ | seans sonu |
| 04.11 23:45 | AAPL | long | -505.78 $ | seans sonu |
| 04.11 23:39 | NVDA | short | +1575.42 $ | take profit |
| 04.11 22:26 | TSLA | long | +604.29 $ | take profit |

## Son olaylar

```
05.11 13:07 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
05.11 13:07 N  NEWS (17 new) score +0.30 conf 0.40: Dolar ve Treasury getirilerinin ara seçim sonrası zayıflaması ile petrolün Iran'a dair umutlarla düşmesi, altın için kısa vadede destekleyici; ancak İran savaşı riski ve hawkish Fed enflasyon beklentileri karşıt yönde etki yaratıp güveni sınırlıyor. Altının rebound haberleri kısmen fiyatlanmış olabilir.
05.11 13:19 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
05.11 13:19 N  NEWS (11 new) score +0.25 conf 0.40: Dolar ve Treasury getirilerinin ara vermesi, ara seçim sonrası "Gold rallies" haberleri ve petrol fiyatlarındaki düşüşle birlikte altın için hafif pozitif bir tablo var. Ancak İran'a ilişkin jeopolitik gerilimin sürmesi ve Fed'in enflasyon tahminlerine dair sert haberler belirsizliği artırdığı için sinyaller karışık ve güven sınırlı.
05.11 13:31 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
05.11 13:31 N  NEWS (8 new) score +0.40 conf 0.55: 
05.11 13:43 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
05.11 13:43 N  NEWS (11 new) score +0.30 conf 0.50: İran'daki çatışma ve Hürmüz Boğazı'ndaki tanker yangınları, Trump'ın yeni saldırı ihtimali ve Körfez'deki gerilim güvenli liman talebini destekliyor. Dolar ve ABD tahvil getirilerindeki zayıflama da altın için olumlu. Buna karşın petrol fiyatlarındaki sert düşüş ve enflasyon/Fed beklentilerine ilişkin belirsizlik sınırlı bir yükseliş potansiyeli bırakıyor; sinyaller karışık olduğu için güven orta düzeyde tutuldu.
05.11 14:13 N  NEWS (27 new) score +0.05 conf 0.30: Haberler karışık: İran savaşına yönelik gerilimin azalması ve doların toparlanması altın için olumsuz, buna karşılık Trump'ın yeniden saldırı seçeneğini değerlendirmesi ve altının toparlanma eğilimi olumlu. ABD tarım dışı istihdam (NFP) verisi beklenirken kısa vadede net bir yön oluşmadığı için etki sınırlı ve yüksek belirsizlik içeriyor.
05.11 14:13 N  GPT  score +0.20 conf 0.40: İran savaşı ve Suudi Arabistan’a yönelen füze haberi güvenli liman talebini destekleyebilir; altının toparlanması da olumlu. Ancak doların yeniden güçlenmesi ve yaklaşan ABD istihdam verisi yukarı yönlü etkiyi sınırlıyor; savaş söyleminin soğuduğuna dair haberler de tabloyu karışık kılıyor.
05.11 14:19 B5  CLOSE long take profit: +69.07 USD
05.11 14:25 N  NEWS (11 new) score -0.10 conf 0.30: Başlıkların çoğu gürültü veya eski haber. İran savaşı söyleminin ara seçim yenilgisiyle yumuşaması jeopolitik risk primini biraz azaltabilir, ABD doları toparlanması ise altın için baskı yaratıyor. Gold'un kısa vadeli toparlanması ve NFP öncesi belirsizlik, yönü net olmadığı için etkiyi sınırlı tutuyor.
05.11 14:25 N  GPT  score +0.20 conf 0.38: Altının toparlanması ve zayıf dolar haberleri kısa vadede hafif destekleyici; Kuzey Kore’nin füze denemeleri de güvenli liman talebini artırabilir. Ancak doların yeniden güçlenmesi, İran savaşı kaynaklı risklerin siyasi olarak yatışabileceği beklentisi ve yaklaşan ABD istihdam verisi yönü belirsizle
05.11 14:37 N  NEWS (14 new) score +0.10 conf 0.30: Altın, ABD ara seçim sonrası yaklaşık %1,6 yükselerek 4.124,89 dolara çıktı ve toparlanma sürüyor; ancak haber akışının büyük kısmı jeopolitik gürültü ve eski haberlerden oluşuyor. Dolar toparlanması ve yaklaşan ABD NFP verisinin yönü belirsiz olduğu için sinyal zayıf, bu nedenle skor hafif pozitif ve güven düşük tutuldu.
05.11 14:37 N  GPT  score +0.25 conf 0.43: Altın, seçim sonrası oynaklık ve zayıf dolar haberleriyle yükselmiş; bu kısa vadede yukarı yönlü momentumu destekliyor. Ancak doların toparlanması ve yaklaşan ABD istihdam verisi kazançları sınırlayabilir; yükselişin önemli kısmı zaten fiyatlanmış olabilir.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
