# Recover Hopebringer Gorm source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Lookout with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/b01330c40a4928f717fa53b055a94254d38059b0/battlegrounds-backup/pending/20261108-hopebringer-lookout/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Lookout recovery directory containing restored_hopebringer_lookout_runtime, hopebringer_lookout/extracted/hopebringer_lookout_20261108/SOURCE_MAP.json, and HOPEBRINGER_LOOKOUT_REMOTE_CHAIN_VERIFICATION.json.

Required Lookout map SHA256: bc90ec2530f6e815459d2b6e9cd007832d2d49426af6cd3ea0ab7d7ad08d2c69. Required Lookout receipt SHA256: 6e94c0f048e6e333a995b6c82954c7d1c0ea78c31fa12df38b1df0379596c90c.

## Restore this increment

Place verify_and_restore_hopebringer_gorm.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_gorm.py --hopebringer-lookout-recovery /path/to/lookout_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 43a1cc782127d69f967c6d5020efe9ae786dfb91, folder battlegrounds-backup/pending/20261108-hopebringer-gorm. Archive hopebringer_gorm_20261108.tar.xz is 1,599,248 bytes, SHA256 f114bef418e6cada8fb58ec92177eb501023d31b19db2abd8cd644b1d8a0bb8c. It verifies all part hashes, archive hash, 37 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/three additions/zero removals.

Every Lookout baseline file is fully rehashed before copying. The independent restored_hopebringer_gorm_runtime must have exactly 27,863 files / 1,548,592,165 bytes, SOURCE_MAP SHA256 27884941a70c355e56ad91b8ab282927be1edaa52d5eab34832706bb9f79cca1. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Gorm increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Lookout receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
