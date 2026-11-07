# Recover the reconstructed Bridge source

This verifies source bytes only. It is new reconstruction, not recovery of the lost November 6 original, and is not gameplay acceptance. Preserve all old backups. Bridge is an increment requiring the exact Rodeo dependency.

## Obtain the complete Rodeo dependency

Follow this immutable Rodeo recovery document and its `verify_and_restore_rodeo.py` helper:

https://github.com/Ethsigema/AI_text01/blob/fe15aeeba85911aa4ccf9fed6295bdb04e4e1627/battlegrounds-backup/pending/20261107-rodeo-reconstruction/RECOVERY.md

Follow that document through the Chimera, Mythrax, Amalgam and Electron dependency recipes to the complete immutable Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`, including original November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and exact Wrathguard/Theotar increments. Follow its archive hash-index restoration, not only the repository's older RESTORE.md. Run each recipe in its prescribed fresh directory and retain all evidence. Use Python 3, Git, curl and tar and allow several GB for archives and independent runtime copies.

Rodeo must end with 27,525 files / 1,546,515,199 bytes, no extra or mismatched files. Its SOURCE_MAP SHA256 must be `f1167a1cfc675e58bc6babec70b2af586d2f9a171283ef32360e733a8782be39`. Keep this verified runtime unmodified, without running Godot in it before the next step.

Supporting receipts supplied here are `RODEO_REMOTE_CHAIN_VERIFICATION.json` (SHA256 `84dba05b6b81f99caf4afad6004a077e839a334a9e70b039525d36ed5e11022d`) and `FRESH_FULL_CHAIN_VERIFICATION.json` (SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`). The latter documents independent fresh download and restoration of the complete historical chain through Theotar. These are supporting evidence, not substitutes for the dependency source bytes.

## Download and independently restore Bridge

Place `verify_and_restore_bridge.py` in a new empty directory. Run:

```sh
python3 verify_and_restore_bridge.py --rodeo-recovery /path/to/completed-rodeo-recovery
```

The argument is the directory containing `restored_rodeo_runtime` and `rodeo/extracted/timewarp_rodeo_rebuild_20261107/SOURCE_MAP.json`, not the runtime directory itself. The standard-library helper downloads immutable commit `f713aab526335bc98c039f8a92896d3ae00c402d`, path `battlegrounds-backup/pending/20261107-chimera-recruit-bridge`: MANIFEST.json and 5 binary parts. Required archive size is 1,076,072 bytes; SHA256 `5f49742aa35e2c8badfd491bc0e5af22b55c869d6851f31637aaf1e87f93bfb6`.

The helper checks each part, assembled archive and all 60 members, rejects unsafe member paths/types, verifies Rodeo SOURCE_MAP byte-equals Bridge BASE_MAP and rehashes every baseline file. The exact delta is 6 files: 5 modified, 1 added, no removals. It creates an independent `restored_bridge_runtime` with no hardlinks, hashes the complete output, and rehashes the baseline to prove it remains unchanged. No deletion or remote writes occur. Existing destination directories are not overwritten; preserve failed attempts and retry in a fresh directory.

Require `BRIDGE_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, exactly 27,526 files / 1,546,521,203 bytes, and empty missing/mismatched/unexpected lists. Target SOURCE_MAP SHA256 must be `ba5f61b6263fba3ab6303bedbf83640f7b2e33ca4e6b0e21383c13a2f975ef69`. `RESTORE_PROVENANCE.json` records the source of each output file.

This helper freshly downloads Bridge only; earlier source bytes come from the verified Rodeo dependency and are all rehashed. The earlier full-chain recipe and supporting receipts establish the historical provenance. Recovery verification does not execute gameplay, validate natural acquisition, or establish full gameplay/UI acceptance. Consult the package's own validation records for bounded test scope.

## Explicit removals

The helper also downloads REMOVALS.json, validates its size and SHA256 against MANIFEST.json companion_files, requires its empty list to equal removed_source_files and the actual BASE_MAP minus SOURCE_MAP path set. No file removals are needed. The original archive is preserved unchanged; the removal list is a separately hash-bound companion.
