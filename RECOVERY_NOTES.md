# Recovery identity correction — 16 November 2026

The legacy fingerprint uses path, byte size and filesystem mtime_ns. All three task fingerprints changed in the attempted Version 3 continuation. Direct comparison of downloaded V2/V3 output archives found only dataset_fingerprints.json, dataset_inventory.json and session state changed; checkpoints, splits, repairs and geometry audit were identical. This supports volatile metadata as the explanation; it does not prove which original stat fields changed, and no original per-file stat snapshot exists to attribute every individual metadata change.

Kaggle V2 Input UI identifies BraTS parts 1/2 as v1/v1, LiTS parts 1/2 as v5/v2 and ACDC as v2. These exact numbered source versions were explicitly selected in the editor before saving Version 4. Immutable dataset version identity is the historical content assurance for unrepaired source volumes; V2 did not save their full SHA-256 hashes. This trust boundary is explicit, not a claim that historical source bytes were rehashed.

The corrected code hashes all current source/repair files in bounded chunks and saves content_provenance.json. Every future session recomputes those hashes and compares them to the prior manifest. Paths inside known source roots are canonicalized so mount relocation and timestamps do not alter content identity.

The one-time legacy migration requires the exact 41 published V2 artifacts anchored in recovery_baseline_v2.json, byte-identical current repair files/splits/pairing audit, identical full preparation configuration and pipeline revision, and the externally verified immutable dataset version pins. Cached indices are copied under new content-derived names, and an explicit migration receipt plus the untouched original prepared marker are saved. Checkpoint bytes are never rewritten. The existing configuration, model layout, task, experiment, seed and numerical-state guards remain active; only the two exact SHA-256-identified V2 checkpoints may use the documented legacy identity alias.

Do not reuse this migration for other saved versions or changed source snapshots. If any evidence differs, execution stops before indexing/training. A failed live audit must not trigger repeated relaunches.

Local validation: timestamp/mount invariance, changed-content rejection, corrupted-artifact rejection, out-of-root rejection, and a synthetic full migration preserving checkpoint bytes and rejecting unauthorized aliases; generated cells parse; all Config values exactly match V2. Live Kaggle audit and resumed validation still require verification.

## Live verification in progress

Version 4 (`370110745`), “V2 recovery with verified content provenance”, is running on GPU T4 x2 with exactly one prior notebook output. At 63.4 seconds it verified the exact 41-artifact V2 set before source hashing. At 148.4 seconds the integrity audit passed for 1,582 records and 5,335 image-mask pairs. At 237.5 seconds the full content audit reached 400/6,917 files (5.8%). The audit, migration receipt, cached index reuse and original checkpoint acceptance must all be verified before claiming training resumed. V2 remains the trusted recovery source until a compatible successor publishes its saved output.
