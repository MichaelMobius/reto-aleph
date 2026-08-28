import sys, urllib.request, urllib.parse

if len(sys.argv)!=2:
    raise SystemExit('Uso: python tools/verify_http.py https://tu-dominio.example/')

base=sys.argv[1].rstrip('/')+'/'
paths=[
    'index.html',
    '03-dom/index.html',
    '38-history/index.html',
    '41-metadata/artifact.png',
    'artifacts/memory-case.bundle',
    'artifacts/coups_de_des.csv',
    'artifacts/signal-52.wav',
    'artifacts/qr-81.png',
    'artifacts/sevenseg-82.png',
    'artifacts/pigpen-83.svg',
    'artifacts/xor84-a.png',
    'artifacts/xor84-b.png',
    'artifacts/bitmap-85.txt',
    'artifacts/dtmf-86.wav',
    'final/index.html',
    'secret/index.html',
    'secret/hasard/index.html',
    'assets/dom-runtime.js',
    'assets/aleph3d.js',
    'codex/index.html',
    'codex/mod/app.js',
    'codex/mod/data-1.js',
    'codex/mod/data-7.js',
    'comedia/index.html',
    '.well-known/security.txt',
]

failed=[]
for p in paths:
    url=urllib.parse.urljoin(base,p)
    try:
        with urllib.request.urlopen(url,timeout=10) as r:
            ok=200 <= r.status < 400
            print(('PASS' if ok else 'FAIL'), r.status, url)
            if not ok:
                failed.append(url)
    except Exception as e:
        print('FAIL',url,e)
        failed.append(url)

if failed:
    raise SystemExit(1)
print('HTTP DEPLOY AUDIT: PASS')
