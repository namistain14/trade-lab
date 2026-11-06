# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 06.11.2026 11:17 (İstanbul)

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
| Net kâr/zarar | -335.82 $ | -369.77 $ |
| İşlem sayısı | 6 | 58 |
| Kazanma oranı | %0.0 | %39.7 |
| Ödenen komisyon/spread | 71.06 $ | 688.52 $ |

**Hesap değeri: 4,630.23 $** (başlangıç 5,000 $, -369.77 $ / %-7.40)

Son haber analizi (06.11 11:14): Claude puan **-0.20**, güven 0.40 — Başlıkların çoğu gündelik veya Dhanteras odaklı gürültü. Fed faiz artırımı beklentisi, %3,7 enflasyon ve Goldman'ın hedef indirimi altını baskılarken, dolardaki yükseliş ve ABD NFP verisi öncesi belirsizlik kısa vadeli görünümü negatife çeviriyor. Buna karşın ETF girişleri ve WGC'nin "dipe yakın" yorumu sınırlı bir destek sağlıyor; jeopolitik risk başlıkları ise belirgin bir kaçış talebi yaratmıyor.

GPT (gpt-6-luna): puan **-0.30**, güven 0.44 — Doların güçlenmesiyle altının %1’den fazla düşmesi kısa vadede aşağı yönlü momentumu destekliyor; Fed faiz artırımı riskine ilişkin beklentiler de baskı yaratabilir. Buna karşılık yeni haberlerde güçlü ve doğrudan bir piyasa katalizörü yok, bu yüzden görünümün güveni sınırlı.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 10:57 | PAXGUSDT | short | -55.94 $ | stop |
| 06.11 09:25 | PAXGUSDT | short | -55.94 $ | stop |
| 06.11 08:11 | PAXGUSDT | short | -56.23 $ | stop (gap) |
| 06.11 04:01 | PAXGUSDT | long | -55.91 $ | stop |
| 06.11 03:47 | PAXGUSDT | long | -55.90 $ | stop |

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
06.11 10:01 N  NEWS (5 new) score -0.15 conf 0.40: Altın, DXY'nin 101,80 seviyesine toparlanması ve ABD tarım dışı istihdam (NFP) raporu öncesi güçlü ABD verisi ihtimali nedeniyle baskı altında; Fed riski de sürüyor. Buna karşılık WGC'nin ara dip açıklaması, İran savaşında barış sürecinin belirsizliği ve teknoloji hisselerindeki sert düşüşten kaynaklanan güvenli liman talebi kısmen destekleyici; haberlerin çoğu zaten fiyatlanmış tekrarlar olduğu için güven düşük.
06.11 10:01 N  GPT  score -0.30 conf 0.43: ABD istihdam verisi öncesinde doların toparlanması ve altının düştüğünü bildiren çok sayıda başlık, önümüzdeki birkaç saat için baskının aşağı yönlü olduğuna işaret ediyor. WGC’nin dip oluşabileceği görüşü daha uzun vadeli ve jeopolitik haberler kısa vadede net bir güvenli liman desteği sağlamıyor.
06.11 10:13 N  NEWS (2 new) score -0.10 conf 0.35: Altın, yaklaşık %25'lik düşüşün ardından zayıf seyrediyor; DXY'nin 101,80 civarında toparlanması ve ABD tarım dışı istihdam (NFP) raporu öncesi temkinli hava kısa vadede baskı yaratıyor. Buna karşılık WGC'nin "geçici dip yakın" değerlendirmesi, ABD ara seçim sonuçlarının altına hafif olumlu olması ve İran savaşının sürmesi güvenli liman talebini destekleyebilir; bu nedenle etki sınırlı ve yön belirsiz.
06.11 10:13 N  GPT  score -0.35 conf 0.56: ABD istihdam verisi öncesinde doların güçlenmesi ve altındaki düşüş haberleri kısa vadede aşağı yönlü baskıya işaret ediyor. İran savaşı ve petrol piyasasındaki belirsizlik güvenli liman talebiyle bu baskıyı kısmen dengeleyebilir; yeni ve belirleyici bir veri henüz yok.
06.11 10:25 N  NEWS (1 new) score -0.15 conf 0.40: 
06.11 10:25 N  GPT  score -0.25 conf 0.43: Dolar endeksinin ABD istihdam verisi öncesinde güçlenmesi ve altının veri öncesi gerilemesi kısa vadede baskı yaratıyor. İran’daki barış sürecine ilişkin belirsizlik sınırlı güvenli liman talebi sağlayabilir; yaklaşan veriler ve çelişkili haberler güveni düşürüyor.
06.11 10:37 N  NEWS (4 new) score -0.30 conf 0.50: Altın için kısa vadede hafif negatif görünüm: petrol fiyatlarının yükselmesi enflasyon ve faiz artırımı endişelerini canlandırıyor, DXY toparlanıyor ve ABD tarım dışı istihdam (NFP) verisi öncesinde dolar güçleniyor. Tech hisselerindeki sert düşüş ve İran savaşı gibi güvenli liman talebini artıran unsurlar bu baskıyı kısmen dengeliyor, ancak fiyatlanmış ve çelişkili haberler güveni sınırlıyor.
06.11 10:37 N  GPT  score -0.22 conf 0.42: Altın, yükselen petrol fiyatları ve güçlenen dolar eşliğinde %1’den fazla gerilemiş; yaklaşan ABD istihdam verisi ve faiz artışı endişeleri kısa vadede baskı yaratabilir. Teknoloji hisselerindeki sert düşüş güvenli liman talebini destekleyebilir, bu nedenle görünüm temkinli ve yön sinyalleri çelişki
06.11 10:49 N  NEWS (12 new) score -0.40 conf 0.50: Altın kısa vadede baskı altında: dolar güçleniyor, petrol fiyatları yükseliyor (enflasyon ve Fed sıkılığı beklentisini besliyor) ve ABD tarım dışı istihdam (NFP) verisi öncesi tahvil/dolar hareketleri altını aşağı çekiyor. Iran'a ait füze üssü inşaatı gibi jeopolitik haberler sınırlı bir güvenli liman desteği sağlasa da, bu etki fiyatlanmış ve dolar/faiz kanalının gerisinde kalıyor. Haberlerin çoğu eski veya zaten yansıtılmış bilgiler olduğu için güven orta düzeyde.
06.11 10:49 N  GPT  score -0.40 conf 0.57: Doların güçlenmesiyle altının %1’den fazla gerilemesi ve petrol kaynaklı faiz artırımı endişeleri kısa vadede baskıyı artırıyor; yaklaşan ABD istihdam verisi oynaklık yaratabilir. İran füze üsleri çevresindeki inşaat haberleri güvenli liman talebini desteklese de etkisi belirsiz ve düşüşü şimdilik d
06.11 10:58 B5  CLOSE short stop: -55.94 USD
06.11 11:02 N  NEWS (9 new) score -0.20 conf 0.45: En yeni haberler karışık ama hafif negatif bir tablo çiziyor: dolar güçleniyor (DXY 102'ye yaklaşıyor) ve altın %1'den fazla düştü; enflasyon ve faiz artırımı endişeleri de sınırlı yükseliş beklentisi yaratıyor. İran savaşı ve Hormuz kısıtlamaları güvenli liman talebini destekliyor ancak bu etki büyük ölçüde fiyatlanmış görünüyor; ABD tarım dışı istihdam (NFP) verisi öncesi belirsizlik ve dolar hareketi kısa vadede baskı yaratabilir.
06.11 11:02 N  GPT  score -0.32 conf 0.58: Altının %1’den fazla düşmesi ve doların güçlenmesi kısa vadede aşağı yönlü momentuma işaret ediyor; yaklaşan ABD istihdam verisi de oynaklık yaratabilir. İran’daki olası askeri hazırlıklar güvenli liman talebini desteklese de doğrulanmış yeni bir tırmanış yok ve Ukrayna’da ateşkes çağrısı riskleri k
06.11 11:14 N  NEWS (11 new) score -0.20 conf 0.40: Başlıkların çoğu gündelik veya Dhanteras odaklı gürültü. Fed faiz artırımı beklentisi, %3,7 enflasyon ve Goldman'ın hedef indirimi altını baskılarken, dolardaki yükseliş ve ABD NFP verisi öncesi belirsizlik kısa vadeli görünümü negatife çeviriyor. Buna karşın ETF girişleri ve WGC'nin "dipe yakın" yorumu sınırlı bir destek sağlıyor; jeopolitik risk başlıkları ise belirgin bir kaçış talebi yaratmıyor.
06.11 11:14 N  GPT  score -0.30 conf 0.44: Doların güçlenmesiyle altının %1’den fazla düşmesi kısa vadede aşağı yönlü momentumu destekliyor; Fed faiz artırımı riskine ilişkin beklentiler de baskı yaratabilir. Buna karşılık yeni haberlerde güçlü ve doğrudan bir piyasa katalizörü yok, bu yüzden görünümün güveni sınırlı.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
