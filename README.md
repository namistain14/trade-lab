# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 02.11.2026 12:50 (İstanbul)

## Bot A — Kripto TERS (alım sinyalinde satış, x3)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -162.62 $ | -917.75 $ |
| İşlem sayısı | 12 | 73 |
| Kazanma oranı | %25.0 | %20.5 |
| Ödenen komisyon/spread | 50.20 $ | 325.80 $ |

**Hesap değeri: 4,082.25 $** (başlangıç 5,000 $, -917.75 $ / %-18.36)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 11:41 | DOGEUSDT | short | -13.06 $ | stop |
| 02.11 11:42 | XRPUSDT | short | -26.48 $ | stop |
| 02.11 11:41 | SOLUSDT | short | -26.45 $ | stop |
| 02.11 11:07 | ETHUSDT | short | -13.27 $ | stop |
| 02.11 10:13 | ETHUSDT | short | +1.97 $ | time limit |

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

**Hesap değeri: 100,114.21 $** (başlangıç 100,000 $, +114.21 $ / %+0.11)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
02.11 11:43 A  CLOSE DOGEUSDT stop: -13.06 USD
02.11 11:43 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdohNnPhDtWs2SADU9S7'}
02.11 11:46 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdovgMRdzUBQDeKNNDBT'}
02.11 11:49 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cgdp9vsQjyLwCBiY3AkGU'}
02.11 11:52 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdpPRzUbVxDLpSEhLm7p'}
02.11 11:55 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cgdpca4XRNqmbGrGgWtQo'}
02.11 12:26 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cgdrx6VNLNMcSa4TnhCYC'}
02.11 12:29 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdsBM1N164kavW7VJZZh'}
02.11 12:32 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdsQcCXUqe9gvcZqDvAa'}
02.11 12:35 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdsdrQAQDb9BYpBgv97b'}
02.11 12:38 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cgdss8hYkUg5RJ7LgXeU7'}
02.11 12:41 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cgdt6P8aA4EFMwQNPjsMh'}
02.11 12:44 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdtKfJY71VVoK27rQC5m'}
02.11 12:47 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdtYvPk1qqCYnePPLCxh'}
02.11 12:50 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdtnEqNEJBmdi9ehQGtS'}
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
