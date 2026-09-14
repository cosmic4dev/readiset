# READI: Read the Room, Read the Image

[![ACL Anthology](https://img.shields.io/badge/Findings%20of%20ACL-2026-1f6feb)](https://aclanthology.org/2026.findings-acl.1556/)
[![arXiv](https://img.shields.io/badge/arXiv-2608.30270-b31b1b)](https://arxiv.org/abs/2608.30270)

READI is a bilingual multimodal benchmark for evaluating whether vision-language
models can infer the intended function of indirect directive speech acts from an
utterance and its visual sociopragmatic context.

## Paper

**Read the Room, Read the Image: Understanding Indirect Speech Acts in
Multimodal Visual Contexts**

Findings of the Association for Computational Linguistics: ACL 2026

- [ACL Anthology](https://aclanthology.org/2026.findings-acl.1556/)
- [arXiv](https://arxiv.org/abs/2608.30270)
- [DOI](https://doi.org/10.18653/v1/2026.findings-acl.1556)

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

## Data access

Benchmark data and usage terms follow the authorized archival release. Source
workbooks and manuscript files are not distributed through this repository.

The normalized public format is documented in [the data card](docs/DATA_CARD.md).

## Evaluation

READI is evaluated as four-choice visual pragmatic question answering. The
primary metric is exact-match accuracy.

Predictions use one JSON object per line:

```json
{"item_id":"readi_ko_001","predicted_choice":2}
```

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

## Citation

Please cite the archival paper:

> Jaehee Kim, Ji Hoon Chung, Seoyoon Park, Unsol Kim, Kyungwon Park, JiHak Kim,
> Yi-Jun Chen, and Hansaem Kim. 2026. “Read the Room, Read the Image:
> Understanding Indirect Speech Acts in Multimodal Visual Contexts.” In
> *Findings of the Association for Computational Linguistics: ACL 2026*,
> pages 31109–31124. Association for Computational Linguistics.

## Usage terms

Paper, code, and data usage terms follow their respective official archival
releases. This repository does not grant additional rights beyond those terms.
