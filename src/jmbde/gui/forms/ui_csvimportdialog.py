# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'csvimportdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHeaderView, QSizePolicy, QTableView, QVBoxLayout)

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

