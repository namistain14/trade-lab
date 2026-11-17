# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 17.11.2026 20:42 (İstanbul)

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

**Hesap değeri: 4,536.70 $** (başlangıç 5,000 $, -463.30 $ / %-9.27)

Açık pozisyonlar: PAXGUSDT long @ 3857.75 (TP 3869.32 / SL 3850.04)

Son haber analizi (17.11 20:34): Claude puan **+0.20**, güven 0.35 — Kırım Köprüsü'nün kısmen çökmesi ve Kiev'deki Rus saldırıları jeopolitik gerilimi artırarak altına sınırlı bir güvenli liman talebi getirebilir. Ancak bu gelişmelerin altın fiyatına etkisi genellikle kısa vadede küçük kalır, makro veri ya da Fed beklentileri ise bu haberlerden daha belirleyici olur; bu nedenle güven düşük tutuldu.

GPT (gpt-6-luna): puan **+0.35**, güven 0.55 — Kırım Köprüsü’ne yönelik saldırı ve Rusya-Ukrayna çatışmasındaki tırmanış, kısa vadede güvenli liman talebini artırarak altını destekleyebilir. İran’a ilişkin ABD açıklaması da jeopolitik riski yükseltiyor; ancak dolar ve faizlere dair yeni bir sinyal olmaması etkiyi sınırlıyor.

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

**Hesap değeri: 113,593.64 $** (başlangıç 100,000 $, +13593.64 $ / %+13.59)

Açık pozisyonlar: NVDA long @ 154.28 (TP 156.76 / SL 152.90); QQQ long @ 655.92 (TP 665.89 / SL 649.49); TSLA long @ 380.84 (TP 386.76 / SL 377.23)

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
17.11 20:15 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch8stt9MtqKaknrPX2to1'}
17.11 20:19 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Ch8t8QaYttP3s3uBwDo1p'}
17.11 20:19 B6  Claude cevap vermedi: no Claude model available: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Yo
17.11 20:19 B6  GPT cevap vermedi: OpenAI account problem: 429 credit_balance_exhausted: You have no credits remaining. Add credits to continue using the A
17.11 20:19 B6  karar turu: Claude «-» / GPT «-»
17.11 20:22 N  NEWS (17 new) score +0.15 conf 0.30: Yeni haberlerin çoğu jeopolitik gerilimi artırıyor (Kırım Köprüsü'nde kısmi çöküş, Kiev'deki köprüye Rus saldırısı, İran planına ilişkin ABD açıklaması), bu da güvenli liman talebini hafifçe destekler. Ancak Fed, enflasyon veya dolar tarafında doğrudan bir sürpriz yok ve Trump'ın Asya'daki Putin/Şi zirveleri diplomatik bir gevşemeye işaret edebilir; bu nedenle etki sınırlı ve güven düşük.
17.11 20:22 N  GPT  score +0.30 conf 0.46: Kırım Köprüsü’ne yönelik saldırı ve ABD’nin İran kaynaklı olası tehditleri ciddiye aldığını söylemesi kısa vadede güvenli liman talebini artırarak altını destekleyebilir. Ancak haberlerin etkisi belirsiz ve faiz ya da dolar yönüne dair yeni bir sinyal yok; bu nedenle yükseliş etkisinin sınırlı kalma
17.11 20:30 B6  karar turu: Claude «Piyasa günü ekside geçiriyor ancak son bir saatte teknoloji öncülüğünde tepki yükselişi var; seçici long pozisyonlar mantıklı.» / GPT «Günlük kayıplara rağmen saatlik toparlanma alım yönünde ılımlı avantaj sağlıyor; ancak 1:4 kaldıraçta aynı yöne korelasyonlu pozisyonların toplam riski sınırlanmalı.»
17.11 20:30 B6  ALIŞ QQQ 173 adet ≈ 113,497 $ (1:4) @ 656.05 (TP 665.89, SL 649.49; ikisi de hemfikir, güven 0.55)
17.11 20:30 B6  ALIŞ NVDA 739 adet ≈ 114,131 $ (1:4) @ 154.44 (TP 156.76, SL 152.9; ikisi de hemfikir, güven 0.55)
17.11 20:30 B6  ALIŞ TSLA 299 adet ≈ 113,931 $ (1:4) @ 381.04 (TP 386.76, SL 377.23; ikisi de hemfikir, güven 0.60)
17.11 20:34 N  NEWS (1 new) score +0.20 conf 0.35: Kırım Köprüsü'nün kısmen çökmesi ve Kiev'deki Rus saldırıları jeopolitik gerilimi artırarak altına sınırlı bir güvenli liman talebi getirebilir. Ancak bu gelişmelerin altın fiyatına etkisi genellikle kısa vadede küçük kalır, makro veri ya da Fed beklentileri ise bu haberlerden daha belirleyici olur; bu nedenle güven düşük tutuldu.
17.11 20:34 N  GPT  score +0.35 conf 0.55: Kırım Köprüsü’ne yönelik saldırı ve Rusya-Ukrayna çatışmasındaki tırmanış, kısa vadede güvenli liman talebini artırarak altını destekleyebilir. İran’a ilişkin ABD açıklaması da jeopolitik riski yükseltiyor; ancak dolar ve faizlere dair yeni bir sinyal olmaması etkiyi sınırlıyor.
17.11 20:34 B5  LONG gold 25000 USD x10 @ 3857.75 (TP 3869.32, SL 3850.04; news +0.28)
17.11 20:42 B6  karar turu: Claude «Piyasa yaklaşık %1 ekside, öğleden sonraki tepki yükselişi zayıflıyor ve hafif negatif eğilim sürüyor.» / GPT «Endekslerde gün içi tepki yükselişi zayıflarken, yeni şirket haberleriyle desteklenmeyen hareketleri kovalamak yerine göreli zayıflıkta seçici kısa pozisyonlar öne çıkıyor.»
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
