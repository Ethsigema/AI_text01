# Recover Hopebringer Lookout source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Tempest with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/5f3989915b014b2e8b1b1c8a75d1c8f85f1acd0e/battlegrounds-backup/pending/20261108-hopebringer-tempest/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Tempest recovery directory containing restored_hopebringer_tempest_runtime, hopebringer_tempest/extracted/hopebringer_tempest_20261108/SOURCE_MAP.json, and HOPEBRINGER_TEMPEST_REMOTE_CHAIN_VERIFICATION.json.

Required Tempest map SHA256: de48bfbed3023efe269dd77bace9008480f685d2a9a18b75e2fc4bdb03eee229. Required Tempest receipt SHA256: cc5ff0af3f49d6883f11d067b5482bdebd01397a23b1aa3efd482cfced1eca29.

## Restore this increment

Place verify_and_restore_hopebringer_lookout.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_lookout.py --hopebringer-tempest-recovery /path/to/tempest_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 83e0675af41320886e6aed676d62aa46c3e3cf51, folder battlegrounds-backup/pending/20261108-hopebringer-lookout. Archive hopebringer_lookout_20261108.tar.xz is 1,664,652 bytes, SHA256 af1e76d62b2a4e3fdbc74b02a1dd3a08f95582150eada2481ba77877cc907a93. It verifies all part hashes, archive hash, 62 safe members and companion hashes, exact BASE_MAP continuity, and six modifications/two additions/zero removals.

Every Tempest baseline file is fully rehashed before copying. The independent restored_hopebringer_lookout_runtime must have exactly 27,860 files / 1,548,578,458 bytes, SOURCE_MAP SHA256 bc90ec2530f6e815459d2b6e9cd007832d2d49426af6cd3ea0ab7d7ad08d2c69. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Lookout increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Tempest receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
