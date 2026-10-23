# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 20:36 (İstanbul)

## Bot A — Kripto kurallar (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.30 $ | +0.30 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %100.0 | %100.0 |
| Ödenen komisyon/spread | 2.00 $ | 2.00 $ |

**Hesap değeri: 5,000.30 $** (başlangıç 5,000 $, +0.30 $ / %+0.01)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 09:46 | ETHUSDT | long | +0.30 $ | time limit |

## Bot A2 — Kripto: sert düşüş sonrası toparlanma (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot B1 — Altın + haber (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -73.85 $ | -70.04 $ |
| İşlem sayısı | 30 | 31 |
| Kazanma oranı | %23.3 | %25.8 |
| Ödenen komisyon/spread | 71.20 $ | 73.57 $ |

**Hesap değeri: 4,929.96 $** (başlangıç 5,000 $, -70.04 $ / %-1.40)

Son haber analizi (23.10 19:34): Claude puan **-0.20**, güven 0.40 — Başlıklar karışık: İran savaşının hızlı sona erebileceği haberi jeopolitik risk primini azaltarak altı hafif baskılıyor, ayrıca güçlü ABD işletme verisi doları destekliyor ve Fed kararı öncesi enflasyon kaygıları faiz beklentilerini sıkılaştırıcı yöne itiyor. Buna karşılık Eylül enflasyon baskılarının hafiflemesi ve sürmekte olan Orta Doğu/Ukrayna çatışmaları altın için destekleyici unsurlar; ayrıca birçok haber eski veya yerel nitelikte olduğundan güven düşük.

GPT (gpt-6-luna): puan **-0.20**, güven 0.38 — ABD iş gücü/işletme gücünün doları desteklemesi altın üzerinde kısa vadeli baskı yaratabilir; Trump’ın İran savaşını hızlı bitirmeyi değerlendirmesi de güvenli liman talebini azaltabilir. Ancak savaşın sürmesi olasılığı ve Fed kararı öncesi belirsizlik sinyalleri çelişkili kılıyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 20:31 | PAXGUSDT | short | -3.00 $ | stop |
| 23.10 20:03 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 19:47 | PAXGUSDT | short | -4.47 $ | stop (gap) |
| 23.10 19:31 | PAXGUSDT | short | +3.81 $ | take profit |
| 23.10 18:43 | PAXGUSDT | short | -4.19 $ | stop |

## Bot B2 — Altın: sıkı haber eşiği (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -35.22 $ | -35.22 $ |
| İşlem sayısı | 6 | 6 |
| Kazanma oranı | %16.7 | %16.7 |
| Ödenen komisyon/spread | 14.24 $ | 14.24 $ |

**Hesap değeri: 4,964.78 $** (başlangıç 5,000 $, -35.22 $ / %-0.70)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 18:03 | PAXGUSDT | short | -4.28 $ | stop (gap) |
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 08:32 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 05:27 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 04:52 | PAXGUSDT | short | +13.82 $ | take profit |

## Bot B4 — Altın: haberin TERSİ (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -11.18 $ | -11.18 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 4,988.82 $** (başlangıç 5,000 $, -11.18 $ / %-0.22)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 17:08 | PAXGUSDT | long | -11.18 $ | stop |

## Bot B3 — Altın: B2 + seans filtresi + momentum (net +2$ / -3$, hızlı kapanış)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -26.82 $ | -26.82 $ |
| İşlem sayısı | 3 | 3 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 7.12 $ | 7.12 $ |

**Hesap değeri: 4,973.18 $** (başlangıç 5,000 $, -26.82 $ / %-0.54)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 18:22 | PAXGUSDT | short | -11.35 $ | stop (gap) |
| 23.10 18:03 | PAXGUSDT | short | -4.28 $ | stop (gap) |
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +13.82 $ | +13.82 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %100.0 | %100.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 5,022.58 $** (başlangıç 5,000 $, +22.58 $ / %+0.45)

Açık pozisyonlar: PAXGUSDT short @ 4015.71 (TP 4003.66 / SL 4023.74)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 17:11 | PAXGUSDT | short | +13.82 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:2

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 100,000.00 $** (başlangıç 100,000 $, +0.00 $ / %+0.00)

## Son olaylar

```
23.10 19:34 B6  karar turu: Claude «Piyasa düşük volatiliteyle yatay seyrediyor; net bir avantaj olmadığı için beklemek en doğrusu.» / GPT «Endekslerde yönsüzlük ve hisselerde sınırlı teyit nedeniyle önümüzdeki 1–3 saat için yüzde 1,5 hedefi destekleyen net bir haber-fiyat avantajı yok.»
23.10 19:43 B1  SHORT gold 5000 USD x10 @ 4015.46 (TP 4011.44, SL 4017.87; news -0.20)
23.10 19:52 B1  CLOSE short stop (gap): -4.47 USD
23.10 19:52 B6  karar turu: Claude «Piyasa karışık ve düşük volatiliteli bir seyir izliyor; yapay zekâ altyapısına dair şüpheler teknolojiyi baskılasa da işlem açmayı haklı kılacak net bir avantaj yok.» / GPT «Endekslerde hafif satış baskısı var ancak haber ve fiyat teyidi birlikte yeterince güçlü olmadığından kaldıraçlı yeni pozisyon açmadan beklemek daha disiplinli.»
23.10 20:01 B1  SHORT gold 5000 USD x10 @ 4012.62 (TP 4008.60, SL 4015.02; news -0.20)
23.10 20:05 B1  CLOSE short stop: -4.19 USD
23.10 20:16 B1  SHORT gold 5000 USD x10 @ 4008.77 (TP 4004.76, SL 4011.17; news -0.20)
23.10 20:16 B6  karar turu: Claude «Piyasa geniş tabanlı hafif zayıflıkta ve yapay zeka harcamalarına dair şüpheler var, fakat net ve şirkete özel bir avantaj olmadığından beklemek en doğrusu.» / GPT «Endekslerde son saatte satış baskısı var ancak önümüzdeki 1–3 saatte yüzde 1,5 hedefi destekleyen taze katalizör ve güçlü fiyat teyidi birleşmediği için beklemek daha disiplinli.»
23.10 20:23 B1  hedefler güncellendi: TP 4007.16 (+2$), SL 4011.17 (-3$)
23.10 20:23 B2  hedefler güncellendi: TP 4014.10 (+2$), SL 4018.12 (-3$)
23.10 20:23 B2  CLOSE short stop (gap): -4.28 USD
23.10 20:34 B6  Claude cevap vermedi: no Claude model available: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Yo
23.10 20:34 B6  karar turu: Claude «-» / GPT «Endekslerde aşağı eğilim ve jeopolitik risk baskın olsa da mevcut fiyat hareketleri önümüzdeki 1–3 saat için %1,5 hedef ve %1 stop koşullarında net avantaj sunmuyor.»
23.10 20:36 B1  hedefler güncellendi: TP 4006.21 (+2$ net), SL 4010.22 (-3$ net)
23.10 20:36 B1  CLOSE short stop: -3.00 USD
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
