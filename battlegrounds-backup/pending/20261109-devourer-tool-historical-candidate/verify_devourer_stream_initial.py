#!/usr/bin/env python3
"""Verify pinned Devourer historical tool candidate bytes by streaming actual target files.
Reuses a verified Harbinger full tree and eight pinned historical archives.
Default downloads use immutable GitHub URLs. No full runtime tree, no gameplay,
no old-save acceptance, no claim that source-map equality resolves all references.
"""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,tarfile,os,io,gc,re,ast,datetime,shutil,urllib.request
COMMIT='cfb226a7f5888740371748b49aeb5ad6eda445cf'
REPO_PATH='battlegrounds-backup/pending/20261109-devourer-tool-historical-candidate'
BASE_URL=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{COMMIT}/{REPO_PATH}/'
PACKAGE='devourer_tool_historical_candidate_lowmem_20261109'
ARCHIVE_SHA='c807dd1229f5c4480631a446c8b7b0aa3f00d48e4602bc91d7d23c1480fa5a44'
MANIFEST_SHA='5ba05d0f1d95b5c9fb3e8e0bcf5c6a961dcaf5c5fcec5356233b28a468b9e6c7'
BASE_MAP_SHA='608a981c9b82b255c37fefb004a4bfe98bcf95d9717cfa3a5ee2917961ff2d00'
TARGET_MAP_SHA='9baabc104b5f2f93087dfec0e385d6cb9fceffbf3b1d4441ec91da463a727260'
BASE_COMMIT='4df40aa115e16fce48e4a17461893d36360613d9'
BASE_URL_PRIOR=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{BASE_COMMIT}/battlegrounds-backup/pending/20261109-historical-tools-batch4-three-candidate/'
BASE_MANIFEST_SHA='c5711e27d97ab3a82a8339112d80aaa6e9d4ba045a776fbe2e44f849de801cce'
BASE_RECEIPT_SHA='1dffa961d83010bc496009434b113690d9a9506932acbb71bcbf1718a55ed80f'
STATUS='DEVOURER_HISTORICAL_TOOL_CANDIDATE_PHASE_SCOPED_VALIDATION_PASS'
LAYERS=[
 ('native_listener','native_spell_listener_leaf_partial_candidate_20261109','46ceb12b81c5db0c417933482d6572f3c89693d2ba3ef2d507ccebc5f0ed4ec7','e31eb74faca1a774b42a7c8bcef11b1592eae64ad350b08fa930f9a1d7cd64fe','9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111',247,5),
 ('earth_mother','earth_mother_helper_leaf_partial_candidate_20261109','333aad27ba8ed0d0699c97cd4a33be5494310247a8350993532cd725f26e753c','9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111','d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960',79,4),
 ('golden_source','native_golden_source_leaf_partial_candidate_20261109','181a6415d954795e0b40286165c39a55d0469745185e7e6d24840eb769025cef','d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960','c0454c30ce7eb2a71fb8ea3e513f0db0d2fd684f63129a1b7da2e4a47666603b',71,3),
 ('golden_tool','golden_arrow_tool_patch_reconstruction_candidate_20261109','3122135a4912a58c361b522e67b946dffbbe29b3618051972a4898e8cac7edd9','c0454c30ce7eb2a71fb8ea3e513f0db0d2fd684f63129a1b7da2e4a47666603b','bfd5d82ede8559200aed89547e4584ac091873a9392079af5ee20c41ea764a0a',98,1),
 ('megasaur_tool','megasaur_tool_fixed_pin_candidate_20261109','27514275c7204a972de2a5193b93deb35c7d4a72b137d1bc5c9477c2f7e9cf66','bfd5d82ede8559200aed89547e4584ac091873a9392079af5ee20c41ea764a0a','28b1d1c523dfc566bc5eacd04ccea1e1787c1b15e0cca8f9e67ecf9229b46bf4',143,1),
 ('batch1_tools','historical_tools_batch1_candidate_20261109','d4de01b2fa7a530c00b383455e94f1a0da62d81c68b03b4205b90aca1c46aea1','28b1d1c523dfc566bc5eacd04ccea1e1787c1b15e0cca8f9e67ecf9229b46bf4','53da1c13fbebb6eb8c5672ad8828109720efdfab1a8a97b6792a6da3202e6080',199,5),
 ('batch2_tools','historical_tools_batch2_four_candidate_20261109','51263c49a09a0a735a417e147e4f64f0529be4d5fa12529807653da7187693eb','53da1c13fbebb6eb8c5672ad8828109720efdfab1a8a97b6792a6da3202e6080','3581d683af1a208f00c3dd853e268d799abc5e2811847954a339cad2a68434ea',282,4),
 ('batch4_tools','historical_tools_batch4_three_candidate_20261109','85e5b08ccafa5dde8ecc02bdd24ecb740a5eb20baf2a81329e8c52b61773cc20','3581d683af1a208f00c3dd853e268d799abc5e2811847954a339cad2a68434ea',BASE_MAP_SHA,155,3)]

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
 for name in ['native-archive','earth-archive','golden-archive','golden-tool-archive','megasaur-archive','batch1-archive','batch2-archive','batch4-archive']:p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--download-dir',type=Path);p.add_argument('--baseline-receipt',type=Path);p.add_argument('--baseline-manifest',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 out=a.output.resolve();baseline=a.historical_baseline.resolve();require(not out.exists() and baseline not in out.parents,'Output must be new and outside baseline');out.mkdir(parents=True);free_before=shutil.disk_usage(out).free
 fresh=a.download_dir is None;d=a.download_dir.resolve() if a.download_dir else out/'downloaded'
 if fresh:d.mkdir();get(BASE_URL+'MANIFEST.json',d/'MANIFEST.json')
 require(file_meta(d/'MANIFEST.json')['sha256']==MANIFEST_SHA,'Pinned manifest mismatch');m=read_json(d/'MANIFEST.json');require(m['sha256']==ARCHIVE_SHA and m['bytes']==2558872 and len(m['files'])==137 and len(m['parts'])==11,'Package metadata mismatch')
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
 leaves=['tools/'+x+'_patterns.py' for x in ['devourer_souls']];changes={'added':leaves,'modified':[],'removed':[]}
 require(len(base)==27911 and len(target)==27912 and set(delta)==set(leaves)==set(target)-set(base) and {**base,**delta}==target,'Not the exact single-file addition')
 require(sum(x['bytes'] for x in target.values())==1549132284 and sum(x['bytes'] for x in delta.values())==41205,'Target size mismatch')
 for n in target:require(safe(n),'Unsafe source path')
 require(read_json(d/'CHANGES.json')==changes and read_json(d/'REMOVALS.json')==m['removed_source_files']==[],'External change/removal mismatch')
 require(read_json(pkg/'CHANGES.json')==[{'path':n,'status':'added_byte_exact_historical_candidate_not_proven_latest','before':None,'after':delta[n]} for n in leaves],'Archived change record mismatch')
 result=read_json(pkg/'RESULT.json');require(result['status']==m['status']==STATUS and result['input_commit']==BASE_COMMIT and result['target']==leaves[0] and delta[leaves[0]]=={'bytes':result['bytes'],'sha256':result['sha256']} and result['Python_checks']==69 and result['successful_Godot_assertions']==414 and result['static_cross_checks']==38,'Candidate scope mismatch')
 for key in ['latest_installed_version_proven','tool_itself_in_current_admission_pins','full_Catalog_fingerprint_computed','full_Catalog_loaded','full_Game_tested','old_save_compatibility_verified','full_compiler_run','new_value_override_added']:require(result[key] is False,'Missing scope limitation: '+key)
 require(result['remaining_original_367_scope']==m['remaining_tools_reference_gaps_within_original_367']==353 and result['remaining_original_historical_68']==55,'Remaining gap scope mismatch')
 interruption=read_json(pkg/'PACKAGE_INTERRUPTION_NOTE.json');require(interruption['initial_archive_is_complete'] is False and interruption['initial_archive_bytes']==983132 and interruption['initial_archive_sha256']=='af7d0a1a43f34031e12224ab30146ee589f0f3bf63ee6f4f633e58dfc616e737' and m['initial_truncated_archive_uploaded'] is False and m['initial_truncated_archive_preserved'] is True,'Truncated archive scope mismatch')
 for arg,name,urlname,expected in [(a.baseline_manifest,'PINNED_INPUT_MANIFEST.json','MANIFEST.json',BASE_MANIFEST_SHA),(a.baseline_receipt,'PINNED_INPUT_RECEIPT.json','HISTORICAL_TOOLS_BATCH4_STREAM_VERIFICATION.json',BASE_RECEIPT_SHA)]:
  dest=out/name
  if arg:dest.write_bytes(arg.read_bytes())
  else:get(BASE_URL_PRIOR+urlname,dest)
  require(file_meta(dest)['sha256']==expected,'Pinned dependency hash mismatch')
 dep=read_json(out/'PINNED_INPUT_MANIFEST.json');receipt=read_json(out/'PINNED_INPUT_RECEIPT.json')
 require(m['depends_on']['recovery_commit']==BASE_COMMIT and m['depends_on']['archive_sha256']==dep['sha256']==LAYERS[7][2] and m['depends_on']['manifest_sha256']==BASE_MANIFEST_SHA and m['depends_on']['receipt_sha256']==BASE_RECEIPT_SHA,'Dependency pointers mismatch')
 require(receipt['status']=='PASS_EXACT_STREAMED_SOURCE_MAP_BYTES_WITH_THREE_HISTORICAL_TOOLS' and receipt['source_map_sha256']==BASE_MAP_SHA and receipt['historical_baseline_and_prior_archives_unchanged'] is True and receipt['full_game_validation_passed'] is False,'Pinned receipt scope mismatch')
 historical=None;composed=None;overlays={};origin_by_path={};prior_members=[]
 archives=[a.native_archive,a.earth_archive,a.golden_archive,a.golden_tool_archive,a.megasaur_archive,a.batch1_archive,a.batch2_archive,a.batch4_archive]
 for index,(path,layer) in enumerate(zip(archives,LAYERS)):
  label,root,expected,bhash,thash,count,delta_count=layer
  oldmembers,keep=archive_verify(path,expected,root,dep if index==7 else None)
  require(len(oldmembers)==count and sha(keep['BASE_MAP.json'])==bhash and sha(keep['SOURCE_MAP.json'])==thash,'Prior archive map/count mismatch')
  oldbase=json.loads(keep.pop('BASE_MAP.json'));oldtarget=json.loads(keep.pop('SOURCE_MAP.json'))
  current_delta={n.removeprefix('delta/'):b for n,b in keep.items() if n.startswith('delta/')};require(len(current_delta)==delta_count,'Prior delta count mismatch')
  delta_meta={n:meta(b) for n,b in current_delta.items()};require({n:v for n,v in oldtarget.items() if oldbase.get(n)!=v}==delta_meta and {**oldbase,**delta_meta}==oldtarget,'Prior source delta/removal continuity mismatch')
  if historical is None:historical=oldbase;composed=dict(oldbase)
  require(composed==oldbase,'Adjacent archive map mismatch');composed.update(delta_meta);require(composed==oldtarget,'Layer composition mismatch')
  overlays.update(current_delta);origin_by_path.update({n:label for n in current_delta});prior_members.append({'archive':root+'.tar.xz','sha256':expected,'members_reverified':count,'source_files':delta_count,'freshly_downloaded_this_round':False})
  del oldbase,oldtarget,keep,current_delta,oldmembers,delta_meta;gc.collect()
 require(composed==base,'Eight historical layers do not match direct input');del composed;gc.collect()
 check_tree(baseline,historical,'historical baseline before')
 def actual_bytes(name):return overlays[name] if name in overlays else (baseline/name).read_bytes()
 provenance=read_json(pkg/'PROVENANCE.json');cfg=read_json(pkg/'CONFIG.json');name=leaves[0];restored=(pkg/'delta'/name).read_bytes()
 require(provenance['target']==cfg['target']==name and restored==actual_bytes(provenance['original'])==(pkg/'evidence/historical'/provenance['original']).read_bytes() and meta(restored)==delta[name],'Historical original mismatch')
 require(provenance['candidate_latest_installed_version_proven'] is False,'Historical version boundary changed')
 for path,expected in provenance['evidence_files'].items():
  require(safe(path),'Unsafe evidence path');evidence=(pkg/'evidence/historical'/path).read_bytes();require(meta(evidence)==expected and evidence==actual_bytes(path),'Evidence differs from actual baseline')
  if path.endswith('/integration_manifest.json'):
   matches=[x for x in json.loads(evidence) if x.get('path')==name];require(len(matches)==1 and matches[0]['after_sha256']==sha(restored),'Historical installation mismatch')
  if path.endswith('/shared_manifest.json'):
   matches=[x for x in json.loads(evidence) if x.get('install_path')==name];require(len(matches)==1 and matches[0]['after_sha256']==sha(restored),'Shared installation mismatch')
 source=actual_bytes(cfg['source']);require(source==(pkg/'probe_inputs'/cfg['source']).read_bytes(),'Current source mismatch')
 constant=lambda key:json.loads(re.search('^const '+key+r'[^=]*=(.*)$',source.decode(),re.M)[1])
 pins=constant('PROOF_SHA256');require(len(pins)==15 and name not in pins,'Wrong current pin scope')
 for pin,expected in pins.items():require(safe(pin) and sha(actual_bytes(pin))==expected,'Current fixed pin mismatch')
 values={};module=ast.parse(restored)
 for node in module.body:
  if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
   try:values[node.targets[0].id]=ast.literal_eval(node.value)
   except (TypeError,ValueError):pass
 for key in ['RAW','EXPECTED','VALUE_OVERRIDE']:require(values[key]==constant(key),'Current literal mismatch: '+key)
 override=values['VALUE_OVERRIDE'];require(override==json.loads(actual_bytes(cfg['override_path'])) and pins[cfg['override_path']]==sha(actual_bytes(cfg['override_path'])),'Existing override pin mismatch')
 require(override['fields']=={'attack':1,'health':3} and [x for x in json.loads(actual_bytes('data/catalog_value_overrides.json'))['overrides'] if x['id']==override['id']]==[override],'Independent golden/global existing override mismatch')
 import xml.etree.ElementTree as ET
 xml=ET.fromstring(actual_bytes(cfg['native_xml_path']));entity=xml if xml.tag=='Entity' else xml.find('.//Entity');require(entity is not None and entity.attrib.get('CardID')==override['id'] and entity.attrib.get('ID')=='103508','Native golden entity mismatch')
 tags={int(t.attrib['enumID']):t.attrib for t in entity.findall('Tag')};require(tags[47].get('value')=='1' and tags[45].get('value')=='3','Native golden 1/3 tags mismatch')
 raw_bytes,compiled_bytes=actual_bytes(cfg['raw_dependency_path']),actual_bytes(cfg['compiled_dependency_path']);raw,compiled=json.loads(raw_bytes),json.loads(compiled_bytes)
 reference=actual_bytes(cfg['raw_dependency_reference_source']);reference_pins=json.loads(re.search(rb'^const PROOF_SHA256[^=]*=(.*)$',reference,re.M)[1])
 require(reference_pins[cfg['raw_dependency_path']]==sha(raw_bytes)==cfg['raw_dependency_expected_sha256'] and pins[cfg['compiled_dependency_path']]==sha(compiled_bytes),'Raw/compiled dependency pins mismatch')
 require(values['DEPENDENCY_RAW']==raw and constant('DEPENDENCIES')==compiled and set(raw)==set(compiled) and len(raw)==4,'Raw/compiled dependency mismatch')
 allowed={'supported','effects','coverage_rule','coverage_text_sha256','default_pool','pool_supported'}
 for cid in raw:
  changed={key for key in set(raw[cid])|set(compiled[cid]) if key not in raw[cid] or key not in compiled[cid] or json.dumps(raw[cid][key],sort_keys=True)!=json.dumps(compiled[cid][key],sort_keys=True)}
  require(changed<=allowed,'Native dependency fields changed')
 ex=read_json(pkg/'evidence/CATALOG_CURRENT_EXCERPTS.json');catalog=actual_bytes('core/catalog.gd')
 fragment='func apply_existing_catalog_override(cards: Dictionary) -> void:'+chr(10)+ex['existing_override_application']['text']+chr(10)
 require(ex['sha256']==sha(catalog) and ex['existing_override_application']['text'] in catalog.decode() and fragment==(pkg/'existing_catalog_override_fragment.gd').read_text() and (pkg/'gate.gd').read_text().endswith(fragment),'Current Catalog excerpt/fragment mismatch')
 require({x['field'] for x in read_json(pkg/'CANONICAL_DIFFERENCE.json')}=={'field_status','value_override_verification'} and read_json(pkg/'INITIAL_COMPARISON_FAILURE.json')['initial_comparison_crossed_metadata_stages'] is True,'Initial comparison evidence missing')
 reports={}
 for mode in ['before','after','tamper']:
  reports[mode]=read_json(pkg/(mode+'_3')/'report.json');proc=read_json(pkg/(mode+'_3')/'PROCESS.json');portable=read_json(pkg/'portable_reports'/mode/'report.json')
  require(reports[mode]==portable and reports[mode]['checks']==69 and reports[mode]['failures']==[] and proc['exit']==0 and proc['reason']=='process_exit','Sealed successful report mismatch')
  for rel,record in read_json(pkg/(mode+'_INPUT_MAP.json')).items():require(safe(rel) and file_meta(pkg/(mode+'_runtime')/rel)==record,'Probe input map mismatch')
  initial=read_json(pkg/mode/'PROCESS.json');require(initial['exit']==-15 and initial['reason']=='controlled_script_error','Initial parse-stop evidence missing')
 require(len({r['segment_sha256'] for r in reports.values()})==3,'Missing three distinct segment fingerprints')
 for mode in ['after','tamper']:require([a.split(':')[0] for a,b in zip(reports['before']['entries'],reports[mode]['entries']) if a!=b]==[name] and len(reports['before']['entries'])==len(reports[mode]['entries']),'Unexpected fingerprint entry difference')
 require(read_json(pkg/'before_2/report.json')['failures']==['existing_Catalog_override_equals_compiler_input:BG_RLK_538_G'],'Initial numeric reference evidence missing')
 for rel in ['PACKAGE_MANIFEST_INITIAL.json','initial_test_compiler.py','gate_initial_fixture_reference_order.gd','gate_initial_mixed_indentation.gd']:require((pkg/rel).is_file(),'Missing preserved failed material')
 with tarfile.open(a.megasaur_archive,'r:xz') as previous:
  prefix='megasaur_tool_fixed_pin_candidate_20261109/evidence/tools_reference_inventory_20261109/';inventory_bytes=previous.extractfile(prefix+'FINAL_INVENTORY.json').read();internal=json.loads(previous.extractfile('megasaur_tool_fixed_pin_candidate_20261109/PACKAGE_MANIFEST.json').read());require(meta(inventory_bytes)==internal['evidence/tools_reference_inventory_20261109/FINAL_INVENTORY.json'],'Original inventory mismatch')
 inv=json.loads(inventory_bytes);require(len(inv)==367 and len({x['target'] for x in inv})==367 and sum(x['target'] not in base for x in inv)==354 and sum(x['target'] not in target for x in inv)==353,'Inventory gap counts mismatch')
 selected=read_json(pkg/'evidence/PRIOR_INVENTORY_TARGET.json');require(selected==next(x for x in inv if x['target']==name),'Selected inventory row mismatch')
 deferred_targets=['tools/'+x+'_patterns.py' for x in ['sinstone_sticker','ancient_wishbone','factory_line','balinda_spell','boogie_monster','partner_in_crime']]
 require(all(n not in base and n not in target and n not in delta for n in deferred_targets),'Prior deferred tool changed')
 print('PASS: historical original, installation evidence, 15 current pins, native 1/3 existing override, four dependency rows, preserved phase/harness failures, 353 gaps',flush=True)
 del inv,inventory_bytes;gc.collect()
 origins={'historical_tree':0,'native_listener':0,'earth_mother':0,'golden_source':0,'golden_tool':0,'megasaur_tool':0,'batch1_tools':0,'batch2_tools':0,'batch4_tools':0,'fresh_devourer_tool':0};reconstructed={};aggregate=hashlib.sha256()
 for name in sorted(target):
  if name in delta:h=(pkg/'delta'/name).open('rb');origin='fresh_devourer_tool'
  elif name in overlays:h=io.BytesIO(overlays[name]);origin=origin_by_path[name]
  else:
   source=baseline/name;require(source.is_file() and not source.is_symlink(),'Invalid historical source');h=source.open('rb');origin='historical_tree'
  digest=hashlib.sha256();count=0;aggregate.update(name.encode()+b'\0'+str(target[name]['bytes']).encode()+b'\0')
  with h:
   for b in iter(lambda:h.read(1024*1024),b''):digest.update(b);aggregate.update(b);count+=len(b)
  reconstructed[name]={'bytes':count,'sha256':digest.hexdigest()};require(reconstructed[name]==target[name],'Streamed target mismatch: '+name);origins[origin]+=1
 require(reconstructed==target and origins=={'historical_tree':27885,'native_listener':5,'earth_mother':4,'golden_source':3,'golden_tool':1,'megasaur_tool':1,'batch1_tools':5,'batch2_tools':4,'batch4_tools':3,'fresh_devourer_tool':1},'Final map/origin mismatch')
 check_tree(baseline,historical,'historical baseline after')
 for path,layer in zip(archives,LAYERS):require(file_meta(path)['sha256']==layer[2],'Historical archive changed')
 (out/'STREAM_RECONSTRUCTED_SOURCE_MAP.json').write_text(json.dumps(reconstructed,indent=2,sort_keys=True)+'\n');require(file_meta(out/'STREAM_RECONSTRUCTED_SOURCE_MAP.json')['sha256']==TARGET_MAP_SHA,'Canonical target map bytes differ')
 r={'status':'PASS_EXACT_STREAMED_SOURCE_MAP_BYTES_WITH_DEVOURER_HISTORICAL_TOOL','candidate_status':STATUS,'archive_commit':COMMIT,'repository_path':REPO_PATH,'manifest_sha256':MANIFEST_SHA,'archive_sha256':ARCHIVE_SHA,'archive_bytes':2558872,'parts_verified':11,'members_verified':137,'internal_manifest_members_verified':136,'input_verified_commit':BASE_COMMIT,'input_manifest_sha256':BASE_MANIFEST_SHA,'input_receipt_sha256':BASE_RECEIPT_SHA,'input_source_map_sha256':BASE_MAP_SHA,'source_map_sha256':TARGET_MAP_SHA,'historical_full_tree_files_rehashed_before_and_after':len(historical),'historical_tree_source_map_sha256':LAYERS[0][3],'prior_archive_verifications':prior_members,'direct_input_files_verified_by_actual_bytes':len(base),'target_files_streamed_and_verified':len(target),'actual_target_bytes_streamed':sum(v['bytes'] for v in target.values()),'stream_source_origins':origins,'aggregate_stream_sha256':aggregate.hexdigest(),'aggregate_stream_format':'Sorted UTF-8 target path, NUL, ASCII file byte count, NUL, actual file bytes; repeated for every target file.','change_lists':changes,'historical_original_and_supporting_evidence_match_actual_baseline_bytes':True,'historical_installation_and_shared_manifest_hashes_rechecked':True,'restored_python_ast_parse_passed':True,'current_source_literal_comparisons_passed':3,'current_source_pins_verified':15,'tool_itself_is_current_fixed_pin':False,'current_pin_constants_unchanged':True,'latest_installed_version_proven':False,'prior_inventory_before_items_preserved':367,'remaining_missing_within_inventory_scope':353,'remaining_historical_candidates_from_68':55,'upstream_inventory_and_selected_row_reverified':True,'inventory_scan_repeated_this_round':False,'inventory_scope':'Original 367 pre-restoration targets, not all possible tools gaps; 354 to 353 after this addition.','dependency_raw_and_compiled_entries_verified':4,'previously_deferred_six_targets_still_absent':deferred_targets,'raw_and_compiled_dependency_data_separately_checked_against_current_pins':True,'dependency_native_fields_unchanged':True,'existing_global_override_and_native_golden_1_3_verified':True,'new_override_added':False,'current_Catalog_excerpt_exact_bytes_verified':True,'initial_cross_stage_comparison_failure_preserved':True,'initial_three_parse_stops_and_numeric_reference_failure_preserved':True,'sealed_successful_phase_reports_checked_but_not_rerun':True,'initial_truncated_archive_uploaded':False,'initial_truncated_archive_preserved':True,'initial_compression_exit':137,'initial_compression_cause':'unknown','partial_validation_only':True,'full_game_validation_passed':False,'save_compatibility_verified':False,'full_catalog_fingerprint_executed':False,'full_compiler_executed':False,'gameplay_test_run_by_verifier':False,'Godot_proof_error_rerun_by_verifier':False,'candidate_Python_modules_executed_by_verifier':False,'whole_game_memory_improvement_verified':False,'complete_runtime_directory_created':False,'verification_mode':'Actual per-file bytes from reused Harbinger tree and eight pinned archive layers, plus freshly downloaded single-file Devourer delta; not merely map comparison.','historical_chain_freshly_downloaded_this_round':False,'increment_downloaded_by_this_helper':fresh,'increment_input_mode':'fresh immutable URLs' if fresh else 'Separately fetched pinned bytes; see FETCH_PROVENANCE.json proving all eleven part objects absent before fetch.','historical_baseline_and_prior_archives_unchanged':True,'missing_files_relative_to_source_map':[],'mismatched_files_relative_to_source_map':[],'unexpected_files_relative_to_source_map':[],'source_map_equality_does_not_establish_complete_game_recovery':True,'all_prior_backups_preserved':True,'no_deletion_performed':True,'free_disk_bytes_before':free_before,'free_disk_bytes_after':shutil.disk_usage(out).free,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 (out/'DEVOURER_HISTORICAL_TOOL_STREAM_VERIFICATION.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2),flush=True)
if __name__=='__main__':main()
