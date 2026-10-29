import argparse
import json
from pathlib import Path
from aster.matrix import multiply
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description="Multiply two matrices from a JSON file.")
    parser.add_argument("input", type=Path, help="JSON file containing matrices a and b")
    parser.add_argument("output", type=Path, help="file where the result will be written")

    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("input JSON must be an object")
        if "a" not in data or "b" not in data:
            raise ValueError("input JSON must contain keys 'a' and 'b'")
        result = multiply(data["a"], data["b"])

        args.output.write_text(
            json.dumps({
                "result": result
            }, indent=2) + "\n", encoding="utf-8"
        )
    except (OSError, json.JSONDecodeError, KeyError, ValueError) as error:
        print(f"aster: {error}", file=sys.stderr)
        raise SystemExit(1)