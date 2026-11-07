# Recover the reconstructed Rodeo source

This verifies source bytes only. It is new reconstruction, not recovery of the lost November 6 original, and is not gameplay acceptance. Preserve all old backups. Rodeo is an increment requiring the exact Chimera dependency.

## Obtain the complete Chimera dependency

Follow this immutable Chimera recovery document and its `verify_and_restore_chimera.py` helper:

https://github.com/Ethsigema/AI_text01/blob/5b936e03dc323efe07f2d5e29ba13a20aae3d5c2/battlegrounds-backup/pending/20261107-chimera-reconstruction/RECOVERY.md

Follow that document through the Mythrax, Amalgam and Electron dependency recipes to the complete immutable Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`, including original November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and exact Wrathguard/Theotar increments. Follow its archive hash-index restoration, not only the repository's older RESTORE.md. Run each recipe in its prescribed fresh directory and retain all evidence. Use Python 3, Git, curl and tar and allow several GB for archives and independent runtime copies.

Chimera must end with 27,516 files / 1,546,472,180 bytes, no extra or mismatched files. Its SOURCE_MAP SHA256 must be `2f30ae8f177cc4c1b12ce0c8e34d295aa4d991ac8c4f524c56bfab58e05925d8`. Keep this verified runtime unmodified, without running Godot in it before the next step.

Supporting receipts supplied here are `CHIMERA_REMOTE_CHAIN_VERIFICATION.json` (SHA256 `b8f275c38ede201d2610bd190d2be0ce82eeaa8d96129f4f94b415026f67a7fd`) and `FRESH_FULL_CHAIN_VERIFICATION.json` (SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`). The latter documents independent fresh download and restoration of the complete historical chain through Theotar. These are supporting evidence, not substitutes for the dependency source bytes.

## Download and independently restore Rodeo

Place `verify_and_restore_rodeo.py` in a new empty directory. Run:

```sh
python3 verify_and_restore_rodeo.py --chimera-recovery /path/to/completed-chimera-recovery
```

The argument is the directory containing `restored_chimera_runtime` and `chimera/extracted/timewarp_chimera_rebuild_20261107/SOURCE_MAP.json`, not the runtime directory itself. The standard-library helper downloads immutable commit `707cd3fed534172ae72418fdeb9809bfe2402cde`, path `battlegrounds-backup/pending/20261107-rodeo-reconstruction`: MANIFEST.json and 13 binary parts. Required archive size is 3,207,808 bytes; SHA256 `6e35af0fca0b7a504708c818e7c0207c4f04e39e15c4e2ba6cf135653825b966`.

The helper checks each part, assembled archive and all 110 members, rejects unsafe member paths/types, verifies Chimera SOURCE_MAP byte-equals Rodeo BASE_MAP and rehashes every baseline file. The exact delta is 65 files: 56 modified, 9 added, no removals. It creates an independent `restored_rodeo_runtime` with no hardlinks, hashes the complete output, and rehashes the baseline to prove it remains unchanged. No deletion or remote writes occur. Existing destination directories are not overwritten; preserve failed attempts and retry in a fresh directory.

Require `RODEO_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, exactly 27,525 files / 1,546,515,199 bytes, and empty missing/mismatched/unexpected lists. Target SOURCE_MAP SHA256 must be `f1167a1cfc675e58bc6babec70b2af586d2f9a171283ef32360e733a8782be39`. `RESTORE_PROVENANCE.json` records the source of each output file.

This helper freshly downloads Rodeo only; earlier source bytes come from the verified Chimera dependency and are all rehashed. The earlier full-chain recipe and supporting receipts establish the historical provenance. Recovery verification does not execute gameplay, validate natural acquisition, or establish full gameplay/UI acceptance. Consult the package's own validation records for bounded test scope.
