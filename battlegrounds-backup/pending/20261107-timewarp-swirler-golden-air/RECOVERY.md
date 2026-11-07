# Recover Timewarp Swirler Golden Air source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable First Action Play Sequence recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/f24d56e5dea28b557e1dc416b1fa34241051da91/battlegrounds-backup/pending/20261107-first-action-play-sequence/RECOVERY.md

Follow each pinned prerequisite through Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed First Action Play Sequence directory must contain restored_first_action_runtime and first_action/extracted/first_action_play_sequence_20261107/SOURCE_MAP.json. Require exactly 27,650 files / 1,547,857,574 bytes, map SHA256 d2e0de287713ef40084422492d6ea58ca0a6c7af03c52c0a5c3fcc05434debf8. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- FIRST_ACTION_REMOTE_CHAIN_VERIFICATION.json: SHA256 669ecd2e26ebc88e71962efc8aadde7b342208fe22074bfef8b91459106195e9.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to First Action Play Sequence. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_golden_air.py in a new directory and run:

```sh
python3 verify_and_restore_golden_air.py --first-action-recovery /path/to/completed-first-action-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit cf984730977bc3e5013af67638e50e370ae823f1, path battlegrounds-backup/pending/20261107-timewarp-swirler-golden-air. Archive timewarp_swirler_golden_air_20261107.tar.xz: 1,055,068 bytes, SHA256 69a42acaeac6fec9e9ed3a8d67f79df68dc549120ba98aee147931207f439c1a.

It verifies all part hashes, assembled archive and all 37 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: two modifications, zero additions/removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_golden_air_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require GOLDEN_AIR_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,650 files / 1,547,857,831 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 e1f5d4fa719ca683553c6f641205fd33ea38382693ca8fa60b8cf95e070ce958. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
