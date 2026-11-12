# Empty opponent slot compatibility: source freeze

This increment starts from the independently restored, verified Tier5 source at 3da3922e990fd2ed2637d1cc95c8a6e11322e32f, whose final receipt is fd0355f88ef67f7e05fb5eae8c7e677356624734. It does not recover missing or unuploaded files.

## Changed implementation

- Adds a stateless zero-source shape validator for the native right-side empty opponent used in odd-player rooms before any real dead-player snapshot exists.
- Waterlogged Pen and Owned Observer adapters admit only the exact original empty owner and coherent empty contexts. Negative or malformed negative owner representations trigger strict cross-checking, rather than bypassing it.
- Combat passes its original right input into Observer initialization. The initial empty internal board array is not accepted as evidence that the original input was empty.
- Both ghost flags must be explicit false. Owner is an integer -1; board, hand, trinket sources and resource entries must be empty; native positive owner paths retain their existing validation.
- Adds the helper to both runtime dependency lists and propagates inherited source hashes from known Tier5 preimages. Changed hash declarations do not represent newly implemented card abilities.

No Game, card data, random selection, pool, UID factory, damage, or acquisition logic is replaced. No new hero or unrelated mechanism is introduced. Naga remain included; the scope exclusion of Aberrations is unchanged. Detached identical shapes are intentionally not represented as private Game-issued authority.

## Stage and limits

This is the early unaccepted source snapshot, saved before a long complete-Game run. Its pure contract and static review are not native gameplay acceptance. Planned native regression is three-, five-, and seven-player initial empty slots plus a four-player control, with existing Darkcrest acquisition and end-of-turn level 1 to 2. The six-output Tier5 matrix is not repeated. Natural elimination/dead-owner snapshots, active trinket abilities, mixed boards, all latest content, UI, default pool, and complete matches remain outside this tranche's acceptance.

Apply this cumulative delta only to the fixed batch14 base identified by MANIFEST.json. Keep all previous backups. Restore and hash every target file before long tests; publish later test receipts without altering the frozen source archive or map.
