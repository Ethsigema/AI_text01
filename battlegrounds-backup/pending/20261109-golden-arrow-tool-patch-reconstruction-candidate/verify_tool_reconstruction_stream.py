#!/usr/bin/env python3
"""Verify pinned tool reconstruction bytes by streaming actual target files.
Reuses a verified Harbinger full tree and three pinned historical archives.
Default downloads use immutable GitHub URLs. No full runtime tree, no gameplay,
no old-save acceptance, no claim that source-map equality resolves all references.
"""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,tarfile,os,io,gc,re,ast,datetime,shutil,urllib.request
COMMIT='edf067470abc889b166ea39d1cec97c3dcf7c528'
REPO_PATH='battlegrounds-backup/pending/20261109-golden-arrow-tool-patch-reconstruction-candidate'
BASE_URL=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{COMMIT}/{REPO_PATH}/'
PACKAGE='golden_arrow_tool_patch_reconstruction_candidate_20261109'
ARCHIVE_SHA='3122135a4912a58c361b522e67b946dffbbe29b3618051972a4898e8cac7edd9'
MANIFEST_SHA='a5016309666174b5a84523f5760f50b530110d8ce6f6dcdb1012c0f614af1a94'
BASE_MAP_SHA='c0454c30ce7eb2a71fb8ea3e513f0db0d2fd684f63129a1b7da2e4a47666603b'
TARGET_MAP_SHA='bfd5d82ede8559200aed89547e4584ac091873a9392079af5ee20c41ea764a0a'
BASE_COMMIT='839d5dd71e4d0e4bf59f97c1fb6ed50b5807daa6'
BASE_URL_PRIOR=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{BASE_COMMIT}/battlegrounds-backup/pending/20261109-native-golden-source-leaf-partial-candidate/'
BASE_MANIFEST_SHA='5d967b3a52ac20fa32791171eef32b013e930ceefa3b13481fd602fc9a083a71'
BASE_RECEIPT_SHA='2f24988e51c5acfc08df4f2417aefad974dd8717b9bbf2673ad4baadf48b66b0'
STATUS='PATCH_DERIVED_RECONSTRUCTION_BOUNDED_VALIDATION_PASS'
LAYERS=[
 ('native_listener','native_spell_listener_leaf_partial_candidate_20261109','46ceb12b81c5db0c417933482d6572f3c89693d2ba3ef2d507ccebc5f0ed4ec7','e31eb74faca1a774b42a7c8bcef11b1592eae64ad350b08fa930f9a1d7cd64fe','9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111',247,5),
 ('earth_mother','earth_mother_helper_leaf_partial_candidate_20261109','333aad27ba8ed0d0699c97cd4a33be5494310247a8350993532cd725f26e753c','9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111','d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960',79,4),
 ('golden_source','native_golden_source_leaf_partial_candidate_20261109','181a6415d954795e0b40286165c39a55d0469745185e7e6d24840eb769025cef','d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960',BASE_MAP_SHA,71,3)]

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

def strict_rebuild(source,patch):
 leaf='tools/golden_arrow_patterns.py';lines=source.decode().splitlines(True);diff=patch.decode().splitlines(True)
 require(diff[:2]==['--- a/'+leaf+'\n','+++ b/'+leaf+'\n'],'Unexpected patch target')
 require(sum(x.startswith('@@') for x in diff)==1,'Must contain one exact hunk')
 m=re.fullmatch(r'@@ -(\d+),(\d+) \+(\d+),(\d+) @@\n',diff[2]);require(m is not None,'Invalid hunk header')
 require(all(x[:1] in [' ','+','-'] for x in diff[3:]),'Unsupported hunk line')
 before=[x[1:] for x in diff[3:] if x[0] in ' -'];after=[x[1:] for x in diff[3:] if x[0] in ' +'];at=int(m[1])-1
 require(int(m[1])==int(m[3]) and len(before)==int(m[2]) and len(after)==int(m[4]) and lines[at:at+len(before)]==before,'Hunk context/line counts mismatch')
 return ''.join(lines[:at]+after+lines[at+len(before):]).encode()

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--historical-baseline',type=Path,required=True)
 for name in ['native-archive','earth-archive','golden-archive']:p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--download-dir',type=Path);p.add_argument('--baseline-receipt',type=Path);p.add_argument('--baseline-manifest',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 out=a.output.resolve();baseline=a.historical_baseline.resolve();require(not out.exists() and baseline not in out.parents,'Output must be new and outside baseline');out.mkdir(parents=True);free_before=shutil.disk_usage(out).free
 fresh=a.download_dir is None;d=a.download_dir.resolve() if a.download_dir else out/'downloaded'
 if fresh:d.mkdir();get(BASE_URL+'MANIFEST.json',d/'MANIFEST.json')
 require(file_meta(d/'MANIFEST.json')['sha256']==MANIFEST_SHA,'Pinned manifest mismatch');m=read_json(d/'MANIFEST.json');require(m['sha256']==ARCHIVE_SHA and m['bytes']==1085500 and len(m['files'])==98 and len(m['parts'])==5,'Package metadata mismatch')
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
 base=read_json(pkg/'BASE_MAP.json');target=read_json(pkg/'SOURCE_MAP.json');leaf='tools/golden_arrow_patterns.py';delta={n.removeprefix(PACKAGE+'/delta/'):v for n,v in members.items() if n.startswith(PACKAGE+'/delta/')};changes={'added':[leaf],'modified':[],'removed':[]}
 require(len(base)==27897 and len(target)==27898 and len(delta)==1 and leaf not in base and {**base,**delta}==target,'Not the exact one-file addition')
 require(sum(x['bytes'] for x in target.values())==1548752837 and delta[leaf]=={'bytes':32647,'sha256':'886717620eaa0da57b9a8d7f579fb78b08b2f2a54c45f7899e6e3ded10d642d3'},'Target size/hash mismatch')
 for n in target:require(safe(n),'Unsafe source path')
 require(read_json(d/'CHANGES.json')==changes and read_json(d/'REMOVALS.json')==m['removed_source_files']==[],'External change/removal mismatch')
 require(read_json(pkg/'CHANGES.json')==[{'path':leaf,'status':'added_reconstructed_from_preserved_patch','before':None,'after':delta[leaf]}],'Archived change record mismatch')
 result=read_json(pkg/'RESULT.json');require(result['status']==m['status']==STATUS and result['input_commit']==BASE_COMMIT and result['checks']==69,'Candidate status mismatch')
 for key in ['latest_post_patch_installed_original_found','all_missing_tooling_recovered','full_catalog_execution_fingerprint_computed','full_compiler_executed','full_Game_run','old_save_compatibility_preserved_or_verified']:require(result[key] is False,'Missing scope limitation: '+key)
 require(result['other_static_runtime_paths_tools_gaps_remaining']==m['remaining_static_tools_reference_gaps']==367 and m['reconstruction_not_recovered_installed_original'] is True,'Reference/source boundary missing')
 for arg,name,urlname,expected in [(a.baseline_manifest,'PINNED_INPUT_MANIFEST.json','MANIFEST.json',BASE_MANIFEST_SHA),(a.baseline_receipt,'PINNED_INPUT_RECEIPT.json','GOLDEN_SOURCE_LEAF_PARTIAL_STREAM_VERIFICATION.json',BASE_RECEIPT_SHA)]:
  dest=out/name
  if arg:dest.write_bytes(arg.read_bytes())
  else:get(BASE_URL_PRIOR+urlname,dest)
  require(file_meta(dest)['sha256']==expected,'Pinned dependency hash mismatch')
 dep=read_json(out/'PINNED_INPUT_MANIFEST.json');receipt=read_json(out/'PINNED_INPUT_RECEIPT.json')
 require(m['depends_on']['recovery_commit']==BASE_COMMIT and m['depends_on']['archive_sha256']==dep['sha256']==LAYERS[2][2] and m['depends_on']['manifest_sha256']==BASE_MANIFEST_SHA and m['depends_on']['receipt_sha256']==BASE_RECEIPT_SHA,'Dependency pointers mismatch')
 require(receipt['status']=='PASS_EXACT_STREAMED_SOURCE_MAP_BYTES_WITH_KNOWN_REFERENCE_GAP' and receipt['source_map_sha256']==BASE_MAP_SHA and receipt['historical_baseline_and_prior_archives_unchanged'] is True and receipt['full_game_validation_passed'] is False,'Pinned receipt scope mismatch')
 historical=None;composed=None;overlays={};origin_by_path={};prior_members=[]
 archives=[a.native_archive,a.earth_archive,a.golden_archive]
 for index,(path,layer) in enumerate(zip(archives,LAYERS)):
  label,root,expected,bhash,thash,count,delta_count=layer
  oldmembers,keep=archive_verify(path,expected,root,dep if index==2 else None)
  require(len(oldmembers)==count and sha(keep['BASE_MAP.json'])==bhash and sha(keep['SOURCE_MAP.json'])==thash,'Prior archive map/count mismatch')
  oldbase=json.loads(keep.pop('BASE_MAP.json'));oldtarget=json.loads(keep.pop('SOURCE_MAP.json'))
  current_delta={n.removeprefix('delta/'):b for n,b in keep.items() if n.startswith('delta/')};require(len(current_delta)==delta_count,'Prior delta count mismatch')
  delta_meta={n:meta(b) for n,b in current_delta.items()};require({n:v for n,v in oldtarget.items() if oldbase.get(n)!=v}==delta_meta and {**oldbase,**delta_meta}==oldtarget,'Prior source delta/removal continuity mismatch')
  if historical is None:historical=oldbase;composed=dict(oldbase)
  require(composed==oldbase,'Adjacent archive map mismatch');composed.update(delta_meta);require(composed==oldtarget,'Layer composition mismatch')
  overlays.update(current_delta);origin_by_path.update({n:label for n in current_delta});prior_members.append({'archive':root+'.tar.xz','sha256':expected,'members_reverified':count,'source_files':delta_count,'freshly_downloaded_this_round':False})
  del oldbase,oldtarget,keep,current_delta,oldmembers,delta_meta;gc.collect()
 require(composed==base,'Three historical layers do not match direct input');del composed;gc.collect()
 check_tree(baseline,historical,'historical baseline before')
 def actual_bytes(name):return overlays[name] if name in overlays else (baseline/name).read_bytes()
 original_path='research/golden_arrow_native_recovery/candidates/tools/golden_arrow_patterns.py';patch_path='research/arrow_native_periodic_delivery/tools_golden_arrow_patterns.py.patch'
 original=(pkg/'evidence/original_candidate.py').read_bytes();patch=(pkg/'evidence/original_followup.patch').read_bytes();rebuilt=(pkg/'delta'/leaf).read_bytes()
 require(sha(original)=='ff0073009c27627cdb4a4065c3a2f56769cd64ced5fd1033b4b5a0586e139025' and sha(patch)=='b3e586190991034d248a3bb80c4549b235d315a90366524df470ad244c49cd4f','Reconstruction source hashes mismatch')
 require(original==actual_bytes(original_path) and patch==actual_bytes(patch_path),'Historical evidence does not equal actual baseline bytes')
 require(strict_rebuild(original,patch)==rebuilt,'Independent exact patch reconstruction differs');ast.parse(original);ast.parse(rebuilt)
 for consumer in read_json(pkg/'evidence/FINGERPRINT_CONSUMERS.json'):
  body=actual_bytes(consumer['source']);require(sha(body)==consumer['source_sha256'],'Fingerprint consumer source mismatch');lines=body.decode().splitlines()
  for r in consumer['ranges']:require('\n'.join(lines[r['start_line']-1:r['end_line']])==r['text'],'Fingerprint consumer snippet mismatch')
 print('PASS: historical source/patch bytes and independent strict patch reconstruction; no installed-original claim',flush=True)
 origins={'historical_tree':0,'native_listener':0,'earth_mother':0,'golden_source':0,'fresh_tool_reconstruction':0};reconstructed={};aggregate=hashlib.sha256()
 for name in sorted(target):
  if name==leaf:h=(pkg/'delta'/leaf).open('rb');origin='fresh_tool_reconstruction'
  elif name in overlays:h=io.BytesIO(overlays[name]);origin=origin_by_path[name]
  else:
   source=baseline/name;require(source.is_file() and not source.is_symlink(),'Invalid historical source');h=source.open('rb');origin='historical_tree'
  digest=hashlib.sha256();count=0;aggregate.update(name.encode()+b'\0'+str(target[name]['bytes']).encode()+b'\0')
  with h:
   for b in iter(lambda:h.read(1024*1024),b''):digest.update(b);aggregate.update(b);count+=len(b)
  reconstructed[name]={'bytes':count,'sha256':digest.hexdigest()};require(reconstructed[name]==target[name],'Streamed target mismatch: '+name);origins[origin]+=1
 require(reconstructed==target and origins=={'historical_tree':27885,'native_listener':5,'earth_mother':4,'golden_source':3,'fresh_tool_reconstruction':1},'Final map/origin mismatch')
 check_tree(baseline,historical,'historical baseline after')
 for path,layer in zip(archives,LAYERS):require(file_meta(path)['sha256']==layer[2],'Historical archive changed')
 (out/'STREAM_RECONSTRUCTED_SOURCE_MAP.json').write_text(json.dumps(reconstructed,indent=2,sort_keys=True)+'\n');require(file_meta(out/'STREAM_RECONSTRUCTED_SOURCE_MAP.json')['sha256']==TARGET_MAP_SHA,'Canonical target map bytes differ')
 r={'status':'PASS_EXACT_STREAMED_SOURCE_MAP_BYTES_WITH_RECONSTRUCTED_TOOL_AND_REMAINING_REFERENCE_GAPS','candidate_status':STATUS,'archive_commit':COMMIT,'repository_path':REPO_PATH,'manifest_sha256':MANIFEST_SHA,'archive_sha256':ARCHIVE_SHA,'archive_bytes':1085500,'parts_verified':5,'members_verified':98,'internal_manifest_members_verified':97,'input_verified_commit':BASE_COMMIT,'input_manifest_sha256':BASE_MANIFEST_SHA,'input_receipt_sha256':BASE_RECEIPT_SHA,'input_source_map_sha256':BASE_MAP_SHA,'source_map_sha256':TARGET_MAP_SHA,'historical_full_tree_files_rehashed_before_and_after':len(historical),'historical_tree_source_map_sha256':LAYERS[0][3],'prior_archive_verifications':prior_members,'direct_input_files_verified_by_actual_bytes':len(base),'target_files_streamed_and_verified':len(target),'actual_target_bytes_streamed':sum(v['bytes'] for v in target.values()),'stream_source_origins':origins,'aggregate_stream_sha256':aggregate.hexdigest(),'aggregate_stream_format':'Sorted UTF-8 target path, NUL, ASCII file byte count, NUL, actual file bytes; repeated for every target file.','change_lists':changes,'reconstruction_source_and_patch_match_actual_historical_bytes':True,'strict_patch_reconstruction_independently_repeated':True,'original_and_rebuilt_python_ast_parse_passed':True,'fingerprint_consumer_source_and_snippets_reverified':True,'reconstructed_tool_sha256':sha(rebuilt),'post_patch_installed_original_recovered':False,'remaining_static_runtime_paths_tools_gaps':367,'gap_count_scope':'Producer sealed research: 355 static RUNTIME_PATHS declarations; not a universal enumeration. This verifier preserves the count/scope and does not rerun that scan.','partial_validation_only':True,'full_game_validation_passed':False,'save_compatibility_verified':False,'full_catalog_fingerprint_executed':False,'full_compiler_executed':False,'gameplay_test_run_by_verifier':False,'whole_game_memory_improvement_verified':False,'complete_runtime_directory_created':False,'verification_mode':'Actual per-file bytes from reused Harbinger tree and three pinned archive layers, plus freshly downloaded tool reconstruction delta; not merely map comparison.','historical_chain_freshly_downloaded_this_round':False,'increment_downloaded_by_this_helper':fresh,'increment_input_mode':'fresh immutable URLs' if fresh else 'Separately fetched pinned bytes; see FETCH_PROVENANCE.json proving all five part objects absent before fetch.','historical_baseline_and_prior_archives_unchanged':True,'missing_files_relative_to_source_map':[],'mismatched_files_relative_to_source_map':[],'unexpected_files_relative_to_source_map':[],'source_map_equality_does_not_establish_complete_game_recovery':True,'all_prior_backups_preserved':True,'no_deletion_performed':True,'free_disk_bytes_before':free_before,'free_disk_bytes_after':shutil.disk_usage(out).free,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 (out/'TOOL_RECONSTRUCTION_STREAM_VERIFICATION.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2),flush=True)
if __name__=='__main__':main()
