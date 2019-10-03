#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    JMBDe app.
"""

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

import sys
import os
import versioneer
import configparser


from PySide2 import QtGui, QtCore
from PySide2.QtCore import QTranslator, QLocale, Qt
from PySide2.QtWidgets import QMainWindow, QApplication, QSystemTrayIcon, QMenu
from PySide2.QtGui import QGuiApplication, QColor, QIcon

from jmbde.views.ui_mainwindow import Ui_MainWindow

from .logger import Logger


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.green_color = None
        self.yellow_color = None
        self.red_color = None
        self.tray = QSystemTrayIcon(self)

        self.config_filename = None
        self.base_output_filename = None

        self.log = Logger().create_log()
        self.log.info(self.translate("Launched jmbde"))

        self.set_application_constants()
        self.setup_ui()
        self.connect_ui_to_functions()

        QApplication.instance().aboutToQuit.connect(self.prepare_to_exit)
        self.show()

    def set_application_constants(self):

        if sys.platform == "darwin":
            QGuiApplication.setAttribute(Qt.AA_DontShowIconsInMenus)

        QtCore.QCoreApplication.setApplicationName("jmbde")
        #  QtCore.QCoreApplication.setOrgnizationName("jmbde")
        # QtCore.QCoreApplication.setOrginazationDomain("io.jmuelbert.github")
        QtCore.QCoreApplication.setApplicationVersion(versioneer.get_version())

        self.log.info("Set Appname to: " + QtCore.QCoreApplication.applicationName())

        QGuiApplication.setWindowIcon(QIcon(":/icons/app.svg"))

        # f = QFile(":/style.qss")
        # f.open(QFile.ReadOnly | QFile.Text)
        # QApplication.setStyleSheet(QTextStream(f).readAll())
        # f.close()

        translator = QTranslator()
        translator.load(":/translations/" + QLocale.system().name() + ".qm")
        QApplication.installTranslator(translator)

    def setup_ui(self):
        self.setupUi(self)
        self.setup_colors()
        self.setup_tray_icon()
        self.setup_last_used_settings()

    def setup_colors(self):
        green = QColor(55, 195, 58)
        palette_green = QtGui.QPalette()
        palette_green.setColor(QtGui.QPalette.Text, green)
        palette_green.setColor(QtGui.QPalette.Foreground, green)
        self.green_color = palette_green

        yellow = QColor(244, 212, 66)
        palette_yellow = QtGui.QPalette()
        palette_yellow.setColor(QtGui.QPalette.Text, yellow)
        palette_yellow.setColor(QtGui.QPalette.Foreground, yellow)
        self.yellow_color = palette_yellow

        red = QColor(242, 86, 77)
        palette_red = QtGui.QPalette()
        palette_red.setColor(QtGui.QPalette.Text, red)
        palette_red.setColor(QtGui.QPalette.Foreground, red)
        self.red_color = palette_red

    def setup_tray_icon(self):
        if self.tray.isSystemTrayAvailable():
            self.tray.setIcon(QIcon("assets/icon_256.png"))
            menu = QMenu()
            action_quit = menu.addAction("Quit")
            action_quit.triggered.connect(self.close)

            self.tray.setContextMenu(menu)
            self.tray.show()
        else:
            self.tray = None

    def connect_ui_to_functions(self):
        pass

    def write_gui_config_options_to_config_file(self):
        config = configparser.ConfigParser()
        config.read(self.config_filename)

        # config.set('cat', 'setting', value)

        with open(
            os.path.join(os.path.expanduser("~"), "jmbde", "input_properties.cfg"), "w"
        ) as configfile:
            config.write(configfile)
        self.log.info("Updated input_properties.cfg file with new settings.")

    def setup_last_used_settings(self):
        config = configparser.ConfigParser()
        self.config_filename = os.path.join(
            os.path.expanduser("~"), "jmbde", "input_properties.cfg"
        )
        if self.need_new_config_file(config):
            self.log.info(
                "No input_properties.cfg file found. Creating the default one."
            )
            self.write_default_config()

        config.read(self.config_filename)
        self.set_instance_variables_from_config(config)

    def need_new_config_file(self, config):
        if not os.path.isfile(self.config_filename):
            return True
        if os.stat(self.config_filename).st_size == 0:
            return True

        try:
            config.read(self.config_filename)
        except configparser.MissingSectionHeaderError:
            return True

        # if not config.has_option('input_properties', 'serial_port'):
        #    return True

    def write_default_config(self):
        with open(self.config_filename, "w") as config_file:
            print("[input_properties]", file=config_file)

    def set_instance_variables_from_config(self, config):
        pass
        # self.tabWidget_serialIp.setCurrentIndex(1)  # TODO: Make this an actual config parameter

    @staticmethod
    def str2bool(bool_string):
        if bool_string == "True":
            return True
        if bool_string == "False":
            return False
        raise ValueError(
            'Can only accept exact strings "True" or "False". Was passed {}'.format(
                bool_string
            )
        )

    def prepare_to_exit(self):
        self.log.info("About to quit.")
        # self.upload_data()  # Only occurs if forward data is toggled on
        self.log.info("Closing jmbde.")


def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.setWindowTitle = "Test"
    ret = app.exec_()
    sys.exit(ret)


if __name__ == "__main__":
    main()
