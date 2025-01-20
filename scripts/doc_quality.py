#!/usr/bin/env python3
"""Check the quality of Markdown documentation files."""

import argparse
import re
from pathlib import Path
from typing import List, Dict, Tuple
import frontmatter


def check_frontmatter(file_path: Path) -> List[str]:
    """Check YAML front matter for required fields."""
    try:
        post = frontmatter.load(file_path)
        required_fields = ["title", "description"]
        missing_fields = [field for field in required_fields if field not in post.metadata]

        if missing_fields:
            return [f"Missing required front matter fields: {', '.join(missing_fields)}"]
    except Exception as e:
        return [f"Failed to parse front matter: {e}"]

    return []


def check_line_length(file_path: Path, max_length: int = 120) -> List[str]:
    """Check for lines exceeding the maximum length."""
    issues = []
    with file_path.open() as f:
        for i, line in enumerate(f, start=1):
            if len(line.strip()) > max_length:
                issues.append(f"Line {i} exceeds {max_length} characters.")
    return issues


def check_links(file_path: Path) -> List[str]:
    """Check for malformed or suspicious links."""
    issues = []
    link_pattern = re.compile(r'\[.*?\]\((.*?)\)')
    with file_path.open() as f:
        for i, line in enumerate(f, start=1):
            for match in link_pattern.finditer(line):
                url = match.group(1)
                if not (url.startswith("http://") or url.startswith("https://") or url.startswith("/")):
                    issues.append(f"Line {i} contains a malformed or non-absolute link: {url}")
    return issues


def check_spelling(file_path: Path, banned_words: List[str] = None) -> List[str]:
    """Check for banned or misspelled words."""
    if banned_words is None:
        banned_words = ["teh", "dont", "recieve"]
    issues = []
    with file_path.open() as f:
        for i, line in enumerate(f, start=1):
            for word in banned_words:
                if word in line:
                    issues.append(f"Line {i} contains banned or misspelled word: {word}")
    return issues


def analyze_file(file_path: Path) -> Dict[str, List[str]]:
    """Run all quality checks on a single file."""
    results = {
        "frontmatter": check_frontmatter(file_path),
        "line_length": check_line_length(file_path),
        "links": check_links(file_path),
        "spelling": check_spelling(file_path),
    }
    return results


def main():
    parser = argparse.ArgumentParser(description="Check the quality of Markdown documentation files.")
    parser.add_argument("--source-dir", required=True, type=Path, help="Directory containing Markdown files.")
    parser.add_argument("--max-line-length", type=int, default=120, help="Maximum allowed line length.")
    args = parser.parse_args()

    source_dir = args.source_dir
    if not source_dir.is_dir():
        print(f"Error: {source_dir} is not a valid directory.")
        return

    all_issues = []
    for file_path in source_dir.glob("*.md"):
        print(f"Analyzing {file_path}...")
        issues = analyze_file(file_path)
        for check, problems in issues.items():
            if problems:
                print(f"  [{check}]")
                for problem in problems:
                    print(f"    - {problem}")
                all_issues.extend(problems)

    if all_issues:
        print("\nSummary of Issues:")
        for issue in all_issues:
            print(f"  - {issue}")
        exit(1)
    else:
        print("\nAll checks passed successfully!")


if __name__ == "__main__":
    main()
