from pathlib import Path,PurePosixPath
import ast,json,hashlib,urllib.request,tarfile,io,datetime,concurrent.futures
r=Path(__file__).resolve().parent
H=lambda b:hashlib.sha256(b).hexdigest()
def safe(n):return n and not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and '\\' not in n
def download(url,p):
 with urllib.request.urlopen(url,timeout=120) as f:b=f.read()
 with p.open('xb') as f:f.write(b)
 return b
packages=json.loads((r/'PINNED_INCREMENT_CHAIN.json').read_text())
# All cache bytes below originate in this invocation's fresh remote prefetch.
assert not (r/'increments').exists(), 'Use a fresh directory; preserve failed attempts'
def prefetch(pkg):
 label,commit,folder,expected,count=pkg
 d=r/'increments'/label;d.mkdir(parents=True)
 url=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{commit}/battlegrounds-backup/pending/{folder}/'
 mb=download(url+'MANIFEST.json',d/'MANIFEST.json');m=json.loads(mb)
 assert m['sha256']==expected and len(m['files'])==count
 def piece(rec):
  name,meta=rec;assert safe(name) and '/' not in name
  b=download(url+name,d/name);assert len(b)==meta['bytes'] and H(b)==meta['sha256']
 records=[(p['name'],p) for p in m['parts']]+list(m.get('companion_files',{}).items())
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as inner:list(inner.map(piece,records))
 return True
prefetch_pool=concurrent.futures.ThreadPoolExecutor(max_workers=4)
pending={pkg[0]:prefetch_pool.submit(prefetch,pkg) for pkg in packages}
def get(url,p):
 # The package future must have completed; no prior-run bytes are accepted.
 return p.read_bytes()


for label,future in pending.items():
 assert future.result() is True
 print(label,flush=True)
prefetch_pool.shutdown(wait=True)
