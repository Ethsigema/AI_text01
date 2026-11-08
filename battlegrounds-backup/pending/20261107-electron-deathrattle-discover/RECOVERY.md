# Fresh complete-chain verification through Deathrattle Discover

This method freshly obtains every source archive dependency rather than relying on historical verification receipts. It verifies complete source-byte recoverability by hash-index composition without writing a full runtime directory. It does not execute gameplay or recover lost uncommitted work.

Copy RUN_FRESH_CHAIN.sh, verify_historical_bytes.py, verify_fresh_increment_chain.py and PINNED_INCREMENT_CHAIN.json into a new empty directory, then run:

```sh
sh RUN_FRESH_CHAIN.sh
```

Requirements: Python 3 standard library, Git, curl, tar, network access to GitHub and release assets, approximately 2.5 GB free disk and enough memory for archive decoding. Existing destinations are not overwritten. Preserve any failed attempt and diagnose before retrying; no deletion is performed.

The shell script freshly downloads the original November 1 release ZIP (SHA256 33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65), clones/fetches recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c and Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and checks Git objects with git fsck. The clone is shallow: the complete pinned trees and their source blobs are obtained, not unrelated commit history.

The historical helper verifies archive part sizes and hashes, assembled archives, nested archives and exact source-byte hashes for all 27,463 Bloodbound files against its authoritative SOURCE_MAP (SHA256 9a517b7c2e0ba0c14308248884696b008e5a6f0b500a1d1d97bcd53c4b7a9c71). It records per-file archive origins in PROVENANCE.json and all scanned archives in ARCHIVE_SCANS.json. RESTORE_RESULT.json must have no missing files, mismatches or archive errors.

The increment helper then freshly downloads MANIFEST.json and every binary part for all 61 pinned increments listed in PINNED_INCREMENT_CHAIN.json. It verifies all part, archive and member sizes/hashes and safe member paths. Every BASE_MAP must exactly match the preceding source map; every changed source member must match the exact map difference. CHANGES.json and REMOVALS.json, where supplied, are freshly downloaded, hash-bound to the manifest and compared to actual differences. No removals are allowed in this chain.

The last increment is pinned to commit 2396666108903c8f4d84681cbf6114d6ad3a128c at battlegrounds-backup/pending/20261107-electron-deathrattle-discover. Archive SHA256: 7f9f4353665bd1b3aa09f5dd6acd5808f09e77cf32f7b52487b954ef800f7a3a. Expected final source: 27,701 files / 1,548,052,627 bytes; SOURCE_MAP SHA256 64db47233c38a84eae77365374b1f834172c21b5cdafd2ec6c596a38c2cd0a5f.

Success requires FRESH_WHOLE_CHAIN_VERIFICATION.json status PASS_FRESH_FULL_CHAIN_SOURCE_BYTES and the exact final counts/map. All unchanged files inherit provenance from freshly verified source bytes, and all changed files are verified from fresh archive member bytes. This is complete byte composition, not a second materialized runtime. No existing runtime, baseline, hardlink or backup is modified.

To materialize a runtime, follow the existing pinned recovery helpers in chronological order. This fresh verification does not itself create that directory or establish gameplay acceptance.

## Completed run and safe resumption

This run completed after an interrupted HTTP request following Forest Choice (42 increments). The original INCREMENTS.log is preserved. resume_fresh_increment_chain.py rereads and rehashes only downloads already created by this same run, downloads missing files, and repeats every map/member check. It must only be used in the same fresh run directory, never to label older cached archives as fresh. Run `python3 resume_fresh_increment_chain.py` after diagnosing an interruption. RESUME.log records the successful completion. The original historical verification did not need rerunning because its freshly downloaded source evidence remained intact.

The final full-chain receipt SHA256 is 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7. The dedicated DEATHRATTLE_DISCOVER_REMOTE_CHAIN_VERIFICATION.json summarizes exact counts, interruption/resumption, and no-runtime-directory limitation. Both helpers were executed successfully. The full source-byte composition passed; gameplay was not run.
