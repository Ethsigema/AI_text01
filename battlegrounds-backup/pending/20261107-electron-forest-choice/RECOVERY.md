# Recover Electron Forest Choice source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Timewarp Golden Molten Swirler recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/53bfcd64be35948812aa0e6481f933a4934e4b06/battlegrounds-backup/pending/20261107-timewarp-golden-molten-swirler/RECOVERY.md

Follow each pinned prerequisite through Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Timewarp Golden Molten Swirler directory must contain restored_golden_molten_runtime and golden_molten/extracted/timewarp_golden_molten_swirler_20261107/SOURCE_MAP.json. Require exactly 27,656 files / 1,547,918,193 bytes, map SHA256 3d562a0ccde4e3d74ec9794139497ac99378b5550971c73fac996cc7d2cfafd3. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- GOLDEN_MOLTEN_REMOTE_CHAIN_VERIFICATION.json: SHA256 4012b2b8dab7a7dbf6e3d768b73340e20a033d542ebf5942473eced19f1fa97e.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Timewarp Golden Molten Swirler. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_forest_choice.py in a new directory and run:

```sh
python3 verify_and_restore_forest_choice.py --golden-molten-recovery /path/to/completed-golden-molten-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 374052ea51b5be0ac464a0cdbbb004d7096b761e, path battlegrounds-backup/pending/20261107-electron-forest-choice. Archive electron_forest_choice_20261107.tar.xz: 1,067,452 bytes, SHA256 bd4fc1b7c89233d278852b1fd3836a9652d02c5a265bd53534ec695495b28930.

It verifies all part hashes, assembled archive and all 40 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, four additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_forest_choice_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require FOREST_CHOICE_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,660 files / 1,547,931,654 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 7125eba781ac69fcd0f7d6b43f88a88ad151a63f075cbd1cd52092278816ac5d. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
