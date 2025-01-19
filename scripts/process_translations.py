#!/usr/bin/env python3
"""Process and validate PySide6/Qt6 translation files."""
from pathlib import Path
import json
import argparse
from typing import Dict, List
from xml.etree import ElementTree

class TranslationProcessor:
    """Process Qt6 translation files."""

    def __init__(self, ts_dir: Path):
        """Initialize processor."""
        self.ts_dir = ts_dir
        self.warnings: List[str] = []

    def process_file(self, file_path: Path) -> Dict:
        """Process a single .ts file."""
        tree = ElementTree.parse(file_path)
        root = tree.getroot()

        stats = {
            'total': 0,
            'translated': 0,
            'missing': 0,
            'warnings': []
        }

        # Process each context
        for context in root.findall('.//context'):
            context_name = context.find('name').text

            for message in context.findall('message'):
                stats['total'] += 1

                source = message.find('source').text
                translation = message.find('translation')

                if translation is None or translation.get('type') == 'unfinished':
                    stats['missing'] += 1
                    stats['warnings'].append(
                        f"Missing translation in {context_name}: {source}"
                    )
                else:
                    stats['translated'] += 1

                # Check for Qt quick translations
                if 'qml' in context_name.lower():
                    self.validate_qml_translation(source, translation.text, stats)

        return stats

    def validate_qml_translation(self, source: str, translation: str, stats: Dict):
        """Validate QML-specific translations."""
        # Check for QML placeholders
        qml_placeholders = ["%1", "%2", "%3"]
        for placeholder in qml_placeholders:
            if source.count(placeholder) != (translation or "").count(placeholder):
                stats['warnings'].append(
                    f"Mismatched QML placeholder {placeholder} in: {source}"
                )

    def process_all(self) -> Dict:
        """Process all translation files."""
        results = {
            'totalStrings': 0,
            'updated': 0,
            'missing': 0,
            'languages': {},
            'warnings': []
        }

        for ts_file in self.ts_dir.glob('*.ts'):
            lang = ts_file.stem.split('_')[-1]
            stats = self.process_file(ts_file)

            results['languages'][lang] = {
                'total': stats['total'],
                'translated': stats['translated'],
                'missing': stats['missing']
            }

            results['totalStrings'] += stats['total']
            results['updated'] += stats['translated']
            results['missing'] += stats['missing']
            results['warnings'].extend(stats['warnings'])

        return results

def main():
    """Main function."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--ts-dir', type=Path, required=True)
    parser.add_argument('--report-file', type=Path, required=True)
    args = parser.parse_args()

    processor = TranslationProcessor(args.ts_dir)
    report = processor.process_all()

    args.report_file.write_text(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
