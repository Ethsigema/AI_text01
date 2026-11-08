# Recover Hopebringer Executor source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Costume with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/8ef597733bb2ac0fe8eface4f901588b1d4c149b/battlegrounds-backup/pending/20261108-hopebringer-costume/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Costume recovery directory containing restored_hopebringer_costume_runtime, hopebringer_costume/extracted/hopebringer_costume_20261108/SOURCE_MAP.json, and HOPEBRINGER_COSTUME_REMOTE_CHAIN_VERIFICATION.json.

Required Costume map SHA256: 3f25aeca6742477e702ba19c7ee90f0af5d0528b8f37512d57115d5e8e7e56b0. Required Costume receipt SHA256: 40955b7bac81107a8c3d1e019d07ddcb0ed6c680c590a64c3d713d449dcde184.

## Restore this increment

Place verify_and_restore_hopebringer_executor.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_executor.py --hopebringer-costume-recovery /path/to/costume_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 494937c2cd2caaf19c53f3ff56a3ce85a5adb5cd, folder battlegrounds-backup/pending/20261108-hopebringer-executor. Archive hopebringer_executor_20261108.tar.xz is 1,601,824 bytes, SHA256 1402ee584d4a6e78cac7ca1fc91e806316ee61c6917b560a02fb61f2cbde2e73. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Costume baseline file is fully rehashed before copying. The independent restored_hopebringer_executor_runtime must have exactly 27,850 files / 1,548,543,144 bytes, SOURCE_MAP SHA256 40e55a22bbd70f972c6c8b0e7e61e880dbbf6c39f73d2f677f2964080ee51985. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Executor increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Costume receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
