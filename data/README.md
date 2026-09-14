# Data release status

The final release is expected to contain `readi.jsonl`, one image per item under
`images/`, and a `manifest.json` with counts and SHA-256 digests.

The supplied XLSX files are private source artifacts and must not be committed as
the public dataset. The converter extracts embedded images and normalized
annotations only after an owner-approved correction file resolves documented
source inconsistencies.

Generated data remains ignored by Git until the source discrepancies are resolved
and the official archival release, including its usage terms, is finalized. At
that point the public repository may link to or mirror the official data release.
Until then, data access is private rather than handled through an informal
request-by-request distribution process.
