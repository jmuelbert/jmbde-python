# -*- coding: utf-8 -*-
################################################################################
# Form generated from reading UI file 'employeetable.ui'
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


class Ui_EmployeeTable(object):
    def setupUi(self, EmployeeTable):
        if not EmployeeTable.objectName():
            EmployeeTable.setObjectName("EmployeeTable")
        EmployeeTable.resize(765, 596)
        self.verticalLayoutWidget = QWidget(EmployeeTable)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 751, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.tableView = QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setVisible(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(EmployeeTable)

        QMetaObject.connectSlotsByName(EmployeeTable)

    # setupUi

    def retranslateUi(self, EmployeeTable):
        EmployeeTable.setWindowTitle(
            QCoreApplication.translate("EmployeeTable", "Form", None)
        )

    # retranslateUi
