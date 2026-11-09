#!/usr/bin/env python3
"""Verify pinned four historical tool candidate bytes by streaming actual target files.
Reuses a verified Harbinger full tree and six pinned historical archives.
Default downloads use immutable GitHub URLs. No full runtime tree, no gameplay,
no old-save acceptance, no claim that source-map equality resolves all references.
"""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,tarfile,os,io,gc,re,ast,datetime,shutil,urllib.request
COMMIT='5d17cb79f7f7b6abdddb68e3b9e420e0167184b3'
REPO_PATH='battlegrounds-backup/pending/20261109-historical-tools-batch2-four-candidate'
BASE_URL=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{COMMIT}/{REPO_PATH}/'
PACKAGE='historical_tools_batch2_four_candidate_20261109'
ARCHIVE_SHA='51263c49a09a0a735a417e147e4f64f0529be4d5fa12529807653da7187693eb'
MANIFEST_SHA='26e1d37470f663358cc246c5a860d0d563b1eae60a3729f466f2080546ed678b'
BASE_MAP_SHA='53da1c13fbebb6eb8c5672ad8828109720efdfab1a8a97b6792a6da3202e6080'
TARGET_MAP_SHA='3581d683af1a208f00c3dd853e268d799abc5e2811847954a339cad2a68434ea'
BASE_COMMIT='cfe5366f7e0a115532e8996549782c635481b97a'
BASE_URL_PRIOR=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{BASE_COMMIT}/battlegrounds-backup/pending/20261109-historical-tools-batch1-candidate/'
BASE_MANIFEST_SHA='1339271a1dc7d2789e931e1a2c2270d9b45613ed5717a7269332919949c7624d'
BASE_RECEIPT_SHA='c3e5df6796a973d499533adae754dc3501d26d721f62f9c78f33dd158089af1e'
STATUS='FOUR_HISTORICAL_TOOL_CANDIDATE_SCOPED_VALIDATION_PASS'
LAYERS=[
 ('native_listener','native_spell_listener_leaf_partial_candidate_20261109','46ceb12b81c5db0c417933482d6572f3c89693d2ba3ef2d507ccebc5f0ed4ec7','e31eb74faca1a774b42a7c8bcef11b1592eae64ad350b08fa930f9a1d7cd64fe','9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111',247,5),
 ('earth_mother','earth_mother_helper_leaf_partial_candidate_20261109','333aad27ba8ed0d0699c97cd4a33be5494310247a8350993532cd725f26e753c','9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111','d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960',79,4),
 ('golden_source','native_golden_source_leaf_partial_candidate_20261109','181a6415d954795e0b40286165c39a55d0469745185e7e6d24840eb769025cef','d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960','c0454c30ce7eb2a71fb8ea3e513f0db0d2fd684f63129a1b7da2e4a47666603b',71,3),
 ('golden_tool','golden_arrow_tool_patch_reconstruction_candidate_20261109','3122135a4912a58c361b522e67b946dffbbe29b3618051972a4898e8cac7edd9','c0454c30ce7eb2a71fb8ea3e513f0db0d2fd684f63129a1b7da2e4a47666603b','bfd5d82ede8559200aed89547e4584ac091873a9392079af5ee20c41ea764a0a',98,1),
 ('megasaur_tool','megasaur_tool_fixed_pin_candidate_20261109','27514275c7204a972de2a5193b93deb35c7d4a72b137d1bc5c9477c2f7e9cf66','bfd5d82ede8559200aed89547e4584ac091873a9392079af5ee20c41ea764a0a','28b1d1c523dfc566bc5eacd04ccea1e1787c1b15e0cca8f9e67ecf9229b46bf4',143,1),
 ('batch1_tools','historical_tools_batch1_candidate_20261109','d4de01b2fa7a530c00b383455e94f1a0da62d81c68b03b4205b90aca1c46aea1','28b1d1c523dfc566bc5eacd04ccea1e1787c1b15e0cca8f9e67ecf9229b46bf4',BASE_MAP_SHA,199,5)]

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
 for name in ['native-archive','earth-archive','golden-archive','golden-tool-archive','megasaur-archive','batch1-archive']:p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--download-dir',type=Path);p.add_argument('--baseline-receipt',type=Path);p.add_argument('--baseline-manifest',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 out=a.output.resolve();baseline=a.historical_baseline.resolve();require(not out.exists() and baseline not in out.parents,'Output must be new and outside baseline');out.mkdir(parents=True);free_before=shutil.disk_usage(out).free
 fresh=a.download_dir is None;d=a.download_dir.resolve() if a.download_dir else out/'downloaded'
 if fresh:d.mkdir();get(BASE_URL+'MANIFEST.json',d/'MANIFEST.json')
 require(file_meta(d/'MANIFEST.json')['sha256']==MANIFEST_SHA,'Pinned manifest mismatch');m=read_json(d/'MANIFEST.json');require(m['sha256']==ARCHIVE_SHA and m['bytes']==1145088 and len(m['files'])==282 and len(m['parts'])==5,'Package metadata mismatch')
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
 base=read_json(pkg/'BASE_MAP.json');target=read_json(pkg/'SOURCE_MAP.json');delta={n.removeprefix(PACKAGE+'/delta/'):v for n,v in members.items() if n.startswith(PACKAGE+'/delta/')}
 leaves=['tools/'+x+'_patterns.py' for x in ['old_soul','warband_whistle','lovely_locket','replica_cathedral']];changes={'added':leaves,'modified':[],'removed':[]}
 require(len(base)==27904 and len(target)==27908 and set(delta)==set(leaves)==set(target)-set(base) and {**base,**delta}==target,'Not the exact four-file addition')
 require(sum(x['bytes'] for x in target.values())==1548971251 and sum(x['bytes'] for x in delta.values())==132315,'Target size mismatch')
 for n in target:require(safe(n),'Unsafe source path')
 require(read_json(d/'CHANGES.json')==changes and read_json(d/'REMOVALS.json')==m['removed_source_files']==[],'External change/removal mismatch')
 require(read_json(pkg/'CHANGES.json')==[{'path':n,'status':'added_byte_exact_historical_candidate_not_proven_latest','before':None,'after':delta[n]} for n in leaves],'Archived change record mismatch')
 result=read_json(pkg/'RESULT.json');require(result['status']==m['status']==STATUS and result['input_commit']==BASE_COMMIT and result['files']==delta and result['bounded_Python_module_checks']==161 and result['Godot_assertions_including_repeat_runs']==1098 and result['static_cross_checks']==69,'Candidate scope mismatch')
 for key in ['latest_installed_versions_proven','tools_fixed_by_current_admission_pins','full_Catalog_fingerprint_computed','full_Catalog_loaded','full_Game_tested','old_save_compatibility_verified','full_project_compiler_run','pool_or_gameplay_acceptance_promoted']:require(result[key] is False,'Missing scope limitation: '+key)
 require(result['remaining_original_367_missing_scope']==m['remaining_tools_reference_gaps_within_original_367']==357 and result['remaining_prior_68_historical_candidates']==59,'Remaining gap scope mismatch')
 for arg,name,urlname,expected in [(a.baseline_manifest,'PINNED_INPUT_MANIFEST.json','MANIFEST.json',BASE_MANIFEST_SHA),(a.baseline_receipt,'PINNED_INPUT_RECEIPT.json','HISTORICAL_TOOLS_BATCH1_STREAM_VERIFICATION.json',BASE_RECEIPT_SHA)]:
  dest=out/name
  if arg:dest.write_bytes(arg.read_bytes())
  else:get(BASE_URL_PRIOR+urlname,dest)
  require(file_meta(dest)['sha256']==expected,'Pinned dependency hash mismatch')
 dep=read_json(out/'PINNED_INPUT_MANIFEST.json');receipt=read_json(out/'PINNED_INPUT_RECEIPT.json')
 require(m['depends_on']['recovery_commit']==BASE_COMMIT and m['depends_on']['archive_sha256']==dep['sha256']==LAYERS[5][2] and m['depends_on']['manifest_sha256']==BASE_MANIFEST_SHA and m['depends_on']['receipt_sha256']==BASE_RECEIPT_SHA,'Dependency pointers mismatch')
 require(receipt['status']=='PASS_EXACT_STREAMED_SOURCE_MAP_BYTES_WITH_FIVE_HISTORICAL_TOOL_CANDIDATES' and receipt['source_map_sha256']==BASE_MAP_SHA and receipt['historical_baseline_and_prior_archives_unchanged'] is True and receipt['full_game_validation_passed'] is False,'Pinned receipt scope mismatch')
 historical=None;composed=None;overlays={};origin_by_path={};prior_members=[]
 archives=[a.native_archive,a.earth_archive,a.golden_archive,a.golden_tool_archive,a.megasaur_archive,a.batch1_archive]
 for index,(path,layer) in enumerate(zip(archives,LAYERS)):
  label,root,expected,bhash,thash,count,delta_count=layer
  oldmembers,keep=archive_verify(path,expected,root,dep if index==5 else None)
  require(len(oldmembers)==count and sha(keep['BASE_MAP.json'])==bhash and sha(keep['SOURCE_MAP.json'])==thash,'Prior archive map/count mismatch')
  oldbase=json.loads(keep.pop('BASE_MAP.json'));oldtarget=json.loads(keep.pop('SOURCE_MAP.json'))
  current_delta={n.removeprefix('delta/'):b for n,b in keep.items() if n.startswith('delta/')};require(len(current_delta)==delta_count,'Prior delta count mismatch')
  delta_meta={n:meta(b) for n,b in current_delta.items()};require({n:v for n,v in oldtarget.items() if oldbase.get(n)!=v}==delta_meta and {**oldbase,**delta_meta}==oldtarget,'Prior source delta/removal continuity mismatch')
  if historical is None:historical=oldbase;composed=dict(oldbase)
  require(composed==oldbase,'Adjacent archive map mismatch');composed.update(delta_meta);require(composed==oldtarget,'Layer composition mismatch')
  overlays.update(current_delta);origin_by_path.update({n:label for n in current_delta});prior_members.append({'archive':root+'.tar.xz','sha256':expected,'members_reverified':count,'source_files':delta_count,'freshly_downloaded_this_round':False})
  del oldbase,oldtarget,keep,current_delta,oldmembers,delta_meta;gc.collect()
 require(composed==base,'Six historical layers do not match direct input');del composed;gc.collect()
 check_tree(baseline,historical,'historical baseline before')
 def actual_bytes(name):return overlays[name] if name in overlays else (baseline/name).read_bytes()
 provenance=read_json(pkg/'PROVENANCE.json');require(len(provenance['files'])==4 and {x['target'] for x in provenance['files']}==set(leaves),'Provenance target mismatch');pin_sum=0;literal_comparisons=0;dependency_count=0;dependency_ids=set()
 for item in provenance['files']:
  name=item['target'];restored=(pkg/'delta'/name).read_bytes();require(restored==actual_bytes(item['original'])==(pkg/'evidence/historical'/item['original']).read_bytes() and meta(restored)==delta[name],'Historical original byte mismatch')
  require(item['latest_installed_original_proven'] is item['current_target_is_fixed_admission_pin'] is False,'Version/pin boundary changed')
  for path,expected in item['evidence_files'].items():
   require(safe(path),'Unsafe evidence path');evidence=(pkg/'evidence/historical'/path).read_bytes();require(meta(evidence)==expected and evidence==actual_bytes(path),'Historical evidence differs from actual baseline')
   if path.endswith('/integration_manifest.json'):
    rows=json.loads(evidence);matches=[x for x in rows if x.get('path')==name];require(len(matches)==1 and matches[0]['after_sha256']==sha(restored),'Historical installation hash mismatch')
   if path.endswith('/shared_manifest.json'):
    rows=json.loads(evidence);matches=[x for x in rows if x.get('install_path')==name];require(len(matches)==1 and matches[0]['after_sha256']==sha(restored),'Historical shared installation hash mismatch')
  source=actual_bytes(item['current_source']);require(meta(source)==item['current_source_record'] and source==(pkg/'probe_inputs'/item['current_source']).read_bytes(),'Current source differs')
  pins=json.loads(re.search(rb'^const PROOF_SHA256[^=]*=(.*)$',source,re.M)[1]);require(len(pins)==item['current_source_pin_count'] and name not in pins,'Wrong current pin scope');pin_sum+=len(pins)
  for pin,expected in pins.items():require(safe(pin) and sha(actual_bytes(pin))==expected,'Current fixed pin mismatch')
  module=ast.parse(restored);values={}
  for node in module.body:
   if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
    try:values[node.targets[0].id]=ast.literal_eval(node.value)
    except (TypeError,ValueError):pass
  for key in ['RAW','EXPECTED','PROGRAMS']:
   if key in values:
    gd=json.loads(re.search('^const '+key+r'[^=]*=(.*)$',source.decode(),re.M)[1]);require(values[key]==gd,'Current literal mismatch: '+key);literal_comparisons+=1
  if 'DEPENDENCY_RAW' in values:
   gd=json.loads(re.search(r'^const DEP_RAW[^=]*=(.*)$',source.decode(),re.M)[1]);require(values['DEPENDENCY_RAW']==gd,'Dependency literal mismatch');dependency_count+=len(gd);dependency_ids.update(gd)
 require(pin_sum==55 and dependency_count==16 and len(dependency_ids)==9,'Current pin/dependency counts mismatch')
 with tarfile.open(a.megasaur_archive,'r:xz') as previous:
  prefix='megasaur_tool_fixed_pin_candidate_20261109/evidence/tools_reference_inventory_20261109/'
  inventory_bytes=previous.extractfile(prefix+'FINAL_INVENTORY.json').read();summary_bytes=previous.extractfile(prefix+'FINAL_SUMMARY.json').read()
  prior_internal=json.loads(previous.extractfile('megasaur_tool_fixed_pin_candidate_20261109/PACKAGE_MANIFEST.json').read());require(meta(inventory_bytes)==prior_internal['evidence/tools_reference_inventory_20261109/FINAL_INVENTORY.json'] and meta(summary_bytes)==prior_internal['evidence/tools_reference_inventory_20261109/FINAL_SUMMARY.json'],'Upstream inventory member mismatch')
 inv=json.loads(inventory_bytes);require(len(inv)==367 and len({x['target'] for x in inv})==367 and all(not x['current_root_file_exists'] for x in inv),'Historical 367-item state mismatch')
 require(sum(x['target'] not in base for x in inv)==361 and sum(x['target'] not in target for x in inv)==357,'Remaining gap counts differ')
 require((pkg/'evidence/PRIOR_367_SUMMARY.json').read_bytes()==summary_bytes,'Sealed summary differs from upstream inventory')
 selected=read_json(pkg/'evidence/SELECTED_PRIOR_INVENTORY.json');by_target={x['target']:x for x in inv};require(len(selected)==4 and {x['target'] for x in selected}==set(leaves) and all(x==by_target[x['target']] for x in selected),'Selected prior inventory rows differ')
 deferred='tools/sinstone_sticker_patterns.py';require(deferred not in base and deferred not in target and deferred not in delta,'Sinstone unexpectedly restored')
 review=read_json(pkg/'DEFERRED_SINSTONE_REVIEW.json');require(review['deferred_target']==deferred and review['failed_comparison_assertions_per_state']==6 and review['Sinstone_not_added_to_final_delta'] is True,'Deferred review mismatch')
 failed_trial_states=[]
 for mode in ['before','after','tamper']:
  report=read_json(pkg/'evidence/deferred_sinstone_trial'/mode/'report.json');require(len(report['failures'])==6 and all(x.startswith(deferred+':closure_rejects_missing_dependency:') for x in report['failures']),'Original failed trial evidence mismatch');failed_trial_states.append({'mode':mode,'failed_assertions':6})
 print('PASS: four historical originals/installation records/current literals; 55 unchanged pins; 16 dependency entries/9 IDs; 357 missing paths; deferred failed trial retained',flush=True)
 del inv,by_target,selected,inventory_bytes,summary_bytes;gc.collect()
 origins={'historical_tree':0,'native_listener':0,'earth_mother':0,'golden_source':0,'golden_tool':0,'megasaur_tool':0,'batch1_tools':0,'fresh_batch2_tools':0};reconstructed={};aggregate=hashlib.sha256()
 for name in sorted(target):
  if name in delta:h=(pkg/'delta'/name).open('rb');origin='fresh_batch2_tools'
  elif name in overlays:h=io.BytesIO(overlays[name]);origin=origin_by_path[name]
  else:
   source=baseline/name;require(source.is_file() and not source.is_symlink(),'Invalid historical source');h=source.open('rb');origin='historical_tree'
  digest=hashlib.sha256();count=0;aggregate.update(name.encode()+b'\0'+str(target[name]['bytes']).encode()+b'\0')
  with h:
   for b in iter(lambda:h.read(1024*1024),b''):digest.update(b);aggregate.update(b);count+=len(b)
  reconstructed[name]={'bytes':count,'sha256':digest.hexdigest()};require(reconstructed[name]==target[name],'Streamed target mismatch: '+name);origins[origin]+=1
 require(reconstructed==target and origins=={'historical_tree':27885,'native_listener':5,'earth_mother':4,'golden_source':3,'golden_tool':1,'megasaur_tool':1,'batch1_tools':5,'fresh_batch2_tools':4},'Final map/origin mismatch')
 check_tree(baseline,historical,'historical baseline after')
 for path,layer in zip(archives,LAYERS):require(file_meta(path)['sha256']==layer[2],'Historical archive changed')
 (out/'STREAM_RECONSTRUCTED_SOURCE_MAP.json').write_text(json.dumps(reconstructed,indent=2,sort_keys=True)+'\n');require(file_meta(out/'STREAM_RECONSTRUCTED_SOURCE_MAP.json')['sha256']==TARGET_MAP_SHA,'Canonical target map bytes differ')
 r={'status':'PASS_EXACT_STREAMED_SOURCE_MAP_BYTES_WITH_FOUR_HISTORICAL_TOOLS_AND_SINSTONE_DEFERRED','candidate_status':STATUS,'archive_commit':COMMIT,'repository_path':REPO_PATH,'manifest_sha256':MANIFEST_SHA,'archive_sha256':ARCHIVE_SHA,'archive_bytes':1145088,'parts_verified':5,'members_verified':282,'internal_manifest_members_verified':281,'input_verified_commit':BASE_COMMIT,'input_manifest_sha256':BASE_MANIFEST_SHA,'input_receipt_sha256':BASE_RECEIPT_SHA,'input_source_map_sha256':BASE_MAP_SHA,'source_map_sha256':TARGET_MAP_SHA,'historical_full_tree_files_rehashed_before_and_after':len(historical),'historical_tree_source_map_sha256':LAYERS[0][3],'prior_archive_verifications':prior_members,'direct_input_files_verified_by_actual_bytes':len(base),'target_files_streamed_and_verified':len(target),'actual_target_bytes_streamed':sum(v['bytes'] for v in target.values()),'stream_source_origins':origins,'aggregate_stream_sha256':aggregate.hexdigest(),'aggregate_stream_format':'Sorted UTF-8 target path, NUL, ASCII file byte count, NUL, actual file bytes; repeated for every target file.','change_lists':changes,'historical_originals_and_supporting_evidence_match_actual_baseline_bytes':True,'historical_installation_and_shared_manifest_hashes_rechecked':True,'restored_python_ast_parse_passed':True,'current_source_literal_comparisons_passed':literal_comparisons,'current_source_pins_verified':pin_sum,'four_tools_themselves_are_current_fixed_pins':False,'current_pin_constants_unchanged':True,'latest_installed_versions_proven':False,'prior_inventory_before_items_preserved':367,'remaining_missing_within_inventory_scope':357,'remaining_historical_candidates_from_68':59,'upstream_full_inventory_and_selected_rows_reverified':True,'inventory_scan_repeated_this_round':False,'inventory_scope':'Original 367 pre-restoration targets, not all possible tools gaps. This batch adds four and leaves 357 absent; original inventory records preserved.','current_dependency_raw_entries_verified':dependency_count,'unique_dependency_card_ids':len(dependency_ids),'deferred_target':deferred,'deferred_target_absent_from_runtime_map':True,'deferred_original_failed_trial_reports':failed_trial_states,'failed_trials_counted_as_passes':False,'partial_validation_only':True,'full_game_validation_passed':False,'save_compatibility_verified':False,'full_catalog_fingerprint_executed':False,'full_compiler_executed':False,'gameplay_test_run_by_verifier':False,'Godot_proof_error_rerun_by_verifier':False,'candidate_Python_modules_executed_by_verifier':False,'whole_game_memory_improvement_verified':False,'complete_runtime_directory_created':False,'verification_mode':'Actual per-file bytes from reused Harbinger tree and six pinned archive layers, plus freshly downloaded four-file batch delta; not merely map comparison.','historical_chain_freshly_downloaded_this_round':False,'increment_downloaded_by_this_helper':fresh,'increment_input_mode':'fresh immutable URLs' if fresh else 'Separately fetched pinned bytes; see FETCH_PROVENANCE.json proving all five part objects absent before fetch.','historical_baseline_and_prior_archives_unchanged':True,'missing_files_relative_to_source_map':[],'mismatched_files_relative_to_source_map':[],'unexpected_files_relative_to_source_map':[],'source_map_equality_does_not_establish_complete_game_recovery':True,'all_prior_backups_preserved':True,'no_deletion_performed':True,'free_disk_bytes_before':free_before,'free_disk_bytes_after':shutil.disk_usage(out).free,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 (out/'HISTORICAL_TOOLS_BATCH2_STREAM_VERIFICATION.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2),flush=True)
if __name__=='__main__':main()
