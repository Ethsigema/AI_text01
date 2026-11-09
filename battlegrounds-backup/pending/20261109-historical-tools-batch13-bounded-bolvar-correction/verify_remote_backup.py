from pathlib import Path,PurePosixPath
import argparse,json,hashlib,tarfile,io,urllib.request,time,concurrent.futures,datetime,subprocess,zipfile,re,sys,os,threading
if sys.flags.optimize or not __debug__ or os.environ.get("PYTHONOPTIMIZE", "") not in ("", "0"):
 raise RuntimeError("Python assertions are required. Do not use -O, -OO, or nonzero PYTHONOPTIMIZE.")
assert sys.implementation.name=='cpython' and sys.version_info[:3]==(3,12,14), 'Use tested CPython 3.12.14 or validate interpreter behavior separately.'
PLAN = {'folder': 'battlegrounds-backup/pending/20261109-historical-tools-batch13-bounded-bolvar-correction', 'branch': 'battlegrounds-recovery-20261103', 'parent': '1e2ede27d0312440996e2c7c9e88ebdd033ee195', 'tree': '8a8080db2e7698e5a4807a37a73b7afee211b2d7', 'files': [{'name': 'CHANGES.json', 'bytes': 101, 'sha256': '4a9b7ca8be0761637b734213a275e63466487cdafc90b80c8068e0b382d6e54a', 'git_sha': 'cf1b85f19bec95a0d7f73510c11973c350244ee9'}, {'name': 'CURRENT_DEPENDENCY_STATUS.json', 'bytes': 491, 'sha256': '18287881f843de894c6e5381e53377a9cb8a42a44c619266811cb2d496872ee4', 'git_sha': '4bc5c133c0ae02746c0cb0551dce9bd946e44ef5'}, {'name': 'DEPENDENCIES.json', 'bytes': 634, 'sha256': '6d59b5f0a05db7a9c5c1e6256600f09c836d8208f6d55fcdac491fe032df2646', 'git_sha': '904dfa56cfc70ec602dbf6dcb8f052cab11bebc4'}, {'name': 'MANIFEST.json', 'bytes': 41816, 'sha256': 'be62ced6784ab18d54c0849c5662f7ed6914b03629af4606e3de09b65641e561', 'git_sha': '94c09e2e679fbb5762e30849191309ce45b5e9d2'}, {'name': 'PACKAGE_VERIFIED.json', 'bytes': 902, 'sha256': 'f52ab8d52f1e98a3cbc93f13ae7bd54a454f12811894af56bb117f9581ac19ba', 'git_sha': '8206076c68cd4f9727668266dbb7949364293053'}, {'name': 'README.md', 'bytes': 7722, 'sha256': 'e6f98176acbe2ac3b3830f12d575ef2fbda4045298a39d69002916fa01dc8abd', 'git_sha': '0a4a320ddd474505330c51fb8679c586b8a97dd3'}, {'name': 'RECOVERY.md', 'bytes': 2744, 'sha256': '6ad8b2a2e9dbd82fd9431b2d14c96ab0616ce2f533216ce077f9706eba2e33cb', 'git_sha': '700ee9ec32cb4ad602eb55d69f0ebe9670048f6f'}, {'name': 'REMAINING_SCOPE.json', 'bytes': 15437, 'sha256': '01184963d02c33ec2d430064a7525098c0faf9d55e9aed25767e5f3d6023db03', 'git_sha': '5e9f61259fea50c28eb71337cb7b6e5d216556f8'}, {'name': 'REMOVALS.json', 'bytes': 3, 'sha256': '37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570', 'git_sha': 'fe51488c7066f6687ef680d6bfaa4f7768ef205c'}, {'name': 'SHA256SUMS.txt', 'bytes': 3094, 'sha256': 'f126de39930b517cbce7860e729f6251089b7b7392f9336a8aed5145f3430e25', 'git_sha': 'ebf2d23db29261cb36910cbe8e984c4d33dc339e'}, {'name': 'TESTS_VERIFIED.json', 'bytes': 1880, 'sha256': 'bb43f64b19cf4b9c6af3be5ac574690d5333c506632c267e7e731c9c81640ad8', 'git_sha': '30a226fcf32b925415ba8fa1c06bb36f73b95221'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part000', 'bytes': 250000, 'sha256': '4dd52cd9b7c1c13c75f7468f36cbe726a25414f877cdcd5f59f5847a70e7681c', 'git_sha': '010de26a9a010961d6fd47f2564a6baa4fa8af2d'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part001', 'bytes': 250000, 'sha256': '25f1fbbde855d1fdc2cb797ed962fb8bb432b933cb6ad79ea86f416edf62c300', 'git_sha': '68e4f84c3f43d0e95569c2f118599304a5aaeb1c'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part002', 'bytes': 250000, 'sha256': 'd3fdd1dee69794f9a271b8d26e3c8cf4116903ce32669d99290554d7dc08e40f', 'git_sha': '7ecfb474266856a949fe38c2934c0fd836b1e5ed'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part003', 'bytes': 250000, 'sha256': 'faa579bc2bd7e97f2edcfb134f41fe76123524e0724c05f064f3ff129cdd998d', 'git_sha': '9b571708e66da80ed68974137969cb07693374bf'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part004', 'bytes': 250000, 'sha256': 'c9a70dd09e8c12450bb3a4c9c985e84193b8fbde5a0ead682673fa03f38fc57b', 'git_sha': 'c191dda4734e946f372ce334475aac600a0553cb'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part005', 'bytes': 250000, 'sha256': '1a87457f772e044d4a6e31334cfa7938e2c0221499912057217f3e5d1ad7154c', 'git_sha': 'df178d80a3ffac2ed7022781753820d38c54f885'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part006', 'bytes': 250000, 'sha256': 'b4c3e0c3384762d7f84b9271fb43bf3d387a9536951723e1608ac45ef0668543', 'git_sha': '69da1ff17d55caf7927fe90881161f914ba16b7a'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part007', 'bytes': 250000, 'sha256': '3509fdb70689825d0f746e4d20ee4c2cb235f7e1b5c6e62c6caee92daadc1473', 'git_sha': 'b10cdc9cec4b58622173c47b46d2d15e4b2610c7'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part008', 'bytes': 250000, 'sha256': '26121ad13de1d15ff941c2c3c2149c44e921901d93058aa83361f0db4fa10ad6', 'git_sha': '89f1b155ecd0ec17df1976bb704717c185cc2243'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part009', 'bytes': 250000, 'sha256': '2181f23d5b9c707f203e6857edfacbbe8a37de628aaa8704c5db15bfa7ad4e3d', 'git_sha': 'defb9333ff5d5d026b1d44d2dc62aa01de3848ce'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part010', 'bytes': 250000, 'sha256': '149f8cf63b1ef28e3b7c8975c2e58ac716d08d4a5ec21512a2dbee07aeba77ea', 'git_sha': '9cc9a0da9550d5ddffdf323d7d2e36ac7282b28b'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part011', 'bytes': 250000, 'sha256': '0d4b04f626f8182f4770817349073d41770635b59a281efdb2d917058614cb98', 'git_sha': '69680b638ea2769da1df542e0438e231a1e50a63'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part012', 'bytes': 250000, 'sha256': 'b906541ab733fc285d673ef2d46896b21813a86d777c42e02d1ed4c474c4b438', 'git_sha': '5c568d92b3f794e9159e88fcfe48e3b4f1f72a05'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part013', 'bytes': 250000, 'sha256': 'b841cb9f11c3bf8286d9d8c9005c4c3e6eb9b725e579ba4b40a0e5377a7efc52', 'git_sha': 'c50e4a2cfbf7a783ef7f1bcd235082bb7dceaab7'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part014', 'bytes': 250000, 'sha256': '566bf67e549e0a7651feedf9124b093280fbdf782ef6d20bcb897507ae06cf49', 'git_sha': 'aa922396d7adb1ae5476027ce3687410f85dcb34'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part015', 'bytes': 250000, 'sha256': 'f0f22180d1251113b2238856732aca9c7f5cac3833165fec7933d1570a059eac', 'git_sha': 'ff3a6cf578c9df5ccb2305aed185413db629fc3a'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part016', 'bytes': 250000, 'sha256': '835002b972556890d06d5d87cec07a7b8bc5cd742b62b895c279e6bd7d4ad032', 'git_sha': '5b294d10ade687a7f1d4a992bd372ad99e5c7a8c'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part017', 'bytes': 250000, 'sha256': '3b100b589f67f52174db8e10e2c79d69bede1974bddd86a6faa77ab519a4bb59', 'git_sha': '96f4ebf8339cb8344fb4733a2c1bf30e64339c78'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part018', 'bytes': 250000, 'sha256': 'f687ea6d686cc1246dd3d5c43fb9ee2b10be9fb956e18dfd9cbed57f59881a7f', 'git_sha': '39783cdc7e8d3f409fad0fdecf8628be680859a7'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part019', 'bytes': 250000, 'sha256': 'e3dc7e5a9f4aee7e2663fa853590cb5bd7db5e9819cf7b8de92bcb87b363d2f1', 'git_sha': '5262cfde82a283e6bc48790f236c77b8017c39ac'}, {'name': 'historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz.part020', 'bytes': 112724, 'sha256': '5014a8d5488278a851aff424eef90b227aa54afdb8f4c4107b4b87c0c2d58553', 'git_sha': 'ba8af4f796bce273cdb98e2f93b08de74fb2db31'}]}
COMMIT='2fa5d43c1d49600b3aa1cb4a4b2f3b2d3f00caf2'
REPO='https://raw.githubusercontent.com/Ethsigema/AI_text01/'
ap=argparse.ArgumentParser(description='Verify downloaded batch13 bounded Bolvar new correction and fixed batch12 source dependency against exact existing source baseline; does not run game or create complete runtime directory.')
ap.add_argument('--baseline-tree',type=Path,required=True)
ap.add_argument('--out',type=Path,required=True)
a=ap.parse_args();BASE=a.baseline_tree.resolve();OUT=a.out.resolve();assert BASE.is_dir() and not OUT.exists();OUT.mkdir(parents=True)
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
batch(COMMIT,PLAN['folder'],PLAN['files'],OUT/'batch13')
m=json.loads((OUT/'batch13/MANIFEST.json').read_text());b=b''.join((OUT/'batch13'/p['name']).read_bytes() for p in m['parts'])
assert meta(b)=={k:m[k] for k in ['bytes','sha256']};(OUT/'batch13'/m['archive']).write_bytes(b)
prefix=m['archive'].removesuffix('.tar.xz');content=archive_content(b,prefix,m['files']);internal=json.loads(content[prefix+'/FILE_MANIFEST.json'])
assert {prefix+'/'+n:v for n,v in internal.items()}=={n:meta(v) for n,v in content.items() if n!=prefix+'/FILE_MANIFEST.json'}
assert len(content)==158 and len(internal)==157
whitelist=json.loads(content[prefix+'/FILE_WHITELIST.json']);assert set(whitelist['files'])==set(internal)
assert all(not set(x.lower() for x in PurePosixPath(n).parts)&{'runtime','runtime_revision2_intermediate','home','cache','__pycache__','.godot','.aws','.ssh','.codex','sessions','cookies','chats','messages'} for n in content)
pkg=OUT/'extracted'/prefix
for name,data in content.items():p=OUT/'extracted'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
sr=subprocess.run([sys.executable,'-B',str(pkg/'verify_candidate.py')],capture_output=True,text=True,check=True);static=json.loads(sr.stdout);assert static['checks']==83 and static==json.loads(content[prefix+'/STATIC_VERIFICATION.json'])
dump(OUT/'STATIC_EVIDENCE_VERIFICATION.json',static)
print('PASS: fresh batch13 archive, 21 parts, 158 members, exact whitelist, 157 internal entries, 83 read-only checks',flush=True)
dep=m['dependencies']['source_baseline'];dd=OUT/'source_baseline'
mb=fetch(dep['commit'],dep['folder'],'MANIFEST.json',dd/'MANIFEST.json');assert meta(mb)['sha256']==dep['manifest_sha256'];dm=json.loads(mb)
parts=batch(dep['commit'],dep['folder'],dm['parts'],dd);db=b''.join(parts);assert meta(db)=={k:dm[k] for k in ['bytes','sha256']} and meta(db)['sha256']==dep['archive_sha256'];(dd/dm['archive']).write_bytes(db)
dp=dm['archive'].removesuffix('.tar.xz');dc=archive_content(db,dp,dm['files']);di=json.loads(dc[dp+'/FILE_MANIFEST.json'])
assert {dp+'/'+n:v for n,v in di.items()}=={n:meta(v) for n,v in dc.items() if n!=dp+'/FILE_MANIFEST.json'}
assert len(dc)==274 and len(di)==273 and set(json.loads(dc[dp+'/FILE_WHITELIST.json'])['files'])==set(di)
basebytes=content[prefix+'/BASE_MAP.json'];assert dc[dp+'/SOURCE_MAP.json']==basebytes and meta(basebytes)['sha256']==dep['source_map_sha256']
dep_receipt=json.loads(fetch(dep['commit'],dep['folder'],'REMOTE_STREAM_VERIFIED.json',dd/'REMOTE_STREAM_VERIFIED.json'));assert dep_receipt['candidate_source_map_sha256']==dep['source_map_sha256'] and dep_receipt['remaining_reference_gaps_within_original_scope']==348 and not dep_receipt['full_game_verified']
dpkg=OUT/'extracted_dependency'/dp
for name,data in dc.items():p=OUT/'extracted_dependency'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
dr=subprocess.run([sys.executable,'-B',str(dpkg/'verify_candidate.py')],capture_output=True,text=True,check=True);dstatic=json.loads(dr.stdout);assert dstatic['checks']==175;dump(OUT/'DEPENDENCY_STATIC_VERIFICATION.json',dstatic)
print('PASS: fresh fixed batch12 source dependency, 6 parts, 274 members, 175 read-only checks; exact BASE_MAP continuity',flush=True)
base=json.loads(basebytes);target=json.loads(content[prefix+'/SOURCE_MAP.json']);changes=json.loads(content[prefix+'/CHANGES.json']);added=changes['added'];name='tools/native_bolvar_shield_patterns.py'
assert added==[name] and changes['modified']==changes['removed']==[] and set(target)-set(base)=={name}
delta={n:meta(content[prefix+'/delta/'+n]) for n in added};assert {**base,**delta}==target and sum(x['bytes'] for x in delta.values())==17277
assert len(base)==27917 and len(target)==27918 and sum(v['bytes'] for v in target.values())==1549299108
actual=set()
for p in BASE.rglob('*'):
 assert not p.is_symlink(),str(p)
 if p.is_file():actual.add(p.relative_to(BASE).as_posix())
assert actual==set(base)
for n in target:
 p=PurePosixPath(n);assert not p.is_absolute() and '..' not in p.parts
# Existing historical baseline is reused; each actual file is hashed below, not called a fresh chain rebuild.
inputs=json.loads(content[prefix+'/review/SOURCE_INPUT_MAP.json']);assert len(inputs)==25
for rel,record in inputs.items():
 captured=content[prefix+'/review/source_inputs/'+rel]
 assert meta(captured)==record==base[rel] and captured==(BASE/rel).read_bytes()
# Pin both initial inputs directly to the freshly downloaded fixed batch12 package.
historical=content[prefix+'/review/historical/'+name];numeric=content[prefix+'/review/numeric_only/'+name]
assert historical==dc[dp+'/correction_review/originals/'+name] and numeric==dc[dp+'/correction_review/proposed/'+name]
assert meta(historical)=={'bytes':10524,'sha256':'68c4b12f8940d0458c151a638f3597538225d99bebd22ffffbb34a2d3d6d4a4c'}
assert meta(numeric)=={'bytes':10843,'sha256':'11781f8b74063d52aa777ea630867016f2ce8916bd38337c1b0243667ac716c9'}
links=json.loads(content[prefix+'/review/PRIOR_HISTORICAL_VERSION_LINKS.json']);link=next(x for x in links if x['target']==name)
pin=dc[dp+'/historical_inputs/'+link['independent_manifest_path']]
assert meta(pin)['sha256']==link['independent_manifest_sha256'] and json.loads(pin)[link['field']][name]==meta(historical)['sha256']
assert pin==(BASE/link['independent_manifest_path']).read_bytes()
assert content[prefix+'/review/PRIOR_TYPED_ORACLE.json']==dc[dp+'/typed_numeric_probe/before/report.json']
ledger=json.loads(content[prefix+'/review/FINAL_VERSION_LEDGER.json']);assert ledger['prior_fixed_backup']==dep['commit']
versions={v['label']:content[prefix+'/review/'+v['label']+'/'+name] for v in ledger['versions']}
for v in ledger['versions']:assert meta(versions[v['label']])=={'bytes':v['bytes'],'sha256':v['sha256']}
# Direct supplied replay reconstructs final V3 from preserved historical bytes only, not through module execution.
reconstruction=OUT/'reconstructed_final_review'
pr=subprocess.run([sys.executable,'-B',str(pkg/'apply_review_patch_to_new.py'),str(reconstruction)],capture_output=True,text=True,check=True)
(OUT/'NEW_PATCH_REPLAY.log').write_text(pr.stdout);patchreport=json.loads((reconstruction/'REPLAY.json').read_text());assert patchreport['status']=='PASS_ZERO_FUZZ_ZERO_OFFSET_NEW_CORRECTION_PATCH'
assert (reconstruction/name).read_bytes()==versions['revision3']==content[prefix+'/delta/'+name]
# Every preserved patch edge must reproduce exact version bytes in both directions.
edges=[('historical','numeric_only'),('numeric_only','initial'),('initial','revision2'),('historical','revision2'),('historical','revision3'),('numeric_only','revision3'),('revision2','revision3')]
edge_results=[]
for before,after in edges:
 edge=before+'_to_'+after;root=OUT/'patch_edges'/edge;p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(versions[before]);patch=content[prefix+'/review/'+edge+'.patch']
 for reverse,wanted in [(False,after),(True,before),(False,after)]:
  cmd=['patch','--batch','--fuzz=0','-p1','-d',str(root),'--reverse' if reverse else '--forward'];proc=subprocess.run(cmd,input=patch,capture_output=True,timeout=15)
  assert proc.returncode==0 and not any(x in proc.stdout.lower() for x in [b'offset',b'fuzz',b'failed']),proc.stdout
  assert p.read_bytes()==versions[wanted]
 edge_results.append({'from':before,'to':after,'patch_sha256':meta(patch)['sha256'],'forward_reverse_forward_exact':True,'zero_fuzz':True,'zero_offset':True})
remaining=json.loads(content[prefix+'/REMAINING_SCOPE.json']);assert remaining['remaining_original_scope']==347 and len(remaining['remaining_targets'])==347 and all(n not in target for n in remaining['remaining_targets'])
print('PASS: 25 actual baseline inputs, fixed historical/numeric originals, all 7 patch edges exact forward/reverse/forward; final V3 only',flush=True)
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
assert rebuilt==target and baseaggregate.hexdigest()=='c7698b11fbc7045b82ce0f7f096d3417b31d5984b6a6ec5236de74cc8034aff9'
assert aggregate.hexdigest()=='fefcdb171d91f8101f743848cf4266925004991e66c32d513493cc4abad6e57c'
sourcebytes=(json.dumps(rebuilt,sort_keys=True,indent=2)+'\n').encode();assert sourcebytes==content[prefix+'/SOURCE_MAP.json'];(OUT/'REBUILT_SOURCE_MAP.json').write_bytes(sourcebytes)
for n,v in base.items():assert filemeta(BASE/n)==v,n
assert {p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()}==set(base)
print('PASS: 27,918 candidate files streamed, 1,549,299,108 bytes; 27,917 baseline files rehashed twice unchanged',flush=True)
report={'status':'PASS_FRESH_BATCH13_BOUNDED_BOLVAR_CORRECTION_STREAM_RECONSTRUCTION','archive_commit':COMMIT,'folder':PLAN['folder'],'published_files_freshly_downloaded':len(PLAN['files']),'archive':m['archive'],**meta(b),'archive_parts_verified':len(m['parts']),'archive_members_verified':len(content),'internal_manifest_entries_verified':len(internal),'exact_whitelist_verified':True,'read_only_evidence_checks':83,'source_baseline_commit':dep['commit'],'source_baseline_archive_freshly_downloaded':True,'source_baseline_archive_sha256':meta(db)['sha256'],'source_baseline_archive_parts_verified':len(dm['parts']),'source_baseline_archive_members_verified':len(dc),'source_baseline_archive_internal_entries_verified':len(di),'source_baseline_read_only_checks':175,'historical_baseline_tree_reused':True,'historical_chain_freshly_downloaded':False,'historical_chain_rerun':False,'official_original_zip_rehashed_this_run':False,'captured_source_inputs_verified_against_actual_baseline':len(inputs),'historical_and_numeric_only_bytes_match_fixed_dependency':True,'prior_numeric_oracle_bytes_match_fixed_dependency':True,'patch_edges_checked':edge_results,'historical_generators_executed':False,'candidate_modules_executed':False,'new_differential_and_full_current_source_tests_rerun':False,'tested_interpreter':'CPython 3.12.14','backup_verifier_interpreter':sys.version,'stable_seekable_regular_files_required':True,'arbitrarily_huge_values_bounded_memory_guaranteed':False,'atomic_snapshot_under_concurrent_mutation_guaranteed':False,'exact_error_text_position_or_traceback_guaranteed':False,'historical_original_full_current_source_success_claimed':False,'Bolvar_golden_hold_retained':True,'normal_partial_and_non_default_pool_limits_retained':True,'baseline_files_rehashed_twice':len(base),'baseline_bytes':sum(v['bytes'] for v in base.values()),'candidate_files_rebuilt_as_actual_byte_stream':len(rebuilt),'candidate_bytes':sum(v['bytes'] for v in rebuilt.values()),'candidate_source_map_sha256':meta(sourcebytes)['sha256'],'candidate_source_aggregate_sha256':aggregate.hexdigest(),'source_changes':changes,'runtime_source_changes':1,'historical_originals_restored_this_batch':0,'remaining_reference_gaps_within_original_scope':347,'assertions_enabled_required':True,'assertions_enabled_during_verification':not sys.flags.optimize and __debug__,'full_runtime_directory_created_by_backup_verifier':False,'full_static_dependency_audit_rerun':False,'all_historical_searches_rerun':False,'gameplay_rerun':False,'Godot_rerun':False,'full_compiler_executed':False,'full_game_verified':False,'full_catalog_verified':False,'old_save_compatibility_verified':False,'latest_versions_proven':False,'historical_baseline_unchanged':True,'all_prior_backups_preserved':True,'missing_source_files':[],'mismatched_source_files':[],'unexpected_source_files':[],'downloads':sorted(downloads,key=lambda x:x['url']),'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
dump(OUT/'REMOTE_STREAM_VERIFIED.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='downloads'},indent=2),flush=True)
