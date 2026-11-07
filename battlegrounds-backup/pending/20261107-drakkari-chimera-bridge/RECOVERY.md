# Recover the Drakkari Chimera bridge source

Source-byte verification only. This is new reconstruction, not recovery of the lost original or gameplay acceptance. Preserve every backup. This increment requires the exact random bridge baseline.

## Restore the prerequisite chain

Follow the immutable random bridge recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/c582b4324786a88081487d581b073cc5ca8b9713/battlegrounds-backup/pending/20261107-chimera-random-bridge/RECOVERY.md

Follow its linked recruit bridge, Rodeo, Chimera, Mythrax, Amalgam and Electron recipes back to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe downloads the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the old repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and sufficient disk space for retained archives and independent runtime copies.

The completed random bridge directory must contain `restored_random_bridge_runtime` and `random_bridge/extracted/chimera_random_bridge_20261107/SOURCE_MAP.json`. Require 27,526 files / 1,546,523,202 bytes and SOURCE_MAP SHA256 `d454821446645d5dc6e299a38431a8611cc2e3d70b5c658a820e16c3f6959bd4`. Leave this baseline unmodified; do not launch Godot in it before verification.

Supporting receipts: `RANDOM_BRIDGE_REMOTE_CHAIN_VERIFICATION.json` SHA256 `ce881e6598f5299e0cc953255a95cad5db80067af2e64ee58ae592572c5907d9`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter records independently fresh historical-chain recovery through Theotar. Receipts are evidence, not replacements for source bytes.

## Download and restore Drakkari

Place `verify_and_restore_drakkari.py` in another new empty directory:

```sh
python3 verify_and_restore_drakkari.py --random_bridge-recovery /path/to/completed-random-bridge-recovery
```

The Python standard-library helper freshly downloads MANIFEST.json, 5 binary parts, REMOVALS.json and CHANGES.json from immutable commit `8a492883700b1ac392900955387b907f6c2e8801`, directory `battlegrounds-backup/pending/20261107-drakkari-chimera-bridge`. Archive: 1,063,800 bytes, SHA256 `cede912e7dd1a265fc3ee198f4d84550e94bbbebfe1c4575e2af716897a78ab6`.

It verifies all parts, assembled archive and 37 members, rejecting unsafe paths/types. Both companion files are size/hash-checked against MANIFEST.json companion_files. Their added/modified/removed arrays must equal actual map differences: 3 modifications, no additions/removals. REMOVALS.json must also match manifest removed_source_files. Baseline SOURCE_MAP and increment BASE_MAP must be byte-identical, and every baseline file is rehashed.

The helper independently copies `restored_drakkari_runtime` without hardlinks and rehashes every output file and the unchanged baseline. Require `DRAKKARI_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,526 files / 1,546,523,624 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `3d7912ba375c31ef80867c78d7bfe36380596bb531606db4563f58ffcfda0288`. Per-file sources appear in RESTORE_PROVENANCE.json.

Existing destinations are not overwritten. Preserve failed attempts and retry in a new directory. No deletion or remote writes occur. This helper freshly downloads Drakkari only and rehashes the supplied verified baseline; use the prerequisite recipes for fresh historical downloads. Gameplay is not executed or accepted by recovery verification.
