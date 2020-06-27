# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'employeetable.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import QCoreApplication
from PySide2.QtCore import QDate
from PySide2.QtCore import QDateTime
from PySide2.QtCore import QMetaObject
from PySide2.QtCore import QObject
from PySide2.QtCore import QPoint
from PySide2.QtCore import QRect
from PySide2.QtCore import QSize
from PySide2.QtCore import Qt
from PySide2.QtCore import QTime
from PySide2.QtCore import QUrl
from PySide2.QtGui import QBrush
from PySide2.QtGui import QColor
from PySide2.QtGui import QConicalGradient
from PySide2.QtGui import QCursor
from PySide2.QtGui import QFont
from PySide2.QtGui import QFontDatabase
from PySide2.QtGui import QIcon
from PySide2.QtGui import QKeySequence
from PySide2.QtGui import QLinearGradient
from PySide2.QtGui import QPainter
from PySide2.QtGui import QPalette
from PySide2.QtGui import QPixmap
from PySide2.QtGui import QRadialGradient
from PySide2.QtWidgets import *


class Ui_EmployeeTable(object):
    def setupUi(self, EmployeeTable):
        if not EmployeeTable.objectName():
            EmployeeTable.setObjectName(u"EmployeeTable")
        EmployeeTable.resize(765, 596)
        self.verticalLayoutWidget = QWidget(EmployeeTable)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 751, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.tableView = QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName(u"tableView")
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
            QCoreApplication.translate("EmployeeTable", u"Form", None)
        )

    # retranslateUi
