# trade-lab — SANAL işlem denemesi

> ⚠️ Bu tamamen **sanal (paper) trading**. Hiçbir borsaya emir gitmez, gerçek para yoktur.
> Son güncelleme: 06.11.2026 07:11 (İstanbul)

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
| Net kâr/zarar | -167.72 $ | -201.66 $ |
| İşlem sayısı | 3 | 55 |
| Kazanma oranı | %0.0 | %41.8 |
| Ödenen komisyon/spread | 35.49 $ | 652.94 $ |

**Hesap değeri: 4,798.34 $** (başlangıç 5,000 $, -201.66 $ / %-4.03)

Son haber analizi (06.11 07:10): Claude puan **+0.02**, güven 0.30 — Haberler karışık: İran savaşı kaynaklı petrol enflasyonu endişesi ve bekleyen ABD tarım dışı istihdam (NFP) verisi altını baskılayabilirken, Trump'ın savaş tonunun yumuşaması jeopolitik risk primini azaltıyor. Fiyat seviyeleri de çelişkili (4.000 üstü ile 4.060-4.100 altı), bu yüzden yön belirsiz ve güven düşük.

GPT (gpt-6-luna): puan **-0.15**, güven 0.35 — İran savaşına ilişkin Trump’ın daha az yıkıcı tonda konuşması güvenli liman talebini bir miktar azaltabilir; altının petrol kaynaklı enflasyon kaygılarıyla gerilediği haberleri de kısa vadede baskı unsuru. Doların zayıflaması bu etkiyi dengelerken, yaklaşan ABD istihdam verisi yön konusunda belirsiz

Son işlemler:

| Kapanış | Parite | Yön | Sonuç | Neden |
|---|---|---|---|---|
| 06.11 04:01 | PAXGUSDT | long | -55.91 $ | stop |
| 06.11 03:47 | PAXGUSDT | long | -55.90 $ | stop |
| 06.11 02:52 | PAXGUSDT | long | -55.91 $ | stop |
| 05.11 19:13 | PAXGUSDT | short | -55.93 $ | stop |
| 05.11 19:03 | PAXGUSDT | short | -55.93 $ | stop |

## Bot B5P — Brent petrol: Claude + GPT hemfikir (x10, 25.000 $ pozisyon)

| | Bugün | Toplam |
|---|---|---|
| Net kâr/zarar | +0.00 $ | +66.43 $ |
| İşlem sayısı | 0 | 1 |
| Kazanma oranı | %0.0 | %100.0 |
| Ödenen komisyon/spread | 0.00 $ | 17.17 $ |

**Hesap değeri: 5,066.43 $** (başlangıç 5,000 $, +66.43 $ / %+1.33)

Son haber analizi (05.11 07:59): Claude puan **-0.05**, güven 0.40 — Haberler çelişkili: İran'ın Hürmüz'de dört tankerin mayınlarla vurulduğunu öne sürmesi ve petrol fiyatlarındaki Hürmüz arz riskleri fiyatı yukarı iter; buna karşılık Brent'in İran müzakereleri nedeniyle 4 haftalık dibe inmesi ve ABD-İran arasında anlaşmanın hâlâ uzak olması aşağı yönlü baskı yaratır. Tanker iddiası doğrulanmamış olduğu için net etki hafif pozitif, güven düşük.

GPT (gpt-6-luna): puan **+0.28**, güven 0.55 — Hürmüz’de iki tanker ve bir römorkörün alev aldığı haberi, doğrulanması hâlinde yakın vadeli arz ve taşımacılık risk primini artırarak Brent’i yukarı destekleyebilir. Ancak İran geriliminin azalacağı beklentileriyle süren sert satış ve haberin nedeni hakkındaki belirsizlik yükseliş etkisini sınırlıy

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
06.11 05:45 N  GPT  score +0.30 conf 0.44: İran’a ilişkin yaklaşan karar ve sert tehditler ile hisse senetlerindeki düşüş, kısa vadede güvenli liman talebini destekleyebilir. Doların istikrar kazanması altını sınırlarken, haber akışı karışık ve bir kısmı zaten biliniyor.
06.11 05:57 N  NEWS (2 new) score +0.30 conf 0.40: İran savaşına ilişkin yeni gelişmeler (Trump'ın "yakında" karar açıklaması, İran güvenlik şefinin Putin'le görüşmesi) jeopolitik risk ve güvenli liman talebini artırarak altı destekliyor. ABD hisselerindeki sert düşüş de risk iştahını zayıflatıyor; ancak dolar yatay seyrediyor ve Fed beklentilerine dair yeni bir sinyal yok, bu da yukarı yönlü etkiyi sınırlıyor. Haberler karışık ve bir kısmı zaten fiyatlanmış olduğu için güven düşük.
06.11 05:57 N  GPT  score +0.20 conf 0.34: İran güvenlik şefinin Putin’le görüşmesi ve süren savaş haberleri kısa vadede güvenli liman talebini destekleyebilir; ancak görüşmenin etkisi belirsiz. Doların dayanıklı seyri ve yaklaşan ABD istihdam verisi altındaki olası yükselişi sınırlıyor.
06.11 06:09 N  NEWS (7 new) score +0.35 conf 0.50: Küresel teknoloji hisselerindeki sert düşüş ve risk iştahındaki zayıflama, İran savaşına dair belirsizlik ve "karar yakında" açıklamaları güvenli liman talebini destekliyor. Dolar ise ABD ara seçim sonrası sakinleşiyor; bu da altın için sınırlı bir baskı oluşturuyor. Altının 4.000 doların üzerine yeniden çıkması gibi haberler kısmen fiyatlanmış olduğu için güveni sınırlı tutuyorum.
06.11 06:09 N  GPT  score +0.25 conf 0.34: Hisse senetlerindeki sert düşüş ve İran gerilimine ilişkin haberler kısa vadede güvenli liman talebini destekleyebilir. Ancak doların güçlü kalması, yaklaşan ABD istihdam verisi ve haber akışındaki çok sayıda ilgisiz ya da tekrarlanan başlık altının yükselişini sınırlıyor.
06.11 06:21 N  NEWS (7 new) score +0.50 conf 0.60: Jeopolitik risk (İran savaşında olası yeni saldırı kararı), hisse senetlerindeki sert düşüş ve güvenli liman talebi altını destekliyor; ayrıca altın seçim sonrası haftalık en büyük kazanım için yolda. Dolar stabil kaldığı ve Fed beklentilerine dair yeni bir sıkılaştırma sinyali olmadığı için baskı sınırlı; yine de bazı haberler genel nitelikli ve fiyatlanmış olabileceğinden güven orta düzeyde.
06.11 06:21 N  GPT  score +0.25 conf 0.35: İran savaşının süreceğine dair yeni açıklama kısa vadede güvenli liman talebini destekleyebilir. Ancak haber doğrudan yeni bir askerî gelişme değil; altındaki güçlü yükselişin ve doların toparlanmasının etkisi zaten kısmen fiyatlanmış olabilir.
06.11 06:34 N  NEWS (9 new) score +0.15 conf 0.35: Haber akışı karışık: ABD ara seçimleri sonrası altın haftalık en büyük kazanç yolunda ve borsalarda sert düşüş risk-off talebini destekliyor, ancak Trump'ın İran savaşı tonunu yumuşatması jeopolitik prim baskısı yaratabilir ve güçlü dolar ile NFP öncesi belirsizlik kısa vadeli yönü sınırlıyor. Birçok başlık tekrar eden veya fiyatlanmış haber niteliğinde olduğu için güven düşük tutuldu.
06.11 06:34 N  GPT  score -0.15 conf 0.34: NFP öncesinde doların güçlenmesi ve altın yükselişinin yavaşladığına dair haberler kısa vadede baskı yaratabilir. Trump’ın İran konusunda daha temkinli tonu güvenli liman talebini azaltırken, jeopolitik belirsizlik ve hisse senetlerindeki düşüş aşağı yönü sınırlıyor.
06.11 06:46 N  NEWS (8 new) score +0.05 conf 0.30: Haberler karışık: İran savaşı ve Trump'ın kararının "yakında" açıklanacağı beklentisi jeopolitik risk kaynaklı hafif destek sağlıyor, ancak altın 4.060 dolar civarına gerilemiş, dolar toparlanıyor ve NFP verisi öncesi temkin hakim. Yakın vadede etki sınırlı ve yön belirsiz; büyük ölçüde NFP sonucuna bağlı olacak.
06.11 06:46 N  GPT  score -0.20 conf 0.40: Altın fiyatının 4.100 doların altına gerilemesi ve NFP öncesinde doların güçlenmesi kısa vadede baskı yaratıyor. Hindistan’daki festival talebi ve İran kaynaklı jeopolitik riskler düşüşü sınırlayabilir; haber akışı karışık olduğu için görünüm zayıf ve güven düşük.
06.11 06:58 N  NEWS (5 new) score +0.02 conf 0.30: Haberler birbiriyle çelişiyor: petrol kaynaklı enflasyon endişeleri ve Orta Doğu barış beklentileri (güvenli liman talebini azaltıyor) altın üzerinde baskı yaratırken, zayıflayan dolar ve teknoloji hisselerindeki sert düşüş bazı destek sağlıyor. Asıl belirleyici olacak ABD tarım dışı istihdam (NFP) verisi henüz açıklanmadığı için yön belirsiz; sinyal zayıf.
06.11 06:58 N  GPT  score -0.18 conf 0.43: Altın, yüksek petrol fiyatlarının enflasyon ve faiz beklentilerini desteklemesiyle geriliyor; yaklaşan ABD istihdam verisi kısa vadede temkinliliği artırıyor. Doların hafif düşmesi destekleyici olsa da Orta Doğu’da barış umutları güvenli liman talebini sınırlayabilir.
06.11 07:10 N  NEWS (5 new) score +0.02 conf 0.30: Haberler karışık: İran savaşı kaynaklı petrol enflasyonu endişesi ve bekleyen ABD tarım dışı istihdam (NFP) verisi altını baskılayabilirken, Trump'ın savaş tonunun yumuşaması jeopolitik risk primini azaltıyor. Fiyat seviyeleri de çelişkili (4.000 üstü ile 4.060-4.100 altı), bu yüzden yön belirsiz ve güven düşük.
06.11 07:10 N  GPT  score -0.15 conf 0.35: İran savaşına ilişkin Trump’ın daha az yıkıcı tonda konuşması güvenli liman talebini bir miktar azaltabilir; altının petrol kaynaklı enflasyon kaygılarıyla gerilediği haberleri de kısa vadede baskı unsuru. Doların zayıflaması bu etkiyi dengelerken, yaklaşan ABD istihdam verisi yön konusunda belirsiz
```

Günlük analiz raporları: `reports/` klasörü. Ayarlar: `config.yaml`.
