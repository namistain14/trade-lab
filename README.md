# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 10.11.2026 09:21 (İstanbul)

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
| Net kâr/zarar | +13.20 $ | -666.22 $ |
| İşlem sayısı | 2 | 70 |
| Kazanma oranı | %50.0 | %37.1 |
| Ödenen komisyon/spread | 23.64 $ | 830.63 $ |

**Hesap değeri: 4,333.78 $** (başlangıç 5,000 $, -666.22 $ / %-13.32)

Son haber analizi (10.11 09:18): Claude puan **-0.10**, güven 0.35 — Trump'ın İran savaşının "esasen bittiğini" ve daha fazla saldırının "pek olası olmadığını" söylemesi güvenli liman talebini azaltarak altı hafif baskılıyor. Buna karşılık Ekim enflasyonunun yavaşlaması beklentisi faiz indirimi ihtimallerini destekleyip altı destekleyebilir; ancak CPI beklentilere göre zaten fiyatlanmış olduğundan net etki sınırlı ve yön belirsiz.

GPT (gpt-6-luna): puan **-0.25**, güven 0.48 — İran’da yeni saldırıların düşük olasılıklı görülmesi ve Ukrayna barış görüşmelerinin yeniden başlaması güvenli liman talebini azaltabilir; doların güçlenmesi ve altının CPI öncesi gerilemesi de kısa vadede baskı yaratıyor. Ancak enflasyon verisi henüz açıklanmadığından yön ve etki konusunda güven sı

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 10.11 06:45 | PAXGUSDT | short | +69.10 $ | take profit |
| 10.11 03:20 | PAXGUSDT | long | -55.90 $ | stop |
| 09.11 22:29 | PAXGUSDT | short | -55.93 $ | stop |
| 09.11 17:36 | PAXGUSDT | long | -55.90 $ | stop |
| 09.11 14:18 | PAXGUSDT | short | -55.93 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -67.46 $ | -123.04 $ |
| İşlem sayısı | 1 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 18.21 $ | 70.51 $ |

**Hesap değeri: 4,876.96 $** (başlangıç 5,000 $, -123.04 $ / %-2.46)

Son haber analizi (10.11 07:59): Claude puan **-0.25**, güven 0.50 — Trump'ın İran savaşının askeri olarak bittiğini söylemesi ve Brent'in %6,7 düşüp 91,70 dolara gerilemesi, barış beklentileri nedeniyle kısa vadede baskı yaratıyor. Ancak Hormuz'daki gemi saldırıları, Husilerin Suudi boru hattına yönelik saldırıları ve Çin'in ham petrol ithalatının artması arz riskini canlı tutuyor; bu çelişkili haberler güveni sınırlıyor.

GPT (gpt-6-luna): puan **-0.55**, güven 0.68 — İran savaşının askerî olarak sona erdiği açıklaması, saldırı risklerinin azaldığına dair haberler ve Brent’in %6,73 düşmesi kısa vadede güçlü aşağı yönlü baskıya işaret ediyor. Suudi petrol boru hattına yönelik saldırı ve Hürmüz’deki gemi iddiaları arz riskini canlı tutsa da haberler çelişkili ve dü

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
| Net kâr/zarar | +0.00 $ | +9437.07 $ |
| İşlem sayısı | 0 | 34 |
| Kazanma oranı | %0.0 | %50.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 111,691.09 $** (başlangıç 100,000 $, +11691.09 $ / %+11.69)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 09.11 23:48 | TSLA | long | +1105.07 $ | seans sonu |
| 09.11 23:48 | SPY | long | +281.01 $ | seans sonu |
| 09.11 23:48 | QQQ | long | +996.60 $ | seans sonu |
| 09.11 21:28 | NVDA | long | -1113.38 $ | stop |
| 09.11 19:06 | NVDA | long | -1115.17 $ | stop |

## Son olaylar

```
10.11 08:05 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
10.11 08:08 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
10.11 08:11 B5P  CLOSE short stop (gap): -67.46 USD
10.11 08:17 N  NEWS (8 new) score +0.10 conf 0.35: Ekim ayı ABD TÜFE'sinin beklentiden yavaş artması ihtimali faiz indirimi beklentilerini destekleyip altı kısa vadede yukarı taşıyabilir. Ancak Trump'ın İran savaşının askeri olarak bittiğini ve yeni saldırıların "çok olası olmadığını" söylemesi jeopolitik güvenli liman talebini zayıflatıyor, Ukrayna müzakereleri de risk iştahını artırabilir. Veri beklentilerde zaten fiyatlanmış olduğundan etki sınırlı ve yön belirsiz kalıyor.
10.11 08:17 N  GPT  score +0.15 conf 0.40: Ekim TÜFE’sinin yavaşlamasının beklenmesi ve doların zayıflığı altını kısa vadede destekleyebilir; ancak veri öncesi belirsizlik yüksek. Ukrayna barış görüşmeleri ve İran savaşının sona erebileceğine dair açıklamalar güvenli liman talebini sınırlarken, Orta Doğu’daki gerilimler ters yönde etki ediyo
10.11 08:29 N  NEWS (12 new) score -0.10 conf 0.40: Trump'ın İran savaşının "fiilen bitti" olduğunu söylemesi jeopolitik güvenli liman talebini zayıflatarak altın için hafif baskılayıcı. Buna karşılık petrol fiyatlarının düşmesi ve ABD CPI'ın yavaşlaması beklentisi enflasyon ve faiz artırımı baskısını azaltarak altı destekleyebilir; bu nedenle etki karışık ve sınırlı.
10.11 08:29 N  GPT  score -0.28 conf 0.48: Trump’ın İran savaşının fiilen sona erdiği yönündeki açıklaması güvenli liman talebini azaltabilir; doların güçlenmesi de altın üzerinde baskı oluşturuyor. Ancak beklenen daha düşük ABD enflasyonu ve yaklaşan CPI verisi yönü belirsizleştiriyor.
10.11 08:41 N  NEWS (4 new) score +0.10 conf 0.40: ABD CPI'nın yavaşlaması beklentisi ve dolardaki zayıflama altın için hafif olumlu; ancak Trump'ın İran'a yeni saldırı ihtimalini "çok düşük" görmesi ve savaşın "askeri olarak bitti" demesi jeopolitik güvenli liman primini azaltarak sınırlı bir baskı yaratıyor. Altın ayrıca 4.150 dolar civarındaki direnç altında kararsız seyrediyor; CPI sonucu belirleyici olacağı için güven düşük.
10.11 08:41 N  GPT  score -0.18 conf 0.42: İran’a yeni ABD saldırılarının düşük olasılıklı görülmesi ve Rusya-Ukrayna barış görüşmeleri güvenli liman talebini azaltarak altın üzerinde hafif baskı yaratabilir. Buna karşılık doların gerilemesi ve enflasyonun yavaşlayabileceği beklentisi düşüşü sınırlıyor; ABD TÜFE verisi öncesi yön belirsiz.
10.11 08:53 N  NEWS (5 new) score -0.10 conf 0.40: Trump'ın İran'a yeni saldırıların "son derece olası olmadığını" söylemesi ve savaşın askeri olarak bittiği yönündeki haberler jeopolitik güvenli liman talebini azaltıyor, bu da altın için hafif negatif. Ancak ABD TÜFE verisinin beklentiden yumuşak gelmesi beklentisi faiz indirimi ihtimalini destekleyip altını dengeleyebilir; piyasa CPI öncesi temkinli ve sonuç belirsiz olduğundan güven düşük.
10.11 08:53 N  GPT  score -0.25 conf 0.48: Altın, ABD TÜFE verisi öncesinde gerilerken doların tutunması kısa vadede baskı yaratıyor. İran’da çatışmanın sona ermesine yönelik açıklamalar ve Ukrayna barış görüşmeleri güvenli liman talebini azaltabilir; ancak yaklaşan TÜFE verisi yön konusunda belirsizlik bırakıyor.
10.11 09:06 N  NEWS (11 new) score -0.05 conf 0.35: Trump'ın İran savaşının "esasen bittiğini" ve daha fazla saldırının "pek olası olmadığını" söylemesi güvenli liman talebini azaltarak altı hafif baskılıyor. Buna karşılık Ekim enflasyonunun yavaşlaması beklentisi faiz indirimi ihtimallerini destekleyip altı destekleyebilir; ancak CPI beklentilere göre zaten fiyatlanmış olduğundan net etki sınırlı ve yön belirsiz.
10.11 09:06 N  GPT  score -0.32 conf 0.48: Trump’ın İran savaşının fiilen sona erdiğini ve yeni saldırıların pek olası olmadığını söylemesi güvenli liman talebini azaltarak altın için baskı yaratabilir; Rusya-Ukrayna barış görüşmeleri de bu yönde. Ancak yaklaşan ABD TÜFE verisi ve sonucu henüz bilinmediğinden kısa vadeli yön konusunda temkin
10.11 09:18 N  NEWS (6 new) score -0.10 conf 0.35: 
10.11 09:18 N  GPT  score -0.25 conf 0.48: İran’da yeni saldırıların düşük olasılıklı görülmesi ve Ukrayna barış görüşmelerinin yeniden başlaması güvenli liman talebini azaltabilir; doların güçlenmesi ve altının CPI öncesi gerilemesi de kısa vadede baskı yaratıyor. Ancak enflasyon verisi henüz açıklanmadığından yön ve etki konusunda güven sı
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
