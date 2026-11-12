"""Read/verify helpers; no work at import, no Godot, no upload."""
from pathlib import Path,PurePosixPath
import argparse,datetime,fcntl,gzip,hashlib,io,json,re,tarfile
import run_remote_lava_rebuy as runner
ROOT=Path(__file__).resolve().parent.parent

def sha(b):return hashlib.sha256(b).hexdigest()
def enc(v):return (json.dumps(v,sort_keys=True,indent=2)+'\n').encode()
def read(p):return json.loads(p.read_text())
def put(p,b):
 with p.open('xb') as f:f.write(b)
def safe(n):return isinstance(n,str) and bool(n) and not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and '\\' not in n
def parser(doc):
 p=argparse.ArgumentParser(description=doc);p.add_argument('--execute',action='store_true',required=True);p.add_argument('--source-commit');p.add_argument('--remote-root',type=Path,required=True);p.add_argument('--remote-folder');return p
def context(a):
 pub=read(ROOT/'SOURCE_PUBLICATION.json') if (ROOT/'SOURCE_PUBLICATION.json').exists() else {}
 commit=a.source_commit or pub.get('commit');folder=a.remote_folder or pub.get('remote_folder',pub.get('folder'))
 assert isinstance(commit,str) and re.fullmatch('[0-9a-f]{40}',commit)
 assert safe(folder) and folder.startswith('battlegrounds-backup/')
 if pub:assert pub['commit']==commit
 r=a.remote_root.resolve();assert ROOT in r.parents and not (r/'run_tree').exists()
 d=read(r/'FRESH_PACKAGE_DOWNLOAD_VERIFIED.json');assert d['source_commit']==commit
 assert d['files']==len(d['records']) and len({x['filename'] for x in d['records']})==d['files']
 for row in d['records']:
  n=row['filename'];assert safe(n) and '/' not in n
  b=(r/'package'/n).read_bytes();assert len(b)==row['bytes'] and sha(b)==row['sha256'],n
 m=read(r/'package/MANIFEST.json');raw=gzip.decompress((r/'package/SOURCE_MAP.json.gz').read_bytes());assert sha(raw)==m['source_map_sha256']==runner.FROZEN_SOURCE['source_map_sha256']
 assert m['aggregate_sha256']==runner.FROZEN_SOURCE['aggregate_sha256']
 restore=read(r/'INDEPENDENT_RESTORE_VERIFIED.json');validate_restore_shape(restore,r,m,commit)
 return r,commit,folder,m,json.loads(raw),d

def lock():
 f=(ROOT.parent/'develop_empty_ghost_20261112/.independent_full_game.lock').open('a');fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB);return f

def rows(p):
 out=[]
 for f in sorted(p.iterdir()):
  assert f.is_file() and not f.is_symlink()
  b=f.read_bytes();out.append(dict(name=f.name,bytes=len(b),sha256=sha(b),git_sha=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()))
 return out

def checksum(p):
 (p/'SHA256SUMS.txt').write_text(''.join(sha(f.read_bytes())+'  '+f.name+'\n' for f in sorted(p.iterdir()) if f.is_file() and f.name!='SHA256SUMS.txt'))

def verify_archive(data,meta):
 expected=meta.get('members',meta);seen={}
 if 'archive_sha256' in meta:assert sha(data)==meta['archive_sha256']
 with tarfile.open(fileobj=io.BytesIO(data),mode='r:xz') as t:
  for member in t:
   assert member.isfile() and safe(member.name) and member.name not in seen and member.name in expected
   b=t.extractfile(member).read();seen[member.name]={'bytes':len(b),'sha256':sha(b)}
 assert seen==expected
 return len(seen)

def archive(files,commit):
 out=io.BytesIO()
 with tarfile.open(fileobj=out,mode='w:xz') as t:
  for n,b in sorted(files.items()):
   assert safe(n);entry=tarfile.TarInfo(n);entry.size=len(b);entry.mode=0o644;entry.mtime=0;t.addfile(entry,io.BytesIO(b))
 data=out.getvalue();meta={'source_commit':commit,'archive_sha256':sha(data),'members':{n:{'bytes':len(b),'sha256':sha(b)} for n,b in files.items()}}
 verify_archive(data,meta);return data,meta

def outcome_metadata(summary,audit,final):
 """Pure decision: never promote an incomplete/failed suite to success."""
 assert summary['runtime_mode']==audit['runtime_mode']==runner.RUNTIME_MODE
 assert summary['two_runtime_copies'] is False and audit['two_runtime_copies'] is False
 accepted=audit.get('runner_suite_accepted') is True
 if accepted:
  assert final is not None and final['status']==runner.FINAL_STATUS
  assert summary['status']=='TESTS_VALIDATED_SOURCE_INTEGRITY_PASS' and summary['error'] is None
  assert len(final['tests'])==9 and set(final['tests'])=={x[0] for x in runner.TESTS}
  assert all(x['classification']=='executed_validated' for x in audit['tests'].values()) and len(audit['tests'])==9
  assert final['full_game_processes']==1 and not final['full_game_acceptance'] and not final['default_pool_promoted']
  return 'success'
 assert final is None, 'Conflicting success receipt cannot be packaged as failure'
 assert summary['status']=='FAILED_OR_INCOMPLETE_ATTEMPT'
 assert summary.get('error') is not None or len(summary['validated_tests'])<9
 return 'failure'

def validate_restore_shape(restore,r,m,commit):
 assert restore['status']=='PASS_REMOTE_UNACCEPTED_SINGLE_TREE_SOURCE_RESTORE_BYTES_ONLY'
 assert restore['source_commit']==commit and restore['source_map_sha256']==m['source_map_sha256']
 assert restore['fresh_base_checkpoint_then_single_target_tree'] is True and restore['separate_runtime_copy_created'] is False
 assert restore['game_started'] is False and restore['gameplay_acceptance'] is False
 assert Path(restore['restored_tree']).resolve()==r/'single_tree_restore/restored_snapshot'
 validate_tree_report(restore['restored'],m['source_files'],m['source_bytes'],m['aggregate_sha256'])

def validate_tree_report(row,files,size,aggregate):
 assert row['files']==files and row['bytes']==size and row['aggregate_sha256']==aggregate
 assert all(row[k]==[] for k in ['missing','extra','mismatched'])

def completed_single_tree_evidence(r,m,commit):
 names=['single_tree_restore/'+n for n in ['STARTED.json','BASE_RESTORE.log','BASE_RESTORE_CURRENT.json','BASE_FULL_CHECKPOINT.json','APPLY_STARTED.json','SINGLE_TREE_RESTORE_VERIFIED.json']]+['RESTORE.log']
 files={}
 for name in names:
  p=r/name;before=p.stat();b=p.read_bytes();after=p.stat()
  assert (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns) and b,name
  files['restore_execution/'+name]=b
 def obj(n):return json.loads(files['restore_execution/single_tree_restore/'+n])
 start=obj('STARTED.json');base=obj('BASE_RESTORE_CURRENT.json');checkpoint=obj('BASE_FULL_CHECKPOINT.json');apply=obj('APPLY_STARTED.json');done=obj('SINGLE_TREE_RESTORE_VERIFIED.json')
 assert start['status']=='STARTED_NOT_VERIFIED' and start['game_started'] is False and start['source_map_sha256']==m['source_map_sha256']
 assert Path(start['new_workspace']).resolve()==r/'single_tree_restore'
 assert base['status']=='PASS_ACTUAL_DISK_RESTORE_EVERY_FILE_REHASHED' and base['source_map_sha256']==m['base_map_sha256'] and base['gameplay_tested'] is False
 validate_tree_report(base,base['files'],base['bytes'],base['aggregate_sha256'])
 assert checkpoint['status']=='PASS_FRESH_BASE_COMPLETE_BEFORE_INPLACE_DELTA' and checkpoint['source_map_sha256']==base['source_map_sha256']
 validate_tree_report(checkpoint['tree'],base['files'],base['bytes'],base['aggregate_sha256'])
 assert apply['status']=='TARGET_NOT_YET_VERIFIED' and apply['changed']==len(m['changed_files']) and apply['removed']==m.get('removed',[])
 assert done['status']=='PASS_FRESH_SINGLE_TREE_CUMULATIVE_RESTORE' and done['source_map_sha256']==m['source_map_sha256']
 assert done['game_started'] is False and done['old_tree_modified'] is False and done['one_tree_reused_only_within_new_workspace'] is True
 assert done['base_checkpoint']==checkpoint['tree']
 for k in ['target','second_independent_read']:validate_tree_report(done[k],m['source_files'],m['source_bytes'],m['aggregate_sha256'])
 assert start['utc']<checkpoint['utc']<=apply['utc']<done['utc']
 assert json.loads(files['restore_execution/single_tree_restore/BASE_RESTORE.log'])==base
 assert 'PASS_FRESH_SINGLE_TREE_CUMULATIVE_RESTORE' in files['restore_execution/RESTORE.log'].decode()
 optional=r/'CANDIDATE_REMOTE_RESTORE_DOUBLE_REHASH.json'
 if optional.exists():
  b=optional.read_bytes();j=json.loads(b)
  assert j['status']=='PASS_CANDIDATE_AND_ONE_INDEPENDENT_FRESH_RESTORE_REHASH' and j['source_commit']==commit and j['source_map_sha256']==m['source_map_sha256']
  assert j['distinct_fresh_restore_tree_count']==1 and j['separate_runtime_copy_created'] is False and j['game_started'] is False and j['gameplay_acceptance'] is False
  for row in j['trees'].values():validate_tree_report(row,m['source_files'],m['source_bytes'],m['aggregate_sha256'])
  files['restore_execution/'+optional.name]=b
 return files
