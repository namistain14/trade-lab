# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 02.11.2026 07:44 (İstanbul)

## Bot A — Kripto TERS (alım sinyalinde satış, x3)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -105.36 $ | -860.50 $ |
| İşlem sayısı | 5 | 66 |
| Kazanma oranı | %0.0 | %18.2 |
| Ödenen komisyon/spread | 22.82 $ | 298.41 $ |

**Hesap değeri: 4,139.50 $** (başlangıç 5,000 $, -860.50 $ / %-17.21)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 04:08 | XRPUSDT | short | -26.51 $ | stop |
| 02.11 02:30 | BNBUSDT | short | -22.05 $ | time limit |
| 02.11 02:14 | XRPUSDT | short | -13.35 $ | stop |
| 02.11 02:14 | SOLUSDT | short | -26.91 $ | stop |
| 02.11 01:04 | ETHUSDT | short | -16.55 $ | time limit |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +78.66 $ |
| İşlem sayısı | 0 | 12 |
| Kazanma oranı | %0.0 | %50.0 |
| Ödenen komisyon/spread | 0.00 $ | 142.76 $ |

**Hesap değeri: 5,062.92 $** (başlangıç 5,000 $, +62.92 $ / %+1.26)

Açık pozisyonlar: PAXGUSDT short @ 3910.21 (TP 3898.48 / SL 3918.03)

Son haber analizi (02.11 07:42): Claude puan **-0.60**, güven 0.60 — Faiz artırımı beklentileri ve Warsh'un ek Fed sıkılaştırma sinyalleri, güçlü ABD enflasyonu ve marj çağrıları altın fiyatını bir yılın en düşük seviyesine çekti; bu baskı kısa vadede altın için negatif. Buna karşın İran savaşı ve Ukrayna'daki çatışmalar güvenli liman talebini destekliyor ve altın aşırı satılmış görünüyor, bu nedenle toparlanma ihtimali ve sinyallerin çelişkili olması güveni sınırlıyor.

GPT (gpt-6-luna): puan **-0.48**, güven 0.65 — Fed’in enflasyon nedeniyle yeni faiz artırımlarına işaret etmesi ve faiz artışı beklentilerinin güçlenmesi, kısa vadede altın üzerinde baskı yaratıyor; marjin çağrılarının düşüşü büyütmesi de aşağı yönlü riski artırıyor. İran gerilimi ve yuanın güçlenmesi sınırlı destek sağlasa da haberler çelişkili

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 31.10 00:48 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 23:07 | PAXGUSDT | short | -55.97 $ | stop |
| 30.10 20:35 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 18:48 | PAXGUSDT | short | +69.06 $ | take profit |
| 30.10 17:39 | PAXGUSDT | short | -55.97 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 100,040.89 $** (başlangıç 100,000 $, +40.89 $ / %+0.04)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
02.11 02:11 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 02:14 A  CLOSE SOLUSDT stop: -26.91 USD
02.11 02:14 A  CLOSE XRPUSDT stop: -13.35 USD
02.11 02:14 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 02:17 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
02.11 02:32 A  CLOSE BNBUSDT time limit: -22.05 USD
02.11 03:30 A  SHORT XRPUSDT 4999 USD x3 @ 1.25 (ters sinyal, RSI 43)
02.11 04:56 A  CLOSE XRPUSDT stop: -26.51 USD
02.11 07:01 N  NEWS (45 new) score -0.15 conf 0.35: Haberler çelişkili: Fed faiz artırımı beklentilerinin yükselmesi ve doların güçlü kalması altını baskılarken, İran savaşı ve güvenli liman talebi destek sağlıyor. Altın bir yıllık dibe yakın seyrediyor ve kısa vadede 3.900 doların üzerinde toparlanma var, bu yüzden etki hafif negatif kabul edildi.
02.11 07:01 N  GPT  score -0.10 conf 0.38: Altın, aşırı satım sonrası toparlanıyor ve İran çevresindeki gerilim güvenli liman talebini destekleyebilir; ancak doların güçlü/istikrarlı seyri ve Fed faiz artırımı beklentilerinin yükselmesi kısa vadede baskı yaratıyor. Haber akışı çelişkili ve büyük ölçüde tekrarlı olduğundan net yön sinyali zay
02.11 07:13 N  NEWS (9 new) score -0.30 conf 0.50: Altın yıllık en düşük seviyesine yakın işlem görüyor ve Fed faiz artırımı beklentilerinin güçlenmesi, reel faizler üzerinden baskı yaratıyor. İran savaşına ilişkin jeopolitik risk güvenli liman talebini destekliyor olsa da, bu talep fiyatlara yeterince yansımıyor; petrol fiyatlarındaki gerileme ve müzakere sinyalleri de sınırlı bir toparlanma ihtimali taşıyor.
02.11 07:13 N  GPT  score -0.35 conf 0.48: Altının sert düşüşü ve Fed faiz artırımı beklentilerinin güçlenmesi kısa vadede aşağı yönlü baskıyı destekliyor; doların istikrarlı seyri de bunu pekiştiriyor. İran konusunda hem müzakere hem çatışma haberleri bulunduğundan güvenli liman etkisi belirsiz ve hareketin bir kısmı önceden fiyatlanmış ola
02.11 07:42 N  NEWS (22 new) score -0.60 conf 0.60: Faiz artırımı beklentileri ve Warsh'un ek Fed sıkılaştırma sinyalleri, güçlü ABD enflasyonu ve marj çağrıları altın fiyatını bir yılın en düşük seviyesine çekti; bu baskı kısa vadede altın için negatif. Buna karşın İran savaşı ve Ukrayna'daki çatışmalar güvenli liman talebini destekliyor ve altın aşırı satılmış görünüyor, bu nedenle toparlanma ihtimali ve sinyallerin çelişkili olması güveni sınırlıyor.
02.11 07:42 N  GPT  score -0.48 conf 0.65: Fed’in enflasyon nedeniyle yeni faiz artırımlarına işaret etmesi ve faiz artışı beklentilerinin güçlenmesi, kısa vadede altın üzerinde baskı yaratıyor; marjin çağrılarının düşüşü büyütmesi de aşağı yönlü riski artırıyor. İran gerilimi ve yuanın güçlenmesi sınırlı destek sağlasa da haberler çelişkili
02.11 07:42 B5  SHORT gold 25000 USD x10 @ 3910.21 (TP 3898.48, SL 3918.03; news -0.54)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
