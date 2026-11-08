# Recover Hopebringer Tidecaller source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Twilight with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/943d3115d65fb6bbe880bc8e45a3be49dd5ecbb6/battlegrounds-backup/pending/20261108-hopebringer-twilight/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Twilight recovery directory containing restored_hopebringer_twilight_runtime, hopebringer_twilight/extracted/hopebringer_twilight_20261108/SOURCE_MAP.json, and HOPEBRINGER_TWILIGHT_REMOTE_CHAIN_VERIFICATION.json.

Required Twilight map SHA256: c579c174b7659d977f92dc89a2fcf82d7c83006b525dd539b49b784e78202345. Required Twilight receipt SHA256: 1260442ad8107aad13494fc5edf1905a8d93faab1894369f9c790fd82ca6be63.

## Restore this increment

Place verify_and_restore_hopebringer_tidecaller.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_tidecaller.py --hopebringer-twilight-recovery /path/to/twilight_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit fe9358d32cb53dabf90042689408d614882a1fef, folder battlegrounds-backup/pending/20261108-hopebringer-tidecaller. Archive hopebringer_tidecaller_20261108.tar.xz is 1,619,548 bytes, SHA256 c3865bfb0e61f41372627b8a984fca3e497c1324590ec8a0eace5b31f9b95451. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Twilight baseline file is fully rehashed before copying. The independent restored_hopebringer_tidecaller_runtime must have exactly 27,867 files / 1,548,605,979 bytes, SOURCE_MAP SHA256 46541e56bc2b577cd2532ac521451a1a93d67c36d05ec19dc9a2c5a0908d7da8. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Tidecaller increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Twilight receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
