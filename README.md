# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 01:07 (İstanbul)

## Bot A — Kripto kurallar (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot A2 — Kripto: sert düşüş sonrası toparlanma (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot B1 — Altın + haber (şimdiki ayarlar, TP 5$ / SL 3$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -4.19 $ | -0.37 $ |
| İşlem sayısı | 1 | 2 |
| Kazanma oranı | %0.0 | %50.0 |
| Ödenen komisyon/spread | 2.37 $ | 4.74 $ |

**Hesap değeri: 4,999.63 $** (başlangıç 5,000 $, -0.37 $ / %-0.01)

Son haber analizi (23.10 01:07): puan **+0.05**, güven 0.30 — Yeni gelen başlıkların çoğu altı doğrudan etkilemiyor (Ukrayna-Starlink, Kansas dizel tartışması, Kansas Fed imalat verisi, EUR/USD tahmini). Arka planda İran savaşı ve petrol fiyatının 110 doları aşması güvenli liman talebini destekliyor, ancak enerji kaynaklı enflasyon baskısı Fed'in sıkı kalma beklentisini güçlendirerek altı aşağı çekebilir; bu karşıt etkiler nedeniyle sinyal zayıf ve net bir yön yok.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 00:03 | PAXGUSDT | short | -4.19 $ | stop |
| 22.10 23:16 | PAXGUSDT | short | +3.82 $ | take profit |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Bot B3 — Altın: B2 + seans filtresi + momentum + kârı koruma

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

## Son olaylar

```
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
23.10 00:30 B  NEWS (9 new) score +0.20 conf 0.35: İran savaşına ilişkin jeopolitik gerilim, petrol fiyatlarının 110 doların üzerine çıkması ve piyasalardaki sert düşüş güvenli liman talebini destekliyor; bu nedenle altın için hafif pozitif bir eğilim var. Ancak petrol kaynaklı enflasyon riski Fed'in sıkı kalma beklentisini artırıp reel faizleri yükseltebileceğinden etki sınırlı ve belirsiz; haberlerin çoğu da bilinen veya fiyatlanmış gelişmeler.
23.10 00:39 B  NEWS (12 new) score +0.25 conf 0.45: 
23.10 00:49 N  NEWS (14 new) score +0.10 conf 0.30: İran savaşının sürmesi, petrol fiyatlarının 110 doların üzerinde seyretmesi ve piyasalardaki risk-kaçışı altın için hafif destekleyici; ancak petrol kaynaklı enflasyon baskısı Fed'in sıkı kalma beklentisini güçlendirip altını aşağı çekebilir. Yeni başlıkların çoğu (Newmont kazançları, Ukrayna, Kansas dizel tartışması) altın fiyatına doğrudan etki etmeyen veya zaten fiyatlanmış haberler, bu yüzden güven düşük.
23.10 00:58 N  NEWS (6 new) score +0.10 conf 0.30: Yeni başlıklar karışık: Romanya'nın Rusya'nın savaşı tırmandırdığı uyarısı ve Trump'ın enerji üretimi için Savunma Üretim Yasası'nı devreye alması güvenli liman talebini hafifçe destekliyor. Ancak petrolün 110 doların üzerine çıkması enflasyon ve sıkı para politikası beklentilerini canlandırarak altın üzerinde baskı yaratabilir. Çoğu haber zaten fiyatlanmış veya dolaylı olduğundan güven düşük.
23.10 01:07 N  NEWS (8 new) score +0.05 conf 0.30: Yeni gelen başlıkların çoğu altı doğrudan etkilemiyor (Ukrayna-Starlink, Kansas dizel tartışması, Kansas Fed imalat verisi, EUR/USD tahmini). Arka planda İran savaşı ve petrol fiyatının 110 doları aşması güvenli liman talebini destekliyor, ancak enerji kaynaklı enflasyon baskısı Fed'in sıkı kalma beklentisini güçlendirerek altı aşağı çekebilir; bu karşıt etkiler nedeniyle sinyal zayıf ve net bir yön yok.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
