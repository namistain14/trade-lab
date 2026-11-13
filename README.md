# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 13.11.2026 08:22 (İstanbul)

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
| Net kâr/zarar | -111.95 $ | -387.63 $ |
| İşlem sayısı | 2 | 103 |
| Kazanma oranı | %0.0 | %41.7 |
| Ödenen komisyon/spread | 23.86 $ | 1223.31 $ |

**Hesap değeri: 4,612.37 $** (başlangıç 5,000 $, -387.63 $ / %-7.75)

Son haber analizi (13.11 08:19): Claude puan **-0.60**, güven 0.70 — Altın 13 aylık dip seviyesine yakın işlem görüyor; ABD doları endeksi 19 aylık zirvesine yakın ve Fed faiz artırımı beklentileri güçleniyor, petrol kaynaklı enflasyon endişeleri de baskıyı artırıyor. İran'ın ABD radar sahasını hedef aldığını bildirmesi güvenli liman talebi açısından destekleyici olsa da, bu gelişme dolar ve faiz kaynaklı baskının gerisinde kalıyor; yakın vadede etki negatif görünüyor.

GPT (gpt-6-luna): puan **-0.25**, güven 0.56 — Yeni başlıkların çoğu altın fiyatını etkileyebilecek somut bir gelişme içermiyor. İran kaynaklı gerilim güvenli liman talebini desteklese de güçlü dolar, Fed’in faiz artırımı beklentileri ve altındaki düşüş eğilimi önümüzdeki saatlerde baskın görünüyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 13.11 08:18 | PAXGUSDT | short | -55.97 $ | stop |
| 13.11 03:05 | PAXGUSDT | short | -55.98 $ | stop |
| 12.11 21:37 | PAXGUSDT | short | -56.18 $ | stop (gap) |
| 12.11 19:56 | PAXGUSDT | short | -55.98 $ | stop |
| 12.11 19:06 | PAXGUSDT | short | -55.98 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -123.04 $ |
| İşlem sayısı | 0 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 0.00 $ | 70.51 $ |

**Hesap değeri: 4,876.96 $** (başlangıç 5,000 $, -123.04 $ / %-2.46)

Son haber analizi (12.11 07:59): Claude puan **-0.15**, güven 0.40 — Başlıklar karışık: ABD-İran barış görüşmesi umutları, Brent'in 92 doların altına inmesi ve Suudi üretim artışı fiyatı aşağı çekiyor, ancak Hormuz'da mayına çarpan tanker, İran'ın misilleme tehditleri ve barış görüşmelerinin tıkanması ciddi bir yukarı risk oluşturuyor. Bu çelişkiler ve bazı haberlerin eski veya zaten fiyatlanmış olması nedeniyle yön sinyali zayıf ve güven düşük.

GPT (gpt-6-luna): puan **-0.35**, güven 0.56 — Barış görüşmesi umutları, Suudi üretimindeki artış ve OPEC+ ihracatının savaş öncesi seviyelere yaklaşması yakın vadede arz endişelerini azaltıp Brent üzerinde baskı kuruyor. Hürmüz’deki mayın/tanker haberleri ve İran’ın misilleme tehdidi düşüşü sınırlıyor; haber akışının bir kısmı doğrulanmamış vey

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
| Net kâr/zarar | +0.00 $ | +10683.69 $ |
| İşlem sayısı | 0 | 44 |
| Kazanma oranı | %0.0 | %52.3 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 113,945.80 $** (başlangıç 100,000 $, +13945.80 $ / %+13.95)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 12.11 23:46 | SPY | long | -466.64 $ | seans sonu |
| 12.11 23:46 | QQQ | long | +93.52 $ | seans sonu |
| 12.11 23:21 | TSLA | long | +774.55 $ | take profit |
| 12.11 21:50 | NVDA | long | -834.20 $ | stop |
| 12.11 20:38 | AAPL | long | -1155.20 $ | stop |

## Son olaylar

```
13.11 07:30 N  NEWS (5 new) score -0.40 conf 0.60: Dolar endeksinin 19 aylık zirvede olması ve Fed faiz artırımı beklentileri altın için baskılayıcı; ABD tahvil getirilerindeki yükseliş de reel faiz kanalıyla altı olumsuz etkiliyor. İran'ın ABD radar tesisini hedef aldığı haberi ve Ukrayna/Orta Doğu gerilimleri sınırlı bir güvenli liman desteği sağlasa da, bu etki dolar ve faiz baskısının gerisinde kalıyor; ayrıca altının yeni dip seviyelerden toparlanma sinyali vermesi kısa vadeli düşüşün bir kısmını sınırlıyor.
13.11 07:30 N  GPT  score -0.30 conf 0.46: DXY’nin Fed beklentileriyle 103 üzerinde tutunması kısa vadede altın üzerinde baskı yaratıyor. Houthi üretimini durdurmaya yönelik BM adımı gerilimi sınırlayabilir; ancak bölgesel riskler ve yaklaşan ABD verileri aşağı yönlü görünümü belirsizleştiriyor.
13.11 07:43 N  NEWS (8 new) score -0.60 conf 0.70: Altın, Fed faiz artırımı beklentileri, dolar endeksinin 19 aylık zirvelere yakın seyri ve petrol kaynaklı enflasyon endişeleri nedeniyle baskı altında; reel faiz ve dolar kanalı altın için belirgin olumsuz. İran ve Ukrayna gelişmeleri jeopolitik risk primi sağlasa da bu etkiyi bastıracak düzeyde değil; ayrıca ABD PPI verisi kısa vadede oynaklık yaratabilir.
13.11 07:43 N  GPT  score -0.58 conf 0.70: Petrolün toparlanmasının enflasyon ve Fed’in faiz artırımı beklentilerini güçlendirdiği haberleri ile doların güçlü seyri, kısa vadede altın üzerinde baskı yaratıyor. İran kaynaklı riskler ve olası PPI verisi bu görünümü sınırlayabilir; altındaki tepki yükselişi de haber akışının tamamen tek yönlü o
13.11 07:55 N  NEWS (6 new) score -0.40 conf 0.60: Altın 13 aylık dibe yakın seyrediyor; doların 19 aylık zirvede olması, Fed faiz artırımı beklentileri ve petrol kaynaklı enflasyon endişeleri baskı oluşturuyor. Ancak İran'ın ABD radar sahasını hedef aldığı haberi ve ABD PPI verisi öncesi ucuzluk alımları kısa vadeli toparlanma riskini artırıyor, bu nedenle güven orta düzeyde.
13.11 07:55 N  GPT  score -0.35 conf 0.58: Doların güçlü seyri ve Fed faiz artırımı beklentileri altın üzerinde baskı yaratıyor; petrol kaynaklı enflasyon endişeleri de bu baskıyı destekliyor. Dipten gelen pazarlık alımları kısa vadeli toparlanma sağlasa da altının haftalık düşüşte olması aşağı yönlü eğilimi öne çıkarıyor.
13.11 08:00 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
13.11 08:03 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
13.11 08:07 N  NEWS (5 new) score -0.60 conf 0.70: Altın 13 aylık dip seviyesine geriledi; Fed faiz artırımı beklentileri, DXY'nin 19 aylık zirvesine yakın seviyelerde seyretmesi ve petrol kaynaklı enflasyon endişeleri altın üzerinde baskı oluşturuyor. İran'ın ABD radar üssünü hedef alması gibi jeopolitik gelişmeler güvenli liman talebini destekleyebilir, ancak bu etki güçlü dolar ve sıkılaşma beklentileriyle dengelenemiyor; bu nedenle kısa vadede negatif görünüm hakim.
13.11 08:07 N  GPT  score -0.45 conf 0.62: Güçlü dolar ve Fed’in faiz artırımı beklentileri altın üzerindeki baskıyı artırıyor; fiyatın 3.900 doların altına gerilemesi de kısa vadeli momentumu zayıf gösteriyor. İran’ın ABD radar sahasını hedef aldığı haberi güvenli liman talebini destekleyebilir, ancak şu anki baskın etki aşağı yönlü görünüy
13.11 08:07 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
13.11 08:09 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
13.11 08:19 B5  CLOSE short stop: -55.97 USD
13.11 08:19 N  NEWS (4 new) score -0.60 conf 0.70: Altın 13 aylık dip seviyesine yakın işlem görüyor; ABD doları endeksi 19 aylık zirvesine yakın ve Fed faiz artırımı beklentileri güçleniyor, petrol kaynaklı enflasyon endişeleri de baskıyı artırıyor. İran'ın ABD radar sahasını hedef aldığını bildirmesi güvenli liman talebi açısından destekleyici olsa da, bu gelişme dolar ve faiz kaynaklı baskının gerisinde kalıyor; yakın vadede etki negatif görünüyor.
13.11 08:19 N  GPT  score -0.25 conf 0.56: Yeni başlıkların çoğu altın fiyatını etkileyebilecek somut bir gelişme içermiyor. İran kaynaklı gerilim güvenli liman talebini desteklese de güçlü dolar, Fed’in faiz artırımı beklentileri ve altındaki düşüş eğilimi önümüzdeki saatlerde baskın görünüyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
