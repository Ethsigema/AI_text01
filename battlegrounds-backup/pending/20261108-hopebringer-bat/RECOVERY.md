# Recover Hopebringer Bat source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Wolf with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/540922e329ef3fa5987146973cb4b449afd4ac9b/battlegrounds-backup/pending/20261108-hopebringer-wolf/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, and Wolf. Retain the Wolf recovery directory containing restored_hopebringer_wolf_runtime, hopebringer_wolf/extracted/hopebringer_wolf_20261108/SOURCE_MAP.json, and HOPEBRINGER_WOLF_REMOTE_CHAIN_VERIFICATION.json.

Required Wolf map SHA256: ebb7c3b356e7f04caecdd0839354579d1c98d6a38bed50be642c3a1e91d33282. Required Wolf receipt SHA256: 0b6b8a5ad77d69f61684fc06852707301c71cded25fd52d76e41fffe1f9f544e.

## Restore this increment

Place verify_and_restore_hopebringer_bat.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_bat.py --hopebringer-wolf-recovery /path/to/wolf_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 928b9a0ff682eff9239c3479b3da4ede26d4532b, folder battlegrounds-backup/pending/20261108-hopebringer-bat. Archive hopebringer_bat_20261108.tar.xz is 1,570,588 bytes, SHA256 8c68e495e707797731b720d8e16287cb8a06f0fb8a0e5602de6357008e7e34e0. It verifies all part hashes, archive hash, 37 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/three additions/zero removals.

Every Wolf baseline file is fully rehashed before copying. The independent restored_hopebringer_bat_runtime must have exactly 27,796 files / 1,548,361,228 bytes, SOURCE_MAP SHA256 55bfec869fd2b4c1868b7d61028118375ae2eac626f8624b2c8ebee640e2dd80. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Bat increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
