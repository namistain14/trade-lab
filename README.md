# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 17.11.2026 22:39 (İstanbul)

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
| Net kâr/zarar | -55.96 $ | -510.70 $ |
| İşlem sayısı | 1 | 114 |
| Kazanma oranı | %0.0 | %41.2 |
| Ödenen komisyon/spread | 11.94 $ | 1354.61 $ |

**Hesap değeri: 4,517.58 $** (başlangıç 5,000 $, -482.42 $ / %-9.65)

Açık pozisyonlar: PAXGUSDT short @ 3845.81 (TP 3834.27 / SL 3853.50)

Son haber analizi (17.11 21:08): Claude puan **-0.40**, güven 0.55 — Altın yıllık en düşük seviyesine yakın işlem görürken dolar ve tahvil getirileri yükseliyor ve faiz artırımı beklentileri fiyatlamaya devam ediyor; bu, kısa vadede altın için baskılayıcı bir tablo. İran ve Ukrayna'daki savaş haberleri güvenli liman talebini destekleyebilir ancak mevcut fiyat hareketinde bu etkinin zayıf kaldığı görülüyor.

GPT (gpt-6-luna): puan **-0.25**, güven 0.48 — Altın, yükselen dolar ve tahvil getirileri ile faiz artırımı beklentileri nedeniyle baskı altında; Meksika Merkez Bankası yetkilisinin enflasyon riskleri vurgusu da hafifçe olumsuz. İran ve Ukrayna başlıkları güvenli liman talebini destekleyebilir, ancak yeni ve ani bir tırmanış göstermedikleri için

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 17.11 21:41 | PAXGUSDT | long | -55.96 $ | stop |
| 13.11 19:25 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 18:39 | PAXGUSDT | short | +69.05 $ | take profit |
| 13.11 17:32 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 16:56 | PAXGUSDT | short | -55.98 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -123.04 $ |
| İşlem sayısı | 0 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 0.00 $ | 70.51 $ |

**Hesap değeri: 4,876.96 $** (başlangıç 5,000 $, -123.04 $ / %-2.46)

Son haber analizi (17.11 08:00): Claude puan **-0.30**, güven 0.50 — Hormuz'daki tanker saldırıları ve mayın isabeti arz riskini artırıp fiyatı destekliyor, ancak piyasa bunu görmezden gelip Goldman'ın 2027'ye kadar büyük arz fazlası öngörüsü, Hormuz sevkiyatlarının iyileşmesi ve dolar güçlenmesi nedeniyle Brent'i 92 doların altına çekti. Haber akışı net olarak fiyatı aşağı çekiyor, ancak jeopolitik risk yüksek olduğundan güven orta düzeyde.

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
| Net kâr/zarar | +0.00 $ | +11832.47 $ |
| İşlem sayısı | 0 | 48 |
| Kazanma oranı | %0.0 | %52.1 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 112,753.12 $** (başlangıç 100,000 $, +12753.12 $ / %+12.75)

Açık pozisyonlar: NVDA long @ 154.28 (TP 156.76 / SL 152.90); QQQ long @ 655.92 (TP 665.89 / SL 649.49); TSLA long @ 380.84 (TP 386.76 / SL 377.23)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 13.11 23:33 | AAPL | long | -1154.98 $ | stop |
| 13.11 20:09 | TSLA | short | -1169.49 $ | stop |
| 13.11 18:11 | QQQ | short | +1751.13 $ | take profit |
| 13.11 17:37 | NVDA | short | +1722.12 $ | take profit |
| 12.11 23:46 | SPY | long | -466.64 $ | seans sonu |

## Son olaylar

```
17.11 20:55 B6  karar turu: Claude «Endeksler %1'in üzerinde ekside ve öğleden sonra yatay-zayıf konsolide oluyor; tepkiler satış fırsatı olarak değerlendiriliyor.» / GPT «Endekslerde günlük satış baskısı sürerken son saat yatay; yeni işlemde göreli zayıflık gösteren hisselerde seçici kısa pozisyonları tercih ediyorum.»
17.11 20:56 N  NEWS (40 new) score -0.40 conf 0.55: Altın bir yılın en düşük seviyesinde, ABD doları ve tahvil getirileri yükselirken toparlanmakta zorlanıyor; faiz artırımı beklentileri de baskı yaratıyor. Savaş ve jeopolitik haberleri (İran, Kırım köprüsü saldırısı) güvenli liman talebini kısmen destekliyor olsa da, bu etki ana baskı olan güçlü dolar ve sıkı para politikası beklentileri karşısında sınırlı kalıyor.
17.11 20:56 N  GPT  score -0.25 conf 0.46: Altın için kısa vadede dolar ve yükselen getirilerin yarattığı baskı, jeopolitik risklerden gelebilecek güvenli liman talebinden ağır basıyor. Doların kâr satışlarıyla geri çekilmesi ve savaş başlıkları düşüşü sınırlayabilir; haber akışı bu nedenle karışık.
17.11 21:08 N  NEWS (7 new) score -0.40 conf 0.55: Altın yıllık en düşük seviyesine yakın işlem görürken dolar ve tahvil getirileri yükseliyor ve faiz artırımı beklentileri fiyatlamaya devam ediyor; bu, kısa vadede altın için baskılayıcı bir tablo. İran ve Ukrayna'daki savaş haberleri güvenli liman talebini destekleyebilir ancak mevcut fiyat hareketinde bu etkinin zayıf kaldığı görülüyor.
17.11 21:08 N  GPT  score -0.25 conf 0.48: Altın, yükselen dolar ve tahvil getirileri ile faiz artırımı beklentileri nedeniyle baskı altında; Meksika Merkez Bankası yetkilisinin enflasyon riskleri vurgusu da hafifçe olumsuz. İran ve Ukrayna başlıkları güvenli liman talebini destekleyebilir, ancak yeni ve ani bir tırmanış göstermedikleri için
17.11 21:08 B6  karar turu: Claude «Piyasa yaklaşık %1 ekside ve son bir saatte dengelenmiş durumda; belirgin bir katalizör olmadan kapanışa kadar yatay ile hafif tepki alımları bekleniyor.» / GPT «Endekslerde günlük satışın ardından dar bantta dengelenme görülüyor; 1:4 kaldıraçla mevcut fiyatlardan yön kovalamak yerine yeni bir kırılma beklemek daha disiplinli.»
17.11 21:20 B6  karar turu: Claude «Piyasa genel olarak satış baskısı altında; düşük momentumla aşağı eğilimli yatay bir seyir izliyor.» / GPT «Endekslerde aşağı eğilim sürüyor; taze şirket haberi bulunmadığından mevcut pozisyonlara ek piyasa riski sınırlı tutulmalı.»
17.11 21:32 B6  karar turu: Claude «Piyasa günü ekside geçiriyor ancak son saatte ılımlı bir tepki alımı var; seçici ve temkinli alım tarafı öne çıkıyor.» / GPT «Endekslerde gün içi kayıplara rağmen son bölümde toparlanma güçleniyor; yükseliş yönünde sınırlı avantaj var ancak kaldıraç dönüş riskini büyütüyor.»
17.11 21:40 B5  CLOSE long stop: -55.96 USD
17.11 21:44 B6  karar turu: Claude «Piyasa günü yaklaşık %1,2 düşüşle geçiriyor ve öğleden sonraki tepki alımları satışla karşılanıyor, kapanışa doğru hafif negatif eğilim sürebilir.» / GPT «Başarısız tepki yükselişi aşağı yönü destekliyor ancak dar saatlik hareketler ve kapanışa kalan 77 dakika, yüzde 1,5 hedefe ulaşmayı zorlaştırıyor.»
17.11 21:47 B5  SHORT gold 25000 USD x10 @ 3845.81 (TP 3834.27, SL 3853.50; news -0.33)
17.11 21:56 B6  karar turu: Claude «Piyasa %1'in üzerinde ekside ve yatay-aşağı seyrediyor; son saatte toparlanma zayıf kaldı, kapanışa doğru hafif satış baskısı bekleniyor.» / GPT «Genel görünüm aşağı yönlü; ancak normal seansın bitimine yaklaşık 64 dakika kalması, yüzde 1,5 kâr hedefine ulaşma olasılığını sınırlıyor.»
17.11 22:08 B6  karar turu: Claude «Piyasa günü yaklaşık %1 düşüşle geçiriyor ve son saatte dengelenmiş görünüyor; kapanışa doğru şirkete özgü olumlu haberler seçici fırsat sunabilir.» / GPT «Piyasa zayıf ve dar bantta; normal seansın kapanmasına 52 dakika kaldığından 1–3 saatlik hedef seans dışına taşabilir ve 1:4 kaldıraç riski büyütür.»
17.11 22:20 B6  karar turu: Claude «Piyasa günü yaklaşık %1 ekside geçiriyor ancak son saatte satış baskısı durulmuş ve kapanış öncesi hafif tepki alımları görülüyor.» / GPT «Endeksler zayıf ve yönsüz olduğundan şirkete özgü taze katalizörler öncelikli; normal seansın kapanmasına 40 dakika kalması, 1–3 saatlik tutuşta seans sonrası likidite ve braket emirlerinin geçerliliğini önemli kılıyor.»
17.11 22:32 B6  karar turu: Claude «Piyasa gün genelinde zayıf ama son saatte satış baskısı azaldı ve fiyatlar yatay seyrediyor; kapanışa kadar şirkete özgü olumlu haberler öne çıkabilir.» / GPT «Piyasa zayıf; normal seansın kapanmasına 28 dakika kaldığından 1–3 saatlik işlemler seans dışına taşabilir ve dört kat kaldıraçta stop fiyatından gerçekleşme garanti değildir.»
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
