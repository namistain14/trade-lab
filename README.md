# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 05.11.2026 00:30 (İstanbul)

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
| Net kâr/zarar | +0.00 $ | -112.88 $ |
| İşlem sayısı | 0 | 40 |
| Kazanma oranı | %0.0 | %42.5 |
| Ödenen komisyon/spread | 0.00 $ | 475.49 $ |

**Hesap değeri: 4,889.33 $** (başlangıç 5,000 $, -110.67 $ / %-2.21)

Açık pozisyonlar: PAXGUSDT long @ 4058.22 (TP 4070.40 / SL 4050.11)

Son haber analizi (05.11 00:27): Claude puan **+0.25**, güven 0.40 — Dolar zayıflaması ve petrol fiyatlarındaki sert düşüşün enflasyon beklentilerini aşağı çekmesi altı destekliyor; ancak İran savaşının sona erme ihtimali jeopolitik güvenli liman primini azaltıyor. Haberlerin çoğu zaten fiyatlanmış olduğu için güven orta-düşük tutuldu.

GPT (gpt-6-luna): puan **+0.55**, güven 0.58 — İran’ın Qeşm Adası’na yönelik yeni ABD saldırısı kısa vadede güvenli liman talebini artırabilir; doların iki ayın dibine gerilemesi de altını destekliyor. Ancak savaşın sona erebileceği beklentisi ve petrol düşüşü bu desteği sınırlıyor; haber akışı çelişkili olduğundan güven orta düzeyde.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 04.11 21:43 | PAXGUSDT | long | -55.99 $ | stop (gap) |
| 04.11 19:39 | PAXGUSDT | long | +69.06 $ | take profit |
| 04.11 17:56 | PAXGUSDT | long | -55.92 $ | stop |
| 04.11 17:40 | PAXGUSDT | long | +69.06 $ | take profit |
| 04.11 16:18 | PAXGUSDT | long | -55.92 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +66.43 $ |
| İşlem sayısı | 0 | 1 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 17.17 $ |

**Hesap değeri: 5,066.43 $** (başlangıç 5,000 $, +66.43 $ / %+1.33)

Son haber analizi (04.11 13:40): Claude puan **+0.15**, güven 0.40 — Haberler çelişkili: İran'ın Hürmüz'de dört tankerin mayınlarla vurulduğunu öne sürmesi ve petrol fiyatlarındaki Hürmüz arz riskleri fiyatı yukarı iter; buna karşılık Brent'in İran müzakereleri nedeniyle 4 haftalık dibe inmesi ve ABD-İran arasında anlaşmanın hâlâ uzak olması aşağı yönlü baskı yaratır. Tanker iddiası doğrulanmamış olduğu için net etki hafif pozitif, güven düşük.

GPT (gpt-6-luna): puan **+0.35**, güven 0.43 — Hürmüz’de dört tankerin mayına çarptığı iddiası ve İran-ABD görüşmelerindeki tıkanma, kısa vadeli arz riskini artırarak Brent’i destekleyebilir. Ancak tanker haberleri henüz doğrulanmış değil ve Brent’in görüşmeler beklentisiyle gerilediğine dair çelişkili başlıklar yükseliş etkisini sınırlıyor.

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

**Hesap değeri: 105,886.16 $** (başlangıç 100,000 $, +5886.16 $ / %+5.89)

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
04.11 23:33 N  NEWS (11 new) score +0.20 conf 0.40: 
04.11 23:33 N  GPT  score +0.35 conf 0.48: İran’ın Qeşm Adası’na yönelik ABD saldırısı kısa vadede güvenli liman talebini destekleyebilir; ancak Trump’ın savaş riskini küçümsemesi ve petrolün düşüşü tırmanmanın sınırlanacağı beklentisini güçlendiriyor. Demokratların seçim zaferiyle altının zaten 4.000 doların üzerine çıktığına dair haber, bu
04.11 23:39 B6  CLOSE short NVDA take profit: +1575.42 USD
04.11 23:45 N  NEWS (6 new) score +0.30 conf 0.50: 
04.11 23:45 N  GPT  score +0.35 conf 0.52: Doların seçim sonrası gerilemesi ve İran’daki yeni saldırı haberi altına kısa vadede destek sağlayabilir. Ancak savaş riskinin azalacağı beklentisi, düşen petrol fiyatları ve haberlerin bir kısmının zaten fiyatlanmış olması yükseliş görünümünü sınırlıyor.
04.11 23:45 B6  CLOSE long AAPL seans sonu: -505.78 USD
04.11 23:45 B6  CLOSE long QQQ seans sonu: -222.60 USD
04.11 23:45 B6  CLOSE long SPY seans sonu: +485.08 USD
04.11 23:45 B6  seans kapanışı: tüm pozisyonlar kapatıldı
04.11 23:57 N  NEWS (7 new) score +0.20 conf 0.40: Dolar zayıflaması ve petrol fiyatlarındaki sert düşüşün enflasyon beklentilerini aşağı çekmesi altı destekliyor; ancak İran savaşının sona erme ihtimali jeopolitik güvenli liman primini azaltıyor. Haberlerin çoğu zaten fiyatlanmış olduğu için güven orta-düşük tutuldu.
04.11 23:57 N  GPT  score +0.35 conf 0.58: Demokratların zaferi sonrası doların gerilemesi ve altının 4.000 doların üzerine çıktığı haberleri kısa vadede destekleyici. İran savaşının sona erebileceği beklentisi petrolü ve güvenli liman talebini aşağı çekebilir; yeni İran yaptırımları ve çelişkili etkiler yükseliş beklentisini sınırlıyor.
05.11 00:15 N  NEWS (5 new) score +0.25 conf 0.40: 
05.11 00:15 N  GPT  score +0.35 conf 0.58: Doların seçim sonrası gerilemesi ve altının yükseldiğine dair haberler kısa vadede altını destekliyor. Ancak İran savaşının sona erebileceği beklentisi güvenli liman talebini azaltabilir; petrol düşüşü ve olası yeni gerilim haberleri görünümü karışık kılıyor.
05.11 00:27 N  NEWS (9 new) score +0.25 conf 0.40: 
05.11 00:27 N  GPT  score +0.55 conf 0.58: İran’ın Qeşm Adası’na yönelik yeni ABD saldırısı kısa vadede güvenli liman talebini artırabilir; doların iki ayın dibine gerilemesi de altını destekliyor. Ancak savaşın sona erebileceği beklentisi ve petrol düşüşü bu desteği sınırlıyor; haber akışı çelişkili olduğundan güven orta düzeyde.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
