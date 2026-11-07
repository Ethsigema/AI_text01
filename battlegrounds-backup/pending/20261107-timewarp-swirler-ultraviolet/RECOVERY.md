# Recover Timewarp Swirler Ultraviolet source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve every backup and hardlink. The exact verified Swirler Air baseline is required.

## Restore the prerequisite chain

Follow the immutable Swirler Air recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/f128be1abe471dcc2374b47614c6a53c6a72ea49/battlegrounds-backup/pending/20261107-timewarp-swirler-air/RECOVERY.md

Follow its pinned prerequisites through Swirler Molten, Golden Scout, Scout, Red Whelp, Spark, Molten, Murky and all earlier increments to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not just the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The Swirler Air recovery directory must contain `restored_swirler_air_runtime` and `swirler_air/extracted/timewarp_swirler_air_20261107/SOURCE_MAP.json`. Require 27,650 files / 1,547,853,328 bytes and SOURCE_MAP SHA256 `62e6602590ccb3b1793e5bc91b7e72080ff9c69d4558cd17bae36621fab6a8b0`. Do not modify it or launch Godot in it before verification.

Place these published receipts in that Swirler Air directory:

- SWIRLER_AIR_REMOTE_CHAIN_VERIFICATION.json, SHA256 `a36dc56e645fed5ba2280a5d744d265a4c506859ebc463870feded7180fc3034`.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 `edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2`.

The earlier whole-chain check freshly verified historical bytes through Murky. Later pinned receipts connect that endpoint through Molten, Spark, Red Whelp, Scout, Golden Scout, Swirler Molten and Swirler Air. This helper pins both supplied receipt hashes, checks endpoint/prior continuity and directly rehashes all Swirler Air bytes. Receipts are supporting evidence, not source substitutes or a new historical-download claim.

## Download and restore Swirler Ultraviolet

Place `verify_and_restore_swirler_ultraviolet.py` in another new empty directory:

```sh
python3 verify_and_restore_swirler_ultraviolet.py --swirler-air-recovery /path/to/completed-swirler-air-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 6 binary parts, REMOVALS.json and CHANGES.json from immutable commit `b7ff72e43e97801ed5846cd5d491ee0d660a22a5`, directory `battlegrounds-backup/pending/20261107-timewarp-swirler-ultraviolet`. Archive: 1,295,432 bytes, SHA256 `d9fe87719cb9fb7fa482a8f4a49c91513f22aa99f73ecddad4ae4e0f28f4d74f`.

Every part, assembled archive and all 83 members are verified, rejecting unsafe paths/types. Companion sizes/hashes must match MANIFEST.json companion_files and actual differences: 51 modifications, no additions/removals. REMOVALS.json also must match manifest removed_source_files. Swirler Air SOURCE_MAP must byte-equal Swirler Ultraviolet BASE_MAP; all baseline bytes are rehashed.

The helper independently copies `restored_swirler_ultraviolet_runtime` without hardlinks and never writes baseline files. Every output and unchanged baseline are rehashed, with per-file RESTORE_PROVENANCE.json. Require SWIRLER_ULTRAVIOLET_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,650 files / 1,547,857,399 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `b7832ebe2a8d4ef16b98eb3730eb46be615a12c01cc74e484055b01fafba9249`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only Swirler Ultraviolet is freshly downloaded this round. Swirler Air and historical evidence are reused, with all baseline bytes rehashed; the historical chain is not redownloaded. No gameplay is executed or accepted.
