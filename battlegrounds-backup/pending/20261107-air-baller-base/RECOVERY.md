# Recover Air Baller base source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve all backups and shared hardlinks. The exact verified Temperature Shift baseline is required.

## Restore the prerequisite chain

Follow the immutable Temperature Shift recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/2933d223e2b6144cd68a65e5208574967d332f39/battlegrounds-backup/pending/20261107-temperature-shift/RECOVERY.md

Follow its prerequisite links through Snow, Fire, dynamic spells and all earlier increments to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and enough space for retained archives and independent runtimes.

The completed Temperature recovery directory must contain `restored_temperature_runtime` and `temperature/extracted/temperature_shift_20261107/SOURCE_MAP.json`. Require 27,586 files / 1,547,065,227 bytes and SOURCE_MAP SHA256 `c7e94e89019ab848f268c4b9cfa2bedebb747d50342b542b0cf8d0a3546b9215`. Do not modify the baseline or launch Godot in it before verification.

Supporting receipts: `TEMPERATURE_REMOTE_CHAIN_VERIFICATION.json` SHA256 `39b4d8d6d3718e2916a194e3d56f2f3e5cedfe61bf1ece78d92afe49b204dbb1`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter documents independently fresh historical recovery through Theotar; later pinned recipes and receipts connect that baseline through Temperature Shift. Receipts do not replace source bytes.

## Download and restore Air Baller

Place `verify_and_restore_air.py` in another new empty directory:

```sh
python3 verify_and_restore_air.py --temperature-recovery /path/to/completed-temperature-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 12 binary parts, REMOVALS.json and CHANGES.json from immutable commit `eed64e34b6aba9b3b650a71cda34a41d49cb70f7`, directory `battlegrounds-backup/pending/20261107-air-baller-base`. Archive: 2,809,236 bytes, SHA256 `7c4f8dcb961f49ef05eb9c8c0e0bf3f3ec91bbf441b723321f7591029840444a`.

Every part, assembled archive and all 104 members are verified, rejecting unsafe paths/types. Both companions are hash/size checked against MANIFEST.json companion_files; their arrays must equal actual differences: 9 additions, 65 modifications, no removals. REMOVALS.json must also match manifest removed_source_files. Temperature SOURCE_MAP must byte-equal Air BASE_MAP; every baseline file is rehashed.

The helper independently copies `restored_air_runtime` without hardlinks and never writes baseline files. It rehashes every output and the unchanged baseline, recording per-file RESTORE_PROVENANCE.json. Require `AIR_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,595 files / 1,547,161,659 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `3d326b2610fae0996fb5ae339abe8a04559fefcdba0356009313c8020854c46b`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. This helper freshly downloads Air only and rehashes the already-verified Temperature baseline; it does not redownload the historical chain. Use prerequisite recipes to download that chain anew. No gameplay is executed or accepted by source verification.
