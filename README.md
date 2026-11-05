# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 05.11.2026 21:04 (İstanbul)

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
| Net kâr/zarar | +78.93 $ | -33.95 $ |
| İşlem sayısı | 12 | 52 |
| Kazanma oranı | %50.0 | %44.2 |
| Ödenen komisyon/spread | 141.97 $ | 617.46 $ |

**Hesap değeri: 4,966.06 $** (başlangıç 5,000 $, -33.94 $ / %-0.68)

Son haber analizi (05.11 21:01): Claude puan **-0.20**, güven 0.40 — Faiz artırımları ve dolar güvenli liman talebi altın için kısa vadede baskı yaratıyor; İran savaşının sürmesi ve petrol fiyatlarındaki yükseliş enflasyon beklentilerini destekleyerek bu baskıyı kısmen dengeliyor. Haberlerin çoğu zaten fiyatlanmış veya dolaylı olduğu için güven düşük tutuldu.

GPT (gpt-6-luna): puan **+0.15**, güven 0.34 — İran’a yönelik Rus füze sistemleri tedariki haberleri ve yükselen petrol fiyatı kısa vadede güvenli liman talebini destekleyebilir. Ancak doların güçlenmesi altını baskılıyor; savaşın geleceğine ilişkin haberler de kesin bir yeni tırmanış göstermiyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 05.11 19:13 | PAXGUSDT | short | -55.93 $ | stop |
| 05.11 19:03 | PAXGUSDT | short | -55.93 $ | stop |
| 05.11 18:54 | PAXGUSDT | short | +69.10 $ | take profit |
| 05.11 18:18 | PAXGUSDT | short | -55.93 $ | stop |
| 05.11 18:10 | PAXGUSDT | short | -55.92 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +66.43 $ |
| İşlem sayısı | 0 | 1 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 17.17 $ |

**Hesap değeri: 5,066.43 $** (başlangıç 5,000 $, +66.43 $ / %+1.33)

Son haber analizi (05.11 07:59): Claude puan **-0.05**, güven 0.40 — Haberler çelişkili: İran'ın Hürmüz'de dört tankerin mayınlarla vurulduğunu öne sürmesi ve petrol fiyatlarındaki Hürmüz arz riskleri fiyatı yukarı iter; buna karşılık Brent'in İran müzakereleri nedeniyle 4 haftalık dibe inmesi ve ABD-İran arasında anlaşmanın hâlâ uzak olması aşağı yönlü baskı yaratır. Tanker iddiası doğrulanmamış olduğu için net etki hafif pozitif, güven düşük.

GPT (gpt-6-luna): puan **+0.28**, güven 0.55 — Hürmüz’de iki tanker ve bir römorkörün alev aldığı haberi, doğrulanması hâlinde yakın vadeli arz ve taşımacılık risk primini artırarak Brent’i yukarı destekleyebilir. Ancak İran geriliminin azalacağı beklentileriyle süren sert satış ve haberin nedeni hakkındaki belirsizlik yükseliş etkisini sınırlıy

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 23:09 | BZ=F | short | +66.43 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +104.67 $ | +3412.21 $ |
| İşlem sayısı | 5 | 17 |
| Kazanma oranı | %40.0 | %41.2 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 108,194.64 $** (başlangıç 100,000 $, +8194.64 $ / %+8.19)

Açık pozisyonlar: AAPL long @ 345.10 (TP 350.16 / SL 341.54); NVDA short @ 183.87 (TP 181.37 / SL 185.97); QQQ short @ 653.82 (TP 644.30 / SL 660.65); SPY short @ 738.48 (TP 727.62 / SL 746.09)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 05.11 20:37 | QQQ | short | -1070.92 $ | stop |
| 05.11 19:14 | NVDA | short | -955.66 $ | stop |
| 05.11 18:53 | SPY | short | +1593.26 $ | take profit |
| 05.11 18:12 | NVDA | short | +1589.76 $ | take profit |
| 05.11 18:03 | AAPL | long | -1051.77 $ | stop |

## Son olaylar

```
05.11 19:14 B6  CLOSE short NVDA stop: -955.66 USD
05.11 20:37 N  NEWS (43 new) score -0.25 conf 0.40: 
05.11 20:37 N  GPT  score +0.16 conf 0.38: İran savaşının tırmanma ihtimali ve Rusya'nın İran'a füze sistemleri sağladığına dair haberler kısa vadede güvenli liman talebini destekleyebilir. Ancak İran'ın somut nükleer önerileri değerlendirmesi ve doların güçlenmesi bu etkiyi sınırlıyor; haber akışı çelişkili olduğundan yön sinyali zayıf.
05.11 20:37 B6  CLOSE short QQQ stop: -1070.92 USD
05.11 20:37 B6  karar turu: Claude «Seçim sonrası rallinin ardından AI/teknoloji kaynaklı sert satış sürüyor; savunmacı sektörler öne çıkarken trend kapanışa kadar aşağı yönlü görünüyor.» / GPT «Önümüzdeki 1–3 saatte aşağı yön ağır basıyor; ancak sert günlük kayıplar tepki riskini artırırken 1:4 kaldıraçlı ve yüksek korelasyonlu kısa pozisyonların toplam riski sınırlı tutulmalı.»
05.11 20:37 B6  AÇIĞA SATIŞ SPY 143 adet ≈ 105,634 $ (1:4) @ 738.7 (TP 727.62, SL 746.09; ikisi de hemfikir, güven 0.45)
05.11 20:37 B6  AÇIĞA SATIŞ QQQ 162 adet ≈ 105,966 $ (1:4) @ 654.11 (TP 644.3, SL 660.65; ikisi de hemfikir, güven 0.55)
05.11 20:37 B6  AÇIĞA SATIŞ NVDA 576 adet ≈ 106,059 $ (1:4) @ 184.13 (TP 181.37, SL 185.97; ikisi de hemfikir, güven 0.55)
05.11 20:49 N  NEWS (12 new) score -0.25 conf 0.40: 
05.11 20:49 N  GPT  score +0.15 conf 0.32: İran’a Rusya’dan füze sistemleri tedarik edildiğine dair haberler jeopolitik risk ve güvenli liman talebini artırabilir. Ancak doların güçlenmesi ve petrol kaynaklı faiz/enflasyon kaygıları altının yükselişini sınırlıyor; kısa vadeli etki bu nedenle hafif pozitif ve belirsiz.
05.11 20:49 B6  karar turu: Claude «AI ve teknoloji odaklı sert satış sürüyor, defansif hisseler göreli olarak güçlü kalırken kapanışa doğru oynaklık yüksek kalabilir.» / GPT «Piyasanın ana yönü aşağı; AAPL’deki göreli güç seçici alımı desteklese de mevcut endeks ve NVDA pozisyonlarıyla birleşen dört kat kaldıraç toplam riski artırıyor.»
05.11 20:49 B6  ALIŞ AAPL 128 adet ≈ 44,159 $ (1:4) @ 344.99 (TP 350.16, SL 341.54; ikisi de hemfikir, güven 0.55)
05.11 21:01 N  NEWS (9 new) score -0.20 conf 0.40: Faiz artırımları ve dolar güvenli liman talebi altın için kısa vadede baskı yaratıyor; İran savaşının sürmesi ve petrol fiyatlarındaki yükseliş enflasyon beklentilerini destekleyerek bu baskıyı kısmen dengeliyor. Haberlerin çoğu zaten fiyatlanmış veya dolaylı olduğu için güven düşük tutuldu.
05.11 21:01 N  GPT  score +0.15 conf 0.34: İran’a yönelik Rus füze sistemleri tedariki haberleri ve yükselen petrol fiyatı kısa vadede güvenli liman talebini destekleyebilir. Ancak doların güçlenmesi altını baskılıyor; savaşın geleceğine ilişkin haberler de kesin bir yeni tırmanış göstermiyor.
05.11 21:01 B6  karar turu: Claude «Yapay zeka ve teknoloji hisselerindeki sert satış ile şahin Fed açıklamaları piyasayı baskılıyor ve gün sonuna doğru zayıflığın sürmesi muhtemel görünüyor.» / GPT «Endekslerde satış baskısı ve teknoloji hisselerinde zayıflık sürüyor; sert günlük kayıplar nedeniyle 4 kat kaldıraçta ani tepki yükselişleri önemli risk oluşturuyor.»
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
