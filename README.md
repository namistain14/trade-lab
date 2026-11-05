# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 05.11.2026 18:15 (İstanbul)

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
| Net kâr/zarar | +177.62 $ | +64.74 $ |
| İşlem sayısı | 8 | 48 |
| Kazanma oranı | %62.5 | %45.8 |
| Ödenen komisyon/spread | 94.62 $ | 570.11 $ |

**Hesap değeri: 5,058.82 $** (başlangıç 5,000 $, +58.82 $ / %+1.18)

Açık pozisyonlar: PAXGUSDT short @ 4097.84 (TP 4085.55 / SL 4106.04)

Son haber analizi (05.11 18:12): Claude puan **-0.40**, güven 0.55 — Fed yetkilileri (Barkin, Hammack, TD Securities) kademeli ama ek sıkılaştırma beklentisini destekliyor ve reel getiriler altına baskı yapıyor; ayrıca İran savaşında geri çekilme ihtimali güvenli liman talebini azaltıyor. Buna karşılık madencilik hisselerindeki yaklaşık %9 yükselişler altındaki kısa vadeli toparlanmaya işaret ediyor, bu yüzden güven orta düzeyde tutuldu.

GPT (gpt-6-luna): puan **-0.40**, güven 0.55 — Fed yetkililerinin kısıtlayıcı faizlerin sürmesi ve kademeli faiz artışları yönündeki mesajları, reel getiriler üzerinden altına kısa vadede baskı yapıyor; doların toparlanması da bu etkiyi destekliyor. İran konusunda diplomatik ilerleme ve savaşı sona erdirme söylemleri güvenli liman talebini sınır

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 05.11 18:10 | PAXGUSDT | short | -55.92 $ | stop |
| 05.11 14:18 | PAXGUSDT | long | +69.07 $ | take profit |
| 05.11 10:28 | PAXGUSDT | long | -55.90 $ | stop |
| 05.11 08:21 | PAXGUSDT | long | -55.90 $ | stop |
| 05.11 06:55 | PAXGUSDT | long | +69.07 $ | take profit |

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
| Net kâr/zarar | +537.99 $ | +3845.53 $ |
| İşlem sayısı | 2 | 14 |
| Kazanma oranı | %50.0 | %42.9 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 106,113.20 $** (başlangıç 100,000 $, +6113.20 $ / %+6.11)

Açık pozisyonlar: SPY short @ 750.58 (TP 738.86 / SL 757.61)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 05.11 18:12 | NVDA | short | +1589.76 $ | take profit |
| 05.11 18:03 | AAPL | long | -1051.77 $ | stop |
| 04.11 23:45 | SPY | long | +485.08 $ | seans sonu |
| 04.11 23:45 | QQQ | long | -222.60 $ | seans sonu |
| 04.11 23:45 | AAPL | long | -505.78 $ | seans sonu |

## Son olaylar

```
05.11 17:48 N  GPT  score -0.18 conf 0.32: İran’ın diplomatik ilerleme bildirmesi güvenli liman talebini sınırlayabilir; doların yeniden güçlenmesi de altın için kısa vadede baskı oluşturuyor. Buna karşılık haber akışı çelişkili ve bazı faiz haberlerinin ABD politikasına doğrudan etkisi belirsiz olduğundan görünüm temkinli ve hafif aşağı yön
05.11 17:48 B6  karar turu: Claude «Piyasa, teknoloji ve yapay zekâ hisselerinin önderliğinde güçlü bir risk-off satışı yaşıyor; düşüş ivmesi sürse de aşırı uzamış hareketlerde tepki riski var.» / GPT «Piyasa satış ağırlıklı; dört kat kaldıraçta ilişkili kısa pozisyonların toplam riskini sınırlamak ve sert düşmüş hisselerde tepki yükselişlerine dikkat etmek gerekiyor.»
05.11 17:48 B6  AÇIĞA SATIŞ NVDA 552 adet ≈ 105,432 $ (1:4) @ 191.0 (TP 188.13, SL 192.91; ikisi de hemfikir, güven 0.58)
05.11 18:00 N  NEWS (17 new) score -0.40 conf 0.60: 
05.11 18:00 N  GPT  score -0.30 conf 0.42: Doların toparlanması ve Fed’in enflasyon/rate görünümüne ilişkin şahin sinyaller altını kısa vadede baskılayabilir. İran savaşının sona erdirilmesine dair açıklama da güvenli liman talebini azaltabilir; ancak bu söylem koşullu ve haber akışı karışık olduğundan etki sınırlı görünüyor.
05.11 18:00 B5  SHORT gold 25000 USD x10 @ 4102.76 (TP 4090.45, SL 4110.96; news -0.35)
05.11 18:00 B6  karar turu: Claude «Piyasa teknoloji ve AI hisseleri öncülüğünde güçlü bir satış baskısı altında; ivme aşağı yönlü ancak hareketin büyük kısmı gerçekleşmiş durumda.» / GPT «Şahin Fed mesajları ve teknoloji öncülüğündeki satışlar kısa vadede aşağı yönü destekliyor; ancak aşırı düşen hisselerde tepki riski nedeniyle seçici kalıyorum.»
05.11 18:03 B6  CLOSE long AAPL stop: -1051.77 USD
05.11 18:12 B5  CLOSE short stop: -55.92 USD
05.11 18:12 N  NEWS (15 new) score -0.40 conf 0.55: Fed yetkilileri (Barkin, Hammack, TD Securities) kademeli ama ek sıkılaştırma beklentisini destekliyor ve reel getiriler altına baskı yapıyor; ayrıca İran savaşında geri çekilme ihtimali güvenli liman talebini azaltıyor. Buna karşılık madencilik hisselerindeki yaklaşık %9 yükselişler altındaki kısa vadeli toparlanmaya işaret ediyor, bu yüzden güven orta düzeyde tutuldu.
05.11 18:12 N  GPT  score -0.40 conf 0.55: Fed yetkililerinin kısıtlayıcı faizlerin sürmesi ve kademeli faiz artışları yönündeki mesajları, reel getiriler üzerinden altına kısa vadede baskı yapıyor; doların toparlanması da bu etkiyi destekliyor. İran konusunda diplomatik ilerleme ve savaşı sona erdirme söylemleri güvenli liman talebini sınır
05.11 18:12 B6  CLOSE short NVDA take profit: +1589.76 USD
05.11 18:12 B6  karar turu: Claude «Teknoloji öncülüğünde sert bir risk-off trend günü yaşanıyor; Fed'in şahin tonu ve yapay zeka şüpheleri baskıyı sürdürüyor, aşırı uzamış isimler yerine daha az uzamış olanlarda short tercih ediliyor.» / GPT «Piyasa genelinde satış eğilimi baskın; kısa pozisyonlar avantajlı görünse de uzamış düşüş ve 1:4 kaldıraç nedeniyle ani tepki ve eşzamanlı stop riski yüksek.»
05.11 18:12 B6  AÇIĞA SATIŞ SPY 141 adet ≈ 105,766 $ (1:4) @ 750.11 (TP 738.86, SL 757.61; ikisi de hemfikir, güven 0.50)
05.11 18:15 B5  SHORT gold 25000 USD x10 @ 4097.84 (TP 4085.55, SL 4106.04; news -0.40)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
