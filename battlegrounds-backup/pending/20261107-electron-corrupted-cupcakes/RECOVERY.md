# Recover Electron Corrupted Cupcakes source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Tomb Turning recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/a85ed00007f36a1e1f714604b05f254d245adfb8/battlegrounds-backup/pending/20261107-electron-tomb-turning/RECOVERY.md

Follow each pinned prerequisite through Electron Tier1 Discover, Electron Golden Touch, Electron Scavenge Clock, Electron Alliance Choice, Timewarp Golden Ultraviolet Bridge, Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Tomb Turning directory must contain restored_tomb_turning_runtime and tomb_turning/extracted/electron_tomb_turning_20261107/SOURCE_MAP.json. Require exactly 27,681 files / 1,547,994,230 bytes, map SHA256 f2cd6744f457c94ca7b3d0338cfcab412b1cf8687edfce87fe76466ba90c68b9. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- TOMB_TURNING_REMOTE_CHAIN_VERIFICATION.json: SHA256 ddbc7a0c2f9f27fe7251e2c48478cc3a78d9d4e6b0b1926c5e0e4bac77101487.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Tomb Turning. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_corrupted_cupcakes.py in a new directory and run:

```sh
python3 verify_and_restore_corrupted_cupcakes.py --tomb-turning-recovery /path/to/completed-tomb-turning-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 4410b4e065a9308eab4784fd36c343ea38191f05, path battlegrounds-backup/pending/20261107-electron-corrupted-cupcakes. Archive electron_corrupted_cupcakes_20261107.tar.xz: 1,076,440 bytes, SHA256 7f7187e7b3107e26825788355e7fd4946cc54c8de37543b0f59216ab4761f9a1.

It verifies all part hashes, assembled archive and all 48 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_corrupted_cupcakes_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require CORRUPTED_CUPCAKES_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,683 files / 1,548,001,078 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 22fa70dd74fadfe687dfdfabab2ad62abcaf961955ff31197fa271f997cb38dc. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
