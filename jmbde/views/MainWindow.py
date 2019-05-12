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


from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import QCoreApplication, QObject, QModelIndex
from PySide2.QtWidgets import QMainWindow


from .mainwindow_ui import Ui_MainWindow


class Model(QStandardItemModel):
    """
     [{"type":str, "objects":[str, ...]}, ...]
    """

    def __init__(self, data):
        QStandardItemModel.__init__(self)
        self._data = data
        for j, d in enumerate(data):
            item = QStandardItem(d["type"])
            for obj in d["objects"]:
                child = QStandardItem(obj)
                if d["picture"] != '':
                    child.setData(d["picture"], QtCore.Qt.DecorationRole)
                item.appendRow(child)
            self.setItem(j, 0, item)

    def data(self, QModelIndex, role=None):
        # item Data
        data = self.itemData(QModelIndex)

        if role == QtCore.Qt.DisplayRole:
            ret = data[role]
        elif role in data and role == QtCore.Qt.DecorationRole:
            ret = QPixmap(data[role]).scaledToHeight(25)
        else:
            ret = None
        return ret


class MainWindow(QMainWindow):
    """ Main Window """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.readSettings()
        self.initOutLine()

    def readSettings(self):
        pass

    def writeSettings(self):
        pass

    def initOutLine(self):
        obj = QObject()
        outline = [
            {"type": QCoreApplication.translate("app", "Person"),
             "objects": [
                QCoreApplication.translate("app", "Employee"), QCoreApplication.translate("app", "Function"), QCoreApplication.translate("app", "Department"), QCoreApplication.translate("app", "Title")],
             "picture": ""},
            {"type": QCoreApplication.translate("app", "Device"),
             "objects": [
                QCoreApplication.translate(
                    "app", "Computer"), QCoreApplication.translate("app", "Processor"),
                QCoreApplication.translate("app", "Operation System"), QCoreApplication.translate("app", "Software"), QCoreApplication.translate("app", "Printer")],
             "picture": ''},
            {"type": QCoreApplication.translate("app", "Communication"),
             "objects": [QCoreApplication.translate("app", "Phone"), QCoreApplication.translate("app", "Mobile")],
             "picture": ''},
            {"type": QCoreApplication.translate("app", "Misc"),
             "objects": [QCoreApplication.translate("app", "Manufacturer"),
                         QCoreApplication.translate("app", "City"), QCoreApplication.translate("app", "Chipcard")],
             "picture": ''}
        ]

        model = Model(outline)
        self.ui.treeView.setModel(model)
        self.ui.treeView.expandAll()
        self.ui.treeView.clicked.connect(self.test)

    def test(self, selected):
        index = QModelIndex(selected)
        print("hello!")
        print(selected)
        print(index.data())
