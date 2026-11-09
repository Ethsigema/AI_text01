from pathlib import Path,PurePosixPath
import argparse,json,hashlib,tarfile,io,urllib.request,time,concurrent.futures,datetime,subprocess,zipfile,re
PLAN = {'folder': 'battlegrounds-backup/pending/20261109-historical-tools-batch9-trip-candidate', 'branch': 'battlegrounds-recovery-20261103', 'parent': '24034fe9f1c068880f0792b88a434845d3df78d6', 'tree': '10829997bee6b7767fa909447fbaa0c875bcebff', 'files': [{'name': 'CHANGES.json', 'bytes': 94, 'sha256': '958fc1b1c84af858b62c1e6eef73ae3952f71e0d8c9fab075dd954bb4ee1b126', 'git_sha': '9253b2064c0eb78151ffda8df3459d5ff420a8bc'}, {'name': 'DEPENDENCIES.json', 'bytes': 625, 'sha256': '064971e304a094acb3b193c90ce5e03a1f8628f0c0f03fea8d031af9075e4bd7', 'git_sha': '20b70922c43dd0c50109133a6186134d12a758cd'}, {'name': 'MANIFEST.json', 'bytes': 40499, 'sha256': '374c0f1a24efabdb1f62dac9d1dc3391eb292b08e803f2d983eab70b1da1f663', 'git_sha': '24655b770ca7f534be1942f3b56258f323936f9d'}, {'name': 'PACKAGE_VERIFIED.json', 'bytes': 1173, 'sha256': 'e30972c40972f369314e321ea5857013fb83f8ef774f88265e2d4febf5af939a', 'git_sha': '73f9387209629a07543f63c5263bec6bed331a2e'}, {'name': 'README.md', 'bytes': 6141, 'sha256': 'ee3199920ce885932d160fc1603cd6eb2ffe6e2b5981ee30131d0eb08ea4ce9c', 'git_sha': 'd11235f14beb7e386a03cefcbed7e8a80d36e7ef'}, {'name': 'RECONSTRUCTION_PROVENANCE.json', 'bytes': 1217, 'sha256': '3a32430c10a22c0df1818cb04311e25c07a95b37312d43251221a62bde454155', 'git_sha': '178b2dd206279ba2e41e1f0e32187df758916d81'}, {'name': 'RECOVERY.md', 'bytes': 1841, 'sha256': '6c5ec769a27162cacc08094fbb1a95bfd7dd2529bbc10cb2bb4c675c5f2d561f', 'git_sha': '816d1069b2126196a34b58ad5ed69c82d8a3baca'}, {'name': 'REMAINING_SCOPE.json', 'bytes': 16588, 'sha256': '392cc8c193225c3877bf75e099daf42b00663cf4a0defa6382b614df609f316b', 'git_sha': 'ccc4e351cda3b535742e4021b3b7bcf49678d919'}, {'name': 'REMOVALS.json', 'bytes': 3, 'sha256': '37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570', 'git_sha': 'fe51488c7066f6687ef680d6bfaa4f7768ef205c'}, {'name': 'SHA256SUMS.txt', 'bytes': 766, 'sha256': '109be6dfc4486aa3138e2106e52f84b8da233e24983d6e69390b24e4f7f3250c', 'git_sha': '0624403bdd9b0b2528a51034cb9608d4f41f9cc2'}, {'name': 'historical_tools_batch9_trip_candidate_20261109.tar.xz.part000', 'bytes': 250000, 'sha256': '84b95a77d1845770398512ddbb850847798f96f67a1af9af5c6a5d0b20cf5360', 'git_sha': '6e05a3235e82c51866d6adfc0ca5c089287a4834'}, {'name': 'historical_tools_batch9_trip_candidate_20261109.tar.xz.part001', 'bytes': 250000, 'sha256': '79c6be5c393bc18076726af22dd89b8943ddff269d73490532d1023b8b474672', 'git_sha': '9b74fefd7836011f64b1e906ddd9465546cbdecb'}, {'name': 'historical_tools_batch9_trip_candidate_20261109.tar.xz.part002', 'bytes': 250000, 'sha256': '8091aa17b0a054667e86d9dd4835093b2cbb31a4ec07c3cead996b166fc69b3d', 'git_sha': '2597615506064dd0b1edf4f92bdc81030d371eb6'}, {'name': 'historical_tools_batch9_trip_candidate_20261109.tar.xz.part003', 'bytes': 250000, 'sha256': '4756c2bc34e63820bf2f63610de62a371f212101b74a1bed32271ae4c10816de', 'git_sha': '33865d704e09bb7ee610a7f6e5062275ca75b612'}, {'name': 'historical_tools_batch9_trip_candidate_20261109.tar.xz.part004', 'bytes': 117320, 'sha256': '4d248d1ea99cfb181572e3fd48aa448846a97e8f8059825aa87d55ea17a67a2e', 'git_sha': '9cfe5c1743ea80faf4b3efca4903f3ee7611dee9'}]}
COMMIT='bfd73cc2854bc3fda3e4ad461c155ff1fff59b85'
REPO='https://raw.githubusercontent.com/Ethsigema/AI_text01/'
ap=argparse.ArgumentParser(description='Verify downloaded batch9 candidate against exact existing source baseline; does not run game or create complete runtime directory.')
ap.add_argument('--baseline-tree',type=Path,required=True)
ap.add_argument('--original-zip',type=Path,required=True)
ap.add_argument('--out',type=Path,required=True)
a=ap.parse_args();BASE=a.baseline_tree.resolve();ZIP=a.original_zip.resolve();OUT=a.out.resolve();assert BASE.is_dir() and ZIP.is_file() and not OUT.exists();OUT.mkdir(parents=True)
downloads=[]
def meta(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def filemeta(p):
 with p.open('rb') as f:h=hashlib.file_digest(f,'sha256').hexdigest()
 return {'bytes':p.stat().st_size,'sha256':h}
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def fetch(commit,folder,name,dest,expected=None):
 url=REPO+commit+'/'+folder+'/'+name
 for attempt in range(3):
  try:
   with urllib.request.urlopen(url,timeout=60) as response:b=response.read()
   break
  except Exception:
   if attempt==2:raise
   time.sleep(2*(attempt+1))
 v=meta(b)
 if expected:
  assert v=={k:expected[k] for k in ['bytes','sha256']},name
  if 'git_sha' in expected:assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==expected['git_sha']
 dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
 downloads.append({'url':url,'name':name,**v,'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
 dump(OUT/'DOWNLOADS.json',sorted(downloads,key=lambda x:x['url']))
 return b
def batch(commit,folder,files,dest):
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:return list(e.map(lambda f:fetch(commit,folder,f['name'],dest/f['name'],f),files))
def archive_content(b,prefix,expected):
 actual={};content={}
 with tarfile.open(fileobj=io.BytesIO(b),mode='r:xz') as tf:
  for t in tf:
   assert t.isfile() and t.name not in actual
   p=PurePosixPath(t.name);assert not p.is_absolute() and '..' not in p.parts and p.parts[0]==prefix
   data=tf.extractfile(t).read();actual[t.name]=meta(data);content[t.name]=data
 assert actual==expected,{'missing':sorted(set(expected)-set(actual)),'extra':sorted(set(actual)-set(expected))}
 return content
batch(COMMIT,PLAN['folder'],PLAN['files'],OUT/'batch9')
m=json.loads((OUT/'batch9/MANIFEST.json').read_text());b=b''.join((OUT/'batch9'/p['name']).read_bytes() for p in m['parts'])
assert meta(b)=={k:m[k] for k in ['bytes','sha256']};(OUT/'batch9'/m['archive']).write_bytes(b)
prefix=m['archive'].removesuffix('.tar.xz');content=archive_content(b,prefix,m['files']);internal=json.loads(content[prefix+'/FILE_MANIFEST.json'])
assert {prefix+'/'+n:v for n,v in internal.items()}=={n:meta(v) for n,v in content.items() if n!=prefix+'/FILE_MANIFEST.json'}
assert len(content)==178 and len(internal)==177
assert all(not set(x.lower() for x in PurePosixPath(n).parts)&{'home','cache','__pycache__','.godot','.aws','.ssh','.codex','sessions','cookies','chats','messages'} for n in content)
pkg=OUT/'extracted'/prefix
for name,data in content.items():p=OUT/'extracted'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
sr=subprocess.run(['python',str(pkg/'verify_candidate.py')],capture_output=True,text=True,check=True);static=json.loads(sr.stdout);assert static['checks']==126
dump(OUT/'STATIC_EVIDENCE_VERIFICATION.json',static)
print('PASS: fresh batch9 archive, 5 parts, 178 members, 177 internal manifest entries, 126 read-only checks',flush=True)
deps=m['dependencies'];dep=deps['source_baseline'];dd=OUT/'source_baseline'
mb=fetch(dep['commit'],dep['folder'],'MANIFEST.json',dd/'MANIFEST.json');assert meta(mb)['sha256']==dep['manifest_sha256'];dm=json.loads(mb)
parts=batch(dep['commit'],dep['folder'],dm['parts'],dd);db=b''.join(parts);assert meta(db)=={k:dm[k] for k in ['bytes','sha256']} and meta(db)['sha256']==dep['archive_sha256'];(dd/dm['archive']).write_bytes(db)
dp=dm['archive'].removesuffix('.tar.xz');dc=archive_content(db,dp,dm['files']);di=json.loads(dc[dp+'/FILE_MANIFEST.json'])
assert {dp+'/'+n:v for n,v in di.items()}=={n:meta(v) for n,v in dc.items() if n!=dp+'/FILE_MANIFEST.json'}
basebytes=content[prefix+'/BASE_MAP.json'];assert dc[dp+'/SOURCE_MAP.json']==basebytes and meta(basebytes)['sha256']==dep['source_map_sha256']
dep_receipt=json.loads(fetch(dep['commit'],dep['folder'],'REMOTE_STREAM_VERIFIED.json',dd/'REMOTE_STREAM_VERIFIED.json'));assert dep_receipt['candidate_source_map_sha256']==dep['source_map_sha256'] and dep_receipt['remaining_reference_gaps_within_original_scope']==351 and not dep_receipt['full_game_verified']
print('PASS: fresh fixed batch8 baseline archive, 6 parts, 234 members, 233 internal entries; exact BASE_MAP continuity',flush=True)
base=json.loads(basebytes);target=json.loads(content[prefix+'/SOURCE_MAP.json']);changes=json.loads(content[prefix+'/CHANGES.json']);added=changes['added'];expected=['tools/trip_vouchers_patterns.py']
assert added==expected and changes['modified']==changes['removed']==[] and set(target)-set(base)==set(added)
delta={n:meta(content[prefix+'/delta/'+n]) for n in added};assert {**base,**delta}==target and sum(x['bytes'] for x in delta.values())==58891
assert len(base)==27914 and len(target)==27915 and sum(v['bytes'] for v in target.values())==1549275367
# Actual historical bytes are reused from a previously restored baseline, not called fresh downloads.
actual=set()
for p in BASE.rglob('*'):
 assert not p.is_symlink(),str(p)
 if p.is_file():actual.add(p.relative_to(BASE).as_posix())
assert actual==set(base)
for n in target:
 p=PurePosixPath(n);assert not p.is_absolute() and '..' not in p.parts
reconstruction=OUT/'reconstructed_delta'
rr=subprocess.run(['python',str(pkg/'reconstruct_to_new.py'),str(reconstruction)],capture_output=True,text=True,check=True);(OUT/'PATCH_REPLAY.log').write_text(rr.stdout)
provenance=json.loads(content[prefix+'/RECONSTRUCTION_PROVENANCE.json']);assert filemeta(ZIP)['sha256']==provenance['baseline_ZIP_sha256']=='33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65'
patch_results=[]
with zipfile.ZipFile(ZIP) as z:
 for row in provenance['records']:
  if row['target'] not in added:continue
  original=content[prefix+'/inputs/'+row['original_path']];patch=content[prefix+'/inputs/'+row['patch_path']]
  assert (BASE/row['original_path']).read_bytes()==original and (BASE/row['patch_path']).read_bytes()==patch
  assert z.read('酒馆战棋_新范围半成品交接包_20261101/游戏工程/'+row['original_path'])==original
  assert z.read('酒馆战棋_新范围半成品交接包_20261101/游戏工程/'+row['patch_path'])==patch
  sections=[s for s in re.split(r'(?m)(?=^--- )',patch.decode()) if s.startswith('--- a/'+row['target']+'\n')];assert len(sections)==1
  work=OUT/'gnu_patch'/Path(row['target']).stem;src=work/row['target'];src.parent.mkdir(parents=True);src.write_bytes(original);patchfile=work/'SELECTED.patch';patchfile.write_text(sections[0])
  p=subprocess.run(['patch','--batch','--fuzz=0','--forward','-p1','-i',str(patchfile)],cwd=work,capture_output=True,text=True,check=True)
  assert 'offset' not in p.stdout.lower() and 'fuzz' not in p.stdout.lower()
  assert src.read_bytes()==(reconstruction/row['target']).read_bytes()==content[prefix+'/delta/'+row['target']]
  reverse=subprocess.run(['patch','--batch','--fuzz=0','--reverse','-p1','-i',str(patchfile)],cwd=work,capture_output=True,text=True,check=True)
  assert 'offset' not in reverse.stdout.lower() and 'fuzz' not in reverse.stdout.lower() and src.read_bytes()==original
  forward=subprocess.run(['patch','--batch','--fuzz=0','--forward','-p1','-i',str(patchfile)],cwd=work,capture_output=True,text=True,check=True)
  assert 'offset' not in forward.stdout.lower() and 'fuzz' not in forward.stdout.lower() and src.read_bytes()==content[prefix+'/delta/'+row['target']]
  assert not row['independent_historical_postimage_found'] and not row['latest_installed_version_proven']
  patch_results.append({'target':row['target'],'bytes':row['reconstructed_bytes'],'sha256':row['reconstructed_sha256'],'exact_patch_replay_equal':True,'GNU_zero_fuzz_no_offset_equal':True,'GNU_reverse_and_forward_roundtrip_equal':True,'reused_official_ZIP_original_and_patch_members_equal':True})
assert len(patch_results)==1
print('PASS: one exact patch reconstructions, independent GNU zero-fuzz check, reused official ZIP rehashed and selected members matched',flush=True)
aggregate=hashlib.sha256();baseaggregate=hashlib.sha256();rebuilt={}
for n in sorted(target):
 p=reconstruction/n if n in delta else BASE/n
 header=n.encode()+b'\0'+str(target[n]['bytes']).encode()+b'\0';aggregate.update(header)
 if n in base:baseaggregate.update(header)
 h=hashlib.sha256();size=0
 with p.open('rb') as f:
  while block:=f.read(1024*1024):
   h.update(block);aggregate.update(block);size+=len(block)
   if n in base:baseaggregate.update(block)
 rebuilt[n]={'bytes':size,'sha256':h.hexdigest()};assert rebuilt[n]==target[n],n
assert rebuilt==target and baseaggregate.hexdigest()=='2808118a744b4b62973ddd639dc39d4313a6d653e2ced479909a7a125e067f55'
assert aggregate.hexdigest()=='ed0a7b545e0fc5339619cd7b735f426962e7a47874e9908e75b9ea9fb9e6c519'
sourcebytes=(json.dumps(rebuilt,sort_keys=True,indent=2)+'\n').encode();assert sourcebytes==content[prefix+'/SOURCE_MAP.json'];(OUT/'REBUILT_SOURCE_MAP.json').write_bytes(sourcebytes)
# Re-read every baseline file after reconstruction to establish it remains byte-exact.
for n,v in base.items():assert filemeta(BASE/n)==v,n
assert {p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()}==set(base)
print('PASS: 27,915 actual files streamed, 1,549,275,367 bytes; baseline 27,914 files rehashed again unchanged',flush=True)
report={'status':'PASS_FRESH_BATCH9_PACKAGE_WITH_REUSED_EXACT_BASELINE_ONE_PATCH_STREAM_RECONSTRUCTION','archive_commit':COMMIT,'folder':PLAN['folder'],'published_files_freshly_downloaded':len(PLAN['files']),'archive':m['archive'],**meta(b),'archive_parts_verified':len(m['parts']),'archive_members_verified':len(content),'internal_manifest_entries_verified':len(internal),'read_only_evidence_checks':126,'source_baseline_commit':dep['commit'],'source_baseline_archive_freshly_downloaded':True,'source_baseline_archive_sha256':meta(db)['sha256'],'source_baseline_archive_members_verified':len(dc),'source_baseline_archive_internal_entries_verified':len(di),'source_baseline_archive_parts_verified':len(dm['parts']),'historical_baseline_tree_reused':True,'historical_154_layer_chain_freshly_downloaded':False,'historical_154_layer_chain_rerun':False,'official_original_zip_reused':True,'official_original_zip_fully_rehashed':True,'baseline_source_files_rehashed_before_and_after':len(base),'candidate_files_streamed':len(target),'candidate_bytes_streamed':sum(v['bytes'] for v in target.values()),'candidate_source_map_sha256':meta(sourcebytes)['sha256'],'candidate_aggregate_sha256':aggregate.hexdigest(),'aggregate_format':'Sorted UTF-8 path, NUL, ASCII byte count, NUL, actual file bytes, repeated for all candidate files.','patch_reconstructions':patch_results,'source_changes':changes,'remaining_reference_gaps_within_original_scope':350,'independent_historical_postimages_found':False,'latest_installed_versions_proven':False,'full_candidate_runtime_directory_created_by_backup_verifier':False,'complete_candidate_reconstructed_as_actual_byte_stream':True,'candidate_producer_had_created_full_tree_evidence_checked_not_repeated':True,'gameplay_rerun':False,'Godot_rerun':False,'candidate_compiler_modules_executed_by_backup_verifier':False,'full_game_verified':False,'old_save_compatibility_verified':False,'historical_baseline_unchanged':True,'all_prior_backups_preserved':True,'missing_source_files':[],'mismatched_source_files':[],'unexpected_source_files':[],'downloads':sorted(downloads,key=lambda x:x['url']),'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
dump(OUT/'REMOTE_STREAM_VERIFIED.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='downloads'},indent=2),flush=True)
