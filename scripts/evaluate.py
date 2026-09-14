#!/usr/bin/env python3
"""Score READI four-choice predictions without dropping invalid records."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def load(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def ratio(n: int, d: int) -> float:
    return n / d if d else 0.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gold", type=Path, required=True)
    parser.add_argument("--predictions", type=Path, required=True)
    args = parser.parse_args()
    gold, prediction_rows = load(args.gold), load(args.predictions)
    counts = Counter(row.get("item_id") for row in prediction_rows)
    predictions = {row.get("item_id"): row for row in prediction_rows}
    gold_ids = {row["item_id"] for row in gold}
    by_language = {}
    correct_total = 0
    for language in ("ko", "en"):
        items = [item for item in gold if item["language"] == language]
        correct = 0
        for item in items:
            prediction = predictions.get(item["item_id"], {})
            valid = counts[item["item_id"]] == 1 and type(prediction.get("predicted_choice")) is int
            correct += bool(valid and prediction["predicted_choice"] == item["answer"])
        correct_total += correct
        by_language[language] = {"n": len(items), "accuracy": ratio(correct, len(items))}
    metrics = {
        "n": len(gold),
        "accuracy": ratio(correct_total, len(gold)),
        "by_language": by_language,
        "missing_predictions": sum(counts[item["item_id"]] == 0 for item in gold),
        "duplicate_prediction_ids": sum(count > 1 for item_id, count in counts.items() if item_id in gold_ids),
        "unknown_prediction_ids": len(set(counts) - gold_ids),
    }
    print(json.dumps(metrics, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

