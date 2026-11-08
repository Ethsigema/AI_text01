# Recover Hopebringer Recruiter source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Humming with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/fbbb88d9b902e8d607aeede29cf9833f0674a91b/battlegrounds-backup/pending/20261108-hopebringer-humming/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, and Humming. Retain the Humming recovery directory containing restored_hopebringer_humming_runtime, hopebringer_humming/extracted/hopebringer_humming_20261108/SOURCE_MAP.json, and HOPEBRINGER_HUMMING_REMOTE_CHAIN_VERIFICATION.json.

Required Humming map SHA256: 75ab1ea4ff1dcd8e57495841c0f1e17c7ace505645eea9d0b8abd4b9f8becdc6. Required Humming receipt SHA256: 701fb3a036ce623fa1d11e36847e6d0d30d4b48caa985564c13472e4a252ab59.

## Restore this increment

Place verify_and_restore_hopebringer_recruiter.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_recruiter.py --hopebringer-humming-recovery /path/to/humming_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 6fb0bf7fe49d23031a56347f52c051a8883e0006, folder battlegrounds-backup/pending/20261108-hopebringer-recruiter. Archive hopebringer_recruiter_20261108.tar.xz is 1,566,940 bytes, SHA256 2a83566e0db3621ada041eee32dfdf98c68d513fab928ab60cba21e92108ad8c. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Humming baseline file is fully rehashed before copying. The independent restored_hopebringer_recruiter_runtime must have exactly 27,786 files / 1,548,332,746 bytes, SOURCE_MAP SHA256 708c6bc362cee806ec1932409db9da7f08ccf1430f9b0562a201d653e2027205. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Recruiter increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
