# Recover Electron Timed Choice source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Forest Choice recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/461afb8fe63ec0d8f90061e270c196f2519b1517/battlegrounds-backup/pending/20261107-electron-forest-choice/RECOVERY.md

Follow each pinned prerequisite through Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Forest Choice directory must contain restored_forest_choice_runtime and forest_choice/extracted/electron_forest_choice_20261107/SOURCE_MAP.json. Require exactly 27,660 files / 1,547,931,654 bytes, map SHA256 7125eba781ac69fcd0f7d6b43f88a88ad151a63f075cbd1cd52092278816ac5d. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- FOREST_CHOICE_REMOTE_CHAIN_VERIFICATION.json: SHA256 7c191a0bc933c7b4c735e0d8662d947e55a57596113e25ee48212ecc7c51c7ed.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Forest Choice. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_timed_choice.py in a new directory and run:

```sh
python3 verify_and_restore_timed_choice.py --forest-choice-recovery /path/to/completed-forest-choice-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 9b286088ce25f3e3348a8426e1a341eed52795df, path battlegrounds-backup/pending/20261107-electron-timed-choice. Archive electron_timed_choice_20261107.tar.xz: 1,106,720 bytes, SHA256 9d968a78546da3a09125d931e3adc1e1e6a28e0c0f5891e8cb56c92269d97945.

It verifies all part hashes, assembled archive and all 78 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: six modifications, four additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_timed_choice_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require TIMED_CHOICE_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,664 files / 1,547,945,669 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 3d73c34d37058c194cd9b6362943da522908723a0d2761852bfa358bbed997d7. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
