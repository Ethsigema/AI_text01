# Restore the November 7 reconstructed Theotar source

This is **new reconstruction**, not recovery of the lost November 6 Theotar checkpoint. Preserve all historical backups. The increment alone is not a complete game: it requires the exact Bloodbound baseline plus the Wrathguard increment.

## Verified scope

The accompanying receipt distinguishes the two freshly downloaded GitHub increments from the previously restored historical baseline. All baseline source bytes were rehashed, both dependency maps matched, and an independent new runtime was reconstructed and checked. This is source-byte recovery verification, not gameplay acceptance, full card implementation, UI verification or natural acquisition validation. The historical baseline was not freshly downloaded again during this increment check.

## Obtain the complete historical baseline

Use a new empty work directory with Python 3, Git, curl and tar. Allow several GB for retained archives and source. Put the accompanying `restore_bloodbound_from_archives.py` and `verify_and_restore_latest.py` in that directory. These scripts use relative directories and never need the original assistant workspace.

The published original ZIP is:
https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip

Its required SHA256 is `33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65`.

```sh
mkdir baseline_download
curl --fail --location 'https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip' -o baseline_download/battlegrounds_new_scope_handoff_20261101.zip

git clone --branch battlegrounds-recovery-20261103 https://github.com/Ethsigema/AI_text01.git repository
git -C repository checkout --detach e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c
git -C repository fetch origin 32180d3af0db59fb3374f53100f9eaa5bb62d26a
mkdir bloodbound
git -C repository archive 32180d3af0db59fb3374f53100f9eaa5bb62d26a | tar -x -C bloodbound
python3 restore_bloodbound_from_archives.py
```

The baseline helper verifies ZIP SHA256 and the pinned recovery checkout, assembles split/base64 archive parts using their manifest size/hash records, recursively scans source-containing archives, and reconstructs only bytes matching the authoritative Bloodbound SOURCE_MAP. This is a content-index reconstruction, not a sequence of speculative overlays. It does not need every old intermediate runtime. It retains assembled archives, source provenance and verification records.

Require `RESTORE_RESULT.json` to report 27,463 expected/found files, empty missing/mismatch/archive_errors lists, and SOURCE_MAP SHA256 `9a517b7c2e0ba0c14308248884696b008e5a6f0b500a1d1d97bcd53c4b7a9c71`. Do not proceed on an assertion, download failure or incomplete result. The earlier repository RESTORE.md describes older snapshots and is supplemental; it does not by itself reconstruct this exact Bloodbound target.

## Download and restore the increments

From the same directory, run:

```sh
python3 verify_and_restore_latest.py
```

It downloads immutable inputs:

- Wrathguard commit `cf0a57917c570773382f8bcad5e33f86d141846f`, directory `battlegrounds-backup/pending/20261107-wrathguard-new-reconstruction`, 6 binary parts, 42 archived files. Archive SHA256: `9e96a7b8f3a182975bd1237a4e68259568a38530be3738478883f3b8d5943432`.
- Theotar commit `8a746239fec90cbc37983da1e2c4e271a1b05bbc`, directory `battlegrounds-backup/pending/20261107-theotar-reconstruction`, 12 binary parts, 103 archived files. Archive SHA256: `ac02652611912136525b97bc1d309c4a0d4193c972933dedef572ac39ab16800`.

The helper validates every part, complete archive, regular member, size and SHA256 before safely extracting. It checks Bloodbound SOURCE_MAP equals Wrathguard BASE_MAP and Wrathguard SOURCE_MAP equals Theotar BASE_MAP. Manifest-listed baseline files must match exactly. Only generated `.godot/*` and `*.gd.uid` extras may be ignored; they are recorded and not copied. No manifest-listed file is exempted.

It independently copies into the new `restored_theotar_runtime` directory using Theotar delta, then Wrathguard delta, then baseline precedence. It does not hardlink the output to either baseline or delta. The final runtime must contain exactly 27,480 files and 1,546,230,646 bytes, with no missing, mismatched or extra files. Theotar SOURCE_MAP SHA256 must be `23c1cd9b8f037c39c7b748348312f3c5e327d35a471f9ded31b4e186574d0c8e`; Wrathguard SOURCE_MAP SHA256 is `e16ce2b99917f46f9492c0ad14f36060e0d90d19b76ae702fd13ebb9a51bfcd9`.

Require successful `REMOTE_CHAIN_VERIFICATION.json`. Existing destination directories are not overwritten. Keep a failed partial attempt for diagnosis and use another fresh work directory when rerunning; do not delete any historical backups to make a retry work.

## Opening the source

Only after byte verification, open `restored_theotar_runtime/project.godot` in Godot 4.6.3, or import using its headless editor with writable task-local HOME/XDG directories. Import generates caches/UIDs, so keep the verification receipt and original maps. Import success is not gameplay acceptance. Consult the extracted Theotar README, VALIDATION.json and all run records for bounded behavior, acquisition/fixture limits, untested golden gameplay and the first-command-play issue.

The portable helpers were syntax-checked. The increment verification/restoration logic was executed successfully in the verification environment with its already-verified baseline. The portable historical-baseline wrapper was prepared from the prior successful recovery script; its fresh-directory download recipe was not independently executed again during this increment check.
