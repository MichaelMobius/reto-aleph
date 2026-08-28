from pathlib import Path
import re,sys,subprocess,csv,collections,wave

ROOT=Path(__file__).resolve().parents[1]
checks=[]

def ck(name,ok):
    checks.append((name,bool(ok)))
    print(('PASS' if ok else 'FAIL')+'  '+name)

def read(path):
    return (ROOT/path).read_text(encoding='utf-8',errors='ignore')

ck('index exists',(ROOT/'index.html').is_file())
stations=[p for p in ROOT.iterdir() if p.is_dir() and re.match(r'^\d\d-',p.name)]
ck('42 visible station folders',len(stations)==42)
ck('secret/codex/comedia gates',all((ROOT/p).is_file() for p in ['secret/index.html','codex/index.html','comedia/index.html']))
ck('DOM + visual engines',all((ROOT/p).is_file() for p in ['assets/dom-runtime.js','assets/aleph3d.js','assets/style.css']))
ck('memory bundle exists',(ROOT/'artifacts/memory-case.bundle').is_file())
ck('spectral audio exists',(ROOT/'artifacts/signal-52.wav').is_file())

if (ROOT/'artifacts/signal-52.wav').is_file():
    try:
        with wave.open(str(ROOT/'artifacts/signal-52.wav'),'rb') as w:
            ck('spectral audio readable',w.getnchannels()==1 and w.getnframes()>1000 and w.getframerate()>=8000)
    except Exception:
        ck('spectral audio readable',False)

if (ROOT/'artifacts/memory-case.bundle').is_file():
    r=subprocess.run(['git','bundle','list-heads',str(ROOT/'artifacts/memory-case.bundle')],capture_output=True,text=True)
    ck('memory bundle readable',r.returncode==0 and bool(r.stdout.strip()))

# HASARD: six blocks must statistically depart from a 36-outcome uniform model.
try:
    rows=list(csv.DictReader((ROOT/'artifacts/coups_de_des.csv').open(encoding='utf-8')))
    chis=[]
    for b in range(1,7):
        rr=[x for x in rows if int(x['bloc'])==b]
        c=collections.Counter((x['de_1'],x['de_2']) for x in rr)
        e=len(rr)/36 if rr else 0
        chis.append(sum((v-e)**2/e for v in c.values()) if e else 0)
    ck('HASARD six statistically strong blocks',len(chis)==6 and all(x>58 for x in chis))
except Exception:
    ck('HASARD six statistically strong blocks',False)

# Visible-station regressions found by manual playthrough.
s03=read('03-dom/index.html')
ck('station 03 has a formal validator','checkShadow' in s03 and "reveal('../04-query/index.html'" in s03)
ck('GitHub Pages robots route', '/reto-aleph/38-history/' in read('robots.txt'))
ck('GitHub Pages security canonical','/reto-aleph/.well-known/security.txt' in read('.well-known/security.txt'))

# Hidden-trace integrity without exposing their reconstructed plaintext.
visible=''.join(read(p.relative_to(ROOT)/'index.html') for p in sorted(stations))
for name,count in {'cache':13,'build':8,'delta':10,'junction':4,'balance':5,'orbit':10,'shift':6,'mesh':8}.items():
    ids=sorted(int(x) for x in re.findall(r'<!--\s*'+re.escape(name)+r'\.(\d+)=',visible))
    ck(f'hidden trace {name} complete',ids==list(range(1,count+1)))

rings=['ring-source','ring-encode','ring-cipher','ring-traces','ring-borges','ring-coords','ring-memory']
axis=''.join(read(f'{r}/index.html') for r in rings)
ck('seven axis fragments',len(re.findall(r'<!--\s*axis\.[^=]+=',axis))==7)
ck('HASARD semantic alias',(ROOT/'secret/hasard/index.html').is_file())

# CODEX is modular: inspect the engine and all seven data modules together.
codex_files=[ROOT/'codex/index.html',ROOT/'codex/mod/app.js']+sorted((ROOT/'codex/mod').glob('data-*.js'))
codex='\n'.join(p.read_text(encoding='utf-8',errors='ignore') for p in codex_files if p.is_file())
ck('CODEX seven data modules',len(list((ROOT/'codex/mod').glob('data-*.js')))==7)
ck('CODEX has 37 challenges',len(re.findall(r'"n":(?:5[4-9]|[6-8]\d|90)\b',codex))==37)
ck('CODEX has no plaintext seal fields','"seal"' not in codex and "seal:'" not in codex)
ck('CODEX uses proof-backed state','proofHash' in codex and 'markMask' in codex and 'readMark' in codex)
ck('UTF-8 challenge preserves case','"case":"preserve"' in codex and "c.case!=='preserve'" in codex)
ck('Semaphore encoding is non-degenerate','(90,315) (45,135) (0,315) (45,315) (0,45) (45,225)' in codex)
ck('BWT sentinel instruction','sin el centinela $' in codex)

# COMEDIA gates and proof-backed intermediate state.
comedia=read('comedia/index.html')
ck('COMEDIA has 8 precursor challenges',len(re.findall(r'"n":9[2-9]\b',comedia))==8)
ck('COMEDIA uses proof-backed state','proofHash' in comedia and 'markMask' in comedia and 'readMark' in comedia)
ck('COMEDIA evidence gate exists','EVIDENCE GATE' in comedia and 'DANTE_HASH' in comedia and 'ALEPH_HASH' in comedia)

style=read('assets/style.css')
a3=read('assets/aleph3d.js')
ck('visual layer is not behind body',bool(re.search(r'#aleph-webgl,#aleph-fallback\{[^}]*z-index:0',style)))
ck('lite mode precedes remote import',a3.find('if(lite') < a3.find("import('https://cdn.jsdelivr.net"))
ck('no static Three.js import',not bool(re.search(r'^\s*import\s+.*https://cdn',a3,re.M)))
ck('station 27 URL does not reveal year',not (ROOT/'27-1945').exists() and (ROOT/'27-first-publication/index.html').is_file())
ck('license present',(ROOT/'LICENSE').is_file())
ck('no production .git',not (ROOT/'.git').exists())

# Explicit local href/src references.
broken=[]
for f in ROOT.rglob('*.html'):
    txt=f.read_text(encoding='utf-8',errors='ignore')
    for u in re.findall(r'(?:href|src)=["\']([^"\']+)["\']',txt):
        if u.startswith(('http:','https:','#','data:','mailto:','javascript:')) or '${' in u:
            continue
        u=u.split('?')[0].split('#')[0]
        if not u:
            continue
        p=(f.parent/u).resolve()
        p=p/'index.html' if p.is_dir() else p
        if not p.exists():
            broken.append((str(f.relative_to(ROOT)),u))
ck('no broken explicit local refs',not broken)

failed=[n for n,o in checks if not o]
if failed:
    print('\nFAILED:',', '.join(failed))
    if broken:
        print('BROKEN REFS:',broken[:20])
    sys.exit(1)
print('\nRELEASE AUDIT: PASS')
