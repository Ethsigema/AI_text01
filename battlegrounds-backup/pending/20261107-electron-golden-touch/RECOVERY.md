# Recover Electron Golden Touch source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Scavenge Clock recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/b98e2c26abf8843f45b9e88af678465bfa8c011b/battlegrounds-backup/pending/20261107-electron-scavenge-clock/RECOVERY.md

Follow each pinned prerequisite through Electron Alliance Choice, Timewarp Golden Ultraviolet Bridge, Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Scavenge Clock directory must contain restored_scavenge_clock_runtime and scavenge_clock/extracted/electron_scavenge_clock_20261107/SOURCE_MAP.json. Require exactly 27,675 files / 1,547,979,952 bytes, map SHA256 6f163c0fc8a881d3c666b68599a5ce089e388f8168765aa07369a559e78a2520. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- SCAVENGE_CLOCK_REMOTE_CHAIN_VERIFICATION.json: SHA256 669b3a0f6465850ba1ddf2299de68940c8b33a5e08f3911cd1a5b1f5a6ff9288.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Scavenge Clock. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_golden_touch.py in a new directory and run:

```sh
python3 verify_and_restore_golden_touch.py --scavenge-clock-recovery /path/to/completed-scavenge-clock-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit e7042656795d785110e75b0ee1e70b0fc82afc88, path battlegrounds-backup/pending/20261107-electron-golden-touch. Archive electron_golden_touch_20261107.tar.xz: 1,068,540 bytes, SHA256 9dbbfc1a4e1d10efa6216e5bdbfb9683989b32d7427c3a58056c1c4bfd72b596.

It verifies all part hashes, assembled archive and all 37 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_golden_touch_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require GOLDEN_TOUCH_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,677 files / 1,547,984,539 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 8266106c62d99359a96445abb99687141b12673e3fd79299abb28a5cf1a7514a. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
