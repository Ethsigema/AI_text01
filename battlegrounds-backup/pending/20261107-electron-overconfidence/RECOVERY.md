# Recover Electron Overconfidence source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Timed Choice recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/ffb2f1a61678824d2493b7fac34e675e29870e05/battlegrounds-backup/pending/20261107-electron-timed-choice/RECOVERY.md

Follow each pinned prerequisite through Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Timed Choice directory must contain restored_timed_choice_runtime and timed_choice/extracted/electron_timed_choice_20261107/SOURCE_MAP.json. Require exactly 27,664 files / 1,547,945,669 bytes, map SHA256 3d73c34d37058c194cd9b6362943da522908723a0d2761852bfa358bbed997d7. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- TIMED_CHOICE_REMOTE_CHAIN_VERIFICATION.json: SHA256 f92972dd6836589184b957c8b5f90113750c0e07228940ab78cb4d779e19eadd.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Timed Choice. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_overconfidence.py in a new directory and run:

```sh
python3 verify_and_restore_overconfidence.py --timed-choice-recovery /path/to/completed-timed-choice-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit edcf54ac1ed8b3628f1a04fd1e80e58a283e385c, path battlegrounds-backup/pending/20261107-electron-overconfidence. Archive electron_overconfidence_20261107.tar.xz: 1,069,880 bytes, SHA256 58b36a80a7c4957e774eafbad5d6ebc160e4f37e889a76a0451756346c398e9e.

It verifies all part hashes, assembled archive and all 38 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_overconfidence_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require OVERCONFIDENCE_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,666 files / 1,547,950,530 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 7a139b4f1834493fa7fb32ad3ffdeda86e6a6660ece3fa5cc2399146e3e6960c. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
