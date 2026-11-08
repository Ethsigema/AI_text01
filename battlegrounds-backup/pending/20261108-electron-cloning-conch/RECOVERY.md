# Recover Electron Cloning Conch source

Source-byte verification only. No gameplay acceptance or recovery of lost uncommitted work is claimed. Preserve all backups and do not launch Godot in verification baselines.

## Obtain the composed Deathrattle baseline

The preceding scheduled check verified the entire historical chain through Deathrattle from fresh remote bytes, without materializing a Deathrattle runtime. Its reproducible methods and receipts are pinned here:
https://github.com/Ethsigema/AI_text01/blob/7447a788957f620a490bf8dc89a5ec30a470b111/battlegrounds-backup/pending/20261107-electron-deathrattle-discover/RECOVERY.md

Follow that recipe for the November 1 original release ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a and all pinned increments. To obtain a materialized Recruitment runtime, follow its preceding portable recovery recipe:
https://github.com/Ethsigema/AI_text01/blob/b3e251569af5ac4ee31db577318381c9c832f226/battlegrounds-backup/pending/20261107-electron-recruitment/RECOVERY.md

Use the verified Deathrattle archive from content commit 2396666108903c8f4d84681cbf6114d6ad3a128c at battlegrounds-backup/pending/20261107-electron-deathrattle-discover. Its five parts, ordered by MANIFEST.json, assemble electron_deathrattle_discover_20261107.tar.xz, SHA256 7f9f4353665bd1b3aa09f5dd6acd5808f09e77cf32f7b52487b954ef800f7a3a. The fresh-chain verifier downloads and verifies these parts and all members. Safely extract the verified archive to obtain electron_deathrattle_discover_20261107 containing BASE_MAP.json, SOURCE_MAP.json, SOURCE_DELTA.json and delta/. Do not overwrite the Recruitment runtime.

The helper below requires the Recruitment runtime plus that extracted Deathrattle package. It verifies the entire Recruitment inventory against Deathrattle BASE_MAP, verifies every Deathrattle delta byte and its exact map differences, and rehashes all 27,701 composed Deathrattle files. Required Deathrattle SOURCE_MAP SHA256: 64db47233c38a84eae77365374b1f834172c21b5cdafd2ec6c596a38c2cd0a5f.

Supply the published Deathrattle evidence directory containing:
- DEATHRATTLE_DISCOVER_REMOTE_CHAIN_VERIFICATION.json, SHA256 0d0a749024680d5e855fcc906bc445a7469dc484a84329dd4f6ecec72ef821d1.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

## Download and restore Conch

Place verify_and_restore_cloning_conch.py in a new directory. Python 3 standard library and approximately 2 GB free disk are required once the prerequisites exist.

```sh
python3 verify_and_restore_cloning_conch.py --recruitment-runtime /path/to/restored_recruitment_runtime --deathrattle-package /path/to/electron_deathrattle_discover_20261107 --deathrattle-evidence /path/to/deathrattle-evidence
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 730a84f6e10bd6debdb3cc144ca46fa527bdbce2 at battlegrounds-backup/pending/20261108-electron-cloning-conch. Archive: 1,077,228 bytes, SHA256 20427fe9c99003c39932cf902669651703e936b6b24d99c9f0cc9bb297968f77. Every part, archive and all 56 safe members are hash-verified. Companion hashes and exact changes must match: five modified files, two additions, no removals.

The exact Deathrattle SOURCE_MAP must byte-equal Conch BASE_MAP. The helper creates restored_cloning_conch_runtime using independent copies, hashes every output, then rehashes unchanged Recruitment and Deathrattle delta sources. No hardlinks are created. Expected final inventory: 27,703 files / 1,548,057,670 bytes; source map SHA256 4af4961f1d1b1f67ab9981f92bcd202553c8a35a9f2faa9a1f69bd47627883dd. Require CLONING_CONCH_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY and empty discrepancy lists. RESTORE_PROVENANCE.json identifies each file's source.

Only this Conch increment is freshly downloaded by this helper. The prior whole-chain proof and composed historical baseline are reused explicitly, with all baseline source bytes rehashed. Existing destinations are not overwritten; preserve failed attempts and diagnose before retrying in a new directory. No deletion or remote writes occur.
