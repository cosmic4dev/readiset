# Data access

The READI dataset is available for research use upon request. Email Kyungwon Park
at `cosmic4intelligencel@gmail.com` with your name, affiliation, and a brief
description of the intended research use. Source workbooks and manuscript files
are not distributed in this repository.

The evaluation utilities expect the following local structure:

```text
data/release/
├── readi.jsonl
├── manifest.json
└── images/
```

`data/release/` is ignored by Git so that locally obtained benchmark assets are
not accidentally committed.
