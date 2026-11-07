# Recover Timewarp Golden Scout source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve all backups and hardlinks. The exact verified Scout baseline is required.

## Restore the prerequisite chain

Follow the immutable Scout recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/5d1396ad54b7a3085e8b64566776bbf40d174a01/battlegrounds-backup/pending/20261107-timewarp-scout-base/RECOVERY.md

Follow its pinned prerequisites through Red Whelp, Spark, Molten, Murky and all earlier increments to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the old repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient disk space.

The Scout recovery directory must contain `restored_scout_runtime` and `scout/extracted/timewarp_scout_base_20261107/SOURCE_MAP.json`. Require 27,641 files / 1,547,735,641 bytes and SOURCE_MAP SHA256 `2f3de1eaccbd95c22a88d7b624aa3b9fe693e5c074f10759cfb7496e575282c0`. Do not modify it or launch Godot in it before verification.

Place these published receipts in that Scout recovery directory:

- SCOUT_REMOTE_CHAIN_VERIFICATION.json, SHA256 `d7bd4b53fea719eac540a1e79ac85a3458fa24d96f9e5ecd53f2f0811c629f4b`.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 `edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2`.

The prior whole-chain check freshly verified historical bytes through Murky. Later pinned receipts connect Murky through Molten, Spark, Red Whelp and Scout. This helper pins the two supplied receipt hashes and checks their continuity/endpoint, then directly rehashes all Scout source bytes. Receipts are supporting evidence, not replacements for source or a new historical download claim.

## Download and restore Golden Scout

Place `verify_and_restore_golden_scout.py` in another new empty directory:

```sh
python3 verify_and_restore_golden_scout.py --scout-recovery /path/to/completed-scout-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 6 binary parts, REMOVALS.json and CHANGES.json from immutable commit `9b0267afa48ce70d004da3c1608a615350112d35`, directory `battlegrounds-backup/pending/20261107-timewarp-scout-golden`. Archive: 1,295,140 bytes, SHA256 `e6d8bfc06cbc4744b908b9271b5f53dcb4efe8129d09997a21193783988c121b`.

It verifies every part, the assembled archive and all 49 members, rejecting unsafe paths/types. Companion sizes/hashes must match MANIFEST.json companion_files and actual map differences: 4 additions, 3 modifications, no removals. REMOVALS.json also must match manifest removed_source_files. Scout SOURCE_MAP must byte-equal Golden Scout BASE_MAP; every baseline byte is rehashed.

It independently copies `restored_golden_scout_runtime` without hardlinks and never writes baseline files. Every output and the unchanged baseline are rehashed, with per-file RESTORE_PROVENANCE.json. Require GOLDEN_SCOUT_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,645 files / 1,547,792,627 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `b181d94c863a5d5016e31a03f89d3120c42a06f42ed7fbb3c8d42acdb975c2b4`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only Golden Scout is freshly downloaded this round. Scout and historical evidence are reused, with all baseline bytes rehashed; the historical chain is not redownloaded. No gameplay is executed or accepted.
