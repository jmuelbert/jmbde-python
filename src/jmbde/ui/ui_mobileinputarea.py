# -*- coding: utf-8 -*-
################################################################################
# Form generated from reading UI file 'mobileinputarea.ui'
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


class Ui_MobileInputArea(object):
    def setupUi(self, MobileInputArea):
        if not MobileInputArea.objectName():
            MobileInputArea.setObjectName("MobileInputArea")
        MobileInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(MobileInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayoutWidget = QWidget(MobileInputArea)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Header = QLabel(self.formLayoutWidget)
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
        self.comboBox_Place = QComboBox(self.formLayoutWidget)
        self.comboBox_Place.setObjectName("comboBox_Place")

        self.gridLayout.addWidget(self.comboBox_Place, 3, 5, 1, 1)

        self.label_DeviceName = QLabel(self.formLayoutWidget)
        self.label_DeviceName.setObjectName("label_DeviceName")

        self.gridLayout.addWidget(self.label_DeviceName, 4, 0, 1, 1)

        self.label_Department = QLabel(self.formLayoutWidget)
        self.label_Department.setObjectName("label_Department")

        self.gridLayout.addWidget(self.label_Department, 3, 0, 1, 1)

        self.lineEdit_CardNumber = QLineEdit(self.formLayoutWidget)
        self.lineEdit_CardNumber.setObjectName("lineEdit_CardNumber")

        self.gridLayout.addWidget(self.lineEdit_CardNumber, 1, 5, 1, 1)

        self.label_Inventory = QLabel(self.formLayoutWidget)
        self.label_Inventory.setObjectName("label_Inventory")

        self.gridLayout.addWidget(self.label_Inventory, 5, 3, 1, 1)

        self.comboBox_Department = QComboBox(self.formLayoutWidget)
        self.comboBox_Department.setObjectName("comboBox_Department")

        self.gridLayout.addWidget(self.comboBox_Department, 3, 2, 1, 1)

        self.label_Employee = QLabel(self.formLayoutWidget)
        self.label_Employee.setObjectName("label_Employee")

        self.gridLayout.addWidget(self.label_Employee, 2, 0, 1, 1)

        self.label_Manufacturer = QLabel(self.formLayoutWidget)
        self.label_Manufacturer.setObjectName("label_Manufacturer")

        self.gridLayout.addWidget(self.label_Manufacturer, 5, 0, 1, 1)

        self.lineEdit_Pin = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Pin.setObjectName("lineEdit_Pin")
        self.lineEdit_Pin.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_Pin, 0, 5, 1, 1)

        self.checkBox_Replace = QCheckBox(self.formLayoutWidget)
        self.checkBox_Replace.setObjectName("checkBox_Replace")

        self.gridLayout.addWidget(self.checkBox_Replace, 6, 2, 1, 1)

        self.label_Place = QLabel(self.formLayoutWidget)
        self.label_Place.setObjectName("label_Place")

        self.gridLayout.addWidget(self.label_Place, 3, 3, 1, 1)

        self.label_CardNumber = QLabel(self.formLayoutWidget)
        self.label_CardNumber.setObjectName("label_CardNumber")

        self.gridLayout.addWidget(self.label_CardNumber, 1, 3, 1, 1)

        self.lineEdit_Number = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Number.setObjectName("lineEdit_Number")

        self.gridLayout.addWidget(self.lineEdit_Number, 0, 2, 1, 1)

        self.label_Pin = QLabel(self.formLayoutWidget)
        self.label_Pin.setObjectName("label_Pin")

        self.gridLayout.addWidget(self.label_Pin, 0, 3, 1, 1)

        self.label_DeviceType = QLabel(self.formLayoutWidget)
        self.label_DeviceType.setObjectName("label_DeviceType")

        self.gridLayout.addWidget(self.label_DeviceType, 4, 3, 1, 1)

        self.comboBox_DeviceType = QComboBox(self.formLayoutWidget)
        self.comboBox_DeviceType.setObjectName("comboBox_DeviceType")

        self.gridLayout.addWidget(self.comboBox_DeviceType, 4, 5, 1, 1)

        self.checkBox_Active = QCheckBox(self.formLayoutWidget)
        self.checkBox_Active.setObjectName("checkBox_Active")

        self.gridLayout.addWidget(self.checkBox_Active, 6, 0, 1, 1)

        self.label_SerialNumber = QLabel(self.formLayoutWidget)
        self.label_SerialNumber.setObjectName("label_SerialNumber")

        self.gridLayout.addWidget(self.label_SerialNumber, 1, 0, 1, 1)

        self.comboBox_Manufacturer = QComboBox(self.formLayoutWidget)
        self.comboBox_Manufacturer.setObjectName("comboBox_Manufacturer")

        self.gridLayout.addWidget(self.comboBox_Manufacturer, 5, 2, 1, 1)

        self.label_Number = QLabel(self.formLayoutWidget)
        self.label_Number.setObjectName("label_Number")

        self.gridLayout.addWidget(self.label_Number, 0, 0, 1, 1)

        self.comboBox_DeviceName = QComboBox(self.formLayoutWidget)
        self.comboBox_DeviceName.setObjectName("comboBox_DeviceName")

        self.gridLayout.addWidget(self.comboBox_DeviceName, 4, 2, 1, 1)

        self.lineEdit_SerialNumber = QLineEdit(self.formLayoutWidget)
        self.lineEdit_SerialNumber.setObjectName("lineEdit_SerialNumber")

        self.gridLayout.addWidget(self.lineEdit_SerialNumber, 1, 2, 1, 1)

        self.comboBox_Employee = QComboBox(self.formLayoutWidget)
        self.comboBox_Employee.setObjectName("comboBox_Employee")

        self.gridLayout.addWidget(self.comboBox_Employee, 2, 2, 1, 1)

        self.comboBox_Inventory = QComboBox(self.formLayoutWidget)
        self.comboBox_Inventory.setObjectName("comboBox_Inventory")

        self.gridLayout.addWidget(self.comboBox_Inventory, 5, 5, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Add = QPushButton(self.formLayoutWidget)
        self.pushButton_Add.setObjectName("pushButton_Add")

        self.horizontalLayout.addWidget(self.pushButton_Add)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_EditFinish = QPushButton(self.formLayoutWidget)
        self.pushButton_EditFinish.setObjectName("pushButton_EditFinish")

        self.horizontalLayout.addWidget(self.pushButton_EditFinish)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addWidget(self.formLayoutWidget)

        # if QT_CONFIG(shortcut)
        self.label_DeviceName.setBuddy(self.comboBox_DeviceName)
        self.label_Department.setBuddy(self.comboBox_Department)
        self.label_Inventory.setBuddy(self.comboBox_Inventory)
        self.label_Employee.setBuddy(self.comboBox_Employee)
        self.label_Manufacturer.setBuddy(self.comboBox_Manufacturer)
        self.label_Place.setBuddy(self.comboBox_Place)
        self.label_CardNumber.setBuddy(self.lineEdit_CardNumber)
        self.label_Pin.setBuddy(self.lineEdit_Pin)
        self.label_DeviceType.setBuddy(self.comboBox_DeviceType)
        self.label_SerialNumber.setBuddy(self.lineEdit_SerialNumber)
        self.label_Number.setBuddy(self.lineEdit_Number)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_Number, self.lineEdit_Pin)
        QWidget.setTabOrder(self.lineEdit_Pin, self.lineEdit_SerialNumber)
        QWidget.setTabOrder(self.lineEdit_SerialNumber, self.lineEdit_CardNumber)
        QWidget.setTabOrder(self.lineEdit_CardNumber, self.comboBox_Employee)
        QWidget.setTabOrder(self.comboBox_Employee, self.comboBox_Department)
        QWidget.setTabOrder(self.comboBox_Department, self.comboBox_Place)
        QWidget.setTabOrder(self.comboBox_Place, self.comboBox_DeviceName)
        QWidget.setTabOrder(self.comboBox_DeviceName, self.comboBox_DeviceType)
        QWidget.setTabOrder(self.comboBox_DeviceType, self.comboBox_Manufacturer)
        QWidget.setTabOrder(self.comboBox_Manufacturer, self.comboBox_Inventory)
        QWidget.setTabOrder(self.comboBox_Inventory, self.checkBox_Active)
        QWidget.setTabOrder(self.checkBox_Active, self.checkBox_Replace)
        QWidget.setTabOrder(self.checkBox_Replace, self.pushButton_Add)
        QWidget.setTabOrder(self.pushButton_Add, self.pushButton_EditFinish)

        self.retranslateUi(MobileInputArea)

        QMetaObject.connectSlotsByName(MobileInputArea)

    # setupUi

    def retranslateUi(self, MobileInputArea):
        MobileInputArea.setWindowTitle(
            QCoreApplication.translate("MobileInputArea", "Mobile", None)
        )
        # if QT_CONFIG(accessibility)
        MobileInputArea.setAccessibleName(
            QCoreApplication.translate("MobileInputArea", "MobileInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        MobileInputArea.setTitle(
            QCoreApplication.translate("MobileInputArea", "Mobile", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("MobileInputArea", "Mobile", None)
        )
        self.label_DeviceName.setText(
            QCoreApplication.translate("MobileInputArea", "Devicename", None)
        )
        self.label_Department.setText(
            QCoreApplication.translate("MobileInputArea", "Department", None)
        )
        self.label_Inventory.setText(
            QCoreApplication.translate("MobileInputArea", "Inventory", None)
        )
        self.label_Employee.setText(
            QCoreApplication.translate("MobileInputArea", "Employee", None)
        )
        self.label_Manufacturer.setText(
            QCoreApplication.translate("MobileInputArea", "Manufacturer", None)
        )
        self.checkBox_Replace.setText(
            QCoreApplication.translate("MobileInputArea", "Replace", None)
        )
        self.label_Place.setText(
            QCoreApplication.translate("MobileInputArea", "Place", None)
        )
        self.label_CardNumber.setText(
            QCoreApplication.translate("MobileInputArea", "Card Number", None)
        )
        self.label_Pin.setText(
            QCoreApplication.translate("MobileInputArea", "Pin", None)
        )
        self.label_DeviceType.setText(
            QCoreApplication.translate("MobileInputArea", "Devicetype", None)
        )
        self.checkBox_Active.setText(
            QCoreApplication.translate("MobileInputArea", "Active", None)
        )
        self.label_SerialNumber.setText(
            QCoreApplication.translate("MobileInputArea", "Serial Number", None)
        )
        self.label_Number.setText(
            QCoreApplication.translate("MobileInputArea", "Number", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("MobileInputArea", "+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("MobileInputArea", "Edit", None)
        )

    # retranslateUi
