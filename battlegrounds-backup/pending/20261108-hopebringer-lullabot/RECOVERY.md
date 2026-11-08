# Recover Hopebringer Lullabot source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Geomancer with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/ec2ed8220e11d89649c01b29b12ef0d2525568dc/battlegrounds-backup/pending/20261108-hopebringer-geomancer/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, Brann, and Geomancer. Retain the Geomancer recovery directory containing restored_hopebringer_geomancer_runtime, hopebringer_geomancer/extracted/hopebringer_geomancer_20261108/SOURCE_MAP.json, and HOPEBRINGER_GEOMANCER_REMOTE_CHAIN_VERIFICATION.json.

Required Geomancer map SHA256: f05abac1c5b185aab5ea1b68643f9a2e7447008203f3dd515e459b4d8498cbcf. Required Geomancer receipt SHA256: 354514ec8b9b84a4ece33c1d64c4bb911df1b15d31a9ba2f88e76bdd6aced54d.

## Restore this increment

Place verify_and_restore_hopebringer_lullabot.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_lullabot.py --hopebringer-geomancer-recovery /path/to/geomancer_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 45d8a587913024e1b6e697ddccaa70083ba51e3f, folder battlegrounds-backup/pending/20261108-hopebringer-lullabot. Archive hopebringer_lullabot_20261108.tar.xz is 1,573,176 bytes, SHA256 e247a55168f1bdcea2a4d1593a38ea143cef7dc6fe07f034389cc086c6a0d4af. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Geomancer baseline file is fully rehashed before copying. The independent restored_hopebringer_lullabot_runtime must have exactly 27,814 files / 1,548,421,793 bytes, SOURCE_MAP SHA256 0416cdda6d96751509c39dc3dcfe60983fede6130615ba68df1eefa1dea4eb9e. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Lullabot increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
