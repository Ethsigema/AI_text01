# Recover Hopebringer Choral source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Sushi with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/4008acad359b6a6fb8143de0a2489490d086bc4a/battlegrounds-backup/pending/20261108-hopebringer-sushi/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Sushi recovery directory containing restored_hopebringer_sushi_runtime, hopebringer_sushi/extracted/hopebringer_sushi_20261108/SOURCE_MAP.json, and HOPEBRINGER_SUSHI_REMOTE_CHAIN_VERIFICATION.json.

Required Sushi map SHA256: 79affdba332bb0ab59d6cfc4a56a86b2b8a08ae42e2e2efe860db26a0d81bad7. Required Sushi receipt SHA256: 89184e5a1660d2741d0b6590746ddaf78eafbd68e93e13c06bff884890529dc5.

## Restore this increment

Place verify_and_restore_hopebringer_choral.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_choral.py --hopebringer-sushi-recovery /path/to/sushi_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit efa6466a49c6e924d1a3409c9153beb998f8198c, folder battlegrounds-backup/pending/20261108-hopebringer-choral. Archive hopebringer_choral_20261108.tar.xz is 1,592,864 bytes, SHA256 77fb35c87ee9cad8038ced9012c8798b43d4a53ebfa9e528d3569e0333678bd4. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Sushi baseline file is fully rehashed before copying. The independent restored_hopebringer_choral_runtime must have exactly 27,846 files / 1,548,529,188 bytes, SOURCE_MAP SHA256 514c88f919c33e4b533233745a36ff0521a85848eebc27e9e05d0d1012d15cd1. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Choral increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Sushi receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
