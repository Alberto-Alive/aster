import argparse
import json
from pathlib import Path
from aster.matrix import multiply

def main() -> None:
    parser = argparse.ArgumentParser(description="Multiply two matrices from a JSON file.")
    parser.add_argument("input", type=Path, help="JSON file containing matrices a and b")
    parser.add_argument("output", type=Path, help="file where the result will be written")

    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    result = multiply(data["a"], data["b"])

    args.output.write_text(
        json.dumps({
            "result": result
        }, indent=2) + "\n", encoding="utf-8"
    )