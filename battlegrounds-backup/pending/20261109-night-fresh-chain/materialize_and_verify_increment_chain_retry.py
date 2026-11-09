from pathlib import Path,PurePosixPath
import ast,json,hashlib,urllib.request,tarfile,io,datetime,concurrent.futures
r=Path(__file__).resolve().parent
H=lambda b:hashlib.sha256(b).hexdigest()
def safe(n):return n and not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and '\\' not in n
def download(url,p):
 with urllib.request.urlopen(url,timeout=120) as f:b=f.read()
 with p.open('xb') as f:f.write(b)
 return b
packages=json.loads((r/'PINNED_INCREMENT_CHAIN_CURRENT.json').read_text())
# Downloaded into this new invocation directory by prefetch.py and prefetch_candidate.py.
def get(url,p):return p.read_bytes()
current=json.loads((r/'bloodbound_metadata/bloodbound_earrings_v1/SOURCE_MAP.json').read_text());receipts=[]
historical=json.loads((r/'RESTORE_RESULT.json').read_text());assert historical['missing']==[] and historical['archive_errors']==[] and historical['files']==27463
for label,commit,folder,expected,count in packages:
 d=r/'increments'/label;url=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{commit}/battlegrounds-backup/pending/{folder}/'
 # All objects came from this invocation's fresh remote Git clone.
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
 delta_prefix=prefix+('patch/' if label=='catalog_memory' else 'delta/')
 delta={n[len(delta_prefix):]:{'bytes':len(b),'sha256':H(b)} for n,b in members.items() if n.startswith(delta_prefix)}
 removed=sorted(set(base)-set(target));assert not removed
 actual_changes={n:v for n,v in target.items() if base.get(n)!=v}
 redundant={n:v for n,v in delta.items() if base.get(n)==v}
 expected_redundant={'research/electron_chef_choice/evidence.json','research/electron_chef_choice/BG28_518.native.xml'} if label=='chef_magnetic' else set()
 assert set(redundant)==expected_redundant and all(target.get(n)==v for n,v in redundant.items())
 assert delta=={**actual_changes,**redundant};assert {**base,**delta}==target
 companions={}
 for name,meta in m.get('companion_files',{}).items():
  b=fetch(name);assert len(b)==meta['bytes'] and H(b)==meta['sha256'];companions[name]=json.loads(b) if name.endswith('.json') else b.decode('utf-8')
 if 'REMOVALS.json' in companions:assert companions['REMOVALS.json']==removed==m['removed_source_files']
 if 'CHANGES.json' in companions:
  changes=companions['CHANGES.json'];assert set(changes)=={'added','modified','removed'}
  assert all(isinstance(v,list) and len(v)==len(set(v)) for v in changes.values())
  assert {k:sorted(v) for k,v in changes.items()}=={'added':sorted(set(target)-set(base)),'modified':sorted(n for n in set(base)&set(target) if base[n]!=target[n]),'removed':removed}
 runtime=r/'runtime_final_current'
 for n,b in members.items():
  if not n.startswith(delta_prefix):continue
  rel=n[len(delta_prefix):];assert safe(rel)
  dest=runtime/rel;assert not dest.is_symlink()
  dest.parent.mkdir(parents=True,exist_ok=True)
  with dest.open('wb') as output:output.write(b)
 current=target;receipt={'label':label,'commit':commit,'manifest_sha256':H(mb),'archive_sha256':expected,'parts':len(blocks),'members':len(members),'source_map_sha256':H(members[roots[0]]),'target_files':len(target),'redundant_unchanged_delta_files':sorted(redundant),'fresh_download':True,'murky_download_reused_within_same_check':False};receipts.append(receipt);print(json.dumps(receipt),flush=True)
result={'prefetch_method':'All 154 fixed-commit package inputs were materialized from a fresh remote Git clone made during this invocation, then each part and archive member was rehashed during ordered composition. No prior-run source bytes or object database reused.','status':'PASS_FRESH_FULL_CHAIN_SOURCE_BYTES','verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'historical_baseline_freshly_downloaded':True,'every_increment_freshly_downloaded':True,'increments':receipts,'final_files':len(current),'final_bytes':sum(v['bytes'] for v in current.values()),'final_source_map_sha256':receipts[-1]['source_map_sha256'],'verification_method':'Fresh historical source bytes establish Bloodbound; exact delta bytes and dependency maps compose all 154 runtime layers through Devourer into a new isolated tree, then every resulting file is independently rehashed.','fresh_full_runtime_directory_created':True,'gameplay_test_run':False,'no_deletion_performed':True}
assert len(current)==27912 and sum(v["bytes"] for v in current.values())==1549132284
assert receipts[-1]['source_map_sha256']=='9baabc104b5f2f93087dfec0e385d6cb9fceffbf3b1d4441ec91da463a727260'
result['historical_provenance']={'release_sha256':'33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65','recovery_commit':'e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c','bloodbound_commit':'32180d3af0db59fb3374f53100f9eaa5bb62d26a','historical_result':json.loads((r/'RESTORE_RESULT.json').read_text())}
import os
actual={};aggregate=hashlib.sha256()
for name in sorted(current):
 path=runtime/name;assert path.is_file() and not path.is_symlink(),name
 digest=hashlib.sha256();count=0
 aggregate.update(name.encode()+b'\0'+str(current[name]['bytes']).encode()+b'\0')
 with path.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):
   digest.update(b);aggregate.update(b);count+=len(b)
 actual[name]={'bytes':count,'sha256':digest.hexdigest()}
 assert actual[name]==current[name],name
seen=[]
for folder,dirs,files in os.walk(runtime):
 for d in dirs:assert not (Path(folder)/d).is_symlink()
 for name in files:seen.append((Path(folder)/name).relative_to(runtime).as_posix())
assert set(seen)==set(current) and len(seen)==len(current)
mapbytes=(json.dumps(actual,indent=2,sort_keys=True)+'\n').encode()
assert H(mapbytes)=='9baabc104b5f2f93087dfec0e385d6cb9fceffbf3b1d4441ec91da463a727260'
(r/'REBUILT_SOURCE_MAP_CURRENT.json').write_bytes(mapbytes)
result.update({'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actual_runtime_files_rehashed':len(actual),'actual_runtime_bytes_rehashed':sum(v['bytes'] for v in actual.values()),'actual_map_sha256':H(mapbytes),'actual_aggregate_stream_sha256':aggregate.hexdigest(),'missing_files':[],'mismatched_files':[],'extra_files':[],'save_compatibility_test_run':False,'complete_game_recovery_proven':False,'source_scope':'Matches pinned candidate source map only; 353 original-scope referenced tools remain unresolved. The original pre-interruption local working tree remains unavailable.'})
assert aggregate.hexdigest()=='930f77dd965da27e5d16f2e29f5b495b99c95b526cf52a1279bad7eb9f42ec0b'
print('ACTUAL_FINAL_REHASH_PASS',len(actual),sum(v['bytes'] for v in actual.values()),aggregate.hexdigest(),flush=True)
(r/'FRESH_WHOLE_CHAIN_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
