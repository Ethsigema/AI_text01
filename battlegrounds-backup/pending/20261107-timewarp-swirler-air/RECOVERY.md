# Recover Timewarp Swirler Air source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve every backup and hardlink. The exact verified Swirler Molten baseline is required.

## Restore the prerequisite chain

Follow the immutable Swirler Molten recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/8533853fec40dcace4510ab0c7b520dd50d98217/battlegrounds-backup/pending/20261107-timewarp-swirler-molten/RECOVERY.md

Follow its pinned prerequisites through Golden Scout, Scout, Red Whelp, Spark, Molten, Murky and all earlier increments to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not just the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The Swirler recovery directory must contain `restored_swirler_runtime` and `swirler/extracted/timewarp_swirler_molten_20261107/SOURCE_MAP.json`. Require 27,650 files / 1,547,851,439 bytes and SOURCE_MAP SHA256 `3c73101f8f0d4f215f127efb6773df218c52032d43afb78891c2a2629f5be476`. Do not modify it or launch Godot in it before verification.

Place these published receipts in that Swirler directory:

- SWIRLER_REMOTE_CHAIN_VERIFICATION.json, SHA256 `385567b747cf38336f3d33ff429de8f950936f0948d0dac6e32df9435b130c29`.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 `edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2`.

The earlier whole-chain check freshly verified historical bytes through Murky. Later pinned receipts connect that endpoint through Molten, Spark, Red Whelp, Scout, Golden Scout and Swirler Molten. This helper pins both supplied receipt hashes, checks endpoint/prior continuity and directly rehashes all Swirler bytes. Receipts are supporting evidence, not source substitutes or a new historical-download claim.

## Download and restore Swirler Air

Place `verify_and_restore_swirler_air.py` in another new empty directory:

```sh
python3 verify_and_restore_swirler_air.py --swirler-recovery /path/to/completed-swirler-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 5 binary parts, REMOVALS.json and CHANGES.json from immutable commit `96dee8c079156c30a717e46e2630d79a596c52e5`, directory `battlegrounds-backup/pending/20261107-timewarp-swirler-air`. Archive: 1,069,796 bytes, SHA256 `ef9255cdb356b236e99349486b0b460ade7cd13e4a69fc6aea486c4563118a4c`.

Every part, assembled archive and all 50 members are verified, rejecting unsafe paths/types. Companion sizes/hashes must match MANIFEST.json companion_files and actual differences: 6 modifications, no additions/removals. REMOVALS.json also must match manifest removed_source_files. Swirler SOURCE_MAP must byte-equal Swirler Air BASE_MAP; all baseline bytes are rehashed.

The helper independently copies `restored_swirler_air_runtime` without hardlinks and never writes baseline files. Every output and unchanged baseline are rehashed, with per-file RESTORE_PROVENANCE.json. Require SWIRLER_AIR_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,650 files / 1,547,853,328 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `62e6602590ccb3b1793e5bc91b7e72080ff9c69d4558cd17bae36621fab6a8b0`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only Swirler Air is freshly downloaded this round. Swirler and historical evidence are reused, with all baseline bytes rehashed; the historical chain is not redownloaded. No gameplay is executed or accepted.
