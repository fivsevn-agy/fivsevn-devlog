#!/usr/bin/env python3
"""Read-only source registry audit. Optional --spec-root checks enum parity."""
import argparse
import json
import re
from pathlib import Path

import yaml

from build import read_yaml_blocks
from source_validation import ENUMS, audit_blocks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, default=Path(__file__).with_name("sources.md"))
    parser.add_argument("--spec-root", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit_blocks(read_yaml_blocks(args.sources.read_text()))
    if args.spec_root:
        text = (args.spec_root / "appendix/spec-source-intake-enums-001.md").read_text()
        spec = {}
        for block in re.findall(r"```yaml\s*\n(.*?)\n```", text, re.S):
            spec.update({k: set(v) for k, v in yaml.safe_load(block).items() if isinstance(v, list)})
        for field, values in ENUMS.items():
            if values != spec.get(field):
                result["errors"].append(f"Spec enum mismatch: {field}")
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(output)
        print(f"{result['source_count']} sources, {result['section_count']} sections, "
              f"{len(result['errors'])} errors, {len(result['cross_section_conflicts'])} conflicts, "
              f"{len(result['pending_reviews'])} pending reviews")
    else:
        print(output, end="")
    raise SystemExit(bool(result["errors"]))


if __name__ == "__main__":
    main()
