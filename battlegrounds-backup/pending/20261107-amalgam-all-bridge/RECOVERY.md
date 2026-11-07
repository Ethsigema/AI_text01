# Recover the Amalgam ALL bridge source

Source-byte verification only. This is new reconstruction, not recovery of the lost original or gameplay acceptance. Preserve all backups. This increment requires the exact Drakkari Chimera bridge baseline.

## Restore the prerequisite chain

Follow the immutable Drakkari recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/f37e3632220ea8ec00734443b62927a062ced48a/battlegrounds-backup/pending/20261107-drakkari-chimera-bridge/RECOVERY.md

Follow its linked randomized Chimera bridge, recruit bridge, Rodeo, Chimera, Mythrax, Amalgam and Electron recipes to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe downloads the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories, and enough space for retained archives and independent runtime copies.

The completed Drakkari directory must contain `restored_drakkari_runtime` and `drakkari/extracted/drakkari_chimera_bridge_20261107/SOURCE_MAP.json`. Require 27,526 files / 1,546,523,624 bytes and SOURCE_MAP SHA256 `3d7912ba375c31ef80867c78d7bfe36380596bb531606db4563f58ffcfda0288`. Leave the verified baseline unmodified; do not launch Godot in it before verification.

Supporting receipts: `DRAKKARI_REMOTE_CHAIN_VERIFICATION.json` SHA256 `ec57603b02864f8a865b25935d8aa2dcd915613883cacb88577e51305b157a31`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter records independent fresh historical-chain recovery through Theotar. Receipts are evidence, not replacements for source bytes.

## Download and restore the ALL bridge

Place `verify_and_restore_all_bridge.py` in another new empty directory:

```sh
python3 verify_and_restore_all_bridge.py --drakkari-recovery /path/to/completed-drakkari-recovery
```

The Python standard-library helper freshly downloads MANIFEST.json, 5 binary parts, REMOVALS.json and CHANGES.json from immutable commit `e491723278e6068d6e001f0e7f9b7027827b5715`, directory `battlegrounds-backup/pending/20261107-amalgam-all-bridge`. Archive: 1,049,612 bytes, SHA256 `157b43f2d5e4cf8749f58dd0858df764c9ba3d67d3f5c8434fba7fc820222bb0`.

It verifies every part, the assembled archive and all 38 members, rejecting unsafe paths/types. Both companions are size/hash-checked against MANIFEST.json companion_files. Their added/modified/removed arrays must equal the actual map differences: 6 modifications, no additions/removals. REMOVALS.json must also match manifest removed_source_files. Drakkari SOURCE_MAP and ALL bridge BASE_MAP must be byte-identical, and every baseline file is rehashed.

The helper independently copies `restored_all_bridge_runtime` without hardlinks, then rehashes every output file and the unchanged baseline. Require `ALL_BRIDGE_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,526 files / 1,546,524,109 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `1c1bc2d4916afc3e457ea61faf8ce8592b78653c76a08c756e2e1c9c0b04e9dd`. Per-file origins are recorded in RESTORE_PROVENANCE.json.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. This helper freshly downloads only the Amalgam ALL bridge increment and rehashes the verified Drakkari baseline; use the prerequisite recipes for fresh historical downloads. Gameplay is not executed or accepted by this verification.
