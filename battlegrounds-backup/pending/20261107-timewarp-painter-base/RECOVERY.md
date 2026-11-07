# Recover Timewarp Painter base source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve all backups and shared hardlinks. The exact verified Air Baller baseline is required.

## Restore the prerequisite chain

Follow the immutable Air Baller recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/44bdbdefa02b429195f5313e38296a4b0002c726/battlegrounds-backup/pending/20261107-air-baller-base/RECOVERY.md

Follow its prerequisite links through Temperature Shift, Snow, Fire, dynamic spells and all earlier increments to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and enough space for retained archives and independent runtimes.

The completed Air recovery directory must contain `restored_air_runtime` and `air/extracted/air_baller_base_20261107/SOURCE_MAP.json`. Require 27,595 files / 1,547,161,659 bytes and SOURCE_MAP SHA256 `3d326b2610fae0996fb5ae339abe8a04559fefcdba0356009313c8020854c46b`. Do not modify the baseline or launch Godot in it before verification.

Supporting receipts: `AIR_REMOTE_CHAIN_VERIFICATION.json` SHA256 `93b5a7f469b3bfd1bb2e904f8edba633418da3fd65955aea540aedaa0a044d61`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter documents independently fresh historical recovery through Theotar; later pinned recipes and receipts connect that baseline through Air Baller. Receipts do not replace source bytes.

## Download and restore Timewarp Painter

Place `verify_and_restore_painter.py` in another new empty directory:

```sh
python3 verify_and_restore_painter.py --air-recovery /path/to/completed-air-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 13 binary parts, REMOVALS.json and CHANGES.json from immutable commit `a8da85f1ca8d7f2c4d82ee43e6afe162f26756bb`, directory `battlegrounds-backup/pending/20261107-timewarp-painter-base`. Archive: 3,234,632 bytes, SHA256 `b9544311e21722384a3e7bc05597fdbc1b5e6a46ebf6eee2f9fe84d90c16c5ed`.

Every part, assembled archive and all 120 members are verified, rejecting unsafe paths/types. Both companions are hash/size checked against MANIFEST.json companion_files; their arrays must equal actual differences: 9 additions, 67 modifications, no removals. REMOVALS.json must also match manifest removed_source_files. Air SOURCE_MAP must byte-equal Painter BASE_MAP; every baseline file is rehashed.

The helper independently copies `restored_painter_runtime` without hardlinks and never writes baseline files. It rehashes every output and the unchanged baseline, recording per-file RESTORE_PROVENANCE.json. Require `PAINTER_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,604 files / 1,547,279,535 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `bc2a6ee18a9d14875b104dbb990544cf1299ea93c03885da66fec8cea5c09246`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. This helper freshly downloads Painter only and rehashes the already-verified Air baseline; it does not redownload the historical chain. Use prerequisite recipes to download that chain anew. No gameplay is executed or accepted by source verification.
