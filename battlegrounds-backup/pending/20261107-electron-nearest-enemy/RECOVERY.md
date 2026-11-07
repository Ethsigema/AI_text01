# Recover Electron Nearest Enemy source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Undead Army recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/f2afd6a9950608571a4db22eb8ee58ac4046e20f/battlegrounds-backup/pending/20261107-electron-undead-army/RECOVERY.md

Follow each pinned prerequisite through Electron Corrupted Cupcakes, Electron Tomb Turning, Electron Tier1 Discover, Electron Golden Touch, Electron Scavenge Clock, Electron Alliance Choice, Timewarp Golden Ultraviolet Bridge, Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Undead Army directory must contain restored_undead_army_runtime and undead_army/extracted/electron_undead_army_20261107/SOURCE_MAP.json. Require exactly 27,685 files / 1,548,009,285 bytes, map SHA256 237533b3bed6e4eeea709c9e1670720dbe6e53f8ebcd24ad1eb103c364f45933. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- UNDEAD_ARMY_REMOTE_CHAIN_VERIFICATION.json: SHA256 94ff34428914efa9810692559ce46c3057b62a15021ac92ea7d3d689eade68cb.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Undead Army. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_nearest_enemy.py in a new directory and run:

```sh
python3 verify_and_restore_nearest_enemy.py --undead-army-recovery /path/to/completed-undead-army-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 201b2ecd5eb4e50db48a3995b5e48b58d798a1be, path battlegrounds-backup/pending/20261107-electron-nearest-enemy. Archive electron_nearest_enemy_20261107.tar.xz: 1,078,336 bytes, SHA256 9e800a250fc9a6936082eed99bb11d22f1d1c09a29c5efe56ebd76e05f6f51f8.

It verifies all part hashes, assembled archive and all 37 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_nearest_enemy_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require NEAREST_ENEMY_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,687 files / 1,548,015,414 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 c6d66a3d40b242f9238e80cc2d28a96615fd3ebf7f4a0363e31ed3ba8445803c. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
