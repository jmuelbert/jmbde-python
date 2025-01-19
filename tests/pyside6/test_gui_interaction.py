from PySide6.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QWidget


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.on_submit)

    def on_submit(self):
        self.edit.setText("Submitted!")


def test_gui_interaction(qtbot):
    window = MyWindow()
    qtbot.addWidget(window)

    # Simulate typing in the QLineEdit
    qtbot.keyClicks(window.edit, "Hello")
    assert window.edit.text() == "Hello"

    # Simulate clicking the button
    qtbot.mouseClick(window.button, Qt.LeftButton)
    assert window.edit.text() == "Submitted!"
