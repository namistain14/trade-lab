# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 04.11.2026 08:25 (İstanbul)

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
| Net kâr/zarar | -42.87 $ | -385.62 $ |
| İşlem sayısı | 3 | 27 |
| Kazanma oranı | %33.3 | %33.3 |
| Ödenen komisyon/spread | 35.71 $ | 321.30 $ |

**Hesap değeri: 4,624.28 $** (başlangıç 5,000 $, -375.72 $ / %-7.51)

Açık pozisyonlar: PAXGUSDT long @ 3960.40 (TP 3972.28 / SL 3952.48)

Son haber analizi (04.11 08:25): Claude puan **+0.25**, güven 0.40 — Dolar zayıflaması ve ABD ara seçim sonuçlarının İran savaşı üzerindeki belirsizliği artırması altın için hafif olumlu; ayrıca petrol fiyatlarının düşmesi enflasyon ve faiz artırımı beklentilerini zayıflatabilir. Buna karşın istihdam verisi kaynaklı faiz artırımı beklentileri ve altındaki satış baskısı haberleri olumsuz, bu nedenle güven düşük tutuldu.

GPT (gpt-6-luna): puan **+0.35**, güven 0.53 — İran savaşının sürmesi ve tarafların anlaşmadan uzak görünmesi güvenli liman talebini destekler; tahvil fiyatlarındaki yükseliş de altına yardımcı olabilir. Ancak doların yeniden toparlanması ve faiz artışı beklentileri bu desteği sınırlıyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 04.11 07:50 | PAXGUSDT | long | +69.04 $ | take profit |
| 04.11 06:01 | PAXGUSDT | long | -55.94 $ | stop |
| 04.11 01:49 | PAXGUSDT | short | -55.96 $ | stop |
| 03.11 23:04 | PAXGUSDT | short | +69.06 $ | take profit |
| 03.11 15:57 | PAXGUSDT | long | +69.03 $ | take profit |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +66.43 $ |
| İşlem sayısı | 0 | 1 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 17.17 $ |

**Hesap değeri: 5,066.43 $** (başlangıç 5,000 $, +66.43 $ / %+1.33)

Son haber analizi (02.11 23:07): Claude puan **-0.50**, güven 0.60 — Baskın haber akışı İran ile barış görüşmelerine ve Hürmüz Boğazı'nın iki gün içinde yeniden açılabileceği ihtimaline işaret ediyor; bu, savaş primini hızla eritip Brent'i aşağı çekiyor (piyasada %7'ye varan düşüş bildirildi). Kazakistan'ın Samara hattındaki taşımayı durdurması ve Hindistan'daki rafineri yangını gibi arz kaynaklı yukarı yönlü riskler var, ancak bunlar müzakere iyimserliğinin gerisinde kalıyor; Goldman'ın hedef artışı ise uzun vadeli bir sinyal.

GPT (gpt-6-luna): puan **-0.78**, güven 0.82 — ABD-İran ateşkes görüşmeleri ve İran’ın anlaşma kapsamında Hürmüz Boğazı’nı yeniden açabileceği haberleri yakın vadeli arz kesintisi riskini azaltıyor; petrolün %7’den fazla düşmesi bu beklentinin fiyatlandığını gösteriyor. Kazakistan’ın petrol transitini durdurması sınırlı bir karşı unsur, ancak kı

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

**Hesap değeri: 102,500.90 $** (başlangıç 100,000 $, +2500.90 $ / %+2.50)

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
04.11 07:29 N  NEWS (8 new) score +0.10 conf 0.35: Dolar zayıflığı ve Demokratların ara seçimde öne geçmesi altını kısa vadede hafifçe destekliyor, ancak güçlü ABD istihdam verisinin faiz artırımı beklentilerini yükseltmesi ve gümüşteki sert düşüş baskı yaratıyor. Haberler birbiriyle çelişkili olduğu için yön belirsiz ve güven düşük.
04.11 07:29 N  GPT  score +0.18 conf 0.42: Midterm sonuçlarıyla doların gerilemesi ve İran kaynaklı jeopolitik risk altını destekliyor. Ancak yaklaşan istihdam verisi öncesi faiz artışı beklentileri ve altındaki baskı görünümü kazancı sınırlıyor.
04.11 07:49 B5  CLOSE long take profit: +69.04 USD
04.11 07:49 N  NEWS (15 new) score +0.20 conf 0.40: İran'daki yeni çatışma haberleri (ABD'nin Qeshm Adası'ndaki IRGC füze sahasını vurması ve Trump'ın saldırıları doğrulaması) güvenli liman talebini destekleyerek altı hafif yukarı çekiyor. Buna karşılık ABD istihdam verisinin faiz artırımı beklentilerini körüklemesi ve ABD dolarının ara seçim sonuçlarıyla zayıflaması karışık sinyaller yaratıyor; bu nedenle etki sınırlı ve belirsiz.
04.11 07:49 N  GPT  score +0.58 conf 0.66: İran’ın ABD’nin Hürmüz planına yanıtını yetersiz bulması ve Trump’ın saldırıları doğrulaması, kısa vadede güvenli liman talebini artırabilir. Doların seçim sonuçlarıyla zayıflaması da altını destekliyor; ancak çelişkili altın haberleri ve hareketin kısmen fiyatlanmış olma ihtimali yükselişi sınırlıy
04.11 07:55 B5  LONG gold 25000 USD x10 @ 3960.40 (TP 3972.28, SL 3952.48; news +0.39)
04.11 08:02 N  NEWS (10 new) score +0.25 conf 0.40: Doların ABD ara seçim sonrası sert zayıflaması ve İran'daki çatışmanın tırmanması (ABD saldırıları, Hürmüz gerginliği) altına kısa vadede destek veriyor. Ancak güçlü istihdam verisinin faiz artırımı beklentilerini körüklemesi ve bazı haberlerde altının değer kaybetmesi bu etkiyi sınırlıyor, bu yüzden güven düşük tutuldu.
04.11 08:02 N  GPT  score +0.32 conf 0.43: İran’ın Hürmüz planına olumsuz yanıt vermesi ve ABD saldırılarını doğrulaması güvenli liman talebini destekleyebilir; doların seçim sonuçlarıyla zayıflaması da altına olumlu. Ancak istihdam verileri kaynaklı faiz artırımı beklentileri baskı yaratıyor ve haber akışı çelişkili olduğundan etki sınırlı,
04.11 08:02 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
04.11 08:04 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
04.11 08:07 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
04.11 08:13 N  NEWS (10 new) score +0.05 conf 0.35: Dolar, ara seçim sonrası Demokratların önde gitmesiyle zayıfladı ve bu altın için destekleyici; İran savaşının sürmesi ve Qeshm'e yapılan saldırılar güvenli liman talebini canlı tutuyor. Buna karşılık ABD istihdam verisinin faiz artırımı beklentilerini güçlendirmesi ve bazı haberlerde altının "kritik destek" altında kalma riski olması baskı yaratıyor. Sinyaller karışık olduğu için yön belirsiz ve güven düşük.
04.11 08:13 N  GPT  score +0.35 conf 0.48: Demokratların seçimlerde güç kazanmasıyla doların gerilemesi ve İran savaşının sürmesi altını kısa vadede destekliyor. Ancak güçlü istihdam verilerinin faiz artırımı beklentilerini beslemesi ve altındaki aşağı yönlü baskı sinyalleri kazanımı sınırlayabilir.
04.11 08:25 N  NEWS (14 new) score +0.25 conf 0.40: Dolar zayıflaması ve ABD ara seçim sonuçlarının İran savaşı üzerindeki belirsizliği artırması altın için hafif olumlu; ayrıca petrol fiyatlarının düşmesi enflasyon ve faiz artırımı beklentilerini zayıflatabilir. Buna karşın istihdam verisi kaynaklı faiz artırımı beklentileri ve altındaki satış baskısı haberleri olumsuz, bu nedenle güven düşük tutuldu.
04.11 08:25 N  GPT  score +0.35 conf 0.53: İran savaşının sürmesi ve tarafların anlaşmadan uzak görünmesi güvenli liman talebini destekler; tahvil fiyatlarındaki yükseliş de altına yardımcı olabilir. Ancak doların yeniden toparlanması ve faiz artışı beklentileri bu desteği sınırlıyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
