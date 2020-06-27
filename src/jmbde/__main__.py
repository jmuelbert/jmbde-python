#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   jmbde a BDE Tool for datacontext
#   Copyright (C) 2018-2020  Jürgen Mülbert
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
"""JMBDe app."""
import sys
from typing import Any

import click
from PySide2.QtCore import QCoreApplication
from PySide2.QtCore import QLocale
from PySide2.QtCore import QThread
from PySide2.QtCore import QTranslator
from PySide2.QtCore import Signal
from PySide2.QtGui import QGuiApplication
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QMessageBox

from .qrc_resources import *  # noqa
from jmbde.ui.ui_mainwindow import Ui_MainWindow


class ApplicationWindow(QMainWindow):
    """Main Window."""

    def __init__(self, parent: Any = None) -> None:
        """Init the class.

        Args:
            parent: The initializer for the parent QMainWindow.
        """
        super(ApplicationWindow, self).__init__(parent)
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


class Worker(QThread):
    """Worker Thread.

    Runs work method, and create signals:

    Finished.
        No data

    Error.
        tuple (exctype, value, traceback.format_exc() )

    Result.
        object data returned from processing, anything

    Progress.
        in indicating % progress

    Send_text.
        str send text to textBrowser
    """

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)
    send_text = Signal(str)

    def __init__(self, parent: Any = None) -> None:
        """Init the class.

        Args:
            parent: The initializer for the parent oject.
        """
        super(Worker, self).__init__(parent)

    def run(self) -> None:
        """Start work method and take care about run-time errors in thread."""
        result = self.work()
        self.result.emit(result)

    def work(self) -> None:
        """Emit program arguments as 'send_text' signal."""
        arguments = QCoreApplication.arguments()
        if len(arguments) > 1:
            for arg in arguments[1:]:
                self.send_text.emit(arg)


@click.command()
@click.version_option()
def main() -> None:
    """The Application main function."""
    app = QApplication(sys.argv)

    # QGuiApplication.setWindowIcon(QIcon("qrc:/icons/app.svg"))

    translator = QTranslator()
    translator.load("qrc:/translations/" + QLocale.system().name() + ".qm")
    QGuiApplication.installTranslator(translator)

    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(prog_name="jmbde-python")  # pragma: no cover
