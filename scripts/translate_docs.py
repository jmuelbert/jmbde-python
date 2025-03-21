#!/usr/bin/env python3
"""Translate documentation files."""

import argparse
from pathlib import Path
from typing import List

import frontmatter


def process_markdown(content: str, lang: str) -> str:
    """Process markdown content for translation."""
    # Parse front matter
    post = frontmatter.loads(content)

    # Update metadata for translation
    metadata = dict(post.metadata)
    metadata["language"] = lang

    # Create translated document
    return frontmatter.dumps(post)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Translate documents.")
    parser.add_argument(
        "--source-dir",
        required=True,
        type=Path,
        help="Source directory containing documents.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        type=Path,
        help="Output directory for translated documents.",
    )
    parser.add_argument(
        "--languages",
        required=True,
        nargs="+",
        help="List of languages to translate to.",
    )
    args = parser.parse_args()

    # `args.languages` is already a list, no need for `.split()`
    languages = args.languages

    # Process each markdown file in the source directory
    for source_file in args.source_dir.glob("*.md"):
        content = source_file.read_text()

        for lang in languages:
            # Create language directory
            lang_dir = args.output_dir / lang
            lang_dir.mkdir(parents=True, exist_ok=True)

            # Process and save translated file
            translated = process_markdown(content, lang)
            output_file = lang_dir / source_file.name

            if not output_file.exists():
                output_file.write_text(translated)


if __name__ == "__main__":
    main()
