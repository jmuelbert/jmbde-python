"""Capture screenshots of UI components on test failure."""

import sys
from pathlib import Path

from PySide6.QtCore import QTimer
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QApplication


def capture_widget_screenshot(widget, name):
    """Capture a screenshot of a widget."""
    screen = QApplication.primaryScreen()
    if not widget.isVisible():
        widget.show()
    screenshot = screen.grabWindow(widget.winId())
    path = Path("test-artifacts/screenshots")
    path.mkdir(parents=True, exist_ok=True)
    screenshot.save(str(path / f"{name}.png"))


def main():
    """Main function to capture screenshots."""
    app = QApplication(sys.argv)

    # Import your widgets here
    from src.jmbde.gui.main_app import MainWindow

    # Create and capture main window
    main_window = MainWindow()
    capture_widget_screenshot(main_window, "main_window")

    # Add more widgets as needed

    QTimer.singleShot(0, app.quit)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
