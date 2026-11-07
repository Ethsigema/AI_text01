# Recover the reconstructed Chimera source

This verifies source bytes only. It is new reconstruction, not recovery of the lost November 6 original, and is not gameplay acceptance. Preserve all old backups. Chimera is an increment requiring the exact Mythrax dependency.

## Obtain the complete Mythrax dependency

Follow this immutable Mythrax recovery document and its `verify_and_restore_mythrax.py` helper:

https://github.com/Ethsigema/AI_text01/blob/898c71b742b58bb02024a5c0106aea27578a2f79/battlegrounds-backup/pending/20261107-mythrax-reconstruction/RECOVERY.md

Follow that document through the Amalgam and Electron dependency recipes to the complete immutable Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`, including original November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and exact Wrathguard/Theotar increments. Follow its archive hash-index restoration, not only the repository's older RESTORE.md. Run each recipe in its prescribed fresh directory and retain all evidence. Use Python 3, Git, curl and tar and allow several GB for archives and independent runtime copies.

Mythrax must end with 27,507 files / 1,546,431,495 bytes, no extra or mismatched files. Its SOURCE_MAP SHA256 must be `f87e45df66016dcffa35e07d20e4f3aec5dd167e583f60bd6fb7c7318bb7cf95`. Keep this verified runtime unmodified, without running Godot in it before the next step.

Supporting receipts supplied here are `MYTHRAX_REMOTE_CHAIN_VERIFICATION.json` (SHA256 `77f6280a7f7baa7be3aba777e1b05ab57960d6dd200edbae4f5beed28f49f925`) and `FRESH_FULL_CHAIN_VERIFICATION.json` (SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`). The latter documents independent fresh download and restoration of the complete historical chain through Theotar. These are supporting evidence, not substitutes for the dependency source bytes.

## Download and independently restore Chimera

Place `verify_and_restore_chimera.py` in a new empty directory. Run:

```sh
python3 verify_and_restore_chimera.py --mythrax-recovery /path/to/completed-mythrax-recovery
```

The argument is the directory containing `restored_mythrax_runtime` and `mythrax/extracted/timewarp_mythrax_rebuild_20261107/SOURCE_MAP.json`, not the runtime directory itself. The standard-library helper downloads immutable commit `3a247a00aa8b02694875354498ae4c1a1e3223ab`, path `battlegrounds-backup/pending/20261107-chimera-reconstruction`: MANIFEST.json and 12 binary parts. Required archive size is 2,801,160 bytes; SHA256 `85909f7da4581207da4ccc0ed16d4248cc20df29cd60f55bde3321d0c26b313a`.

The helper checks each part, assembled archive and all 94 members, rejects unsafe member paths/types, verifies Mythrax SOURCE_MAP byte-equals Chimera BASE_MAP and rehashes every baseline file. The exact delta is 62 files: 53 modified, 9 added, no removals. It creates an independent `restored_chimera_runtime` with no hardlinks, hashes the complete output, and rehashes the baseline to prove it remains unchanged. No deletion or remote writes occur. Existing destination directories are not overwritten; preserve failed attempts and retry in a fresh directory.

Require `CHIMERA_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, exactly 27,516 files / 1,546,472,180 bytes, and empty missing/mismatched/unexpected lists. Target SOURCE_MAP SHA256 must be `2f30ae8f177cc4c1b12ce0c8e34d295aa4d991ac8c4f524c56bfab58e05925d8`. `RESTORE_PROVENANCE.json` records the source of each output file.

This helper freshly downloads Chimera only; earlier source bytes come from the verified Mythrax dependency and are all rehashed. The earlier full-chain recipe and supporting receipts establish the historical provenance. Recovery verification does not execute gameplay, validate natural acquisition, or establish full gameplay/UI acceptance. Consult the package's own validation records for bounded test scope.
