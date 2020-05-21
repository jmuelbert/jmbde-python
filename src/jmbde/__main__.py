#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    JMBDe app.
"""
# Standard library imports
#
# Copyright (c) 2019 Jürgen Mülbert. All rights reserved.
#
# Licensed under the EUPL, Version 1.2 or – as soon they
# will be approved by the European Commission - subsequent
# versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the
# Licence.
# You may obtain a copy of the Licence at:
#
# https://joinup.ec.europa.eu/page/eupl-text-11-12
#
# Unless required by applicable law or agreed to in
# writing, software distributed under the Licence is
# distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.
# See the Licence for the specific language governing
# permissions and limitations under the Licence.
#
# Lizenziert unter der EUPL, Version 1.2 oder - sobald
#  diese von der Europäischen Kommission genehmigt wurden -
# Folgeversionen der EUPL ("Lizenz");
# Sie dürfen dieses Werk ausschließlich gemäß
# dieser Lizenz nutzen.
# Eine Kopie der Lizenz finden Sie hier:
#
# https://joinup.ec.europa.eu/page/eupl-text-11-12
#
# Sofern nicht durch anwendbare Rechtsvorschriften
# gefordert oder in schriftlicher Form vereinbart, wird
# die unter der Lizenz verbreitete Software "so wie sie
# ist", OHNE JEGLICHE GEWÄHRLEISTUNG ODER BEDINGUNGEN -
# ausdrücklich oder stillschweigend - verbreitet.
# Die sprachspezifischen Genehmigungen und Beschränkungen
# unter der Lizenz sind dem Lizenztext zu entnehmen.
#
import configparser
import os
import sys

from PySide2 import QtCore
from PySide2.QtCore import QLocale
from PySide2.QtCore import Qt
from PySide2.QtCore import QTranslator

from PySide2.QtGui import QGuiApplication
from PySide2.QtGui import QIcon
from PySide2.QtQml import QQmlApplicationEngine

from .rcs import *

from jmbde.models.datacontext import DataContext
from jmbde.models.employee import EmployeeModel
from .logger import Logger
# Third party imports


class MainWindow():
    def __init__(self) -> None:
        # super(MainWindow, self).__init__()

        self.config_filename = None
        self.base_output_filename = None

        self.log = Logger().create_log()
        self.log.info("Launched jmbde")

        self.set_application_constants()

    def set_application_constants(self) -> None:
        if sys.platform == "darwin":
            QGuiApplication.setAttribute(Qt.AA_DontShowIconsInMenus)

        QtCore.QCoreApplication.setApplicationName("jmbde")
        QtCore.QCoreApplication.setOrganizationName("io.jmuelbert.github")
        QtCore.QCoreApplication.setOrganizationDomain("Jürgen Mülbert")
        QtCore.QCoreApplication.setApplicationVersion("0.4.0")

        self.log.info("Set Appname to: {}".format(
                      QtCore.QCoreApplication.applicationName()))

        QGuiApplication.setWindowIcon(QIcon(":/icons/app.svg"))

        translator = QTranslator()
        translator.load(":/translations/" + QLocale.system().name() + ".qm")
        QGuiApplication.installTranslator(translator)


def main() -> None:
    app = QGuiApplication(sys.argv)
    mainWin = MainWindow()

    engine = QQmlApplicationEngine()

    # Export pertinent objects to QML
    engine.rootContext().setContextProperty("employee_model", EmployeeModel)
    engine.load(":/qml/main.qml")
    dc = DataContext()
    dc.createConnection()
    ret = app.exec_()
    sys.exit(ret)


if __name__ == "__main__":
    main()
