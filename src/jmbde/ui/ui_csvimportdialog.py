# -*- coding: utf-8 -*-
################################################################################
# Form generated from reading UI file 'csvimportdialog.ui'
##
# Created by: Qt User Interface Compiler version 5.15.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *


class Ui_CsvImportDialog(object):
    def setupUi(self, CsvImportDialog):
        if not CsvImportDialog.objectName():
            CsvImportDialog.setObjectName("CsvImportDialog")
        CsvImportDialog.resize(671, 318)
        CsvImportDialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(CsvImportDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QTableView(CsvImportDialog)
        self.tableView.setObjectName("tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.buttonBox = QDialogButtonBox(CsvImportDialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CsvImportDialog)
        self.buttonBox.accepted.connect(CsvImportDialog.accept)
        self.buttonBox.rejected.connect(CsvImportDialog.reject)

        QMetaObject.connectSlotsByName(CsvImportDialog)

    # setupUi

    def retranslateUi(self, CsvImportDialog):
        CsvImportDialog.setWindowTitle(
            QCoreApplication.translate("CsvImportDialog", "CSV Import", None)
        )

    # retranslateUi
