# -*- coding: utf-8 -*-
################################################################################
# Form generated from reading UI file 'phoneinputarea.ui'
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


class Ui_PhoneInputArea(object):
    def setupUi(self, PhoneInputArea):
        if not PhoneInputArea.objectName():
            PhoneInputArea.setObjectName("PhoneInputArea")
        PhoneInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(PhoneInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayoutWidget = QWidget(PhoneInputArea)
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
        self.label_Department = QLabel(self.formLayoutWidget)
        self.label_Department.setObjectName("label_Department")

        self.gridLayout.addWidget(self.label_Department, 4, 0, 1, 1)

        self.label_Number = QLabel(self.formLayoutWidget)
        self.label_Number.setObjectName("label_Number")

        self.gridLayout.addWidget(self.label_Number, 1, 0, 1, 1)

        self.label_Place = QLabel(self.formLayoutWidget)
        self.label_Place.setObjectName("label_Place")
        self.label_Place.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_Place, 4, 2, 1, 1)

        self.comboBox_DeviceName = QComboBox(self.formLayoutWidget)
        self.comboBox_DeviceName.setObjectName("comboBox_DeviceName")

        self.gridLayout.addWidget(self.comboBox_DeviceName, 6, 1, 1, 1)

        self.label_Manufacturer = QLabel(self.formLayoutWidget)
        self.label_Manufacturer.setObjectName("label_Manufacturer")

        self.gridLayout.addWidget(self.label_Manufacturer, 8, 0, 1, 1)

        self.label_DeviceType = QLabel(self.formLayoutWidget)
        self.label_DeviceType.setObjectName("label_DeviceType")
        self.label_DeviceType.setAlignment(
            Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft
        )

        self.gridLayout.addWidget(self.label_DeviceType, 6, 2, 1, 1)

        self.lineEdit_SerialNumber = QLineEdit(self.formLayoutWidget)
        self.lineEdit_SerialNumber.setObjectName("lineEdit_SerialNumber")

        self.gridLayout.addWidget(self.lineEdit_SerialNumber, 2, 1, 1, 1)

        self.comboBox_DeviceType = QComboBox(self.formLayoutWidget)
        self.comboBox_DeviceType.setObjectName("comboBox_DeviceType")

        self.gridLayout.addWidget(self.comboBox_DeviceType, 6, 3, 1, 1)

        self.comboBox_Manufacturer = QComboBox(self.formLayoutWidget)
        self.comboBox_Manufacturer.setObjectName("comboBox_Manufacturer")

        self.gridLayout.addWidget(self.comboBox_Manufacturer, 8, 1, 1, 1)

        self.lineEdit_Pin = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Pin.setObjectName("lineEdit_Pin")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Pin.sizePolicy().hasHeightForWidth())
        self.lineEdit_Pin.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_Pin, 1, 3, 1, 1)

        self.label_Employee = QLabel(self.formLayoutWidget)
        self.label_Employee.setObjectName("label_Employee")
        self.label_Employee.setAlignment(
            Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft
        )

        self.gridLayout.addWidget(self.label_Employee, 3, 0, 1, 1)

        self.checkBox_Replace = QCheckBox(self.formLayoutWidget)
        self.checkBox_Replace.setObjectName("checkBox_Replace")

        self.gridLayout.addWidget(self.checkBox_Replace, 9, 1, 1, 1)

        self.lineEdit_Number = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Number.setObjectName("lineEdit_Number")
        sizePolicy.setHeightForWidth(
            self.lineEdit_Number.sizePolicy().hasHeightForWidth()
        )
        self.lineEdit_Number.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineEdit_Number, 1, 1, 1, 1)

        self.comboBox_Department = QComboBox(self.formLayoutWidget)
        self.comboBox_Department.setObjectName("comboBox_Department")

        self.gridLayout.addWidget(self.comboBox_Department, 4, 1, 1, 1)

        self.comboBox_Place = QComboBox(self.formLayoutWidget)
        self.comboBox_Place.setObjectName("comboBox_Place")

        self.gridLayout.addWidget(self.comboBox_Place, 4, 3, 1, 1)

        self.comboBox_Employee = QComboBox(self.formLayoutWidget)
        self.comboBox_Employee.setObjectName("comboBox_Employee")

        self.gridLayout.addWidget(self.comboBox_Employee, 3, 1, 1, 1)

        self.label_Pin = QLabel(self.formLayoutWidget)
        self.label_Pin.setObjectName("label_Pin")

        self.gridLayout.addWidget(self.label_Pin, 1, 2, 1, 1)

        self.label_DeviceName = QLabel(self.formLayoutWidget)
        self.label_DeviceName.setObjectName("label_DeviceName")
        self.label_DeviceName.setAlignment(
            Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft
        )

        self.gridLayout.addWidget(self.label_DeviceName, 6, 0, 1, 1)

        self.checkBox_Active = QCheckBox(self.formLayoutWidget)
        self.checkBox_Active.setObjectName("checkBox_Active")

        self.gridLayout.addWidget(self.checkBox_Active, 9, 0, 1, 1)

        self.label_Inventory = QLabel(self.formLayoutWidget)
        self.label_Inventory.setObjectName("label_Inventory")

        self.gridLayout.addWidget(self.label_Inventory, 8, 2, 1, 1)

        self.comboBox_Inventory = QComboBox(self.formLayoutWidget)
        self.comboBox_Inventory.setObjectName("comboBox_Inventory")

        self.gridLayout.addWidget(self.comboBox_Inventory, 8, 3, 1, 1)

        self.label_SerialNumber = QLabel(self.formLayoutWidget)
        self.label_SerialNumber.setObjectName("label_SerialNumber")

        self.gridLayout.addWidget(self.label_SerialNumber, 2, 0, 1, 1)

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
        self.label_Department.setBuddy(self.comboBox_Department)
        self.label_Number.setBuddy(self.lineEdit_Number)
        self.label_Place.setBuddy(self.comboBox_Place)
        self.label_Manufacturer.setBuddy(self.comboBox_Manufacturer)
        self.label_DeviceType.setBuddy(self.comboBox_DeviceType)
        self.label_Employee.setBuddy(self.comboBox_Employee)
        self.label_Pin.setBuddy(self.lineEdit_Pin)
        self.label_DeviceName.setBuddy(self.comboBox_DeviceName)
        self.label_Inventory.setBuddy(self.comboBox_Inventory)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.pushButton_Add, self.pushButton_EditFinish)

        self.retranslateUi(PhoneInputArea)

        QMetaObject.connectSlotsByName(PhoneInputArea)

    # setupUi

    def retranslateUi(self, PhoneInputArea):
        PhoneInputArea.setWindowTitle(
            QCoreApplication.translate("PhoneInputArea", "Phone", None)
        )
        # if QT_CONFIG(accessibility)
        PhoneInputArea.setAccessibleName(
            QCoreApplication.translate("PhoneInputArea", "PhoneInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        PhoneInputArea.setTitle(
            QCoreApplication.translate("PhoneInputArea", "Phone", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("PhoneInputArea", "Phone", None)
        )
        self.label_Department.setText(
            QCoreApplication.translate("PhoneInputArea", "Department", None)
        )
        self.label_Number.setText(
            QCoreApplication.translate("PhoneInputArea", "Number", None)
        )
        self.label_Place.setText(
            QCoreApplication.translate("PhoneInputArea", "Place", None)
        )
        self.label_Manufacturer.setText(
            QCoreApplication.translate("PhoneInputArea", "Manufacturer", None)
        )
        self.label_DeviceType.setText(
            QCoreApplication.translate("PhoneInputArea", "Devicetype", None)
        )
        self.label_Employee.setText(
            QCoreApplication.translate("PhoneInputArea", "Employee", None)
        )
        self.checkBox_Replace.setText(
            QCoreApplication.translate("PhoneInputArea", "Replace", None)
        )
        self.label_Pin.setText(
            QCoreApplication.translate("PhoneInputArea", "Pin", None)
        )
        self.label_DeviceName.setText(
            QCoreApplication.translate("PhoneInputArea", "Devicename", None)
        )
        self.checkBox_Active.setText(
            QCoreApplication.translate("PhoneInputArea", "Active", None)
        )
        self.label_Inventory.setText(
            QCoreApplication.translate("PhoneInputArea", "Inventory", None)
        )
        self.label_SerialNumber.setText(
            QCoreApplication.translate("PhoneInputArea", "Serial Number", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("PhoneInputArea", "+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("PhoneInputArea", "Edit", None)
        )

    # retranslateUi
