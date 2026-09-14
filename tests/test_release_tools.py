import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
from build_release import normalize_intensity, parse_choices


class ReleaseToolsTest(unittest.TestCase):
    def test_intensity_normalization(self):
        self.assertEqual(normalize_intensity(2), 2)
        self.assertEqual(normalize_intensity("3단계"), 3)
        self.assertIsNone(normalize_intensity(None))

    def test_choice_parsing(self):
        self.assertEqual(parse_choices("1) A\n2) B\n3) C\n4) D"), {"1": "A", "2": "B", "3": "C", "4": "D"})

    def test_missing_prediction_stays_in_denominator(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            gold = root / "gold.jsonl"
            pred = root / "pred.jsonl"
            gold.write_text(
                '{"item_id":"a","language":"ko","answer":2}\n'
                '{"item_id":"b","language":"en","answer":1}\n', encoding="utf-8"
            )
            pred.write_text('{"item_id":"a","predicted_choice":2}\n', encoding="utf-8")
            script = Path(__file__).parents[1] / "scripts" / "evaluate.py"
            result = subprocess.run(
                [sys.executable, str(script), "--gold", str(gold), "--predictions", str(pred)],
                capture_output=True, text=True, check=True,
            )
            metrics = json.loads(result.stdout)
            self.assertEqual(metrics["accuracy"], 0.5)
            self.assertEqual(metrics["missing_predictions"], 1)


if __name__ == "__main__":
    unittest.main()

