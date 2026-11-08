# Recover Hopebringer Tempest source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Mindmuck with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/f2f3ddd014b455db68679fed6cabd44314ac134f/battlegrounds-backup/pending/20261108-hopebringer-mindmuck/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Mindmuck recovery directory containing restored_hopebringer_mindmuck_runtime, hopebringer_mindmuck/extracted/hopebringer_mindmuck_20261108/SOURCE_MAP.json, and HOPEBRINGER_MINDMUCK_REMOTE_CHAIN_VERIFICATION.json.

Required Mindmuck map SHA256: d18852cb8aa7c99d31e6d9ebb297f6151e4a1a8639e3401292c601470bf7a0e7. Required Mindmuck receipt SHA256: fadae46de41370f8f4b761cddcb59b79aeb9c3bb5a21e74aab96372a260978d8.

## Restore this increment

Place verify_and_restore_hopebringer_tempest.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_tempest.py --hopebringer-mindmuck-recovery /path/to/mindmuck_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 753edcc791ab61c2e9f78e05dd7e302b6cad4147, folder battlegrounds-backup/pending/20261108-hopebringer-tempest. Archive hopebringer_tempest_20261108.tar.xz is 1,604,236 bytes, SHA256 bcf4c0fcbaefc9ceebd7892194131ee3fb41150242b762a8dcf9c58d3e06cc31. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Mindmuck baseline file is fully rehashed before copying. The independent restored_hopebringer_tempest_runtime must have exactly 27,858 files / 1,548,570,897 bytes, SOURCE_MAP SHA256 de48bfbed3023efe269dd77bace9008480f685d2a9a18b75e2fc4bdb03eee229. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Tempest increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Mindmuck receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
