# Data access

The authorized archival release defines access to the READI benchmark data and
its usage terms. Source workbooks and manuscript files are not distributed in
this repository.

The evaluation utilities expect the following local structure:

```text
data/release/
├── readi.jsonl
├── manifest.json
└── images/
```

`data/release/` is ignored by Git so that locally obtained benchmark assets are
not accidentally committed.
