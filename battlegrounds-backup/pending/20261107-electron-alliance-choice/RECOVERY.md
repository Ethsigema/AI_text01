# Recover Electron Alliance Choice source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Timewarp Golden Ultraviolet Bridge recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/7c650db07c27e961d655fd2b146692390afb58eb/battlegrounds-backup/pending/20261107-timewarp-golden-ultraviolet-bridge/RECOVERY.md

Follow each pinned prerequisite through Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Timewarp Golden Ultraviolet Bridge directory must contain restored_golden_ultraviolet_runtime and golden_ultraviolet/extracted/timewarp_golden_ultraviolet_bridge_20261107/SOURCE_MAP.json. Require exactly 27,669 files / 1,547,960,474 bytes, map SHA256 ad387f3dd43e4f2239efa641f9eb4168de901331342741a36ffe85cf924aef6d. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- GOLDEN_ULTRAVIOLET_REMOTE_CHAIN_VERIFICATION.json: SHA256 89d48d8b396783a6e75b86b826f70e62ff0b019ad4f1bb8fa201dadb75a97985.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Timewarp Golden Ultraviolet Bridge. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_alliance_choice.py in a new directory and run:

```sh
python3 verify_and_restore_alliance_choice.py --golden-ultraviolet-recovery /path/to/completed-golden-ultraviolet-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 8be0744a863586ebd290c7aba6a8002d5571eaa1, path battlegrounds-backup/pending/20261107-electron-alliance-choice. Archive electron_alliance_choice_20261107.tar.xz: 1,069,516 bytes, SHA256 6a960e606db53e60e3328a1287f80e7a762b46113c7deef7217d58cbf9b6fc20.

It verifies all part hashes, assembled archive and all 40 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, four additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_alliance_choice_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require ALLIANCE_CHOICE_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,673 files / 1,547,974,412 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 07dd29436f95d0fba4d71cd33c71ae8cba079be3017cb5152ca34468e09a39c7. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
