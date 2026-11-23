# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.11.2026 15:45 (İstanbul)

## Bot A — Kripto 1 saatlik trend (x1)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +104.97 $ |
| İşlem sayısı | 0 | 2 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 3.25 $ |

**Hesap değeri: 5,108.75 $** (başlangıç 5,000 $, +108.75 $ / %+2.18)

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

Son haber analizi (23.11 15:38): Claude puan **-0.10**, güven 0.35 — Haberler karışık: Aralık'ta Fed faiz artırımı ihtimali ve doların 19 aylık zirveye yakın seyri altın için baskı yaratıyor, altın da 9/2/25'ten bu yana en düşük seviyeden açıldı. Buna karşılık Ukrayna savaşının genişlemesi, İran savaş fonlaması tartışması ve borsa satışlarından doğan güvenli liman talebi destek sağlayabilir; bu nedenle etki hafif negatif kabul edildi ve güven düşük tutuldu.

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
23.11 14:14 N  NEWS (12 new) score -0.10 conf 0.35: Başlıklar karışık: güçlü dolar ve şahin Fed beklentileri (faiz artışı uyarıları) altına baskı yaparken, İran ve Ukrayna savaşlarındaki gerilim güvenli liman talebini destekliyor. Haftalık düşüşün ardından gelen toparlanma ve ABD enflasyon (PCE) verisi öncesi belirsizlik nedeniyle yön net değil, bu yüzden skor hafif negatif ve güven düşük.
23.11 14:26 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 14:26 N  NEWS (10 new) score -0.20 conf 0.40: Haberlerin ağırlığı hafif negatif: Fed'in sert duruşu ve faiz artırımı beklentileri ile güçlenen dolar altın için baskı oluşturuyor. Jeopolitik gelişmeler (Ukrayna-Rusya, İran tehditleri) güvenli liman talebini destekliyor ancak etkisi sınırlı ve büyük ölçüde fiyatlanmış durumda; ayrıca ABD enflasyon verisi (PCE) öncesi belirsizlik var.
23.11 14:38 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 14:38 N  NEWS (18 new) score -0.10 conf 0.30: Başlıklar birbiriyle çelişiyor: FOMC tutanakları doları güçlendirdiği için altında sert satış ve güçlü dolar baskısı var, ancak yüzde 2'den fazla yükselişi tetikleyen Fed faiz artırımı beklentilerinin azalması ve PCE verisi öne çıkıyor. Jeopolitik risk (İran savaşı) ise güvenli liman talebini destekleyici olsa da fonlamanın kesilmesi yönündeki haberler bu etkiyi sınırlıyor. Net etki hafif negatif, düşük güvenle değerlendirilmeli.
23.11 14:50 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 14:50 N  NEWS (7 new) score +0.05 conf 0.30: 
23.11 15:02 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 15:02 N  NEWS (10 new) score +0.05 conf 0.30: Haberler karışık: Warsh yönetiminde Fed 'put' beklentisi ve ABD PCE enflasyon verisi altın için destekleyici olabilir, ancak DXY'nin yükselişi, zayıf Avro bölgesi/İngiltere PMI verileri ve 14 aylık en düşük seviyeden gelen zayıf trend altını baskılıyor. İran ve Ukrayna çatışmaları güvenli liman talebini artırsa da bunlar büyük ölçüde fiyatlanmış durumda; net etki sınırlı ve yön belirsiz.
23.11 15:14 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 15:14 N  NEWS (20 new) score -0.20 conf 0.40: Dolar 19 aylık zirvesinden hafif geri çekilse de güçlü kalması ve HSBC'nin 2027'ye dair güçlü dolar görünümü altın için baskı yaratıyor. Savaş haberleri (İran, Ukrayna) güvenli liman talebini destekliyor ancak büyük ölçüde fiyatlanmış durumda; PCE enflasyon verisi ve Warsh Fed'i yönündeki belirsizlik ise net bir yön vermiyor.
23.11 15:26 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 15:26 N  NEWS (11 new) score -0.15 conf 0.35: Dolar 19 aylık zirvesine yakın seyrediyor ve Aralık ayında Fed faiz artırımı ihtimali gündeme geliyor; bu, altın için kısa vadede baskı yaratıyor. Savaş haberleri (İran, Ukrayna, Libya) güvenli liman talebini destekleyebilir, ancak çoğu eski ve büyük ölçüde fiyatlanmış olduğundan etkisi sınırlı kalıyor. PCE enflasyon verisi beklenirken olası bir sürpriz, ana belirleyici olacak.
23.11 15:38 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 15:38 N  NEWS (18 new) score -0.10 conf 0.35: Haberler karışık: Aralık'ta Fed faiz artırımı ihtimali ve doların 19 aylık zirveye yakın seyri altın için baskı yaratıyor, altın da 9/2/25'ten bu yana en düşük seviyeden açıldı. Buna karşılık Ukrayna savaşının genişlemesi, İran savaş fonlaması tartışması ve borsa satışlarından doğan güvenli liman talebi destek sağlayabilir; bu nedenle etki hafif negatif kabul edildi ve güven düşük tutuldu.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
