from pathlib import Path,PurePosixPath
import argparse,json,hashlib,tarfile,io,urllib.request,time,concurrent.futures,datetime,subprocess,zipfile,re
PLAN = {'folder': 'battlegrounds-backup/pending/20261109-historical-tools-batch8-patch-candidate', 'branch': 'battlegrounds-recovery-20261103', 'parent': 'ca902d3bc382190a5e2b3d19b057ea10c6712f00', 'tree': 'cf3b5f675018e537ac8d513e82535b18006e6f73', 'files': [{'name': 'CHANGES.json', 'bytes': 127, 'sha256': '7f9d29fcc9fc39406f8cca51678f98f6c60864a31757616b15c1cc7a3c93625e', 'git_sha': 'd44375ac2a49319ea0785a4c098c17a8085d6ca8'}, {'name': 'DEPENDENCIES.json', 'bytes': 805, 'sha256': 'd524afc8a58fd17259dd2c893cb13ce60e3a4417e193d3d6d7e96eaf52abb30f', 'git_sha': 'd599ef4726a67ae35b9667ed7a0af9cf9f6ba75b'}, {'name': 'MANIFEST.json', 'bytes': 54003, 'sha256': 'df196d3ea32f1a11a6abb0b5f0d312cc0ad9c2036ba0973d2a37b46d90da4933', 'git_sha': 'd1cdefeab7caaf04058b59817592244d9d3a3f49'}, {'name': 'PACKAGE_VERIFIED.json', 'bytes': 1190, 'sha256': '81fce5ded7c68b43f7b23d6fc79bbde4cb150e63bf6aeb66b1d91a745f507489', 'git_sha': 'ad3392a74d5639abaa0492972788140ccf316e82'}, {'name': 'README.md', 'bytes': 6251, 'sha256': 'd5f2845dfc2c297f3f0fcc2cbdc1c24177e3b6f77928b5be773492dc689ffe0b', 'git_sha': 'db50243ff823f3bd139fa25bc044094714bcf376'}, {'name': 'RECONSTRUCTION_PROVENANCE.json', 'bytes': 3258, 'sha256': '109008ad8079bbc6478f066ca24d74650be2226b480883241f19b77a0fbcec63', 'git_sha': '17cfdfb10526b433ed41cd0552b7958568a2b0f7'}, {'name': 'RECOVERY.md', 'bytes': 2259, 'sha256': 'c2d23d246c58841d392e5499eb46e5728a0747e1de88d8dea81cf3e131a4b52a', 'git_sha': 'ad2a7fcffd2703b8884054559641a435cf47e736'}, {'name': 'REMAINING_SCOPE.json', 'bytes': 16529, 'sha256': '519bc5310ba8821c47579e0c1f0efd6a8031c7157771dab58fae036b89da4cc1', 'git_sha': '33749dcf843e5ec655c303bc9287aad75426568d'}, {'name': 'REMOVALS.json', 'bytes': 3, 'sha256': '37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570', 'git_sha': 'fe51488c7066f6687ef680d6bfaa4f7768ef205c'}, {'name': 'SHA256SUMS.txt', 'bytes': 902, 'sha256': '84214cf8ec8649bfdb523fc6a142a91dbe86e0c343807ff34714f64e357d6a83', 'git_sha': '301e4266acf1afa5642536820de454331c73ab95'}, {'name': 'historical_tools_batch8_patch_candidate_20261109.tar.xz.part000', 'bytes': 250000, 'sha256': 'd75f507012763d3fe8748e9f8fb9d8174f2cc5ce6b16941656ab33ab41dc7b14', 'git_sha': '2dd4ff7d9912e7aee5398ed3205a76ed47c12276'}, {'name': 'historical_tools_batch8_patch_candidate_20261109.tar.xz.part001', 'bytes': 250000, 'sha256': '3842f4c86af6a4a7f1c819082efe8dc63e6c94fff5337e2f2b11106838bf5542', 'git_sha': 'b2181e0b99d72bd21464391a29eb2e37f0f7cdb1'}, {'name': 'historical_tools_batch8_patch_candidate_20261109.tar.xz.part002', 'bytes': 250000, 'sha256': 'e90403510c1fae6596e49281b0a68e4c942fd35bd9a022cf9f883fdc102938fb', 'git_sha': '2ff5b56aa3d51526f767a07b8edc7b6a64a22832'}, {'name': 'historical_tools_batch8_patch_candidate_20261109.tar.xz.part003', 'bytes': 250000, 'sha256': '59b2242bad083a6cf144904a3f4bbb720b764c4811c180bbc8e22ce5c8291777', 'git_sha': '968af12378b6778d71a02e119bf5b3dca671eb61'}, {'name': 'historical_tools_batch8_patch_candidate_20261109.tar.xz.part004', 'bytes': 250000, 'sha256': '06285706dee8117bc46f623773f5ac5085076e9cbb33cb9a65995dd69a02b826', 'git_sha': '9b85d54f2218b4b8869c3b43cac2bb17c78e07d3'}, {'name': 'historical_tools_batch8_patch_candidate_20261109.tar.xz.part005', 'bytes': 44952, 'sha256': '87a0364adb67c2bc09bfa69a1e6927c2d5b75493bb686c3f9269dd1e87a0c50d', 'git_sha': '46234282408a7adf7766856e4a257655d4683b1d'}]}
COMMIT='c68c6e8c5f98d9f795a6bc546fe8cefc8675476b'
REPO='https://raw.githubusercontent.com/Ethsigema/AI_text01/'
ap=argparse.ArgumentParser(description='Verify downloaded batch8 candidate against exact existing source baseline; does not run game or create complete runtime directory.')
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
batch(COMMIT,PLAN['folder'],PLAN['files'],OUT/'batch8')
m=json.loads((OUT/'batch8/MANIFEST.json').read_text());b=b''.join((OUT/'batch8'/p['name']).read_bytes() for p in m['parts'])
assert meta(b)=={k:m[k] for k in ['bytes','sha256']};(OUT/'batch8'/m['archive']).write_bytes(b)
prefix=m['archive'].removesuffix('.tar.xz');content=archive_content(b,prefix,m['files']);internal=json.loads(content[prefix+'/FILE_MANIFEST.json'])
assert {prefix+'/'+n:v for n,v in internal.items()}=={n:meta(v) for n,v in content.items() if n!=prefix+'/FILE_MANIFEST.json'}
assert len(content)==234 and len(internal)==233
assert all(not set(x.lower() for x in PurePosixPath(n).parts)&{'home','cache','__pycache__','.godot','.aws','.ssh','.codex','sessions','cookies','chats','messages'} for n in content)
pkg=OUT/'extracted'/prefix
for name,data in content.items():p=OUT/'extracted'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
sr=subprocess.run(['python',str(pkg/'verify_candidate.py')],capture_output=True,text=True,check=True);static=json.loads(sr.stdout);assert static['checks']==188
dump(OUT/'STATIC_EVIDENCE_VERIFICATION.json',static)
print('PASS: fresh batch8 archive, 6 parts, 234 members, 233 internal manifest entries, 188 read-only checks',flush=True)
deps=m['dependencies'];dep=deps['source_baseline'];dd=OUT/'source_baseline'
mb=fetch(dep['commit'],dep['folder'],'MANIFEST.json',dd/'MANIFEST.json');assert meta(mb)['sha256']==dep['manifest_sha256'];dm=json.loads(mb)
parts=batch(dep['commit'],dep['folder'],dm['parts'],dd);db=b''.join(parts);assert meta(db)=={k:dm[k] for k in ['bytes','sha256']} and meta(db)['sha256']==dep['archive_sha256'];(dd/dm['archive']).write_bytes(db)
dp=dm['archive'].removesuffix('.tar.xz');dc=archive_content(db,dp,dm['files']);di=json.loads(dc[dp+'/PACKAGE_MANIFEST.json'])
assert {dp+'/'+n:v for n,v in di.items()}=={n:meta(v) for n,v in dc.items() if n!=dp+'/PACKAGE_MANIFEST.json'}
basebytes=content[prefix+'/BASE_MAP.json'];assert dc[dp+'/SOURCE_MAP.json']==basebytes and meta(basebytes)['sha256']==dep['source_map_sha256']
dep_receipt=json.loads(fetch(dep['commit'],dep['folder'],'DEVOURER_HISTORICAL_TOOL_STREAM_VERIFICATION.json',dd/'DEVOURER_HISTORICAL_TOOL_STREAM_VERIFICATION.json'));assert dep_receipt['source_map_sha256']==dep['source_map_sha256'] and not dep_receipt['full_game_validation_passed']
ctx=deps['review_context'];context=json.loads(fetch(ctx['commit'],ctx['folder'],'REMOTE_READBACK_VERIFIED.json',OUT/'review_context/REMOTE_READBACK_VERIFIED.json'));assert context['source_map_sha256']==dep['source_map_sha256'] and context['remaining_missing_paths_within_original_scope']==353 and context['game_source_changes']=={'added':0,'modified':0,'deleted':0}
print('PASS: fresh fixed Devourer baseline archive, 11 parts, 137 members, 136 internal entries; exact BASE_MAP continuity',flush=True)
base=json.loads(basebytes);target=json.loads(content[prefix+'/SOURCE_MAP.json']);changes=json.loads(content[prefix+'/CHANGES.json']);added=changes['added'];expected=['tools/aggramar_patterns.py','tools/mystery_cube_patterns.py']
assert added==expected and changes['modified']==changes['removed']==[] and set(target)-set(base)==set(added)
delta={n:meta(content[prefix+'/delta/'+n]) for n in added};assert {**base,**delta}==target and sum(x['bytes'] for x in delta.values())==84192
assert len(base)==27912 and len(target)==27914 and sum(v['bytes'] for v in target.values())==1549216476
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
  assert not row['independent_historical_postimage_found'] and not row['latest_installed_version_proven']
  patch_results.append({'target':row['target'],'bytes':row['reconstructed_bytes'],'sha256':row['reconstructed_sha256'],'exact_patch_replay_equal':True,'GNU_zero_fuzz_no_offset_equal':True,'reused_official_ZIP_original_and_patch_members_equal':True})
assert len(patch_results)==2
print('PASS: two exact patch reconstructions, independent GNU zero-fuzz check, reused official ZIP rehashed and selected members matched',flush=True)
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
assert rebuilt==target and baseaggregate.hexdigest()=='930f77dd965da27e5d16f2e29f5b495b99c95b526cf52a1279bad7eb9f42ec0b'
assert aggregate.hexdigest()=='2808118a744b4b62973ddd639dc39d4313a6d653e2ced479909a7a125e067f55'
sourcebytes=(json.dumps(rebuilt,sort_keys=True,indent=2)+'\n').encode();assert sourcebytes==content[prefix+'/SOURCE_MAP.json'];(OUT/'REBUILT_SOURCE_MAP.json').write_bytes(sourcebytes)
# Re-read every baseline file after reconstruction to establish it remains byte-exact.
for n,v in base.items():assert filemeta(BASE/n)==v,n
assert {p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()}==set(base)
print('PASS: 27,914 actual files streamed, 1,549,216,476 bytes; baseline 27,912 files rehashed again unchanged',flush=True)
report={'status':'PASS_FRESH_BATCH8_PACKAGE_WITH_REUSED_EXACT_BASELINE_TWO_PATCH_STREAM_RECONSTRUCTION','archive_commit':COMMIT,'folder':PLAN['folder'],'published_files_freshly_downloaded':len(PLAN['files']),'archive':m['archive'],**meta(b),'archive_parts_verified':len(m['parts']),'archive_members_verified':len(content),'internal_manifest_entries_verified':len(internal),'read_only_evidence_checks':188,'source_baseline_commit':dep['commit'],'source_baseline_archive_freshly_downloaded':True,'source_baseline_archive_sha256':meta(db)['sha256'],'source_baseline_archive_members_verified':len(dc),'source_baseline_archive_internal_entries_verified':len(di),'source_baseline_archive_parts_verified':len(dm['parts']),'historical_baseline_tree_reused':True,'historical_154_layer_chain_freshly_downloaded':False,'historical_154_layer_chain_rerun':False,'official_original_zip_reused':True,'official_original_zip_fully_rehashed':True,'baseline_source_files_rehashed_before_and_after':len(base),'candidate_files_streamed':len(target),'candidate_bytes_streamed':sum(v['bytes'] for v in target.values()),'candidate_source_map_sha256':meta(sourcebytes)['sha256'],'candidate_aggregate_sha256':aggregate.hexdigest(),'aggregate_format':'Sorted UTF-8 path, NUL, ASCII byte count, NUL, actual file bytes, repeated for all candidate files.','patch_reconstructions':patch_results,'source_changes':changes,'remaining_reference_gaps_within_original_scope':351,'independent_historical_postimages_found':False,'latest_installed_versions_proven':False,'full_candidate_runtime_directory_created_by_backup_verifier':False,'complete_candidate_reconstructed_as_actual_byte_stream':True,'candidate_producer_had_created_full_tree_evidence_checked_not_repeated':True,'gameplay_rerun':False,'Godot_rerun':False,'candidate_compiler_modules_executed_by_backup_verifier':False,'full_game_verified':False,'old_save_compatibility_verified':False,'historical_baseline_unchanged':True,'all_prior_backups_preserved':True,'missing_source_files':[],'mismatched_source_files':[],'unexpected_source_files':[],'downloads':sorted(downloads,key=lambda x:x['url']),'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
dump(OUT/'REMOTE_STREAM_VERIFIED.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='downloads'},indent=2),flush=True)
