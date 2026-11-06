# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 06.11.2026 16:31 (İstanbul)

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
| Net kâr/zarar | -323.09 $ | -357.03 $ |
| İşlem sayısı | 8 | 60 |
| Kazanma oranı | %12.5 | %40.0 |
| Ödenen komisyon/spread | 94.76 $ | 712.22 $ |

**Hesap değeri: 4,642.97 $** (başlangıç 5,000 $, -357.03 $ / %-7.14)

Son haber analizi (06.11 16:30): Claude puan **-0.20**, güven 0.40 — Haberler çelişkili: Goldman'ın Fed'in sertleşmesi nedeniyle altın tahminini düşürmesi, güçlenen dolar ve DXY'nin yükselişi altın için olumsuz; buna karşılık küresel borsa sell-off'u ve Iran savaşı kaynaklı güvenli liman talebi destekleyici. Fiyat başlığı (%4,31 artış) ile diğer haberler (Pakistan ve Hindistan'da düşüş) birbiriyle uyumsuz olduğundan güven düşük.

GPT (gpt-6-luna): puan **-0.30**, güven 0.56 — Küresel hisse senedi satışları ve İran savaşı güvenli liman talebini destekleyebilir; ancak riskten kaçışın doları güçlendirmesi, Fed’in enflasyon konusundaki temkinli duruşu ve beklenen faiz artışları altın için yakın vadede daha baskın bir baskı oluşturuyor. Altının sert yükseldiğine dair haberler

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 16:31 | PAXGUSDT | short | +69.09 $ | take profit |
| 06.11 14:26 | PAXGUSDT | short | -56.36 $ | stop (gap) |
| 06.11 10:57 | PAXGUSDT | short | -55.94 $ | stop |
| 06.11 09:25 | PAXGUSDT | short | -55.94 $ | stop |
| 06.11 08:11 | PAXGUSDT | short | -56.23 $ | stop (gap) |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -58.75 $ | +7.68 $ |
| İşlem sayısı | 1 | 2 |
| Kazanma oranı | %0.0 | %50.0 |
| Ödenen komisyon/spread | 17.52 $ | 34.69 $ |

**Hesap değeri: 5,007.68 $** (başlangıç 5,000 $, +7.68 $ / %+0.15)

Son haber analizi (06.11 13:40): Claude puan **+0.10**, güven 0.40 — Hormuz'da iki tankerin mayına çarpıp yanması ve Iran'ın bazı ülkelere geçiş kısıtlaması getirmesi arz riskini artırarak fiyatları destekliyor. Ancak Bloomberg'in de-eskalasyon sinyallerine bağlı düşüşü, Iran'ın nükleer teklifi ve Qatar aracılığıyla yürüyen diplomasi ile haftalık yaklaşık %12'lik düşüş eğilimi baskılayıcı; haberler çelişkili olduğu için net etki hafif pozitif kalıyor.

GPT (gpt-6-luna): puan **+0.38**, güven 0.52 — Hürmüz Boğazı’nda iki tankerin mayına çarparak yanması iddiası, arz kesintisi ve taşımacılık riskini artırarak Brent’i kısa vadede destekliyor. Ancak İran’ın Katar aracılığıyla teklif ilettiği ve gerilimin azalabileceği yönündeki haberler, ayrıca düşüş eğilimi, yükselişin güvenini sınırlıyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 08:11 | BZ=F | long | -58.75 $ | stop |
| 02.11 23:09 | BZ=F | short | +66.43 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +5879.74 $ |
| İşlem sayısı | 0 | 21 |
| Kazanma oranı | %0.0 | %52.4 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 108,259.60 $** (başlangıç 100,000 $, +8259.60 $ / %+8.26)

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
06.11 15:30 N  NEWS (14 new) score +0.05 conf 0.30: 
06.11 15:30 N  GPT  score +0.12 conf 0.36: İran savaşının yeniden tırmanabileceğine dair haberler ve küresel piyasalardaki riskten kaçış altına sınırlı destek sağlayabilir. Ancak NFP öncesi doların görece güçlü olması ve altının geri çekilmesi bu etkiyi dengeliyor; haber akışı çelişkili.
06.11 15:42 N  NEWS (7 new) score +0.05 conf 0.30: 
06.11 15:42 N  GPT  score +0.20 conf 0.38: İran savaşının yeniden başlayabileceğine dair haberler ve küresel hisse senetlerindeki düşüş güvenli liman talebini destekleyebilir; ancak petrol haberleri çelişkili ve altın istihdam verisi öncesinde geri çekiliyor. En yeni başlıkların çoğu piyasa açısından önemsiz olduğundan kısa vadeli yön sinyal
06.11 15:54 N  NEWS (31 new) score +0.00 conf 0.30: 
06.11 15:54 N  GPT  score -0.18 conf 0.34: İstihdam verisi öncesi doların yükselmesi ve İran savaşı kaynaklı risk priminin petrol düşüşüyle azalması altın üzerinde hafif baskı yaratabilir. Ancak altının haftalık kazanç yönünde olması ve verinin henüz açıklanmaması kısa vadeli yönü belirsiz kılıyor.
06.11 16:06 N  NEWS (11 new) score -0.25 conf 0.40: Dolar endeksi (DXY) haftalık zirvelere yaklaşıyor ve yatırımcılar ABD tarım dışı istihdam (NFP) verisini bekliyor; güçlü bir veri dolarızı ve Fed beklentilerini sertleştirip altın için olumsuz olabilir. Jeopolitik başlıklar (İran savaşından çıkış tartışması, petrol fiyatlarının düşüşü) güvenli liman talebini azaltıyor, ancak sonuç NFP sürprizine bağlı olduğu için güven düşük.
06.11 16:06 N  GPT  score -0.20 conf 0.42: DXY'nin haftalık zirvelere çıkması ve doların istihdam verisi öncesi güçlenmesi altın üzerinde kısa vadeli baskı yaratabilir. Ancak altının yükselişini sürdürmesi ve NFP öncesi belirsizlik etkinin sınırlı kalabileceğini düşündürüyor.
06.11 16:06 B5  SHORT gold 25000 USD x10 @ 4052.11 (TP 4039.95, SL 4060.21; news -0.23)
06.11 16:18 N  NEWS (12 new) score -0.30 conf 0.50: Dolar, AI hisselerindeki satış nedeniyle güvenli liman talebiyle yükseliyor ve DXY haftalık zirvelere yaklaşıyor; bu altın için baskı oluşturuyor. Fed'in Williams'ın enflasyonun hâlâ çok yüksek olduğu yönündeki açıklaması sıkı para politikası beklentisini destekleyerek altın için olumsuz. İran savaşı ile ilgili başlıklar ise büyük ölçüde eski ve fiyatlanmış haberler; yeni bir jeopolitik tırmanış sinyali zayıf. Öte yandan "altın haftalık kazanç yolunda" gibi karşıt bir haber var ve NFP verisi henüz açıklanmadığı için sinyal belirsiz.
06.11 16:18 N  GPT  score -0.28 conf 0.56: Fed’den Williams’ın enflasyonun hâlâ yüksek olduğu mesajı ve doların istihdam verisi öncesi güçlenmesi, kısa vadede altın için baskı oluşturuyor. İran ve Doğu Avrupa kaynaklı riskler güvenli liman talebini desteklese de etkiler karışık; yaklaşan istihdam verisi belirsizliği artırıyor.
06.11 16:31 B5  CLOSE short take profit: +69.09 USD
06.11 16:31 N  NEWS (13 new) score -0.20 conf 0.40: Haberler çelişkili: Goldman'ın Fed'in sertleşmesi nedeniyle altın tahminini düşürmesi, güçlenen dolar ve DXY'nin yükselişi altın için olumsuz; buna karşılık küresel borsa sell-off'u ve Iran savaşı kaynaklı güvenli liman talebi destekleyici. Fiyat başlığı (%4,31 artış) ile diğer haberler (Pakistan ve Hindistan'da düşüş) birbiriyle uyumsuz olduğundan güven düşük.
06.11 16:31 N  GPT  score -0.30 conf 0.56: Küresel hisse senedi satışları ve İran savaşı güvenli liman talebini destekleyebilir; ancak riskten kaçışın doları güçlendirmesi, Fed’in enflasyon konusundaki temkinli duruşu ve beklenen faiz artışları altın için yakın vadede daha baskın bir baskı oluşturuyor. Altının sert yükseldiğine dair haberler
06.11 16:31 B6  seans öncesi görüş: Teknoloji ağırlıklı sert satış sonrası açılışta tepki alımı olası, ancak istihdam verisi öncesi oynaklık yüksek olduğundan pozisyonlar küçük ve seçici tutulmalı.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
