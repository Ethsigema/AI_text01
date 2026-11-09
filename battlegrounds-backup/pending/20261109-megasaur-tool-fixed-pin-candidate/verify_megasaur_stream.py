#!/usr/bin/env python3
"""Verify pinned Megasaur fixed-pin historical tool bytes by streaming actual target files.
Reuses a verified Harbinger full tree and four pinned historical archives.
Default downloads use immutable GitHub URLs. No full runtime tree, no gameplay,
no old-save acceptance, no claim that source-map equality resolves all references.
"""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,tarfile,os,io,gc,re,ast,datetime,shutil,urllib.request
COMMIT='a00e227da42ecf4563c324e7994ecf9c5a63dde8'
REPO_PATH='battlegrounds-backup/pending/20261109-megasaur-tool-fixed-pin-candidate'
BASE_URL=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{COMMIT}/{REPO_PATH}/'
PACKAGE='megasaur_tool_fixed_pin_candidate_20261109'
ARCHIVE_SHA='27514275c7204a972de2a5193b93deb35c7d4a72b137d1bc5c9477c2f7e9cf66'
MANIFEST_SHA='b79689ba046d94fc59f08b8c870cde67e0ed46fe1d3dbf32b0f103db7f78b370'
BASE_MAP_SHA='bfd5d82ede8559200aed89547e4584ac091873a9392079af5ee20c41ea764a0a'
TARGET_MAP_SHA='28b1d1c523dfc566bc5eacd04ccea1e1787c1b15e0cca8f9e67ecf9229b46bf4'
BASE_COMMIT='9b60cad21ed6dc06d2b4c8f67a36f8c88ab92290'
BASE_URL_PRIOR=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{BASE_COMMIT}/battlegrounds-backup/pending/20261109-golden-arrow-tool-patch-reconstruction-candidate/'
BASE_MANIFEST_SHA='a5016309666174b5a84523f5760f50b530110d8ce6f6dcdb1012c0f614af1a94'
BASE_RECEIPT_SHA='088ba4a90cda426adf92be1af7516689511e08f6ce3c1d40f5225589022ba862'
STATUS='SCOPED_SINGLE_FILE_FIXED_PIN_RESTORATION_CANDIDATE_VERIFIED'
LAYERS=[
 ('native_listener','native_spell_listener_leaf_partial_candidate_20261109','46ceb12b81c5db0c417933482d6572f3c89693d2ba3ef2d507ccebc5f0ed4ec7','e31eb74faca1a774b42a7c8bcef11b1592eae64ad350b08fa930f9a1d7cd64fe','9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111',247,5),
 ('earth_mother','earth_mother_helper_leaf_partial_candidate_20261109','333aad27ba8ed0d0699c97cd4a33be5494310247a8350993532cd725f26e753c','9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111','d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960',79,4),
 ('golden_source','native_golden_source_leaf_partial_candidate_20261109','181a6415d954795e0b40286165c39a55d0469745185e7e6d24840eb769025cef','d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960','c0454c30ce7eb2a71fb8ea3e513f0db0d2fd684f63129a1b7da2e4a47666603b',71,3),
 ('golden_tool','golden_arrow_tool_patch_reconstruction_candidate_20261109','3122135a4912a58c361b522e67b946dffbbe29b3618051972a4898e8cac7edd9','c0454c30ce7eb2a71fb8ea3e513f0db0d2fd684f63129a1b7da2e4a47666603b',BASE_MAP_SHA,98,1)]

def require(ok,message):
 if not ok: raise ValueError(message)
def sha(b):return hashlib.sha256(b).hexdigest()
def meta(b):return {'bytes':len(b),'sha256':sha(b)}
def safe(name):
 p=PurePosixPath(name);return bool(name) and not p.is_absolute() and '..' not in p.parts and '\\' not in name and str(p)==name

def file_meta(path):
 require(path.is_file() and not path.is_symlink(),'Not a regular file: '+str(path));digest=hashlib.sha256();count=0
 with path.open('rb') as h:
  for b in iter(lambda:h.read(1024*1024),b''):digest.update(b);count+=len(b)
 return {'bytes':count,'sha256':digest.hexdigest()}
def read_json(p):return json.loads(p.read_text())
def get(url,path):
 with urllib.request.urlopen(url,timeout=120) as r:path.write_bytes(r.read())
def check_tree(root,expected,label):
 require(root.is_dir() and not root.is_symlink(),'Invalid historical tree');count=0
 for folder,dirs,files in os.walk(root):
  folder=Path(folder)
  for name in dirs:require(not (folder/name).is_symlink(),'Historical directory symlink')
  for name in files:
   p=folder/name;rel=p.relative_to(root).as_posix();require(rel in expected and file_meta(p)==expected[rel],'Historical byte mismatch: '+rel);count+=1
 require(count==len(expected),'Historical file count mismatch');print('PASS:',label,count,'actual files',flush=True)

def archive_verify(path,expected_sha,root,external=None,extract=None):
 require(file_meta(path)['sha256']==expected_sha,'Archive hash mismatch: '+str(path));members={};keep={};internal=None
 with tarfile.open(path,'r:xz') as t:
  for m in t:
   require(m.isfile() and safe(m.name) and m.name.startswith(root+'/') and m.name not in members,'Unsafe/duplicate archive member')
   retain=m.name.startswith(root+'/delta/') or m.name in [root+'/'+n for n in ['BASE_MAP.json','SOURCE_MAP.json','PACKAGE_MANIFEST.json','REMOVALS.json']]
   if extract:
    dst=extract/m.name;dst.parent.mkdir(parents=True,exist_ok=True);writer=dst.open('xb')
   else:writer=None
   digest=hashlib.sha256();count=0;chunks=[]
   with t.extractfile(m) as h:
    for b in iter(lambda:h.read(1024*1024),b''):
     digest.update(b);count+=len(b)
     if retain and not extract:chunks.append(b)
     if writer:writer.write(b)
   if writer:writer.close()
   members[m.name]={'bytes':count,'sha256':digest.hexdigest()}
   if retain:
    body=(extract/m.name).read_bytes() if extract else b''.join(chunks)
    if m.name==root+'/PACKAGE_MANIFEST.json':internal=json.loads(body)
    elif m.name==root+'/REMOVALS.json':require(json.loads(body)==[],'Unexpected deletion')
    elif not extract:keep[m.name.removeprefix(root+'/')]=body
 if external is not None:require(members==external['files'],'External member manifest mismatch')
 require(internal=={n.removeprefix(root+'/'):v for n,v in members.items() if n!=root+'/PACKAGE_MANIFEST.json'},'Internal manifest mismatch')
 print('PASS: archive',root,len(members),'members',flush=True);return members,keep

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--historical-baseline',type=Path,required=True)
 for name in ['native-archive','earth-archive','golden-archive','golden-tool-archive']:p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--download-dir',type=Path);p.add_argument('--baseline-receipt',type=Path);p.add_argument('--baseline-manifest',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 out=a.output.resolve();baseline=a.historical_baseline.resolve();require(not out.exists() and baseline not in out.parents,'Output must be new and outside baseline');out.mkdir(parents=True);free_before=shutil.disk_usage(out).free
 fresh=a.download_dir is None;d=a.download_dir.resolve() if a.download_dir else out/'downloaded'
 if fresh:d.mkdir();get(BASE_URL+'MANIFEST.json',d/'MANIFEST.json')
 require(file_meta(d/'MANIFEST.json')['sha256']==MANIFEST_SHA,'Pinned manifest mismatch');m=read_json(d/'MANIFEST.json');require(m['sha256']==ARCHIVE_SHA and m['bytes']==1490252 and len(m['files'])==143 and len(m['parts'])==6,'Package metadata mismatch')
 for name,expected in m['companion_files'].items():
  require(safe(name) and '/' not in name,'Unsafe companion')
  if fresh:get(BASE_URL+name,d/name)
  require(file_meta(d/name)==expected,'Companion mismatch')
 archive=out/m['archive'];require(safe(m['archive']) and '/' not in m['archive'],'Unsafe archive name')
 with archive.open('xb') as h:
  for part in m['parts']:
   name=part['name'];require(safe(name) and '/' not in name,'Unsafe part')
   if fresh:get(BASE_URL+name,d/name)
   require(file_meta(d/name)=={'bytes':part['bytes'],'sha256':part['sha256']},'Part mismatch');h.write((d/name).read_bytes())
 require((d/'SHA256SUMS.txt').read_text().strip()==ARCHIVE_SHA+'  '+m['archive'],'Checksum file mismatch')
 members,_=archive_verify(archive,ARCHIVE_SHA,PACKAGE,m,out/'extracted');pkg=out/'extracted'/PACKAGE
 require(file_meta(pkg/'BASE_MAP.json')['sha256']==BASE_MAP_SHA and file_meta(pkg/'SOURCE_MAP.json')['sha256']==TARGET_MAP_SHA,'Source map hash mismatch')
 base=read_json(pkg/'BASE_MAP.json');target=read_json(pkg/'SOURCE_MAP.json');leaf='tools/megasaur_adapt_patterns.py';delta={n.removeprefix(PACKAGE+'/delta/'):v for n,v in members.items() if n.startswith(PACKAGE+'/delta/')};changes={'added':[leaf],'modified':[],'removed':[]}
 require(len(base)==27898 and len(target)==27899 and len(delta)==1 and leaf not in base and {**base,**delta}==target,'Not the exact one-file addition')
 require(sum(x['bytes'] for x in target.values())==1548785133 and delta[leaf]=={'bytes':32296,'sha256':'adf31c928468bb9be4dcca89bda2dd0096626dbbbc926dae639ce24bea23b1a2'},'Target size/hash mismatch')
 for n in target:require(safe(n),'Unsafe source path')
 require(read_json(d/'CHANGES.json')==changes and read_json(d/'REMOVALS.json')==m['removed_source_files']==[],'External change/removal mismatch')
 require(read_json(pkg/'CHANGES.json')==[{'path':leaf,'status':'added_byte_exact_current_fixed_pin_original','before':None,'after':delta[leaf]}],'Archived change record mismatch')
 result=read_json(pkg/'RESULT.json');require(result['status']==m['status']==STATUS and result['input_commit']==BASE_COMMIT and result['Godot_assertions_including_repeated_portability_runs']==546 and result['static_cross_checks']==55,'Candidate status mismatch')
 for key in ['other_68_restored','full_Catalog_loaded','full_Game_tested','old_save_compatibility_verified','offline_target_Python_executed','full_compiler_tested','gameplay_acceptance']:require(result[key] is False,'Missing scope limitation: '+key)
 require(result['remaining_missing_within_original_367_scope']==m['remaining_tools_reference_gaps_within_original_367']==366 and result['historical_original_byte_exact_not_patch_reconstruction'] is result['matches_current_explicit_fixed_pin'] is m['historical_original_matches_current_fixed_pin'] is True,'Historical original/pin boundary missing')
 for arg,name,urlname,expected in [(a.baseline_manifest,'PINNED_INPUT_MANIFEST.json','MANIFEST.json',BASE_MANIFEST_SHA),(a.baseline_receipt,'PINNED_INPUT_RECEIPT.json','TOOL_RECONSTRUCTION_STREAM_VERIFICATION.json',BASE_RECEIPT_SHA)]:
  dest=out/name
  if arg:dest.write_bytes(arg.read_bytes())
  else:get(BASE_URL_PRIOR+urlname,dest)
  require(file_meta(dest)['sha256']==expected,'Pinned dependency hash mismatch')
 dep=read_json(out/'PINNED_INPUT_MANIFEST.json');receipt=read_json(out/'PINNED_INPUT_RECEIPT.json')
 require(m['depends_on']['recovery_commit']==BASE_COMMIT and m['depends_on']['archive_sha256']==dep['sha256']==LAYERS[3][2] and m['depends_on']['manifest_sha256']==BASE_MANIFEST_SHA and m['depends_on']['receipt_sha256']==BASE_RECEIPT_SHA,'Dependency pointers mismatch')
 require(receipt['status']=='PASS_EXACT_STREAMED_SOURCE_MAP_BYTES_WITH_RECONSTRUCTED_TOOL_AND_REMAINING_REFERENCE_GAPS' and receipt['source_map_sha256']==BASE_MAP_SHA and receipt['historical_baseline_and_prior_archives_unchanged'] is True and receipt['full_game_validation_passed'] is False,'Pinned receipt scope mismatch')
 historical=None;composed=None;overlays={};origin_by_path={};prior_members=[]
 archives=[a.native_archive,a.earth_archive,a.golden_archive,a.golden_tool_archive]
 for index,(path,layer) in enumerate(zip(archives,LAYERS)):
  label,root,expected,bhash,thash,count,delta_count=layer
  oldmembers,keep=archive_verify(path,expected,root,dep if index==3 else None)
  require(len(oldmembers)==count and sha(keep['BASE_MAP.json'])==bhash and sha(keep['SOURCE_MAP.json'])==thash,'Prior archive map/count mismatch')
  oldbase=json.loads(keep.pop('BASE_MAP.json'));oldtarget=json.loads(keep.pop('SOURCE_MAP.json'))
  current_delta={n.removeprefix('delta/'):b for n,b in keep.items() if n.startswith('delta/')};require(len(current_delta)==delta_count,'Prior delta count mismatch')
  delta_meta={n:meta(b) for n,b in current_delta.items()};require({n:v for n,v in oldtarget.items() if oldbase.get(n)!=v}==delta_meta and {**oldbase,**delta_meta}==oldtarget,'Prior source delta/removal continuity mismatch')
  if historical is None:historical=oldbase;composed=dict(oldbase)
  require(composed==oldbase,'Adjacent archive map mismatch');composed.update(delta_meta);require(composed==oldtarget,'Layer composition mismatch')
  overlays.update(current_delta);origin_by_path.update({n:label for n in current_delta});prior_members.append({'archive':root+'.tar.xz','sha256':expected,'members_reverified':count,'source_files':delta_count,'freshly_downloaded_this_round':False})
  del oldbase,oldtarget,keep,current_delta,oldmembers,delta_meta;gc.collect()
 require(composed==base,'Four historical layers do not match direct input');del composed;gc.collect()
 check_tree(baseline,historical,'historical baseline before')
 def actual_bytes(name):return overlays[name] if name in overlays else (baseline/name).read_bytes()
 historical_path='research/megasaur_adapt_native_recovery/candidates/tools/megasaur_adapt_patterns.py';original=(pkg/'evidence/historical_original.py').read_bytes();restored=(pkg/'delta'/leaf).read_bytes()
 require(original==restored==actual_bytes(historical_path) and meta(original)==delta[leaf],'Restored tool differs from actual historical original');ast.parse(restored)
 provenance=read_json(pkg/'PROVENANCE.json')
 for name,expected in provenance['evidence_files'].items():
  require(safe(name),'Unsafe evidence source');evidence=(pkg/'evidence/historical'/name).read_bytes();require(meta(evidence)==expected and evidence==actual_bytes(name),'Historical supporting evidence mismatch: '+name)
 pin_source=actual_bytes('core/amalgadon_sources.gd');require(meta(pin_source)=={k:v for k,v in provenance['current_fixed_pin_source'].items() if k in ['bytes','sha256']},'Current fixed-pin source mismatch')
 require(pin_source==(pkg/'probe_inputs/core/amalgadon_sources.gd').read_bytes(),'Sealed probe source differs from actual source')
 pins=json.loads(re.search(rb'^const PROOF_SHA256[^=]*=(.*)$',pin_source,re.M)[1]);require(len(pins)==43 and pins[leaf]==sha(restored),'Target current fixed pin mismatch')
 before_pins=0;after_pins=0
 for name,expected in pins.items():
  require(safe(name),'Unsafe pin path')
  if name in base:require(sha(actual_bytes(name))==expected,'Other current pin mismatch');before_pins+=1
  after=restored if name==leaf else actual_bytes(name);require(sha(after)==expected,'Restored current pin mismatch');after_pins+=1
 require(before_pins==42 and after_pins==43,'Current fixed-pin counts mismatch')
 adapt=actual_bytes('core/megasaur_adapt_sources.gd');require(adapt==(pkg/'probe_inputs/core/megasaur_adapt_sources.gd').read_bytes(),'Delegated source changed');adapt_pins=json.loads(re.search(rb'^const PROOF_SHA256[^=]*=(.*)$',adapt,re.M)[1]);require(len(adapt_pins)==32,'Delegated pin count mismatch')
 for name,expected in adapt_pins.items():require(safe(name) and sha(restored if name==leaf else actual_bytes(name))==expected,'Delegated pin mismatch')
 creation=actual_bytes('research/megasaur_adapt_native_recovery/megasaur_adapt_candidates.patch');found=[]
 for section in re.split(r'(?=^--- )',creation.decode(),flags=re.M):
  lines=section.splitlines(True)
  if len(lines)>2 and lines[0].strip()=='--- /dev/null' and lines[1].strip() in ['+++ b/'+leaf,'+++ '+leaf]:
   require(sum(x.startswith('@@') for x in lines)==1,'Creation patch hunk count');head=re.fullmatch(r'@@ -0,0 \+1,(\d+) @@\n',lines[2]);require(head is not None and all(x.startswith('+') for x in lines[3:]) and len(lines[3:])==int(head[1]),'Creation patch format/count');found.append(''.join(x[1:] for x in lines[3:]).encode())
 require(found==[restored],'Historical creation patch does not exactly reproduce original')
 snapshot=read_json(pkg/'evidence/INVENTORY_SNAPSHOT_MAP.json');require(len(snapshot)==22,'Inventory snapshot count');snapshot_root=pkg/'evidence/tools_reference_inventory_20261109'
 for name,expected in snapshot.items():require(safe(name) and file_meta(snapshot_root/name)==expected,'Inventory snapshot mismatch')
 require(sorted(x.relative_to(snapshot_root).as_posix() for x in snapshot_root.rglob('*') if x.is_file())==sorted(snapshot),'Extra or missing inventory snapshot file')
 inv=read_json(snapshot_root/'FINAL_INVENTORY.json');require(len(inv)==367 and len({x['target'] for x in inv})==367 and all(not x['current_root_file_exists'] and x['target'] not in base for x in inv),'Original inventory before state mismatch')
 require(sum(x['target'] not in target for x in inv)==366 and 'tools/amalgadon_native_patterns.py' not in target,'Remaining gaps not preserved')
 print('PASS: exact historical original, creation patch, 43 current pins, 32 delegated pins and 22-file inventory; no Godot rerun',flush=True)
 origins={'historical_tree':0,'native_listener':0,'earth_mother':0,'golden_source':0,'golden_tool':0,'fresh_megasaur_tool':0};reconstructed={};aggregate=hashlib.sha256()
 for name in sorted(target):
  if name==leaf:h=(pkg/'delta'/leaf).open('rb');origin='fresh_megasaur_tool'
  elif name in overlays:h=io.BytesIO(overlays[name]);origin=origin_by_path[name]
  else:
   source=baseline/name;require(source.is_file() and not source.is_symlink(),'Invalid historical source');h=source.open('rb');origin='historical_tree'
  digest=hashlib.sha256();count=0;aggregate.update(name.encode()+b'\0'+str(target[name]['bytes']).encode()+b'\0')
  with h:
   for b in iter(lambda:h.read(1024*1024),b''):digest.update(b);aggregate.update(b);count+=len(b)
  reconstructed[name]={'bytes':count,'sha256':digest.hexdigest()};require(reconstructed[name]==target[name],'Streamed target mismatch: '+name);origins[origin]+=1
 require(reconstructed==target and origins=={'historical_tree':27885,'native_listener':5,'earth_mother':4,'golden_source':3,'golden_tool':1,'fresh_megasaur_tool':1},'Final map/origin mismatch')
 check_tree(baseline,historical,'historical baseline after')
 for path,layer in zip(archives,LAYERS):require(file_meta(path)['sha256']==layer[2],'Historical archive changed')
 (out/'STREAM_RECONSTRUCTED_SOURCE_MAP.json').write_text(json.dumps(reconstructed,indent=2,sort_keys=True)+'\n');require(file_meta(out/'STREAM_RECONSTRUCTED_SOURCE_MAP.json')['sha256']==TARGET_MAP_SHA,'Canonical target map bytes differ')
 r={'status':'PASS_EXACT_STREAMED_SOURCE_MAP_BYTES_WITH_FIXED_PIN_HISTORICAL_TOOL_AND_REMAINING_GAPS','candidate_status':STATUS,'archive_commit':COMMIT,'repository_path':REPO_PATH,'manifest_sha256':MANIFEST_SHA,'archive_sha256':ARCHIVE_SHA,'archive_bytes':1490252,'parts_verified':6,'members_verified':143,'internal_manifest_members_verified':142,'input_verified_commit':BASE_COMMIT,'input_manifest_sha256':BASE_MANIFEST_SHA,'input_receipt_sha256':BASE_RECEIPT_SHA,'input_source_map_sha256':BASE_MAP_SHA,'source_map_sha256':TARGET_MAP_SHA,'historical_full_tree_files_rehashed_before_and_after':len(historical),'historical_tree_source_map_sha256':LAYERS[0][3],'prior_archive_verifications':prior_members,'direct_input_files_verified_by_actual_bytes':len(base),'target_files_streamed_and_verified':len(target),'actual_target_bytes_streamed':sum(v['bytes'] for v in target.values()),'stream_source_origins':origins,'aggregate_stream_sha256':aggregate.hexdigest(),'aggregate_stream_format':'Sorted UTF-8 target path, NUL, ASCII file byte count, NUL, actual file bytes; repeated for every target file.','change_lists':changes,'historical_original_and_supporting_evidence_match_actual_baseline_bytes':True,'historical_creation_patch_reproduces_exact_original':True,'restored_python_ast_parse_passed':True,'restored_tool_sha256':sha(restored),'current_Amalgadon_fixed_pins':43,'before_existing_matching_pins':before_pins,'after_matching_pins':after_pins,'delegated_Megasaur_pins_verified':32,'current_pin_constants_unchanged':True,'inventory_snapshot_files_verified':22,'inventory_before_items_preserved':367,'remaining_missing_within_inventory_scope':366,'inventory_scan_repeated_this_round':False,'inventory_scope':'Sealed 367-item pre-restoration investigation preserved, not all possible tools gaps. Target-map comparison independently confirms one restored and 366 still absent.','other_68_historical_candidates_restored':False,'partial_validation_only':True,'full_game_validation_passed':False,'save_compatibility_verified':False,'full_catalog_fingerprint_executed':False,'full_compiler_executed':False,'gameplay_test_run_by_verifier':False,'Godot_proof_error_rerun_by_verifier':False,'whole_game_memory_improvement_verified':False,'complete_runtime_directory_created':False,'verification_mode':'Actual per-file bytes from reused Harbinger tree and four pinned archive layers, plus freshly downloaded Megasaur delta; not merely map comparison.','historical_chain_freshly_downloaded_this_round':False,'increment_downloaded_by_this_helper':fresh,'increment_input_mode':'fresh immutable URLs' if fresh else 'Separately fetched pinned bytes; see FETCH_PROVENANCE.json proving all six part objects absent before fetch.','historical_baseline_and_prior_archives_unchanged':True,'missing_files_relative_to_source_map':[],'mismatched_files_relative_to_source_map':[],'unexpected_files_relative_to_source_map':[],'source_map_equality_does_not_establish_complete_game_recovery':True,'all_prior_backups_preserved':True,'no_deletion_performed':True,'free_disk_bytes_before':free_before,'free_disk_bytes_after':shutil.disk_usage(out).free,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 (out/'MEGASAUR_FIXED_PIN_STREAM_VERIFICATION.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2),flush=True)
if __name__=='__main__':main()
