"""Download every pinned dependency without replacing existing files."""
from pathlib import Path
import argparse,concurrent.futures,hashlib,json,urllib.request

def main():
 p=argparse.ArgumentParser();p.add_argument('--destination',type=Path,required=True);a=p.parse_args();assert not a.destination.exists();a.destination.mkdir(parents=True)
 entries=json.loads((Path(__file__).resolve().parent/'DEPENDENCIES.json').read_text())
 def get(r):
  q=a.destination/r['filename'];q.parent.mkdir(parents=True,exist_ok=True);h=hashlib.sha256();size=0
  with urllib.request.urlopen(r['url'],timeout=900) as response,q.open('xb') as out:
   while b:=response.read(1024*1024):out.write(b);h.update(b);size+=len(b)
  assert size==r['bytes'] and h.hexdigest()==r['sha256'],r['filename']
  return {'filename':r['filename'],'bytes':size,'sha256':h.hexdigest(),'status':'PASS_FRESH_DOWNLOAD'}
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(get,entries))
 (a.destination/'DOWNLOAD_RESULT.json').write_text(json.dumps(results,indent=2)+'\n');print('PASS',len(results))
if __name__=='__main__':main()
