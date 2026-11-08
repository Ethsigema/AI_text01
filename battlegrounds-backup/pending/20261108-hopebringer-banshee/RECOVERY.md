# Recover Hopebringer Banshee source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Synth with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/89dc5e76342a57c249a73b5f089e60fd2dfbb712/battlegrounds-backup/pending/20261108-hopebringer-synth/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Synth recovery directory containing restored_hopebringer_synth_runtime, hopebringer_synth/extracted/hopebringer_synth_20261108/SOURCE_MAP.json, and HOPEBRINGER_SYNTH_REMOTE_CHAIN_VERIFICATION.json.

Required Synth map SHA256: d84abb3fdf815f3d3c29b2c7c7b603caaf17edffb23679a05a17960f4e4b8d6b. Required Synth receipt SHA256: eae3feb10ad306578c0cf268ce817e1850e639429a3fbc56f5ca24bec248f49b.

## Restore this increment

Place verify_and_restore_hopebringer_banshee.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_banshee.py --hopebringer-synth-recovery /path/to/synth_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit df9c23a088e88f0b06c6aa01b8907ca2237700d2, folder battlegrounds-backup/pending/20261108-hopebringer-banshee. Archive hopebringer_banshee_20261108.tar.xz is 1,606,472 bytes, SHA256 8da9b9bb11f3f0af65d4014804acba2e3a4956894ffb7dd46f8ed9b2675fec6e. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Synth baseline file is fully rehashed before copying. The independent restored_hopebringer_banshee_runtime must have exactly 27,871 files / 1,548,619,751 bytes, SOURCE_MAP SHA256 f14143c5758249a34f6b837037aae9fd71a726c5a4d92de96bebc29675826883. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Banshee increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Synth receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
