# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 22.10.2026 22:59 (İstanbul)

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
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 5,000.00 $** (başlangıç 5,000 $, +0.00 $ / %+0.00)

Son haber analizi (22.10 22:59): puan **+0.10**, güven 0.35 — Jeopolitik risk artıyor (Hürmüz'de tanker saldırıları, İran'ın Körfez tesislerini tehdidi) ve bu altın için güvenli liman talebini destekliyor; ancak petrol fiyatlarındaki yükseliş faiz tartışmasını sertleştiriyor, dolar zayıflamasına rağmen altın "güvenli liman talebinin Hazine tahvillerine kayması" nedeniyle düştü. Sinyaller karışık ve bir kısmı zaten fiyatlanmış olduğu için güven düşük.

## Son olaylar

```
22.10 20:51 B  NEWS score -0.30 conf 0.40: The most gold-relevant items lean bearish: a 2% gold drop on energy-driven inflation worries and commentary that hot September PPI makes an October Fed rate hike nearly assured, which pushes real yields up. Geopolitical headlines (Iran war risk, NATO Black Sea buildup) offer some safe-haven support, but they are mostly old or already priced in, so the net tilt is mildly bearish with low confidence.
22.10 21:59 B  NEWS score +0.20 conf 0.40: Hormuz'da 7 tankerin vurulduğu iddiası ve Iran savaşının yeniden başlayabileceğine dair korkular jeopolitik risk kaynaklı güvenli liman talebini destekliyor. Ancak Treasury getirilerinin %5'in altına inmesi ve doların zayıflaması altın için olumlu; öte yandan haberler altının güvenli liman yerine ABD tahvillerine kaydığını ve petrol kaynaklı faiz tartışmasının altını baskıladığını da gösteriyor. Bu çelişkili sinyaller nedeniyle yön belirsiz, güven düşük.
22.10 22:49 B  NEWS (45 new) score -0.10 conf 0.35: Haberler karışık: Hürmüz'de tanker saldırıları ve Rusya'nın saldırı tırmanışı jeopolitik risk yaratıp altını destekliyor, ancak altına özgü başlıklar (güvenli liman talebinin Hazine tahvillerine kayması, petrol fiyatlarının faiz tartışmasını yeniden alevlendirmesi, Fed'in yakın zamanda faiz artırmaması beklentisi) altın üzerinde baskı oluşturuyor. Net etki hafif negatif ve düşük güvenilirlikte.
22.10 22:59 B  NEWS (5 new) score +0.10 conf 0.35: Jeopolitik risk artıyor (Hürmüz'de tanker saldırıları, İran'ın Körfez tesislerini tehdidi) ve bu altın için güvenli liman talebini destekliyor; ancak petrol fiyatlarındaki yükseliş faiz tartışmasını sertleştiriyor, dolar zayıflamasına rağmen altın "güvenli liman talebinin Hazine tahvillerine kayması" nedeniyle düştü. Sinyaller karışık ve bir kısmı zaten fiyatlanmış olduğu için güven düşük.
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
