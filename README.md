# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 02.11.2026 22:07 (İstanbul)

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
| Net kâr/zarar | -111.90 $ | -33.24 $ |
| İşlem sayısı | 2 | 14 |
| Kazanma oranı | %0.0 | %42.9 |
| Ödenen komisyon/spread | 23.81 $ | 166.57 $ |

**Hesap değeri: 4,952.36 $** (başlangıç 5,000 $, -47.64 $ / %-0.95)

Açık pozisyonlar: PAXGUSDT long @ 3959.62 (TP 3971.50 / SL 3951.70)

Son haber analizi (02.11 22:01): Claude puan **-0.20**, güven 0.40 — ABD-İran barış görüşmeleri ve Hürmüz'ün yeniden açılma ihtimali, jeopolitik risk primini düşürerek altın için güvenli liman talebini zayıflatıyor. Petrol fiyatlarının %7'den fazla düşmesi ise enflasyon beklentilerini aşağı çekerek faiz indirimi beklentilerini destekleyip altı kısmen dengeliyor; net etki hafif negatif, düşük güven.

GPT (gpt-6-luna): puan **-0.35**, güven 0.62 — ABD-İran ateşkes görüşmelerindeki ilerleme ve Hürmüz Boğazı’nın yeniden açılabileceği beklentisi petrolü sert düşürerek güvenli liman talebini ve enflasyon endişelerini azaltıyor; bu, altın için kısa vadede hafif aşağı yönlü. Ukrayna’daki ölümcül saldırı ters yönde risk yaratıyor ve gelişmelerin çel

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 20:28 | PAXGUSDT | long | -55.93 $ | stop |
| 02.11 08:08 | PAXGUSDT | short | -55.97 $ | stop |
| 31.10 00:48 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 23:07 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 20:35 | PAXGUSDT | short | +69.06 $ | take profit |

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

**Hesap değeri: 100,480.56 $** (başlangıç 100,000 $, +480.56 $ / %+0.48)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
02.11 21:06 B6  karar turu: Claude «Petroldeki düşüş ve jeopolitik iyimserlik geniş piyasayı destekliyor, ancak teknoloji hisseleri AI değerleme endişeleri ve Apple bilançosu öncesi geride kalıyor.» / GPT «Endeksler gün içi diplerden tepki veriyor ancak saatlik momentum zayıf; 4 kat kaldıraçla mevcut hareketi kovalamak yerine yeni işlem açmıyorum.»
02.11 21:18 N  NEWS (11 new) score +0.25 conf 0.40: Petrol fiyatlarının düşmesi, Fed sıkılaştırma beklentilerini azaltıp dolarda zayıflama yaratarak altı destekliyor; altın bir yıllık dipten yaklaşık %2 toparlandı. Ancak ABD-İran barış görüşmelerinin yoğunlaşması güvenli liman talebini zayıflatıyor ve El Nino kaynaklı enflasyon riski ile OPEC+ endişeleri bu tabloyu karışık hale getiriyor. Bu nedenle hafif pozitif, düşük-orta güvenli bir görünüm.
02.11 21:18 N  GPT  score +0.30 conf 0.57: Petrol fiyatlarındaki geri çekilme ve doların zayıflaması, Fed’in daha şahin fiyatlanması riskini azaltarak altını destekliyor; Ukrayna’daki ölümcül saldırı da güvenli liman talebini artırabilir. Ancak ABD-İran görüşmelerinin sürmesi jeopolitik risk primini sınırlayabilir; kısa vadeli etki bu nedenl
02.11 21:18 B6  karar turu: Claude «Piyasa İran barış umutlarıyla ılımlı pozitif, ancak yapay zeka değerleme endişeleri Nasdaq'ı S&P 500'ün gerisinde tutuyor.» / GPT «Endeksler dar bantta yön arıyor; mevcut hareketler 1:4 kaldıraçla yeni pozisyon açmak için yeterli avantaj göstermiyor.»
02.11 21:37 N  NEWS (18 new) score +0.10 conf 0.35: 
02.11 21:37 N  GPT  score -0.25 conf 0.57: ABD-İran görüşmelerinin savaşı önleyebileceği ve Hürmüz’ün yeniden açılabileceği haberleri petrolü sert düşürerek güvenli liman ve enflasyon kaynaklı altın talebini azaltabilir. Ukrayna’daki ölümcül saldırı altına destek sağlıyor; bu nedenle kısa vadeli net etki sınırlı ölçüde negatif görünüyor.
02.11 21:37 B6  karar turu: Claude «Piyasa İran barış umutlarıyla hafif pozitif seyrediyor ancak teknoloji hisseleri yatay ve zayıf; geniş endekslerde sınırlı bir yükseliş eğilimi var.» / GPT «Endekslerde momentum zayıflarken teknoloji tarafındaki göreli güçsüzlük seçici kısa pozisyonu destekliyor; 14:37 itibarıyla işlemler kapanıştan önce sonlandırılmalı.»
02.11 21:49 N  NEWS (8 new) score -0.10 conf 0.40: ABD-İran barış görüşmeleri ve Hürmüz'ün yeniden açılma ihtimali, jeopolitik risk primini düşürerek altın için güvenli liman talebini zayıflatıyor. Petrol fiyatlarının %7'den fazla düşmesi ise enflasyon beklentilerini aşağı çekerek faiz indirimi beklentilerini destekleyip altı kısmen dengeliyor; net etki hafif negatif, düşük güven.
02.11 21:49 N  GPT  score -0.25 conf 0.42: ABD-İran görüşmelerinin savaş riskini azaltması ve petrolün sert düşmesi, güvenli liman talebini zayıflatarak altın için kısa vadede hafif baskı yaratabilir. Ukrayna’daki ölümcül saldırı bunu kısmen dengeliyor; 2027’ye ilişkin enflasyon haberi ise 1-4 saatlik görünüm için uzak ve etkisi sınırlı.
02.11 21:49 B6  karar turu: Claude «Endeksler İran barış umudu ve düşen petrolle desteklenirken teknoloji tarafında AI şüpheciliği ve Apple bilanço öncesi temkin zayıflık yaratıyor.» / GPT «Endekslerde gün içi momentum aşağı dönüyor; taze şirket haberi bulunmadığından kapanışa yakın kaldıraçlı işlemlerde avantaj sınırlı.»
02.11 21:49 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"102999.24","message":"insufficient buying power"}
02.11 22:01 N  NEWS (5 new) score -0.20 conf 0.40: 
02.11 22:01 N  GPT  score -0.35 conf 0.62: ABD-İran ateşkes görüşmelerindeki ilerleme ve Hürmüz Boğazı’nın yeniden açılabileceği beklentisi petrolü sert düşürerek güvenli liman talebini ve enflasyon endişelerini azaltıyor; bu, altın için kısa vadede hafif aşağı yönlü. Ukrayna’daki ölümcül saldırı ters yönde risk yaratıyor ve gelişmelerin çel
02.11 22:01 B6  karar turu: Claude «Petrol düşüşü ve İran barış umutları döngüsel hisseleri desteklerken teknoloji ve AI hisseleri gün sonuna doğru satış baskısı altında; Nasdaq'ta hafif düşüş eğilimi öne çıkıyor.» / GPT «Teknoloji öncülüğündeki satış baskısı kısa yönü destekliyor; ancak normal seansın bitmesine 59 dakika kalması ve 4 kat kaldıraç riski artırıyor.»
02.11 22:01 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"103470.47","message":"insufficient buying power"}
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
