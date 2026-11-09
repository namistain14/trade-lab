# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 10.11.2026 00:27 (İstanbul)

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
| Net kâr/zarar | +0.00 $ | -679.43 $ |
| İşlem sayısı | 0 | 68 |
| Kazanma oranı | %0.0 | %36.8 |
| Ödenen komisyon/spread | 0.00 $ | 806.99 $ |

**Hesap değeri: 4,320.57 $** (başlangıç 5,000 $, -679.43 $ / %-13.59)

Son haber analizi (10.11 00:25): Claude puan **+0.10**, güven 0.40 — Yeni gelen "sıcak ABD enflasyonu / Fed faiz artırımı" başlığı altın için baskı yaratabilir, ancak petrol düşüşü ve zayıflayan dolar (İran müzakere haberleri, Hormuz talebinde gevşeme) enflasyon ve dolar kanalından altı destekliyor; ayrıca Hegseth/İran savaşı haberleri jeopolitik risk primi sağlıyor. Sinyaller karışık ve birçoğu zaten fiyatlanmış olduğu için hafif pozitif, düşük güvenli bir görünüm.

GPT (gpt-6-luna): puan **+0.15**, güven 0.38 — Petrol ve doların gerilemesi altını kısa vadede destekliyor; yen tahmini de dolar zayıflığına işaret ediyor. Ancak enflasyonun yüksek kalacağı ve Fed’in faiz artırabileceği beklentisi bu desteği sınırlıyor; CPI henüz yayımlanmadığından yön sinyali kesin değil.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 09.11 22:29 | PAXGUSDT | short | -55.93 $ | stop |
| 09.11 17:36 | PAXGUSDT | long | -55.90 $ | stop |
| 09.11 14:18 | PAXGUSDT | short | -55.93 $ | stop |
| 09.11 09:20 | PAXGUSDT | long | -55.90 $ | stop |
| 06.11 18:11 | PAXGUSDT | short | -55.94 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | -55.58 $ |
| İşlem sayısı | 0 | 3 |
| Kazanma oranı | %0.0 | %33.3 |
| Ödenen komisyon/spread | 0.00 $ | 52.30 $ |

**Hesap değeri: 4,944.42 $** (başlangıç 5,000 $, -55.58 $ / %-1.11)

Son haber analizi (09.11 23:06): Claude puan **-0.10**, güven 0.40 — Brent yaklaşık %5 düşüşle 93,5 dolara geriledi; ABD-İran anlaşması umutları ana itici güç ve bu bearish etki kısmen fiyatlandı. Buna karşın Suudi Arabistan'ın Doğu-Batı boru hattına yönelik saldırısı ve Hürmüz Boğazı'ndaki patlama haberleri arz riskini canlı tutuyor, bu nedenle etki çelişkili ve sınırlı.

GPT (gpt-6-luna): puan **-0.18**, güven 0.42 — ABD-İran anlaşması umutlarıyla Brent’in yaklaşık %5 gerilemesi kısa vadede aşağı yönlü momentumu destekliyor. Ancak Hürmüz’de patlama haberleri ve Suudi Arabistan’ın Doğu-Batı petrol hattına yönelik sınırlı saldırı bu düşüşü sınırlayabilecek arz riskleri yaratıyor; haberler çelişkili ve bir kısmı fi

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
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

**Hesap değeri: 111,691.09 $** (başlangıç 100,000 $, +11691.09 $ / %+11.69)

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
09.11 23:36 N  NEWS (7 new) score +0.15 conf 0.40: Altın, petrol düşüşünün dolarda zayıflama yaratmasıyla 4.100 doların üzerine çıktı ve Fed faiz artırımı beklentilerine rağmen yükseldi; bu, kısa vadede boğa yönlü bir tepki. Buna karşın Fed yetkilisi Daly'nin daha fazla faiz artırımına işaret etmesi ve enflasyonun inatçı kalacağı beklentisi altın için baskı oluşturuyor; Hegseth'in görevden alınma girişimi gibi haberlerin piyasa etkisi sınırlı.
09.11 23:36 N  GPT  score +0.25 conf 0.45: Doların İran görüşmeleriyle zayıflaması ve altının 4.100 doların üzerine çıkması kısa vadede yükselişi destekliyor. Ancak Fed’in daha fazla faiz artırabileceği beklentisi ve yükselen tahvil getirileri ters yönde; haber akışı bu nedenle çelişkili.
09.11 23:45 ERROR B6: Alpaca DELETE /v2/positions/AAPL: 403 {"available":"0","code":40310000,"existing_qty":"318","held_for_orders":"318","message":"insufficient qty available for order (requested: 318, available: 0)","symbol":"AAPL"}
09.11 23:48 N  NEWS (7 new) score +0.05 conf 0.35: Haberler karışık: Petrol satışının dolarý zayýflatmasý ve altýn fiyatýnýn 4.100 doların üzerine çýkmasý altýný destekliyor, ancak Fed yetkililerinin (Daly, Barkin) faiz artýrýmý sinyalleri ve enflasyon endiþeleri baský yaratýyor. İran'la müzakere haberleri risk iþtahýný artýrarak güvenli liman talebini sýnýrlýyor; Hegseth/İran savaþý ve Türkiye'deki fabrika patlamasý gibi jeopolitik haberler ise büyük ölçüde fiyatlanmýþ durumda. Net etki hafif pozitif ama belirsiz.
09.11 23:48 N  GPT  score +0.18 conf 0.34: İran parlamento başkanının İsrail’in ABD’yi savaşa çekmeye çalıştığı yönündeki açıklaması sınırlı güvenli liman talebini destekleyebilir. Barkin’in temkinli politika vurgusu belirgin bir şahin sinyal değil; ancak haber akışı karışık ve etkisi belirsiz.
09.11 23:48 B6  CLOSE long QQQ seans sonu: +996.60 USD
09.11 23:48 B6  CLOSE long SPY seans sonu: +281.01 USD
09.11 23:48 B6  CLOSE long TSLA seans sonu: +1105.07 USD
09.11 23:48 B6  seans kapanışı: tüm pozisyonlar kapatıldı
10.11 00:00 N  NEWS (9 new) score +0.10 conf 0.35: Altın, petrol ve doların gerilemesiyle toparlandı, bu kısa vadede destekleyici. Ancak Fed'in faiz artırımı beklentileri (Daly, Barkin) ve İran'la müzakere haberlerinin risk iştahını artırması altını sınırlıyor; Hegseth'e yönelik görevden alma girişimi ise jeopolitik açıdan büyük yeni bir şok değil.
10.11 00:00 N  GPT  score +0.25 conf 0.40: Petrol ve doların gerilemesi altına kısa vadeli destek sağlıyor; İran savaşıyla ilgili söylemler de sınırlı güvenli liman talebi yaratabilir. Ancak manşetlerin bir kısmı mevcut fiyat hareketini zaten yansıtıyor ve CPI verisine ilişkin belirsizlik yönü netleştirmiyor.
10.11 00:13 N  NEWS (15 new) score +0.10 conf 0.35: 
10.11 00:13 N  GPT  score +0.25 conf 0.38: İran-Hürmüz geriliminin yumuşayabileceği haberiyle petrol ve doların gerilemesi altına kısa vadede destek sağlıyor; ancak Fed’den gelen temkinli/şahin sinyaller ve yaklaşan enflasyon verisi yükseliş potansiyelini sınırlıyor. Yeni siyasi haberlerin çoğu doğrudan fiyat katalizörü değil ve genel sinyal
10.11 00:25 N  NEWS (6 new) score +0.10 conf 0.40: Yeni gelen "sıcak ABD enflasyonu / Fed faiz artırımı" başlığı altın için baskı yaratabilir, ancak petrol düşüşü ve zayıflayan dolar (İran müzakere haberleri, Hormuz talebinde gevşeme) enflasyon ve dolar kanalından altı destekliyor; ayrıca Hegseth/İran savaşı haberleri jeopolitik risk primi sağlıyor. Sinyaller karışık ve birçoğu zaten fiyatlanmış olduğu için hafif pozitif, düşük güvenli bir görünüm.
10.11 00:25 N  GPT  score +0.15 conf 0.38: Petrol ve doların gerilemesi altını kısa vadede destekliyor; yen tahmini de dolar zayıflığına işaret ediyor. Ancak enflasyonun yüksek kalacağı ve Fed’in faiz artırabileceği beklentisi bu desteği sınırlıyor; CPI henüz yayımlanmadığından yön sinyali kesin değil.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
