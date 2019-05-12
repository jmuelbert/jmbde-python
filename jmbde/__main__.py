#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    JMBDe app

Copyright (c) 2019 Jürgen Mülbert. All rights reserved.

Licensed under the EUPL, Version 1.2 or – as soon they
will be approved by the European Commission - subsequent
versions of the EUPL (the "Licence");
You may not use this work except in compliance with the
Licence.
You may obtain a copy of the Licence at:

https://joinup.ec.europa.eu/page/eupl-text-11-12

Unless required by applicable law or agreed to in
writing, software distributed under the Licence is
distributed on an "AS IS" basis,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied.
See the Licence for the specific language governing
permissions and limitations under the Licence.

Lizenziert unter der EUPL, Version 1.2 oder - sobald
diese von der Europäischen Kommission genehmigt wurden -
Folgeversionen der EUPL ("Lizenz");
Sie dürfen dieses Werk ausschließlich gemäß
dieser Lizenz nutzen.
Eine Kopie der Lizenz finden Sie hier:

https://joinup.ec.europa.eu/page/eupl-text-11-12

Sofern nicht durch anwendbare Rechtsvorschriften
gefordert oder in schriftlicher Form vereinbart, wird
die unter der Lizenz verbreitete Software "so wie sie
ist", OHNE JEGLICHE GEWÄHRLEISTUNG ODER BEDINGUNGEN -
ausdrücklich oder stillschweigend - verbreitet.
Die sprachspezifischen Genehmigungen und Beschränkungen
unter der Lizenz sind dem Lizenztext zu entnehmen.

"""

import sys

from PySide2 import QtCore
from PySide2.QtGui import QGuiApplication, QFontDatabase, QFont, QIcon
from PySide2.QtCore import QFile, QTextStream, QTranslator, QLocale, Qt
from PySide2.QtWidgets import QApplication

from .views.MainWindow import MainWindow

from . import resources_rc  # noqa


def setApplicationConstants(app):
    QGuiApplication.setApplicationDisplayName("jmbde")

    if sys.platform == 'darwin':
        app.setAttribute(Qt.AA_DontShowIconsInMenus)

    QtCore.QCoreApplication.setApplicationName("JMBde")

    print(QtCore.QCoreApplication.applicationName())


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(':/icons/app.svg'))
    setApplicationConstants(app)

    fontDB = QFontDatabase()
    fontDB.addApplicationFont(':/fonts/Roboto-Regular.ttf')
    app.setFont(QFont('Roboto'))

    f = QFile(':/style.qss')
    f.open(QFile.ReadOnly | QFile.Text)
    app.setStyleSheet(QTextStream(f).readAll())
    f.close()

    translator = QTranslator()
    translator.load(':/translations/' + QLocale.system().name() + '.qm')
    app.installTranslator(translator)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
