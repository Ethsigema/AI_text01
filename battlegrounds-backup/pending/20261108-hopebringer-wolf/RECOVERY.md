# Recover Hopebringer Wolf source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Caretaker with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/5fe5758c78e3b894c8454c2354ad2310da55da73/battlegrounds-backup/pending/20261108-hopebringer-caretaker/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, and Caretaker. Retain the Caretaker recovery directory containing restored_hopebringer_caretaker_runtime, hopebringer_caretaker/extracted/hopebringer_caretaker_20261108/SOURCE_MAP.json, and HOPEBRINGER_CARETAKER_REMOTE_CHAIN_VERIFICATION.json.

Required Caretaker map SHA256: 5d116ed6a31bcc512f6dbefeb2db194cc1bd56dfe321f8759bcb2afc85d0417d. Required Caretaker receipt SHA256: c868e517e7eef70d90d71f02e2dbdba6ba6580760771beb16648c3b5ce426b96.

## Restore this increment

Place verify_and_restore_hopebringer_wolf.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_wolf.py --hopebringer-caretaker-recovery /path/to/caretaker_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 031f6fe674181c15513f52368026cf2d617c3d97, folder battlegrounds-backup/pending/20261108-hopebringer-wolf. Archive hopebringer_wolf_20261108.tar.xz is 1,567,076 bytes, SHA256 16c5f41ce17164a46f2d6c0e077bb53380d45b4e7f843d61f029ce7f705dc15a. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Caretaker baseline file is fully rehashed before copying. The independent restored_hopebringer_wolf_runtime must have exactly 27,793 files / 1,548,353,139 bytes, SOURCE_MAP SHA256 ebb7c3b356e7f04caecdd0839354579d1c98d6a38bed50be642c3a1e91d33282. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Wolf increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
