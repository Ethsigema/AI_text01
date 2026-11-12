from pathlib import Path, PurePosixPath
import datetime, gzip, hashlib, json, tarfile

root=Path(__file__).resolve().parent
workspace=root.parent
def dump(name, value):
    (root/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def meta(p):
    with p.open('rb') as f:h=hashlib.file_digest(f,'sha256').hexdigest()
    return {'bytes':p.stat().st_size,'sha256':h}
base=json.loads(gzip.decompress((root/'base_package/SOURCE_MAP.json.gz').read_bytes()))
cm=json.loads((root/'candidate_package/MANIFEST.json').read_text())
candidate=dict(base)
for p in cm['removed']:candidate.pop(p)
candidate.update(cm['changed_files'])

# Read only the known pre-existing restored project copies. These are not the original active trees.
prior=[]
for name,expected in [('restored_base',base),('restored_shatterer_candidate',candidate)]:
    folder=workspace/'night_backup_check_20261111T1500Z'/name
    actual={p.relative_to(folder).as_posix():meta(p) for p in folder.rglob('*') if p.is_file() and not p.is_symlink()}
    result={'tree_role':'previous_audit_restoration_not_original_worktree','directory':str(folder.relative_to(workspace)),
            'files':len(actual),'bytes':sum(v['bytes'] for v in actual.values()),
            'missing':sorted(set(expected)-set(actual)),'extra':sorted(set(actual)-set(expected)),
            'mismatched':[p for p in expected if p in actual and actual[p]!=expected[p]]}
    result['status']='PASS_NO_FILE_CONTENT_CHANGES' if not any(result[k] for k in ['missing','extra','mismatched']) else 'CHANGES_FOUND'
    prior.append(result)
dump('PREEXISTING_RESTORED_TREES_CURRENT.json',{'checked_at_utc':now(),'trees':prior,'original_worktree_covered':False})

known=['game_working','game_candidate_shatterer','historical_tools_batch14_20261109T191857Z/runtime',
       'backup_batch14_20261109/fresh_remote_verification/REBUILT_SOURCE_MAP.json',
       'backup_batch16_20261109/fresh_remote_verification/isolated_restored_candidate',
       'night_backup_audit_20261109T1507Z/runtime_final_current']
dump('ORIGINAL_WORKTREE_VISIBILITY.json',{'checked_at_utc':now(),
     'known_paths':[{'path':p,'exists':(workspace/p).exists()} for p in known],
     'project_locations_before_current_restore':['night_backup_check_20261111T1500Z/restored_base/project.godot','night_backup_check_20261111T1500Z/restored_shatterer_candidate/project.godot'],
     'search_scope':'Visible /workspace and readable /tmp; initial search before current restorations. Restricted directories were not searched.',
     'cause_of_absent_worktree':'unknown','unuploaded_changes_cannot_be_ruled_out':True,'permanent_loss_claimed':False})

em=json.loads((root/'candidate_package/EVIDENCE_MANIFEST.json').read_text())
actual={}
with tarfile.open(root/'candidate_package/evidence.tar.xz','r:xz') as tf:
    for m in tf:
        p=PurePosixPath(m.name)
        assert m.isfile() and not p.is_absolute() and '..' not in p.parts and m.name not in actual
        b=tf.extractfile(m).read();actual[m.name]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
assert actual==em
dump('EVIDENCE_CURRENT.json',{'checked_at_utc':now(),'status':'PASS_ARCHIVE_AND_EVERY_EVIDENCE_MEMBER_HASHED','members':len(actual),
     'archive':meta(root/'candidate_package/evidence.tar.xz'),'old_logs_rerun':False,'engine_runs_this_audit':0})

# Static progress inspection is deliberately distinct from acceptance or runtime testing.
tree=root/'restored_base'
scope=json.loads((tree/'data/current_scope_manifest.json').read_text())
coverage=json.loads((tree/'data/runtime_coverage.json').read_text())
effect=json.loads((tree/'data/effect_coverage.json').read_text())
progress={'checked_at_utc':now(),'scope_manifest':{'path':'data/current_scope_manifest.json','hash':meta(tree/'data/current_scope_manifest.json'),
          'scope_id':scope['scope_id'],'status':scope['status'],'implementation_status':scope['implementation_status'],
          'patch_slice':scope['patch_slice'],'membership_patch_slice':scope['membership_patch_slice'],
          'policy':scope['policy'],'excluded_aberration_ids_count':len(scope['excluded_aberration_minion_ids']),
          'naga_overlay_ids_count':len(scope['naga_overlay']['minion_ids'])},
          'historical_coverage_not_current_acceptance':{'path':'data/runtime_coverage.json','hash':meta(tree/'data/runtime_coverage.json'),
             'generated_at_as_stored':coverage['generated_at'],'scope_as_stored':coverage['scope'],
             'by_kind_as_stored':{k:coverage['by_kind'][k] for k in ['minion','spell','trinket']},
             'unsupported_count_as_stored':len(coverage['unsupported'])},
          'effect_coverage_hash':meta(tree/'data/effect_coverage.json'),
          'new_complete_identity_credit':{'minions':0,'tavern_spells':0,'trinkets':0},
          'completion_percentages':{'minions':None,'tavern_spells':None,'trinkets':None},
          'reason':'Stored capability counts mix ordinary, golden and derived entities and are not current full-scope acceptance numerators or target denominators. The scope remains written_unverified. No gameplay test was run this audit.',
          'candidate_status':'Shatterer remains isolated and unpromoted; existing historical report was read, no historical test credited as a new run.'}
dump('PROGRESS_BASIS_CURRENT.json',progress)

contracts=['research/piranha_immediate_attack_recovery/SOURCE_CONTRACT.md','research/hand_murloc_gain_recovery/SOURCE_CONTRACT.md']
other=['tools/build_effect_catalog.py']
dump('REFERENCE_GAPS_CURRENT.json',{'checked_at_utc':now(),'contracts':{p:(tree/p).exists() for p in contracts},
     'other_selected_paths':{p:(tree/p).exists() for p in other},'historically_declared_missing_tools':345,
     'full_345_reference_inventory_recounted':False,'historically_unrecovered_old_evidence':4,
     'all_old_evidence_recounted':False,'scope':'Selected missing paths checked this cycle; declared 345-path count remains historical and is not a complete gameplay or dependency census.'})
print(json.dumps({'checked_at_utc':now(),'prior_tree_checks':[x['status'] for x in prior],'evidence_members':len(em),'progress_completion_rates':None}))
