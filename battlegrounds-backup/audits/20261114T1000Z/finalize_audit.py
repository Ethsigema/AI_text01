from pathlib import Path
import json,hashlib,gzip,datetime,collections
r=Path(__file__).resolve().parent; project=r/'restored/project'; pub=r/'publication';pub.mkdir(exist_ok=False)
def sha(b):return hashlib.sha256(b).hexdigest()
def js(p):return json.loads(p.read_text())
def out(n,d):
 p=pub/n;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:f.write(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat();d=js(r/'FRESH_DOWNLOAD_VERIFIED.json');restore=js(r/'restored/RESULT.json');m=js(r/'package/MANIFEST.json')
assert d['requested']==78 and d['passed']==78 and restore['files']==28011
assert all(x['status']=='PASS_DOWNLOADED_AND_HASHED' for x in d['records'])
raw=gzip.decompress(b''.join((r/'package'/x['name']).read_bytes() for x in m['manifest_parts']));assert sha(raw)==m['target_manifest_sha256'];target=json.loads(raw)
# Independently re-read all published source bytes after any scoped runtime test; caches only are excluded.
def scan(root):
 actual={};excluded=[]
 for p in sorted(root.rglob('*')):
  if not p.is_file():continue
  n=p.relative_to(root)
  if any(x in n.parts for x in ['.godot','__pycache__','.git']):excluded.append(str(n));continue
  assert not p.is_symlink(),str(n)
  b=p.read_bytes();actual[n.as_posix()]={'bytes':len(b),'sha256':sha(b)}
 return actual,excluded
actual,ex=scan(project);assert actual==target
current,cur_ex=scan(r.parent/'resume_unfinished_20261114/development')
comparison={'checked_at_utc':now,'known_development_tree_files':len(current),'known_development_tree_bytes':sum(x['bytes'] for x in current.values()),'added':sorted(set(current)-set(target)),'removed':sorted(set(target)-set(current)),'modified':sorted(n for n in set(current)&set(target) if current[n]!=target[n]),'excluded_cache_files':len(cur_ex),'unknown_interrupted_work_captured':False}
assert not any(comparison[k] for k in ['added','removed','modified'])
s=js(project/'data/current_scope_manifest.json');l=js(project/'docs/minion_acceptance/minion_acceptance_ledger.json');base=set(s['official']['minion_ids'])-set(s['excluded_aberration_minion_ids']);naga=set(s['naga_overlay']['minion_ids']);rows=l['minions'];assert len(base)==227 and len(naga)==20 and len(base|naga)==247 and len(rows)==247
scope={'scope_revision':s['revision'],'scope_is_verified_latest_complete_pool':False,'completed_types':None,'verified_latest_total_types':None,'candidate_types':len(base|naga),'base_types':len(base),'naga_overlay_types':len(naga),'ledger_rows':len(rows),'accepted_ledger_entries':sum(x['count_as_complete'] for x in rows),'ledger_status_counts':dict(collections.Counter(x['completion_status'] for x in rows)),'zero_accepted_means_unreviewed_not_zero_implemented':True,'completion_policy':l['completion_policy'],'source_progress_sha256':sha((project/'PROGRESS.md').read_bytes()),'source_ledger_sha256':sha((project/'docs/progress_ledger.json').read_bytes()),'source_scope_sha256':sha((project/'data/current_scope_manifest.json').read_bytes())}
test=js(r/'SCOPED_GAMEPLAY_CURRENT.json')
audit={'audit_time_utc':now,'scheduled_for_utc':'2026-11-14T10:00:00Z','repository_head_before_audit':'521a79120a43d27084583384fb3214c9e9fec9f8','published_source_increment':'5a1cd70bc1f818d5abde913d6482fb6573a15401','downloaded_inputs':78,'downloaded_bytes':sum(x['downloaded_bytes'] for x in d['records']),'fresh_download_only':True,'new_full_project_directory_created':True,'restore':restore,'target_manifest_sha256':sha(raw),'independent_post_test_all_source_bytes_rehashed':True,'post_test_excluded_cache_files':len(ex),'current_gameplay':test,'known_development_tree_comparison':comparison,'new_game_source_changes_this_audit':0,'new_game_source_backup_package_generated':False,'fallback_native_attachment_prepared':False,'attachment_reason':'Known latest development tree matches already published increment; current full remote recovery succeeded. No source delta generated and no audit document misrepresented as game backup.','unknown_unuploaded_work_captured':False,'interrupted_thread_status':'interrupted','old_backups_removed':False,'force_push':False,'cleanup_performed':False,'latest_content_full_functional_acceptance':False,'source_increment_changes':{'added':len(m['added']),'modified':len(m['modified']),'removed':len(m['removed'])}}
ledger={'audit_time_utc':now,'source_commit':audit['published_source_increment'],'minions':scope,'tavern_spells':{'completed':None,'verified_latest_total':None,'percent':None},'trinkets':{'completed':None,'verified_latest_total':None,'percent':None,'requested_scope':'Complete content of most recent live appearance'},'minion_percent':None,'new_complete_minion_credit':0,'retain_naga':True,'exclude_aberration_tribe':True,'new_hero_and_extra_system_development_paused':True,'full_game_accepted':False}
out('AUDIT_RESULT.json',audit);out('docs/progress_ledger.json',ledger);out('SCOPE_CURRENT.json',scope);out('LOCAL_SOURCE_COMPARISON_END.json',comparison)
for dst,src in [('FRESH_DOWNLOAD_VERIFIED.json','FRESH_DOWNLOAD_VERIFIED.json'),('DOWNLOAD_REQUESTS.json','DOWNLOAD_REQUESTS.json'),('PACKAGE_REMOTE_METADATA.json','PACKAGE_REMOTE_METADATA.json'),('BASE_RESTORE_CURRENT.json','restored/BASE_RESTORE.json'),('SOURCE_RESTORE_CURRENT.json','restored/SOURCE_RESTORE.json'),('FULL_CHAIN_RESTORE_CURRENT.json','restored/RESULT.json'),('SCOPED_GAMEPLAY_CURRENT.json','SCOPED_GAMEPLAY_CURRENT.json'),('LOCAL_SOURCE_COMPARISON_START.json','LOCAL_SOURCE_COMPARISON.json')]:out(dst,js(r/src))
for n in ['SCOPED_GAMEPLAY_CURRENT.log','SHA256_CURRENT.log','finalize_audit.py','download_verify.py','run_current_test.py']:
 (pub/n).write_bytes((r/n).read_bytes())
report=f'''# 2026年11月14日18点备份与审计\n\n## 本轮结果\n已从固定远端重新下载78项，共{audit['downloaded_bytes']:,}字节，全部包、依赖和清单分卷匹配固定SHA256。按原始基包 → batch14 → 累积源码 → 六文件台账overlay → 船难海盗增量的顺序，新建完整工程并逐文件重读核验：28,011文件、1,553,163,887字节，缺失/多余/不符均为0。不是复用旧工程或历史回执。测试后另一次完整重读仍匹配全量清单。\n\n[本轮核验源码增量](https://github.com/Ethsigema/AI_text01/tree/5a1cd70bc1f818d5abde913d6482fb6573a15401/battlegrounds-backup/increments/20261114-shipwrecked-discover-overflow)；[恢复顺序、依赖与环境](https://github.com/Ethsigema/AI_text01/blob/5a1cd70bc1f818d5abde913d6482fb6573a15401/battlegrounds-backup/increments/20261114-shipwrecked-discover-overflow/RECOVERY.md)。Godot 4.6.3，Python 3.12+，Linux headless定向测试。delta.tar.xz为20,876字节，SHA256：5e7c60b255b2fc24d22e4b7c0600fe1cde0eafef66de36e58848870d18a58cfe。\n\n对当前可访问开发树全部28,011文件的两次比对，均未发现超出5a1cd70的新改动。本轮不制造重复游戏增量，上传的是新增核验与进度记录，不是新的游戏包。未知旧中断线程仍为interrupted且目录不可访问，不能声称其未上传内容已捕获。当前恢复链核验成功，未产生失败补发游戏包或原生附件；没有把审计记录当作游戏备份。\n\n## 内容变化与实际测试\n最近已发布实质变化是船难海盗普通/金色的有限手牌容量不足场景，1修改、11新增、0移除，已纳入本轮完整恢复；本轮没有再次把该实现计为新功能，也没有重做或计入血缚耳环。\n\n本轮在新恢复源码上实际运行Godot定向测试：{test['status']}，退出码{test['exit_code']}，通过{test['passed_checks']}项。普通/金色各9/10手，共4次发动、6次发现选择，检查费用、次数、库存、UID、队列与烧牌；初始来源/金币/酒馆币手牌与发现池使用fixture，限定单来源、法术手牌、原艾德温未用技能及无额外观察者。此为本轮重测，不是本轮新实现。此前发布前73项、旧候选70项以及其他历史测试均不冒充本轮执行。没有验收完整法术池、自然获取/三连、混合观察者、其他英雄、存档或完整对局。\n\n## 三项进度\n随从：已完成数量待核实／总计数量待核实。候选清单247种（227基础＋20娜迦），范围为partial-37.0.2混合来源，不是已核实最新版完整总池。逐卡台账247项仍未审查，accepted=0只表示未逐卡认证，不等于实际实现0张。普通与金色完整规则及适用交互均有可靠功能验收，才按一种计完成；占位、注册、supported映射和局部测试不计完整。本次完整完成数新增0。\n\n酒馆法术、饰品：可靠已完成数与完整总数均待核实。三项百分比缺可信分子/分母，均不能计算。饰品按最近一次上线完整内容范围，保留娜迦，排除畸变怪；英雄与额外机制新增暂停。\n\n## 保留与阻塞\n旧备份、分卷、失败证据及依赖均保留，没有清理、删除、强推或改写历史。当前磁盘足够，不做冗余清理。仍待解决：未知未上传成果访问、完整最新版范围确认、逐卡普通/金色验收和全功能/旧存档验证。全量清单一致只证明已发布文件集的恢复性，不替代这些功能或覆盖验收。\n'''
(pub/'PROGRESS.md').write_text(report)
(pub/'SHA256SUMS.txt').write_text(''.join(sha(p.read_bytes())+'  '+p.relative_to(pub).as_posix()+'\n' for p in sorted(pub.rglob('*')) if p.is_file()))
print(json.dumps({'publication_files':len([p for p in pub.rglob('*') if p.is_file()]),'audit':audit,'scope_summary':{k:v for k,v in scope.items() if not k.endswith('sha256')}},ensure_ascii=False))
