from pathlib import Path,PurePosixPath
import argparse,json,hashlib,tarfile,io,urllib.request,time,concurrent.futures,datetime,subprocess,zipfile,re,sys,os,threading
if sys.flags.optimize or not __debug__ or os.environ.get("PYTHONOPTIMIZE", "") not in ("", "0"):
 raise RuntimeError("Python assertions are required. Do not use -O, -OO, or nonzero PYTHONOPTIMIZE.")
PLAN = {'folder': 'battlegrounds-backup/pending/20261109-historical-tools-batch10-overlay-candidate', 'branch': 'battlegrounds-recovery-20261103', 'parent': '3dd4db504ab9eba4c28088c1a72a6bbc3ed0e136', 'tree': '6272159b06d29c6e154ed0f24a02eba7de1b8ab3', 'files': [{'name': 'CHAIN_VERIFIED.json', 'bytes': 635, 'sha256': '241712464f1c770e163cf05d869dc657f45c9017d5596b460baf6c95b70b2070', 'git_sha': '36390a4f005877edb1c86fd72dded7144c9112bc'}, {'name': 'CHANGES.json', 'bytes': 94, 'sha256': '2ea95f620f840911c04aa3551a6d31ace011dc8052357cb3bf521bbedc61c08c', 'git_sha': '1bcd15d804cd8b6cdc3ac431fbb33e5c670f5a86'}, {'name': 'DEPENDENCIES.json', 'bytes': 624, 'sha256': '58a071858870c4b7f856445b03f49a181515b93ec2bfeafc3d122d6f6594e6af', 'git_sha': 'b93299ac8f6e81cab187b445b246f2929e8f79ca'}, {'name': 'MANIFEST.json', 'bytes': 38505, 'sha256': 'f90b3fbb3020fc3a63c81c227d26872a21a6b419338dcc51dfa45451156fdb9d', 'git_sha': '6d035c90081ff37c3fd83357cdf6f7f13a80804c'}, {'name': 'ORIGIN_VERIFIED.json', 'bytes': 1405, 'sha256': '7b69de6ff6c58811600f26dc643c539872f04582b9ec4323fae8dc40df00f3dd', 'git_sha': 'c4adffdae41ea3cdcf018ba361fcff2e96f15d04'}, {'name': 'PACKAGE_VERIFIED.json', 'bytes': 724, 'sha256': '21aaf786c7210697e67fd86ea82cbd7f04237a045104eb8cb75a5fb013d32d60', 'git_sha': 'bdeb844462f2a6c15ad07f2f408ff009a725ec32'}, {'name': 'README.md', 'bytes': 7671, 'sha256': '08c39d56818dbdc7247ae7b0fb4a479ab00bfbdc290f526433ee4efd3ad6e937', 'git_sha': 'd1de1d9c498dd1ad730214c703f7897fde1576bb'}, {'name': 'RECOVERY.md', 'bytes': 1911, 'sha256': 'e23e3ee164e2bdbc2059a57c3ab6cab636e3d5b395654e25291aba70f49fc316', 'git_sha': '608c5af62db4281cdf84802ad62c4679b8327d54'}, {'name': 'REMAINING_SCOPE.json', 'bytes': 33715, 'sha256': '746e754b799d2de814d1b6b0416cd869dfb34668c386c97dfd54f9806f175ab4', 'git_sha': 'b02db5772a4fb26daf695483acdce29b7d0a48b8'}, {'name': 'REMOVALS.json', 'bytes': 3, 'sha256': '37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570', 'git_sha': 'fe51488c7066f6687ef680d6bfaa4f7768ef205c'}, {'name': 'SHA256SUMS.txt', 'bytes': 790, 'sha256': '28fe9510a869fa4114d5f64693b97a72d80b558824f3ca05583b1edc287cc207', 'git_sha': 'f04b5b66843bf1a84b22c4872783e8e5e2dfb8b5'}, {'name': 'SOURCE_EVIDENCE_MAP.json', 'bytes': 1094, 'sha256': '1b5203c53a0c6085aedf4ce43c0774b918be068146ba8a947940f5a57d0e6205', 'git_sha': 'e3e5e016dce48387a34cef733347710173c886a6'}, {'name': 'historical_tools_batch10_overlay_candidate_20261109.tar.xz.part000', 'bytes': 250000, 'sha256': 'cfb6b50d8ac815db51355fc7f6c2209024cfe68392a8c5b982f960399cbd5078', 'git_sha': '4b55d28f7e89a0fc29c2b6e16b5c947df0594a43'}, {'name': 'historical_tools_batch10_overlay_candidate_20261109.tar.xz.part001', 'bytes': 250000, 'sha256': '416925cac707e743d95440c622b84771d4df5ae49e7389e2896b3b0a8b6d9811', 'git_sha': '52c6a7aff58cf49a3802d0fe26370a7f39315a1d'}, {'name': 'historical_tools_batch10_overlay_candidate_20261109.tar.xz.part002', 'bytes': 250000, 'sha256': '912cd04c1956677b8f445554d901748e5fe344994ea5a0388ad1879595fb7938', 'git_sha': '32a7c7ea03b7d5e39369cb7fd05bacd9d4665380'}, {'name': 'historical_tools_batch10_overlay_candidate_20261109.tar.xz.part003', 'bytes': 250000, 'sha256': '31ce5836b531092d58f2b25acbd24369b578462af1b4127d4caa62bca203837a', 'git_sha': 'a91bcb4c6a0f32105e9d50fecf57520db8fd72e2'}, {'name': 'historical_tools_batch10_overlay_candidate_20261109.tar.xz.part004', 'bytes': 187512, 'sha256': 'fc4ee430e6ffa4900f93541d6f6ca4d9431165090b3c6379d18c1bb946f6768e', 'git_sha': '066349ccd25a3eb587c902ef2b43731f138f6474'}]}
COMMIT='8c770835a2fbfc6fcec87d2e70ca7ef608214969'
REPO='https://raw.githubusercontent.com/Ethsigema/AI_text01/'
ap=argparse.ArgumentParser(description='Verify downloaded batch10 historical-original candidate against exact existing source baseline; does not run game or create complete runtime directory.')
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
batch(COMMIT,PLAN['folder'],PLAN['files'],OUT/'batch10')
m=json.loads((OUT/'batch10/MANIFEST.json').read_text());b=b''.join((OUT/'batch10'/p['name']).read_bytes() for p in m['parts'])
assert meta(b)=={k:m[k] for k in ['bytes','sha256']};(OUT/'batch10'/m['archive']).write_bytes(b)
prefix=m['archive'].removesuffix('.tar.xz');content=archive_content(b,prefix,m['files']);internal=json.loads(content[prefix+'/FILE_MANIFEST.json'])
assert {prefix+'/'+n:v for n,v in internal.items()}=={n:meta(v) for n,v in content.items() if n!=prefix+'/FILE_MANIFEST.json'}
assert len(content)==166 and len(internal)==165
assert all(not set(x.lower() for x in PurePosixPath(n).parts)&{'home','cache','__pycache__','.godot','.aws','.ssh','.codex','sessions','cookies','chats','messages'} for n in content)
pkg=OUT/'extracted'/prefix
for name,data in content.items():p=OUT/'extracted'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
sr=subprocess.run([sys.executable,str(pkg/'verify_candidate.py')],capture_output=True,text=True,check=True);static=json.loads(sr.stdout);assert static['checks']==560
dump(OUT/'STATIC_EVIDENCE_VERIFICATION.json',static)
print('PASS: fresh batch10 archive, 5 parts, 166 members, 165 internal manifest entries, 560 read-only checks',flush=True)
deps=m['dependencies'];dep=deps['source_baseline'];dd=OUT/'source_baseline'
mb=fetch(dep['commit'],dep['folder'],'MANIFEST.json',dd/'MANIFEST.json');assert meta(mb)['sha256']==dep['manifest_sha256'];dm=json.loads(mb)
parts=batch(dep['commit'],dep['folder'],dm['parts'],dd);db=b''.join(parts);assert meta(db)=={k:dm[k] for k in ['bytes','sha256']} and meta(db)['sha256']==dep['archive_sha256'];(dd/dm['archive']).write_bytes(db)
dp=dm['archive'].removesuffix('.tar.xz');dc=archive_content(db,dp,dm['files']);di=json.loads(dc[dp+'/FILE_MANIFEST.json'])
assert {dp+'/'+n:v for n,v in di.items()}=={n:meta(v) for n,v in dc.items() if n!=dp+'/FILE_MANIFEST.json'}
basebytes=content[prefix+'/BASE_MAP.json'];assert dc[dp+'/SOURCE_MAP.json']==basebytes and meta(basebytes)['sha256']==dep['source_map_sha256']
dep_receipt=json.loads(fetch(dep['commit'],dep['folder'],'REMOTE_STREAM_VERIFIED.json',dd/'REMOTE_STREAM_VERIFIED.json'));assert dep_receipt['candidate_source_map_sha256']==dep['source_map_sha256'] and dep_receipt['remaining_reference_gaps_within_original_scope']==350 and not dep_receipt['full_game_verified']
print('PASS: fresh fixed batch9 baseline archive, 5 parts, 178 members, 177 internal entries; exact BASE_MAP continuity',flush=True)
base=json.loads(basebytes);target=json.loads(content[prefix+'/SOURCE_MAP.json']);changes=json.loads(content[prefix+'/CHANGES.json']);added=changes['added'];expected=['tools/final_source_overrides.py']
assert added==expected and changes['modified']==changes['removed']==[] and set(target)-set(base)==set(added)
delta={n:meta(content[prefix+'/delta/'+n]) for n in added};assert {**base,**delta}==target and sum(x['bytes'] for x in delta.values())==3984
assert len(base)==27915 and len(target)==27916 and sum(v['bytes'] for v in target.values())==1549279351
# Actual historical bytes are reused from a previously restored baseline, not called fresh downloads.
actual=set()
for p in BASE.rglob('*'):
 assert not p.is_symlink(),str(p)
 if p.is_file():actual.add(p.relative_to(BASE).as_posix())
assert actual==set(base)
for n in target:
 p=PurePosixPath(n);assert not p.is_absolute() and '..' not in p.parts
reconstruction=OUT/'selected_original_delta'
origin=json.loads(content[prefix+'/ORIGIN_VERIFIED.json']);evidence=json.loads(content[prefix+'/SOURCE_EVIDENCE_MAP.json'])
assert filemeta(ZIP)['sha256']==origin['original_zip_sha256']=='33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65'
with zipfile.ZipFile(ZIP) as z:
 for rel,record in evidence.items():
  captured=content[prefix+'/source_evidence/'+rel]
  assert meta(captured)==record==base[rel] and captured==(BASE/rel).read_bytes()
  assert z.read('酒馆战棋_新范围半成品交接包_20261101/游戏工程/'+rel)==captured
chain_run=subprocess.run([sys.executable,str(pkg/'verify_chain.py')],capture_output=True,text=True,check=True)
chain=json.loads(chain_run.stdout);assert chain==json.loads(content[prefix+'/CHAIN_VERIFIED.json'])
dump(OUT/'HISTORICAL_CHAIN_REVERIFIED.json',chain)
helper='tools/final_source_overrides.py';p1='research/bouncy_refresh_native_recovery/';p2='research/sparring_partner_native_recovery/'
old=content[prefix+'/source_evidence/'+p1+'candidates/'+helper];new=content[prefix+'/source_evidence/'+p2+'candidates/'+helper]
assert new==content[prefix+'/delta/'+helper] and meta(new)==delta[helper]
selected=reconstruction/helper;selected.parent.mkdir(parents=True);selected.write_bytes(new)
def section(blob):
 lines=blob.splitlines(keepends=True);selected=[]
 for i,line in enumerate(lines):
  if line==b'--- a/'+helper.encode()+b'\n' and lines[i+1]==b'+++ b/'+helper.encode()+b'\n':
   j=i+2
   while j<len(lines) and not lines[j].startswith((b'--- ',b'diff --git ')):j+=1
   selected.append(b''.join(lines[i:j]))
 assert len(selected)==1;return selected[0]
work=OUT/'gnu_chain';src=work/helper;src.parent.mkdir(parents=True);src.write_bytes(old)
first=work/'FIRST.patch';second=work/'SECOND.patch'
first.write_bytes(section(content[prefix+'/source_evidence/'+p1+'bouncy_refresh.patch']))
second.write_bytes(section(content[prefix+'/source_evidence/'+p2+'shared_changes.patch']))
steps=[]
for patch,reverse,expected_sha in [(first,True,chain['derived_ancestor_sha256']),(first,False,meta(old)['sha256']),(second,False,meta(new)['sha256']),(second,True,meta(old)['sha256'])]:
 proc=subprocess.run(['patch','--batch','--fuzz=0','--reverse' if reverse else '--forward','-p1','-i',str(patch)],cwd=work,capture_output=True,text=True,check=True)
 assert 'offset' not in proc.stdout.lower() and 'fuzz' not in proc.stdout.lower() and filemeta(src)['sha256']==expected_sha
 steps.append({'patch':patch.name,'reverse':reverse,'sha256':expected_sha,'zero_fuzz_and_offset':True})
original_result={'target':helper,**meta(new),'existing_historical_original_matches_fresh_delta':True,'six_source_evidence_members_match_reused_original_zip':True,'GNU_chain_steps':steps,'derived_ancestor_is_not_independently_found_original':True}
dump(OUT/'ORIGINAL_BYTE_VERIFICATION.json',original_result)
print('PASS: exact existing original, six official ZIP evidence members, two historical patch edges with independent GNU forward/reverse checks',flush=True)
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
assert rebuilt==target and baseaggregate.hexdigest()=='ed0a7b545e0fc5339619cd7b735f426962e7a47874e9908e75b9ea9fb9e6c519'
assert aggregate.hexdigest()=='f159ef6f456e8cade1b5d8eebc84e8833b95659af2a5ef6f7bd5911d3e95074b'
sourcebytes=(json.dumps(rebuilt,sort_keys=True,indent=2)+'\n').encode();assert sourcebytes==content[prefix+'/SOURCE_MAP.json'];(OUT/'REBUILT_SOURCE_MAP.json').write_bytes(sourcebytes)
# Re-read every baseline file after reconstruction to establish it remains byte-exact.
for n,v in base.items():assert filemeta(BASE/n)==v,n
assert {p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()}==set(base)
print('PASS: 27,916 actual files streamed, 1,549,279,351 bytes; baseline 27,915 files rehashed again unchanged',flush=True)
report={'status':'PASS_FRESH_BATCH10_PACKAGE_WITH_REUSED_EXACT_BASELINE_HISTORICAL_ORIGINAL_STREAM_RECONSTRUCTION','archive_commit':COMMIT,'folder':PLAN['folder'],'published_files_freshly_downloaded':len(PLAN['files']),'archive':m['archive'],**meta(b),'archive_parts_verified':len(m['parts']),'archive_members_verified':len(content),'internal_manifest_entries_verified':len(internal),'read_only_evidence_checks':560,'source_baseline_commit':dep['commit'],'source_baseline_archive_freshly_downloaded':True,'source_baseline_archive_sha256':meta(db)['sha256'],'source_baseline_archive_members_verified':len(dc),'source_baseline_archive_internal_entries_verified':len(di),'source_baseline_archive_parts_verified':len(dm['parts']),'historical_baseline_tree_reused':True,'historical_154_layer_chain_freshly_downloaded':False,'historical_154_layer_chain_rerun':False,'official_original_zip_reused':True,'official_original_zip_fully_rehashed':True,'baseline_source_files_rehashed_before_and_after':len(base),'candidate_files_streamed':len(target),'candidate_bytes_streamed':sum(v['bytes'] for v in target.values()),'candidate_source_map_sha256':meta(sourcebytes)['sha256'],'candidate_aggregate_sha256':aggregate.hexdigest(),'aggregate_format':'Sorted UTF-8 path, NUL, ASCII byte count, NUL, actual file bytes, repeated for all candidate files.','historical_original_verification':original_result,'exact_historical_chain_reverified':chain,'assertions_enabled_required':True,'assertions_enabled_during_verification':not sys.flags.optimize and __debug__,'python_optimization_forbidden':True,'source_changes':changes,'remaining_reference_gaps_within_original_scope':349,'candidate_is_existing_historical_original':True,'candidate_actual_prior_installation_proven':False,'latest_installed_versions_proven':False,'full_candidate_runtime_directory_created_by_backup_verifier':False,'complete_candidate_reconstructed_as_actual_byte_stream':True,'candidate_producer_had_created_full_tree_evidence_checked_not_repeated':True,'gameplay_rerun':False,'Godot_rerun':False,'candidate_compiler_modules_executed_by_backup_verifier':False,'full_game_verified':False,'old_save_compatibility_verified':False,'historical_baseline_unchanged':True,'all_prior_backups_preserved':True,'missing_source_files':[],'mismatched_source_files':[],'unexpected_source_files':[],'downloads':sorted(downloads,key=lambda x:x['url']),'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
dump(OUT/'REMOTE_STREAM_VERIFIED.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='downloads'},indent=2),flush=True)
