#!/usr/bin/env python3
"""Check translation files for completeness and consistency."""

import argparse
import json
from pathlib import Path
from typing import Dict, List
from xml.etree import ElementTree


def check_ts_file(ts_path: Path) -> Dict:
    """Check a .ts file for missing translations."""
    tree = ElementTree.parse(ts_path)
    root = tree.getroot()

    total = 0
    missing = 0
    warnings = []

    for message in root.findall(".//message"):
        total += 1
        translation = message.find("translation")

        if translation is None or translation.get("type") == "unfinished":
            missing += 1
            source = message.find("source").text
            warnings.append(f"Missing translation for: {source}")

    return {
        "file": ts_path.name,
        "total": total,
        "missing": missing,
        "warnings": warnings,
    }


def main():
    """Main function."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--ts-dir", type=Path, required=True)
    parser.add_argument("--report-file", type=Path, required=True)
    args = parser.parse_args()

    results = []
    total_strings = 0
    total_missing = 0
    all_warnings = []

    for ts_file in args.ts_dir.glob("*.ts"):
        result = check_ts_file(ts_file)
        results.append(result)
        total_strings += result["total"]
        total_missing += result["missing"]
        all_warnings.extend(result["warnings"])

    report = {
        "total_strings": total_strings,
        "missing_translations": total_missing,
        "completion_rate": (total_strings - total_missing) / total_strings * 100,
        "files": results,
        "warnings": all_warnings,
    }

    args.report_file.write_text(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
