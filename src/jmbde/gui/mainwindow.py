# -*- coding: utf-8 -*-
import os
import sys

from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QMainWindow

from ..ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    """Main Window."""

    def __init__(self, app, translator, parent: Any = None) -> None:
        """Init the class.

        Args:
            parent: The initializer for the parent QMainWindow.
        """
        super(MainWindow, self).__init__(parent)

        self._app = app
        self._translator = translator
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create Widgets
        # self.clipboard = QApplication.clipboard()
        # Create widgets
        # self.clipboard = QApplication.clipboard()

        # Connect signals and slots
        # self.ui.actionSave.triggered.connect(self.save_content)
        # self.ui.actionQuit.triggered.connect(self.quit_app)
        # self.ui.actionCopy.triggered.connect(self.clipboard_copy)
        # self.ui.actionAbout.triggered.connect(self.about)

        # self.ui.okButton.clicked.connect(self.quit_app)
        # self.ui.cancelButton.clicked.connect(self.quit_app)

        # Configure widgets
        # self.ui.textBrowser.setOpenExternalLinks(True)

        # Start thread
        # self.worker = Worker()
        # self.worker.send_text.connect(self.receive_text)
        # self.worker.start()

    def quit_app(self) -> None:
        """Close application.

        Here is the option to popup a dialog...
        """
        # answer = QMessageBox.question(self, 'Quit program', 'Are you sure?',
        #                               QMessageBox.Yes | QMessageBox.No)
        # if answer == QMessageBox.Yes:
        #     self.close()
        self.close()

    def save_content(self) -> None:
        """Save content of text to a file."""
        # TODO Save to file
        print("Save")

    def clipboard_copy(self) -> None:
        """Copy text box content to the clipboard."""
        # text = self.ui.textBrowser.toPlainText()
        # self.clipboard.setText(text,  QClipboard.Clipboard)
        pass

    def receive_text(self, some_string: str) -> None:
        """Add some_string at the end of textBrowser.

        Args:
            some_string: Add some string
        """
        # self.ui.textBrowser.append(some_string)
        pass

    def about(self) -> None:
        """Help/About message box."""
        QMessageBox.about(self, "jmbde - A BDE tool", "juergen.muelbert@gmail.com")
