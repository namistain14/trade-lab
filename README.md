# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 02.11.2026 10:18 (İstanbul)

## Bot A — Kripto TERS (alım sinyalinde satış, x3)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -83.34 $ | -838.48 $ |
| İşlem sayısı | 8 | 69 |
| Kazanma oranı | %37.5 | %21.7 |
| Ödenen komisyon/spread | 35.22 $ | 310.82 $ |

**Hesap değeri: 4,164.93 $** (başlangıç 5,000 $, -835.07 $ / %-16.70)

Açık pozisyonlar: SOLUSDT short @ 94.35 (TP 93.79 / SL 94.73)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 10:13 | ETHUSDT | short | +1.97 $ | time limit |
| 02.11 10:13 | BTCUSDT | short | +3.08 $ | time limit |
| 02.11 09:52 | BNBUSDT | short | +16.97 $ | time limit |
| 02.11 04:08 | XRPUSDT | short | -26.51 $ | stop |
| 02.11 02:30 | BNBUSDT | short | -22.05 $ | time limit |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -55.97 $ | +22.70 $ |
| İşlem sayısı | 1 | 13 |
| Kazanma oranı | %0.0 | %46.2 |
| Ödenen komisyon/spread | 11.92 $ | 154.68 $ |

**Hesap değeri: 5,022.70 $** (başlangıç 5,000 $, +22.70 $ / %+0.45)

Son haber analizi (02.11 09:19): Claude puan **-0.15**, güven 0.35 — Haberler karışık: İran savaşı ve jeopolitik risk altın için güvenli liman desteği sağlıyor, ancak faiz artırımı beklentileri, Fed sinyalleri ve güçlenen dolar (rupi ve diğer para birimlerinin değer kaybı) altın üzerinde baskı yaratıyor. Yerel altın fiyatı haberlerinin çoğu zaten fiyatlanmış ve gürültü niteliğinde; bu nedenle hafif negatif, düşük güvenli bir görünüm.

GPT (gpt-6-luna): puan **+0.12**, güven 0.35 — Reuters’ın daha yumuşak petrol fiyatları eşliğinde altının yükseldiğini bildirmesi kısa vadede hafif destekleyici; ancak Fed’in faiz görünümüne ilişkin riskler ve doların güçlenmesi kazançları sınırlayabilir. Yeni başlıkların çoğu yerel altın fiyatlarıyla ilgili ve küresel spot fiyat için güçlü bir 

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

**Hesap değeri: 99,889.09 $** (başlangıç 100,000 $, -110.91 $ / %-0.11)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
02.11 09:48 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdevsqSjg88BZ7kScLc8'}
02.11 09:51 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdfA8xtEvjwQroyvQNuQ'}
02.11 09:54 A  CLOSE BNBUSDT time limit: +16.97 USD
02.11 09:54 A  SHORT SOLUSDT 4988 USD x3 @ 94.35 (ters sinyal, RSI 37)
02.11 09:54 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdfPQgoCnGbSVby1agbD'}
02.11 09:57 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdfccreM168QzocvWpQk'}
02.11 10:00 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cgdfqrvqoxgzp4xVwNAnS'}
02.11 10:03 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cgdg5AYrkRfgoPTH9zdWz'}
02.11 10:06 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdgJUirmccG72pjQ3BXh'}
02.11 10:09 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdgXiPVoGNq43JN3TBNJ'}
02.11 10:12 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdgkyVDTF8bMo7r1GHhe'}
02.11 10:15 A  CLOSE BTCUSDT time limit: +3.08 USD
02.11 10:15 A  CLOSE ETHUSDT time limit: +1.97 USD
02.11 10:15 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdgzNHXmSQNqGhrXKEX3'}
02.11 10:18 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdhDaS8YCK8v5yScMms2'}
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
