# Recover Timewarp Swirler Molten source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve all backups and hardlinks. The exact Golden Scout baseline is required.

## Restore the prerequisite chain

Follow the immutable Golden Scout recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/c4d3d4c965f264f9948111d7ee2f3629d80185df/battlegrounds-backup/pending/20261107-timewarp-scout-golden/RECOVERY.md

Follow its pinned prerequisites through Scout, Red Whelp, Spark, Molten, Murky and every earlier increment to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The Golden Scout recovery directory must contain `restored_golden_scout_runtime` and `golden_scout/extracted/timewarp_scout_golden_20261107/SOURCE_MAP.json`. Require 27,645 files / 1,547,792,627 bytes and SOURCE_MAP SHA256 `b181d94c863a5d5016e31a03f89d3120c42a06f42ed7fbb3c8d42acdb975c2b4`. Do not modify it or launch Godot in it before verification.

Place these published receipts in that Golden Scout directory:

- GOLDEN_SCOUT_REMOTE_CHAIN_VERIFICATION.json, SHA256 `269b7d7e51785ad7a4eec0f8773b89cdd49e8773e08912ffc86176955c920a22`.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 `edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2`.

The earlier whole-chain check freshly verified historical bytes through Murky. Later pinned receipts connect Murky through Molten, Spark, Red Whelp, Scout and Golden Scout. This helper pins both supplied hashes, checks endpoint and prior continuity, then directly rehashes every Golden Scout byte. Receipts are supporting evidence, not source substitutes or a new historical-download claim.

## Download and restore Swirler

Place `verify_and_restore_swirler.py` in another new empty directory:

```sh
python3 verify_and_restore_swirler.py --golden_scout-recovery /path/to/completed-golden-scout-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 14 binary parts, REMOVALS.json and CHANGES.json from immutable commit `7257b80eb553009100db9f260197fd39e75ac5bc`, directory `battlegrounds-backup/pending/20261107-timewarp-swirler-molten`. Archive: 3,255,168 bytes, SHA256 `25706de9d052246efdf43713f3464f1056e3c95c4392d854c631cdf42d4e67f3`.

Every part, assembled archive and all 130 members are verified, rejecting unsafe paths/types. Companion sizes/hashes must match MANIFEST.json companion_files and actual differences: 5 additions, 79 modifications, no removals. REMOVALS.json also must match manifest removed_source_files. Golden Scout SOURCE_MAP must byte-equal Swirler BASE_MAP; all baseline bytes are rehashed.

The helper independently copies `restored_swirler_runtime` without hardlinks and never writes baseline files. Every output and unchanged baseline are rehashed, with per-file RESTORE_PROVENANCE.json. Require SWIRLER_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,650 files / 1,547,851,439 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `3c73101f8f0d4f215f127efb6773df218c52032d43afb78891c2a2629f5be476`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only Swirler is freshly downloaded this round. Golden Scout and historical evidence are reused, with all baseline bytes rehashed; the historical chain is not redownloaded. No gameplay is executed or accepted.
