# Fresh whole-chain source-byte verification

The current verification separately downloads the original release ZIP and a new Git repository, pins recovery e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c and Bloodbound32180d3af0db59fb3374f53100f9eaa5bb62d26a, checks Git object integrity, verifies 70 archive-part manifests and scans 103 archives. It hashes source bytes against the exact Bloodbound map without writing a historical runtime.

Each subsequent increment through Murky is independently downloaded from its pinned commit, with all part/archive/member hashes checked and exact dependency map continuity established. REMOVALS/CHANGES companions are checked where supplied. All changed source bytes come from these fresh archives. Unchanged source bytes retain their earlier verified provenance. The final complete content map is therefore composed from freshly verified bytes, not from prior receipts or local runtime assumptions.

The current run reuses Murky bytes freshly downloaded earlier in this same verification task, avoiding a duplicate download. It does not reuse earlier historical or increment archive bytes. Separately, an independent Murky runtime was built using the previously verified Painter baseline and freshly downloaded Murky delta, then every output and baseline byte was rehashed. That independent runtime is not claimed to have been written from the newly downloaded historical chain.

No second full runtime is written during the fresh whole-chain check. This is a complete source-byte composition proof, not gameplay testing. No data is deleted or remote state changed.

## Reproduce in a fresh directory

Place RUN_FRESH_CHAIN.sh, verify_historical_bytes.py, verify_fresh_increment_chain.py and PINNED_INCREMENT_CHAIN.json together in an empty directory, then run `sh RUN_FRESH_CHAIN.sh`. Requirements: Python 3, Git, curl, tar, network access and several GB for retained evidence. The portable helper downloads Murky itself as well; it has no dependency on private workspace paths or prior runtime directories.

The current run uses verify_increment_chain.py with same-check Murky reuse; the published portable variant verify_fresh_increment_chain.py embeds no local workspace assumptions and uses the accompanying pinned coordinates. Verification logic is identical apart from download sourcing. Existing evidence and output files are not overwritten; preserve any partial run and use a new directory for a clean rerun.
