# Curation decisions

## Corrected benchmark identity

An earlier draft treated older dialogue workbooks as a text-only target-localization
benchmark. The final paper and supplied release workbooks establish that READI is
a multimodal four-choice V-PQA benchmark with 102 reported items. The earlier
generated dialogue draft has been moved out of the release path and ignored.

## Frozen release rules

- KRISA and ENGISA remain independent subsets.
- Every item requires one image, question, utterance, four choices, gold answer,
  and indirectness level.
- Source row IDs are replaced with stable release IDs.
- English literature provenance may remain as `source_reference`.
- Missing labels are never inferred from ordering, neighbors, aggregates, or names.
- The builder stops on count, label, image, answer, or parsing inconsistencies.
- Raw XLSX, manuscript PDF, local paths, model outputs, and credentials are not
  part of the generated dataset.

Dataset-owner approval and visual privacy review remain mandatory.

## Publication policy

The repository code and documentation are prepared for public visibility. Source
workbooks, the manuscript PDF, extracted images, and normalized benchmark records
remain private until the official archive resolves the source discrepancies and
publishes authoritative usage terms. Informal request-by-request distribution is
not used as a substitute for a documented archival release.

Repository citation metadata is intentionally deferred until the official
archival citation is publicly available.
