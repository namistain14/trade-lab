# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 30.10.2026 21:35 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -217.43 $ | -467.72 $ |
| İşlem sayısı | 14 | 30 |
| Kazanma oranı | %21.4 | %23.3 |
| Ödenen komisyon/spread | 67.51 $ | 137.19 $ |

**Hesap değeri: 4,532.28 $** (başlangıç 5,000 $, -467.72 $ / %-9.35)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 03:19 | SOLUSDT | long | -14.64 $ | stop |
| 30.10 03:19 | ETHUSDT | long | -29.27 $ | stop |
| 30.10 03:19 | BTCUSDT | long | -29.27 $ | stop |
| 30.10 02:47 | XRPUSDT | long | -14.87 $ | stop |
| 30.10 02:47 | SOLUSDT | long | -29.74 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +233.41 $ | +190.61 $ |
| İşlem sayısı | 7 | 10 |
| Kazanma oranı | %71.4 | %60.0 |
| Ödenen komisyon/spread | 83.31 $ | 118.90 $ |

**Hesap değeri: 5,178.61 $** (başlangıç 5,000 $, +178.61 $ / %+3.57)

Açık pozisyonlar: PAXGUSDT short @ 3896.07 (TP 3884.38 / SL 3903.86)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 30.10 20:35 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 18:48 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 17:39 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 16:51 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 15:43 | PAXGUSDT | short | +69.07 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 101,027.65 $** (başlangıç 100,000 $, +1027.65 $ / %+1.03)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
30.10 19:20 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"104827.21","message":"insufficient buying power"}
30.10 20:09 N  NEWS (31 new) score -0.70 conf 0.70: Fed yetkilileri (Musalem, Barkin) yakında faiz artırımı gerektiğini söyleyerek şahin bir tutum sergiledi; bu reel faiz ve dolar beklentilerini yükselterek altı baskılıyor. Altın bir yıllık dibe inmiş ve sert düşüş yaşanıyor; Orta Doğu gerilimi ise güvenli liman talebini destekleyecek yönde olsa da bu etki şu an fiyatlanmış görünmüyor. Güvenli liman sinyali yerine faiz kaynaklı satış baskın olduğundan skor negatif, güven ise İran diplomasisinin belirsizliği nedeniyle orta düzeyde.
30.10 20:09 N  GPT  score -0.55 conf 0.69: Musalem’in yakında faiz artırımı gerektiğini yinelemesi, dolar ve reel faizleri destekleyerek altın üzerinde kısa vadeli baskı yaratabilir. Suudi Arabistan yakınındaki füze ve İHA önlemeleri güvenli liman talebini artırsa da bu etki, belirgin şahin Fed mesajını muhtemelen dengeleyemiyor; ayrıca habe
30.10 20:09 B6  karar turu: Claude «Şahin Fed açıklamaları ve çip hisselerindeki çöküş Cuma öğleden sonrasında teknoloji ağırlıklı satış baskısını sürdürüyor; ancak gün içi düşüş zaten büyük olduğu için pozisyonlar temkinli tutuluyor.» / GPT «Şahin Fed açıklamaları ve teknoloji hisselerindeki zayıflık kısa yönü destekliyor; iki endeksin yüksek korelasyonu nedeniyle toplam kaldıraçlı risk sınırlı tutulmalı.»
30.10 20:09 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"105073.85","message":"insufficient buying power"}
30.10 20:52 B5  CLOSE short take profit: +69.06 USD
30.10 20:52 N  NEWS (25 new) score -0.60 conf 0.60: Fed yetkililerinin (Logan, Musalem) faiz artırımı çağrısı reel faiz beklentilerini yükseltip altın için net baskı yaratıyor; İran savaşının yakında sona ereceği yönündeki haberler de güvenli liman talebini azaltıyor. Altın zaten sert düşüş yaşadığı için bir kısmı fiyatlanmış durumda, bu yüzden güven orta seviyede tutuldu.
30.10 20:52 N  GPT  score -0.35 conf 0.63: Logan ve Musalem’in yakın zamanda en az iki faiz artışı gerektiği yönündeki açıklamaları, faiz ve dolar beklentileri üzerinden altın için kısa vadede baskın biçimde olumsuz. İran kaynaklı riskler ve teknoloji hisselerindeki sert düşüş güvenli liman talebini destekleyebilir; ancak diplomasi haberleri
30.10 20:52 B5  SHORT gold 25000 USD x10 @ 3896.07 (TP 3884.38, SL 3903.86; news -0.47)
30.10 20:52 B6  karar turu: Claude «Şahin Fed açıklamaları, Intel ve Amazon kaynaklı teknoloji satışı ve risk iştahındaki düşüşle piyasa aşağı yönlü seyrini koruyor.» / GPT «Yeni şahin Fed açıklamaları aşağı yönü destekliyor; ancak sert günlük kayıplar, 1:4 kaldıraçla ani tepki yükselişlerine karşı riski artırıyor.»
30.10 20:52 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"104065.62","message":"insufficient buying power"}
30.10 21:35 N  NEWS (27 new) score -0.70 conf 0.70: Fed yetkililerinin (Logan, Musalem, Lacker) ardı ardına faiz artırımı sinyali vermesi ve "Hawkish Hold" yorumları, reel faiz ve dolar beklentilerini yükselterek altı baskılıyor. Altın zaten 13 aylık dibe inmiş ve sert düşmüş olduğu için bir kısmı fiyatlanmış olabilir; ayrıca İran savaşının müzakere yoluyla yumuşama ihtimali güvenli liman talebini azaltıyor.
30.10 21:35 N  GPT  score -0.58 conf 0.72: Fed yetkililerinin ek faiz artışlarına işaret etmesi, yükselen reel faiz ve dolar beklentileri üzerinden altın için belirgin baskı oluşturuyor; altındaki sert düşüş de bu temanın zaten kısmen fiyatlandığını düşündürüyor. İran’daki çatışma ve enerji kaynaklı belirsizlik güvenli liman talebi sağlayabi
30.10 21:35 B6  karar turu: Claude «Şahin Fed mesajları ve çip hisselerindeki çöküşle piyasa güçlü bir satış baskısı altında, ancak Cuma kapanışı öncesi kısa pozisyon kapatma kaynaklı sert tepki riski var.» / GPT «Piyasa satış baskısı altında; yeni ve güçlü bir şirket katalizörü bulunmadığından kısa pozisyonlar öne çıkıyor, ancak 1:4 kaldıraçta ilişkili pozisyonların toplam riski sınırlanmalı ve işlemler kapa
30.10 21:35 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"103538.71","message":"insufficient buying power"}
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
