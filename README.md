# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 04.11.2026 16:28 (İstanbul)

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
| Net kâr/zarar | +203.67 $ | -139.08 $ |
| İşlem sayısı | 12 | 36 |
| Kazanma oranı | %58.3 | %41.7 |
| Ödenen komisyon/spread | 142.49 $ | 428.08 $ |

**Hesap değeri: 4,860.92 $** (başlangıç 5,000 $, -139.08 $ / %-2.78)

Son haber analizi (04.11 16:20): Claude puan **+0.50**, güven 0.50 — Dolar endeksi, ABD ara seçim sonuçlarının ardından dört haftalık dibe yakın geriledi ve bu altını destekliyor. Ayrıca ABD'nin İran'ın Qeshm Adası'nı vurduğu haberi jeopolitik risk primini artırarak güvenli liman talebini canlandırabilir. Ancak dolar düşüşü ve seçim sonucu kısmen fiyatlanmış durumda, bu nedenle güven orta düzeyde tutuldu.

GPT (gpt-6-luna): puan **+0.68**, güven 0.62 — Qeshm Adası’na ABD saldırısı ve Yemen’deki ölümcül saldırı yakın vadeli güvenli liman talebini artırabilir; doların dört haftalık dipleri test etmesi de altını destekliyor. Ancak seçim kaynaklı hareketlerin büyük ölçüde fiyatlanmış olma ihtimali ve haber akışındaki çelişkiler güveni sınırlıyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 04.11 16:18 | PAXGUSDT | long | -55.92 $ | stop |
| 04.11 15:32 | PAXGUSDT | long | +69.06 $ | take profit |
| 04.11 14:58 | PAXGUSDT | long | -55.92 $ | stop |
| 04.11 12:17 | PAXGUSDT | long | +69.06 $ | take profit |
| 04.11 11:07 | PAXGUSDT | long | +69.05 $ | take profit |

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
| Net kâr/zarar | +0.00 $ | -167.93 $ |
| İşlem sayısı | 0 | 6 |
| Kazanma oranı | %0.0 | %16.7 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 102,491.32 $** (başlangıç 100,000 $, +2491.32 $ / %+2.49)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 03.11 23:48 | QQQ | long | -62.06 $ | seans sonu |
| 03.11 18:34 | AAPL | long | -859.05 $ | stop |
| 02.11 23:51 | TSLA | long | -1109.17 $ | seans sonu |
| 02.11 23:48 | NVDA | short | +5136.86 $ | seans sonu |
| 02.11 23:45 | AAPL | long | -3118.15 $ | seans sonu |

## Son olaylar

```
04.11 14:58 B5  CLOSE long stop: -55.92 USD
04.11 15:09 N  NEWS (12 new) score +0.50 conf 0.55: Demokratların Kongre'yi kazanmasıyla dolar zayıfladı, dolar endeksi bir aylık dibe indi ve Treasury getirileri geriledi; bu altın için net olarak destekleyici. Ancak altın zaten 4.000 doları aştığı için bir kısmı fiyatlanmış durumda ve bazı yorumlar yükselişin sona erebileceğini belirtiyor, bu da güveni sınırlıyor.
04.11 15:09 N  GPT  score +0.55 conf 0.58: Demokratların seçim zaferi sonrası doların gerilemesi ve tahvil rallisinin getirileri düşürmesi altını kısa vadede destekliyor; İran savaşı kaynaklı belirsizlik de güvenli liman talebini artırabilir. Ancak altın 4.000 dolar seviyesini zaten yeniden aşmış görünüyor ve haberler büyük ölçüde aynı geliş
04.11 15:09 B5  LONG gold 25000 USD x10 @ 4034.77 (TP 4046.87, SL 4026.70; news +0.53)
04.11 15:21 N  NEWS (9 new) score +0.40 conf 0.55: Demokratların Kongre zaferi doların bir aylık en düşük seviyesine gerilemesine ve Hazine tahvil getirilerinin düşmesine yol açtı; bu, altın için olumlu bir etkidir. ABD'nin İran'ın Qeshm Adası'nı vurması jeopolitik risk primini artırıyor, ancak Trump'ın riskleri yatıştırma mesajı bu etkiyi sınırlıyor ve haberlerin bir kısmı zaten fiyatlanmış olabilir.
04.11 15:21 N  GPT  score +0.68 conf 0.67: İran’ın Qeşm Adası’na yönelik ABD saldırısı kısa vadeli güvenli liman talebini artırabilir; Trump’ın savaş risklerini küçümsemesi bu etkiyi sınırlıyor. Dolar ve Hazine getirilerindeki düşüş de altını destekliyor, ancak seçim kaynaklı hareketin bir kısmı fiyatlanmış görünüyor.
04.11 15:33 B5  CLOSE long take profit: +69.06 USD
04.11 15:33 N  NEWS (17 new) score +0.30 conf 0.45: Dolar endeksi bir aylık dip seviyesine geriliyor ve Demokratların kongre zaferi Treasury getirilerini baskılıyor; bu, altın için olumlu bir makro tablo. Öte yandan İran savaşına karşı oy sinyali jeopolitik risk primini azaltabileceğinden güvenli liman talebi kısmen zayıflayabilir ve haberlerin birçoğu zaten fiyatlanmış durumda, bu nedenle güven sınırlı.
04.11 15:33 N  GPT  score +0.42 conf 0.57: Demokratların ara seçimlerdeki başarısının doları ve Hazine tahvil getirilerini aşağı çektiğine dair haberler, kısa vadede altını destekliyor. Ancak seçim sonucu büyük ölçüde fiyatlanmış olabilir; İran’la ilgili haberler de net bir gerilimsizleşme sinyali vermiyor.
04.11 15:39 B5  LONG gold 25000 USD x10 @ 4039.62 (TP 4051.74, SL 4031.54; news +0.36)
04.11 15:45 N  NEWS (10 new) score +0.35 conf 0.50: ABD ara seçimlerinde Demokratların güçlenmesi doların bir aylık en düşük seviyeye gerilemesine ve Treasury getirilerinin baskılanmasına yol açtı; bu, altın için olumlu bir etki. Ancak İran ile müzakere beklentileri jeopolitik korku primini azaltabileceği için etki sınırlı ve kısa vadede karışık.
04.11 15:45 N  GPT  score +0.32 conf 0.46: Demokratların ara seçim zaferi sonrası doların ve Hazine getirilerinin gerilemesi altını kısa vadede destekliyor; altının 4.000 dolar üzerine dönmesi bu gelişmelerin bir kısmının zaten fiyatlandığını gösteriyor. İran başlıkları yeni ve belirgin bir tırmanış işareti vermediğinden ek güvenli liman des
04.11 16:20 B5  CLOSE long stop: -55.92 USD
04.11 16:20 N  NEWS (27 new) score +0.50 conf 0.50: Dolar endeksi, ABD ara seçim sonuçlarının ardından dört haftalık dibe yakın geriledi ve bu altını destekliyor. Ayrıca ABD'nin İran'ın Qeshm Adası'nı vurduğu haberi jeopolitik risk primini artırarak güvenli liman talebini canlandırabilir. Ancak dolar düşüşü ve seçim sonucu kısmen fiyatlanmış durumda, bu nedenle güven orta düzeyde tutuldu.
04.11 16:20 N  GPT  score +0.68 conf 0.62: Qeshm Adası’na ABD saldırısı ve Yemen’deki ölümcül saldırı yakın vadeli güvenli liman talebini artırabilir; doların dört haftalık dipleri test etmesi de altını destekliyor. Ancak seçim kaynaklı hareketlerin büyük ölçüde fiyatlanmış olma ihtimali ve haber akışındaki çelişkiler güveni sınırlıyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
