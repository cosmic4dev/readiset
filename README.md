# READI: Read the Room, Read the Image

READI is a bilingual multimodal benchmark for evaluating whether vision-language
models can infer the intended function of indirect directive speech acts from an
utterance and its visual sociopragmatic context.

The benchmark accompanies **“Read the Room, Read the Image: Understanding
Indirect Speech Acts in Multimodal Visual Contexts.”**

> **Release-candidate status:** the code and documentation may be published first.
> The source workbooks, manuscript PDF, extracted images, and generated benchmark
> data remain private until the source discrepancies in `docs/SOURCE_AUDIT.md` are
> resolved and the official archival release is finalized.

## Benchmark task

Each item contains one image, one indirect directive utterance, one question about
the utterance's pragmatic function, four mutually exclusive intent choices, and
one gold choice.

| Level | Category | Interpretation |
|---|---|---|
| 1 | CID | Conventionally indirect directive |
| 2 | NCID - strong hint | Non-conventional directive with a lexical hint |
| 3 | NCID - mild/no hint | Non-conventional directive requiring stronger contextual inference |

KRISA and ENGISA were developed independently through language-specific
procedures. They are not translation pairs and must not be evaluated as aligned
item pairs.

## Reported benchmark size

The paper reports 102 multimodal items: 57 Korean and 45 English. The supplied
workbooks currently contain 56 Korean and 45 English item rows. Several intensity
cells are also blank. The release builder rejects these inconsistencies instead
of inferring labels from row order. See [the source audit](docs/SOURCE_AUDIT.md).

## Build

```bash
python -m pip install -r requirements.txt

python scripts/build_release.py \
  --krisa docs/KRISA_READI.xlsx \
  --engisa docs/ENGISA_READI.xlsx \
  --corrections data/source_corrections.json \
  --output-dir data/release

python scripts/validate_release.py --data-dir data/release
```

`source_corrections.json` must be supplied and approved by the dataset owners.
The repository does not guess missing labels or fabricate the missing Korean item.

## Evaluate

```bash
python scripts/evaluate.py \
  --gold data/release/readi.jsonl \
  --predictions predictions/model.jsonl
```

The primary metric is four-choice accuracy. Missing, duplicate, unknown, and
malformed predictions are reported and never silently removed from the denominator.

## Repository layout

```text
├── data/
│   ├── README.md
│   └── source_corrections.example.json
├── docs/
│   ├── CURATION_AUDIT.md
│   ├── DATA_CARD.md
│   ├── PREDICTION_FORMAT.md
│   ├── RELEASE_CHECKLIST.md
│   └── SOURCE_AUDIT.md
├── scripts/
│   ├── build_release.py
│   ├── evaluate.py
│   └── validate_release.py
└── tests/
```

## Citation

See [`CITATION.cff`](CITATION.cff). Archival paper and proceedings links should
be added once publicly available. Kyungwon Park is listed as the repository
maintainer; the preferred paper citation preserves the complete author list.

## License

Code and data usage terms follow the official archival release. This repository
does not grant additional rights. The manuscript PDF is not redistributed here;
the official proceedings or archive link will be used when available.
