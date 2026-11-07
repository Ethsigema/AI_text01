# Recover Electron Sale Transfer source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Refresh Winds recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/dc77fba14e41dea285049ad866da5f55649811a7/battlegrounds-backup/pending/20261107-electron-refresh-winds/RECOVERY.md

Follow each pinned prerequisite through Electron Spell Refresh, Electron Enchanted Lasso, Electron Nearest Enemy, Electron Undead Army, Electron Corrupted Cupcakes, Electron Tomb Turning, Electron Tier1 Discover, Electron Golden Touch, Electron Scavenge Clock, Electron Alliance Choice, Timewarp Golden Ultraviolet Bridge, Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Refresh Winds directory must contain restored_refresh_winds_runtime and refresh_winds/extracted/electron_refresh_winds_20261107/SOURCE_MAP.json. Require exactly 27,693 files / 1,548,030,719 bytes, map SHA256 5604b3fbd4f22c6cb051a28b8bb540d7b8c5da92dadf53be5614f16a8b6a539e. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- REFRESH_WINDS_REMOTE_CHAIN_VERIFICATION.json: SHA256 fccbd8db0a1dd8f5fcaba488c56ff25c065ea3e78b6b4d1abddc0c7dce276ea7.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Refresh Winds. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_sale_transfer.py in a new directory and run:

```sh
python3 verify_and_restore_sale_transfer.py --refresh-winds-recovery /path/to/completed-refresh-winds-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit e23e6ae902a47156af8a758cb1344e6b70a4f2e8, path battlegrounds-backup/pending/20261107-electron-sale-transfer. Archive electron_sale_transfer_20261107.tar.xz: 1,074,232 bytes, SHA256 8aee2b12df3dfeef17b422069bacca9be81afcd644f00f1ada33010d9a8af553.

It verifies all part hashes, assembled archive and all 37 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_sale_transfer_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require SALE_TRANSFER_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,695 files / 1,548,036,752 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 6f3b6db8269a0e7522b395b534b7ff0fc4bee76533c90e3a24856064737e6f1a. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
