# Recover Hopebringer Tycoon source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Summoner with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/fbfae030439b83859bc82b3be1fb42e4e72195bd/battlegrounds-backup/pending/20261108-hopebringer-summoner/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Summoner recovery directory containing restored_hopebringer_summoner_runtime, hopebringer_summoner/extracted/hopebringer_summoner_20261108/SOURCE_MAP.json, and HOPEBRINGER_SUMMONER_REMOTE_CHAIN_VERIFICATION.json.

Required Summoner map SHA256: a69c018df9169a5f71670d4e88fa164038ae8a92b53f2ac9b4975c7c86aaf7a6. Required Summoner receipt SHA256: 407b7d0b7de6e60f44befcf4fdcd2684d59a9b327cf45ba9ff91037f3113383e.

## Restore this increment

Place verify_and_restore_hopebringer_tycoon.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_tycoon.py --hopebringer-summoner-recovery /path/to/summoner_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 40ee9b3883b19226d252f9fc7b1c7f8e38fa5643, folder battlegrounds-backup/pending/20261108-hopebringer-tycoon. Archive hopebringer_tycoon_20261108.tar.xz is 1,632,412 bytes, SHA256 032055ad0dfad78ad88ee3270efd2a78b18c8d99f6c6bd43e4e147c878933e41. It verifies all part hashes, archive hash, 37 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Summoner baseline file is fully rehashed before copying. The independent restored_hopebringer_tycoon_runtime must have exactly 27,880 files / 1,548,652,434 bytes, SOURCE_MAP SHA256 1ae20915de380fa09051261af4e1aae1abe07f7d9f682dbbca00c3da04619135. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Tycoon increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Summoner receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
