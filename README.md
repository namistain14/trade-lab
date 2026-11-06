# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 06.11.2026 10:37 (İstanbul)

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
| Net kâr/zarar | -279.89 $ | -313.83 $ |
| İşlem sayısı | 5 | 57 |
| Kazanma oranı | %0.0 | %40.4 |
| Ödenen komisyon/spread | 59.20 $ | 676.66 $ |

**Hesap değeri: 4,718.39 $** (başlangıç 5,000 $, -281.61 $ / %-5.63)

Açık pozisyonlar: PAXGUSDT short @ 4043.78 (TP 4031.65 / SL 4051.87)

Son haber analizi (06.11 10:37): Claude puan **-0.30**, güven 0.50 — Altın için kısa vadede hafif negatif görünüm: petrol fiyatlarının yükselmesi enflasyon ve faiz artırımı endişelerini canlandırıyor, DXY toparlanıyor ve ABD tarım dışı istihdam (NFP) verisi öncesinde dolar güçleniyor. Tech hisselerindeki sert düşüş ve İran savaşı gibi güvenli liman talebini artıran unsurlar bu baskıyı kısmen dengeliyor, ancak fiyatlanmış ve çelişkili haberler güveni sınırlıyor.

GPT (gpt-6-luna): puan **-0.22**, güven 0.42 — Altın, yükselen petrol fiyatları ve güçlenen dolar eşliğinde %1’den fazla gerilemiş; yaklaşan ABD istihdam verisi ve faiz artışı endişeleri kısa vadede baskı yaratabilir. Teknoloji hisselerindeki sert düşüş güvenli liman talebini destekleyebilir, bu nedenle görünüm temkinli ve yön sinyalleri çelişki

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 09:25 | PAXGUSDT | short | -55.94 $ | stop |
| 06.11 08:11 | PAXGUSDT | short | -56.23 $ | stop (gap) |
| 06.11 04:01 | PAXGUSDT | long | -55.91 $ | stop |
| 06.11 03:47 | PAXGUSDT | long | -55.90 $ | stop |
| 06.11 02:52 | PAXGUSDT | long | -55.91 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -58.75 $ | +7.68 $ |
| İşlem sayısı | 1 | 2 |
| Kazanma oranı | %0.0 | %50.0 |
| Ödenen komisyon/spread | 17.52 $ | 34.69 $ |

**Hesap değeri: 5,007.68 $** (başlangıç 5,000 $, +7.68 $ / %+0.15)

Son haber analizi (06.11 07:59): Claude puan **+0.35**, güven 0.50 — Hormuz'daki yeni tanker saldırıları ve Rusya'daki rafineri patlamaları/Ukrayna saldırıları arz riskini artırıp Brent'i 100 doların üzerine itti; ancak İran'ın Katar üzerinden nükleer öneri göndermesi, Orta Doğu barış beklentileri ve haftalık yaklaşık %12-13'lük düşüş yukarı yönlü hareketi sınırlayabilir, bu yüzden güven orta düzeyde.

GPT (gpt-6-luna): puan **+0.55**, güven 0.66 — Hürmüz Boğazı’nda yeni tanker saldırısı haberleri ve Rusya’daki rafinerilere yönelik saldırı bildirimleri yakın vadeli arz riskini artırarak Brent’i destekliyor. İran’ın ABD’ye ilettiği bildirilen nükleer öneri ve daha geniş barış beklentileri bu etkiyi sınırlıyor; haberlerin bir kısmı doğrulanmamış

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
06.11 09:24 N  GPT  score -0.30 conf 0.55: ABD istihdam verisi öncesinde dolar endeksinin toparlanması ve altın fiyatlarındaki düşüş, önümüzdeki saatlerde baskının sürebileceğine işaret ediyor. İran savaşı ve Ukrayna diplomasisine ilişkin haberler güvenli liman talebini destekleyebilir; ancak yönleri belirsiz ve yaklaşan veri sonucu belirley
06.11 09:27 B5  CLOSE short stop: -55.94 USD
06.11 09:30 B5  SHORT gold 25000 USD x10 @ 4043.78 (TP 4031.65, SL 4051.87; news -0.25)
06.11 09:36 N  NEWS (4 new) score -0.15 conf 0.40: Dolar endeksi NFP öncesinde toparlanıyor ve enflasyon/Fed riski sürüyor; İran'da barış ilerlemesi jeopolitik güvenli liman talebini zayıflatıyor. Öte yandan ABD ara seçim sonucu ve küresel teknoloji hisselerindeki sert düşüş risk-off etkisiyle altını kısmen destekleyebilir; bu karışık tablo nedeniyle sinyal zayıf.
06.11 09:36 N  GPT  score -0.22 conf 0.38: Doların istihdam verisi öncesinde toparlanması ve altındaki düşüş haberleri kısa vadede baskı yönünde; ancak veri henüz açıklanmadı ve jeopolitik riskler aşağı yönü sınırlayabilir. ABD ara seçimlerinin altın için hafif olumlu görüldüğüne dair yeni yorum bu baskıyı kısmen dengeliyor.
06.11 09:49 N  NEWS (5 new) score -0.15 conf 0.40: Altın, dolar endeksinin (DXY ~101,8) NFP öncesi toparlanması ve yerel piyasalarda art arda düşüşlerle baskı altında. Jeopolitik risk (İran savaşı) ve ara dönüş beklentileri (WGC "interim bottom") olsa da, petrol fiyatlarının gevşemesi ve Fed riski altın için kısa vadede net olumsuz bir tablo çiziyor; sinyaller karışık olduğu için güven düşük.
06.11 09:49 N  GPT  score -0.28 conf 0.39: Dolar endeksinin istihdam verisi öncesinde toparlanması ve altındaki düşüş haberleri kısa vadede baskı yaratıyor. İran kaynaklı belirsizlik ve teknoloji hisselerindeki sert düşüş güvenli liman talebini destekleyebilir; ancak haber akışı karışık ve belirgin yeni bir tırmanış yok.
06.11 10:01 N  NEWS (5 new) score -0.15 conf 0.40: Altın, DXY'nin 101,80 seviyesine toparlanması ve ABD tarım dışı istihdam (NFP) raporu öncesi güçlü ABD verisi ihtimali nedeniyle baskı altında; Fed riski de sürüyor. Buna karşılık WGC'nin ara dip açıklaması, İran savaşında barış sürecinin belirsizliği ve teknoloji hisselerindeki sert düşüşten kaynaklanan güvenli liman talebi kısmen destekleyici; haberlerin çoğu zaten fiyatlanmış tekrarlar olduğu için güven düşük.
06.11 10:01 N  GPT  score -0.30 conf 0.43: ABD istihdam verisi öncesinde doların toparlanması ve altının düştüğünü bildiren çok sayıda başlık, önümüzdeki birkaç saat için baskının aşağı yönlü olduğuna işaret ediyor. WGC’nin dip oluşabileceği görüşü daha uzun vadeli ve jeopolitik haberler kısa vadede net bir güvenli liman desteği sağlamıyor.
06.11 10:13 N  NEWS (2 new) score -0.10 conf 0.35: Altın, yaklaşık %25'lik düşüşün ardından zayıf seyrediyor; DXY'nin 101,80 civarında toparlanması ve ABD tarım dışı istihdam (NFP) raporu öncesi temkinli hava kısa vadede baskı yaratıyor. Buna karşılık WGC'nin "geçici dip yakın" değerlendirmesi, ABD ara seçim sonuçlarının altına hafif olumlu olması ve İran savaşının sürmesi güvenli liman talebini destekleyebilir; bu nedenle etki sınırlı ve yön belirsiz.
06.11 10:13 N  GPT  score -0.35 conf 0.56: ABD istihdam verisi öncesinde doların güçlenmesi ve altındaki düşüş haberleri kısa vadede aşağı yönlü baskıya işaret ediyor. İran savaşı ve petrol piyasasındaki belirsizlik güvenli liman talebiyle bu baskıyı kısmen dengeleyebilir; yeni ve belirleyici bir veri henüz yok.
06.11 10:25 N  NEWS (1 new) score -0.15 conf 0.40: 
06.11 10:25 N  GPT  score -0.25 conf 0.43: Dolar endeksinin ABD istihdam verisi öncesinde güçlenmesi ve altının veri öncesi gerilemesi kısa vadede baskı yaratıyor. İran’daki barış sürecine ilişkin belirsizlik sınırlı güvenli liman talebi sağlayabilir; yaklaşan veriler ve çelişkili haberler güveni düşürüyor.
06.11 10:37 N  NEWS (4 new) score -0.30 conf 0.50: Altın için kısa vadede hafif negatif görünüm: petrol fiyatlarının yükselmesi enflasyon ve faiz artırımı endişelerini canlandırıyor, DXY toparlanıyor ve ABD tarım dışı istihdam (NFP) verisi öncesinde dolar güçleniyor. Tech hisselerindeki sert düşüş ve İran savaşı gibi güvenli liman talebini artıran unsurlar bu baskıyı kısmen dengeliyor, ancak fiyatlanmış ve çelişkili haberler güveni sınırlıyor.
06.11 10:37 N  GPT  score -0.22 conf 0.42: Altın, yükselen petrol fiyatları ve güçlenen dolar eşliğinde %1’den fazla gerilemiş; yaklaşan ABD istihdam verisi ve faiz artışı endişeleri kısa vadede baskı yaratabilir. Teknoloji hisselerindeki sert düşüş güvenli liman talebini destekleyebilir, bu nedenle görünüm temkinli ve yön sinyalleri çelişki
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
