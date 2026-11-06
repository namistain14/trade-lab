# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 06.11.2026 08:14 (İstanbul)

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
| Net kâr/zarar | -223.95 $ | -257.89 $ |
| İşlem sayısı | 4 | 56 |
| Kazanma oranı | %0.0 | %41.1 |
| Ödenen komisyon/spread | 47.34 $ | 664.80 $ |

**Hesap değeri: 4,742.11 $** (başlangıç 5,000 $, -257.89 $ / %-5.16)

Son haber analizi (06.11 08:12): Claude puan **-0.25**, güven 0.40 — Altın, petrol kaynaklı enflasyon kaygıları ve güçlenen dolar (DXY 101.80) nedeniyle baskı altında; haberlerde "gold eases" ve "gold prices plummet" temaları öne çıkıyor. İran savaşı jeopolitik talebi destekleyici olsa da, yüksek petrol fiyatlarının faiz beklentilerini sertleştirmesi bu etkiyi dengeliyor. Yaklaşan ABD tarım dışı istihdam (NFP) verisi yönü belirsiz bir risk yarattığı için güven düşük tutuldu.

GPT (gpt-6-luna): puan **-0.28**, güven 0.57 — DXY’nin 101,80’e yükselmesi ve yüksek petrol kaynaklı enflasyon/faiz endişeleri kısa vadede altını baskılıyor; yaklaşan ABD istihdam verisi de temkinli pozisyonlanmayı destekliyor. İran savaşı güvenli liman talebi sağlasa da haber akışı karışık ve etkisi net değil.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 08:11 | PAXGUSDT | short | -56.23 $ | stop (gap) |
| 06.11 04:01 | PAXGUSDT | long | -55.91 $ | stop |
| 06.11 03:47 | PAXGUSDT | long | -55.90 $ | stop |
| 06.11 02:52 | PAXGUSDT | long | -55.91 $ | stop |
| 05.11 19:13 | PAXGUSDT | short | -55.93 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +66.43 $ |
| İşlem sayısı | 0 | 1 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 17.17 $ |

**Hesap değeri: 5,047.64 $** (başlangıç 5,000 $, +47.64 $ / %+0.95)

Açık pozisyonlar: BZ=F long @ 99.69 (TP 99.99 / SL 99.50)

Son haber analizi (06.11 07:59): Claude puan **+0.35**, güven 0.50 — Hormuz'daki yeni tanker saldırıları ve Rusya'daki rafineri patlamaları/Ukrayna saldırıları arz riskini artırıp Brent'i 100 doların üzerine itti; ancak İran'ın Katar üzerinden nükleer öneri göndermesi, Orta Doğu barış beklentileri ve haftalık yaklaşık %12-13'lük düşüş yukarı yönlü hareketi sınırlayabilir, bu yüzden güven orta düzeyde.

GPT (gpt-6-luna): puan **+0.55**, güven 0.66 — Hürmüz Boğazı’nda yeni tanker saldırısı haberleri ve Rusya’daki rafinerilere yönelik saldırı bildirimleri yakın vadeli arz riskini artırarak Brent’i destekliyor. İran’ın ABD’ye ilettiği bildirilen nükleer öneri ve daha geniş barış beklentileri bu etkiyi sınırlıyor; haberlerin bir kısmı doğrulanmamış

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 02.11 23:09 | BZ=F | short | +66.43 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:4

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +5879.74 $ |
| İşlem sayısı | 0 | 21 |
| Kazanma oranı | %0.0 | %52.4 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 108,278.00 $** (başlangıç 100,000 $, +8278.00 $ / %+8.28)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 05.11 23:46 | SPY | short | +582.01 $ | seans sonu |
| 05.11 23:46 | QQQ | short | +576.72 $ | seans sonu |
| 05.11 23:46 | NVDA | short | +1215.36 $ | seans sonu |
| 05.11 23:46 | AAPL | long | +93.44 $ | seans sonu |
| 05.11 20:37 | QQQ | short | -1070.92 $ | stop |

## Son olaylar

```
06.11 07:35 N  GPT  score +0.05 conf 0.24: Hegseth’in İran savaşını savunması jeopolitik risk algısını bir miktar destekleyebilir, ancak yeni bir askerî tırmanış haberi yok. Petrol kaynaklı enflasyon endişeleri ve yaklaşan istihdam verisi altın için aşağı yönlü risk oluştururken, başlıklar karışık ve etkisi sınırlı görünüyor.
06.11 07:47 N  NEWS (7 new) score -0.10 conf 0.35: Yeni başlıklar karışık: AI satışı ve risk kaçışı güvenli liman talebini artırıyor, ancak dolara olan talep altın için baskı yaratıyor. Petrol kaynaklı enflasyon endişeleri Fed'in sıkı kalma beklentisini güçlendirip altı aşağı çekebilir; ABD tarım dışı istihdam (NFP) verisi de yön belirleyici olacak. Bu nedenle hafif negatif, düşük güvenli bir görünüm.
06.11 07:47 N  GPT  score -0.25 conf 0.55: Asya’daki yapay zekâ kaynaklı riskten kaçışın dolara güvenli liman talebi yaratması ve yüksek petrolün enflasyon/faiz kaygılarını canlı tutması altın için kısa vadede hafif negatif. İran savaşıyla ilgili başlıklar yeni bir tırmanış göstermiyor; yaklaşan ABD istihdam verisi ve çelişkili altın haberle
06.11 07:59 N  NEWS (8 new) score -0.20 conf 0.35: Dolar güvenli liman talebiyle güçleniyor ve petrol kaynaklı enflasyon endişeleri faiz indirimi beklentilerini zayıflatarak altı baskılıyor; öte yandan İran'ın Katar aracılığıyla nükleer teklif göndermesi jeopolitik risk primini azaltabilir. Yaklaşan ABD tarım-dışı istihdam (NFP) verisinin sonucu belirsiz olduğundan genel etki hafif negatif ve düşük güvenilirlikli.
06.11 07:59 N  GPT  score -0.20 conf 0.43: Asya piyasalarındaki AI kaynaklı riskten kaçış dolara güvenli liman talebi getiriyor; bu, altın için güvenli liman desteğini kısmen dengeliyor. Altının petrol kaynaklı enflasyon kaygıları ve ABD istihdam verisi öncesi gerilemesi kısa vadede hafif aşağı yönlü baskıya işaret ederken, İran’ın ABD’ye ön
06.11 07:59 B5  SHORT gold 25000 USD x10 @ 4040.36 (TP 4028.24, SL 4048.44; news -0.20)
06.11 07:59 B5P  NEWS (44 new) score +0.35 conf 0.50: Hormuz'daki yeni tanker saldırıları ve Rusya'daki rafineri patlamaları/Ukrayna saldırıları arz riskini artırıp Brent'i 100 doların üzerine itti; ancak İran'ın Katar üzerinden nükleer öneri göndermesi, Orta Doğu barış beklentileri ve haftalık yaklaşık %12-13'lük düşüş yukarı yönlü hareketi sınırlayabilir, bu yüzden güven orta düzeyde.
06.11 07:59 B5P  GPT  score +0.55 conf 0.66: Hürmüz Boğazı’nda yeni tanker saldırısı haberleri ve Rusya’daki rafinerilere yönelik saldırı bildirimleri yakın vadeli arz riskini artırarak Brent’i destekliyor. İran’ın ABD’ye ilettiği bildirilen nükleer öneri ve daha geniş barış beklentileri bu etkiyi sınırlıyor; haberlerin bir kısmı doğrulanmamış
06.11 07:59 B5P  LONG BZ=F 25000 USD x10 @ 99.69 (TP 99.99, SL 99.50; news +0.45)
06.11 08:02 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
06.11 08:05 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
06.11 08:08 ERROR B5P: No market data for BZ=F: https://query2.finance.yahoo.com: HTTP 200 {"chart":{"result":[{"meta":{"currency":"USD","symbol":"BZ=F","exchangeName":"NYM","fullExchangeName":"NY Mercantile","i
06.11 08:12 B5  CLOSE short stop (gap): -56.23 USD
06.11 08:12 N  NEWS (9 new) score -0.25 conf 0.40: Altın, petrol kaynaklı enflasyon kaygıları ve güçlenen dolar (DXY 101.80) nedeniyle baskı altında; haberlerde "gold eases" ve "gold prices plummet" temaları öne çıkıyor. İran savaşı jeopolitik talebi destekleyici olsa da, yüksek petrol fiyatlarının faiz beklentilerini sertleştirmesi bu etkiyi dengeliyor. Yaklaşan ABD tarım dışı istihdam (NFP) verisi yönü belirsiz bir risk yarattığı için güven düşük tutuldu.
06.11 08:12 N  GPT  score -0.28 conf 0.57: DXY’nin 101,80’e yükselmesi ve yüksek petrol kaynaklı enflasyon/faiz endişeleri kısa vadede altını baskılıyor; yaklaşan ABD istihdam verisi de temkinli pozisyonlanmayı destekliyor. İran savaşı güvenli liman talebi sağlasa da haber akışı karışık ve etkisi net değil.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
