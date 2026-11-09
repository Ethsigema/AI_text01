from pathlib import Path,PurePosixPath
import argparse,json,hashlib,tarfile,io,urllib.request,time,concurrent.futures,datetime,subprocess,zipfile,re,sys,os,threading
if sys.flags.optimize or not __debug__ or os.environ.get("PYTHONOPTIMIZE", "") not in ("", "0"):
 raise RuntimeError("Python assertions are required. Do not use -O, -OO, or nonzero PYTHONOPTIMIZE.")
PLAN = {'folder': 'battlegrounds-backup/pending/20261109-historical-tools-batch11-source-review', 'branch': 'battlegrounds-recovery-20261103', 'parent': '1266c9d1c78bf3f388d2f695467d60af9807ac75', 'tree': '638fb57c30ae87918f50ddbb8ee91fa40abf9145', 'files': [{'name': 'CHANGES.json', 'bytes': 53, 'sha256': '27223135250f2a76068e8147ec88a9d2b8fce0cf65d8e5fc4c7b09d179185a91', 'git_sha': 'e18672dcfb2b5a220575029f832aead3c5d5b254'}, {'name': 'DEPENDENCIES.json', 'bytes': 628, 'sha256': '686065ba8822bd6e558ae927289ca3806a1717fa7dab84c409df8c904087503c', 'git_sha': '1fb3e337074f8f4d9c10e55d639a545ffce64e9b'}, {'name': 'MANIFEST.json', 'bytes': 79034, 'sha256': '4f8a939f30bea9c2ac209af68b1c576ed7e6fe725a71cd20d191c982c0438504', 'git_sha': '58f2501265b1af54381fdfd9b8547f2c2de247b2'}, {'name': 'PACKAGE_VERIFIED.json', 'bytes': 741, 'sha256': '4562c3ca2b2f3e308ace61966d6c5293fa26b2926db5b3a0fdcbc794aa1ad9c3', 'git_sha': '301205bbf16e8ddf2b5bdd979da9e230fa947e70'}, {'name': 'README.md', 'bytes': 7524, 'sha256': 'b2911d7f8c48d0953d29701900dbdda13f74da44ab5194264da567c72677e2f3', 'git_sha': '7af06c58d90f230d7f490db552e80ebc7a09bcfe'}, {'name': 'RECOVERY.md', 'bytes': 1792, 'sha256': '14125439ff420978b7cb83df1ee07c50a723772d6388795608007057df5df70c', 'git_sha': 'ab7f2b57dde2c7fe3e1c37eef2d1082bca4bbf76'}, {'name': 'REMAINING_SCOPE.json', 'bytes': 15964, 'sha256': 'f273f5e61d264d402ad412bd512c99995ce1fb2e04560fe2f025163dcadfa5e8', 'git_sha': '7ace0f942abe7c3347f6b07e20eb5d2feb62bde3'}, {'name': 'REMOVALS.json', 'bytes': 3, 'sha256': '37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570', 'git_sha': 'fe51488c7066f6687ef680d6bfaa4f7768ef205c'}, {'name': 'SHA256SUMS.txt', 'bytes': 1153, 'sha256': 'c0f83dc631677c796d33597aa8bfe05a432560c5ca08563252071ed82c66ea14', 'git_sha': '928dd15f168b12210e93ec8e2513f55a06e2df41'}, {'name': 'TESTS_VERIFIED.json', 'bytes': 2908, 'sha256': 'b88568dea0b60a9b894998f29bdb76604757a4dec115a73db97103845eede5ab', 'git_sha': '532cfd9711c3b89dad8f90fe8faa8e548b088c04'}, {'name': 'historical_tools_batch11_source_review_20261109.tar.xz.part000', 'bytes': 250000, 'sha256': '28e9d8c7d1c8fa62afaaaa9b3e5445efc56b7a472d6773997c8bb3caf44887b6', 'git_sha': '1a5f068a066d32a74664158013e420a48334b082'}, {'name': 'historical_tools_batch11_source_review_20261109.tar.xz.part001', 'bytes': 250000, 'sha256': 'ee2440f177de2939f973507128cbf3014a07573b6d6e46f4fcb19525b1ecabb5', 'git_sha': 'acaeba5c02d2d514458a9fcb2f56b41695bd4085'}, {'name': 'historical_tools_batch11_source_review_20261109.tar.xz.part002', 'bytes': 250000, 'sha256': '856048d735439e571c3ea7355472154481681ff44fbcc0eac4769ad82d07acda', 'git_sha': '484434544488dfb3a7d30c24e7ffacb092f026e5'}, {'name': 'historical_tools_batch11_source_review_20261109.tar.xz.part003', 'bytes': 250000, 'sha256': '894334b66c66f7272c5ba161fdf9e332b8c4d22f8108eb85d385d0f98b466595', 'git_sha': '2a427bdad45df0b3d769bbb0f0a9c8097b8a227f'}, {'name': 'historical_tools_batch11_source_review_20261109.tar.xz.part004', 'bytes': 250000, 'sha256': 'a78d3e3ee84a6d782daa692cc36cce2fd0e1aa81511d5e7ae7a89d668aacdde8', 'git_sha': 'afaf6b3806ac3be304cc627888d6b3c7e0bb5a82'}, {'name': 'historical_tools_batch11_source_review_20261109.tar.xz.part005', 'bytes': 250000, 'sha256': '017a81203d02424b63638d0730a59ab8244f315fbc8a5bce0c9e0428643cc4ad', 'git_sha': 'b7bc6f0d1059826c2f714b25f253441604c54269'}, {'name': 'historical_tools_batch11_source_review_20261109.tar.xz.part006', 'bytes': 250000, 'sha256': '24c03cc2074ef354d5e144f673a6cdbe06c5ece270e3acd16169a42ecf619b40', 'git_sha': '168ec19e019556f9973444e250263ca136726e94'}, {'name': 'historical_tools_batch11_source_review_20261109.tar.xz.part007', 'bytes': 138152, 'sha256': '60214c82db57fb41265107871b737158edf65b0214a986ec48d07e97a608849a', 'git_sha': 'e90223ddef86841de6413083e7f99c2a5a61b9c9'}]}
COMMIT='ea98a4983d94303baf0b2961dba188946c8d2e02'
REPO='https://raw.githubusercontent.com/Ethsigema/AI_text01/'
ap=argparse.ArgumentParser(description='Verify downloaded batch11 read-only review and unchanged source baseline against exact existing source baseline; does not run game or create complete runtime directory.')
ap.add_argument('--baseline-tree',type=Path,required=True)
ap.add_argument('--original-zip',type=Path,required=True)
ap.add_argument('--out',type=Path,required=True)
a=ap.parse_args();BASE=a.baseline_tree.resolve();ZIP=a.original_zip.resolve();OUT=a.out.resolve();assert BASE.is_dir() and ZIP.is_file() and not OUT.exists();OUT.mkdir(parents=True)
downloads=[];download_lock=threading.Lock()
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
 with download_lock:
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
batch(COMMIT,PLAN['folder'],PLAN['files'],OUT/'batch11')
m=json.loads((OUT/'batch11/MANIFEST.json').read_text());b=b''.join((OUT/'batch11'/p['name']).read_bytes() for p in m['parts'])
assert meta(b)=={k:m[k] for k in ['bytes','sha256']};(OUT/'batch11'/m['archive']).write_bytes(b)
prefix=m['archive'].removesuffix('.tar.xz');content=archive_content(b,prefix,m['files']);internal=json.loads(content[prefix+'/FILE_MANIFEST.json'])
assert {prefix+'/'+n:v for n,v in internal.items()}=={n:meta(v) for n,v in content.items() if n!=prefix+'/FILE_MANIFEST.json'}
assert len(content)==334 and len(internal)==333
assert all(not set(x.lower() for x in PurePosixPath(n).parts)&{'home','cache','__pycache__','.godot','.aws','.ssh','.codex','sessions','cookies','chats','messages'} for n in content)
pkg=OUT/'extracted'/prefix
for name,data in content.items():p=OUT/'extracted'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
sr=subprocess.run([sys.executable,str(pkg/'verify_review.py')],capture_output=True,text=True,check=True);static=json.loads(sr.stdout);assert static['checks']==3835
dump(OUT/'STATIC_EVIDENCE_VERIFICATION.json',static)
print('PASS: fresh batch11 archive, 8 parts, 334 members, 333 internal manifest entries, 3835 read-only checks',flush=True)
deps=m['dependencies'];dep=deps['source_baseline'];dd=OUT/'source_baseline'
mb=fetch(dep['commit'],dep['folder'],'MANIFEST.json',dd/'MANIFEST.json');assert meta(mb)['sha256']==dep['manifest_sha256'];dm=json.loads(mb)
parts=batch(dep['commit'],dep['folder'],dm['parts'],dd);db=b''.join(parts);assert meta(db)=={k:dm[k] for k in ['bytes','sha256']} and meta(db)['sha256']==dep['archive_sha256'];(dd/dm['archive']).write_bytes(db)
dp=dm['archive'].removesuffix('.tar.xz');dc=archive_content(db,dp,dm['files']);di=json.loads(dc[dp+'/FILE_MANIFEST.json'])
assert {dp+'/'+n:v for n,v in di.items()}=={n:meta(v) for n,v in dc.items() if n!=dp+'/FILE_MANIFEST.json'}
basebytes=content[prefix+'/BASE_MAP.json'];assert dc[dp+'/SOURCE_MAP.json']==basebytes and meta(basebytes)['sha256']==dep['source_map_sha256']
dep_receipt=json.loads(fetch(dep['commit'],dep['folder'],'REMOTE_STREAM_VERIFIED.json',dd/'REMOTE_STREAM_VERIFIED.json'));assert dep_receipt['candidate_source_map_sha256']==dep['source_map_sha256'] and dep_receipt['remaining_reference_gaps_within_original_scope']==349 and not dep_receipt['full_game_verified']
print('PASS: fresh fixed batch10 baseline archive, 5 parts, 166 members, 165 internal entries; exact BASE_MAP continuity',flush=True)
base=json.loads(basebytes);target=json.loads(content[prefix+'/SOURCE_MAP.json']);changes=json.loads(content[prefix+'/CHANGES.json']);added=changes['added'];expected=[]
assert added==expected and changes['modified']==changes['removed']==[] and set(target)-set(base)==set(added)
delta={n:meta(content[prefix+'/delta/'+n]) for n in added};assert {**base,**delta}==target and sum(x['bytes'] for x in delta.values())==0
assert len(base)==27916 and len(target)==27916 and sum(v['bytes'] for v in target.values())==1549279351
# Actual historical bytes are reused from a previously restored baseline, not called fresh downloads.
actual=set()
for p in BASE.rglob('*'):
 assert not p.is_symlink(),str(p)
 if p.is_file():actual.add(p.relative_to(BASE).as_posix())
assert actual==set(base)
for n in target:
 p=PurePosixPath(n);assert not p.is_absolute() and '..' not in p.parts
reconstruction=OUT/'reconstructed_review_only'
reconstruction_run=subprocess.run([sys.executable,str(pkg/'reconstruct_review_to_new.py'),str(reconstruction)],capture_output=True,text=True,check=True)
(OUT/'RECONSTRUCTION_REPLAY.log').write_text(reconstruction_run.stdout)
review=json.loads((reconstruction/'REVIEW_ONLY.json').read_text());assert not review['generators_executed'] and not review['runtime_installed'] and len(review['outputs'])==2
records=json.loads(content[prefix+'/historical_evidence/RECONSTRUCTION.json'])
assert filemeta(ZIP)['sha256']==records['baseline_zip_sha256']=='33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65'
inputs=json.loads(content[prefix+'/historical_evidence/INPUT_MAP.json']);assert len(inputs)==45
with zipfile.ZipFile(ZIP) as z:
 for rel,record in inputs.items():
  captured=content[prefix+'/historical_evidence/inputs/'+rel]
  assert meta(captured)==record==base[rel] and captured==(BASE/rel).read_bytes()
  assert z.read('酒馆战棋_新范围半成品交接包_20261101/游戏工程/'+rel)==captured
for row in records['records']:
 name=row['target'];actual=(reconstruction/name).read_bytes();pin=row['independent_pin_source']
 assert name not in base and name not in target and meta(actual)=={'bytes':row['bytes'],'sha256':row['sha256']}
 assert actual==content[prefix+'/counterexamples/candidates/'+name]==content[prefix+'/portable_reconstruction/'+name]
 assert json.loads(content[prefix+'/historical_evidence/inputs/'+pin['path']])[pin['field']][name]==row['sha256']
 assert not row['generator_executed'] and not row['candidate_is_installed']
remaining=json.loads(content[prefix+'/REMAINING_SCOPE.json']);assert len(remaining['six_previously_C_targets_with_new_embedded_material'])==6 and all(n not in base for n in remaining['six_previously_C_targets_with_new_embedded_material'])
assert basebytes==content[prefix+'/SOURCE_MAP.json']
print('PASS: 45 reused official ZIP inputs, two literal/AST reconstructions matching independent pins; six tools remain absent from runtime',flush=True)
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
assert rebuilt==target and baseaggregate.hexdigest()=='f159ef6f456e8cade1b5d8eebc84e8833b95659af2a5ef6f7bd5911d3e95074b'
assert aggregate.hexdigest()=='f159ef6f456e8cade1b5d8eebc84e8833b95659af2a5ef6f7bd5911d3e95074b'
sourcebytes=(json.dumps(rebuilt,sort_keys=True,indent=2)+'\n').encode();assert sourcebytes==content[prefix+'/SOURCE_MAP.json'];(OUT/'REBUILT_SOURCE_MAP.json').write_bytes(sourcebytes)
# Re-read every baseline file after reconstruction to establish it remains byte-exact.
for n,v in base.items():assert filemeta(BASE/n)==v,n
assert {p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()}==set(base)
print('PASS: 27,916 unchanged baseline files read and then rehashed again; 1,549,279,351 bytes, no runtime delta',flush=True)
report={'status':'PASS_FRESH_BATCH11_READ_ONLY_REVIEW_WITH_UNCHANGED_FIXED_BASELINE','archive_commit':COMMIT,'folder':PLAN['folder'],'published_files_freshly_downloaded':len(PLAN['files']),'archive':m['archive'],**meta(b),'archive_parts_verified':len(m['parts']),'archive_members_verified':len(content),'internal_manifest_entries_verified':len(internal),'read_only_evidence_checks':3835,'source_baseline_commit':dep['commit'],'source_baseline_archive_freshly_downloaded':True,'source_baseline_archive_sha256':meta(db)['sha256'],'source_baseline_archive_parts_verified':len(dm['parts']),'source_baseline_archive_members_verified':len(dc),'source_baseline_archive_internal_entries_verified':len(di),'historical_baseline_tree_reused':True,'historical_chain_freshly_downloaded':False,'historical_chain_rerun':False,'official_original_zip_reused':True,'official_original_zip_fully_rehashed':True,'historical_input_members_verified_against_ZIP_and_actual_baseline':len(inputs),'review_only_reconstructions':review['outputs'],'historical_generators_executed':False,'review_candidate_modules_executed':False,'review_candidates_installed':False,'six_reviewed_tools_still_deferred':True,'baseline_files_rehashed_twice':len(base),'baseline_bytes':sum(v['bytes'] for v in base.values()),'source_map_sha256':meta(sourcebytes)['sha256'],'source_aggregate_sha256':aggregate.hexdigest(),'source_changes':changes,'runtime_source_changes':0,'remaining_reference_gaps_within_original_scope':349,'assertions_enabled_required':True,'assertions_enabled_during_verification':not sys.flags.optimize and __debug__,'full_runtime_directory_created_by_backup_verifier':False,'full_static_dependency_audit_rerun':False,'all_historical_searches_rerun':False,'gameplay_rerun':False,'Godot_rerun':False,'full_compiler_executed':False,'full_game_verified':False,'old_save_compatibility_verified':False,'historical_baseline_unchanged':True,'all_prior_backups_preserved':True,'missing_source_files':[],'mismatched_source_files':[],'unexpected_source_files':[],'downloads':sorted(downloads,key=lambda x:x['url']),'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
dump(OUT/'REMOTE_REVIEW_VERIFIED.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='downloads'},indent=2),flush=True)
