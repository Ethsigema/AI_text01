# Recover Electron Undead Army source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Corrupted Cupcakes recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/039832c10fe8e8296f92577a36c484df3c1d1d44/battlegrounds-backup/pending/20261107-electron-corrupted-cupcakes/RECOVERY.md

Follow each pinned prerequisite through Electron Tomb Turning, Electron Tier1 Discover, Electron Golden Touch, Electron Scavenge Clock, Electron Alliance Choice, Timewarp Golden Ultraviolet Bridge, Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Corrupted Cupcakes directory must contain restored_corrupted_cupcakes_runtime and corrupted_cupcakes/extracted/electron_corrupted_cupcakes_20261107/SOURCE_MAP.json. Require exactly 27,683 files / 1,548,001,078 bytes, map SHA256 22fa70dd74fadfe687dfdfabab2ad62abcaf961955ff31197fa271f997cb38dc. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- CORRUPTED_CUPCAKES_REMOTE_CHAIN_VERIFICATION.json: SHA256 f33a9ef019f9a0abb6fb73295521cfab064e123a2849caad313eda3e06dc9dac.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Corrupted Cupcakes. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_undead_army.py in a new directory and run:

```sh
python3 verify_and_restore_undead_army.py --corrupted-cupcakes-recovery /path/to/completed-corrupted-cupcakes-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 4666a3f225c0e5c489a731c6a2e407782ef720ad, path battlegrounds-backup/pending/20261107-electron-undead-army. Archive electron_undead_army_20261107.tar.xz: 1,073,824 bytes, SHA256 7258cb92a91181b6285540e6b956f24ff4c0559e4cf0fa5c9c4a30378de92910.

It verifies all part hashes, assembled archive and all 37 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_undead_army_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require UNDEAD_ARMY_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,685 files / 1,548,009,285 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 237533b3bed6e4eeea709c9e1670720dbe6e53f8ebcd24ad1eb103c364f45933. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
