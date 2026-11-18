# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 18.11.2026 03:37 (İstanbul)

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
| Net kâr/zarar | +138.07 $ | -372.62 $ |
| İşlem sayısı | 2 | 116 |
| Kazanma oranı | %100.0 | %42.2 |
| Ödenen komisyon/spread | 23.92 $ | 1378.53 $ |

**Hesap değeri: 4,627.38 $** (başlangıç 5,000 $, -372.62 $ / %-7.45)

Son haber analizi (18.11 03:28): Claude puan **-0.50**, güven 0.60 — Altın 14 aylık dip yakınında, faiz artırımı beklentileri ve güçlenen dolar baskı oluşturuyor; jeopolitik risk (İran savaşı, Qeshm saldırısı) güvenli liman talebi yaratsa da mevcut haber akışında etkisi baskılanmış görünüyor. Güçlü dolar ve sıkılaşma beklentisi kısa vadede altı aşağı çekme eğiliminde, ancak haberlerin bir kısmı eski/fiyatlanmış ve dolar geri çekilmeleri toparlanma ihtimalini de koruyor.

GPT (gpt-6-luna): puan **-0.28**, güven 0.58 — Son haberlerde doların güçlenmesiyle altın ve gümüşte sert düşüş bildirilmesi, ayrıca faiz artışı baskısının altını 14 ayın diplerine yakın tutması kısa vadede aşağı yönlü. ABD’nin İran’daki IRGC füze mevzisini vurması güvenli liman talebini destekleyebilir ve düşüşü sınırlayabilir.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 18.11 03:35 | PAXGUSDT | short | +69.03 $ | take profit |
| 18.11 03:13 | PAXGUSDT | short | +69.04 $ | take profit |
| 17.11 21:41 | PAXGUSDT | long | -55.96 $ | stop |
| 13.11 19:25 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 18:39 | PAXGUSDT | short | +69.05 $ | take profit |

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

**Hesap değeri: 112,393.69 $** (başlangıç 100,000 $, +12393.69 $ / %+12.39)

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
18.11 02:27 N  NEWS (6 new) score -0.15 conf 0.30: Yeni haberlerin çoğu altın için nötr: altın 3.850 dolar civarında sabit ve FOMC tutanakları öncesinde bekliyor. Güçlü dolar, sıkılaşma (faiz artırımı) beklentileri ve sıcak CPI verisi baskı yaratıyor; İran savaşı ise güvenli liman talebini destekliyor ama büyük ölçüde fiyatlanmış durumda. Net görünüm hafif negatif, güven düşük.
18.11 02:27 N  GPT  score +0.08 conf 0.32: İran savaşıyla ilgili önceki haberler güvenli liman talebini destekleyebilir; ancak yeni başlıklar altın için güçlü ve doğrudan bir katalizör sunmuyor. FOMC tutanakları öncesinde altının yatay seyretmesi ve dolar/faiz görünümündeki karışıklık etkiyi sınırlıyor.
18.11 02:39 N  NEWS (12 new) score -0.15 conf 0.40: Fed faiz artırımı beklentilerinin sürmesi ve güçlü dolar altın üzerinde baskı oluşturuyor; altın yıllık dip seviyelerine yakın işlem görüyor. İran'daki çatışmaların (Qeshm saldırısı) güvenli liman talebini artırma ihtimali ise sınırlı bir destek sağlıyor, ancak savaş haberlerinin büyük kısmı zaten fiyatlanmış durumda ve haberler çelişkili olduğu için güven düşük.
18.11 02:39 N  GPT  score +0.24 conf 0.42: İran’daki füze sahasına yönelik ABD saldırısı ve savaşın sürebileceğine dair haberler kısa vadede güvenli liman talebini destekleyebilir; doların geri çekilmesi de altın için hafif olumlu. Ancak süregelen Fed faiz artırımı beklentileri ve altının zayıf seyri bu etkiyi sınırlıyor.
18.11 02:51 N  NEWS (5 new) score -0.40 conf 0.45: Yeni başlıklar güçlü enflasyon verisi ve Fed faiz artırımı beklentilerinin sürdüğünü gösteriyor; bu, reel faizleri ve doları yukarı iten, altın için baskılayıcı bir etkidir. Savaş kaynaklı güvenli liman talebi ise sınırlı ve eski haberlerle zayıf, çelişkili sinyaller veriyor, bu yüzden güven düşük tutuldu.
18.11 02:51 N  GPT  score -0.12 conf 0.31: Güçlü enflasyon verisi ve Fed faiz artırımı beklentileri altın için hafif olumsuz; doların geri çekilmesi ise bu baskıyı kısmen dengeliyor. Yeni başlıkların çoğu altın açısından doğrudan etkisiz ve haber akışı çelişkili olduğundan kısa vadeli yön sinyali zayıf.
18.11 03:03 N  NEWS (4 new) score -0.40 conf 0.50: Sıcak CPI verisi sonrası doların yıllık zirvelere yönelmesi ve Fed faiz artırımı beklentilerinin sürmesi altın için baskı oluşturuyor; altın yakın zamanda bir yıllık dibe yakın işlem görüyor. İran savaşı güvenli liman talebini destekleyebilir, ancak bu etki fiyatlanmış görünüyor ve dolardaki geri çekilme kısa vadeli toparlanma sinyali veriyor. Çelişkili ve eski başlıklar (5.600$ hedefleri gibi) nedeniyle güven orta seviyede tutuldu.
18.11 03:03 N  GPT  score -0.12 conf 0.30: Doların geri çekilmesi altına kısa vadeli destek sağlayabilir; ancak sıcak enflasyon, faiz artırımı beklentileri ve altının zayıf seyri bu desteği sınırlıyor. Yeni haberlerde altın için belirleyici, büyük bir gelişme yok; görünüm hafif aşağı yönlü ve belirsiz.
18.11 03:12 B5  CLOSE short take profit: +69.04 USD
18.11 03:15 N  NEWS (3 new) score -0.20 conf 0.40: Altın, Fed faiz artırımı beklentileri ve güçlü dolar nedeniyle baskı altında; yakın vadede bu ağırlıklı olarak negatif. Buna karşın İran savaşı ve jeopolitik gerilim güvenli liman talebini destekliyor, dolar da son saatlerde geri çekiliyor; bu nedenle sinyal zayıf ve karışık.
18.11 03:15 N  GPT  score +0.12 conf 0.28: Doların geri çekilmesi altına kısa vadeli destek sağlayabilir; ancak Fed’in faiz artırımı beklentileri ve altındaki genel zayıflık bu etkiyi sınırlıyor. Yeni başlıkların çoğu piyasa açısından önemsiz olduğundan yön sinyali zayıf.
18.11 03:28 N  NEWS (9 new) score -0.50 conf 0.60: Altın 14 aylık dip yakınında, faiz artırımı beklentileri ve güçlenen dolar baskı oluşturuyor; jeopolitik risk (İran savaşı, Qeshm saldırısı) güvenli liman talebi yaratsa da mevcut haber akışında etkisi baskılanmış görünüyor. Güçlü dolar ve sıkılaşma beklentisi kısa vadede altı aşağı çekme eğiliminde, ancak haberlerin bir kısmı eski/fiyatlanmış ve dolar geri çekilmeleri toparlanma ihtimalini de koruyor.
18.11 03:28 N  GPT  score -0.28 conf 0.58: Son haberlerde doların güçlenmesiyle altın ve gümüşte sert düşüş bildirilmesi, ayrıca faiz artışı baskısının altını 14 ayın diplerine yakın tutması kısa vadede aşağı yönlü. ABD’nin İran’daki IRGC füze mevzisini vurması güvenli liman talebini destekleyebilir ve düşüşü sınırlayabilir.
18.11 03:28 B5  SHORT gold 25000 USD x10 @ 3824.90 (TP 3813.43, SL 3832.55; news -0.39)
18.11 03:37 B5  CLOSE short take profit: +69.03 USD
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
