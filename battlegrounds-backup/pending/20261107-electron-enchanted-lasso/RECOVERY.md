# Recover Electron Enchanted Lasso source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Nearest Enemy recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/44cd6b27c2a268471ed22c329f3bb4ab47734499/battlegrounds-backup/pending/20261107-electron-nearest-enemy/RECOVERY.md

Follow each pinned prerequisite through Electron Undead Army, Electron Corrupted Cupcakes, Electron Tomb Turning, Electron Tier1 Discover, Electron Golden Touch, Electron Scavenge Clock, Electron Alliance Choice, Timewarp Golden Ultraviolet Bridge, Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Nearest Enemy directory must contain restored_nearest_enemy_runtime and nearest_enemy/extracted/electron_nearest_enemy_20261107/SOURCE_MAP.json. Require exactly 27,687 files / 1,548,015,414 bytes, map SHA256 c6d66a3d40b242f9238e80cc2d28a96615fd3ebf7f4a0363e31ed3ba8445803c. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- NEAREST_ENEMY_REMOTE_CHAIN_VERIFICATION.json: SHA256 221ef8f62d7fe3f7a6d88286387a393551a88053b1ff26ebad15a7afe4296973.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Nearest Enemy. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_enchanted_lasso.py in a new directory and run:

```sh
python3 verify_and_restore_enchanted_lasso.py --nearest-enemy-recovery /path/to/completed-nearest-enemy-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 490988e6f23f0f218b3b5f29168b9b703d3eaba9, path battlegrounds-backup/pending/20261107-electron-enchanted-lasso. Archive electron_enchanted_lasso_20261107.tar.xz: 1,069,460 bytes, SHA256 27649a63c63fdfc0acee933a4cf4d3dea99dcf13a13df5e2916298e4da04d7f1.

It verifies all part hashes, assembled archive and all 37 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_enchanted_lasso_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require ENCHANTED_LASSO_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,689 files / 1,548,019,677 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 4cfd94bc3b414b3d55d0b827028bbfbe1e53c777321cac6c204b5c1d63ea0fec. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
