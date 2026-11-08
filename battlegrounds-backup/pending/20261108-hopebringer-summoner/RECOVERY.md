# Recover Hopebringer Summoner source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Strider with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/f4e2486527edb76e503faf8996f8a9f78f98560f/battlegrounds-backup/pending/20261108-hopebringer-strider/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Strider recovery directory containing restored_hopebringer_strider_runtime, hopebringer_strider/extracted/hopebringer_strider_20261108/SOURCE_MAP.json, and HOPEBRINGER_STRIDER_REMOTE_CHAIN_VERIFICATION.json.

Required Strider map SHA256: 3abb943757c53ed71ccec8b444fdcd7a458d6c96802086c1fa92190ed0ffcdc4. Required Strider receipt SHA256: 9ce81daf319ee4c8b0c045e2985cf8f92af1cb279a394d646ea8c14f42ae2ac6.

## Restore this increment

Place verify_and_restore_hopebringer_summoner.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_summoner.py --hopebringer-strider-recovery /path/to/strider_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 1904961b8460197b6292ef4b3b1e63f1b8397e73, folder battlegrounds-backup/pending/20261108-hopebringer-summoner. Archive hopebringer_summoner_20261108.tar.xz is 1,619,676 bytes, SHA256 3eed301ed728988735f7e376e878ee3e7422c9d8882becacb5fbde1dc62a5fdd. It verifies all part hashes, archive hash, 37 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/three additions/zero removals.

Every Strider baseline file is fully rehashed before copying. The independent restored_hopebringer_summoner_runtime must have exactly 27,878 files / 1,548,645,996 bytes, SOURCE_MAP SHA256 a69c018df9169a5f71670d4e88fa164038ae8a92b53f2ac9b4975c7c86aaf7a6. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Summoner increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Strider receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
