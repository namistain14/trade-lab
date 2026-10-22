# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 00:21 (İstanbul)

## Bot A — Kripto kurallar (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot B — Altın + haber (1:10 kaldıraç)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -4.19 $ | -0.37 $ |
| İşlem sayısı | 1 | 2 |
| Kazanma oranı | %0.0 | %50.0 |
| Ödenen komisyon/spread | 2.37 $ | 4.74 $ |

**Hesap değeri: 4,999.63 $** (başlangıç 5,000 $, -0.37 $ / %-0.01)

Son haber analizi (23.10 00:19): puan **+0.20**, güven 0.35 — Yeni haberlerde İran savaşının yeniden başlayabileceği ve ABD-İsrail saldırılarının Kasım'da planlandığı yönündeki riskler, risk-off ortamı ve petrol fiyatlarının 110 doları aşması gibi unsurlar güvenli liman talebini hafifçe destekliyor. Ancak petrol kaynaklı enflasyon baskısı faiz indirimi beklentilerini geciktirebilir, ABD enflasyonu da belirgin bir sürpriz göstermiyor; bu nedenle etki sınırlı ve karışık.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 00:03 | PAXGUSDT | short | -4.19 $ | stop |
| 22.10 23:16 | PAXGUSDT | short | +3.82 $ | take profit |

## Son olaylar

```
22.10 21:59 B  NEWS score +0.20 conf 0.40: Hormuz'da 7 tankerin vurulduğu iddiası ve Iran savaşının yeniden başlayabileceğine dair korkular jeopolitik risk kaynaklı güvenli liman talebini destekliyor. Ancak Treasury getirilerinin %5'in altına inmesi ve doların zayıflaması altın için olumlu; öte yandan haberler altının güvenli liman yerine ABD tahvillerine kaydığını ve petrol kaynaklı faiz tartışmasının altını baskıladığını da gösteriyor. Bu çelişkili sinyaller nedeniyle yön belirsiz, güven düşük.
22.10 22:49 B  NEWS (45 new) score -0.10 conf 0.35: Haberler karışık: Hürmüz'de tanker saldırıları ve Rusya'nın saldırı tırmanışı jeopolitik risk yaratıp altını destekliyor, ancak altına özgü başlıklar (güvenli liman talebinin Hazine tahvillerine kayması, petrol fiyatlarının faiz tartışmasını yeniden alevlendirmesi, Fed'in yakın zamanda faiz artırmaması beklentisi) altın üzerinde baskı oluşturuyor. Net etki hafif negatif ve düşük güvenilirlikte.
22.10 22:59 B  NEWS (5 new) score +0.10 conf 0.35: Jeopolitik risk artıyor (Hürmüz'de tanker saldırıları, İran'ın Körfez tesislerini tehdidi) ve bu altın için güvenli liman talebini destekliyor; ancak petrol fiyatlarındaki yükseliş faiz tartışmasını sertleştiriyor, dolar zayıflamasına rağmen altın "güvenli liman talebinin Hazine tahvillerine kayması" nedeniyle düştü. Sinyaller karışık ve bir kısmı zaten fiyatlanmış olduğu için güven düşük.
22.10 23:08 B  NEWS (7 new) score -0.30 conf 0.45: Yeni haberlerde altın sert düşüş (“gold plunges”) ve güvenli liman talebinin ABD Hazinelerine kayması öne çıkıyor; petrol 110 doların üzerinde olduğundan enflasyon ve Fed'in sıkı kalma beklentisi altın için baskılayıcı. Buna karşılık İran savaşının yeniden başlama riski ve Hormuz'da tanker saldırıları jeopolitik talebi destekliyor, bu da sinyalleri karışık kılıyor; bu nedenle güven orta düzeyde tutuldu.
22.10 23:08 B  SHORT gold 5000 USD x10 @ 4038.51 (TP 4034.47, SL 4040.94; news -0.30)
22.10 23:21 B  CLOSE short take profit: +3.82 USD
22.10 23:21 B  NEWS (8 new) score -0.10 conf 0.30: 
22.10 23:30 B  NEWS (5 new) score +0.15 conf 0.35: Jeopolitik risk (Hürmüz'de tanker saldırıları, İran'ın Körfez tesislerini tehdidi) ve ABD doların zayıflaması altın için destekleyici; ancak petrol 110 doların üzerinde olduğundan enflasyon ve sert Fed beklentisi, ayrıca güvenli liman talebinin Hazine tahvillerine kayması altın için olumsuz. Sinyaller çelişkili olduğundan güven düşük.
22.10 23:39 B  NEWS (6 new) score +0.10 conf 0.30: 
22.10 23:49 B  NEWS (12 new) score -0.20 conf 0.40: 
22.10 23:49 B  SHORT gold 5000 USD x10 @ 4035.01 (TP 4030.98, SL 4037.43; news -0.20)
23.10 00:00 B  NEWS (11 new) score -0.10 conf 0.35: Hormuz'da 7 tankere yönelik saldırı ve petrolün 110 doların üzerine çıkması jeopolitik güvenli liman talebini destekliyor, ancak enflasyon baskısı artırdığı için Fed'in sıkı kalma beklentisini güçlendirip altın üzerinde baskı yaratabilir. Tahvil faizlerinin geri dönmesi ve ortalama mortgage oranının hafif gerilemesi sınırlı bir yumuşama işareti; haberlerin çoğu ise altın fiyatını doğrudan etkilemeyen gürültü niteliğinde. Net etki hafif negatif, düşük güvenle.
23.10 00:09 B  CLOSE short stop: -4.19 USD
23.10 00:09 B  NEWS (10 new) score -0.15 conf 0.30: Yeni başlıklar karışık: "Gold plunges" başlığı kısa vadede baskı işareti veriyor, ancak petrol 110 doların üzerinde ve İran savaşı/Ukrayna'daki çatışmalar güvenli liman talebini destekliyor. Enflasyon kaynaklı faiz beklentisi endişesi ile jeopolitik risk birbirini dengeliyor; net etki hafif negatif, güven düşük.
23.10 00:19 B  NEWS (10 new) score +0.20 conf 0.35: Yeni haberlerde İran savaşının yeniden başlayabileceği ve ABD-İsrail saldırılarının Kasım'da planlandığı yönündeki riskler, risk-off ortamı ve petrol fiyatlarının 110 doları aşması gibi unsurlar güvenli liman talebini hafifçe destekliyor. Ancak petrol kaynaklı enflasyon baskısı faiz indirimi beklentilerini geciktirebilir, ABD enflasyonu da belirgin bir sürpriz göstermiyor; bu nedenle etki sınırlı ve karışık.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
