# Recover Electron Choose Discover source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Majority Resource recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/4f49c504f48eeac6b7c59dde6866b28d18b72917/battlegrounds-backup/pending/20261108-electron-majority-resource/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Majority Resource. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Majority Resource recovery directory must contain restored_majority_resource_runtime and majority_resource/extracted/electron_majority_resource_20261108/SOURCE_MAP.json. Require exactly 27,709 files / 1,548,074,145 bytes; map SHA256 cb3b14d327715c5654d9fedc6b3e97b1fb7b3759946d338909631d0a701fb2ac.

Place these published receipts in that directory:
- MAJORITY_RESOURCE_REMOTE_CHAIN_VERIFICATION.json, SHA256 1a376d074f9c7c9d3fdfa10df573e38ad88b4e49a98119ab43323af77228df78.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Majority Resource source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_choose_discover.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_choose_discover.py --majority-resource-recovery /path/to/completed-majority-resource-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit d199425ff60960d3da30c47d13e8ac6dae971a8a, path battlegrounds-backup/pending/20261108-electron-choose-discover. Archive electron_choose_discover_20261108.tar.xz: 1,083,080 bytes, SHA256 b4cda8f85bfc6f2f2ab0c034a8e10e0c5456af659ab3970f6ca26e6d8d214ed1.

Every part, assembled archive and all 48 safe members are verified. Companion hashes and exact map differences must match five modifications, four additions and no removals. Majority Resource SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_choose_discover_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require CHOOSE_DISCOVER_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,713 files / 1,548,087,620 bytes, no missing/mismatched/unexpected files, and target map SHA256 3d185d5cfdc669d2400d683609b64237749e8eac4612741f36b6d23120e62dc0. Per-file origins are in RESTORE_PROVENANCE.json.

Only Choose Discover is freshly downloaded this round; historical source evidence and Majority Resource baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.
