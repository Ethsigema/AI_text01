# Recover First Action Play Sequence source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Swirler Ultraviolet recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/1b4c54e7aaf27540a51395cd8bb8ac69839e4ec2/battlegrounds-backup/pending/20261107-timewarp-swirler-ultraviolet/RECOVERY.md

Follow each pinned prerequisite through Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Swirler Ultraviolet directory must contain restored_swirler_ultraviolet_runtime and swirler_ultraviolet/extracted/timewarp_swirler_ultraviolet_20261107/SOURCE_MAP.json. Require exactly 27,650 files / 1,547,857,399 bytes, map SHA256 b7832ebe2a8d4ef16b98eb3730eb46be615a12c01cc74e484055b01fafba9249. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- SWIRLER_ULTRAVIOLET_REMOTE_CHAIN_VERIFICATION.json: SHA256 eb1a8aa2282b4a1a31488f1c86ca70b8e560ce699838d6ef9050a938b2015e83.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Swirler Ultraviolet. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_first_action.py in a new directory and run:

```sh
python3 verify_and_restore_first_action.py --swirler-ultraviolet-recovery /path/to/completed-swirler-ultraviolet-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 25947fe797a1579474ed3bd8564ec352fe8b707f, path battlegrounds-backup/pending/20261107-first-action-play-sequence. Archive first_action_play_sequence_20261107.tar.xz: 1,048,044 bytes, SHA256 69f15683d30a8423abaef1accb9c1fb5d8a7d33efb788d3186456716fb7abdc5.

It verifies all part hashes, assembled archive and all 34 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: one modification, zero additions/removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_first_action_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require FIRST_ACTION_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,650 files / 1,547,857,574 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 d2e0de287713ef40084422492d6ea58ca0a6c7af03c52c0a5c3fcc05434debf8. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
