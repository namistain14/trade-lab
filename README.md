# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 02.11.2026 22:38 (İstanbul)

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
| Net kâr/zarar | -167.84 $ | -89.18 $ |
| İşlem sayısı | 3 | 15 |
| Kazanma oranı | %0.0 | %40.0 |
| Ödenen komisyon/spread | 35.70 $ | 178.46 $ |

**Hesap değeri: 4,910.82 $** (başlangıç 5,000 $, -89.18 $ / %-1.78)

Son haber analizi (02.11 22:37): Claude puan **+0.05**, güven 0.30 — ABD-İran barış görüşmeleri ve Hürmüz'ün yeniden açılma ihtimali, jeopolitik risk primini düşürerek altın için güvenli liman talebini zayıflatıyor. Petrol fiyatlarının %7'den fazla düşmesi ise enflasyon beklentilerini aşağı çekerek faiz indirimi beklentilerini destekleyip altı kısmen dengeliyor; net etki hafif negatif, düşük güven.

GPT (gpt-6-luna): puan **+0.18**, güven 0.40 — Ukrayna’daki yardım merkezine yönelik ölümcül saldırı kısa vadede güvenli liman talebini destekleyebilir. Buna karşılık ABD-İran görüşmelerindeki ilerleme ve petrol fiyatlarındaki sert düşüş jeopolitik risk primini azaltıyor; net etki sınırlı ve karışık görünüyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 22:22 | PAXGUSDT | long | -55.94 $ | stop |
| 02.11 20:28 | PAXGUSDT | long | -55.93 $ | stop |
| 02.11 08:08 | PAXGUSDT | short | -55.97 $ | stop |
| 31.10 00:48 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 23:07 | PAXGUSDT | short | -55.97 $ | stop |

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

**Hesap değeri: 100,272.90 $** (başlangıç 100,000 $, +272.90 $ / %+0.27)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
02.11 21:49 B6  karar turu: Claude «Endeksler İran barış umudu ve düşen petrolle desteklenirken teknoloji tarafında AI şüpheciliği ve Apple bilanço öncesi temkin zayıflık yaratıyor.» / GPT «Endekslerde gün içi momentum aşağı dönüyor; taze şirket haberi bulunmadığından kapanışa yakın kaldıraçlı işlemlerde avantaj sınırlı.»
02.11 21:49 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"102999.24","message":"insufficient buying power"}
02.11 22:01 N  NEWS (5 new) score -0.20 conf 0.40: 
02.11 22:01 N  GPT  score -0.35 conf 0.62: ABD-İran ateşkes görüşmelerindeki ilerleme ve Hürmüz Boğazı’nın yeniden açılabileceği beklentisi petrolü sert düşürerek güvenli liman talebini ve enflasyon endişelerini azaltıyor; bu, altın için kısa vadede hafif aşağı yönlü. Ukrayna’daki ölümcül saldırı ters yönde risk yaratıyor ve gelişmelerin çel
02.11 22:01 B6  karar turu: Claude «Petrol düşüşü ve İran barış umutları döngüsel hisseleri desteklerken teknoloji ve AI hisseleri gün sonuna doğru satış baskısı altında; Nasdaq'ta hafif düşüş eğilimi öne çıkıyor.» / GPT «Teknoloji öncülüğündeki satış baskısı kısa yönü destekliyor; ancak normal seansın bitmesine 59 dakika kalması ve 4 kat kaldıraç riski artırıyor.»
02.11 22:01 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"103470.47","message":"insufficient buying power"}
02.11 22:13 N  NEWS (11 new) score -0.15 conf 0.40: 
02.11 22:13 N  GPT  score -0.18 conf 0.36: İran yönetiminin görüşmelere yetki vermesi ve hızlandırılmış ateşkes girişimi, kısa vadede savaş kaynaklı güvenli liman talebini azaltarak altını hafifçe baskılayabilir. Ancak haberler henüz anlaşma değil ve Ukrayna’daki saldırılar gibi karşıt riskler etkisini sınırlıyor.
02.11 22:13 B6  karar turu: Claude «Piyasa gün sonuna doğru teknoloji ağırlıklı bir zayıflık gösteriyor; döngüsel sektörler ise İran barış umutları ve petrol düşüşüyle destekleniyor.» / GPT «Kısa vadeli yön aşağı; ancak normal seansın bitmesine 47 dakika kalması yüzde 1,5 hedefini zorlaştırırken, iki endeksin yüksek korelasyonu 4 kat kaldıraçla toplam riski artırıyor.»
02.11 22:13 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"102678.14","message":"insufficient buying power"}
02.11 22:38 B5  CLOSE long stop: -55.94 USD
02.11 22:38 N  NEWS (10 new) score +0.05 conf 0.30: 
02.11 22:38 N  GPT  score +0.18 conf 0.40: Ukrayna’daki yardım merkezine yönelik ölümcül saldırı kısa vadede güvenli liman talebini destekleyebilir. Buna karşılık ABD-İran görüşmelerindeki ilerleme ve petrol fiyatlarındaki sert düşüş jeopolitik risk primini azaltıyor; net etki sınırlı ve karışık görünüyor.
02.11 22:38 B6  karar turu: Claude «Petroldeki düşüş ve İran barış umutlarına rağmen teknoloji ağırlıklı satışlar kapanışa doğru endeksleri aşağı çekiyor; kısa vadeli eğilim hafif negatif.» / GPT «Teknoloji hisselerinde satış baskısı baskın; ancak kapanışa 23 dakika kalması ve İran haberleri, 4 kat kaldıraçla kapanış sonrası taşınacak pozisyonlarda likidite ve ters hareket riskini artırıyor.»
02.11 22:38 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"102887","message":"insufficient buying power"}
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
