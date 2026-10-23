# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 23.10.2026 17:48 (İstanbul)

## Bot A — Kripto kurallar (spot, kaldıraçsız)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.30 $ | +0.30 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %100.0 | %100.0 |
| Ödenen komisyon/spread | 2.00 $ | 2.00 $ |

**Hesap değeri: 5,000.30 $** (başlangıç 5,000 $, +0.30 $ / %+0.01)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 09:46 | ETHUSDT | long | +0.30 $ | time limit |

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
| Net kâr/zarar | -44.43 $ | -40.61 $ |
| İşlem sayısı | 22 | 23 |
| Kazanma oranı | %27.3 | %30.4 |
| Ödenen komisyon/spread | 52.20 $ | 54.57 $ |

**Hesap değeri: 4,957.67 $** (başlangıç 5,000 $, -42.33 $ / %-0.85)

Açık pozisyonlar: PAXGUSDT short @ 4018.37 (TP 4014.35 / SL 4020.78)

Son haber analizi (23.10 17:48): Claude puan **-0.30**, güven 0.50 — Yeni başlıklar karışık: ABD-İsrail'in İran'a olası saldırı hazırlığı ve Trump'ın yeni saldırı tehdidi güvenli liman talebini destekliyor, ancak güçlü ABD PMI verileri ve Fed'in Aralık'ta faiz artırma olasılığını yükselten duruş, reel faizleri ve doları yukarı iterek altını baskılıyor. Ayrıca "Haven trade" çözülmesi ve reel faizlerin altın üzerindeki baskısı gibi haberler kısa vadede düşüş yönünü öne çıkarıyor; Kübü füze krizi haberi ise eski olduğu için dikkate alınmadı.

GPT (gpt-6-luna): puan **-0.25**, güven 0.55 — Güçlü ABD PMI verileri ve yüksek reel getiriler altının fırsat maliyetini artırarak kısa vadede baskı yaratabilir. İran gerilimi ve Batı Şeria’daki saldırı güvenli liman talebini destekliyor; bu karşıt etkiler düşüşün sınırlı kalabileceğini düşündürüyor.

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 17:26 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 17:11 | PAXGUSDT | short | +3.81 $ | take profit |
| 23.10 16:49 | PAXGUSDT | short | -4.19 $ | stop |
| 23.10 16:32 | PAXGUSDT | short | -4.51 $ | stop (gap) |
| 23.10 11:23 | PAXGUSDT | short | -4.19 $ | stop |

## Bot B2 — Altın: sıkı haber eşiği + büyük hedef (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -30.94 $ | -30.94 $ |
| İşlem sayısı | 5 | 5 |
| Kazanma oranı | %20.0 | %20.0 |
| Ödenen komisyon/spread | 11.86 $ | 11.86 $ |

**Hesap değeri: 4,969.06 $** (başlangıç 5,000 $, -30.94 $ / %-0.62)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 08:32 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 05:27 | PAXGUSDT | short | -11.19 $ | stop |
| 23.10 04:52 | PAXGUSDT | short | +13.82 $ | take profit |
| 23.10 03:57 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B4 — Altın: haberin TERSİ (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -11.18 $ | -11.18 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 4,988.82 $** (başlangıç 5,000 $, -11.18 $ / %-0.22)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 17:08 | PAXGUSDT | long | -11.18 $ | stop |

## Bot B3 — Altın: B2 + seans filtresi + momentum + kârı koruma

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | -11.19 $ | -11.19 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 4,988.81 $** (başlangıç 5,000 $, -11.19 $ / %-0.22)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 11:45 | PAXGUSDT | short | -11.19 $ | stop |

## Bot B5 — Altın: Claude + GPT hemfikir (TP 15$ / SL 10$)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +13.82 $ | +13.82 $ |
| İşlem sayısı | 1 | 1 |
| Kazanma oranı | %100.0 | %100.0 |
| Ödenen komisyon/spread | 2.37 $ | 2.37 $ |

**Hesap değeri: 5,013.82 $** (başlangıç 5,000 $, +13.82 $ / %+0.28)

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 23.10 17:11 | PAXGUSDT | short | +13.82 $ | take profit |

## Bot B6 — ABD hisse (Alpaca sanal): Claude + GPT hemfikir, 1:2

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +0.00 $ |
| İşlem sayısı | 0 | 0 |
| Kazanma oranı | %0.0 | %0.0 |
| Ödenen komisyon/spread | 0.00 $ | 0.00 $ |

**Hesap değeri: 100,000.00 $** (başlangıç 100,000 $, +0.00 $ / %+0.00)

## Son olaylar

```
23.10 17:18 B1  CLOSE short take profit: +3.81 USD
23.10 17:18 N  NEWS (10 new) score -0.15 conf 0.40: Fed'in Ekim'de faizi sabit tutmasının Aralık'ta faiz artırımı ihtimalini yükseltmesi ve doların direnci altın için kısa vadede baskı yaratıyor. İran savaşının uzayabileceği ve yeni saldırı tehditleri jeopolitik talebi destekliyor, ancak haber akışında güvenli liman talebinin zayıfladığına dair işaretler (altının güvenli liman işlemini kaybetmesi, Ukrayna'da ateşkes) bu desteği sınırlıyor.
23.10 17:18 N  GPT  score +0.18 conf 0.34: İran savaşının uzama ihtimali ve Paris’teki terör soruşturması güvenli liman talebini destekleyebilir; ancak Ukrayna’daki ateşkes haberi ve Fed’in Aralık’ta faiz artırımı ihtimalinin yükselmesi bu desteği sınırlıyor. Altının 4.000 dolar civarında seyretmesi ve haber akışının çelişkili olması nedeniy
23.10 17:18 B5  CLOSE short take profit: +13.82 USD
23.10 17:24 N  NEWS (8 new) score -0.35 conf 0.50: Fed'in Ekim'de faiz sabit tutmasının Aralık artırım olasılığını yükseltmesi, enflasyon beklentilerinin artması ve altının haftalık bazda en büyük kayıp yaşaması reel faiz kaynaklı baskıyı artırıyor. İran savaşı ve Paris'teki saldırı gibi jeopolitik gelişmeler güvenli liman talebini destekleyebilir, ancak haberlerde "güvenli liman talebinin kırıldığı" yorumu öne çıkıyor; bu nedenle net etki hafif-orta düzeyde negatif.
23.10 17:24 N  GPT  score -0.15 conf 0.36: Ukrayna’da ateşkes girişimi ve esir takası kısa vadede güvenli liman talebini bir miktar azaltabilir; Fed’in Aralık’ta faiz artırımı ihtimalinin yükselmesi de altın için baskı oluşturuyor. İran gerilimi ve diğer şiddet haberleri bu etkiyi dengeliyor; sinyaller karışık olduğundan yön güveni düşük.
23.10 17:24 B1  SHORT gold 5000 USD x10 @ 4008.70 (TP 4004.69, SL 4011.10; news -0.35)
23.10 17:33 B1  CLOSE short stop: -4.19 USD
23.10 17:33 N  NEWS (6 new) score -0.12 conf 0.35: Fed'in Ekim'de faiz sabit tutmasının Aralık artırım olasılıklarını yükseltmesi ve "altın güvenli liman talebini kaybediyor" başlığı altın için kısa vadede baskı yaratıyor. İran savaşı ve jeopolitik gerilim riskleri destekleyici olsa da zaten fiyatlanmış görünüyor; enflasyon beklentilerinin yükselmesi ve ABD iş aktivitesindeki karışık veriler ise sinyalleri çelişkili kılıyor.
23.10 17:33 N  GPT  score -0.15 conf 0.34: ABD iş aktivitesindeki yavaşlama altını destekleyebilir; ancak talebin fiyat baskılarını artırması ve Aralık’ta faiz artırımı olasılığının yükselmesi kısa vadede daha güçlü dolar/faiz beklentisiyle baskı yaratabilir. Ukrayna’daki esir takası gerilimi bir miktar azaltırken, İran’a ilişkin haberler gü
23.10 17:40 N  NEWS (8 new) score -0.05 conf 0.35: 
23.10 17:40 N  GPT  score +0.15 conf 0.38: İran savaşının yeniden başlayabileceğine dair haberler ve saldırıların önlenmesi kısa vadede güvenli liman talebini destekleyebilir. Ancak artan enflasyon baskıları ve Fed’in faiz artırımı ihtimalinin yükselmesi altın için olumsuz; net etki bu nedenle sınırlı ve belirsiz.
23.10 17:48 N  NEWS (8 new) score -0.30 conf 0.50: Yeni başlıklar karışık: ABD-İsrail'in İran'a olası saldırı hazırlığı ve Trump'ın yeni saldırı tehdidi güvenli liman talebini destekliyor, ancak güçlü ABD PMI verileri ve Fed'in Aralık'ta faiz artırma olasılığını yükselten duruş, reel faizleri ve doları yukarı iterek altını baskılıyor. Ayrıca "Haven trade" çözülmesi ve reel faizlerin altın üzerindeki baskısı gibi haberler kısa vadede düşüş yönünü öne çıkarıyor; Kübü füze krizi haberi ise eski olduğu için dikkate alınmadı.
23.10 17:48 N  GPT  score -0.25 conf 0.55: Güçlü ABD PMI verileri ve yüksek reel getiriler altının fırsat maliyetini artırarak kısa vadede baskı yaratabilir. İran gerilimi ve Batı Şeria’daki saldırı güvenli liman talebini destekliyor; bu karşıt etkiler düşüşün sınırlı kalabileceğini düşündürüyor.
23.10 17:48 B1  SHORT gold 5000 USD x10 @ 4018.37 (TP 4014.35, SL 4020.78; news -0.30)
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
