# Recover Hopebringer Brann source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Refreshing with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/377b24c9ab5693843b7da3cac398a25649fa2489/battlegrounds-backup/pending/20261108-hopebringer-refreshing/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, and Refreshing. Retain the Refreshing recovery directory containing restored_hopebringer_refreshing_runtime, hopebringer_refreshing/extracted/hopebringer_refreshing_20261108/SOURCE_MAP.json, and HOPEBRINGER_REFRESHING_REMOTE_CHAIN_VERIFICATION.json.

Required Refreshing map SHA256: a5b40d1149d2dc4c762d8294fcef04e43927d8448ce7cb7e2b23cfb328309586. Required Refreshing receipt SHA256: cb3162657b4697b7eb12b36c7ac4e27c0d5cf42c02f78904c27abc51afc4c4b9.

## Restore this increment

Place verify_and_restore_hopebringer_brann.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_brann.py --hopebringer-refreshing-recovery /path/to/refreshing_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 44e519c9afc6d7fc5f288b3eb000208b383101bf, folder battlegrounds-backup/pending/20261108-hopebringer-brann. Archive hopebringer_brann_20261108.tar.xz is 1,580,400 bytes, SHA256 cac4862fc9271d2d0afebd8cb1e9e11595ffd54f956d51cb064554b59308b5d4. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Refreshing baseline file is fully rehashed before copying. The independent restored_hopebringer_brann_runtime must have exactly 27,810 files / 1,548,409,283 bytes, SOURCE_MAP SHA256 b8eb523573635a49b49f81f0d8b2cecb33f221b77896d5aa53fca04909a066f2. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Brann increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
