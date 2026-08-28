from pathlib import Path
import re,sys,subprocess,csv,collections,math,wave
ROOT=Path(__file__).resolve().parents[1];checks=[]
def ck(name,ok):checks.append((name,bool(ok)));print(('PASS' if ok else 'FAIL')+'  '+name)
ck('index exists',(ROOT/'index.html').is_file())
ck('42 visible station folders',len([p for p in ROOT.iterdir() if p.is_dir() and re.match(r'^\d\d-',p.name)])==42)
ck('secret/codex/comedia gates',all((ROOT/p).is_file() for p in ['secret/index.html','codex/index.html','comedia/index.html']))
ck('DOM + visual engines',all((ROOT/p).is_file() for p in ['assets/dom-runtime.js','assets/aleph3d.js','assets/style.css']))
ck('memory bundle exists',(ROOT/'artifacts/memory-case.bundle').is_file())
ck('spectral audio exists',(ROOT/'artifacts/signal-52.wav').is_file())
if (ROOT/'artifacts/signal-52.wav').is_file():
 try:
  with wave.open(str(ROOT/'artifacts/signal-52.wav'),'rb') as w:ck('spectral audio readable',w.getnchannels()==1 and w.getframerate()==16000 and w.getnframes()>1000)
 except Exception:ck('spectral audio readable',False)
if (ROOT/'artifacts/memory-case.bundle').is_file():
 r=subprocess.run(['git','bundle','list-heads',str(ROOT/'artifacts/memory-case.bundle')],capture_output=True,text=True);ck('memory bundle readable',r.returncode==0 and bool(r.stdout.strip()))
# HASARD: each of six blocks must statistically depart from 36-way uniformity.
try:
 rows=list(csv.DictReader((ROOT/'artifacts/coups_de_des.csv').open(encoding='utf-8')));chis=[]
 for b in range(1,7):
  rr=[x for x in rows if int(x['bloc'])==b];c=collections.Counter((x['de_1'],x['de_2']) for x in rr);e=len(rr)/36;chis.append(sum((v-e)**2/e for v in c.values()))
 ck('HASARD six statistically strong blocks',len(rows)==2160 and len(chis)==6 and min(chis)>58)
except Exception:ck('HASARD six statistically strong blocks',False)
# Avoid regressions found by the adversarial audit.
codex=(ROOT/'codex/index.html').read_text(encoding='utf-8');style=(ROOT/'assets/style.css').read_text(encoding='utf-8');a3=(ROOT/'assets/aleph3d.js').read_text(encoding='utf-8')
ck('CODEX has no plaintext seal fields','"seal"' not in codex and "seal:'" not in codex)
ck('CODEX uses proof-backed state','proofHash' in codex and 'markMask' in codex and 'readMark' in codex)
ck('UTF-8 challenge has preserve-case normalization',"case\":\"preserve" in codex and "c.case!=='preserve'" in codex)
ck('visual layer is not behind body',bool(re.search(r'#aleph-webgl,#aleph-fallback\{[^}]*z-index:0',style)))
ck('lite mode precedes remote import',a3.find('if(lite') < a3.find("import('https://cdn.jsdelivr.net"))
ck('no static Three.js import',not bool(re.search(r'^\s*import\s+.*https://cdn',a3,re.M)))
ck('station 27 URL does not reveal year',not (ROOT/'27-1945').exists() and (ROOT/'27-first-publication/index.html').is_file())
ck('license present',(ROOT/'LICENSE').is_file());ck('no production .git',not (ROOT/'.git').exists())
# local refs
broken=[]
for f in ROOT.rglob('*.html'):
 txt=f.read_text(encoding='utf-8',errors='ignore')
 for u in re.findall(r'(?:href|src)=["\']([^"\']+)["\']',txt):
  if u.startswith(('http:','https:','#','data:','mailto:','javascript:')) or '${' in u:continue
  u=u.split('?')[0].split('#')[0]
  if not u:continue
  p=(f.parent/u).resolve();p=p/'index.html' if p.is_dir() else p
  if not p.exists():broken.append((f,u))
ck('no broken explicit local refs',not broken)
failed=[n for n,o in checks if not o]
if failed:print('\nFAILED:',', '.join(failed));sys.exit(1)
print('\nRELEASE AUDIT: PASS')
