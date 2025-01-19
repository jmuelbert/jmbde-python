from PySide6.QtWidgets import QPushButton


def test_button_click(qtbot):
    button = QPushButton("Click Me")
    qtbot.addWidget(button)

    # Simulate a button click
    button.click()

    assert button.text() == "Click Me"
