# Recover Hopebringer Phantom source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Banshee with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/b9c2f662aaf564217f10d6893d7f81fabba3ead2/battlegrounds-backup/pending/20261108-hopebringer-banshee/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Banshee recovery directory containing restored_hopebringer_banshee_runtime, hopebringer_banshee/extracted/hopebringer_banshee_20261108/SOURCE_MAP.json, and HOPEBRINGER_BANSHEE_REMOTE_CHAIN_VERIFICATION.json.

Required Banshee map SHA256: f14143c5758249a34f6b837037aae9fd71a726c5a4d92de96bebc29675826883. Required Banshee receipt SHA256: f580a4188d98f8600f8a03e2b2dc132e95957f61dce1278b495a1f5f83730345.

## Restore this increment

Place verify_and_restore_hopebringer_phantom.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_phantom.py --hopebringer-banshee-recovery /path/to/banshee_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 4584362553c34a86b032899b3ceee92592c8c29a, folder battlegrounds-backup/pending/20261108-hopebringer-phantom. Archive hopebringer_phantom_20261108.tar.xz is 1,606,632 bytes, SHA256 3da24a625c2d219398c381e8dd2702615a00aa04a9a270409c5cf746e5175330. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Banshee baseline file is fully rehashed before copying. The independent restored_hopebringer_phantom_runtime must have exactly 27,873 files / 1,548,627,184 bytes, SOURCE_MAP SHA256 9617b0b0e4f823141049d41f0728b1aba2f306e729ae860bc16fd6647acd89ed. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Phantom increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Banshee receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
