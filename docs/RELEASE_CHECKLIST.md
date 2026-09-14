# Release checklist

- [x] Confirm that the benchmark name and public description match the paper.
- [x] Transcribe the paper title and author list into `CITATION.cff`.
- [ ] Add official proceedings, Anthology, DOI, and/or arXiv identifiers when public.
- [ ] Resolve the 57-paper-vs-56-workbook Korean item discrepancy.
- [ ] Supply owner-approved corrections for seven missing intensity cells.
- [ ] Add the official archival release and its code/data usage terms.
- [ ] Confirm whether the public repository links to or mirrors the archival data.
- [ ] Run a human privacy review of all dialogue and scenario text.
- [ ] Verify that no annotator, translator, source ID, path, credential, or raw output remains.
- [ ] Run `scripts/validate_release.py` and archive its clean report.
- [ ] Visually review every extracted image and verify image-item alignment.
- [ ] Freeze and record the released files' SHA-256 digests.
- [ ] Add paper, project page, and archival links only after they are public.
- [x] Keep manuscript PDF, XLSX sources, extracted images, and generated data out of Git until archival release.
