# Package retention correction

The initial V2 tar with SHA db9a67c511460b5d84e280e198290f309635c4f9b1a4ac978ec2ef1f3e0cc798 was overwritten when correcting the explanatory note. No independent copy of its original bytes was retained by this worker. It must not be described as preserved or byte-for-byte recovered; no reconstruction has been attempted or labeled original.

The corrected final V2 tar SHA f8f9157be7bbe5458029e9811fc802e9eceb88fd1b01d666085a02f883a06490 is present and verified. V1 artifacts and V2 production hashes remain unchanged. The initial V2 statement about an established V1 source-custody vulnerability was incorrect: actual source610cad0 already validated Mini.board_error in consumed_sale_error. V2 adds redundant caller-local validation only.

V2 full diff was independently applied using patch --fuzz=0 to only two temporary files copied from actual immutable610 preimages, after SHA verification. Both outputs exactly match frozen overlay bytes. See V2_ACTUAL_PREIMAGE_DIFF_REBUILD.json. No Game run and no source edits.
