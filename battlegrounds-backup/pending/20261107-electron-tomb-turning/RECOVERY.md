# Recover Electron Tomb Turning source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Tier1 Discover recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/a9d1dd894bf497b17b7bb8a1d9bba4d3e7eb5b3d/battlegrounds-backup/pending/20261107-electron-tier1-discover/RECOVERY.md

Follow each pinned prerequisite through Electron Golden Touch, Electron Scavenge Clock, Electron Alliance Choice, Timewarp Golden Ultraviolet Bridge, Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Tier1 Discover directory must contain restored_tier1_discover_runtime and tier1_discover/extracted/electron_tier1_discover_20261107/SOURCE_MAP.json. Require exactly 27,679 files / 1,547,988,768 bytes, map SHA256 4e0096c08e463090b8b47a88a7b2554b81a931054f87752b66ab59eee792014a. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- TIER1_DISCOVER_REMOTE_CHAIN_VERIFICATION.json: SHA256 9265c9ce6223f9b81972cf76d2980e84d3b03af5e77cb10b523580d4e207bac3.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Tier1 Discover. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_tomb_turning.py in a new directory and run:

```sh
python3 verify_and_restore_tomb_turning.py --tier1-discover-recovery /path/to/completed-tier1-discover-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit a83bbd5337558ab690778a31e33925913d53ff8c, path battlegrounds-backup/pending/20261107-electron-tomb-turning. Archive electron_tomb_turning_20261107.tar.xz: 1,076,532 bytes, SHA256 109b9819c7fa2dfb8a45695c9bb688c3913178354b182cbf62f3a0cabd0f882c.

It verifies all part hashes, assembled archive and all 37 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_tomb_turning_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require TOMB_TURNING_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,681 files / 1,547,994,230 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 f2cd6744f457c94ca7b3d0338cfcab412b1cf8687edfce87fe76466ba90c68b9. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
