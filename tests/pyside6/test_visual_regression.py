"""Visual regression tests for UI components."""

import pytest
from PySide6.QtCore import Qt
from PySide6.QtTest import QTest


def test_main_window_appearance(qtbot, screenshot):
    """Test the appearance of the main window."""
    from src.jmbde.gui.main_app import MainWindow

    window = MainWindow()
    qtbot.addWidget(window)
    window.show()

    # Wait for window to settle
    qtbot.wait(500)

    # Take screenshot and compare
    screenshot.assert_screenshot(window, "main_window")


def test_employee_dialog(qtbot, screenshot):
    """Test the employee dialog appearance."""
    from src.jmbde.gui.employee_dialog import EmployeeDialog

    dialog = EmployeeDialog()
    qtbot.addWidget(dialog)
    dialog.show()

    # Interact with dialog
    qtbot.keyClicks(dialog.findChild(QLineEdit, "name_input"), "John Doe")
    qtbot.wait(200)

    # Take screenshot
    screenshot.assert_screenshot(dialog, "employee_dialog_filled")


@pytest.mark.parametrize("theme", ["light", "dark"])
def test_theme_switching(qtbot, screenshot, theme):
    """Test appearance with different themes."""
    from src.jmbde.gui.main_app import MainWindow

    window = MainWindow()
    window.set_theme(theme)
    qtbot.addWidget(window)
    window.show()
    qtbot.wait(500)

    screenshot.assert_screenshot(window, f"main_window_{theme}")
