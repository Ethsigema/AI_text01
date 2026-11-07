# Recover the reconstructed Electron source

This is source-byte verification of new reconstruction, not recovery of the lost November 6 checkpoint and not gameplay acceptance. Preserve all old backups. The Electron increment is not standalone.

## Obtain the exact Theotar dependency

Use a new empty directory, Python 3, Git, curl and tar, with ample disk space for retained archives and two independent runtimes. Follow the immutable complete dependency recipe:

https://github.com/Ethsigema/AI_text01/blob/e23df857427307b8a29675a62156e96040c72604/battlegrounds-backup/pending/20261107-theotar-reconstruction/RECOVERY.md

Download its two helpers from that same immutable directory: `restore_bloodbound_from_archives.py` and `verify_and_restore_latest.py`. Follow the recipe to freshly download the November 1 release ZIP (SHA256 `33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65`), clone recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, export Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and run both helpers. Do not use only the repository's older RESTORE.md. Exact Bloodbound restoration requires the recipe's archive hash-index scan.

The resulting Theotar runtime must contain exactly 27,480 files / 1,546,230,646 bytes. Its authoritative SOURCE_MAP SHA256 is `23c1cd9b8f037c39c7b748348312f3c5e327d35a471f9ded31b4e186574d0c8e`. Keep this verified source unmodified; do not launch Godot in it before the next step.

The supporting `FRESH_FULL_CHAIN_VERIFICATION.json` documents an independently executed fresh full dependency recovery: original ZIP plus Git dependencies freshly downloaded, 70 part manifests / 103 archives scanned, all source files matched. The older helper's original receipt contains hardcoded prior-baseline wording; the supporting receipt explicitly records the fresh run instead. No helper repair was needed.

## Restore Electron independently

Place the accompanying `verify_and_restore_electron.py` in another new empty directory and run:

```sh
python3 verify_and_restore_electron.py --theotar-recovery /path/to/completed-theotar-recovery
```

The argument is the directory containing `restored_theotar_runtime` and `theotar/extracted/timewarp_theotar_rebuild_20261107/SOURCE_MAP.json`, not the runtime itself. The helper uses only Python's standard library. It downloads immutable Electron commit `a36ee10561aa7b32dd0f44c4c1e8ea32504c0314`, path `battlegrounds-backup/pending/20261107-electron-reconstruction`, manifest and 12 binary parts. Expected archive: 2,831,808 bytes, SHA256 `6baf387fe353cc5d480fd449de97353bbfec11e9651cedc4c9a788602129b976`.

It verifies all part hashes, the full archive and all 89 member hashes, rejects unsafe member paths/types, checks byte-identical Theotar SOURCE_MAP/Electron BASE_MAP, rehashes the baseline, and validates the exact delta (47 modified files plus 9 new files, no removals). It independently copies the result to `restored_electron_runtime` with no hardlinks, then rehashes the result and unchanged baseline. It does not delete backups or modify remote content. Existing destinations are not overwritten. Preserve failed attempts for diagnosis and retry in a new directory.

Require `ELECTRON_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, exactly 27,489 files / 1,546,358,376 bytes, and empty missing/mismatched/unexpected lists. Electron SOURCE_MAP SHA256 must be `8e099df06e47a901875a526a0ea21edcbf21406758f786b77078b8f00845492d`. `RESTORE_PROVENANCE.json` identifies the baseline or remote delta source for every output file.

This helper downloads Electron afresh, not the historical chain; the preceding full recipe supplies that chain. The accompanying supporting receipt records the actual independently fresh historical run. Gameplay was not run during this recovery verification. Package test records describe bounded fixtures and exclude natural acquisition, golden gameplay, automatic cast origins, copy/triple inheritance, broad spell combinations, callback-rejection rollback, UI and full lobby acceptance.
