# Recover Electron Scavenge Clock source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Alliance Choice recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/b96c27f8061ee62de0a8418a880b98ef20793039/battlegrounds-backup/pending/20261107-electron-alliance-choice/RECOVERY.md

Follow each pinned prerequisite through Timewarp Golden Ultraviolet Bridge, Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Alliance Choice directory must contain restored_alliance_choice_runtime and alliance_choice/extracted/electron_alliance_choice_20261107/SOURCE_MAP.json. Require exactly 27,673 files / 1,547,974,412 bytes, map SHA256 07dd29436f95d0fba4d71cd33c71ae8cba079be3017cb5152ca34468e09a39c7. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- ALLIANCE_CHOICE_REMOTE_CHAIN_VERIFICATION.json: SHA256 9ba814811d4098f70617a932232283a98f2dc20c6c163aec43973c0fd55aaebe.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Alliance Choice. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_scavenge_clock.py in a new directory and run:

```sh
python3 verify_and_restore_scavenge_clock.py --alliance-choice-recovery /path/to/completed-alliance-choice-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 392973e9e7c4c37ecf3dc6d5a6ad297732e26ba4, path battlegrounds-backup/pending/20261107-electron-scavenge-clock. Archive electron_scavenge_clock_20261107.tar.xz: 1,074,648 bytes, SHA256 30fc4afb1c1c69829f739cee96cbea942f7f734dcec4275307568b102de52bf8.

It verifies all part hashes, assembled archive and all 37 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_scavenge_clock_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require SCAVENGE_CLOCK_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,675 files / 1,547,979,952 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 6f163c0fc8a881d3c666b68599a5ce089e388f8168765aa07369a559e78a2520. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
