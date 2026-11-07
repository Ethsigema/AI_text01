# Recover Timewarp Scout base source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve every backup and hardlink. The exact verified Timewarp Red Whelp baseline is required.

## Restore the prerequisite chain

Follow the immutable Red Whelp recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/84c3928704177ba384876fee613c6afe351f27bf/battlegrounds-backup/pending/20261107-timewarp-red-whelp-base/RECOVERY.md

Follow its pinned prerequisites through Spark, Molten, Murky, Painter, Air, Temperature Shift and every earlier increment to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not just the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and sufficient space.

The completed Red Whelp directory must contain `restored_red_whelp_runtime` and `red_whelp/extracted/timewarp_red_whelp_base_20261107/SOURCE_MAP.json`. Require 27,636 files / 1,547,673,927 bytes and SOURCE_MAP SHA256 `0f04c4337ca47eb5e04b68c16c676d24535739527deac10e929126afaa896794`. Leave this baseline unmodified; do not launch Godot in it before verification.

Place the published supporting receipts in that Red Whelp directory:

- RED_WHELP_REMOTE_CHAIN_VERIFICATION.json, SHA256 `2969a86744a5955fb9a496dc637907909d42c42bfb3e6f8aa2a41bceda3d2aec`.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 `edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2`.

The whole-chain receipt records the earlier separate fresh check through Murky. Red Whelp's pinned receipt verifies Murky→Molten→Spark→Red Whelp continuity. This helper pins both receipt hashes, checks the Red Whelp endpoint and prior continuity, then verifies every reused Red Whelp source byte. Supporting receipts are not substitutes for source bytes or claims of fresh historical downloads this round.

## Download and restore Scout

Place `verify_and_restore_scout.py` in another new empty directory:

```sh
python3 verify_and_restore_scout.py --red_whelp-recovery /path/to/completed-red_whelp-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 12 binary parts, REMOVALS.json and CHANGES.json from immutable commit `db4ab0ad4d47a5a6050ca6fc8dc3bd4bcefdfd76`, directory `battlegrounds-backup/pending/20261107-timewarp-scout-base`. Archive: 2,839,976 bytes, SHA256 `256b1dd78c050e2a566da8fc5e9cde69afab9959b59fc9048048409954003c7d`.

Every part, assembled archive and all 114 members are verified; unsafe paths/types are rejected. Companion hashes/sizes must match MANIFEST.json companion_files, and their arrays must equal actual differences: 5 additions, 76 modifications, no removals. REMOVALS.json must match manifest removed_source_files. Red Whelp SOURCE_MAP must byte-equal Scout BASE_MAP; every baseline file is rehashed.

An independent `restored_scout_runtime` is copied without hardlinks; baseline files are never written. Every output and the unchanged baseline are rehashed, with per-file RESTORE_PROVENANCE.json. Require SCOUT_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,641 files / 1,547,735,641 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `2f3de1eaccbd95c22a88d7b624aa3b9fe693e5c074f10759cfb7496e575282c0`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only Scout is freshly downloaded this round; Red Whelp and historical-chain evidence are reused, with every baseline byte rehashed. The historical chain is not redownloaded. No gameplay is executed or accepted.
