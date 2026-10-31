# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 31.10.2026 04:17 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -467.72 $ |
| İşlem sayısı | 0 | 30 |
| Kazanma oranı | %0.0 | %23.3 |
| Ödenen komisyon/spread | 0.00 $ | 137.19 $ |

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
| Net kâr/zarar | -55.97 $ | +78.66 $ |
| İşlem sayısı | 1 | 12 |
| Kazanma oranı | %0.0 | %50.0 |
| Ödenen komisyon/spread | 11.93 $ | 142.76 $ |

**Hesap değeri: 5,078.66 $** (başlangıç 5,000 $, +78.66 $ / %+1.57)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 31.10 00:48 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 23:07 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 20:35 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 18:48 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 17:39 | PAXGUSDT | short | -55.97 $ | stop |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 101,078.48 $** (başlangıç 100,000 $, +1078.48 $ / %+1.08)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
30.10 20:52 B6  karar turu: Claude «Şahin Fed açıklamaları, Intel ve Amazon kaynaklı teknoloji satışı ve risk iştahındaki düşüşle piyasa aşağı yönlü seyrini koruyor.» / GPT «Yeni şahin Fed açıklamaları aşağı yönü destekliyor; ancak sert günlük kayıplar, 1:4 kaldıraçla ani tepki yükselişlerine karşı riski artırıyor.»
30.10 20:52 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"104065.62","message":"insufficient buying power"}
30.10 21:35 N  NEWS (27 new) score -0.70 conf 0.70: Fed yetkililerinin (Logan, Musalem, Lacker) ardı ardına faiz artırımı sinyali vermesi ve "Hawkish Hold" yorumları, reel faiz ve dolar beklentilerini yükselterek altı baskılıyor. Altın zaten 13 aylık dibe inmiş ve sert düşmüş olduğu için bir kısmı fiyatlanmış olabilir; ayrıca İran savaşının müzakere yoluyla yumuşama ihtimali güvenli liman talebini azaltıyor.
30.10 21:35 N  GPT  score -0.58 conf 0.72: Fed yetkililerinin ek faiz artışlarına işaret etmesi, yükselen reel faiz ve dolar beklentileri üzerinden altın için belirgin baskı oluşturuyor; altındaki sert düşüş de bu temanın zaten kısmen fiyatlandığını düşündürüyor. İran’daki çatışma ve enerji kaynaklı belirsizlik güvenli liman talebi sağlayabi
30.10 21:35 B6  karar turu: Claude «Şahin Fed mesajları ve çip hisselerindeki çöküşle piyasa güçlü bir satış baskısı altında, ancak Cuma kapanışı öncesi kısa pozisyon kapatma kaynaklı sert tepki riski var.» / GPT «Piyasa satış baskısı altında; yeni ve güçlü bir şirket katalizörü bulunmadığından kısa pozisyonlar öne çıkıyor, ancak 1:4 kaldıraçta ilişkili pozisyonların toplam riski sınırlanmalı ve işlemler kapa
30.10 21:35 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"103538.71","message":"insufficient buying power"}
30.10 22:26 N  NEWS (28 new) score -0.50 conf 0.60: Altın 13 aylık dibe yakın, 3.900 doların altında seyrediyor; Fed yetkililerinin ek faiz artırımı sinyali vermesi ve yüksek petrol fiyatlarının enflasyon korkusunu beslemesi reel faizleri ve doları destekleyerek altın üzerinde baskı yaratıyor. Iran'la arabuluculuk çabaları ve Patriot satışı gibi haberler jeopolitik risk primini sınırlı artırıyor; bu nedenle genel etki negatif, ancak güven orta düzeyde çünkü ara bir jeopolitik şok veya dovish bir sürpriz yönü değiştirebilir.
30.10 22:26 N  GPT  score -0.35 conf 0.62: Altın üzerindeki kısa vadeli baskı, yükselen enerji fiyatlarının enflasyon ve faiz artışı beklentilerini güçlendirmesiyle yaşanan sert düşüş ve Fed yetkililerinin şahin mesajlarından geliyor. Doların gerilemesi ve Ukrayna’ya Patriot satışı bir miktar destek sağlasa da etkileri sınırlı; İran’la ilgil
30.10 23:11 B5  CLOSE short stop: -55.97 USD
30.10 23:11 N  NEWS (26 new) score -0.50 conf 0.60: Fed faizleri sabit tuttu ama "hawkish hold" çerçevesinde yetkililerin yakın dönemde daha fazla faiz artırımı sinyali verdiği ve piyasanın buna inandığı bildiriliyor; bu reel faiz ve dolar beklentilerini yükselterek altı baskılıyor. Altın yıllık dipte ve güçlü büyüme/enflasyon verisi de bu baskıyı destekliyor. Bunun karşısında İran savaşının yeniden başlama riski ve ABD'nin Ukrayna'ya 2,1 milyar dolarlık Patriot satışı gibi jeopolitik haberler güvenli liman talebini kısmen destekleyebilir, ancak bunların büyük çoğunluğu zaten fiyatlanmış görünüyor.
30.10 23:11 N  GPT  score -0.58 conf 0.69: Fed’in faizi sabit tutarken daha fazla artış sinyali vermesi ve kalıcı enflasyon vurgusu, kısa vadede reel faizler ile dolar üzerinden altın için baskı oluşturuyor; altının yıllık dip seviyeye gerilemesi de bu zayıf momentumu destekliyor. Ukrayna ve Orta Doğu’daki gerilimler güvenli liman talebini a
30.10 23:56 N  NEWS (29 new) score -0.65 conf 0.70: Fed yetkililerinin (Logan dahil) ek faiz artışı sinyalleri ve "hawkish hold" havası, reel faiz beklentilerini yükselterek altı baskılıyor; altın yıllık dibe inmiş durumda. Iran savaşının sonlanabileceği yönündeki Trump açıklamaları da güvenli liman talebini zayıflatıyor. Bu haberlerin bir kısmı zaten fiyatlanmış olabileceği için güveni sınırlı tutuyorum.
30.10 23:56 N  GPT  score -0.72 conf 0.78: Fed yetkililerinin iki faiz artışı beklentisini dile getirmesi ve enflasyon kaygıları, altının faiz getirisi olmayan varlık olarak cazibesini azaltıyor; fiyatın yeni yıl dibine gerilemesi de aşağı yönlü momentumu destekliyor. İran savaşının yakında bitebileceği açıklaması güvenli liman talebini sını
30.10 23:56 B5  SHORT gold 25000 USD x10 @ 3891.96 (TP 3880.29, SL 3899.75; news -0.69)
31.10 01:15 B5  CLOSE short stop: -55.97 USD
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
