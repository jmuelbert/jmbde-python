#!/usr/bin/env python3
"""Translate documentation files."""
import argparse
from pathlib import Path
from typing import List, Dict
import frontmatter
import yaml

def process_markdown(content: str, lang: str) -> str:
    """Process markdown content for translation."""
    # Parse front matter
    post = frontmatter.loads(content)
    
    # Update metadata for translation
    metadata = dict(post.metadata)
    metadata['language'] = lang
    
    # Create translated document
    return frontmatter.dumps(post)

def main():
    """Main function."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--languages', type=str, required=True)
    args = parser.parse_args()

    languages = args.languages.split()
    
    # Process each markdown file
    for source_file in args.source_dir.glob('*.md'):
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

if __name__ == '__main__':
    main()