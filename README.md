# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 28.10.2026 13:00 (İstanbul)

## Bot A — Kripto kurallar (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -5.00 $ |
| İşlem sayısı | 0 | 3 |
| Kazanma oranı | %0.0 | %66.7 |
| Ödenen komisyon/spread | 0.00 $ | 6.00 $ |

**Hesap değeri: 4,995.00 $** (başlangıç 5,000 $, -5.00 $ / %-0.10)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 25.10 17:28 | BTCUSDT | long | +0.99 $ | time limit |
| 25.10 09:51 | SOLUSDT | long | -6.29 $ | stop |
| 23.10 09:46 | ETHUSDT | long | +0.30 $ | time limit |

## Bot A2 — Kripto: sert düşüş sonrası toparlanma (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +5.69 $ |
| İşlem sayısı | 0 | 1 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 2.01 $ |

**Hesap değeri: 5,005.69 $** (başlangıç 5,000 $, +5.69 $ / %+0.11)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 24.10 19:51 | ETHUSDT | long | +5.69 $ | take profit |

## Bot B1 — Altın + haber (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -2.08 $ | -95.09 $ |
| İşlem sayısı | 4 | 42 |
| Kazanma oranı | %50.0 | %23.8 |
| Ödenen komisyon/spread | 9.49 $ | 99.68 $ |

**Hesap değeri: 4,904.91 $** (başlangıç 5,000 $, -95.09 $ / %-1.90)

Son haber analizi (28.10 13:00): Claude puan **-0.35**, güven 0.50 — Fed'in bugün faizleri sabit tutması bekleniyor ancak yıl sonuna kadar bir faiz artışı fiyatlanıyor; enflasyon %3'ün üzerinde ve DXY iki haftalık zirveye yakın seyrediyor, bu da altın için baskı oluşturuyor. Buna karşılık İran savaşında Katarlı arabulucuların yeni bir anlaşma önermesi güvenli liman talebini biraz azaltabilir, ancak Fed'in beklenmedik şekilde gevşek çıkması dolar ve reel faizler üzerinden altını destekleyebilir; sinyaller karışık olduğu için güven düşük.

GPT (gpt-6-luna): puan **-0.38**, güven 0.62 — Fed kararı öncesinde ABD tahvil getirileri ve doların yükselmesi, altın için kısa vadede baskı oluşturuyor; faizlerin sabit kalması beklenirken enflasyon ve olası yıl sonu faiz artışı söylemi de temkinli bir görünüm yaratıyor. İran savaşı kaynaklı güvenli liman talebi destekleyici olsa da olası anla

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 28.10 10:24 | PAXGUSDT | short | -3.00 $ | stop |
| 28.10 09:13 | PAXGUSDT | short | -3.08 $ | stop (gap) |
| 28.10 08:56 | PAXGUSDT | short | +2.00 $ | take profit |
| 28.10 07:50 | PAXGUSDT | short | +2.00 $ | take profit |
| 27.10 12:19 | PAXGUSDT | short | -3.00 $ | stop |

## Bot B2 — Altın: sıkı haber eşiği (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -38.22 $ |
| İşlem sayısı | 0 | 7 |
| Kazanma oranı | %0.0 | %14.3 |
| Ödenen komisyon/spread | 0.00 $ | 16.61 $ |

**Hesap değeri: 4,961.78 $** (başlangıç 5,000 $, -38.22 $ / %-0.76)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 27.10 12:19 | PAXGUSDT | short | -3.00 $ | stop |
| 23.10 18:03 | PAXGUSDT | short | -4.28 $ | stop (gap) |
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 08:32 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 05:27 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B4 — Altın: haberin TERSİ (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -1.90 $ | -7.83 $ |
| İşlem sayısı | 1 | 6 |
| Kazanma oranı | %0.0 | %33.3 |
| Ödenen komisyon/spread | 2.37 $ | 14.23 $ |

**Hesap değeri: 4,998.64 $** (başlangıç 5,000 $, -1.36 $ / %-0.03)

Açık pozisyonlar: PAXGUSDT long @ 4053.84 (TP 4066.00 / SL 4045.73)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 28.10 01:16 | PAXGUSDT | long | -1.90 $ | time limit |
| 27.10 17:05 | PAXGUSDT | long | +13.81 $ | take profit |
| 27.10 15:33 | PAXGUSDT | long | +13.81 $ | take profit |
| 27.10 13:18 | PAXGUSDT | long | -11.18 $ | stop |
| 26.10 16:25 | PAXGUSDT | long | -11.18 $ | stop |

## Bot B3 — Altın: B2 + seans filtresi + momentum (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -26.82 $ |
| İşlem sayısı | 0 | 3 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 7.12 $ |

**Hesap değeri: 4,973.18 $** (başlangıç 5,000 $, -26.82 $ / %-0.54)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 18:22 | PAXGUSDT | short | -11.35 $ | stop (gap) |
| 23.10 18:03 | PAXGUSDT | short | -4.28 $ | stop (gap) |
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +10.69 $ |
| İşlem sayısı | 0 | 3 |
| Kazanma oranı | %0.0 | %66.7 |
| Ödenen komisyon/spread | 0.00 $ | 7.12 $ |

**Hesap değeri: 5,010.69 $** (başlangıç 5,000 $, +10.69 $ / %+0.21)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 27.10 13:42 | PAXGUSDT | short | -11.19 $ | stop |
| 24.10 00:03 | PAXGUSDT | short | +8.06 $ | time limit |
| 23.10 17:11 | PAXGUSDT | short | +13.82 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:2

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 99,842.81 $** (başlangıç 100,000 $, -157.19 $ / %-0.16)

## Son olaylar

```
28.10 09:11 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
28.10 09:11 N  NEWS (25 new) score -0.30 conf 0.40: Fed kararı bu gece beklenirken petrol kaynaklı enflasyon endişeleri ve güçlenen dolar (DXY ~102.50) altın için baskılayıcı; Körfez'de barış planı haberleri jeopolitik risk primini de azaltıyor. Öte yandan İran savaşının yeniden başlama riski ve yerel altın fiyatlarındaki yükselişler kısmen karşı yönde olduğu için güven sınırlı.
28.10 09:11 B1  SHORT gold 5000 USD x10 @ 4034.05 (TP 4031.48, SL 4035.52; news -0.30)
28.10 10:18 B1  CLOSE short stop (gap): -3.08 USD
28.10 10:18 N  GPT news failed: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settin
28.10 10:18 N  NEWS (32 new) score -0.35 conf 0.50: Fed kararı öncesinde dolar iki haftalık zirveye yakın seyrediyor ve piyasa faiz artırımı ihtimalini tartışıyor; petrol kaynaklı enflasyon endişeleri reel faiz beklentilerini sertleştirdiği için altın üzerinde baskı oluşturuyor. İran savaşı ve Orta Doğu gerilimi güvenli liman talebi yaratabilse de bu etki bu başlıklarda henüz fiyatlanmış görünmüyor, bu nedenle etki sınırlı kalabilir. Fed'in beklenmedik şekilde yumuşak çıkması ya da savaşta ciddi tırmanma gelmesi durumunda görüş hızla tersine dönebilir.
28.10 10:18 B1  SHORT gold 5000 USD x10 @ 4039.67 (TP 4037.10, SL 4041.14; news -0.35)
28.10 11:15 B1  CLOSE short stop: -3.00 USD
28.10 11:15 N  NEWS (33 new) score -0.40 conf 0.55: Fed öncesi dolar güçleniyor, Treasury getirileri yükseliyor ve piyasa Fed'in faiz artırımına yönelebileceğini fiyatlıyor; enflasyonun %3 üzerinde seyretmesi bu hawkish görünümü destekliyor. İran savaşı ve jeopolitik riskler güvenli liman talebi yaratabilir, ancak bu etki büyük ölçüde fiyatlanmış görünüyor, bu nedenle kısa vadede baskı altındaki altın fiyatı için ağırlıklı olarak negatif bir tablo var.
28.10 11:15 N  GPT  score -0.45 conf 0.65: Fed kararı öncesinde doların güçlenmesi ve ABD tahvil getirilerinin yükselmesi, kısa vadede altını baskılıyor; fiyatın zaten düşmüş olması ve jeopolitik riskler aşağı yönü sınırlayabilir. Karar yaklaşırken yönün hızla değişme ihtimali nedeniyle güven orta düzeyde.
28.10 11:15 B4  LONG gold 5000 USD x10 @ 4053.84 (TP 4066.00, SL 4045.73; news +0.40)
28.10 12:10 N  NEWS (34 new) score -0.25 conf 0.40: Fed'in bugün faizleri sabit tutması bekleniyor ancak yıl sonuna kadar bir faiz artışı fiyatlanıyor; enflasyon %3'ün üzerinde ve DXY iki haftalık zirveye yakın seyrediyor, bu da altın için baskı oluşturuyor. Buna karşılık İran savaşında Katarlı arabulucuların yeni bir anlaşma önermesi güvenli liman talebini biraz azaltabilir, ancak Fed'in beklenmedik şekilde gevşek çıkması dolar ve reel faizler üzerinden altını destekleyebilir; sinyaller karışık olduğu için güven düşük.
28.10 12:10 N  GPT  score -0.25 conf 0.43: Fed kararı öncesinde doların iki haftalık zirveye yakın seyretmesi ve olası faiz artışı beklentileri altın üzerinde baskı yaratıyor. İran savaşı güvenli liman talebini desteklese de yeni anlaşma girişimi gerilimin azalabileceğine işaret ediyor; haber akışı çelişkili ve önemli ölçüde fiyatlanmış olab
28.10 13:00 N  NEWS (28 new) score -0.35 conf 0.50: 
28.10 13:00 N  GPT  score -0.38 conf 0.62: Fed kararı öncesinde ABD tahvil getirileri ve doların yükselmesi, altın için kısa vadede baskı oluşturuyor; faizlerin sabit kalması beklenirken enflasyon ve olası yıl sonu faiz artışı söylemi de temkinli bir görünüm yaratıyor. İran savaşı kaynaklı güvenli liman talebi destekleyici olsa da olası anla
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
