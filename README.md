# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 29.10.2026 20:27 (İstanbul)

## Bot A — Kripto kurallar (x3 çarpan, sık işlem)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -3.78 $ | -15.07 $ |
| İşlem sayısı | 2 | 6 |
| Kazanma oranı | %50.0 | %50.0 |
| Ödenen komisyon/spread | 11.94 $ | 19.93 $ |

**Hesap değeri: 4,975.36 $** (başlangıç 5,000 $, -24.64 $ / %-0.49)

Açık pozisyonlar: BTCUSDT long @ 81120.97 (TP 81607.69 / SL 80796.49); XRPUSDT long @ 1.30 (TP 1.31 / SL 1.29)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 29.10 16:31 | BNBUSDT | long | +27.93 $ | take profit |
| 29.10 14:24 | BNBUSDT | long | -31.71 $ | stop |
| 28.10 16:31 | BTCUSDT | long | -6.29 $ | stop |
| 25.10 17:28 | BTCUSDT | long | +0.99 $ | time limit |
| 25.10 09:51 | SOLUSDT | long | -6.29 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -55.94 $ | -55.94 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 11.86 $ | 11.86 $ |

**Hesap değeri: 4,966.29 $** (başlangıç 5,000 $, -33.71 $ / %-0.67)

Açık pozisyonlar: PAXGUSDT short @ 4029.87 (TP 4017.78 / SL 4037.93)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 29.10 16:36 | PAXGUSDT | short | -55.94 $ | stop |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 99,629.59 $** (başlangıç 100,000 $, -370.41 $ / %-0.37)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
29.10 17:39 B6  karar turu: Claude «Piyasa, Alphabet ve yazılım kaynaklı teknoloji satışının ardından açılış düşüşünü sindirip dengelenmeye çalışıyor; göreceli güçlü hisseler öne çıkıyor.» / GPT «Teknoloji endeksi zayıf olsa da satış baskısı son saatte hafifliyor; dört kat kaldıraç altında endekslerden ziyade göreli güç gösteren TSLA'da seçici alımı tercih ediyorum.»
29.10 17:39 B6  ALIŞ TSLA 245 adet ≈ 99,544 $ (1:4) @ 406.3 (TP 412.39, SL 402.24; ikisi de hemfikir, güven 0.56)
29.10 18:36 N  NEWS (37 new) score -0.30 conf 0.50: Fed faizleri sabit tuttu ancak Hassett, Ekim enflasyonu yüksek gelirse Fed'in harekete geçebileceğini söyledi; Eylül PCE enflasyonu yükseldi ve 6% tahvil getirisi tezi gerçek faizleri yukarı taşıyarak altı baskılıyor. İran savaşı ve olası yeni saldırı haberleri jeopolitik talebi destekliyor, ancak etkisi sınırlı kalıyor ve haberlerin büyük kısmı zaten fiyatlanmış durumda.
29.10 18:36 N  GPT  score -0.28 conf 0.58: Güçlü büyüme ve yükselen enflasyon verileri, Fed’in daha sıkı kalabileceği ve tahvil getirilerinin yükselebileceği beklentisini destekleyerek altını kısa vadede baskılıyor. İran savaşı ve olası yeni saldırılar güvenli liman talebi yaratsa da bu etki, faiz baskısıyla kısmen dengeleniyor.
29.10 18:36 B5  SHORT gold 25000 USD x10 @ 4029.87 (TP 4017.78, SL 4037.93; news -0.29)
29.10 18:36 B6  karar turu: Claude «Alphabet'in sert düşüşü Nasdaq'ı baskılasa da beklentiyle uyumlu PCE ve güçlü GDP verisi sonrası piyasa gün içi dipten kademeli olarak toparlanıyor.» / GPT «Endekslerde kısa vadeli toparlanma alımları öne çıkarken Alphabet kaynaklı teknoloji baskısı nedeniyle yükselişi güçlü trend değil, kırılgan tepki hareketi olarak değerlendiriyorum.»
29.10 19:32 N  NEWS (37 new) score -0.40 conf 0.50: Fed faizleri sabit tuttu ama enflasyon yüksek (3.7%) ve piyasalar yıl sonuna kadar faiz artırımı ihtimalini fiyatlıyor; bu, reel faizler ve dolar açısından altın için baskı yaratıyor. Gold'un 100 saatlik ortalamanın altına inmesi de kısa vadeli zayıflığa işaret ediyor; İran savaşı ile ilgili jeopolitik haberler ise büyük çoğunlukla bilinen ve fiyatlanmış nitelikte, bu yüzden güvenli liman talebini belirgin biçimde artırmıyor.
29.10 19:32 N  GPT  score -0.32 conf 0.58: ABD’de güçlü büyüme ve %3,7 enflasyon faizlerin yüksek kalacağı beklentisini destekliyor; altının saatlik ortalamanın altına gerilemesi kısa vadede baskıya işaret ediyor. Enflasyonun beklentiyle uyumlu olması ve İran kaynaklı jeopolitik riskler düşüşü sınırlayabilir.
29.10 19:32 B6  karar turu: Claude «Endeksler hafif ekside; Alphabet kaynaklı teknoloji zayıflığı Nasdaq'ı aşağı çekerken defansif sektörler ve küçük ölçekli hisseler güçlü GDP verisiyle destek buluyor.» / GPT «Teknoloji hisselerinde aşağı yönlü baskı sürerken geniş piyasa daha dirençli; dört kat kaldıraçta mevcut teknoloji pozisyonlarıyla toplam risk gözetilmeli.»
29.10 19:32 B6  QQQ emir reddedildi: Alpaca POST /v2/orders: 403 {"buying_power":"0","code":40310000,"cost_basis":"102355.11","message":"insufficient buying power"}
29.10 20:27 A  BUY BTCUSDT 5982 USD x3 @ 81120.97 (RSI 43)
29.10 20:27 A  BUY XRPUSDT 5982 USD x3 @ 1.30 (RSI 42)
29.10 20:27 N  NEWS (36 new) score -0.30 conf 0.50: 
29.10 20:27 N  GPT  score -0.25 conf 0.56: Eylül enflasyonunun ve çekirdek PCE’nin hızlandığı haberleri Fed’in daha temkinli kalacağı beklentisini güçlendirerek altın üzerinde baskı yaratabilir. İran ve Ukrayna kaynaklı riskler güvenli liman talebini desteklese de haberler büyük ölçüde süregelen gelişmeler ve kısa vadeli yön net değil.
29.10 20:27 B6  karar turu: Claude «Piyasa, Alphabet'in sert düşüşü nedeniyle teknoloji ağırlıklı zayıf seyrediyor ancak güçlü GDP verisiyle öğleden sonra yatay konsolide oluyor; İran gelişmeleri aşağı yönlü risk taşıyor.» / GPT «Piyasa yatay sıkışırken teknoloji hisseleri görece zayıf; dar saatlik bantlar yüzde 1,5 hedefe ulaşmayı zorlaştırıyor ve 1:4 kaldıraç riski büyütüyor.»
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
