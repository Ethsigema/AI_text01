# Batch 13: bounded Bolvar source-reader correction

## Result and version

This package preserves a clearly **new correction**, not a historical original or a claim to the latest upstream version. The final candidate is `review/revision3/tools/native_bolvar_shield_patterns.py`, SHA-256 `f4a4a9972d00a7bdbf64f0cf10c97d82bce0879bd86515db5b37adbee3154de3` (17,277 bytes).

The independent final development tree adds only this file to the exact batch-12 candidate backed up at commit `1e2ede27d0312440996e2c7c9e88ebdd033ee195`. No prior baseline or backup is overwritten. The 367-path reference inventory has 347 still-unfilled paths in this candidate, compared with 348 in the unchanged batch-12 tree. This is one new corrected tool, zero unchanged historical originals restored. It is not a count of every missing project dependency.

## What changed

The historical original is preserved byte-for-byte. The prior numeric-only proposal is also preserved. Its comparator follows the already captured current Godot int64/float64 behavior, including equal integral floats and rejection of bool/number aliases and out-of-int64 Python integers. This intentional numeric correction is not misrepresented as unchanged historical behavior.

Relative to that numeric-only proposal, the final revision changes only the raw-catalog assignment in `verify_sources` and adds three reader helpers. Imports, constants, all 19 evidence pins, complete output payloads, other source reads, source/admitted IDs, the comparator, and `compile_card` remain unchanged. The original complete overrides and canonical-minions readers are retained.

The reader validates the entire stable, regular text file's decoding in bounded chunks, rewinds the same open stream, and frames the root object and cards array. Every value, including ignored values, is decoded by the standard Python JSON decoder. Temporary original-depth object/array wrappers preserve the decoder's structural recursion boundary. Duplicate keys and selected IDs remain last-value-wins; malformed row shapes are deferred correctly across overwritten root `cards` keys. Invalid ignored content and trailing data are not skipped.

## Preserved failures and revisions

- Historical original `68c4b12f…d4a4c`: the earlier original full-current-source probe hit the 128 MiB address-space limit. No raised-limit retry is claimed.
- A new whitespace-only compact representation of all current raw data also hit the same limit once. Its transform and failed receipt are retained. It is not a successful whole-source old/new oracle.
- Initial streaming proposal `27cc2bdf…29f49`: omitted structural context and accepted a deep payload that the old verifier rejected with `RecursionError`. It is not installed in the final tree.
- Revision 2 `a8424a56…83390`: restored recursion depth but could propagate an early `RecursionError` when the old whole-file reader first encountered later invalid UTF-8 and `compile_card` returned `None`. The concrete combined-failure evidence and intermediate development tree are retained. Its earlier passing reports are not final acceptance.
- Revision 3 `f4a4a997…54de3`: preserves both the original structural depth and full-text-decoding-first priority. No remaining mismatch was found within the tested scope.

## Verification

All executable checks use normal Python with assertions enabled and a 134,217,728-byte address-space limit. No new dependency, Godot run, full compiler driver, Game, Catalog startup, or save workflow is run in this batch.

- 947 independent ordinary syntax/selection/type/duplicate/chunk differential cases.
- 5,000 additional deterministic independent differential checks over 1,250 fixtures.
- 594 implementation differential checks and 12 numeric cases, repeated after portable copying.
- Original deep-array boundaries restored, with actual historical/proposal/new verifier contexts checked.
- 23 independent mixed-invalid fixtures, comparing actual verifier plus normal and golden compiler calls: 69 matched outcomes/error classes.
- Nine additional portable error-priority fixtures preserve the V2 counterexample and verify V3 behavior.
- 49 current-proof/dependency negative cases compare the prior numeric proposal and final revision, totaling 98 tool calls. They cover every one of the 19 pins, missing/nonregular proof paths, raw duplicates, missing selected records, malformed ignored data, the golden override, and canonical rows.
- Eight complete-current-source compiler cases per run, repeated on the independent tree, the self-contained portable source copy, and the complete replay entry point (32 total compile calls). Complete 30,883,879-byte raw, 57,466-byte overrides, and 7,291,137-byte minions inputs are used. Exact outputs, source hashes and input nonmutation are checked; normal output remains partial and golden output remains held.
- All 25 included source inputs match their byte maps. Current GD original/effective/expected constants and proof pins match statically. The previous typed numeric oracle is retained as prior evidence, not called a fresh Godot run.
- Full candidate and unchanged batch-12 trees are hashed, with a one-file delta and no hardlinks.

`TESTS_VERIFIED.json`, `ACTUAL_TREES_VERIFIED.json`, and the included detailed reports contain measured results. `FILE_MANIFEST.json` covers the sealed package.

## Reproduce safely

- `python3 -B verify_candidate.py` performs bounded static package verification.
- `python3 -B replay_to_new.py /new/nonexistent/directory` copies only the explicit portable test inputs and runs the final small and full-source checks sequentially. It does not create or execute a full game tree.
- `python3 -B restore_to_new.py /exact/batch12/runtime /new/nonexistent/runtime` reconstructs the complete candidate using the exact base map and one delta. It never overwrites either tree. This utility is provided; the actual independent-copy/install/full-rehash receipts document the operations performed here.

Do not use `-O` or `PYTHONOPTIMIZE`. Run only on the tested CPython 3.12.14 setup unless the interpreter and boundary behavior are validated again.

## Limits and work still open

The evidence establishes a bounded current-source candidate, not a universal theorem for every input, interpreter or process state. Error message text, offsets and tracebacks are not identical. Input must remain a stable, seekable regular file across preflight and parse; this is not an atomic snapshot against concurrent mutation. Memory depends on the largest individual framed value and unchanged secondary-source parsing, not only the chunk size. Arbitrarily huge single records or ignored values are not guaranteed to fit 128 MiB.

No successful historical-original execution on the full current raw file is claimed. The comparison rests on preserved decoder/projection structure, differential and actual-entry fixtures, exact current selected proof rows, unchanged other-source checks, and unchanged complete outputs.

Golden unresolved-tribe hold, Attack-only/no-rescue, partial implementation, and non-default-pool restrictions are unchanged. No exact historical client trigger order, full/default-pool admission, full compiler integration, full Game/Catalog/driver behavior, or old-save compatibility is accepted. Adding a tool can change fingerprints; old-save behavior remains untested. Other missing tools and previous deferred differences remain open.

The archive uses an explicit whitelist. Runtime trees, font/editor/rebuildable caches, `.godot`, `__pycache__`, private conversations, credentials and unrelated files are excluded. Historical originals, rejected revisions, intermediate receipts, and all prior backups remain preserved.
