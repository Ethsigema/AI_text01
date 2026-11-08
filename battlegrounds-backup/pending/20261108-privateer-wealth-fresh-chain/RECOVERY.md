# Fresh complete-chain verification through Privateer Wealth

This method freshly obtains every source archive dependency rather than relying on historical verification receipts. It verifies complete source-byte recoverability by hash-index composition without writing a full runtime directory. It does not execute gameplay or recover lost uncommitted work.

Copy RUN_FRESH_CHAIN.sh, verify_historical_bytes.py, verify_fresh_increment_chain.py and PINNED_INCREMENT_CHAIN.json into a new empty directory, then run:

```sh
sh RUN_FRESH_CHAIN.sh
```

Requirements: Python 3 standard library, Git, curl, tar, network access to GitHub and release assets, approximately 3 GB free disk and enough memory for archive decoding. Existing destinations are not overwritten. Preserve any failed attempt and diagnose before retrying; no deletion is performed.

The shell script freshly downloads the original November 1 release ZIP (SHA256 33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65), clones/fetches recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c and Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and checks Git objects with git fsck. The clone is shallow: the complete pinned trees and their source blobs are obtained, not unrelated commit history.

The historical helper verifies archive part sizes and hashes, assembled archives, nested archives and exact source-byte hashes for all 27,463 Bloodbound files against its authoritative SOURCE_MAP (SHA256 9a517b7c2e0ba0c14308248884696b008e5a6f0b500a1d1d97bcd53c4b7a9c71). It records per-file archive origins in PROVENANCE.json and all scanned archives in ARCHIVE_SCANS.json. RESTORE_RESULT.json must have no missing files, mismatches or archive errors.

The increment helper then freshly downloads MANIFEST.json and every binary part for all 79 pinned increments listed in PINNED_INCREMENT_CHAIN.json. It verifies all part, archive and member sizes/hashes and safe member paths. Every BASE_MAP must exactly match the preceding source map; every changed source member must match the exact map difference. CHANGES.json and REMOVALS.json, where supplied, are freshly downloaded, hash-bound to the manifest and compared to actual differences. No removals are allowed in this chain.

The last increment is pinned to commit b3a129736c61e94023099ca5a630bee859d4c918 at battlegrounds-backup/pending/20261108-electron-privateer-wealth. Archive SHA256: 2dda901ab44b7c98be52fbad2921012409b87bd2feb58aac4e7dc2cb4ba459f4. Expected final source: 27,739 files / 1,548,173,496 bytes; SOURCE_MAP SHA256 170be091073bebc2381da4f748262098c1093008f5f35f9ae97971f557817c5b.

Success requires FRESH_WHOLE_CHAIN_VERIFICATION.json status PASS_FRESH_FULL_CHAIN_SOURCE_BYTES and the exact final counts/map. All unchanged files inherit provenance from freshly verified source bytes, and all changed files are verified from fresh archive member bytes. This is complete byte composition, not a second materialized runtime. No existing runtime, baseline, hardlink or backup is modified.

To materialize a runtime, follow the existing pinned recovery helpers in chronological order. This fresh verification does not itself create that directory or establish gameplay acceptance.

Chef Magnetic contains two redundant unchanged research files in its delta. Both are freshly member-hashed and verified equal to baseline and target: research/electron_chef_choice/evidence.json and research/electron_chef_choice/BG28_518.native.xml. Every other packaged delta equals the actual map difference.

This scheduled check targets the source content referenced by Privateer Wealth final documentation commit 1a8c1381a5b94ee1b82b198bc8f21bb8bfbd6c04. It freshly obtains the pinned content dependencies, not merely the historical receipts.
