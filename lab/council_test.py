"""Quick wiring check for the S3 council: asks each of the three members one tiny question and prints who answers.
No market data, no signals. Run by the 'Kurul testi' workflow."""
import os
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import council  # noqa: E402

cfg = yaml.safe_load(open(os.path.join(council.ROOT, "config.yaml")))["bots"]["survivor"]
print("eksik anahtar:", council.keys_ready() or "yok")
ok = 0
for m in council.MEMBERS:
    try:
        ans, model = council.ask(m, "Answer with ONE JSON object only.",
                                 'Reply exactly with this json: {"action": "wait", "confidence": 0.5, "reason": "test"}', cfg)
        print(f"{council.NAMES[m]}: TAMAM ({model}) -> {council._clean(ans, 24)['action']}")
        ok += 1
    except Exception as e:  # noqa: BLE001
        print(f"{council.NAMES[m]}: HATA {str(e)[:300]}")
print(f"{ok}/3 üye cevap verdi")
