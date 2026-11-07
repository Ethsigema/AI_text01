# Recover Timewarp Murky base source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve all backups and shared hardlinks. The exact verified Timewarp Painter baseline is required.

## Restore the prerequisite chain

Follow the immutable Timewarp Painter recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/6ec4a6a25f8549a78277cc49e62181908fae8207/battlegrounds-backup/pending/20261107-timewarp-painter-base/RECOVERY.md

Follow its prerequisite links through Air Baller, Temperature Shift, Snow, Fire, dynamic spells and all earlier increments to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and enough space for retained archives and independent runtimes.

The completed Painter recovery directory must contain `restored_painter_runtime` and `painter/extracted/timewarp_painter_base_20261107/SOURCE_MAP.json`. Require 27,604 files / 1,547,279,535 bytes and SOURCE_MAP SHA256 `bc2a6ee18a9d14875b104dbb990544cf1299ea93c03885da66fec8cea5c09246`. Do not modify the baseline or launch Godot in it before verification.

Supporting receipts: `PAINTER_REMOTE_CHAIN_VERIFICATION.json` SHA256 `4d33aca316bf2c0e6ec2647283d67a686102a5587a3350738774558209e83450`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter documents independently fresh historical recovery through Theotar; later pinned recipes and receipts connect that baseline through Timewarp Painter. Receipts do not replace source bytes.

## Download and restore Timewarp Murky

Place `verify_and_restore_murky.py` in another new empty directory:

```sh
python3 verify_and_restore_murky.py --painter-recovery /path/to/completed-painter-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 12 binary parts, REMOVALS.json and CHANGES.json from immutable commit `e7adf5e9d3a3105241193bc867113ffda9b5bd80`, directory `battlegrounds-backup/pending/20261107-timewarp-murky-base`. Archive: 2,825,608 bytes, SHA256 `4227d199db7f7e92edf24fe1a12f630fb2cde86378bf21d72f06e8e3a9802a85`.

Every part, assembled archive and all 109 members are verified, rejecting unsafe paths/types. Both companions are hash/size checked against MANIFEST.json companion_files; their arrays must equal actual differences: 9 additions, 69 modifications, no removals. REMOVALS.json must also match manifest removed_source_files. Painter SOURCE_MAP must byte-equal Murky BASE_MAP; every baseline file is rehashed.

The helper independently copies `restored_murky_runtime` without hardlinks and never writes baseline files. It rehashes every output and the unchanged baseline, recording per-file RESTORE_PROVENANCE.json. Require `MURKY_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,613 files / 1,547,398,343 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `2a72dcaf1d6166065182f3c40c2aadb115cd50b427a7687a667521719febd443`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. This helper freshly downloads Murky only and rehashes the already-verified Painter baseline; it does not redownload the historical chain. Use prerequisite recipes to download that chain anew. No gameplay is executed or accepted by source verification.

## Additional fresh whole-chain verification

FRESH_WHOLE_CHAIN_VERIFICATION.json records a separate completed check using freshly downloaded original release ZIP, new pinned Git snapshots, and every later increment through Murky: 70 historical part manifests, 103 archive scans, 27 increments, 238 increment parts and 2,047 increment members. Every historical target byte was matched by hash, then each fresh delta was composed through exact dependency maps to all 27,613 Murky files / 1,547,398,343 bytes. No second complete runtime was written during this check. Murky bytes freshly downloaded during the same task were reused within this check, not downloaded twice.

This fresh composition proof is distinct from MURKY_REMOTE_CHAIN_VERIFICATION.json, whose independent runtime used the previously verified Painter baseline plus fresh Murky bytes. No claim is made that that runtime was written from the later fresh historical downloads. Both checks passed independently.

To reproduce the fresh composition check, put RUN_FRESH_CHAIN.sh, verify_historical_bytes.py, verify_fresh_increment_chain.py and PINNED_INCREMENT_CHAIN.json in another new empty directory, then run `sh RUN_FRESH_CHAIN.sh`. The portable variant downloads Murky itself too; it has no private workspace dependency. It uses the same executed verification logic with pinned coordinates externalized and same-task Murky reuse removed; this portable sourcing wrapper was syntax-checked, not redundantly rerun. See FRESH_CHECK_METHOD.md for exact distinctions. Preserve all downloaded evidence. No gameplay validation is implied.
