from pathlib import Path,PurePosixPath
import argparse,json,hashlib,tarfile,io,urllib.request,time,concurrent.futures,datetime,subprocess,zipfile,re,sys,os,threading
if sys.flags.optimize or not __debug__ or os.environ.get("PYTHONOPTIMIZE", "") not in ("", "0"):
 raise RuntimeError("Python assertions are required. Do not use -O, -OO, or nonzero PYTHONOPTIMIZE.")
PLAN = {'folder': 'battlegrounds-backup/pending/20261109-historical-tools-batch12-new-enforcer-correction', 'branch': 'battlegrounds-recovery-20261103', 'parent': 'c920ae817ceb3c822ebb8456bcf7ba55643f27e4', 'tree': '51487891e820926ae019c27c81d95022e70173ec', 'files': [{'name': 'CHANGES.json', 'bytes': 103, 'sha256': '9f96c6dc41006981eee4ac0666e1fdefd3f096f1cd016a8aa7be08ed7a494988', 'git_sha': 'dfcbd72fdbee6c52517f09b64126a86cbfc32669'}, {'name': 'DEFERRED_BOLVAR.json', 'bytes': 765, 'sha256': '0dbf8db492f3e8eb79e70be66e422c7e99ab1d723d44fd9c56373a0a7764b414', 'git_sha': 'ca6f2dac0e4a7eaa9907cdd5ae685bde3fd18037'}, {'name': 'DEPENDENCIES.json', 'bytes': 985, 'sha256': 'ccdf8477154aed009470cb7020aa9f39e218611a97633ceb72be88daee338fcd', 'git_sha': '070c226e594ced049321915b8eec521d3c164a36'}, {'name': 'MANIFEST.json', 'bytes': 67006, 'sha256': '5c4f1094a28e392304393fc7eae1b74d9e9a504b3bdd9b427d04055ff70996d7', 'git_sha': '6e35057f4bff9bb41e176f4b0c06b94ba2658467'}, {'name': 'PACKAGE_VERIFIED.json', 'bytes': 848, 'sha256': 'c4bf93d2022b7113531342bff45ffecfa8f43a61add1cb3a3340498d7f90b5af', 'git_sha': 'b6e43c15ca18eccf6b6f0c95a9778ace6fd287cc'}, {'name': 'README.md', 'bytes': 7594, 'sha256': '5f5b8668a17c8b0b44c84fecb81712b4e05bf500fdb3f2ffe446a182329d4918', 'git_sha': '6c236b70395d9f5681d19c871f63ba7c397ff7e9'}, {'name': 'RECOVERY.md', 'bytes': 2331, 'sha256': '03a2b4a4e9dbc7522b684100cbe824b818712c980fff3f558bce0aa0471493b8', 'git_sha': '980b61d2fbaaf7b07e3692c4eb6c3eb56f55b0be'}, {'name': 'REMAINING_SCOPE.json', 'bytes': 15645, 'sha256': 'b1ac707f9d44e35ea1846fb858de6156ccd2bbc64287cb457c64ccb8735bcd02', 'git_sha': 'e6620dade1af469bdd1909ccecd54b0b091391ac'}, {'name': 'REMOVALS.json', 'bytes': 3, 'sha256': '37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570', 'git_sha': 'fe51488c7066f6687ef680d6bfaa4f7768ef205c'}, {'name': 'SHA256SUMS.txt', 'bytes': 965, 'sha256': 'd1b4d9ad7fe9f3d598b782523eba2b962486c740376220a557aec2e84578d596', 'git_sha': 'f7aea7a7d3910bb9007335d1fe5e6abda561703b'}, {'name': 'TESTS_VERIFIED.json', 'bytes': 3550, 'sha256': '276c79c8341f6c047a6388464aca6b2beb74ba869173f38c6ae026f3b96def51', 'git_sha': '0f5a06b215d6b34795206b674319bf1df8eac45f'}, {'name': 'historical_tools_batch12_new_enforcer_correction_20261109.tar.xz.part000', 'bytes': 250000, 'sha256': '84b79a3f6958230f238129a9ca1e9bef446a3b860aee83264aa6e803dbcb5fab', 'git_sha': '18fc182c865f2d07537322885b7b3ccc7ce57a44'}, {'name': 'historical_tools_batch12_new_enforcer_correction_20261109.tar.xz.part001', 'bytes': 250000, 'sha256': '6e282c191110d65cbd6bf14866a55a6dde561217351e03ef83f2f55e55fbb822', 'git_sha': 'dd1125fd3bf62fe5dd4e60551776f9d5b37d75bd'}, {'name': 'historical_tools_batch12_new_enforcer_correction_20261109.tar.xz.part002', 'bytes': 250000, 'sha256': '1319a6d3b5687d81711df04572fdb3dc2a5d7e923a3c086fc02c217dc9620a44', 'git_sha': '7671a91d1165f6e6b8b65879d4808b6b3221af00'}, {'name': 'historical_tools_batch12_new_enforcer_correction_20261109.tar.xz.part003', 'bytes': 250000, 'sha256': '0e3e7fc9dd4c2aec466afe6872c765680ac07ada2be1db722cbc656ee0244e77', 'git_sha': 'f651c54d95a7b8fdd25a483afc19c54ca2b45934'}, {'name': 'historical_tools_batch12_new_enforcer_correction_20261109.tar.xz.part004', 'bytes': 250000, 'sha256': '6774dae643d2a8c49c2a5ab2a472d663961f4cf57e93574d824b93a0cc34481f', 'git_sha': '8cfd587ac375cd77933ab7958c3de99639c8ff08'}, {'name': 'historical_tools_batch12_new_enforcer_correction_20261109.tar.xz.part005', 'bytes': 223752, 'sha256': 'bf3a58132dec7c81eb72bd122ed8330a8ab672bc2d6e900ec48ca4994804de52', 'git_sha': '9633197fb19f6fb574d6adc11ac235ff591e020d'}]}
COMMIT='05cbc747bf7f2ed72fa5ef1d21e440f766258245'
REPO='https://raw.githubusercontent.com/Ethsigema/AI_text01/'
ap=argparse.ArgumentParser(description='Verify downloaded batch12 explicit new correction and fixed dependencies against exact existing source baseline; does not run game or create complete runtime directory.')
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
batch(COMMIT,PLAN['folder'],PLAN['files'],OUT/'batch12')
m=json.loads((OUT/'batch12/MANIFEST.json').read_text());b=b''.join((OUT/'batch12'/p['name']).read_bytes() for p in m['parts'])
assert meta(b)=={k:m[k] for k in ['bytes','sha256']};(OUT/'batch12'/m['archive']).write_bytes(b)
prefix=m['archive'].removesuffix('.tar.xz');content=archive_content(b,prefix,m['files']);internal=json.loads(content[prefix+'/FILE_MANIFEST.json'])
assert {prefix+'/'+n:v for n,v in internal.items()}=={n:meta(v) for n,v in content.items() if n!=prefix+'/FILE_MANIFEST.json'}
assert len(content)==274 and len(internal)==273
whitelist=json.loads(content[prefix+'/FILE_WHITELIST.json']);assert set(whitelist['files'])==set(internal)
assert all(not set(x.lower() for x in PurePosixPath(n).parts)&{'home','cache','__pycache__','.godot','.aws','.ssh','.codex','sessions','cookies','chats','messages'} for n in content)
pkg=OUT/'extracted'/prefix
for name,data in content.items():p=OUT/'extracted'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
sr=subprocess.run([sys.executable,str(pkg/'verify_candidate.py')],capture_output=True,text=True,check=True);static=json.loads(sr.stdout);assert static['checks']==175 and static==json.loads(content[prefix+'/STATIC_VERIFICATION.json'])
dump(OUT/'STATIC_EVIDENCE_VERIFICATION.json',static)
print('PASS: fresh batch12 archive, 6 parts, 274 members, exact whitelist, 273 internal entries, 175 read-only checks',flush=True)
deps=m['dependencies'];dep=deps['source_baseline'];dd=OUT/'source_baseline'
mb=fetch(dep['commit'],dep['folder'],'MANIFEST.json',dd/'MANIFEST.json');assert meta(mb)['sha256']==dep['manifest_sha256'];dm=json.loads(mb)
parts=batch(dep['commit'],dep['folder'],dm['parts'],dd);db=b''.join(parts);assert meta(db)=={k:dm[k] for k in ['bytes','sha256']} and meta(db)['sha256']==dep['archive_sha256'];(dd/dm['archive']).write_bytes(db)
dp=dm['archive'].removesuffix('.tar.xz');dc=archive_content(db,dp,dm['files']);di=json.loads(dc[dp+'/FILE_MANIFEST.json'])
assert {dp+'/'+n:v for n,v in di.items()}=={n:meta(v) for n,v in dc.items() if n!=dp+'/FILE_MANIFEST.json'}
basebytes=content[prefix+'/BASE_MAP.json'];assert dc[dp+'/SOURCE_MAP.json']==basebytes and meta(basebytes)['sha256']==dep['source_map_sha256']
dep_receipt=json.loads(fetch(dep['commit'],dep['folder'],'REMOTE_STREAM_VERIFIED.json',dd/'REMOTE_STREAM_VERIFIED.json'));assert dep_receipt['candidate_source_map_sha256']==dep['source_map_sha256'] and dep_receipt['remaining_reference_gaps_within_original_scope']==349 and not dep_receipt['full_game_verified']
print('PASS: fresh fixed batch10 source dependency, 5 parts, 166 members, exact BASE_MAP continuity',flush=True)
reviewdep=deps['prior_review'];rd=OUT/'prior_review'
rmb=fetch(reviewdep['commit'],reviewdep['folder'],'MANIFEST.json',rd/'MANIFEST.json');assert meta(rmb)['sha256']==reviewdep['manifest_sha256'];rm=json.loads(rmb)
rparts=batch(reviewdep['commit'],reviewdep['folder'],rm['parts'],rd);rb=b''.join(rparts);assert meta(rb)=={k:rm[k] for k in ['bytes','sha256']} and meta(rb)['sha256']==reviewdep['archive_sha256'];(rd/rm['archive']).write_bytes(rb)
rp=rm['archive'].removesuffix('.tar.xz');rc=archive_content(rb,rp,rm['files']);ri=json.loads(rc[rp+'/FILE_MANIFEST.json'])
assert {rp+'/'+n:v for n,v in ri.items()}=={n:meta(v) for n,v in rc.items() if n!=rp+'/FILE_MANIFEST.json'}
assert rc[rp+'/SOURCE_MAP.json']==rc[rp+'/BASE_MAP.json']==basebytes
rpkg=OUT/'extracted_review'/rp
for name,data in rc.items():p=OUT/'extracted_review'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
rr=subprocess.run([sys.executable,str(rpkg/'verify_review.py')],capture_output=True,text=True,check=True);rstatic=json.loads(rr.stdout);assert rstatic['checks']==3835;dump(OUT/'PRIOR_REVIEW_STATIC_VERIFICATION.json',rstatic)
print('PASS: fresh fixed batch11 review, 8 parts, 334 members, 333 internal entries, 3835 read-only checks',flush=True)
base=json.loads(basebytes);target=json.loads(content[prefix+'/SOURCE_MAP.json']);changes=json.loads(content[prefix+'/CHANGES.json']);added=changes['added'];expected=['tools/native_enforcer_shield_patterns.py']
assert added==expected and changes['modified']==changes['removed']==[] and set(target)-set(base)==set(added)
delta={n:meta(content[prefix+'/delta/'+n]) for n in added};assert {**base,**delta}==target and sum(x['bytes'] for x in delta.values())==2480
assert len(base)==27916 and len(target)==27917 and sum(v['bytes'] for v in target.values())==1549281831
# Historical baseline bytes and ZIP are reused and rehashed; they are not called fresh downloads.
actual=set()
for p in BASE.rglob('*'):
 assert not p.is_symlink(),str(p)
 if p.is_file():actual.add(p.relative_to(BASE).as_posix())
assert actual==set(base)
for n in target:
 p=PurePosixPath(n);assert not p.is_absolute() and '..' not in p.parts
assert filemeta(ZIP)['sha256']=='33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65'
inputs=json.loads(content[prefix+'/HISTORICAL_INPUT_MAP.json']);priorinputs=json.loads(rc[rp+'/historical_evidence/INPUT_MAP.json']);assert len(inputs)==5 and len(priorinputs)==45
with zipfile.ZipFile(ZIP) as z:
 for rel,record in priorinputs.items():
  captured=rc[rp+'/historical_evidence/inputs/'+rel]
  assert meta(captured)==record==base[rel] and captured==(BASE/rel).read_bytes()
  assert z.read('酒馆战棋_新范围半成品交接包_20261101/游戏工程/'+rel)==captured
 for rel,record in inputs.items():
  captured=content[prefix+'/historical_inputs/'+rel]
  assert meta(captured)==record==base[rel] and captured==rc[rp+'/historical_evidence/inputs/'+rel]==(BASE/rel).read_bytes()
  assert z.read('酒馆战棋_新范围半成品交接包_20261101/游戏工程/'+rel)==captured
# Reconstruct historical literal/AST payloads without executing generators, modules, or game.
historic=OUT/'historical_review_reconstructed'
hr=subprocess.run([sys.executable,str(rpkg/'reconstruct_review_to_new.py'),str(historic)],capture_output=True,text=True,check=True)
(OUT/'HISTORICAL_RECONSTRUCTION.log').write_text(hr.stdout)
hreport=json.loads((historic/'REVIEW_ONLY.json').read_text());assert not hreport['generators_executed'] and not hreport['runtime_installed'] and len(hreport['outputs'])==2
links=json.loads(content[prefix+'/HISTORICAL_VERSION_LINKS.json'])
for row in links:
 n=row['target'];data=(historic/n).read_bytes();pin=content[prefix+'/historical_inputs/'+row['independent_manifest_path']]
 assert data==content[prefix+'/correction_review/originals/'+n]==rc[rp+'/counterexamples/candidates/'+n]
 assert meta(data)['sha256']==row['historical_postimage_sha256']==json.loads(pin)[row['field']][n]
 assert meta(pin)['sha256']==row['independent_manifest_sha256'] and row['prior_review_fixed_commit']==reviewdep['commit']
# Apply only the explicit patch in a fresh review directory; Bolvar output is never installed.
reconstruction=OUT/'reconstructed_new_review_only'
pr=subprocess.run([sys.executable,str(pkg/'apply_review_patch_to_new.py'),str(reconstruction)],capture_output=True,text=True,check=True)
(OUT/'NEW_PATCH_REPLAY.log').write_text(pr.stdout);patchreport=json.loads((reconstruction/'REPLAY.json').read_text());assert patchreport['zero_offset'] and patchreport['zero_fuzz'] and not patchreport['old_or_runtime_files_modified']
assert len(patchreport['files'])==2
for row in patchreport['files']:
 n=row['target'];data=(reconstruction/n).read_bytes();assert meta(data)=={'bytes':row['bytes'],'sha256':row['sha256']} and data==content[prefix+'/correction_review/proposed/'+n]
 if n in added:assert data==content[prefix+'/delta/'+n] and meta(data)==target[n]
 else:assert row['status']=='DEFERRED_REVIEW_ONLY' and n not in target
# GNU reverse and forward checks establish exact patch reversibility at zero fuzz and offset.
patch=content[prefix+'/correction_review/COMBINED_COMPARATOR_CORRECTIONS.patch']
roundtrip=[]
for reverse,expectedfolder in [(True,'originals'),(False,'proposed')]:
 cmd=['patch','--batch','--fuzz=0','-p1','-d',str(reconstruction),'--reverse' if reverse else '--forward']
 p=subprocess.run(cmd,input=patch,capture_output=True,timeout=10)
 assert p.returncode==0 and b'offset' not in p.stdout.lower() and b'fuzz' not in p.stdout.lower(),p.stdout
 for row in patchreport['files']:assert (reconstruction/row['target']).read_bytes()==content[prefix+'/correction_review/'+expectedfolder+'/'+row['target']]
 roundtrip.append({'direction':'reverse' if reverse else 'forward','exit':p.returncode,'zero_fuzz':True,'zero_offset':True})
remaining=json.loads(content[prefix+'/REMAINING_SCOPE.json']);assert remaining['remaining_original_scope']==348 and len(remaining['remaining_targets'])==348 and all(n not in target for n in remaining['remaining_targets'])
assert 'tools/native_bolvar_shield_patterns.py' not in base and 'tools/native_bolvar_shield_patterns.py' not in target
print('PASS: 45 prior and 5 current official ZIP inputs, historical literal reconstructions, exact new patch forward/reverse/forward; Bolvar remains review-only',flush=True)
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
assert aggregate.hexdigest()=='c7698b11fbc7045b82ce0f7f096d3417b31d5984b6a6ec5236de74cc8034aff9'
sourcebytes=(json.dumps(rebuilt,sort_keys=True,indent=2)+'\n').encode();assert sourcebytes==content[prefix+'/SOURCE_MAP.json'];(OUT/'REBUILT_SOURCE_MAP.json').write_bytes(sourcebytes)
for n,v in base.items():assert filemeta(BASE/n)==v,n
assert {p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()}==set(base)
print('PASS: 27,917 candidate files streamed, 1,549,281,831 bytes; 27,916 baseline files rehashed twice unchanged',flush=True)
report={'status':'PASS_FRESH_BATCH12_NEW_ENFORCER_CORRECTION_STREAM_RECONSTRUCTION','archive_commit':COMMIT,'folder':PLAN['folder'],'published_files_freshly_downloaded':len(PLAN['files']),'archive':m['archive'],**meta(b),'archive_parts_verified':len(m['parts']),'archive_members_verified':len(content),'internal_manifest_entries_verified':len(internal),'exact_whitelist_verified':True,'read_only_evidence_checks':175,'source_baseline_commit':dep['commit'],'source_baseline_archive_freshly_downloaded':True,'source_baseline_archive_sha256':meta(db)['sha256'],'source_baseline_archive_parts_verified':len(dm['parts']),'source_baseline_archive_members_verified':len(dc),'source_baseline_archive_internal_entries_verified':len(di),'prior_review_commit':reviewdep['commit'],'prior_review_archive_freshly_downloaded':True,'prior_review_archive_sha256':meta(rb)['sha256'],'prior_review_archive_parts_verified':len(rm['parts']),'prior_review_archive_members_verified':len(rc),'prior_review_archive_internal_entries_verified':len(ri),'prior_review_read_only_checks':3835,'historical_baseline_tree_reused':True,'historical_chain_freshly_downloaded':False,'historical_chain_rerun':False,'official_original_zip_reused':True,'official_original_zip_fully_rehashed':True,'current_historical_input_members_verified_against_ZIP_and_actual_baseline':len(inputs),'prior_historical_input_members_verified_against_ZIP_and_actual_baseline':len(priorinputs),'historical_review_only_reconstructions':hreport['outputs'],'new_review_patch_reconstructions':patchreport['files'],'new_patch_roundtrip':roundtrip,'historical_generators_executed':False,'candidate_modules_executed':False,'Bolvar_candidate_installed':False,'Bolvar_still_deferred':True,'baseline_files_rehashed_twice':len(base),'baseline_bytes':sum(v['bytes'] for v in base.values()),'candidate_files_rebuilt_as_actual_byte_stream':len(rebuilt),'candidate_bytes':sum(v['bytes'] for v in rebuilt.values()),'candidate_source_map_sha256':meta(sourcebytes)['sha256'],'candidate_source_aggregate_sha256':aggregate.hexdigest(),'source_changes':changes,'runtime_source_changes':1,'historical_originals_restored_this_batch':0,'remaining_reference_gaps_within_original_scope':348,'assertions_enabled_required':True,'assertions_enabled_during_verification':not sys.flags.optimize and __debug__,'full_runtime_directory_created_by_backup_verifier':False,'full_static_dependency_audit_rerun':False,'all_historical_searches_rerun':False,'gameplay_rerun':False,'Godot_rerun':False,'full_compiler_executed':False,'full_game_verified':False,'full_catalog_verified':False,'old_save_compatibility_verified':False,'latest_versions_proven':False,'historical_baseline_unchanged':True,'all_prior_backups_preserved':True,'missing_source_files':[],'mismatched_source_files':[],'unexpected_source_files':[],'downloads':sorted(downloads,key=lambda x:x['url']),'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
dump(OUT/'REMOTE_STREAM_VERIFIED.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='downloads'},indent=2),flush=True)
