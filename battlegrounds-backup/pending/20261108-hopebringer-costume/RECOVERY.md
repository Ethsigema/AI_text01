# Recover Hopebringer Costume source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Choral with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/7393d550fd8f6963c37cd13524d5adfbcb4115f4/battlegrounds-backup/pending/20261108-hopebringer-choral/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Choral recovery directory containing restored_hopebringer_choral_runtime, hopebringer_choral/extracted/hopebringer_choral_20261108/SOURCE_MAP.json, and HOPEBRINGER_CHORAL_REMOTE_CHAIN_VERIFICATION.json.

Required Choral map SHA256: 514c88f919c33e4b533233745a36ff0521a85848eebc27e9e05d0d1012d15cd1. Required Choral receipt SHA256: 727c96569fc708bea72ff2a64937c46487abf45bdb924158050586e0c041229c.

## Restore this increment

Place verify_and_restore_hopebringer_costume.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_costume.py --hopebringer-choral-recovery /path/to/choral_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 6fd696dc3ef0f3288ffc5e129c5934c8a2684c3a, folder battlegrounds-backup/pending/20261108-hopebringer-costume. Archive hopebringer_costume_20261108.tar.xz is 1,593,632 bytes, SHA256 e01f587c685e19624723e276aef2fcba1659901451772dc435e75a98c683cf2f. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Choral baseline file is fully rehashed before copying. The independent restored_hopebringer_costume_runtime must have exactly 27,848 files / 1,548,536,389 bytes, SOURCE_MAP SHA256 3f25aeca6742477e702ba19c7ee90f0af5d0528b8f37512d57115d5e8e7e56b0. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Costume increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Choral receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
