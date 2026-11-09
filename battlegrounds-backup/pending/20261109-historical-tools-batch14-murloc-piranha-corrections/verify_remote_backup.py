from pathlib import Path,PurePosixPath
import argparse,json,hashlib,tarfile,io,urllib.request,time,concurrent.futures,datetime,subprocess,zipfile,re,sys,os,threading
if sys.flags.optimize or not __debug__ or os.environ.get("PYTHONOPTIMIZE", "") not in ("", "0"):
 raise RuntimeError("Python assertions are required. Do not use -O, -OO, or nonzero PYTHONOPTIMIZE.")
assert sys.implementation.name=='cpython' and sys.version_info[:3]==(3,12,14), 'Use tested CPython 3.12.14 or validate interpreter behavior separately.'
PLAN = {'folder': 'battlegrounds-backup/pending/20261109-historical-tools-batch14-murloc-piranha-corrections', 'branch': 'battlegrounds-recovery-20261103', 'parent': 'c2338eec7c0fc95a01614bdfdb85e7efe6a16602', 'tree': '0061b73d4de28051129dfe3f31da46359bd8dfd1', 'files': [{'name': 'CHANGES.json', 'bytes': 138, 'sha256': 'a4bbf2931b712f5b8f0fdff626b794a536b4e87f5166b868b44274e4354567f1', 'git_sha': 'e4cc79ea674872d93eaf797b9fafc1b24f011091'}, {'name': 'CURRENT_DEPENDENCY_STATUS.json', 'bytes': 978, 'sha256': 'bbf7c5a09d99ed924fe4a88b3c6fb603bb6617c4d7b096fadc8b54c66e73c05c', 'git_sha': 'de817295b6772b8572d53090e70e0e65a41166de'}, {'name': 'DEPENDENCIES.json', 'bytes': 636, 'sha256': 'a975cce2f7459ad378ac0901360c749eda0ebef4945c44eae746ba38ae4227d8', 'git_sha': 'a1f2414cdb7fe7cca73d095b75d4b59e8d1fbe0d'}, {'name': 'MANIFEST.json', 'bytes': 95918, 'sha256': '1a8c1eca5dcea9fd1426442b5b759c5736ae105c49e95e4a71fae100a6830bcc', 'git_sha': '68bf6a4f49716f6bf1bfccdcbb47c0e4cb39032e'}, {'name': 'PACKAGE_VERIFIED.json', 'bytes': 1014, 'sha256': '8a7f4f9d64e8698bb315b8c5e8bd386ead45fa7910df9c4a7ce3d94b0d328778', 'git_sha': '059e65b855dc862f0af23ad81a1bc0f833dfee99'}, {'name': 'README.md', 'bytes': 5779, 'sha256': '04892e87e981cc587851258003190190c568b5d9639c5840b7b90cc3650268b4', 'git_sha': '993e147e4746e84887be23120420cad2c6573034'}, {'name': 'RECOVERY.md', 'bytes': 2405, 'sha256': 'fa6bef84bfd81f0b6dfa27c3f1ba3bfc9de5a3e4623afe1c0c0551b77ad3bf61', 'git_sha': 'd96e07a273d0bff7f56566821a8ce86c13646dce'}, {'name': 'REMAINING_SCOPE.json', 'bytes': 15391, 'sha256': '2c205aa8daf5b56693698fad4999d7b0e73e34fb339bcc371fe64bb91e3f73ff', 'git_sha': '7ea589d7a5fd1ab3579b4324a2de0dc91005246c'}, {'name': 'REMOVALS.json', 'bytes': 3, 'sha256': '37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570', 'git_sha': 'fe51488c7066f6687ef680d6bfaa4f7768ef205c'}, {'name': 'SHA256SUMS.txt', 'bytes': 1696, 'sha256': '3409485511972e20a9d404f00829b7698c3e48bec6884ec247eeef0802638167', 'git_sha': '927a2b9a624a7f02c53a71810958290e9fed0bb4'}, {'name': 'TESTS_VERIFIED.json', 'bytes': 2185, 'sha256': '75fac235b8a4b5a28c72191d7c63d2f1c3ac7364ebcd1d315a414d46637ec181', 'git_sha': 'cc06d51b2f0c8deff3299c325a8d6d53ba7dfc3d'}, {'name': 'historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz.part000', 'bytes': 250000, 'sha256': 'a4b200d7434ba8712f782ad33793b04e2c103c2a8fce17524c64a548a78ba856', 'git_sha': '8e8ed0d73290548e19d89b2c3b7edbb0e49d5a4e'}, {'name': 'historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz.part001', 'bytes': 250000, 'sha256': 'a03bb5db8d13b04aeb21eae07648bbcb4c8a3bbb0333b991d928b55d656829ed', 'git_sha': 'ab56ec6dca935e64fa80a2cd8e874fd1b870f734'}, {'name': 'historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz.part002', 'bytes': 250000, 'sha256': 'ae2b7e20ae0777bdc78313cde81efbe1a04412ffaf510bea3d61fa6707fbd2a5', 'git_sha': '7e7ee961d951ac84730a701d55b97cbd5336be11'}, {'name': 'historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz.part003', 'bytes': 250000, 'sha256': 'f7bf681652fe378cf48ba621ac818225c76f00e416dfb933facc75ba1880ce64', 'git_sha': '56aa2b4ef79042bd64fe0482f7d16e8127e26813'}, {'name': 'historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz.part004', 'bytes': 250000, 'sha256': '45ea942fcfa04d5d3597346a156c12a341c2818f7d27b7d08ede2e557a69195e', 'git_sha': '9b6b24f8aff60428e5d34b6eeafa01ba872e1065'}, {'name': 'historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz.part005', 'bytes': 250000, 'sha256': 'f8af88017a4c9bf1c29d94a8b9e953135849bf2179435f8dc84158be4273efdd', 'git_sha': 'ee85ad3d5028e26fa11570036be983abb0d9032b'}, {'name': 'historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz.part006', 'bytes': 250000, 'sha256': '8e208f1958b00dd7d68467e1691a1abe83202cd624be5f58a95cce67f3e8b4fb', 'git_sha': '204057ae405cb1163eafc2fd9fb3dff4e3e4f1ab'}, {'name': 'historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz.part007', 'bytes': 250000, 'sha256': 'fe6531bf0dcbe3ca723e9e9009931dd57fe99a472c63f465f1ff215df9b3de49', 'git_sha': 'e3d1f5f8100497c21d038025a895a49ea3e171be'}, {'name': 'historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz.part008', 'bytes': 250000, 'sha256': '3629eb8caf69796e8c37ab33e5c018901fd7fad408cf06e1c34a81f12d965292', 'git_sha': '2252a3de43a3794029259edcf49183ad0167c4c8'}, {'name': 'historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz.part009', 'bytes': 250000, 'sha256': '46cf30b6add38413b99ee415bdfff4e446f4c88adc84520a6af36e137bd5b8ac', 'git_sha': 'f245cd7a2185cb3cea1a49921c1feab14d86401c'}, {'name': 'historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz.part010', 'bytes': 89844, 'sha256': '61b1aeee00dc002e47c13f431b4a51350031a2e7be3fa25f68a0b4bcaba86bb1', 'git_sha': '25393d28181679a5c75f97194f8e5b3193dff873'}]}
COMMIT='b693f364abe88509ac0986529d8c2f82a41831fd'
REPO='https://raw.githubusercontent.com/Ethsigema/AI_text01/'
ap=argparse.ArgumentParser(description='Verify downloaded batch14 two new conditional corrections and fixed batch13 source dependency against exact existing source baseline; does not run game or create complete runtime directory.')
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
import ast
batch(COMMIT,PLAN['folder'],PLAN['files'],OUT/'batch14')
m=json.loads((OUT/'batch14/MANIFEST.json').read_text());b=b''.join((OUT/'batch14'/p['name']).read_bytes() for p in m['parts'])
assert meta(b)=={k:m[k] for k in ['bytes','sha256']};(OUT/'batch14'/m['archive']).write_bytes(b)
prefix=m['archive'].removesuffix('.tar.xz');content=archive_content(b,prefix,m['files']);internal=json.loads(content[prefix+'/FILE_MANIFEST.json'])
assert {prefix+'/'+n:v for n,v in internal.items()}=={n:meta(v) for n,v in content.items() if n!=prefix+'/FILE_MANIFEST.json'}
assert len(content)==395 and len(internal)==394 and set(json.loads(content[prefix+'/FILE_WHITELIST.json'])['files'])==set(internal)
assert all(not set(x.lower() for x in PurePosixPath(n).parts)&{'runtime','home','cache','__pycache__','.godot','.aws','.ssh','.codex','sessions','cookies','chats','messages'} for n in content)
pkg=OUT/'extracted'/prefix
for name,data in content.items():p=OUT/'extracted'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
sr=subprocess.run([sys.executable,'-B',str(pkg/'verify_candidate.py')],capture_output=True,text=True,check=True);static=json.loads(sr.stdout);assert static['checks']==350 and static==json.loads(content[prefix+'/STATIC_VERIFICATION.json']);dump(OUT/'STATIC_EVIDENCE_VERIFICATION.json',static)
print('PASS: fresh batch14 archive, 11 parts, 395 members, exact whitelist, 394 internal entries, 350 read-only checks',flush=True)
dep=m['dependencies']['source_baseline'];dd=OUT/'source_baseline'
mb=fetch(dep['commit'],dep['folder'],'MANIFEST.json',dd/'MANIFEST.json');assert meta(mb)['sha256']==dep['manifest_sha256'];dm=json.loads(mb)
parts=batch(dep['commit'],dep['folder'],dm['parts'],dd);db=b''.join(parts);assert meta(db)=={k:dm[k] for k in ['bytes','sha256']} and meta(db)['sha256']==dep['archive_sha256'];(dd/dm['archive']).write_bytes(db)
dp=dm['archive'].removesuffix('.tar.xz');dc=archive_content(db,dp,dm['files']);di=json.loads(dc[dp+'/FILE_MANIFEST.json'])
assert {dp+'/'+n:v for n,v in di.items()}=={n:meta(v) for n,v in dc.items() if n!=dp+'/FILE_MANIFEST.json'}
assert len(dc)==158 and len(di)==157 and set(json.loads(dc[dp+'/FILE_WHITELIST.json'])['files'])==set(di)
basebytes=content[prefix+'/BASE_MAP.json'];assert dc[dp+'/SOURCE_MAP.json']==basebytes and meta(basebytes)['sha256']==dep['source_map_sha256']
dep_receipt=json.loads(fetch(dep['commit'],dep['folder'],'REMOTE_STREAM_VERIFIED.json',dd/'REMOTE_STREAM_VERIFIED.json'));assert dep_receipt['candidate_source_map_sha256']==dep['source_map_sha256'] and dep_receipt['remaining_reference_gaps_within_original_scope']==347 and not dep_receipt['full_game_verified']
dpkg=OUT/'extracted_dependency'/dp
for name,data in dc.items():p=OUT/'extracted_dependency'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
dr=subprocess.run([sys.executable,'-B',str(dpkg/'verify_candidate.py')],capture_output=True,text=True,check=True);dstatic=json.loads(dr.stdout);assert dstatic['checks']==83;dump(OUT/'DEPENDENCY_STATIC_VERIFICATION.json',dstatic)
print('PASS: fresh fixed batch13 dependency, 21 parts, 158 members, 83 read-only checks; exact BASE_MAP continuity',flush=True)
base=json.loads(basebytes);target=json.loads(content[prefix+'/SOURCE_MAP.json']);changes=json.loads(content[prefix+'/CHANGES.json']);added=changes['added'];expected=['tools/hand_murloc_gain_patterns.py','tools/piranha_vacancy_patterns.py']
assert added==expected and changes['modified']==changes['removed']==[] and set(target)-set(base)==set(added)
delta={n:meta(content[prefix+'/delta/'+n]) for n in added};assert {**base,**delta}==target and sum(x['bytes'] for x in delta.values())==41298
assert len(base)==27918 and len(target)==27920 and sum(v['bytes'] for v in target.values())==1549340406
actual=set()
for p in BASE.rglob('*'):
 assert not p.is_symlink(),str(p)
 if p.is_file():actual.add(p.relative_to(BASE).as_posix())
assert actual==set(base)
for n in target:
 p=PurePosixPath(n);assert not p.is_absolute() and '..' not in p.parts
inputs=json.loads(content[prefix+'/review/SOURCE_MAP.json']);assert len(inputs)==12
for rel,record in inputs.items():assert meta(content[prefix+'/review/source_inputs/'+rel])==record==base[rel] and content[prefix+'/review/source_inputs/'+rel]==(BASE/rel).read_bytes()
comparatorbytes=content[prefix+'/review/source_inputs/tools/native_bolvar_shield_patterns.py'];assert comparatorbytes==dc[dp+'/delta/tools/native_bolvar_shield_patterns.py']
comparator=comparatorbytes.decode();same_node=next(n for n in ast.parse(comparator).body if isinstance(n,ast.FunctionDef) and n.name=='same');same_source=ast.get_source_segment(comparator,same_node)+'\n'
assert same_source.encode()==content[prefix+'/review/evidence/batch13_same.py.txt']
assert content[prefix+'/review/evidence/PRIOR_TYPED_ORACLE.json']==dc[dp+'/review/PRIOR_TYPED_ORACLE.json']
reconstruction=OUT/'reconstructed_new_review';records=json.loads(content[prefix+'/review/RECONSTRUCTION_AND_AST.json'])
assert records['fixed_backup']==dep['commit'] and not records['historical_generators_executed']
entries={x['target']:x for x in json.loads(content[prefix+'/review/evidence/FOUR_ADDITIONAL_PAYLOADS.json']) if x['target'] in added};patch_results=[]
def literal_assignment(tree,name):
 return ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets)))
# Read only literal IDs and fixed raw/expected JSON. Do not import or execute generators or candidate modules.
for rec in records['records']:
 name=rec['target'];entry=entries[name]
 for rel,record in entry['inputs'].items():assert meta(content[prefix+'/review/source_inputs/'+rel])=={k:record[k] for k in ['bytes','sha256']}
 tree=ast.parse(content[prefix+'/review/source_inputs/'+entry['generator']]);research=str(PurePosixPath(entry['generator']).parent)
 raw=json.loads(content[prefix+'/review/source_inputs/'+research+'/raw_rows.json']);expectedrows=json.loads(content[prefix+'/review/source_inputs/'+research+'/expected_compiled.json'])
 if 'hand_murloc' in name:
  ids=literal_assignment(tree,'ids');assert ids==['BG34_Giant_801','BG34_Giant_801_G']
  original='"""Exact independently sourced Timewarped Astrogill pair."""\nfrom copy import deepcopy\n'+'SOURCE_IDS = '+repr(tuple(ids))+'\nRAW = '+repr(raw)+'\nEXPECTED = '+repr(expectedrows)+'\n';dependency_name='SOURCE_IDS'
 else:
  ids=literal_assignment(tree,'IDS');child=literal_assignment(tree,'CHILD');assert ids==['BG32_201','BG32_201_G'] and child=='BG32_201t'
  original='"""Exact whole native Snapper programs. No inferred golden/token or generic fallback."""\nfrom copy import deepcopy\n'
  for k,v in [('SOURCE_IDS',ids),('ALL_IDS',ids+[child]),('RAW',raw),('EXPECTED',expectedrows)]:original+=k+' = '+repr(v)+'\n'
  dependency_name='ALL_IDS'
 original+=('def compile_card(card, cards):\n'+'    if not isinstance(card, dict) or card.get("id") not in SOURCE_IDS:\n'+'        return None\n'+f'    if any(cards.get(identity) != RAW[identity] for identity in {dependency_name}):\n'+'        return None\n'+'    return deepcopy(EXPECTED[card["id"]])\n')
 original=original.encode();pins=json.loads(content[prefix+'/review/source_inputs/'+rec['independent_pin_file']]);assert meta(original)=={'bytes':rec['historical_bytes'],'sha256':rec['historical_sha256']} and meta(original)['sha256']==pins[name]==entry['independent_historical_output_sha256'] and original==content[prefix+'/review/original/'+name]
 p=reconstruction/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(original);patch=content[prefix+'/review/patches/'+PurePosixPath(name).name+'.patch'];proposal=content[prefix+'/review/new_proposal/'+name]
 for reverse,wanted in [(False,proposal),(True,original),(False,proposal)]:
  proc=subprocess.run(['patch','--batch','--fuzz=0','-p1','-d',str(reconstruction),'--reverse' if reverse else '--forward'],input=patch,capture_output=True,timeout=15)
  assert proc.returncode==0 and not any(x in proc.stdout.lower() for x in [b'offset',b'fuzz',b'failed']),proc.stdout
  assert p.read_bytes()==wanted
 assert proposal==content[prefix+'/delta/'+name] and meta(proposal)==target[name]
 proposal_ast=ast.parse(proposal);assert ast.dump(next(n for n in proposal_ast.body if isinstance(n,ast.FunctionDef) and n.name=='same'))==ast.dump(same_node)
 patch_results.append({'target':name,'historical':meta(original),'new_correction':meta(proposal),'patch_sha256':meta(patch)['sha256'],'independent_historical_pin_match':True,'forward_reverse_forward_exact':True,'zero_fuzz':True,'zero_offset':True})
status=json.loads(content[prefix+'/CURRENT_DEPENDENCY_STATUS.json']);missing=[status['remaining_missing_Piranha_declared_path'],status['missing_hand_historical_contract'],status['aggregate_origin_XML_missing'],status['full_compiler_driver_missing']]
assert all(n not in base and n not in target and not (BASE/n).exists() for n in missing)
assert status['both_contracts_are_not_allowed_omissions'] and not status['documents_fabricated_or_new_exemptions'] and not status['full_runtime_dependency_closure_accepted'] and status['hand_current_host_differs_historical_pin']
assert status['remaining_missing_Piranha_declared_path'] in content[prefix+'/review/source_inputs/core/piranha_vacancy_sources.gd'].decode()
supplement=json.loads(content[prefix+'/source_audit/PROOF_SUPPLEMENT.json'])
for n,record in supplement['current_hosts'].items():assert filemeta(BASE/n)['sha256']==record['sha256']==base[n]['sha256']
hand=supplement['current_hosts']['core/hand_murloc_gain_host.gd'];assert hand['sha256']!=hand['historical_pin'] and not hand['matches_historical_new_files_pin']
remaining=json.loads(content[prefix+'/REMAINING_SCOPE.json']);assert remaining['remaining_original_scope']==345 and len(remaining['remaining_targets'])==345 and all(n not in target for n in remaining['remaining_targets'])
print('PASS: 12 actual baseline inputs, two historical AST/literal reconstructions and strict patch round trips; missing contracts and host difference retained',flush=True)
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
assert rebuilt==target and baseaggregate.hexdigest()=='fefcdb171d91f8101f743848cf4266925004991e66c32d513493cc4abad6e57c'
assert aggregate.hexdigest()=='5ba04ef124fc78cf20e2a942a60589fb92dc76e6808155648226a534a4599e05'
sourcebytes=(json.dumps(rebuilt,sort_keys=True,indent=2)+'\n').encode();assert sourcebytes==content[prefix+'/SOURCE_MAP.json'];(OUT/'REBUILT_SOURCE_MAP.json').write_bytes(sourcebytes)
for n,v in base.items():assert filemeta(BASE/n)==v,n
assert {p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()}==set(base)
print('PASS: 27,920 candidate files streamed, 1,549,340,406 bytes; 27,918 baseline files rehashed twice unchanged',flush=True)
report={'status':'PASS_FRESH_BATCH14_TWO_CONDITIONAL_CORRECTIONS_STREAM_RECONSTRUCTION','archive_commit':COMMIT,'folder':PLAN['folder'],'published_files_freshly_downloaded':len(PLAN['files']),'archive':m['archive'],**meta(b),'archive_parts_verified':len(m['parts']),'archive_members_verified':len(content),'internal_manifest_entries_verified':len(internal),'exact_whitelist_verified':True,'read_only_evidence_checks':350,'source_baseline_commit':dep['commit'],'source_baseline_archive_freshly_downloaded':True,'source_baseline_archive_sha256':meta(db)['sha256'],'source_baseline_archive_parts_verified':len(dm['parts']),'source_baseline_archive_members_verified':len(dc),'source_baseline_archive_internal_entries_verified':len(di),'source_baseline_read_only_checks':83,'historical_baseline_tree_reused':True,'historical_chain_freshly_downloaded':False,'historical_chain_rerun':False,'official_original_zip_rehashed_this_run':False,'captured_source_inputs_verified_against_actual_baseline':len(inputs),'historical_literal_reconstructions_and_new_patch_results':patch_results,'comparator_and_prior_numeric_oracle_match_fixed_dependency':True,'historical_generators_executed':False,'candidate_modules_executed':False,'dynamic_python_or_Godot_tests_rerun':False,'tested_interpreter':'CPython 3.12.14','backup_verifier_interpreter':sys.version,'finite_acyclic_JSON_shaped_values_only':True,'missing_contracts_and_other_fixed_inputs':missing,'missing_Piranha_contract_still_declared':True,'contracts_newly_exempted':False,'hand_current_host_differs_historical_pin':True,'hosts_executed':False,'complete_runtime_dependency_closure_accepted':False,'Bolvar_golden_hold_retained':True,'baseline_files_rehashed_twice':len(base),'baseline_bytes':sum(v['bytes'] for v in base.values()),'candidate_files_rebuilt_as_actual_byte_stream':len(rebuilt),'candidate_bytes':sum(v['bytes'] for v in rebuilt.values()),'candidate_source_map_sha256':meta(sourcebytes)['sha256'],'candidate_source_aggregate_sha256':aggregate.hexdigest(),'source_changes':changes,'runtime_source_changes':2,'historical_originals_restored_this_batch':0,'remaining_reference_gaps_within_original_scope':345,'assertions_enabled_required':True,'assertions_enabled_during_verification':not sys.flags.optimize and __debug__,'full_runtime_directory_created_by_backup_verifier':False,'full_static_dependency_audit_rerun':False,'all_historical_searches_rerun':False,'gameplay_rerun':False,'Godot_rerun':False,'full_compiler_executed':False,'full_game_verified':False,'full_catalog_verified':False,'old_save_compatibility_verified':False,'latest_versions_proven':False,'historical_baseline_unchanged':True,'all_prior_backups_preserved':True,'missing_source_files':[],'mismatched_source_files':[],'unexpected_source_files':[],'downloads':sorted(downloads,key=lambda x:x['url']),'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
dump(OUT/'REMOTE_STREAM_VERIFIED.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='downloads'},indent=2),flush=True)
