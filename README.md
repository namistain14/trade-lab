# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 24.11.2026 10:13 (İstanbul)

## Bot A — Kripto 1 saatlik trend (x1)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +72.47 $ | +145.97 $ |
| İşlem sayısı | 1 | 4 |
| Kazanma oranı | %100.0 | %75.0 |
| Ödenen komisyon/spread | 1.64 $ | 6.58 $ |

**Hesap değeri: 5,145.97 $** (başlangıç 5,000 $, +145.97 $ / %+2.92)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 24.11 06:06 | BNBUSDT | short | +72.47 $ | take profit |
| 23.11 16:57 | SOLUSDT | short | -31.47 $ | stop |
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

Son haber analizi (24.11 10:13): Claude puan **+0.05**, güven 0.40 — Jeopolitik risk (Polonya'ya füze düşmesi, NATO AWACS sevkiyatı, Hormuz'da mayın ve İran savaşı) altın için güvenli liman talebini destekliyor. Ancak doların 19-20 aylık zirvesi, Fed faiz artırımı beklentilerinin güçlenmesi ve yaklaşan ABD PCE verisi altın üzerinde baskı yaratabilir; bu nedenle net etki hafif pozitif ile nötr arasında kalıyor.

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
24.11 08:48 N  NEWS (14 new) score -0.05 conf 0.30: Hormuz'daki mayın olayları ve Pentagon'un Patriot sevkiyatlarını geciktirmesi jeopolitik risk primini destekliyor, ancak Fed faiz artırımı beklentileri ve riskli varlık iştahını artıran AI rallisi altın için baskılayıcı. Gelecek PCE enflasyon verisi belirsizliği artırdığından yön net değil; haberler çelişkili olduğu ve bir kısmı zaten fiyatlanmış olduğu için güven düşük.
24.11 09:00 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
24.11 09:00 N  NEWS (15 new) score +0.10 conf 0.35: Jeopolitik riskler (Hürmüz'de mayın, İran savaşı riski, Ukrayna'ya Patriot gecikmesi) altın için güvenli liman desteği sağlıyor, ancak Fed'in faiz artırımı beklentileri ve ABD doları endeksinin 104,50 civarında dirençli seyretmesi bunu dengeliyor. Altın yeniden toparlanıyor, fakat bu toparlanma hisse senedi piyasasındaki iyileşmeyle ilişkili görünüyor; sinyaller karışık olduğu için yön belirsiz ve güven düşük.
24.11 09:12 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
24.11 09:12 N  NEWS (16 new) score -0.25 conf 0.40: Fed faiz artırımı beklentilerinin yükselmesi ve güçlü dolar altın için baskı yaratıyor; AI kaynaklı risk iştahı da güvenli liman talebini azaltıyor. İran ve Hürmüz gerilimi gibi jeopolitik riskler ise altını destekleyebilecek olsa da piyasa bu riskleri büyük ölçüde fiyatlamış görünüyor, bu nedenle sinyal karışık ve orta düzeyde negatif.
24.11 09:24 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
24.11 09:24 N  NEWS (14 new) score +0.10 conf 0.35: Jeopolitik risk (Hürmüz'de mayın olayları, İran savaşı riski, yaptırımlar) ve borsa satışının Fed 'put' beklentisini canlandırması altın için hafif destekleyici; ancak AI kaynaklı yükseliş Fed faiz artırımı beklentilerini ve doları güçlendirerek altı baskılıyor, ABD enflasyon verisi öncesi belirsizlik yüksek. Karışık sinyaller nedeniyle yön net değil, güven düşük.
24.11 09:37 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
24.11 09:37 N  NEWS (14 new) score -0.20 conf 0.40: Dolar 20 aylık zirvesine yakın seyrediyor ve AI rallisi Fed faiz artırımı beklentilerini güçlendiriyor; bu, altın için kısa vadede baskı yaratıyor. Hormuz'da mayın olayları, İran yaptırımları ve Rusya'ya yeni AP yaptırım paketi gibi jeopolitik gerilim ise güvenli liman talebini destekliyor; ancak bu haberlerin büyük kısmı zaten fiyatlanmış durumda, bu yüzden etkisi sınırlı kalıyor. ABD enflasyon verisi (PCE) öncesi belirsizlik de yön konusunda net bir sinyal vermiyor.
24.11 09:49 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
24.11 09:49 N  NEWS (14 new) score -0.10 conf 0.40: Jeopardi tarafta İran/Hürmüz gerilimi ve yeni yaptırımlar jeopolitik talebi destekliyor, ancak dolar 20 aylık zirveye yakın ve AI rallisi Fed faiz artırımı beklentilerini güçlendirdiği için reel faiz ve dolar baskısı altın üzerinde ağır basıyor. Net etki hafif negatif; ayrıca haberlerin çoğu tekrar niteliğinde olduğundan güven sınırlı.
24.11 10:01 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
24.11 10:01 N  NEWS (23 new) score -0.30 conf 0.50: Dolar 20 aylık zirveye yakın seyrediyor ve AI rallisi Fed faiz artırımı beklentilerini güçlendiriyor; bu, reel faizleri ve doları yukarı iterek altın için olumsuz. Ancak altın son günlerde toparlanma sinyali veriyor ve PCE enflasyon verisi öncesi piyasa kararsız, bu yüzden sinyal orta düzeyde ve güven sınırlı.
24.11 10:13 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
24.11 10:13 N  NEWS (34 new) score +0.05 conf 0.40: Jeopolitik risk (Polonya'ya füze düşmesi, NATO AWACS sevkiyatı, Hormuz'da mayın ve İran savaşı) altın için güvenli liman talebini destekliyor. Ancak doların 19-20 aylık zirvesi, Fed faiz artırımı beklentilerinin güçlenmesi ve yaklaşan ABD PCE verisi altın üzerinde baskı yaratabilir; bu nedenle net etki hafif pozitif ile nötr arasında kalıyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
