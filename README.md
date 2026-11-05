# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 06.11.2026 00:13 (İstanbul)

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
| Net kâr/zarar | +0.00 $ | -33.95 $ |
| İşlem sayısı | 0 | 52 |
| Kazanma oranı | %0.0 | %44.2 |
| Ödenen komisyon/spread | 0.00 $ | 617.46 $ |

**Hesap değeri: 4,966.06 $** (başlangıç 5,000 $, -33.94 $ / %-0.68)

Son haber analizi (06.11 00:04): Claude puan **+0.40**, güven 0.50 — Altın, Aralık faiz artırımı beklentilerinin geri çekilmesi ve Nasdaq 100'deki sert düşüşle birlikte güvenli liman talebinden destek görüyor; İran savaşının sürmesi ve petrol fiyatlarındaki yükseliş de jeopolitik risk primini canlı tutuyor. Ancak çoğu başlık görüş yazısı veya zaten fiyatlanmış haber niteliğinde, ayrıca bekleyen ABD istihdam verisi ve dolardaki olası güçlenme yönünde bir risk var; bu nedenle güven orta düzeyde.

GPT (gpt-6-luna): puan **+0.36**, güven 0.48 — İran savaşıyla ilgili belirsizlik ve Medine’ye yönelen füzenin önlenmesi kısa vadede güvenli liman talebini destekleyebilir. Ancak petrol artışının faiz beklentilerini yükseltme riski ve Ukrayna temaslarının gerilimi azaltma ihtimali yükselişi sınırlıyor.

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
| Net kâr/zarar | +0.00 $ | +5879.74 $ |
| İşlem sayısı | 0 | 21 |
| Kazanma oranı | %0.0 | %52.4 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 108,278.00 $** (başlangıç 100,000 $, +8278.00 $ / %+8.28)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 05.11 23:46 | SPY | short | +582.01 $ | seans sonu |
| 05.11 23:46 | QQQ | short | +576.72 $ | seans sonu |
| 05.11 23:46 | NVDA | short | +1215.36 $ | seans sonu |
| 05.11 23:46 | AAPL | long | +93.44 $ | seans sonu |
| 05.11 20:37 | QQQ | short | -1070.92 $ | stop |

## Son olaylar

```
05.11 23:16 N  NEWS (11 new) score -0.05 conf 0.30: Haberlerin çoğu Iran savaşının siyasi etkilerini tartışan yorumlar ve gündelik altın fiyat içerikleri; yeni ve somut bir jeopolitik şok yok. Güçlü ABD işgücü verisi doları desteklediği için hafif negatif, petrol fiyatlarındaki yükselişle birlikte gelen tahvil faiz düşüşü ise hafif pozitif; bu karışık sinyaller nedeniyle net etki çok zayıf.
05.11 23:16 N  GPT  score +0.08 conf 0.24: İran savaşı ve enerji krizine dair haberler güvenli liman talebini destekleyebilir; ancak yeni ve belirgin bir tırmanış haberi yok. Doların güçlü seyrine ilişkin önceki haberler altını sınırlarken, yeni altın üretim yatırımı kısa vadede anlamlı etki yaratmaz.
05.11 23:28 N  NEWS (10 new) score -0.10 conf 0.35: Yeni haberlerde çelişkili bir tablo var: Putin'in İran savaşını sona erdirme teklifi ve Demokratların seçim zaferinin savaşın bitişine yönelik baskısı jeopolitik risk primini hafifleten, dolayısıyla altın için hafif olumsuz. Buna karşın altının kırılımı koruması ve dolarda sınırlı hareket, ayrıca yaklaşan ABD istihdam verisi belirsizliği, güçlü bir yön sinyali vermiyor.
05.11 23:28 N  GPT  score +0.12 conf 0.28: Altının kırılımını koruduğuna dair başlık kısa vadeli momentumu destekliyor; Çinli firmalara yönelik yaptırımlar da sınırlı güvenli liman talebi yaratabilir. Ancak Putin’in İran savaşını sona erdirmeye yardım teklifinin gerilimi azaltma ihtimali var ve doların yatay seyri yön sinyalini zayıflatıyor.
05.11 23:40 N  NEWS (3 new) score +0.10 conf 0.30: 
05.11 23:40 N  GPT  score +0.16 conf 0.30: Altın için 4.000 dolar üzerindeki güçlü yükseliş ve Dünya Bankası’nın uzun vadeli görünümü hafif destekleyici; ancak bunlar büyük ölçüde bilinen veya geriye dönük haberler. Yeni manşetlerde İran savaşıyla ilgili somut bir tırmanış yok ve doların yatay seyri kısa vadeli yön sinyalini sınırlıyor.
05.11 23:46 B6  CLOSE long AAPL seans sonu: +93.44 USD
05.11 23:46 B6  CLOSE short NVDA seans sonu: +1215.36 USD
05.11 23:46 B6  CLOSE short QQQ seans sonu: +576.72 USD
05.11 23:46 B6  CLOSE short SPY seans sonu: +582.01 USD
05.11 23:46 B6  seans kapanışı: tüm pozisyonlar kapatıldı
05.11 23:52 N  NEWS (6 new) score +0.35 conf 0.45: Altın 4.100 doların üzerine çıktı; Nasdaq 100'ün sert düşüşü ve Aralık faiz artırımı beklentilerinin geri çekilmesi reel faiz baskısını azaltarak altını destekliyor. Ancak yükseliş zaten fiyatlanmaya başladı, ABD tarım dışı istihdam verisi ve dolar hareketi kısa vadede yönü değiştirebilir, bu yüzden güven orta düzeyde.
05.11 23:52 N  GPT  score +0.45 conf 0.56: NASDAQ’taki sert düşüş ve Aralık faiz artırımı beklentilerinin zayıflaması altını kısa vadede destekliyor; ayrıca İran savaşı kaynaklı risk algısı sürüyor. Ancak doların görece istikrarlı olması ve haberlerin bir kısmının mevcut fiyat hareketini yansıtması yükseliş etkisini sınırlıyor.
06.11 00:04 N  NEWS (11 new) score +0.40 conf 0.50: Altın, Aralık faiz artırımı beklentilerinin geri çekilmesi ve Nasdaq 100'deki sert düşüşle birlikte güvenli liman talebinden destek görüyor; İran savaşının sürmesi ve petrol fiyatlarındaki yükseliş de jeopolitik risk primini canlı tutuyor. Ancak çoğu başlık görüş yazısı veya zaten fiyatlanmış haber niteliğinde, ayrıca bekleyen ABD istihdam verisi ve dolardaki olası güçlenme yönünde bir risk var; bu nedenle güven orta düzeyde.
06.11 00:04 N  GPT  score +0.36 conf 0.48: İran savaşıyla ilgili belirsizlik ve Medine’ye yönelen füzenin önlenmesi kısa vadede güvenli liman talebini destekleyebilir. Ancak petrol artışının faiz beklentilerini yükseltme riski ve Ukrayna temaslarının gerilimi azaltma ihtimali yükselişi sınırlıyor.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
