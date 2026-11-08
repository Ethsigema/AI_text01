# Recover Hopebringer Twilight source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Gorm with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/69e94cb46336b8ea8d6740f86439a3da5af1b314/battlegrounds-backup/pending/20261108-hopebringer-gorm/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Gorm recovery directory containing restored_hopebringer_gorm_runtime, hopebringer_gorm/extracted/hopebringer_gorm_20261108/SOURCE_MAP.json, and HOPEBRINGER_GORM_REMOTE_CHAIN_VERIFICATION.json.

Required Gorm map SHA256: 27884941a70c355e56ad91b8ab282927be1edaa52d5eab34832706bb9f79cca1. Required Gorm receipt SHA256: 27d0c76ffc3c5ec5d9c109cf6486d064664215fc5a9c328b6ae7a20920417d15.

## Restore this increment

Place verify_and_restore_hopebringer_twilight.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_twilight.py --hopebringer-gorm-recovery /path/to/gorm_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit a8445be78ea0aeadf79ef4ae429453e3ded8ec57, folder battlegrounds-backup/pending/20261108-hopebringer-twilight. Archive hopebringer_twilight_20261108.tar.xz is 1,614,164 bytes, SHA256 4d8e9d06f1f7e2a086d36835ad8437e672d1486edd7a097a2f9b782660411cc5. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Gorm baseline file is fully rehashed before copying. The independent restored_hopebringer_twilight_runtime must have exactly 27,865 files / 1,548,599,027 bytes, SOURCE_MAP SHA256 c579c174b7659d977f92dc89a2fcf82d7c83006b525dd539b49b784e78202345. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Twilight increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Gorm receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
