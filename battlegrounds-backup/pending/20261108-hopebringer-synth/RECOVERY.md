# Recover Hopebringer Synth source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Tidecaller with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/6ee216e036aded8fbaca7ca3832c795cadc902b4/battlegrounds-backup/pending/20261108-hopebringer-tidecaller/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Tidecaller recovery directory containing restored_hopebringer_tidecaller_runtime, hopebringer_tidecaller/extracted/hopebringer_tidecaller_20261108/SOURCE_MAP.json, and HOPEBRINGER_TIDECALLER_REMOTE_CHAIN_VERIFICATION.json.

Required Tidecaller map SHA256: 46541e56bc2b577cd2532ac521451a1a93d67c36d05ec19dc9a2c5a0908d7da8. Required Tidecaller receipt SHA256: 4646406b4825a8401a9de5537d4da126cdaea2ac2a54de0ed8df4dc369893666.

## Restore this increment

Place verify_and_restore_hopebringer_synth.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_synth.py --hopebringer-tidecaller-recovery /path/to/tidecaller_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit f20d6e2de7687fded13ffe88de1f9f2008c6d71f, folder battlegrounds-backup/pending/20261108-hopebringer-synth. Archive hopebringer_synth_20261108.tar.xz is 1,583,904 bytes, SHA256 9fad160e51b9ea9bb9e900e76fc4c0c64042cc2da459953124c215db6332dd62. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Tidecaller baseline file is fully rehashed before copying. The independent restored_hopebringer_synth_runtime must have exactly 27,869 files / 1,548,612,708 bytes, SOURCE_MAP SHA256 d84abb3fdf815f3d3c29b2c7c7b603caaf17edffb23679a05a17960f4e4b8d6b. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Synth increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Tidecaller receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
