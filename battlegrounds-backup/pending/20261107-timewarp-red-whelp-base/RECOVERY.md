# Recover Timewarp Red Whelp base source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve every backup and hardlink. The exact verified Spark Snapper baseline is required.

## Restore the prerequisite chain

Follow the immutable Spark recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/011dbc1e2cbf195c73fa38b67a37f981cc982b65/battlegrounds-backup/pending/20261107-spark-snapper-base/RECOVERY.md

Follow its pinned prerequisites through Molten, Murky, Painter, Air, Temperature Shift and every earlier increment to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not just the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and sufficient space.

The completed Spark directory must contain `restored_spark_runtime` and `spark/extracted/spark_snapper_base_20261107/SOURCE_MAP.json`. Require 27,631 files / 1,547,612,084 bytes and SOURCE_MAP SHA256 `95de72bfa20d119788db4e0c54c344236f5cb01e8772b3ae1ec87402d4a913ed`. Leave this baseline unmodified; do not launch Godot in it before verification.

Place the published supporting receipts in that Spark directory:

- SPARK_REMOTE_CHAIN_VERIFICATION.json, SHA256 `a7032a1bf6d78ac38c6a55e2b61d6cd25b763f7d8533ec4ad3d889dae0d8cbca`.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 `edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2`.

The whole-chain receipt records the earlier separate fresh check through Murky. Spark's pinned receipt verifies Murky→Molten→Spark continuity. This helper pins both receipt hashes, checks the Spark endpoint and prior continuity, then verifies every reused Spark source byte. Supporting receipts are not substitutes for source bytes or claims of fresh historical downloads this round.

## Download and restore Red Whelp

Place `verify_and_restore_red_whelp.py` in another new empty directory:

```sh
python3 verify_and_restore_red_whelp.py --spark-recovery /path/to/completed-spark-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 12 binary parts, REMOVALS.json and CHANGES.json from immutable commit `f1ef21a7077831c2e4b3677f159dbfaf620fe6af`, directory `battlegrounds-backup/pending/20261107-timewarp-red-whelp-base`. Archive: 2,849,696 bytes, SHA256 `f3b2f83ad43662251448a38012fa80748eb6e6e8e922bf518cd12e186d35bfe8`.

Every part, assembled archive and all 137 members are verified; unsafe paths/types are rejected. Companion hashes/sizes must match MANIFEST.json companion_files, and their arrays must equal actual differences: 5 additions, 76 modifications, no removals. REMOVALS.json must match manifest removed_source_files. Spark SOURCE_MAP must byte-equal Red Whelp BASE_MAP; every baseline file is rehashed.

An independent `restored_red_whelp_runtime` is copied without hardlinks; baseline files are never written. Every output and the unchanged baseline are rehashed, with per-file RESTORE_PROVENANCE.json. Require RED_WHELP_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,636 files / 1,547,673,927 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `0f04c4337ca47eb5e04b68c16c676d24535739527deac10e929126afaa896794`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only Red Whelp is freshly downloaded this round; Spark and historical-chain evidence are reused, with every baseline byte rehashed. The historical chain is not redownloaded. No gameplay is executed or accepted.
