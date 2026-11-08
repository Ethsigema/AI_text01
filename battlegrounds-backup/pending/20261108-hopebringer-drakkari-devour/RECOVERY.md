# Recover Hopebringer Drakkari Devour source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Executor with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/927b729762c1733787a658f8e4eaa893d441a94d/battlegrounds-backup/pending/20261108-hopebringer-executor/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Executor recovery directory containing restored_hopebringer_executor_runtime, hopebringer_executor/extracted/hopebringer_executor_20261108/SOURCE_MAP.json, and HOPEBRINGER_EXECUTOR_REMOTE_CHAIN_VERIFICATION.json.

Required Executor map SHA256: 40e55a22bbd70f972c6c8b0e7e61e880dbbf6c39f73d2f677f2964080ee51985. Required Executor receipt SHA256: 391c7ba4fe3127d32856013c16beabcf364af50c8788cbf8c8567d7c8c8ed56f.

## Restore this increment

Place verify_and_restore_hopebringer_drakkari_devour.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_drakkari_devour.py --hopebringer-executor-recovery /path/to/executor_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit d6bf08f56bbe2489444635371d7d5bce2f7d344e, folder battlegrounds-backup/pending/20261108-hopebringer-drakkari-devour. Archive hopebringer_drakkari_devour_20261108.tar.xz is 1,621,712 bytes, SHA256 932a6a77d0baa98fe16edc1987e25f23fa310cc89d0c42d0b225b3d58531a491. It verifies all part hashes, archive hash, 48 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Executor baseline file is fully rehashed before copying. The independent restored_hopebringer_drakkari_devour_runtime must have exactly 27,852 files / 1,548,550,717 bytes, SOURCE_MAP SHA256 2130f84b455c534c421306136727ca097327f4f9ccb08af6dfd914d4eca28def. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Drakkari Devour increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Executor receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
