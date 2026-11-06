# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 06.11.2026 14:53 (İstanbul)

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
| Net kâr/zarar | -392.18 $ | -426.12 $ |
| İşlem sayısı | 7 | 59 |
| Kazanma oranı | %0.0 | %39.0 |
| Ödenen komisyon/spread | 82.91 $ | 700.37 $ |

**Hesap değeri: 4,573.88 $** (başlangıç 5,000 $, -426.12 $ / %-8.52)

Son haber analizi (06.11 14:53): Claude puan **-0.10**, güven 0.35 — Haberler karışık: Fed'in Williams'ın enflasyonun hâlâ çok yüksek olduğunu söylemesi ve doların güçlü seyri altına baskı yaparken, İran savaşı yeniden alevlenme korkuları ile küresel hisse satışı güvenli liman talebini destekliyor. Bekleyen ABD istihdam verisi nedeniyle kısa vadeli oynaklık yüksek olacağından, net etki hafif negatif ve düşük güvenilirlikli.

GPT (gpt-6-luna): puan **-0.18**, güven 0.36 — Körfez’de gerilimin azalabileceği haberleri ve Fed yetkilisinin enflasyonun hâlâ yüksek olduğu yönündeki açıklaması altını kısa vadede baskılayabilir. Buna karşılık hisse senetlerindeki sert düşüş ve İran kaynaklı devam eden riskler güvenli liman talebini destekliyor; görünüm karışık.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 14:26 | PAXGUSDT | short | -56.36 $ | stop (gap) |
| 06.11 10:57 | PAXGUSDT | short | -55.94 $ | stop |
| 06.11 09:25 | PAXGUSDT | short | -55.94 $ | stop |
| 06.11 08:11 | PAXGUSDT | short | -56.23 $ | stop (gap) |
| 06.11 04:01 | PAXGUSDT | long | -55.91 $ | stop |

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
06.11 13:40 B5P  GPT  score +0.38 conf 0.52: Hürmüz Boğazı’nda iki tankerin mayına çarparak yanması iddiası, arz kesintisi ve taşımacılık riskini artırarak Brent’i kısa vadede destekliyor. Ancak İran’ın Katar aracılığıyla teklif ilettiği ve gerilimin azalabileceği yönündeki haberler, ayrıca düşüş eğilimi, yükselişin güvenini sınırlıyor.
06.11 13:52 N  NEWS (14 new) score -0.15 conf 0.30: Haberler karışık: Fed'in Williams'ın enflasyonun hâlâ yüksek olduğu yönündeki sözleri ve ABD dolarının güvenli liman talebiyle desteklenmesi altın için hafif olumsuz; buna karşılık İran'a yönelik üçüncü ABD uçak gemisi haberi jeopolitik risk primini destekliyor. Petrol fiyatlarındaki düşüş ve NFP öncesi eski tarihli "Fed faiz artırımı" beklentisi gibi unsurlar etkiyi dengeliyor, bu yüzden sinyal zayıf ve güven düşük.
06.11 13:52 N  GPT  score -0.35 conf 0.68: Fed yetkilisinin enflasyonun hâlâ yüksek olduğunu vurgulaması, güçlü dolar ve yükselen tahvil getirileriyle birlikte altın üzerinde kısa vadeli baskı yaratıyor; yaklaşan istihdam verisi de temkinliliği artırıyor. İran savaşı güvenli liman talebini destekleyebilir, ancak gerilimin azalabileceğine dai
06.11 14:04 N  NEWS (9 new) score -0.30 conf 0.40: Fed'in Williams'ın enflasyonun hâlâ yüksek olduğu yönündeki sözleri ve faiz artırımı beklentilerinin dolara destek vermesi altın için olumsuz. Teknoloji satışıyla gelen dolar güvenli liman talebi de altın lehine güçlü bir sığınak etkisi yaratmıyor; ayrıca petrol düşüşü ve İran'da de-eskalasyon işaretleri jeopolitik prim baskısını artırıyor. Haber akışı karışık olduğu için güven düşük tutuldu.
06.11 14:04 N  GPT  score -0.25 conf 0.48: Doların güvenli liman talebiyle yükselmesi ve Fed’den Williams’ın enflasyonun hâlâ yüksek olduğunu vurgulaması altını kısa vadede baskılıyor. İran kaynaklı riskler güvenli liman talebini desteklese de gerilimin azalabileceğine dair işaretler ve çelişkili haberler yönü sınırlıyor.
06.11 14:04 B5  SHORT gold 25000 USD x10 @ 4056.63 (TP 4044.46, SL 4064.74; news -0.28)
06.11 14:16 N  NEWS (13 new) score -0.15 conf 0.35: Dolar, teknoloji satışı kaynaklı güvenli liman talebiyle yükseliyor ve bu altın için baskı yaratıyor; Fed'in Williams'ın enflasyonun hâlâ çok yüksek olduğu yönündeki açıklaması da sıkı para politikası beklentisini destekliyor. Buna karşın İran'ın Avrupa'ya kadar uzanabilecek füze tehdidi jeopolitik risk primini canlı tutuyor, bu da altını destekleyebilir; sinyaller karışık olduğu için düşük güvenle hafif negatif bir görünüm veriyorum.
06.11 14:16 N  GPT  score -0.20 conf 0.42: Teknoloji satışlarıyla doların güvenli liman talebiyle güçlenmesi ve Fed’in enflasyonun hâlâ yüksek olduğu mesajı altını kısa vadede baskılayabilir. İran’dan olası misilleme tehdidi destekleyici olsa da savaş haberlerinin çoğu yeni değil; ayrıca petrol fiyatlarındaki gerileme gerilimin azalabileceği
06.11 14:25 B5  CLOSE short stop (gap): -56.36 USD
06.11 14:28 N  NEWS (17 new) score -0.15 conf 0.40: Fed'in New York ve Williams'ın "enflasyon çok yüksek" yorumları kısa vadede faiz beklentilerini sertleştirerek altı baskılıyor. Küresel borsa satışı ve dolar talebi de güvenli liman etkisiyle altın lehine değil aleyhine çalışıyor; buna karşılık savaş ve jeopolitik gerilim haberleri altı destekliyor. Bekleyen ABD tarım dışı istihdam verisi yönü belirsizleştirdiği için güven düşük.
06.11 14:28 N  GPT  score -0.25 conf 0.56: Küresel hisse satışları güvenli liman talebini destekleyebilir; ancak doların güvenli liman alımlarıyla toparlanması ve Fed yetkilisinin enflasyonu hâlâ yüksek bulması altın üzerinde baskı yaratıyor. İstihdam ve enflasyon verileri öncesi altının gerilemesi, kısa vadede hafif aşağı yönlü görünümü des
06.11 14:41 N  NEWS (15 new) score -0.10 conf 0.35: Haberler karışık: Fed'den Williams ve New York Fed'den gelen "enflasyon çok yüksek" yorumları ve dolardaki haven kaynaklı toparlanma altın için baskılayıcı, buna karşın yenilenen ABD-İran savaş korkuları ve küresel borsa sert düşüşü güvenli liman talebini destekliyor. ABD tarım dışı istihdam (NFP) ve enflasyon verisi öncesinde altın 4.100 doları altında beklemede olduğundan net etki hafif negatif ve belirsiz.
06.11 14:41 N  GPT  score -0.15 conf 0.48: İran’la savaş korkularının petrol fiyatlarını yükseltmesi altına güvenli liman desteği sağlayabilir. Ancak doların güçlenmesi, Fed’in enflasyon vurgusu ve yaklaşan istihdam verisi öncesindeki temkinlilik kısa vadede bu desteği dengeliyor; net etki hafif negatif.
06.11 14:53 N  NEWS (9 new) score -0.10 conf 0.35: Haberler karışık: Fed'in Williams'ın enflasyonun hâlâ çok yüksek olduğunu söylemesi ve doların güçlü seyri altına baskı yaparken, İran savaşı yeniden alevlenme korkuları ile küresel hisse satışı güvenli liman talebini destekliyor. Bekleyen ABD istihdam verisi nedeniyle kısa vadeli oynaklık yüksek olacağından, net etki hafif negatif ve düşük güvenilirlikli.
06.11 14:53 N  GPT  score -0.18 conf 0.36: Körfez’de gerilimin azalabileceği haberleri ve Fed yetkilisinin enflasyonun hâlâ yüksek olduğu yönündeki açıklaması altını kısa vadede baskılayabilir. Buna karşılık hisse senetlerindeki sert düşüş ve İran kaynaklı devam eden riskler güvenli liman talebini destekliyor; görünüm karışık.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
