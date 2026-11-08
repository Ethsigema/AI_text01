# Recover Electron Privateer Wealth source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Sludge Discard recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/a813d1b0ac6d9213af5fb907bbabad44d3999438/battlegrounds-backup/pending/20261108-electron-sludge-discard/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Sludge Discard. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Sludge Discard recovery directory must contain restored_sludge_discard_runtime and sludge_discard/extracted/electron_sludge_discard_20261108/SOURCE_MAP.json. Require exactly 27,735 files / 1,548,160,788 bytes; map SHA256 10779ba8aa53ccf512d9ef0fad64be922ed0b1a0b85b4da0205389088dfe6cbb.

Place these published receipts in that directory:
- SLUDGE_DISCARD_REMOTE_CHAIN_VERIFICATION.json, SHA256 47c33c11c77c1a9fafedde5777fd1609ecbfcee8c136a1977d7ad2c39999573b.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Sludge Discard source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_privateer_wealth.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_privateer_wealth.py --sludge-discard-recovery /path/to/completed-sludge-discard-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit b3a129736c61e94023099ca5a630bee859d4c918, path battlegrounds-backup/pending/20261108-electron-privateer-wealth. Archive electron_privateer_wealth_20261108.tar.xz: 1,088,608 bytes, SHA256 2dda901ab44b7c98be52fbad2921012409b87bd2feb58aac4e7dc2cb4ba459f4.

Every part, assembled archive and all 39 safe members are verified. Companion hashes and exact map differences must match six modifications, four additions and no removals. Sludge Discard SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_privateer_wealth_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require PRIVATEER_WEALTH_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,739 files / 1,548,173,496 bytes, no missing/mismatched/unexpected files, and target map SHA256 170be091073bebc2381da4f748262098c1093008f5f35f9ae97971f557817c5b. Per-file origins are in RESTORE_PROVENANCE.json.

Only Privateer Wealth is freshly downloaded this round; historical source evidence and Sludge Discard baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The ten delta files are exactly six modifications and four additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.
