"""Compare screenshots for visual regression testing."""
from pathlib import Path
import cv2
import numpy as np
from PIL import Image

def compare_screenshots(baseline_path: Path, current_path: Path, diff_path: Path):
    """Compare two screenshots and generate a diff image."""
    baseline = cv2.imread(str(baseline_path))
    current = cv2.imread(str(current_path))

    if baseline.shape != current.shape:
        return False, "Image sizes don't match"

    diff = cv2.absdiff(baseline, current)
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) > 0

    if mask.any():
        # Highlight differences
        current_highlighted = current.copy()
        current_highlighted[mask] = [0, 0, 255]  # Red highlighting

        cv2.imwrite(str(diff_path), current_highlighted)
        return False, "Visual differences found"

    return True, "Images match"

def main():
    """Main function to compare screenshots."""
    baseline_dir = Path("tests/pyside6/baseline_screenshots")
    current_dir = Path("screenshots")
    diff_dir = Path("screenshot-diffs")
    diff_dir.mkdir(exist_ok=True)

    results = []
    for baseline in baseline_dir.glob("*.png"):
        current = current_dir / baseline.name
        if current.exists():
            match, message = compare_screenshots(
                baseline,
                current,
                diff_dir / f"diff_{baseline.name}"
            )
            results.append((baseline.name, match, message))

    # Generate report
    with open("screenshot-diffs/report.md", "w") as f:
        f.write("# Visual Regression Test Report\n\n")
        for name, match, message in results:
            status = "✅" if match else "❌"
            f.write(f"- {status} {name}: {message}\n")

if __name__ == "__main__":
    main()
