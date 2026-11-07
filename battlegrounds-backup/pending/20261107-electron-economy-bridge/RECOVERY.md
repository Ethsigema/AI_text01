# Recover the Electron economy bridge source

Source-byte verification only. This is new reconstruction, not recovery of the lost original or gameplay acceptance. Preserve all backups. This increment requires the exact Amalgam ALL bridge baseline.

## Restore the prerequisite chain

Follow the immutable Amalgam ALL bridge recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/6f2c7ae1d939a4dfd1c98449019ea377bd80de8b/battlegrounds-backup/pending/20261107-amalgam-all-bridge/RECOVERY.md

Follow its linked Drakkari, randomized Chimera bridge, recruit bridge, Rodeo, Chimera, Mythrax, Amalgam and Electron recipes to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe downloads the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and enough space for retained archives and independent runtime copies.

The completed ALL bridge directory must contain `restored_all_bridge_runtime` and `all_bridge/extracted/amalgam_all_bridge_20261107/SOURCE_MAP.json`. Require 27,526 files / 1,546,524,109 bytes and SOURCE_MAP SHA256 `1c1bc2d4916afc3e457ea61faf8ce8592b78653c76a08c756e2e1c9c0b04e9dd`. Leave the verified baseline unmodified; do not launch Godot in it before verification.

Supporting receipts: `ALL_BRIDGE_REMOTE_CHAIN_VERIFICATION.json` SHA256 `b5de179a414c7b01c5c4479da3871004496a07dab1e3bc47a6c0ea10778eee1a`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter records independent fresh historical-chain recovery through Theotar. Receipts are evidence, not replacements for source bytes.

## Download and restore the economy bridge

Place `verify_and_restore_economy.py` in another new empty directory:

```sh
python3 verify_and_restore_economy.py --all_bridge-recovery /path/to/completed-all-bridge-recovery
```

The Python standard-library helper freshly downloads MANIFEST.json, 5 binary parts, REMOVALS.json and CHANGES.json from immutable commit `9e5970c858ed126f40b198282b902fac5fd2864a`, directory `battlegrounds-backup/pending/20261107-electron-economy-bridge`. Archive: 1,063,732 bytes, SHA256 `438990b43593dd35722002c075223fe4cf101708a9b7209d09e5b896b8bb182c`.

It verifies every part, assembled archive and all 42 members, rejecting unsafe paths/types. Both companions are size/hash-checked against MANIFEST.json companion_files. Their added/modified/removed arrays must equal actual map differences: 5 additions, 5 modifications, no removals. REMOVALS.json must also match manifest removed_source_files. ALL bridge SOURCE_MAP and economy BASE_MAP must be byte-identical, and every baseline file is rehashed.

The helper independently copies `restored_economy_runtime` without hardlinks, then rehashes every output file and the unchanged baseline. Require `ECONOMY_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,531 files / 1,546,535,856 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `faa285f0648287c779cefa6f185a22f6355eab160db752f05a2d10a7c459d133`. Per-file origins are recorded in RESTORE_PROVENANCE.json.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. This helper freshly downloads only the Electron economy bridge increment and rehashes the verified Amalgam ALL baseline; use the prerequisite recipes for fresh historical downloads. Gameplay is not executed or accepted by this verification.
