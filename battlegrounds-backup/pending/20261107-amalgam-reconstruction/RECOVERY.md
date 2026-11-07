# Recover the reconstructed Amalgam source

This verifies source bytes only. It is new reconstruction, not recovery of the lost November 6 original, and is not gameplay acceptance. Preserve all old backups. Amalgam is an increment requiring the exact Electron dependency.

## Obtain the complete Electron dependency

Follow this immutable Electron recovery document and its `verify_and_restore_electron.py` helper:

https://github.com/Ethsigema/AI_text01/blob/66ea40c7527f149cfc12d4e325287375a475b35b/battlegrounds-backup/pending/20261107-electron-reconstruction/RECOVERY.md

That document links the complete immutable Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`, including original November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and exact Wrathguard/Theotar increments. Follow its archive hash-index restoration, not only the repository's older RESTORE.md. Run each recipe in its prescribed fresh directory and retain all evidence. Use Python 3, Git, curl and tar and allow several GB for archives and independent runtime copies.

Electron must end with 27,489 files / 1,546,358,376 bytes, no extra or mismatched files. Its SOURCE_MAP SHA256 must be `8e099df06e47a901875a526a0ea21edcbf21406758f786b77078b8f00845492d`. Keep this verified runtime unmodified, without running Godot in it before the next step.

Supporting receipts supplied here are `ELECTRON_REMOTE_CHAIN_VERIFICATION.json` (SHA256 `db112f966e3007373cdb58f23ce9b588966334169b7cf1e3d76e70f10fcba5e3`) and `FRESH_FULL_CHAIN_VERIFICATION.json` (SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`). The latter documents independent fresh download and restoration of the complete historical chain through Theotar. These are supporting evidence, not substitutes for the dependency source bytes.

## Download and independently restore Amalgam

Place `verify_and_restore_amalgam.py` in a new empty directory. Run:

```sh
python3 verify_and_restore_amalgam.py --electron-recovery /path/to/completed-electron-recovery
```

The argument is the directory containing `restored_electron_runtime` and `electron/extracted/timewarp_electron_rebuild_20261107/SOURCE_MAP.json`, not the runtime directory itself. The standard-library helper downloads immutable commit `1859fa0d46420ae19feceeb97f8ba5d0ee15073f`, path `battlegrounds-backup/pending/20261107-amalgam-reconstruction`: MANIFEST.json and 12 binary parts. Required archive size is 2,793,084 bytes; SHA256 `7f0733c2a68d4f7bb831d77f77d313207bb391468a25bf6c4d43439fb9e2f236`.

The helper checks each part, assembled archive and all 115 members, rejects unsafe member paths/types, verifies Electron SOURCE_MAP byte-equals Amalgam BASE_MAP and rehashes every baseline file. The exact delta is 58 files: 49 modified, 9 added, no removals. It creates an independent `restored_amalgam_runtime` with no hardlinks, hashes the complete output, and rehashes the baseline to prove it remains unchanged. No deletion or remote writes occur. Existing destination directories are not overwritten; preserve failed attempts and retry in a fresh directory.

Require `AMALGAM_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, exactly 27,498 files / 1,546,393,840 bytes, and empty missing/mismatched/unexpected lists. Target SOURCE_MAP SHA256 must be `c24bdf4bedf966056670677d504207c3259bf4b3806afc5d2a2f2acb491d53de`. `RESTORE_PROVENANCE.json` records the source of each output file.

This helper freshly downloads Amalgam only; earlier source bytes come from the verified Electron dependency and are all rehashed. The earlier full-chain recipe and supporting receipts establish the historical provenance. Recovery verification does not execute gameplay, validate natural acquisition, or establish full gameplay/UI acceptance. Consult the package's own validation records for bounded test scope.
