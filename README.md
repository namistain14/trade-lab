# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 02.11.2026 15:35 (İstanbul)

## Bot A — Kripto TERS (alım sinyalinde satış, x3)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -203.32 $ | -958.46 $ |
| İşlem sayısı | 15 | 76 |
| Kazanma oranı | %20.0 | %19.7 |
| Ödenen komisyon/spread | 62.46 $ | 338.06 $ |

**Hesap değeri: 4,041.54 $** (başlangıç 5,000 $, -958.46 $ / %-19.17)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 15:31 | BNBUSDT | short | -1.73 $ | time limit |
| 02.11 15:10 | XRPUSDT | short | -12.99 $ | stop |
| 02.11 15:12 | SOLUSDT | short | -25.98 $ | stop |
| 02.11 11:41 | DOGEUSDT | short | -13.06 $ | stop |
| 02.11 11:42 | XRPUSDT | short | -26.48 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -55.97 $ | +22.70 $ |
| İşlem sayısı | 1 | 13 |
| Kazanma oranı | %0.0 | %46.2 |
| Ödenen komisyon/spread | 11.92 $ | 154.68 $ |

**Hesap değeri: 5,022.70 $** (başlangıç 5,000 $, +22.70 $ / %+0.45)

Son haber analizi (02.11 15:26): Claude puan **-0.15**, güven 0.35 — Haberlerde faiz artırımı beklentileri ve güçlenen dolar altın için baskı oluşturuyor; ancak petrol fiyatlarının düşmesi ve İran-ABD savaşında barış umudu enflasyon kaygısını azaltarak bu baskıyı kısmen dengeliyor. Sinyaller karışık ve ağırlıklı olarak tekrar eden ya da fiyatlanmış haberler olduğundan güven düşük.

GPT (gpt-6-luna): puan **-0.12**, güven 0.30 — ABD-İran savaşına dair umutların petrol fiyatlarını düşürmesi ve dolar/faiz artışı beklentileri altın üzerinde hafif baskı oluşturabilir. Yemen ve Lübnan’daki gerilim haberleri güvenli liman talebini desteklese de kısa vadeli etki karışık ve sınırlı görünüyor.

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

**Hesap değeri: 100,841.78 $** (başlangıç 100,000 $, +841.78 $ / %+0.84)

Açık pozisyonlar: AAPL long @ 349.31 (TP 354.74 / SL 346.00); NVDA short @ 213.74 (TP 210.40 / SL 215.74); TSLA long @ 406.46 (TP 412.39 / SL 402.24)

## Son olaylar

```
02.11 14:11 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011CgdzzpetGv6qGehLug5TH'}
02.11 14:26 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cge29d5zJ3pUGm8dmCNKe'}
02.11 14:29 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cge2NviVr8ZkuUdgqzv24'}
02.11 14:32 B  NEWS failed: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits.'}, 'request_id': 'req_011Cge2cCoF6Gn3VtoMt7oSK'}
02.11 14:36 N  NEWS (45 new) score -0.15 conf 0.40: Altın için karışık tablo var: Fed faiz beklentileri altındaki toparlanmayı sınırlıyor ve ekim ayı 2008'den bu yana en kötü performansını gösterdi, bu da kısa vadede baskı yaratıyor. Trump'ın İran diplomasisine daha fazla zaman verdiğini söylemesiyle petrol %3'ten fazla düştü; bu jeopolitik risk primini azaltarak güvenli liman talebini zayıflatıyor, ancak nükleer saldırı ve savaş tehdidi haberleri bu etkiyi kısmen dengeliyor.
02.11 14:36 N  GPT  score -0.15 conf 0.36: Fed faiz beklentilerinin altını sınırlaması ve doların yatay-güçlü seyri kısa vadede hafif baskı yaratıyor; İran kaynaklı risk başlıkları güvenli liman talebini desteklese de petrolün diplomasi sinyalleriyle gerilemesi bu etkiyi azaltıyor. Haberler karışık ve çoğu yeni bir tırmanış teyit etmiyor.
02.11 14:48 N  NEWS (9 new) score +0.15 conf 0.35: Yeni başlıklar karışık: zayıflayan dolar altını destekliyor ve altın/gümüş toparlanıyor, petrol fiyatlarının düşmesi enflasyon beklentilerini yumuşatarak faiz indirimi ihtimallerini artırabilir. Öte yandan Fed faiz beklentileri toparlanmayı sınırlıyor, ISM ve ABD seçim gündemi dolar yönünde belirsizlik yaratıyor ve İran diplomasisi jeopolitik risk primini azaltıyor, bu da güvenli liman talebini zayıflatıyor. Genel etki hafif pozitif, ancak sinyaller karışık olduğu için güven düşük.
02.11 14:48 N  GPT  score +0.05 conf 0.33: Zayıflayan doların altını desteklemesiyle toparlanma görülüyor; ancak Fed faiz beklentileri yükselişi sınırlıyor. İran diplomasisi sinyalleri ve petrol fiyatlarındaki düşüş, kısa vadeli güvenli liman talebini azaltabilir.
02.11 15:00 N  NEWS (9 new) score +0.10 conf 0.35: Karışık sinyaller var: petrol fiyatlarının düşmesi enflasyon endişelerini azaltıp faiz artırımı beklentilerini zayıflatabilir (altın için hafif olumlu), zayıf dolar da destekleyici; öte yandan Trump'ın İran'da diplomasiye zaman verdiği yönündeki haberler jeopolitik risk primini düşürüp güvenli liman talebini sınırlıyor ve Fed faiz beklentileri altın toparlanmasını sınırlıyor. Net etki sınırlı ve yön belirsiz.
02.11 15:00 N  GPT  score +0.08 conf 0.29: Yemen’deki sivil kayıplara yol açan füze saldırısı kısa vadeli güvenli liman talebini destekleyebilir. Ancak petrolün İran diplomasisi beklentisiyle gerilemesi ve Fed faiz beklentilerinin altını sınırlaması tabloyu dengeliyor.
02.11 15:26 A  CLOSE SOLUSDT stop: -25.98 USD
02.11 15:26 A  CLOSE XRPUSDT stop: -12.99 USD
02.11 15:26 N  NEWS (21 new) score -0.15 conf 0.35: Haberlerde faiz artırımı beklentileri ve güçlenen dolar altın için baskı oluşturuyor; ancak petrol fiyatlarının düşmesi ve İran-ABD savaşında barış umudu enflasyon kaygısını azaltarak bu baskıyı kısmen dengeliyor. Sinyaller karışık ve ağırlıklı olarak tekrar eden ya da fiyatlanmış haberler olduğundan güven düşük.
02.11 15:26 N  GPT  score -0.12 conf 0.30: ABD-İran savaşına dair umutların petrol fiyatlarını düşürmesi ve dolar/faiz artışı beklentileri altın üzerinde hafif baskı oluşturabilir. Yemen ve Lübnan’daki gerilim haberleri güvenli liman talebini desteklese de kısa vadeli etki karışık ve sınırlı görünüyor.
02.11 15:32 A  CLOSE BNBUSDT time limit: -1.73 USD
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
