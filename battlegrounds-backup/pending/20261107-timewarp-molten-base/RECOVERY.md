# Recover Timewarp Molten base source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve all backups and shared hardlinks. The exact verified Murky baseline is required.

## Restore the prerequisite chain

Follow the immutable Murky recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/bce9cbf95bbd9e6c9174f547db48d5d900cd2ff0/battlegrounds-backup/pending/20261107-timewarp-murky-base/RECOVERY.md

Follow its pinned prerequisite recipes through Painter, Air, Temperature Shift, Snow, Fire and all earlier increments to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction rather than only the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and sufficient space for retained archives and independent runtimes.

The completed Murky recovery directory must contain `restored_murky_runtime` and `murky/extracted/timewarp_murky_base_20261107/SOURCE_MAP.json`. Require 27,613 files / 1,547,398,343 bytes and SOURCE_MAP SHA256 `2a72dcaf1d6166065182f3c40c2aadb115cd50b427a7687a667521719febd443`. Do not modify the baseline or launch Godot in it before verification.

Place the published `FRESH_WHOLE_CHAIN_VERIFICATION.json` in that Murky recovery directory as supporting evidence. Its SHA256 must be `edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2`. This records the previous separate fresh-chain check: original ZIP and new pinned Git snapshots, 70 historical part manifests / 103 archive scans, and 27 fresh increments through Murky. All target source bytes were proven by hash composition without another complete runtime directory. The helper checks that receipt's final source map equals its reused Murky baseline.

Also supplied: `MURKY_REMOTE_CHAIN_VERIFICATION.json`, SHA256 `5926820e2bb4bd6aa1ed3ac9b99689cb8fb083474e6d7377df806d84b21f2498`. Supporting receipts do not replace source bytes or imply the historical chain was redownloaded in this Molten check.

## Download and restore Molten

Place `verify_and_restore_molten.py` in another new empty directory:

```sh
python3 verify_and_restore_molten.py --murky-recovery /path/to/completed-murky-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 13 binary parts, REMOVALS.json and CHANGES.json from immutable commit `120b5f3a9b86a061be7c6860139b8937f41c8863`, directory `battlegrounds-backup/pending/20261107-timewarp-molten-base`. Archive: 3,236,600 bytes, SHA256 `1befe867b81c1f7ee6baabc93d32e89e12cc8a587f3e48c5af1cdde2e2db6c29`.

Every part, assembled archive and all 123 members are verified, rejecting unsafe paths/types. Both companions are hash/size checked against MANIFEST.json companion_files, and their arrays must equal actual differences: 9 additions, 71 modifications, no removals. REMOVALS.json must also match manifest removed_source_files. Murky SOURCE_MAP must byte-equal Molten BASE_MAP; every baseline file is rehashed.

The helper independently copies `restored_molten_runtime` without hardlinks and never writes to baseline files. It rehashes every output and the unchanged baseline, recording per-file RESTORE_PROVENANCE.json. Require `MOLTEN_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,622 files / 1,547,513,946 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `d1d1689c77b5ddf700b1d5f75ff259ca3a39ea55be0b7ccf2f1786b91c419e51`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. This check freshly downloads Molten only, reuses the verified Murky runtime and prior whole-chain evidence, and rehashes the full baseline. It does not redownload the entire historical chain this round. Murky's published fresh-chain helpers support a separate fresh historical check if desired. No gameplay is executed or accepted.
