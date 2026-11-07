# Recover Electron Recruitment source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Robust Evolution recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/6399412208a7f69d6d60fd00505ca8092b5aafb7/battlegrounds-backup/pending/20261107-electron-robust-evolution/RECOVERY.md

Follow each pinned prerequisite through Electron Sale Transfer, Electron Refresh Winds, Electron Spell Refresh, Electron Enchanted Lasso, Electron Nearest Enemy, Electron Undead Army, Electron Corrupted Cupcakes, Electron Tomb Turning, Electron Tier1 Discover, Electron Golden Touch, Electron Scavenge Clock, Electron Alliance Choice, Timewarp Golden Ultraviolet Bridge, Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Robust Evolution directory must contain restored_robust_evolution_runtime and robust_evolution/extracted/electron_robust_evolution_20261107/SOURCE_MAP.json. Require exactly 27,697 files / 1,548,042,693 bytes, map SHA256 7c6e3c37c5e2efe75c210b667a9e197f97bb8ae6cff6a9d17b5c9e7d66231297. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- ROBUST_EVOLUTION_REMOTE_CHAIN_VERIFICATION.json: SHA256 a43233e69cdde5cfdee9be520509a04258077826abeb82ff9ab461a5c7931994.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Robust Evolution. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_recruitment.py in a new directory and run:

```sh
python3 verify_and_restore_recruitment.py --robust-evolution-recovery /path/to/completed-robust-evolution-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 4f7cb71e9374d9593897887572ca6a72038e5ae2, path battlegrounds-backup/pending/20261107-electron-recruitment. Archive electron_recruitment_20261107.tar.xz: 1,071,908 bytes, SHA256 9d74cf1f510c487462ee6658300e3cf10225082c7225af4f45a6bd808f6d4041.

It verifies all part hashes, assembled archive and all 37 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_recruitment_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require RECRUITMENT_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,699 files / 1,548,047,159 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 91aa9cd267720819bbd5f1a82e5b95921b4fc34fac5b5cec8affd7b29d523982. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
