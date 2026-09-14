# READI: Read the Room, Read the Image

[![ACL Anthology](https://img.shields.io/badge/Findings%20of%20ACL-2026-1f6feb)](https://aclanthology.org/2026.findings-acl.1556/)
[![arXiv](https://img.shields.io/badge/arXiv-2608.30270-b31b1b)](https://arxiv.org/abs/2608.30270)

This is the official companion-code repository for READI, a bilingual multimodal
benchmark for evaluating whether vision-language models can infer the intended
function of indirect directive speech acts from an utterance and its visual
sociopragmatic context.

| Resource | Status |
|---|---|
| Paper | [ACL Anthology](https://aclanthology.org/2026.findings-acl.1556/) · [arXiv](https://arxiv.org/abs/2608.30270) |
| Code | Evaluation and release utilities available in this repository |
| Data | Available for research use upon request |
| License | Paper, code, and data follow their respective release terms |


## Benchmark

Each READI item contains:

- an image encoding sociopragmatic context;
- an indirect directive utterance;
- a question about the utterance's pragmatic function;
- four mutually exclusive intent choices; and
- one gold answer.

The benchmark contains 102 multimodal items across two independently developed
subsets:

| Subset | Language | Items |
|---|---|---:|
| KRISA | Korean | 57 |
| ENGISA | English | 45 |

KRISA and ENGISA are not translation pairs. Each was constructed and validated
through a language-specific process.

### Indirectness levels

READI follows a CCSARP-based graded indirectness design.

| Level | Category | Description |
|---|---|---|
| 1 | CID | Conventionally indirect directive |
| 2 | NCID - strong hint | Non-conventional directive with a lexical hint |
| 3 | NCID - mild/no hint | Non-conventional directive requiring stronger contextual inference |


## Evaluation

READI formulates visual pragmatic understanding as a four-choice
question-answering task. The primary metric is four-choice accuracy.

Predictions must be provided as JSONL, with one object per item:

```json
{"item_id": "readi_ko_001", "predicted_choice": 2}
```

`predicted_choice` must be an integer from 1 to 4.

Run the evaluator with:

```bash
python scripts/evaluate.py \
  --gold data/release/readi.jsonl \
  --predictions predictions/model.jsonl
```

Missing, duplicate, unknown, and malformed predictions are reported and remain
in the evaluation denominator. See [the prediction format](docs/PREDICTION_FORMAT.md)
for details.

## Release utilities

The repository includes deterministic utilities for converting authorized source
workbooks, extracting embedded images, validating annotations and file hashes,
and scoring model predictions.

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

## Repository structure

```text
├── data/                 # Data-access and format notes
├── docs/                 # Data card and prediction specification
├── scripts/              # Build, validation, and evaluation utilities
├── tests/                # Regression tests
└── requirements.txt
```


## Usage terms

Paper, code, and data usage terms follow their respective official archival
releases. This repository does not grant additional rights beyond those terms.

## Data access

The READI dataset is available for research use upon request. To request access,
email **Park** at
[cosmic4intelligence@gmail.com](mailto:cosmic4intelligence@gmail.com) with your
name, affiliation, and a brief description of the intended research use.

Source workbooks and manuscript files are not distributed through this repository.
Access to the released dataset is subject to its accompanying usage terms.

The normalized public format is documented in [the data card](docs/DATA_CARD.md).
