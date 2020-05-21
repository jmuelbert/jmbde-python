# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'csvimportdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_CsvImportDialog(object):
    def setupUi(self, CsvImportDialog):
        if not CsvImportDialog.objectName():
            CsvImportDialog.setObjectName(u"CsvImportDialog")
        CsvImportDialog.resize(671, 318)
        CsvImportDialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(CsvImportDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(CsvImportDialog)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.buttonBox = QDialogButtonBox(CsvImportDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(CsvImportDialog)
        self.buttonBox.accepted.connect(CsvImportDialog.accept)
        self.buttonBox.rejected.connect(CsvImportDialog.reject)

        QMetaObject.connectSlotsByName(CsvImportDialog)
    # setupUi

    def retranslateUi(self, CsvImportDialog):
        CsvImportDialog.setWindowTitle(QCoreApplication.translate("CsvImportDialog", u"CSV Import", None))
    # retranslateUi

