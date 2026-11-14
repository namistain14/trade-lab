# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 14.11.2026 04:48 (İstanbul)

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
| Net kâr/zarar | +0.00 $ | -454.74 $ |
| İşlem sayısı | 0 | 113 |
| Kazanma oranı | %0.0 | %41.6 |
| Ödenen komisyon/spread | 0.00 $ | 1342.67 $ |

**Hesap değeri: 4,545.26 $** (başlangıç 5,000 $, -454.74 $ / %-9.09)

Son haber analizi (13.11 18:04): Claude puan **-0.60**, güven 0.70 — Sıcak ABD üretici fiyat enflasyonu, Fed'de faiz artırımı beklentilerinin güçlenmesi ve doların 19 aylık zirvesi altın için baskılayıcı. Altın 2026'nın en düşük seviyesi olan yaklaşık 3.850 dolara geriledi; İran savaşı ve jeopolitik haberler güvenli liman talebini destekliyor ama bu etki büyük ölçüde fiyatlanmış durumda.

GPT (gpt-6-luna): puan **-0.48**, güven 0.66 — Enflasyon ve Fed yetkililerinin açıklamaları faiz indirimi beklentilerini zayıflatıp daha şahin bir görünümü destekliyor; doların 19 ayın zirvesine yakın seyri altın üzerinde baskı yaratıyor. İran ve Ukrayna kaynaklı riskler güvenli liman talebi sağlayabilir, ancak kısa vadede bu baskıyı dengeleyece

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 13.11 19:25 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 18:39 | PAXGUSDT | short | +69.05 $ | take profit |
| 13.11 17:32 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 16:56 | PAXGUSDT | short | -55.98 $ | stop |
| 13.11 16:31 | PAXGUSDT | short | -55.98 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -123.04 $ |
| İşlem sayısı | 0 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 0.00 $ | 70.51 $ |

**Hesap değeri: 4,876.96 $** (başlangıç 5,000 $, -123.04 $ / %-2.46)

Son haber analizi (12.11 07:59): Claude puan **-0.15**, güven 0.40 — Başlıklar karışık: ABD-İran barış görüşmesi umutları, Brent'in 92 doların altına inmesi ve Suudi üretim artışı fiyatı aşağı çekiyor, ancak Hormuz'da mayına çarpan tanker, İran'ın misilleme tehditleri ve barış görüşmelerinin tıkanması ciddi bir yukarı risk oluşturuyor. Bu çelişkiler ve bazı haberlerin eski veya zaten fiyatlanmış olması nedeniyle yön sinyali zayıf ve güven düşük.

GPT (gpt-6-luna): puan **-0.35**, güven 0.56 — Barış görüşmesi umutları, Suudi üretimindeki artış ve OPEC+ ihracatının savaş öncesi seviyelere yaklaşması yakın vadede arz endişelerini azaltıp Brent üzerinde baskı kuruyor. Hürmüz’deki mayın/tanker haberleri ve İran’ın misilleme tehdidi düşüşü sınırlıyor; haber akışının bir kısmı doğrulanmamış vey

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

**Hesap değeri: 114,154.56 $** (başlangıç 100,000 $, +14154.56 $ / %+14.15)

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
13.11 23:21 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1Yn3jPNMrGdbTYMuZDE'}
13.11 23:24 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1Z1KTZBTjuJVG8m6bf8'}
13.11 23:27 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1ZEa8xDuho1oJyrUXKM'}
13.11 23:30 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1ZTun1oAE74MvWnHSYg'}
13.11 23:33 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1ZhAn2b1QYmv4z1pD8f'}
13.11 23:33 B6  CLOSE long AAPL stop: -1154.98 USD
13.11 23:36 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1ZvNhFECE6xo2YppjVu'}
13.11 23:39 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1a9i1SzsB9t2xYDj8yS'}
13.11 23:42 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1aNy3SoLQcrBdFEtAWo'}
13.11 23:45 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1acKmjYGM7atZnBGjCc'}
13.11 23:45 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1aer6wHf2KvJcUnfxLm'}
13.11 23:48 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1at1sfKY1KUZnadJ9ub'}
13.11 23:51 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1b7Ja7NyzzUKqwE8WfN'}
13.11 23:54 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1bLZMjKwiq8ghKVhwr1'}
13.11 23:57 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch1bZoyuaX1X2U57nhjZD'}
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
