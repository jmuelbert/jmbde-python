# -*- coding: utf-8 -*-
################################################################################
# Form generated from reading UI file 'cityinputarea.ui'
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


class Ui_CityInputArea(object):
    def setupUi(self, CityInputArea):
        if not CityInputArea.objectName():
            CityInputArea.setObjectName("CityInputArea")
        CityInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(CityInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.GroupBox = QWidget(CityInputArea)
        self.GroupBox.setObjectName("GroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.GroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Header = QLabel(self.GroupBox)
        self.label_Header.setObjectName("label_Header")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Header.setFont(font)
        self.label_Header.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Header)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_CityName = QLineEdit(self.GroupBox)
        self.lineEdit_CityName.setObjectName("lineEdit_CityName")

        self.gridLayout.addWidget(self.lineEdit_CityName, 2, 1, 1, 1)

        self.label_ZipCode = QLabel(self.GroupBox)
        self.label_ZipCode.setObjectName("label_ZipCode")

        self.gridLayout.addWidget(self.label_ZipCode, 1, 0, 1, 1)

        self.comboBox_ZipCode = QComboBox(self.GroupBox)
        self.comboBox_ZipCode.setObjectName("comboBox_ZipCode")

        self.gridLayout.addWidget(self.comboBox_ZipCode, 1, 1, 1, 1)

        self.label_CityName = QLabel(self.GroupBox)
        self.label_CityName.setObjectName("label_CityName")

        self.gridLayout.addWidget(self.label_CityName, 2, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Add = QPushButton(self.GroupBox)
        self.pushButton_Add.setObjectName("pushButton_Add")

        self.horizontalLayout.addWidget(self.pushButton_Add)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_EditFinish = QPushButton(self.GroupBox)
        self.pushButton_EditFinish.setObjectName("pushButton_EditFinish")

        self.horizontalLayout.addWidget(self.pushButton_EditFinish)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addWidget(self.GroupBox)

        self.retranslateUi(CityInputArea)

        QMetaObject.connectSlotsByName(CityInputArea)

    # setupUi

    def retranslateUi(self, CityInputArea):
        CityInputArea.setWindowTitle(
            QCoreApplication.translate("CityInputArea", "City", None)
        )
        # if QT_CONFIG(accessibility)
        CityInputArea.setAccessibleName(
            QCoreApplication.translate("CityInputArea", "CityInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        CityInputArea.setTitle(
            QCoreApplication.translate("CityInputArea", "City", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("CityInputArea", "City", None)
        )
        self.label_ZipCode.setText(
            QCoreApplication.translate("CityInputArea", "Zip Code", None)
        )
        self.label_CityName.setText(
            QCoreApplication.translate("CityInputArea", "City Name", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("CityInputArea", "+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("CityInputArea", "Edit", None)
        )

    # retranslateUi
