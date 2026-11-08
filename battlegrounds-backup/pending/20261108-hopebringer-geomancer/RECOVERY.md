# Recover Hopebringer Geomancer source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Brann with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/cb2391a6f872b895a39975b3e77b21e9c6a3166a/battlegrounds-backup/pending/20261108-hopebringer-brann/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, and Brann. Retain the Brann recovery directory containing restored_hopebringer_brann_runtime, hopebringer_brann/extracted/hopebringer_brann_20261108/SOURCE_MAP.json, and HOPEBRINGER_BRANN_REMOTE_CHAIN_VERIFICATION.json.

Required Brann map SHA256: b8eb523573635a49b49f81f0d8b2cecb33f221b77896d5aa53fca04909a066f2. Required Brann receipt SHA256: 4591cbfe560fafb6e6b00ca9ef2bd1aec341ebcb23a8e9379c9775431a573d2c.

## Restore this increment

Place verify_and_restore_hopebringer_geomancer.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_geomancer.py --hopebringer-brann-recovery /path/to/brann_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 227347493d6a30bff7a7f284b8dc9cac8540b5a0, folder battlegrounds-backup/pending/20261108-hopebringer-geomancer. Archive hopebringer_geomancer_20261108.tar.xz is 1,597,916 bytes, SHA256 a4654dcee8225c0c35126279c1855d4146a4dc793a388f1fbc7b3f0d6431914d. It verifies all part hashes, archive hash, 48 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Brann baseline file is fully rehashed before copying. The independent restored_hopebringer_geomancer_runtime must have exactly 27,812 files / 1,548,415,354 bytes, SOURCE_MAP SHA256 f05abac1c5b185aab5ea1b68643f9a2e7447008203f3dd515e459b4d8498cbcf. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Geomancer increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
