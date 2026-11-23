# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.11.2026 18:02 (İstanbul)

## Bot A — Kripto 1 saatlik trend (x1)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -31.47 $ | +73.50 $ |
| İşlem sayısı | 1 | 3 |
| Kazanma oranı | %0.0 | %66.7 |
| Ödenen komisyon/spread | 1.70 $ | 4.95 $ |

**Hesap değeri: 5,072.16 $** (başlangıç 5,000 $, +72.16 $ / %+1.44)

Açık pozisyonlar: BNBUSDT short @ 573.21 (TP 547.67 / SL 585.98)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
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

Son haber analizi (23.11 17:53): Claude puan **+0.05**, güven 0.30 — Başlıkların çoğu altın fiyatıyla doğrudan ilgili değil (Nvidia, İngiltere refah ve Pip, Belçika grevi, Gazze insani durumu). Ukrayna'nın Libya açıklarında Rus savaş gemisini vurduğu haberi küçük bir jeopolitik gerilim yaratabilir, ancak etkisi sınırlı ve kısa vadede fiyatlanmış olabilir. Merkez bankası, enflasyon veya dolar tarafında önemli yeni bir veri yok.

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
23.11 17:04 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 17:04 N  NEWS (12 new) score +0.10 conf 0.35: Haberler karışık: Kitco'nun "dolar yükselişi duraklarken altın %2'den fazla yükseldi" başlığı kısa vadede olumlu momentum gösteriyor, ancak BBH'nin Fed faiz artırımı beklentilerinin doları desteklediği ve TD'nin sağlam verilerle doları desteklediği yorumları altın için baskı oluşturuyor. İran savaşı ve ABD'deki bütçe/finansman tartışmaları ile Ukrayna'daki çatışmaların genişlemesi güvenli liman talebini sınırlı biçimde artırabilir; fakat bu riskler yeni değil ve fiyatlanmış durumda olabilir. Net etki hafif pozitif, güven düşük.
23.11 17:16 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 17:16 N  NEWS (7 new) score +0.15 conf 0.40: Altın haftalık sert düşüşün ardından toparlanıyor ve dolar yükselişi duraklıyor; bu kısa vadede altın lehine. Ancak Fed faiz artırımı beklentileri ve güçlü ABD verileri altın için baskı yaratıyor, İran savaşı ve ABD bloke etkisi ise güvenli liman talebini sınırlı destekliyor. Sinyaller karışık olduğu için temkinli bir pozitif eğilim.
23.11 17:29 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 17:29 N  NEWS (13 new) score +0.05 conf 0.20: Yeni başlıkların çoğu altını doğrudan etkilemeyen iç politika, şirket ve yerel olaylar. Ukrayna'nın Libya açıklarındaki Rus savaş gemisine saldırısı ve Gazze'ye ilişkin haberler hafif bir jeopolitik risk iştahı yaratabilir, ancak etkisi sınırlı ve büyük ölçüde fiyatlanmış. Fed, reel faiz, dolar veya enflasyonla ilgili yeni bir haber yok.
23.11 17:32 B6  GPT cevap vermedi: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 17:32 B6  karar turu: Claude «Piyasa son derece güçlü ve aşırı uzamış; olağandışı büyük hareketler nedeniyle kovalamaktan kaçınıp yalnızca seçici fırsatlara giriyorum.» / GPT «-»
23.11 17:44 B6  GPT cevap vermedi: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 17:44 B6  karar turu: Claude «Piyasa çok güçlü ama aşırı oynak bir risk iştahı rallisinde; sıkı stoplarla en mantıklı yol, büyük hareketleri kovalamak yerine geride kalan düşük oynaklıklı hisselere seçici girmek.» / GPT «-»
23.11 17:53 N  GPT news failed: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 17:53 N  NEWS (1 new) score +0.05 conf 0.30: Başlıkların çoğu altın fiyatıyla doğrudan ilgili değil (Nvidia, İngiltere refah ve Pip, Belçika grevi, Gazze insani durumu). Ukrayna'nın Libya açıklarında Rus savaş gemisini vurduğu haberi küçük bir jeopolitik gerilim yaratabilir, ancak etkisi sınırlı ve kısa vadede fiyatlanmış olabilir. Merkez bankası, enflasyon veya dolar tarafında önemli yeni bir veri yok.
23.11 17:56 B6  GPT cevap vermedi: OpenAI account problem: 401 expired_secret_key: Your API key has expired. Create a new API key to continue.
23.11 17:56 B6  karar turu: Claude «Piyasa çok güçlü bir yükseliş gününde ve oynaklık aşırı; büyük hareketleri kovalamak yerine istikrarlı trendlerde seçici uzun pozisyonlar tercih ediliyor.» / GPT «-»
23.11 18:02 A  SHORT BNBUSDT 1674 USD @ 573.2 (1s RSI 65, TP 547.7, SL 586)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
