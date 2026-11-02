# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 02.11.2026 19:16 (İstanbul)

## Bot A — Kripto TERS (alım sinyalinde satış, x3)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -267.62 $ | -1022.76 $ |
| İşlem sayısı | 18 | 79 |
| Kazanma oranı | %16.7 | %19.0 |
| Ödenen komisyon/spread | 74.61 $ | 350.21 $ |

**Hesap değeri: 3,977.24 $** (başlangıç 5,000 $, -1022.76 $ / %-20.46)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 16:39 | BNBUSDT | short | -25.72 $ | stop |
| 02.11 16:38 | ETHUSDT | short | -12.86 $ | stop |
| 02.11 16:39 | BTCUSDT | short | -25.72 $ | stop |
| 02.11 15:31 | BNBUSDT | short | -1.73 $ | time limit |
| 02.11 15:10 | XRPUSDT | short | -12.99 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -55.97 $ | +22.70 $ |
| İşlem sayısı | 1 | 13 |
| Kazanma oranı | %0.0 | %46.2 |
| Ödenen komisyon/spread | 11.92 $ | 154.68 $ |

**Hesap değeri: 5,022.70 $** (başlangıç 5,000 $, +22.70 $ / %+0.45)

Son haber analizi (02.11 19:16): Claude puan **+0.10**, güven 0.40 — Yeni haberler karışık ama hafif negatif ağırlıklı: ABD imalat PMI beklentinin altında kalsa da satış fiyatı enflasyonu Eylül 2022'den bu yana en yüksek seviyede ve OCBC Fed sıkılaştırma endişeleri nedeniyle altın tahminini düşürdü; İran'la müzakerelerde kopuş olmaması ve Hamaney'in hükümete müzakere yetkisi vermesi de güvenli liman talebini sınırlıyor. Öte yandan Doların aşırı alım bölgesinde olması ve bazı analistlerin toparlanma beklentisi, düşüşü sınırlayabilir; eski haberler ve çelişkili sinyaller güveni düşürüyor.

GPT (gpt-6-luna): puan **+0.22**, güven 0.38 — Altın fiyatındaki yaklaşık %2’lik yükseliş ve düşük reel getirilerin destekleyici olduğuna dair haberler kısa vadede hafif pozitif. Ancak Orta Doğu’da barış umuduyla petrolün gerilemesi güvenli liman talebini azaltabilir; karışık dolar ve enflasyon sinyalleri görünümü belirsiz kılıyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 08:08 | PAXGUSDT | short | -55.97 $ | stop |
| 31.10 00:48 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 23:07 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 20:35 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 18:48 | PAXGUSDT | short | +69.06 $ | take profit |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

Son haber analizi (02.11 08:00): Claude puan **+0.15**, güven 0.40 — Hürmüz Boğazı'nda iki tankerin mayına çarpıp patlaması arz riskini ciddi biçimde artırdığı için kısa vadede yukarı yönlü baskı yaratabilir. Ancak İran-ABD müzakerelerine ilişkin haberler fiyatları son saatlerde yüzde 3 civarında aşağı çekti ve haberler birbiriyle çelişkili; Goldman'ın tahmin artırımı ise büyük ölçüde fiyatlanmış durumda. Bu nedenle sinyal zayıf ve yönü belirsiz.

GPT (gpt-6-luna): puan **+0.20**, güven 0.48 — Hürmüz Boğazı’nda iki tankerin mayına çarparak patladığına dair yeni haber, doğrulanması hâlinde kısa vadede arz ve taşımacılık risk primini artırabilir. Ancak İran’la diplomasi haberleriyle petrolün zaten %3’ten fazla gerilemesi ve Ceyhan ihracatındaki artış bu yükseliş etkisini sınırlıyor.

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 101,628.67 $** (başlangıç 100,000 $, +1628.67 $ / %+1.63)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
02.11 18:19 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"99688.17","message":"insufficient buying power"}
02.11 18:40 N  NEWS (16 new) score -0.20 conf 0.40: Yeni haberler karışık ama hafif negatif ağırlıklı: ABD imalat PMI beklentinin altında kalsa da satış fiyatı enflasyonu Eylül 2022'den bu yana en yüksek seviyede ve OCBC Fed sıkılaştırma endişeleri nedeniyle altın tahminini düşürdü; İran'la müzakerelerde kopuş olmaması ve Hamaney'in hükümete müzakere yetkisi vermesi de güvenli liman talebini sınırlıyor. Öte yandan Doların aşırı alım bölgesinde olması ve bazı analistlerin toparlanma beklentisi, düşüşü sınırlayabilir; eski haberler ve çelişkili sinyaller güveni düşürüyor.
02.11 18:40 N  GPT  score -0.15 conf 0.38: Savaşın sona ermesine yönelik temaslar sürse de anlaşma çıkmaması güvenli liman talebini destekliyor; buna karşılık üretici fiyat enflasyonunun yüksek seyri Fed’in sıkı kalacağı beklentisini güçlendirerek altına baskı yapabilir. Etkiler çelişkili ve haberlerin bir kısmı zaten fiyatlanmış göründüğünd
02.11 18:40 B6  karar turu: Claude «Güçlü ISM verisi ve Hürmüz umutlarıyla piyasa ılımlı pozitif seyrediyor, ancak AI harcama endişeleri ve akşamki bilançolar yukarı potansiyeli sınırlayabilir.» / GPT «Piyasa yönü pozitif olsa da son ivme kaybı ve karışık makro veriler nedeniyle 1:4 kaldıraçta sınırlı pozisyon büyüklüğü tercih edilmeli.»
02.11 18:40 B6  SPY emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"100684.33","message":"insufficient buying power"}
02.11 18:52 N  NEWS (7 new) score +0.10 conf 0.35: 
02.11 18:52 N  GPT  score +0.25 conf 0.43: İranlı vekillerin savaşı genişletme tehdidi ve tüketici harcamalarındaki zayıflık altına sınırlı destek sağlayabilir. Ancak savaşın sona erdirilmesine yönelik temaslar sürüyor ve yüksek girdi fiyatları faiz indirimi beklentilerini sınırlayabilir; bu nedenle etki belirsiz.
02.11 18:52 B6  karar turu: Claude «Piyasa güçlü ISM verisi ve İran müzakere umutlarıyla pozitif seyrediyor, ancak öğle saatlerinde ivme zayıflıyor.» / GPT «Endeksler günlük kazanımlarını korusa da son yarım saatte ivme zayıflıyor; teknoloji ağırlıklı endekste seçici kısa pozisyonu tercih ediyorum.»
02.11 19:04 N  NEWS (8 new) score -0.10 conf 0.35: 
02.11 19:04 N  GPT  score +0.25 conf 0.43: İran’da savaşın genişleyebileceğine dair tehditler ve görüşmelerden sonuç çıkmaması güvenli liman talebini destekleyebilir; doların borç maliyetleri nedeniyle baskı görebileceği beklentisi de altın için olumlu. Ancak görüşmelerin sürmesi, Fed sıkılaşması endişeleri ve altının önceki sert düşüş sonra
02.11 19:04 B6  karar turu: Claude «Piyasa güçlü ISM verisiyle pozitif açıldı ancak öğle saatlerinde zirveden geri çekilip yatay seyre geçti; jeopolitik riskler ve Apple bilançosu öncesi temkinli bir görünüm hakim.» / GPT «Endeksler günlük kazançlarını korusa da son bölümdeki ivme kaybı kısa vadede temkinli satış yönünü destekliyor; dört kat kaldıraçta pozisyon büyüklüğü sınırlı tutulmalı.»
02.11 19:16 N  NEWS (12 new) score +0.10 conf 0.40: 
02.11 19:16 N  GPT  score +0.22 conf 0.38: Altın fiyatındaki yaklaşık %2’lik yükseliş ve düşük reel getirilerin destekleyici olduğuna dair haberler kısa vadede hafif pozitif. Ancak Orta Doğu’da barış umuduyla petrolün gerilemesi güvenli liman talebini azaltabilir; karışık dolar ve enflasyon sinyalleri görünümü belirsiz kılıyor.
02.11 19:16 B6  karar turu: Claude «Sabahki yükseliş öğlene doğru sönümleniyor; teknoloji öncülüğünde hafif satış baskısı ve jeopolitik riskler kısa vadede aşağı yönlü eğilimi öne çıkarıyor.» / GPT «Endeksler günlük artıda olsa da saatlik satış eğilimi kısa yönünü destekliyor; iki pozisyonun yüksek korelasyonu nedeniyle toplam kaldıraç riski sınırlanmalı.»
02.11 19:16 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"104434.41","message":"insufficient buying power"}
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
