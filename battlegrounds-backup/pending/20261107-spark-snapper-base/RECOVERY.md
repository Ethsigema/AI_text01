# Recover Spark Snapper base source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve every backup and hardlink. The exact verified Molten baseline is required.

## Restore the prerequisite chain

Follow the immutable Molten recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/7ce90c87e7d41bb2f84f7430971fc6f86e15fd20/battlegrounds-backup/pending/20261107-timewarp-molten-base/RECOVERY.md

Follow its pinned prerequisite recipes through Murky, Painter, Air, Temperature Shift and all earlier increments to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not just the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and sufficient disk space.

The completed Molten directory must contain `restored_molten_runtime` and `molten/extracted/timewarp_molten_base_20261107/SOURCE_MAP.json`. Require 27,622 files / 1,547,513,946 bytes and SOURCE_MAP SHA256 `d1d1689c77b5ddf700b1d5f75ff259ca3a39ea55be0b7ccf2f1786b91c419e51`. Leave this baseline unmodified; do not launch Godot in it before verification.

Place the published supporting receipts in that Molten directory:

- MOLTEN_REMOTE_CHAIN_VERIFICATION.json, SHA256 `15c0c30e9cefe9c29f1c58def006d2ebf54ee9a590d33eeb5128f3c5989454f0`.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 `edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2`.

The whole-chain receipt records the earlier separate fresh check through Murky: original ZIP/new pinned Git snapshots, 70 historical part manifests/103 archives and 27 fresh increments. The Molten receipt connects that exact Murky endpoint to Molten. The helper pins both receipt hashes, verifies these map links, then checks the reused Molten bytes directly. Receipts are supporting evidence, not source-byte substitutes or claims of fresh historical downloads this round.

## Download and restore Spark

Place `verify_and_restore_spark.py` in another new empty directory:

```sh
python3 verify_and_restore_spark.py --molten-recovery /path/to/completed-molten-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 13 binary parts, REMOVALS.json and CHANGES.json from immutable commit `aeadeb25a594dd9ae3fb7236cc13ea57c4cb4958`, directory `battlegrounds-backup/pending/20261107-spark-snapper-base`. Archive: 3,249,228 bytes, SHA256 `1228308f44eaf78c887f9a42046f2820d2b7d311b2fad606dc071f5b8b6a7d7f`.

Every part, assembled archive and all 136 members are verified; unsafe paths/types are rejected. Companion sizes/hashes must match MANIFEST.json companion_files, and their arrays must equal actual differences: 9 additions, 73 modifications, no removals. REMOVALS.json must match manifest removed_source_files. Molten SOURCE_MAP must byte-equal Spark BASE_MAP; every baseline file is rehashed.

An independent `restored_spark_runtime` is copied without hardlinks; the baseline is never written. Every output and the unchanged baseline are rehashed, with per-file RESTORE_PROVENANCE.json. Require SPARK_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, exactly 27,631 files / 1,547,612,084 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `95de72bfa20d119788db4e0c54c344236f5cb01e8772b3ae1ec87402d4a913ed`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only Spark is freshly downloaded this round; Molten runtime and prior historical-chain evidence are reused, with every baseline byte rehashed. The historical chain is not redownloaded. No gameplay is executed or accepted.
