# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employeetable.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QHeaderView,
    QSizePolicy,
    QTableView,
    QVBoxLayout,
    QWidget,
)


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