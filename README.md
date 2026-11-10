# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 10.11.2026 20:45 (İstanbul)

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
| Net kâr/zarar | +289.59 $ | -389.84 $ |
| İşlem sayısı | 6 | 74 |
| Kazanma oranı | %83.3 | %40.5 |
| Ödenen komisyon/spread | 71.00 $ | 877.99 $ |

**Hesap değeri: 4,610.16 $** (başlangıç 5,000 $, -389.84 $ / %-7.80)

Son haber analizi (10.11 14:46): Claude puan **-0.35**, güven 0.50 — Fed'in Waller'ın Aralık'ta faiz artırımını destekleyen sert açıklamaları ve dolar desteği altın için baskılayıcı; Trump'ın İran savaşının "yakında bitebileceği" yönündeki sözleri ve petrol fiyatlarındaki gerileme jeopolitik korku primini azaltarak ek bir olumsuz etki yaratıyor. Ancak ABD enflasyon verisinin (CPI) sonucu belirsiz olduğu için güven orta düzeyde tutuldu.

GPT (gpt-6-luna): puan **-0.40**, güven 0.68 — Waller’ın daha büyük faiz artışının değerlendirilmesi gerektiği yönündeki şahin mesajı ve yaklaşan ABD TÜFE verisi altını baskılıyor; İran savaşının yakında sona erebileceği açıklaması da güvenli liman talebini azaltabilir. Ancak İran’ın koşulları ve TÜFE belirsizliği yönü sınırlıyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 10.11 16:31 | PAXGUSDT | short | +69.09 $ | take profit |
| 10.11 13:56 | PAXGUSDT | short | +69.09 $ | take profit |
| 10.11 12:36 | PAXGUSDT | short | +69.10 $ | take profit |
| 10.11 12:01 | PAXGUSDT | short | +69.10 $ | take profit |
| 10.11 06:45 | PAXGUSDT | short | +69.10 $ | take profit |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -67.46 $ | -123.04 $ |
| İşlem sayısı | 1 | 4 |
| Kazanma oranı | %0.0 | %25.0 |
| Ödenen komisyon/spread | 18.21 $ | 70.51 $ |

**Hesap değeri: 4,876.96 $** (başlangıç 5,000 $, -123.04 $ / %-2.46)

Son haber analizi (10.11 07:59): Claude puan **-0.25**, güven 0.50 — Trump'ın İran savaşının askeri olarak bittiğini söylemesi ve Brent'in %6,7 düşüp 91,70 dolara gerilemesi, barış beklentileri nedeniyle kısa vadede baskı yaratıyor. Ancak Hormuz'daki gemi saldırıları, Husilerin Suudi boru hattına yönelik saldırıları ve Çin'in ham petrol ithalatının artması arz riskini canlı tutuyor; bu çelişkili haberler güveni sınırlıyor.

GPT (gpt-6-luna): puan **-0.55**, güven 0.68 — İran savaşının askerî olarak sona erdiği açıklaması, saldırı risklerinin azaldığına dair haberler ve Brent’in %6,73 düşmesi kısa vadede güçlü aşağı yönlü baskıya işaret ediyor. Suudi petrol boru hattına yönelik saldırı ve Hürmüz’deki gemi iddiaları arz riskini canlı tutsa da haberler çelişkili ve dü

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
| Net kâr/zarar | +0.00 $ | +9437.07 $ |
| İşlem sayısı | 0 | 34 |
| Kazanma oranı | %0.0 | %50.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 111,676.47 $** (başlangıç 100,000 $, +11676.47 $ / %+11.68)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 09.11 23:48 | TSLA | long | +1105.07 $ | seans sonu |
| 09.11 23:48 | SPY | long | +281.01 $ | seans sonu |
| 09.11 23:48 | QQQ | long | +996.60 $ | seans sonu |
| 09.11 21:28 | NVDA | long | -1113.38 $ | stop |
| 09.11 19:06 | NVDA | long | -1115.17 $ | stop |

## Son olaylar

```
10.11 20:17 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgudMNAX4FgZeJtmWvWmN'}
10.11 20:20 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgudahAPEzn8uuLSS5HrQ'}
10.11 20:23 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cgudow5Q7xzTV2woS1UaQ'}
10.11 20:23 B6  Claude cevap vermedi: no Claude model available: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Yo
10.11 20:23 B6  karar turu: Claude «-» / GPT «Verilen akışta sıcak enflasyon, şahin Fed mesajları ve jeopolitik riskler satış yönünü desteklerken, dört kat kaldıraç nedeniyle düşüşü kovalamadan göreli güç ve zayıflık üzerinden seçici işlem tercih ediyorum.»
10.11 20:24 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgudsxyNMeKwpdsosPQPG'}
10.11 20:27 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cgue79G73XjpXgp8fY3NU'}
10.11 20:30 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgueLU1pvFdGZ7irefGTW'}
10.11 20:33 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgueZhSb8RtxgSx1avbVD'}
10.11 20:36 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CguenvuaSzc1yzRY2g8WF'}
10.11 20:36 B6  Claude cevap vermedi: no Claude model available: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Yo
10.11 20:36 B6  karar turu: Claude «-» / GPT «Verilen akışta enflasyon ve faiz artışı baskısı endekslerde kısa yönü destekliyor; dört kat kaldıraçla SPY ve QQQ işlemleri aynı riskin yoğunlaşması olarak değerlendirilmelidir.»
10.11 20:39 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cguf2EUcdb6wj6vCBxwze'}
10.11 20:42 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgufFUCidvTpYZKWJ3b53'}
10.11 20:45 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgufUhDfn8KZu4yVGEjTC'}
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
