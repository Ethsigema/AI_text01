# Recover Hopebringer Sushi source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Kalecgos with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/c169e598ee03c7b069a9f9ba6bc314b37250701c/battlegrounds-backup/pending/20261108-hopebringer-kalecgos/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Kalecgos recovery directory containing restored_hopebringer_kalecgos_runtime, hopebringer_kalecgos/extracted/hopebringer_kalecgos_20261108/SOURCE_MAP.json, and HOPEBRINGER_KALECGOS_REMOTE_CHAIN_VERIFICATION.json.

Required Kalecgos map SHA256: c7b7e6e47b59346f7c2e1f9799ad631c2e074c802f46b21a1ba444abcb645c71. Required Kalecgos receipt SHA256: 0d6b106f76561e15666a64977bc652f984335967b3e1748db94d2ebb4331ba89.

## Restore this increment

Place verify_and_restore_hopebringer_sushi.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_sushi.py --hopebringer-kalecgos-recovery /path/to/kalecgos_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit d99914656d556823cb29716756e520dc3af748bb, folder battlegrounds-backup/pending/20261108-hopebringer-sushi. Archive hopebringer_sushi_20261108.tar.xz is 1,592,560 bytes, SHA256 c9434ded0c92ecc03c5f89bdc2a37e16b95be2568c73772b35013598f2a26c6e. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Kalecgos baseline file is fully rehashed before copying. The independent restored_hopebringer_sushi_runtime must have exactly 27,844 files / 1,548,522,793 bytes, SOURCE_MAP SHA256 79affdba332bb0ab59d6cfc4a56a86b2b8a08ae42e2e2efe860db26a0d81bad7. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Sushi increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Kalecgos receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
