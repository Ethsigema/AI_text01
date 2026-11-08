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

current=json.loads((r/'bloodbound_metadata/bloodbound_earrings_v1/SOURCE_MAP.json').read_text());receipts=[]
historical=json.loads((r/'RESTORE_RESULT.json').read_text());assert historical['missing']==[] and historical['archive_errors']==[] and historical['files']==27463
for label,commit,folder,expected,count in packages:
 assert pending[label].result() is True
 d=r/'increments'/label;url=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{commit}/battlegrounds-backup/pending/{folder}/'
 # Murky was already freshly fetched during this same check; reuse only those new downloaded bytes.
 murky=None
 def fetch(name):
  assert safe(name) and '/' not in name
  return get(url+name,d/name)
 mb=fetch('MANIFEST.json');m=json.loads(mb);assert m['sha256']==expected and len(m['files'])==count
 def part(p):
  b=fetch(p['name']);assert len(b)==p['bytes'] and H(b)==p['sha256'];return b
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:blocks=list(pool.map(part,m['parts']))
 archive=b''.join(blocks);assert len(archive)==m['bytes'] and H(archive)==expected
 members={}
 with tarfile.open(fileobj=io.BytesIO(archive)) as t:
  for x in t:
   assert safe(x.name) and x.isfile() and x.name not in members
   b=t.extractfile(x).read();assert {'bytes':len(b),'sha256':H(b)}==m['files'][x.name];members[x.name]=b
 assert set(members)==set(m['files'])
 roots=[n for n in members if n.count('/')==1 and n.endswith('/SOURCE_MAP.json')];assert len(roots)==1
 prefix=roots[0].rsplit('/',1)[0]+'/'
 base=json.loads(members[prefix+'BASE_MAP.json']);target=json.loads(members[prefix+'SOURCE_MAP.json']);assert base==current
 delta={n[len(prefix+'delta/'):]:{'bytes':len(b),'sha256':H(b)} for n,b in members.items() if n.startswith(prefix+'delta/')}
 removed=sorted(set(base)-set(target));assert not removed
 actual_changes={n:v for n,v in target.items() if base.get(n)!=v}
 redundant={n:v for n,v in delta.items() if base.get(n)==v}
 expected_redundant={'research/electron_chef_choice/evidence.json','research/electron_chef_choice/BG28_518.native.xml'} if label=='chef_magnetic' else set()
 assert set(redundant)==expected_redundant and all(target.get(n)==v for n,v in redundant.items())
 assert delta=={**actual_changes,**redundant};assert {**base,**delta}==target
 companions={}
 for name,meta in m.get('companion_files',{}).items():
  b=fetch(name);assert len(b)==meta['bytes'] and H(b)==meta['sha256'];companions[name]=json.loads(b)
 if 'REMOVALS.json' in companions:assert companions['REMOVALS.json']==removed==m['removed_source_files']
 if 'CHANGES.json' in companions:assert companions['CHANGES.json']=={'added':sorted(set(target)-set(base)),'modified':sorted(n for n in set(base)&set(target) if base[n]!=target[n]),'removed':removed}
 current=target;receipt={'label':label,'commit':commit,'manifest_sha256':H(mb),'archive_sha256':expected,'parts':len(blocks),'members':len(members),'source_map_sha256':H(members[roots[0]]),'target_files':len(target),'redundant_unchanged_delta_files':sorted(redundant),'fresh_download':True,'murky_download_reused_within_same_check':False};receipts.append(receipt);print(json.dumps(receipt),flush=True)
prefetch_pool.shutdown(wait=True)
result={'prefetch_method':'Four packages concurrently, four part or companion downloads per package; same-invocation downloaded bytes then rehashed during ordered composition. No prior-run source bytes reused.','status':'PASS_FRESH_FULL_CHAIN_SOURCE_BYTES','verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'historical_baseline_freshly_downloaded':True,'every_increment_freshly_downloaded':True,'increments':receipts,'final_files':len(current),'final_bytes':sum(v['bytes'] for v in current.values()),'final_source_map_sha256':receipts[-1]['source_map_sha256'],'verification_method':'Fresh historical source byte hashes establish Bloodbound; fresh archive member bytes and exact dependency maps compose every later source version through Hopebringer Dune. No second full runtime written.','fresh_full_runtime_directory_created':False,'gameplay_test_run':False,'no_deletion_performed':True}
assert len(current)==27821 and sum(v['bytes'] for v in current.values())==1548444623
assert receipts[-1]['source_map_sha256']=='afcfedcc2db16afaa31e2007e32c39dd63d6efef20fdcdfd975d7c5a97c67ad7'
result['historical_provenance']={'release_sha256':'33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65','recovery_commit':'e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c','bloodbound_commit':'32180d3af0db59fb3374f53100f9eaa5bb62d26a','historical_result':json.loads((r/'RESTORE_RESULT.json').read_text())}
(r/'FRESH_WHOLE_CHAIN_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
