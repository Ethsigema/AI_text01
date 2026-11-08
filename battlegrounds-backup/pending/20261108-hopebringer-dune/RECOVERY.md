# Recover Hopebringer Dune source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Sylvar with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/a6388174be2b42fa913592329c28d7a31dc94d57/battlegrounds-backup/pending/20261108-hopebringer-sylvar/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, Brann, Geomancer, Lullabot, Sellemental, and Sylvar. Retain the Sylvar recovery directory containing restored_hopebringer_sylvar_runtime, hopebringer_sylvar/extracted/hopebringer_sylvar_20261108/SOURCE_MAP.json, and HOPEBRINGER_SYLVAR_REMOTE_CHAIN_VERIFICATION.json.

Required Sylvar map SHA256: 4342a26be4032b422da1599de730f3b4634ef902954cc3eea82556fbfa8df88a. Required Sylvar receipt SHA256: b788427486862b5cd20d255ffbce48e029e61017c7fcec4fd9b8f38701a02889.

## Restore this increment

Place verify_and_restore_hopebringer_dune.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_dune.py --hopebringer-sylvar-recovery /path/to/sylvar_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 7e1804464d9f703161883e9371358f0e4525881f, folder battlegrounds-backup/pending/20261108-hopebringer-dune. Archive hopebringer_dune_20261108.tar.xz is 1,571,908 bytes, SHA256 e09b9a16e325b39fffdc3359543d527ff364737f247191407915b984c57ba073. It verifies all part hashes, archive hash, 58 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Sylvar baseline file is fully rehashed before copying. The independent restored_hopebringer_dune_runtime must have exactly 27,821 files / 1,548,444,623 bytes, SOURCE_MAP SHA256 afcfedcc2db16afaa31e2007e32c39dd63d6efef20fdcdfd975d7c5a97c67ad7. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Dune increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
