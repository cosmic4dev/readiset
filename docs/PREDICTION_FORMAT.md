# Prediction format

Use one JSON object per line:

```json
{"item_id":"readi_ko_001","predicted_choice":2}
```

`predicted_choice` must be an integer from 1 through 4. Optional explanations may
be stored under `explanation`, but do not affect primary accuracy. Missing,
duplicate, unknown, or malformed records are reported and scored as incorrect.

