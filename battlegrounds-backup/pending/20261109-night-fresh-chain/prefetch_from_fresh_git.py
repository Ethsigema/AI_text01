from pathlib import Path, PurePosixPath
import subprocess, json, hashlib, datetime
r=Path(__file__).resolve().parent
chain=json.loads((r/'PINNED_INCREMENT_CHAIN.json').read_text())
extensions=[
 ('golden_source','11e9e8188a23f62542aad8a43a2560aff9e3b402','20261109-native-golden-source-leaf-partial-candidate','181a6415d954795e0b40286165c39a55d0469745185e7e6d24840eb769025cef',71),
 ('golden_tool','edf067470abc889b166ea39d1cec97c3dcf7c528','20261109-golden-arrow-tool-patch-reconstruction-candidate','3122135a4912a58c361b522e67b946dffbbe29b3618051972a4898e8cac7edd9',98),
 ('megasaur_tool','a00e227da42ecf4563c324e7994ecf9c5a63dde8','20261109-megasaur-tool-fixed-pin-candidate','27514275c7204a972de2a5193b93deb35c7d4a72b137d1bc5c9477c2f7e9cf66',143),
 ('batch1_tools','1e60aed5d8555d76a0e81704e84ad15dacb737d2','20261109-historical-tools-batch1-candidate','d4de01b2fa7a530c00b383455e94f1a0da62d81c68b03b4205b90aca1c46aea1',199),
 ('batch2_tools','5d17cb79f7f7b6abdddb68e3b9e420e0167184b3','20261109-historical-tools-batch2-four-candidate','51263c49a09a0a735a417e147e4f64f0529be4d5fa12529807653da7187693eb',282),
 ('batch4_tools','e4b9f301a494c0623daebfd17d7b60fd933c4c6f','20261109-historical-tools-batch4-three-candidate','85e5b08ccafa5dde8ecc02bdd24ecb740a5eb20baf2a81329e8c52b61773cc20',155),
 ('devourer_tool','cfb226a7f5888740371748b49aeb5ad6eda445cf','20261109-devourer-tool-historical-candidate','c807dd1229f5c4480631a446c8b7b0aa3f00d48e4602bc91d7d23c1480fa5a44',137),
]
chain.extend(extensions)
(r/'PINNED_INCREMENT_CHAIN_CURRENT.json').write_text(json.dumps(chain,indent=2)+'\n')
assert not (r/'increments').exists()
proc=subprocess.Popen(['git','-C',str(r/'remote_repo'),'cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
records=[]
def get(commit,folder,name,dest):
 assert name and PurePosixPath(name).name==name and '\\' not in name
 path='battlegrounds-backup/pending/'+folder+'/'+name
 proc.stdin.write((commit+':'+path+'\n').encode());proc.stdin.flush()
 header=proc.stdout.readline().decode().strip().split()
 assert len(header)==3 and header[1]=='blob',header
 blob,n=header[0],int(header[2]);data=proc.stdout.read(n);assert len(data)==n and proc.stdout.read(1)==b'\n'
 assert hashlib.sha1(b'blob '+str(n).encode()+b'\0'+data).hexdigest()==blob
 with dest.open('xb') as f:f.write(data)
 records.append({'commit':commit,'path':path,'git_blob_sha':blob,'bytes':n,'sha256':hashlib.sha256(data).hexdigest(),'origin':'Fresh Git remote clone made during this audit; no prior-run object database','materialized_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
 return data
for label,commit,folder,expected,count in chain:
 d=r/'increments'/label;d.mkdir(parents=True)
 m=json.loads(get(commit,folder,'MANIFEST.json',d/'MANIFEST.json'))
 assert m['sha256']==expected and len(m['files'])==count
 for name,meta in [(p['name'],p) for p in m['parts']]+list(m.get('companion_files',{}).items()):
  b=get(commit,folder,name,d/name)
  assert len(b)==meta['bytes'] and hashlib.sha256(b).hexdigest()==meta['sha256']
 print(label,commit,flush=True)
proc.stdin.close();assert proc.wait()==0
(r/'FRESH_GIT_MATERIALIZATION_PROVENANCE.json').write_text(json.dumps(records,indent=2)+'\n')
print('DONE',len(chain),'packages',len(records),'objects',flush=True)
