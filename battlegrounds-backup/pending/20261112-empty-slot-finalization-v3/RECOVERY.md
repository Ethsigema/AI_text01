# Unaccepted empty-slot compatibility snapshot

Status: UNACCEPTED_EMPTY_SLOT_V3_BEFORE_GAME

Use original Release + fixed batch14 consolidated baseline from 5143e8fb41bc8332ce4ba196144172167a74318c. All earlier backups retained. Apply this cumulative increment directly to batch14, not v2.

`python restore_increment.py --base-tree /fresh/batch14 --base-map /baseline/SOURCE_MAP.json.gz --destination /new/tree --report /new/report.json`

Check SHA256SUMS.txt first. Full expected file map is SOURCE_MAP.json.gz; expected aggregate is in MANIFEST.json. This snapshot is not gameplay acceptance and covers no new content mechanism or full trinket class. Prior v2 results do not validate this changed source.
