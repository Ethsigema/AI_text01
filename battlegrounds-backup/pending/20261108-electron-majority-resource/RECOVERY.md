# Recover Electron Majority Resource source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Locked Discover recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/d46400728900b29681ce989cf164eb2edb63d7be/battlegrounds-backup/pending/20261108-electron-locked-discover/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Locked Discover. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Locked Discover recovery directory must contain restored_locked_discover_runtime and locked_discover/extracted/electron_locked_discover_20261108/SOURCE_MAP.json. Require exactly 27,707 files / 1,548,068,875 bytes; map SHA256 c18e95627f7b1d7c754829f58a5364f77069c1e458c43eddde2b7251b9674297.

Place these published receipts in that directory:
- LOCKED_DISCOVER_REMOTE_CHAIN_VERIFICATION.json, SHA256 095d8d9362120476725185317b1dd30a8ad9f4bf8fe62e299edae32aad1b25c6.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Locked Discover source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_majority_resource.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_majority_resource.py --locked-discover-recovery /path/to/completed-locked-discover-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit fd7fa142148d3ffe42e5cab300aed699baa73207, path battlegrounds-backup/pending/20261108-electron-majority-resource. Archive electron_majority_resource_20261108.tar.xz: 1,075,500 bytes, SHA256 13909ad876ae7b1ee213aabdfbec6d204bf2af49cefd15f3b320a32e6c163bcf.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Locked Discover SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_majority_resource_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require MAJORITY_RESOURCE_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,709 files / 1,548,074,145 bytes, no missing/mismatched/unexpected files, and target map SHA256 cb3b14d327715c5654d9fedc6b3e97b1fb7b3759946d338909631d0a701fb2ac. Per-file origins are in RESTORE_PROVENANCE.json.

Only Majority Resource is freshly downloaded this round; historical source evidence and Locked Discover baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.
