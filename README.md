# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 20:05 (İstanbul)

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

## Bot B1 — Altın + haber (şimdiki ayarlar, TP 5$ / SL 3$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -70.85 $ | -67.04 $ |
| İşlem sayısı | 29 | 30 |
| Kazanma oranı | %24.1 | %26.7 |
| Ödenen komisyon/spread | 68.82 $ | 71.19 $ |

**Hesap değeri: 4,932.96 $** (başlangıç 5,000 $, -67.04 $ / %-1.34)

Son haber analizi (23.10 19:34): Claude puan **-0.20**, güven 0.40 — Başlıklar karışık: İran savaşının hızlı sona erebileceği haberi jeopolitik risk primini azaltarak altı hafif baskılıyor, ayrıca güçlü ABD işletme verisi doları destekliyor ve Fed kararı öncesi enflasyon kaygıları faiz beklentilerini sıkılaştırıcı yöne itiyor. Buna karşılık Eylül enflasyon baskılarının hafiflemesi ve sürmekte olan Orta Doğu/Ukrayna çatışmaları altın için destekleyici unsurlar; ayrıca birçok haber eski veya yerel nitelikte olduğundan güven düşük.

GPT (gpt-6-luna): puan **-0.20**, güven 0.38 — ABD iş gücü/işletme gücünün doları desteklemesi altın üzerinde kısa vadeli baskı yaratabilir; Trump’ın İran savaşını hızlı bitirmeyi değerlendirmesi de güvenli liman talebini azaltabilir. Ancak savaşın sürmesi olasılığı ve Fed kararı öncesi belirsizlik sinyalleri çelişkili kılıyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 20:03 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 19:47 | PAXGUSDT | short | -4.47 $ | stop (gap) |
| 23.10 19:31 | PAXGUSDT | short | +3.81 $ | take profit |
| 23.10 18:43 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 18:21 | PAXGUSDT | short | -6.96 $ | stop (gap) |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -30.94 $ | -30.94 $ |
| İşlem sayısı | 5 | 5 |
| Kazanma oranı | %20.0 | %20.0 |
| Ödenen komisyon/spread | 11.86 $ | 11.86 $ |

**Hesap değeri: 4,971.90 $** (başlangıç 5,000 $, -28.10 $ / %-0.56)

Açık pozisyonlar: PAXGUSDT short @ 4015.71 (TP 4003.66 / SL 4023.74)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 08:32 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 05:27 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 04:52 | PAXGUSDT | short | +13.82 $ | take profit |
| 23.10 03:57 | PAXGUSDT | short | -11.19 $ | stop |

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

## Bot B3 — Altın: B2 + seans filtresi + momentum + kârı koruma

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

**Hesap değeri: 5,016.65 $** (başlangıç 5,000 $, +16.65 $ / %+0.33)

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
23.10 19:01 B1  SHORT gold 5000 USD x10 @ 4018.98 (TP 4014.96, SL 4021.39; news -0.25)
23.10 19:13 N  NEWS (11 new) score -0.30 conf 0.40: 
23.10 19:13 N  GPT  score -0.25 conf 0.48: Altının 4.000 doların altına gerilemesi ve yüksek reel faizlerin fırsat maliyetini artırması kısa vadede baskı yaratıyor. Yeni bölgesel saldırılar güvenli liman talebini destekleyebilir; ancak İran savaşının hızlı sona erebileceği haberleri ve karışık enflasyon sinyalleri düşüşü sınırlıyor.
23.10 19:13 B6  karar turu: Claude «Piyasa öğle saatlerinde yatay ve kararsız; enerji öne çıkarken teknoloji hafif pozitif, net bir işlem fırsatı görünmüyor.» / GPT «Endekslerde dar bant ve Tesla'da önceden gerçekleşmiş satış baskısı nedeniyle mevcut haber-fiyat uyumu yeni pozisyon açmak için yeterince güçlü değil.»
23.10 19:22 N  NEWS (10 new) score -0.20 conf 0.35: Başlıklar karışık ama ağırlıklı olarak altın için hafif negatif: Trump'ın İran savaşını hızla bitirme ihtimali jeopolitik güvenli liman talebini azaltıyor, Fed'in aralık ayında faiz artırımı beklentisi ve yüksek reel getiriler fırsat maliyetini yükseltiyor. Eylül enflasyon baskısının gevşemesi ise sınırlı bir dengeleyici etki yaratıyor; Paris ve Ürdün'deki saldırılar ise kısa vadede güvenli liman talebini destekleyebilecek ama etkisi zayıf haberler. Birçok başlık eski veya tekrar eden olduğu için güven düşük.
23.10 19:22 N  GPT  score -0.20 conf 0.42: Trump’ın İran savaşını hızla bitirme seçeneğini değerlendirmesi ve Ukrayna’daki olası ateşkes güvenli liman talebini azaltabilir; buna karşılık bölgedeki saldırılar jeopolitik riskleri canlı tutuyor. Yüksek reel getiriler ve Fed’in sıkı kalabileceği beklentisi altın için hafif olumsuz, ancak haber a
23.10 19:34 B1  CLOSE short take profit: +3.81 USD
23.10 19:34 N  NEWS (10 new) score -0.20 conf 0.40: Başlıklar karışık: İran savaşının hızlı sona erebileceği haberi jeopolitik risk primini azaltarak altı hafif baskılıyor, ayrıca güçlü ABD işletme verisi doları destekliyor ve Fed kararı öncesi enflasyon kaygıları faiz beklentilerini sıkılaştırıcı yöne itiyor. Buna karşılık Eylül enflasyon baskılarının hafiflemesi ve sürmekte olan Orta Doğu/Ukrayna çatışmaları altın için destekleyici unsurlar; ayrıca birçok haber eski veya yerel nitelikte olduğundan güven düşük.
23.10 19:34 N  GPT  score -0.20 conf 0.38: ABD iş gücü/işletme gücünün doları desteklemesi altın üzerinde kısa vadeli baskı yaratabilir; Trump’ın İran savaşını hızlı bitirmeyi değerlendirmesi de güvenli liman talebini azaltabilir. Ancak savaşın sürmesi olasılığı ve Fed kararı öncesi belirsizlik sinyalleri çelişkili kılıyor.
23.10 19:34 B6  karar turu: Claude «Piyasa düşük volatiliteyle yatay seyrediyor; net bir avantaj olmadığı için beklemek en doğrusu.» / GPT «Endekslerde yönsüzlük ve hisselerde sınırlı teyit nedeniyle önümüzdeki 1–3 saat için yüzde 1,5 hedefi destekleyen net bir haber-fiyat avantajı yok.»
23.10 19:43 B1  SHORT gold 5000 USD x10 @ 4015.46 (TP 4011.44, SL 4017.87; news -0.20)
23.10 19:52 B1  CLOSE short stop (gap): -4.47 USD
23.10 19:52 B6  karar turu: Claude «Piyasa karışık ve düşük volatiliteli bir seyir izliyor; yapay zekâ altyapısına dair şüpheler teknolojiyi baskılasa da işlem açmayı haklı kılacak net bir avantaj yok.» / GPT «Endekslerde hafif satış baskısı var ancak haber ve fiyat teyidi birlikte yeterince güçlü olmadığından kaldıraçlı yeni pozisyon açmadan beklemek daha disiplinli.»
23.10 20:01 B1  SHORT gold 5000 USD x10 @ 4012.62 (TP 4008.60, SL 4015.02; news -0.20)
23.10 20:05 B1  CLOSE short stop: -4.19 USD
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
