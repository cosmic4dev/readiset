#!/usr/bin/env python3
"""Validate READI annotations, images, hashes, and paper-level counts."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

EXPECTED_COUNTS = {"ko": 57, "en": 45}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads((args.data_dir / "manifest.json").read_text(encoding="utf-8"))
    data_path = args.data_dir / "readi.jsonl"
    records = [json.loads(line) for line in data_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    errors = []
    ids = [r.get("item_id") for r in records]
    if len(ids) != len(set(ids)):
        errors.append("duplicate item_id")
    counts = Counter(r.get("language") for r in records)
    if dict(counts) != EXPECTED_COUNTS:
        errors.append(f"count mismatch: {dict(counts)} != {EXPECTED_COUNTS}")
    for record in records:
        item_id = record.get("item_id", "<missing>")
        if record.get("isa_intensity") not in {1, 2, 3}:
            errors.append(f"{item_id}: invalid intensity")
        if type(record.get("answer")) is not int or record["answer"] not in {1, 2, 3, 4}:
            errors.append(f"{item_id}: invalid answer")
        if set(record.get("choices", {})) != {"1", "2", "3", "4"}:
            errors.append(f"{item_id}: invalid choices")
        if not record.get("question") or not record.get("utterance"):
            errors.append(f"{item_id}: missing text")
        image = args.data_dir / record.get("image", "")
        if not image.is_file() or image.stat().st_size == 0:
            errors.append(f"{item_id}: missing image")
    for relative, expected_hash in manifest.get("files", {}).items():
        path = args.data_dir / relative
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected_hash:
            errors.append(f"hash mismatch: {relative}")
    if not manifest.get("release_ready"):
        errors.append("manifest is not release-ready")
    if errors:
        raise SystemExit("VALIDATION FAILED\n" + "\n".join(errors[:50]))
    print(f"VALIDATION PASSED: {len(records)} items and {len(records)} images")


if __name__ == "__main__":
    main()

