# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 02.11.2026 17:25 (İstanbul)

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

Son haber analizi (02.11 17:20): Claude puan **+0.12**, güven 0.35 — ABD-İran savaşının sürmesi ve müzakerelerin sonuçsuz bitmesi jeopolitik risk primini hafifçe destekliyor, bu da altın için sınırlı bir yükseliş yönlü etki yaratabilir. Ancak enerji kaynaklı enflasyon ve Fed'in bekle-gör duruşu ile güçlü dolar haberleri altını baskılayabileceğinden etki zayıf ve karışık kalıyor.

GPT (gpt-6-luna): puan **+0.28**, güven 0.43 — İran savaşının sürmesi ve Körfez’de savaş sigortasının daralması kısa vadeli güvenli liman talebini destekleyebilir. Ancak temasların sürmesi, diplomasi çağrıları ve petrol fiyatlarındaki gerileme bu etkiyi sınırlıyor; dolar ve faiz görünümünden net yeni bir sinyal yok.

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

**Hesap değeri: 100,898.58 $** (başlangıç 100,000 $, +898.58 $ / %+0.90)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
02.11 16:02 A  SHORT ETHUSDT 2425 USD x3 @ 2282.60 (ters sinyal, RSI 45)
02.11 16:02 N  NEWS (13 new) score -0.10 conf 0.35: Haberler karışık: İran'a yönelik Trump tehdidi jeopolitik risk yoluyla altını destekliyor, ancak petrol fiyatlarının %3'ten fazla düşmesi ve diplomasiye zaman verilmesi güvenli liman talebini ve enflasyon beklentilerini zayıflatıyor. Fed faiz artırımı beklentileri ile güçlenen dolar altın üzerinde baskı yaratıyor. Bu nedenle net etki hafif negatif, güven düşük.
02.11 16:02 N  GPT  score +0.10 conf 0.30: Trump’ın İran’a yönelik tehdidinin Körfez’de savaş kaygılarını canlandırması altına sınırlı güvenli liman desteği sağlayabilir. Ancak İran diplomasisi umuduyla petrolün sert düşmesi ve doların karışık seyri, kısa vadeli yönü belirsizleştiriyor.
02.11 16:44 A  CLOSE BTCUSDT stop: -25.72 USD
02.11 16:44 A  CLOSE ETHUSDT stop: -12.86 USD
02.11 16:44 A  CLOSE BNBUSDT stop: -25.72 USD
02.11 16:44 N  NEWS (19 new) score +0.10 conf 0.35: 
02.11 16:44 N  GPT  score +0.12 conf 0.34: İran’la yeniden çatışma ve gerilimin bölgeye yayılma ihtimali güvenli liman talebini sınırlı ölçüde destekleyebilir. Ancak diplomasi umutlarıyla petrolün gerilemesi ve dolar görünümündeki karışık sinyaller, kısa vadeli yönü belirsiz kılıyor.
02.11 16:44 B6  seans öncesi görüş: AI harcama endişeleriyle teknoloji ağırlıklı riskten kaçış var; son saatte hafif tepki alımı görülse de piyasa kırılgan, göreceli güç TSLA'da.
02.11 16:56 N  NEWS (23 new) score +0.05 conf 0.30: İran savaşının sürmesi ve Trump'ın "daha fazla askeri eylem mümkün" açıklaması güvenli liman talebini destekleyerek altı hafifçe yukarı çekebilir. Buna karşılık, güçlü dolar görüşü (HSBC), FOMC'nin faiz sabitlemesi ve petrol fiyatlarındaki düşüş (enflasyon beklentilerini zayıflatarak) altı baskılayabilir; ayrıca altın Ekim'de ciddi düşüş yaşadığı için haberlerin büyük kısmı zaten fiyatlanmış durumda. Sonuç olarak yönsüz, zayıf pozitif bir eğilim.
02.11 16:56 N  GPT  score +0.18 conf 0.32: İran savaşında yeni askerî adım ihtimalinin açık kalması kısa vadede güvenli liman talebini destekleyebilir. Ancak diplomasi temaslarının sürmesi ve petrolün ilerleme umuduyla gerilemesi bu etkiyi sınırlıyor; dolar ve faiz yönünde belirgin yeni bir sinyal yok.
02.11 17:08 N  NEWS (10 new) score +0.15 conf 0.35: İran savaşının sürmesi ve Trump'ın daha fazla askeri eylem ihtimalini sürdürmesi jeopolitik güvenli liman talebini destekliyor. Ancak müzakerelerde kırılma olmaması, petrol fiyatlarının gerilemesi ve ABD dolarında zayıf momentum gibi karışık sinyaller ile FOMC'nin faiz sabit tutması sonrası dolar lehine görüşler nedeniyle etki sınırlı ve yön belirsiz.
02.11 17:08 N  GPT  score +0.15 conf 0.28: İran savaşında askeri seçeneğin hâlâ masada olması ve görüşmelerde ilerleme sağlanamaması kısa vadede güvenli liman talebini destekleyebilir. Ancak diplomasi çağrıları ve petrol fiyatlarındaki düşüş bu etkiyi sınırlıyor; dolar haberleri de yön konusunda çelişkili.
02.11 17:20 N  NEWS (12 new) score +0.12 conf 0.35: ABD-İran savaşının sürmesi ve müzakerelerin sonuçsuz bitmesi jeopolitik risk primini hafifçe destekliyor, bu da altın için sınırlı bir yükseliş yönlü etki yaratabilir. Ancak enerji kaynaklı enflasyon ve Fed'in bekle-gör duruşu ile güçlü dolar haberleri altını baskılayabileceğinden etki zayıf ve karışık kalıyor.
02.11 17:20 N  GPT  score +0.28 conf 0.43: İran savaşının sürmesi ve Körfez’de savaş sigortasının daralması kısa vadeli güvenli liman talebini destekleyebilir. Ancak temasların sürmesi, diplomasi çağrıları ve petrol fiyatlarındaki gerileme bu etkiyi sınırlıyor; dolar ve faiz görünümünden net yeni bir sinyal yok.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
