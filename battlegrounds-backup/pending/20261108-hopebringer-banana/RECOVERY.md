# Recover Hopebringer Banana source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Amber with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/ce32d27a35fcd141af0b417423fd337efd92f657/battlegrounds-backup/pending/20261108-hopebringer-amber/RECOVERY.md

That recipe specifies the original November 1 release ZIP, pinned recovery and Bloodbound Git sources, the complete Mummifier chain, and composition of Blade plus Mummifier followed by Amber. Retain the Amber recovery directory containing restored_hopebringer_amber_runtime, hopebringer_amber/extracted/hopebringer_amber_20261108/SOURCE_MAP.json, and HOPEBRINGER_AMBER_REMOTE_CHAIN_VERIFICATION.json.

Required Amber map SHA256: b561cff2dc05128e28ccdd6363c9116b0275ab3c3428b48e5f4db9979559ffc7. Required Amber receipt SHA256: 1ce989aab7e1d512e8a8a3af214c22d93113299720293986028ea12337395f6c.

## Restore this increment

Place verify_and_restore_hopebringer_banana.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_banana.py --hopebringer-amber-recovery /path/to/amber_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 76100de1a7391e400d3d3d8c529aa84394431d53, folder battlegrounds-backup/pending/20261108-hopebringer-banana. Archive hopebringer_banana_20261108.tar.xz is 1,573,252 bytes, SHA256 96e9468cb6914ee1d6e2af7616d24c313a25e8932fbf96446ffb23eb619fa5ac. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Amber baseline file is fully rehashed before copying. The independent restored_hopebringer_banana_runtime must have exactly 27,782 files / 1,548,319,878 bytes, SOURCE_MAP SHA256 801ee9d585dbf6b6bc51b57f89ec3dc769c644d23799867cd600db71f1791d28. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Banana increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
