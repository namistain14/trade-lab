# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 02.11.2026 20:50 (İstanbul)

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
| Net kâr/zarar | -111.90 $ | -33.24 $ |
| İşlem sayısı | 2 | 14 |
| Kazanma oranı | %0.0 | %42.9 |
| Ödenen komisyon/spread | 23.81 $ | 166.57 $ |

**Hesap değeri: 4,986.51 $** (başlangıç 5,000 $, -13.49 $ / %-0.27)

Açık pozisyonlar: PAXGUSDT long @ 3959.62 (TP 3971.50 / SL 3951.70)

Son haber analizi (02.11 20:42): Claude puan **+0.30**, güven 0.50 — Petrol fiyatlarının düşmesi Fed faiz artırımı beklentilerini zayıflatıyor ve dolar beş haftanın en düşüğüne geriledi; bu, altın için destekleyici. Buna karşılık İran ile barış görüşmelerinin hızlanması güvenli liman talebini biraz azaltabilir ve altındaki yükseliş kısmen fiyatlanmış durumda, bu nedenle güven orta düzeyde tutuldu.

GPT (gpt-6-luna): puan **+0.38**, güven 0.54 — Petrol fiyatlarındaki düşüşün Fed faiz artırımı beklentilerini zayıflatması ve doların gerilemesi altını destekliyor; Ukrayna ve Sudan’daki çatışmalar da güvenli liman talebini artırabilir. Ancak İran’la barış görüşmeleri ve altının son saatlerde zaten yükselmiş olması ek yükselişin gücünü sınırlıyo

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 20:28 | PAXGUSDT | long | -55.93 $ | stop |
| 02.11 08:08 | PAXGUSDT | short | -55.97 $ | stop |
| 31.10 00:48 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 23:07 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 20:35 | PAXGUSDT | short | +69.06 $ | take profit |

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

**Hesap değeri: 100,765.82 $** (başlangıç 100,000 $, +765.82 $ / %+0.77)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
02.11 19:56 N  GPT  score +0.35 conf 0.53: Petrol fiyatlarındaki sert düşüşün Fed’in faiz artırma beklentilerini zayıflatması ve doların geri çekilmesi kısa vadede altını destekleyebilir. İran’la barış görüşmeleri güvenli liman talebini azaltırken yeni saldırı tehdidi bu etkiyi sınırlıyor.
02.11 19:56 B5  LONG gold 25000 USD x10 @ 3972.84 (TP 3984.76, SL 3964.90; news +0.32)
02.11 19:56 B6  karar turu: Claude «Endeksler günü artıda tutsa da öğleden sonra teknoloji ağırlıklı hafif bir zayıflama var; İran gerilimi ve Apple bilançosu öncesi temkinli bir hava hakim.» / GPT «Endekslerde gün içi kazançlar korunurken teknoloji tarafındaki belirgin zayıflık seçici kısa pozisyonları destekliyor.»
02.11 20:08 N  NEWS (12 new) score +0.25 conf 0.40: Petrol fiyatlarının İran savaşının sona erebileceği umutlarıyla sert düşmesi, Fed faiz artırımı beklentilerini zayıflatarak altı destekliyor; dolar ayrıca bir aylık dibe gerilemiş durumda. Buna karşın barış umudu jeopolitik korku primini azaltarak güvenli liman talebini baskılıyor, bu nedenle etki sınırlı ve karışık.
02.11 20:08 N  GPT  score +0.35 conf 0.56: Doların bir aylık dip seviyeye gerilemesi ve petrol düşüşünün Fed’in faiz artırımı beklentilerini zayıflatması altını kısa vadede destekliyor; altının zaten %2 yükseldiği bildiriliyor. İran’la yoğun görüşmelerin savaş riskini azaltabileceği yönündeki haberler güvenli liman talebini sınırlayabilir.
02.11 20:08 B6  karar turu: Claude «Piyasa güçlü ISM verisiyle hafif pozitif ancak öğle saatlerinde yatay seyrediyor; Apple bilançosu ve İran haberleri öncesinde temkinli iyimserlik hakim.» / GPT «Endeksler gün içi kazanımlarını korurken son saatte ivme kaybediyor; dar bantta 4 kat kaldıraçla yeni işlem açmayı destekleyen belirgin bir avantaj yok.»
02.11 20:20 N  NEWS (6 new) score +0.30 conf 0.45: Petrol fiyatlarının düşmesi (Brent %5,9 geriledi) Fed sıkılaşma beklentilerini zayıflatarak altın için destekleyici; dolar ise bir aylık düşüğe geriledi. Buna karşılık İran savaşının uzayabileceği yönündeki haberler jeopolitik risk talebini canlı tutuyor ve diplomatik umutlar hızla değişebilir, bu yüzden sinyal karışık ve güven sınırlı.
02.11 20:20 N  GPT  score +0.30 conf 0.43: Doların bir aylık dipte olması ve petrol düşüşünün Fed faiz artışı beklentilerini zayıflatması altını destekleyebilir. İran’dan uzun savaş uyarısı güvenli liman talebini artırsa da diplomatik umutlar ve haber akışındaki çelişkiler yükseliş görünümünü sınırlıyor.
02.11 20:20 B6  karar turu: Claude «Endeksler güçlü ISM verisiyle günü artıda geçiriyor ancak öğleden sonra yatay ve yönsüz bir seyir izliyor; İran gerilimi ve Apple bilançosu öncesi temkinli olmak gerekiyor.» / GPT «Endeksler günlük kazanımlarını korusa da son saatte yatay seyrediyor; şirket bazlı haberler henüz endekslerde işlem açılabilecek bir yön oluşturmuyor.»
02.11 20:42 B5  CLOSE long stop: -55.93 USD
02.11 20:42 N  NEWS (19 new) score +0.30 conf 0.50: Petrol fiyatlarının düşmesi Fed faiz artırımı beklentilerini zayıflatıyor ve dolar beş haftanın en düşüğüne geriledi; bu, altın için destekleyici. Buna karşılık İran ile barış görüşmelerinin hızlanması güvenli liman talebini biraz azaltabilir ve altındaki yükseliş kısmen fiyatlanmış durumda, bu nedenle güven orta düzeyde tutuldu.
02.11 20:42 N  GPT  score +0.38 conf 0.54: Petrol fiyatlarındaki düşüşün Fed faiz artırımı beklentilerini zayıflatması ve doların gerilemesi altını destekliyor; Ukrayna ve Sudan’daki çatışmalar da güvenli liman talebini artırabilir. Ancak İran’la barış görüşmeleri ve altının son saatlerde zaten yükselmiş olması ek yükselişin gücünü sınırlıyo
02.11 20:42 B5  LONG gold 25000 USD x10 @ 3959.62 (TP 3971.50, SL 3951.70; news +0.34)
02.11 20:42 B6  karar turu: Claude «Endeksler gün içi kazançlarını yavaşça geri veriyor ve teknoloji, petrol düşüşüne rağmen göreceli zayıf kalıyor.» / GPT «Endekslerde kısa vadeli momentum aşağı yönlü; ancak taze ve doğrudan bir olumsuz katalizörün yokluğu, sabit yüzde 1,5 hedefin kalan seansta gerçekleşmesini belirsiz kılıyor.»
02.11 20:42 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"103191.9","message":"insufficient buying power"}
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
