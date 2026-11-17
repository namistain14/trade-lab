# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 17.11.2026 20:10 (İstanbul)

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

Son haber analizi (17.11 19:38): Claude puan **-0.15**, güven 0.40 — Altın yıllık en düşük seviyesinden toparlanmakta zorlanıyor; dolar ve tahvil getirileri yükseliyor, piyasada Fed faiz artırımı beklentisi fiyatlanıyor, bu da altın için baskı yaratıyor. Hürmüz'deki tanker saldırıları ve İran savaşı jeopolitik risk üretse de etkisi enflasyon/faiz kanalıyla sınırlı kalıyor; Fed Gov. Cook'un Beyaz Saray duruşmasına katılmayı reddetmesi Fed bağımsızlığı endişesi yaratıp kısmen altını destekleyebilir ancak bu haber daha az belirleyici.

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

**Hesap değeri: 114,145.15 $** (başlangıç 100,000 $, +14145.15 $ / %+14.15)

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
17.11 19:44 B6  karar turu: Claude «-» / GPT «-»
17.11 19:50 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch8qywsjzb3fgHuhuEvm6'}
17.11 19:53 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch8rD3xEsM5M5r1XVXeHV'}
17.11 19:56 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch8rSCiShnf9cv8qentMY'}
17.11 19:56 B6  Claude cevap vermedi: no Claude model available: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Yo
17.11 19:56 B6  GPT cevap vermedi: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the A
17.11 19:56 B6  karar turu: Claude «-» / GPT «-»
17.11 19:59 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch8rfbZyxxVMraTE1kGvi'}
17.11 20:02 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch8rtqCeLjSnTunZTsQgH'}
17.11 20:05 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch8s84RzEyRVgzMau2Pw3'}
17.11 20:06 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch8sD26EQhn6wZi5w4cin'}
17.11 20:06 B6  Claude cevap vermedi: no Claude model available: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Yo
17.11 20:06 B6  GPT cevap vermedi: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the A
17.11 20:06 B6  karar turu: Claude «-» / GPT «-»
17.11 20:10 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch8sSqXdQJZWdgK6J82Cj'}
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
