#!/usr/bin/env python3
"""Enhanced documentation quality checker with multilingual support."""

import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Set

import yaml
from rich.console import Console
from rich.table import Table


@dataclass
class DocConfig:
    """Documentation configuration."""

    min_length: int = 100
    required_sections: Set[str] = None
    supported_languages: Set[str] = None
    code_example_required: bool = True
    image_required: bool = False

    @classmethod
    def from_yaml(cls, path: Path) -> "DocConfig":
        """Load configuration from YAML file."""
        with open(path, encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return cls(
            min_length=config.get("min_length", 100),
            required_sections=set(config.get("required_sections", [])),
            supported_languages=set(config.get("supported_languages", [])),
            code_example_required=config.get("code_example_required", True),
            image_required=config.get("image_required", False),
        )


class DocChecker:
    """Documentation quality checker."""

    def __init__(self, config: DocConfig):
        self.config = config
        self.console = Console()
        self.issues: Dict[str, List[str]] = {}

    def check_markdown(self, file_path: Path) -> None:
        """Check a markdown file for quality issues."""
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        file_issues = []

        # Basic checks
        if len(content) < self.config.min_length:
            file_issues.append(f"Content too short ({len(content)} chars)")

        if not re.search(r"^#\s.+", content, re.MULTILINE):
            file_issues.append("Missing main header")

        # Code examples
        if self.config.code_example_required and file_path.stem not in [
            "changelog",
            "license",
        ]:
            if not re.search(r"```.*\n", content):
                file_issues.append("No code examples found")

        # Section checks
        if self.config.required_sections:
            sections = set(re.findall(r"^##\s+(.+)$", content, re.MULTILINE))
            missing = self.config.required_sections - sections
            if missing:
                file_issues.append(f"Missing required sections: {', '.join(missing)}")

        # Image checks
        if self.config.image_required:
            if not re.search(r"!\[.*\]\(.*\)", content):
                file_issues.append("No images found")

        # Links check
        links = re.findall(r"\[([^\]]+)\]\(([^\)]+)\)", content)
        for text, url in links:
            if not url.startswith(("http", "#", "/", "..")):
                file_issues.append(f"Invalid link: {url}")

        # Language-specific checks
        lang_code = self._get_language_code(file_path)
        if lang_code and lang_code not in self.config.supported_languages:
            file_issues.append(f"Unsupported language: {lang_code}")

        if file_issues:
            self.issues[str(file_path)] = file_issues

    def _get_language_code(self, file_path: Path) -> str:
        """Extract language code from file path."""
        parts = file_path.parts
        if len(parts) > 1:
            for lang in self.config.supported_languages:
                if lang in parts:
                    return lang
        return None

    def check_translations(self, docs_dir: Path) -> None:
        """Check if all documents are translated."""
        base_docs = set()
        translated_docs = {lang: set() for lang in self.config.supported_languages}

        # Collect all documents
        for file in docs_dir.rglob("*.md"):
            if "i18n" not in str(file):
                base_docs.add(file.name)
            else:
                lang = self._get_language_code(file)
                if lang:
                    translated_docs[lang].add(file.name)

        # Check missing translations
        for lang, docs in translated_docs.items():
            missing = base_docs - docs
            if missing:
                self.issues[f"Missing {lang} translations"] = list(missing)

    def generate_report(self) -> None:
        """Generate a formatted report of issues."""
        table = Table(title="Documentation Quality Report")
        table.add_column("File", style="cyan")
        table.add_column("Issues", style="red")

        for file, file_issues in self.issues.items():
            table.add_row(file, "\n".join(f"- {issue}" for issue in file_issues))

        self.console.print(table)


def main():
    """Run documentation quality checks."""
    # Load configuration
    config_path = Path("docs/config/doc_quality.yml")
    if not config_path.exists():
        print(f"Creating default configuration at {config_path}")
        config = DocConfig(
            min_length=100,
            required_sections={"Installation", "Usage", "Configuration"},
            supported_languages={"en", "de", "it", "es"},
            code_example_required=True,
            image_required=True,
        )
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, "w", encoding="utf-8") as f:
            yaml.dump(
                {
                    "min_length": config.min_length,
                    "required_sections": list(config.required_sections),
                    "supported_languages": list(config.supported_languages),
                    "code_example_required": config.code_example_required,
                    "image_required": config.image_required,
                },
                f,
            )
    else:
        config = DocConfig.from_yaml(config_path)

    checker = DocChecker(config)
    docs_dir = Path("docs")

    # Check all markdown files
    for md_file in docs_dir.rglob("*.md"):
        checker.check_markdown(md_file)

    # Check translations
    checker.check_translations(docs_dir)

    # Generate report
    checker.generate_report()

    if checker.issues:
        sys.exit(1)

    print("Documentation quality check passed!")
    sys.exit(0)


if __name__ == "__main__":
    main()
