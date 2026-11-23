# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.11.2026 14:44 (İstanbul)

## Bot A — Kripto 1 saatlik trend (x1)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +104.97 $ |
| İşlem sayısı | 0 | 2 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 3.25 $ |

**Hesap değeri: 5,092.68 $** (başlangıç 5,000 $, +92.68 $ / %+1.85)

Açık pozisyonlar: SOLUSDT short @ 72.30 (TP 69.79 / SL 73.55)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 20.11 04:03 | SOLUSDT | short | +37.10 $ | time limit |
| 19.11 01:49 | XRPUSDT | short | +67.87 $ | take profit |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +297.35 $ |
| İşlem sayısı | 0 | 193 |
| Kazanma oranı | %0.0 | %46.1 |
| Ödenen komisyon/spread | 0.00 $ | 2307.16 $ |

**Hesap değeri: 5,297.35 $** (başlangıç 5,000 $, +297.35 $ / %+5.95)

Son haber analizi (23.11 14:38): Claude puan **-0.10**, güven 0.30 — Başlıklar birbiriyle çelişiyor: FOMC tutanakları doları güçlendirdiği için altında sert satış ve güçlü dolar baskısı var, ancak yüzde 2'den fazla yükselişi tetikleyen Fed faiz artırımı beklentilerinin azalması ve PCE verisi öne çıkıyor. Jeopolitik risk (İran savaşı) ise güvenli liman talebini destekleyici olsa da fonlamanın kesilmesi yönündeki haberler bu etkiyi sınırlıyor. Net etki hafif negatif, düşük güvenle değerlendirilmeli.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 20.11 19:13 | PAXGUSDT | short | -56.07 $ | stop |
| 20.11 19:02 | PAXGUSDT | short | +68.96 $ | take profit |
| 20.11 18:37 | PAXGUSDT | short | -56.07 $ | stop |
| 20.11 18:28 | PAXGUSDT | short | +68.95 $ | take profit |
| 20.11 17:53 | PAXGUSDT | short | +68.97 $ | take profit |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -123.04 $ |
| İşlem sayısı | 0 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 0.00 $ | 70.51 $ |

**Hesap değeri: 4,876.96 $** (başlangıç 5,000 $, -123.04 $ / %-2.46)

Son haber analizi (23.11 08:00): Claude puan **+0.05**, güven 0.40 — Husi saldırıları Suudi rafineri ve tesislerini hedef alarak arz riskini artırıyor ve Hürmüz'deki tanker saldırıları jeopolitik primi destekliyor. Ancak piyasa bu riskleri fiyatlamakta zorlanıyor: küresel hisse senedi satışı, güçlü Orta Doğu ihracatı ve son bir ayda %21'lik düşüş Brent'i aşağı çekiyor, bu nedenle net etki hafif pozitif ama belirsiz.

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
| Net kâr/zarar | +0.00 $ | +25414.95 $ |
| İşlem sayısı | 0 | 79 |
| Kazanma oranı | %0.0 | %53.2 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 128,183.18 $** (başlangıç 100,000 $, +28183.18 $ / %+28.18)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 20.11 23:45 | AAPL | short | +1408.47 $ | seans sonu |
| 20.11 23:32 | SPY | short | +1844.50 $ | take profit |
| 20.11 23:26 | QQQ | short | +1847.34 $ | take profit |
| 20.11 20:02 | QQQ | short | +1793.08 $ | take profit |
| 20.11 19:32 | TSLA | short | +1798.50 $ | take profit |

## Son olaylar

```
23.11 13:25 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 13:25 N  NEWS (13 new) score -0.20 conf 0.40: Fed faiz artırımı beklentileri ve güçlenen doların (EUR/USD 2025 Nisan dibi) altın üzerinde baskı yaratıyor; ancak İran'daki gerilim ve ABD donanma ablukası jeopolitik talebi destekliyor ve düşen Treasury getirileri altını yukarı taşıyor. Net etki hafif negatif, sinyaller çelişkili olduğu için güven düşük.
23.11 13:37 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 13:37 N  NEWS (14 new) score -0.15 conf 0.40: Faiz artırımı beklentileri, güçlü dolar ve "3 ardışık faiz artırımı" yorumları altın için baskılayıcı. Buna karşılık teknoloji satışı ve İran savaşı güvenli liman talebini destekliyor, altın da 3.600$ üzerinde toparlanıyor; sinyaller çelişkili olduğu için etki hafif negatif ve düşük güvenle değerlendirildi.
23.11 13:49 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 13:49 N  NEWS (8 new) score -0.15 conf 0.40: Haberler karışık: Fed'in sıkılaşma beklentileri ve güçlü dolar altın üzerinde baskı yaratırken, Orta Doğu ve Ukrayna'daki savaş gelişmeleri ile teknoloji satışının güvenli liman talebini destekleyebilir. Altının haftalık sert düşüşün ardından toparlanması ve yakın vadede beklenen PCE verisi belirsizliği artırdığı için etki sınırlı ve zayıf negatif görünüyor.
23.11 14:01 A  SHORT SOLUSDT 1685 USD @ 72.3 (1s RSI 68, TP 69.79, SL 73.55)
23.11 14:01 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 14:01 N  NEWS (13 new) score -0.10 conf 0.40: Faiz artırımı ve sıkı Fed beklentileri ile güçlü dolar altını baskılıyor; buna karşın İran ve Ukrayna savaşlarındaki tırmanış güvenli liman talebini destekliyor. Düşen Treasury getirileri ve haftalık düşüşten toparlanma kısa vadeli alımı desteklese de, net etki hafif negatif ve belirsiz görünüyor.
23.11 14:14 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 14:14 N  NEWS (12 new) score -0.10 conf 0.35: Başlıklar karışık: güçlü dolar ve şahin Fed beklentileri (faiz artışı uyarıları) altına baskı yaparken, İran ve Ukrayna savaşlarındaki gerilim güvenli liman talebini destekliyor. Haftalık düşüşün ardından gelen toparlanma ve ABD enflasyon (PCE) verisi öncesi belirsizlik nedeniyle yön net değil, bu yüzden skor hafif negatif ve güven düşük.
23.11 14:26 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 14:26 N  NEWS (10 new) score -0.20 conf 0.40: Haberlerin ağırlığı hafif negatif: Fed'in sert duruşu ve faiz artırımı beklentileri ile güçlenen dolar altın için baskı oluşturuyor. Jeopolitik gelişmeler (Ukrayna-Rusya, İran tehditleri) güvenli liman talebini destekliyor ancak etkisi sınırlı ve büyük ölçüde fiyatlanmış durumda; ayrıca ABD enflasyon verisi (PCE) öncesi belirsizlik var.
23.11 14:38 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 14:38 N  NEWS (18 new) score -0.10 conf 0.30: Başlıklar birbiriyle çelişiyor: FOMC tutanakları doları güçlendirdiği için altında sert satış ve güçlü dolar baskısı var, ancak yüzde 2'den fazla yükselişi tetikleyen Fed faiz artırımı beklentilerinin azalması ve PCE verisi öne çıkıyor. Jeopolitik risk (İran savaşı) ise güvenli liman talebini destekleyici olsa da fonlamanın kesilmesi yönündeki haberler bu etkiyi sınırlıyor. Net etki hafif negatif, düşük güvenle değerlendirilmeli.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
