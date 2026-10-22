# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 22.10.2026 23:39 (İstanbul)

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
| Net kâr/zarar | +3.82 $ | +3.82 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %100.0 | %100.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 5,003.82 $** (başlangıç 5,000 $, +3.82 $ / %+0.08)

Son haber analizi (22.10 23:39): puan **+0.10**, güven 0.30 — Jeopolitik risk (Hürmüz'de tanker saldırıları, İran'ın Körfez tesislerini tehdidi) ve ABD doların zayıflaması altın için destekleyici; ancak petrol 110 doların üzerinde olduğundan enflasyon ve sert Fed beklentisi, ayrıca güvenli liman talebinin Hazine tahvillerine kayması altın için olumsuz. Sinyaller çelişkili olduğundan güven düşük.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 22.10 23:16 | PAXGUSDT | short | +3.82 $ | take profit |

## Son olaylar

```
22.10 20:51 B  NEWS score -0.30 conf 0.40: The most gold-relevant items lean bearish: a 2% gold drop on energy-driven inflation worries and commentary that hot September PPI makes an October Fed rate hike nearly assured, which pushes real yields up. Geopolitical headlines (Iran war risk, NATO Black Sea buildup) offer some safe-haven support, but they are mostly old or already priced in, so the net tilt is mildly bearish with low confidence.
22.10 21:59 B  NEWS score +0.20 conf 0.40: Hormuz'da 7 tankerin vurulduğu iddiası ve Iran savaşının yeniden başlayabileceğine dair korkular jeopolitik risk kaynaklı güvenli liman talebini destekliyor. Ancak Treasury getirilerinin %5'in altına inmesi ve doların zayıflaması altın için olumlu; öte yandan haberler altının güvenli liman yerine ABD tahvillerine kaydığını ve petrol kaynaklı faiz tartışmasının altını baskıladığını da gösteriyor. Bu çelişkili sinyaller nedeniyle yön belirsiz, güven düşük.
22.10 22:49 B  NEWS (45 new) score -0.10 conf 0.35: Haberler karışık: Hürmüz'de tanker saldırıları ve Rusya'nın saldırı tırmanışı jeopolitik risk yaratıp altını destekliyor, ancak altına özgü başlıklar (güvenli liman talebinin Hazine tahvillerine kayması, petrol fiyatlarının faiz tartışmasını yeniden alevlendirmesi, Fed'in yakın zamanda faiz artırmaması beklentisi) altın üzerinde baskı oluşturuyor. Net etki hafif negatif ve düşük güvenilirlikte.
22.10 22:59 B  NEWS (5 new) score +0.10 conf 0.35: Jeopolitik risk artıyor (Hürmüz'de tanker saldırıları, İran'ın Körfez tesislerini tehdidi) ve bu altın için güvenli liman talebini destekliyor; ancak petrol fiyatlarındaki yükseliş faiz tartışmasını sertleştiriyor, dolar zayıflamasına rağmen altın "güvenli liman talebinin Hazine tahvillerine kayması" nedeniyle düştü. Sinyaller karışık ve bir kısmı zaten fiyatlanmış olduğu için güven düşük.
22.10 23:08 B  NEWS (7 new) score -0.30 conf 0.45: Yeni haberlerde altın sert düşüş (“gold plunges”) ve güvenli liman talebinin ABD Hazinelerine kayması öne çıkıyor; petrol 110 doların üzerinde olduğundan enflasyon ve Fed'in sıkı kalma beklentisi altın için baskılayıcı. Buna karşılık İran savaşının yeniden başlama riski ve Hormuz'da tanker saldırıları jeopolitik talebi destekliyor, bu da sinyalleri karışık kılıyor; bu nedenle güven orta düzeyde tutuldu.
22.10 23:08 B  SHORT gold 5000 USD x10 @ 4038.51 (TP 4034.47, SL 4040.94; news -0.30)
22.10 23:21 B  CLOSE short take profit: +3.82 USD
22.10 23:21 B  NEWS (8 new) score -0.10 conf 0.30: 
22.10 23:30 B  NEWS (5 new) score +0.15 conf 0.35: Jeopolitik risk (Hürmüz'de tanker saldırıları, İran'ın Körfez tesislerini tehdidi) ve ABD doların zayıflaması altın için destekleyici; ancak petrol 110 doların üzerinde olduğundan enflasyon ve sert Fed beklentisi, ayrıca güvenli liman talebinin Hazine tahvillerine kayması altın için olumsuz. Sinyaller çelişkili olduğundan güven düşük.
22.10 23:39 B  NEWS (6 new) score +0.10 conf 0.30: 
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
