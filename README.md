# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 02.11.2026 19:59 (İstanbul)

## Bot A — Kripto TERS (alım sinyalinde satış, x3)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -267.62 $ | -1022.76 $ |
| İşlem sayısı | 18 | 79 |
| Kazanma oranı | %16.7 | %19.0 |
| Ödenen komisyon/spread | 74.61 $ | 350.21 $ |

**Hesap değeri: 3,977.24 $** (başlangıç 5,000 $, -1022.76 $ / %-20.46)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 16:39 | BNBUSDT | short | -25.72 $ | stop |
| 02.11 16:38 | ETHUSDT | short | -12.86 $ | stop |
| 02.11 16:39 | BTCUSDT | short | -25.72 $ | stop |
| 02.11 15:31 | BNBUSDT | short | -1.73 $ | time limit |
| 02.11 15:10 | XRPUSDT | short | -12.99 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -55.97 $ | +22.70 $ |
| İşlem sayısı | 1 | 13 |
| Kazanma oranı | %0.0 | %46.2 |
| Ödenen komisyon/spread | 11.92 $ | 154.68 $ |

**Hesap değeri: 5,010.27 $** (başlangıç 5,000 $, +10.27 $ / %+0.21)

Açık pozisyonlar: PAXGUSDT long @ 3972.84 (TP 3984.76 / SL 3964.90)

Son haber analizi (02.11 19:56): Claude puan **+0.30**, güven 0.50 — Petrol fiyatlarının %6 düşüşü, enflasyon ve Fed faiz artırımı beklentilerini gevşeterek altın için reel faiz kanalından destekleyici bir etki yaratıyor; dolar da geri çekildi. Ancak ABD-İran müzakerelerinin yeniden başlaması güvenli liman talebini azaltıyor ve Trump'ın yeni saldırı tehdidi gibi çelişkili haberler sinyali karıştırıyor, bu yüzden etki orta düzeyde pozitif kalıyor.

GPT (gpt-6-luna): puan **+0.35**, güven 0.53 — Petrol fiyatlarındaki sert düşüşün Fed’in faiz artırma beklentilerini zayıflatması ve doların geri çekilmesi kısa vadede altını destekleyebilir. İran’la barış görüşmeleri güvenli liman talebini azaltırken yeni saldırı tehdidi bu etkiyi sınırlıyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 08:08 | PAXGUSDT | short | -55.97 $ | stop |
| 31.10 00:48 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 23:07 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 20:35 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 18:48 | PAXGUSDT | short | +69.06 $ | take profit |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

Son haber analizi (02.11 08:00): Claude puan **+0.15**, güven 0.40 — Hürmüz Boğazı'nda iki tankerin mayına çarpıp patlaması arz riskini ciddi biçimde artırdığı için kısa vadede yukarı yönlü baskı yaratabilir. Ancak İran-ABD müzakerelerine ilişkin haberler fiyatları son saatlerde yüzde 3 civarında aşağı çekti ve haberler birbiriyle çelişkili; Goldman'ın tahmin artırımı ise büyük ölçüde fiyatlanmış durumda. Bu nedenle sinyal zayıf ve yönü belirsiz.

GPT (gpt-6-luna): puan **+0.20**, güven 0.48 — Hürmüz Boğazı’nda iki tankerin mayına çarparak patladığına dair yeni haber, doğrulanması hâlinde kısa vadede arz ve taşımacılık risk primini artırabilir. Ancak İran’la diplomasi haberleriyle petrolün zaten %3’ten fazla gerilemesi ve Ceyhan ihracatındaki artış bu yükseliş etkisini sınırlıyor.

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 101,313.45 $** (başlangıç 100,000 $, +1313.45 $ / %+1.31)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
02.11 18:52 B6  karar turu: Claude «Piyasa güçlü ISM verisi ve İran müzakere umutlarıyla pozitif seyrediyor, ancak öğle saatlerinde ivme zayıflıyor.» / GPT «Endeksler günlük kazanımlarını korusa da son yarım saatte ivme zayıflıyor; teknoloji ağırlıklı endekste seçici kısa pozisyonu tercih ediyorum.»
02.11 19:04 N  NEWS (8 new) score -0.10 conf 0.35: 
02.11 19:04 N  GPT  score +0.25 conf 0.43: İran’da savaşın genişleyebileceğine dair tehditler ve görüşmelerden sonuç çıkmaması güvenli liman talebini destekleyebilir; doların borç maliyetleri nedeniyle baskı görebileceği beklentisi de altın için olumlu. Ancak görüşmelerin sürmesi, Fed sıkılaşması endişeleri ve altının önceki sert düşüş sonra
02.11 19:04 B6  karar turu: Claude «Piyasa güçlü ISM verisiyle pozitif açıldı ancak öğle saatlerinde zirveden geri çekilip yatay seyre geçti; jeopolitik riskler ve Apple bilançosu öncesi temkinli bir görünüm hakim.» / GPT «Endeksler günlük kazançlarını korusa da son bölümdeki ivme kaybı kısa vadede temkinli satış yönünü destekliyor; dört kat kaldıraçta pozisyon büyüklüğü sınırlı tutulmalı.»
02.11 19:16 N  NEWS (12 new) score +0.10 conf 0.40: 
02.11 19:16 N  GPT  score +0.22 conf 0.38: Altın fiyatındaki yaklaşık %2’lik yükseliş ve düşük reel getirilerin destekleyici olduğuna dair haberler kısa vadede hafif pozitif. Ancak Orta Doğu’da barış umuduyla petrolün gerilemesi güvenli liman talebini azaltabilir; karışık dolar ve enflasyon sinyalleri görünümü belirsiz kılıyor.
02.11 19:16 B6  karar turu: Claude «Sabahki yükseliş öğlene doğru sönümleniyor; teknoloji öncülüğünde hafif satış baskısı ve jeopolitik riskler kısa vadede aşağı yönlü eğilimi öne çıkarıyor.» / GPT «Endeksler günlük artıda olsa da saatlik satış eğilimi kısa yönünü destekliyor; iki pozisyonun yüksek korelasyonu nedeniyle toplam kaldıraç riski sınırlanmalı.»
02.11 19:16 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"104434.41","message":"insufficient buying power"}
02.11 19:44 N  NEWS (20 new) score -0.15 conf 0.35: İran'la müzakere ve savaşın sona erebileceği umutları, jeopolitik güvenli liman talebini biraz azaltabileceği için altı hafif olumsuz etkileyebilir. Ancak petrol fiyatlarının düşmesi enflasyon beklentilerini yumuşatıp faiz indirimi beklentilerini destekleyebileceğinden ve bir haberde altının %2 yükseldiği bildirildiğinden sinyaller çelişkili; bu nedenle güven düşük tutuldu.
02.11 19:44 N  GPT  score -0.23 conf 0.46: İran-ABD görüşmelerinin yoğunlaştığı ve petrolün barış umuduyla gerilediği haberleri kısa vadede güvenli liman talebini azaltarak altını baskılayabilir. Ancak İran’dan gelen tehditler ve çatışmanın yeniden başlayabileceğine dair değerlendirmeler tabloyu belirsiz kılıyor.
02.11 19:44 B6  karar turu: Claude «Endeksler günü artıda ama öğleden sonra yorulma, İran gerilimi ve AI kaygıları nedeniyle hafif aşağı yönlü bir sürüklenme var; Apple bilançosu öncesi temkin hakim.» / GPT «Endekslerde gün içi kazançlar erirken kısa vadeli eğilim aşağı; QQQ'da satış yönü öne çıksa da 1–3 saatte %1,5 hedefi iddialı ve dört kat kaldıraç riski büyütüyor.»
02.11 19:56 N  NEWS (12 new) score +0.30 conf 0.50: Petrol fiyatlarının %6 düşüşü, enflasyon ve Fed faiz artırımı beklentilerini gevşeterek altın için reel faiz kanalından destekleyici bir etki yaratıyor; dolar da geri çekildi. Ancak ABD-İran müzakerelerinin yeniden başlaması güvenli liman talebini azaltıyor ve Trump'ın yeni saldırı tehdidi gibi çelişkili haberler sinyali karıştırıyor, bu yüzden etki orta düzeyde pozitif kalıyor.
02.11 19:56 N  GPT  score +0.35 conf 0.53: Petrol fiyatlarındaki sert düşüşün Fed’in faiz artırma beklentilerini zayıflatması ve doların geri çekilmesi kısa vadede altını destekleyebilir. İran’la barış görüşmeleri güvenli liman talebini azaltırken yeni saldırı tehdidi bu etkiyi sınırlıyor.
02.11 19:56 B5  LONG gold 25000 USD x10 @ 3972.84 (TP 3984.76, SL 3964.90; news +0.32)
02.11 19:56 B6  karar turu: Claude «Endeksler günü artıda tutsa da öğleden sonra teknoloji ağırlıklı hafif bir zayıflama var; İran gerilimi ve Apple bilançosu öncesi temkinli bir hava hakim.» / GPT «Endekslerde gün içi kazançlar korunurken teknoloji tarafındaki belirgin zayıflık seçici kısa pozisyonları destekliyor.»
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
