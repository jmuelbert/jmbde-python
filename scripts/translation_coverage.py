#!/usr/bin/env python3
"""Calculate translation coverage statistics."""
import argparse
import json
from pathlib import Path
from typing import Dict

def calculate_ts_coverage(ts_dir: Path) -> Dict:
    """Calculate translation coverage for Qt translation files."""
    coverage = {}

    for ts_file in ts_dir.glob('*.ts'):
        lang = ts_file.stem.split('_')[-1]
        tree = ElementTree.parse(ts_file)
        root = tree.getroot()

        total = 0
        translated = 0

        for message in root.findall('.//message'):
            total += 1
            translation = message.find('translation')
            if translation is not None and translation.get('type') != 'unfinished':
                translated += 1

        coverage[lang] = {
            'total': total,
            'translated': translated,
            'missing': total - translated,
            'coverage': (translated / total * 100) if total > 0 else 0
        }

    return coverage

def calculate_docs_coverage(docs_dir: Path) -> Dict:
    """Calculate translation coverage for documentation."""
    coverage = {}
    base_files = set(Path('docs/en').glob('*.md'))

    for lang_dir in docs_dir.glob('*'):
        if not lang_dir.is_dir():
            continue

        lang = lang_dir.name
        translated_files = set(lang_dir.glob('*.md'))

        coverage[lang] = {
            'total': len(base_files),
            'translated': len(translated_files),
            'missing': len(base_files - translated_files),
            'coverage': (len(translated_files) / len(base_files) * 100)
        }

    return coverage

def main():
    """Main function."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--ts-dir', type=Path, required=True)
    parser.add_argument('--docs-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()

    ts_coverage = calculate_ts_coverage(args.ts_dir)
    docs_coverage = calculate_docs_coverage(args.docs_dir)

    # Combine coverages
    combined_coverage = {}
    all_languages = set(ts_coverage.keys()) | set(docs_coverage.keys())

    for lang in all_languages:
        ts_stats = ts_coverage.get(lang, {'coverage': 0})
        docs_stats = docs_coverage.get(lang, {'coverage': 0})

        combined_coverage[lang] = {
            'ui_coverage': ts_stats['coverage'],
            'docs_coverage': docs_stats['coverage'],
            'coverage': (ts_stats['coverage'] + docs_stats['coverage']) / 2,
            'missing': (ts_stats.get('missing', 0) + docs_stats.get('missing', 0))
        }

    # Calculate overall coverage
    total_coverage = sum(lang['coverage'] for lang in combined_coverage.values()) / len(combined_coverage)

    report = {
        'overall_coverage': total_coverage,
        'languages': combined_coverage
    }

    args.output.write_text(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
