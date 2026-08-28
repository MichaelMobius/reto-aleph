import sys, urllib.request, urllib.parse
if len(sys.argv)!=2:
    raise SystemExit('Uso: python tools/verify_http.py https://tu-dominio.example/')
base=sys.argv[1].rstrip('/')+'/'
paths=['index.html','03-dom/index.html','38-history/index.html','artifacts/memory-case.bundle','artifacts/signal-52.wav','final/index.html','secret/index.html','assets/dom-runtime.js','codex/index.html','comedia/index.html']
failed=[]
for p in paths:
    url=urllib.parse.urljoin(base,p)
    try:
        with urllib.request.urlopen(url,timeout=10) as r:
            ok=200 <= r.status < 400
            print(('PASS' if ok else 'FAIL'), r.status, url)
            if not ok: failed.append(url)
    except Exception as e:
        print('FAIL',url,e); failed.append(url)
if failed: raise SystemExit(1)
print('HTTP DEPLOY AUDIT: PASS')
