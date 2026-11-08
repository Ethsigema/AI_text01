# Recover Hopebringer Refreshing source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Roadboar with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/01d8faa2ff1f55335c9bd152d755d60c3ec8759d/battlegrounds-backup/pending/20261108-hopebringer-roadboar/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, and Roadboar. Retain the Roadboar recovery directory containing restored_hopebringer_roadboar_runtime, hopebringer_roadboar/extracted/hopebringer_roadboar_20261108/SOURCE_MAP.json, and HOPEBRINGER_ROADBOAR_REMOTE_CHAIN_VERIFICATION.json.

Required Roadboar map SHA256: b71cabdcc391dff896e08ca9207f6dd667ed7bee71dac789fea1967cf5b0e8df. Required Roadboar receipt SHA256: 671f7144c39593aed338df0487f0f7330e55b47318ff5cffa381ecdcc049bb0a.

## Restore this increment

Place verify_and_restore_hopebringer_refreshing.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_refreshing.py --hopebringer-roadboar-recovery /path/to/roadboar_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit c2b5abeeb5452e6e4ec39d815d694a72961d29b4, folder battlegrounds-backup/pending/20261108-hopebringer-refreshing. Archive hopebringer_refreshing_20261108.tar.xz is 1,562,608 bytes, SHA256 e43c7a145216147d01e4dba2492aa02e1c9b2aba950bcca5f017e472a85095d9. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Roadboar baseline file is fully rehashed before copying. The independent restored_hopebringer_refreshing_runtime must have exactly 27,808 files / 1,548,401,971 bytes, SOURCE_MAP SHA256 a5b40d1149d2dc4c762d8294fcef04e43927d8448ce7cb7e2b23cfb328309586. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Refreshing increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
