# Recover Hopebringer Glim source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Bat with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/4fbdf47d48edb978e29785565619309e78de8c2a/battlegrounds-backup/pending/20261108-hopebringer-bat/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, and Bat. Retain the Bat recovery directory containing restored_hopebringer_bat_runtime, hopebringer_bat/extracted/hopebringer_bat_20261108/SOURCE_MAP.json, and HOPEBRINGER_BAT_REMOTE_CHAIN_VERIFICATION.json.

Required Bat map SHA256: 55bfec869fd2b4c1868b7d61028118375ae2eac626f8624b2c8ebee640e2dd80. Required Bat receipt SHA256: a742fc36f702934b4e7911048c30d263556c17a16529e7680fcfe599725bbbe3.

## Restore this increment

Place verify_and_restore_hopebringer_glim.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_glim.py --hopebringer-bat-recovery /path/to/bat_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 171a5d0ed41f3b1d2b897bd4107eca5804c496ce, folder battlegrounds-backup/pending/20261108-hopebringer-glim. Archive hopebringer_glim_20261108.tar.xz is 1,566,272 bytes, SHA256 23d9b34f6db77f0bbf928ed7cd53f9b7cc80cd64586d4c889969de253103dcb7. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Bat baseline file is fully rehashed before copying. The independent restored_hopebringer_glim_runtime must have exactly 27,798 files / 1,548,366,890 bytes, SOURCE_MAP SHA256 6317c4fa555653bb258ce726b19dbfd2881980bc082e5f406bee60921357af90. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Glim increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
