# Recover the Chimera random bridge source

Source-byte verification only: this is new reconstruction, not recovery of the lost original or gameplay acceptance. Preserve all backups. The increment requires the exact recruit bridge baseline.

## Restore the complete prerequisite chain

Follow the immutable recruit bridge recipe and its tested helper:

https://github.com/Ethsigema/AI_text01/blob/1565ae7402d9f21c411e2400ce3e49cdaa008156/battlegrounds-backup/pending/20261107-chimera-recruit-bridge/RECOVERY.md

Follow its prerequisite links through Rodeo, Chimera, Mythrax, Amalgam and Electron to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe downloads the original November 1 ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the old repository RESTORE.md. Use Python 3, Git, curl and tar, fresh work directories and sufficient disk space for archives and independent runtimes.

The completed recruit bridge directory must contain `restored_bridge_runtime` and `bridge/extracted/chimera_recruit_bridge_20261107/SOURCE_MAP.json`. Require 27,526 exact files / 1,546,521,203 bytes and SOURCE_MAP SHA256 `ba5f61b6263fba3ab6303bedbf83640f7b2e33ca4e6b0e21383c13a2f975ef69`. Do not open Godot in this baseline before the next verification.

Supporting receipts: `BRIDGE_REMOTE_CHAIN_VERIFICATION.json` SHA256 `bee79c22e2b3ce12fa6ff1ac770f73f0cc8626607da2fc4e31eb58307992f6d7`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter records an independent fresh historical-chain download through Theotar. Receipts do not replace required source bytes.

## Download and restore the random bridge

Place `verify_and_restore_random_bridge.py` in another new empty directory:

```sh
python3 verify_and_restore_random_bridge.py --bridge-recovery /path/to/completed-recruit-bridge-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 5 binary parts, REMOVALS.json and CHANGES.json from immutable commit `de33b3f720d4461fc9084e7527bbc3195efd963d`, directory `battlegrounds-backup/pending/20261107-chimera-random-bridge`. Archive: 1,072,328 bytes; SHA256 `e140a1799a047b4b04a38c474a410ae2b681435273caf41f69e9d4263203778a`.

It validates each part, assembled archive and all 40 members; rejects unsafe member paths/types; verifies both companions against MANIFEST.json companion_files; and compares their added/modified/removed lists to the actual source map difference. Exactly 7 files are modified, none added or removed. REMOVALS.json must also equal manifest removed_source_files. It requires byte-identical baseline SOURCE_MAP and increment BASE_MAP and rehashes all baseline files.

A new independent `restored_random_bridge_runtime` is copied without hardlinks, then fully hashed. The baseline is rehashed unchanged. Require `RANDOM_BRIDGE_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,526 files / 1,546,523,202 bytes, empty missing/mismatched/unexpected lists, and SOURCE_MAP SHA256 `d454821446645d5dc6e299a38431a8611cc2e3d70b5c658a820e16c3f6959bd4`. Per-file origins are in RESTORE_PROVENANCE.json.

Existing destinations are not overwritten. Keep failed attempts and use a fresh directory for retries. No deletion or remote modification occurs. This helper freshly downloads only the random bridge, reusing and rehashing the verified baseline; follow the prerequisite recipe to download the earlier chain anew. No gameplay is executed or accepted by this verification.
