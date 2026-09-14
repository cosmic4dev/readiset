# Source consistency audit

Audit date: 2026-09-14

The final 16-page paper and both author-provided release workbooks were reviewed.

| Check | KRISA | ENGISA |
|---|---:|---:|
| Non-empty item rows | 56 | 45 |
| Embedded image files | 56 | 45 |
| Images mapped one-to-one to item rows | 56 | 45 |
| Four parseable choices per item | 56 | 45 |
| Gold answers in range 1-4 | 56 | 45 |

Images are stored as PNG or JPEG objects inside the workbooks. No existing item
row has a missing embedded image.

## Blocking discrepancies

1. The paper reports 57 Korean items, while the KRISA workbook contains 56 rows
   and 56 images.
2. Two KRISA intensity cells are blank.
3. Five ENGISA intensity cells are blank.
4. KRISA intensity notation mixes integers with strings such as `2단계`; these
   strings are safely normalizable, while blank values are not.

The English total of 45 matches the paper. Although aggregate paper results imply
complete level labels, missing labels must not be reconstructed from row order or
result tables.

## Required owner action

- provide the missing Korean item or confirm that the paper count should be 56;
- supply the seven missing intensity annotations in an approved correction file;
- confirm that all 101 supplied images are the final release assets;
- approve redistribution terms and code/data licenses.

Until then, the builder fails closed and generated data must not be published.

