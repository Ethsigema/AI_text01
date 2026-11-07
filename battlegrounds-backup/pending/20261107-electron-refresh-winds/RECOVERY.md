# Recover Electron Refresh Winds source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Spell Refresh recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/5e10d603f318e5e474f02e6483cfe7041fb76804/battlegrounds-backup/pending/20261107-electron-spell-refresh/RECOVERY.md

Follow each pinned prerequisite through Electron Enchanted Lasso, Electron Nearest Enemy, Electron Undead Army, Electron Corrupted Cupcakes, Electron Tomb Turning, Electron Tier1 Discover, Electron Golden Touch, Electron Scavenge Clock, Electron Alliance Choice, Timewarp Golden Ultraviolet Bridge, Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Spell Refresh directory must contain restored_spell_refresh_runtime and spell_refresh/extracted/electron_spell_refresh_20261107/SOURCE_MAP.json. Require exactly 27,691 files / 1,548,024,597 bytes, map SHA256 cdf2bf2193b604df9f9214fd1ca16c9a1cc0a0edc1d4ed334d6d0687fd6ecc08. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- SPELL_REFRESH_REMOTE_CHAIN_VERIFICATION.json: SHA256 2a81d6a39baeab9f0dfaabed85aad4c8626241f059d578cce4880c4af14104e9.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Spell Refresh. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_refresh_winds.py in a new directory and run:

```sh
python3 verify_and_restore_refresh_winds.py --spell-refresh-recovery /path/to/completed-spell-refresh-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 20d0053ba34819629af0cefc39c98536ef3387c3, path battlegrounds-backup/pending/20261107-electron-refresh-winds. Archive electron_refresh_winds_20261107.tar.xz: 1,074,420 bytes, SHA256 c41002a958c13639d4b2a1a6bfddeccc43218c9e74a73f8659cd460a3b51465d.

It verifies all part hashes, assembled archive and all 37 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_refresh_winds_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require REFRESH_WINDS_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,693 files / 1,548,030,719 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 5604b3fbd4f22c6cb051a28b8bb540d7b8c5da92dadf53be5614f16a8b6a539e. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
