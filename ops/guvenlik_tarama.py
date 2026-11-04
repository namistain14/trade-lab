"""Repoya anahtar ya da kişisel veri girmesini yakalar.

Kullanım:
  python3 ops/guvenlik_tarama.py diff <eski_sha> <yeni_sha>   # sadece eklenen satırlar (workflow)
  python3 ops/guvenlik_tarama.py tum                          # tüm repo (temel ölçüm)

Bulduğu değeri ASLA yazdırmaz: sadece dosya:satır ve tür. Çıkış kodu 1 = bulgu var.
Yayınlanan site içeriği (web/public, web/static) telefon/e-posta için taranmaz; anahtar için taranır.
"""
import re, subprocess, sys, pathlib, json, os

ANAHTAR = {
    'özel anahtar (PEM)': r'-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY',
    'Anthropic anahtarı': r'sk-ant-[A-Za-z0-9_-]{20,}',
    'OpenAI anahtarı': r'\bsk-(?!ant-)(?:proj-|svcacct-|admin-)?[A-Za-z0-9_-]{32,}',
    'GitHub token': r'\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}',
    'Telegram bot token': r'\b\d{8,10}:AA[A-Za-z0-9_-]{30,}',
    'Meta/Instagram token': r'\b(?:EAA[A-Za-z0-9]{60,}|IGAA[A-Za-z0-9_-]{60,})',
    'Google API anahtarı': r'\bAIza[0-9A-Za-z_-]{35}',
    'Google OAuth token': r'\bya29\.[0-9A-Za-z_-]{30,}|\b1//0[0-9A-Za-z_-]{30,}',
    'Google istemci sırrı': r'\bGOCSPX-[A-Za-z0-9_-]{20,}',
    'AWS anahtarı': r'\bAKIA[0-9A-Z]{16}',
    'Slack token': r'\bxox[abposr]-[A-Za-z0-9-]{10,}',
    'ElevenLabs anahtarı': r'\bsk_[a-f0-9]{48}\b',
    'Cloudflare token (atama)': r'(?i)(?:cloudflare|cf)_?api_?token\s*[:=]\s*["\']?[A-Za-z0-9_-]{40}',
    'şifre ataması': r'(?i)\b(?:password|passwd|parola|sifre|şifre|secret)\s*[:=]\s*["\'][^"\'\s$\{]{8,}["\']',
}
TELEFON = r'(?<![\d+])(?:\+?90[\s-]?)?0?5\d{2}[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}(?!\d)'
IBAN = r'\bTR\d{2}(?:\s?\d{4}){5}\s?\d{2}\b'
TCKN = r'(?<!\d)[1-9]\d{10}(?!\d)'
YAYIN = ('state/', 'reports/', 'docs/')   # trade-lab: fiyat/işlem verisi (uzun ondalıklar telefon sanılıyor) ve herkese açık sayfalar; anahtar taraması yine yapılır   # site kaynağı ve herkese açık işletme verisi (şube telefonları vb.)
TEST = re.compile(r'(^|/)(test|tests|e2e|__tests__)/|\.test\.[jt]sx?$|(^|/)(e2e|shots|dev)\.(c?js|ts|py)$|/seed\.mjs$')   # sahte test verisi
TCKN_BAGLAM = re.compile(r'(?i)t\.?c\.?|tckn|kimlik|vatanda|identity|national')
ATLA_UZANTI = {'.wasm', '.step', '.stp', '.stl', '.glb', '.svg', '.png', '.jpg', '.jpeg', '.gif', '.webp', '.mp4', '.mp3', '.m4a', '.wav', '.pdf', '.xlsx', '.zip', '.ttf', '.otf', '.woff', '.woff2', '.ico', '.lock'}
ATLA_DOSYA = ('ops/guvenlik_tarama.py', 'package-lock.json', 'bun.lock')
IZIN = '# guvenlik:izin'   # satır sonuna eklenirse bilinçli istisna (ör. test verisi)

def tckn_gecerli(s):
    d = [int(c) for c in s]
    return d[0] != 0 and (sum(d[0:9:2]) * 7 - sum(d[1:8:2])) % 10 == d[9] and sum(d[:10]) % 10 == d[10]

def iban_gecerli(s):
    s = s.replace(' ', ''); r = s[4:] + s[:4]
    return int(''.join(str(int(c, 36)) for c in r)) % 97 == 1

def tara_satir(yol, satir):
    if IZIN in satir: return []
    test = bool(TEST.search(yol))
    out = [t for t, rx in ANAHTAR.items() if re.search(rx, satir) and not (test and t == 'şifre ataması')]
    if not yol.startswith(YAYIN) and not test:
        if re.search(TELEFON, satir) and not re.search(r'444\s?4\s?982', satir): out.append('cep telefonu')
        if any(iban_gecerli(m.group()) for m in re.finditer(IBAN, satir)): out.append('IBAN')
        if TCKN_BAGLAM.search(satir) and any(tckn_gecerli(m.group()) for m in re.finditer(TCKN, satir)): out.append('TC kimlik no')
    return out

def atla(yol):
    return pathlib.Path(yol).suffix.lower() in ATLA_UZANTI or yol.endswith(ATLA_DOSYA) or '/node_modules/' in yol

def diff_tara(eski, yeni):
    if not eski or set(eski) == {'0'}:
        eski = subprocess.run(['git', 'rev-parse', f'{yeni}~1'], capture_output=True, text=True).stdout.strip() or '4b825dc642cb6eb9a060e54bf8d69288fbee4904'
    d = subprocess.run(['git', 'diff', '--unified=0', '--no-color', eski, yeni], capture_output=True, text=True, errors='ignore').stdout
    yol, no, bul = None, 0, []
    for l in d.splitlines():
        if l.startswith('+++ '): yol = l[6:] if l.startswith('+++ b/') else None; continue
        m = re.match(r'@@ -\d+(?:,\d+)? \+(\d+)', l)
        if m: no = int(m.group(1)); continue
        if yol and l.startswith('+') and not atla(yol):
            for t in tara_satir(yol, l[1:]): bul.append((yol, no, t))
            no += 1
    return bul

def tum_tara():
    dosyalar = subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout.splitlines()
    bul = []
    for yol in dosyalar:
        if atla(yol): continue
        try: metin = pathlib.Path(yol).read_text(errors='ignore')
        except Exception: continue
        for i, l in enumerate(metin.splitlines(), 1):
            for t in tara_satir(yol, l): bul.append((yol, i, t))
    return bul

if __name__ == '__main__':
    bul = diff_tara(sys.argv[2], sys.argv[3]) if sys.argv[1] == 'diff' else tum_tara()
    for yol, no, t in bul:
        print(f'::error file={yol},line={no}::{t} bulundu (değer gizlendi)')
    ozet = {}
    for _, _, t in bul: ozet[t] = ozet.get(t, 0) + 1
    print('GUVENLIK_OZET ' + json.dumps({'bulgu': len(bul), 'tur': ozet, 'dosya': sorted({b[0] for b in bul})[:40]}, ensure_ascii=False))
    sys.exit(1 if bul else 0)
