# Recover Electron dynamic spells bridge source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve all backups. The exact verified Electron shared-type bridge baseline is required.

## Restore the prerequisite chain

Follow the immutable shared-type recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/8a85c0e6268e59adcbf2244fa5584b16c9347352/battlegrounds-backup/pending/20261107-electron-shared-type-bridge/RECOVERY.md

Follow its linked double spell Discover, spell Discover, stock Discover, Hooktusk base, Ultraviolet, Electron shop/targeted/economy bridges, Amalgam ALL, Drakkari, randomized Chimera/recruit bridges, Rodeo, Chimera, Mythrax, Amalgam and Electron recipes to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and sufficient space for archives and independent runtimes.

The completed shared-type recovery directory must contain `restored_shared_type_runtime` and `shared_type/extracted/electron_shared_type_bridge_20261107/SOURCE_MAP.json`. Require 27,560 files / 1,546,780,587 bytes and SOURCE_MAP SHA256 `4540582564ab747c5c284ca9f9cc60aeb7703a304c29ba0475d63f59d88d40e2`. Leave the baseline unmodified; do not launch Godot in it before verification.

Supporting receipts: `SHARED_TYPE_REMOTE_CHAIN_VERIFICATION.json` SHA256 `e69c99a360d12612a504e4159dc0de6caaff40ef1c13890c9e7b31db902a208c`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter records independently fresh historical recovery through Theotar. Receipts do not replace source bytes.

## Download and restore dynamic spells

Place `verify_and_restore_dynamic.py` in another new empty directory:

```sh
python3 verify_and_restore_dynamic.py --shared_type-recovery /path/to/completed-shared-type-recovery
```

The Python standard-library helper freshly downloads MANIFEST.json, 5 binary parts, REMOVALS.json and CHANGES.json from immutable commit `e4f9ec3f04a9fd16ea1130d0e79cc0d5db257b90`, directory `battlegrounds-backup/pending/20261107-electron-dynamic-spells-bridge`. Archive: 1,067,540 bytes, SHA256 `25c73f9558afbcf9a0a41b777faa1de0c14d96fe2a4a30f41439cd9c2a2e199f`.

Every part, assembled archive and all 50 members are verified, rejecting unsafe paths/types. Both companions are hash/size checked against MANIFEST.json companion_files, and their arrays must equal actual map differences: 4 additions, 5 modifications, no removals. REMOVALS.json must also match manifest removed_source_files. Baseline SOURCE_MAP must byte-equal increment BASE_MAP; every baseline file is rehashed.

The helper independently copies `restored_dynamic_runtime` without hardlinks, rehashes every output and the unchanged baseline, and records per-file RESTORE_PROVENANCE.json. Require `DYNAMIC_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,564 files / 1,546,795,597 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `693f098913d7eb84ef16e6e09e95d8edfadbce2fdfe25b956bc83af91ac761d0`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. This helper freshly downloads the dynamic spells increment only and rehashes the verified shared-type baseline; use prerequisite recipes for fresh historical downloads. No gameplay is executed or accepted by this verification.
