# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'mobileinputarea.ui'
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


class Ui_MobileInputArea(object):
    def setupUi(self, MobileInputArea):
        if not MobileInputArea.objectName():
            MobileInputArea.setObjectName(u"MobileInputArea")
        MobileInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(MobileInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayoutWidget = QWidget(MobileInputArea)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Header = QLabel(self.formLayoutWidget)
        self.label_Header.setObjectName(u"label_Header")
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
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_Place = QComboBox(self.formLayoutWidget)
        self.comboBox_Place.setObjectName(u"comboBox_Place")

        self.gridLayout.addWidget(self.comboBox_Place, 3, 5, 1, 1)

        self.label_DeviceName = QLabel(self.formLayoutWidget)
        self.label_DeviceName.setObjectName(u"label_DeviceName")

        self.gridLayout.addWidget(self.label_DeviceName, 4, 0, 1, 1)

        self.label_Department = QLabel(self.formLayoutWidget)
        self.label_Department.setObjectName(u"label_Department")

        self.gridLayout.addWidget(self.label_Department, 3, 0, 1, 1)

        self.lineEdit_CardNumber = QLineEdit(self.formLayoutWidget)
        self.lineEdit_CardNumber.setObjectName(u"lineEdit_CardNumber")

        self.gridLayout.addWidget(self.lineEdit_CardNumber, 1, 5, 1, 1)

        self.label_Inventory = QLabel(self.formLayoutWidget)
        self.label_Inventory.setObjectName(u"label_Inventory")

        self.gridLayout.addWidget(self.label_Inventory, 5, 3, 1, 1)

        self.comboBox_Department = QComboBox(self.formLayoutWidget)
        self.comboBox_Department.setObjectName(u"comboBox_Department")

        self.gridLayout.addWidget(self.comboBox_Department, 3, 2, 1, 1)

        self.label_Employee = QLabel(self.formLayoutWidget)
        self.label_Employee.setObjectName(u"label_Employee")

        self.gridLayout.addWidget(self.label_Employee, 2, 0, 1, 1)

        self.label_Manufacturer = QLabel(self.formLayoutWidget)
        self.label_Manufacturer.setObjectName(u"label_Manufacturer")

        self.gridLayout.addWidget(self.label_Manufacturer, 5, 0, 1, 1)

        self.lineEdit_Pin = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Pin.setObjectName(u"lineEdit_Pin")
        self.lineEdit_Pin.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_Pin, 0, 5, 1, 1)

        self.checkBox_Replace = QCheckBox(self.formLayoutWidget)
        self.checkBox_Replace.setObjectName(u"checkBox_Replace")

        self.gridLayout.addWidget(self.checkBox_Replace, 6, 2, 1, 1)

        self.label_Place = QLabel(self.formLayoutWidget)
        self.label_Place.setObjectName(u"label_Place")

        self.gridLayout.addWidget(self.label_Place, 3, 3, 1, 1)

        self.label_CardNumber = QLabel(self.formLayoutWidget)
        self.label_CardNumber.setObjectName(u"label_CardNumber")

        self.gridLayout.addWidget(self.label_CardNumber, 1, 3, 1, 1)

        self.lineEdit_Number = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Number.setObjectName(u"lineEdit_Number")

        self.gridLayout.addWidget(self.lineEdit_Number, 0, 2, 1, 1)

        self.label_Pin = QLabel(self.formLayoutWidget)
        self.label_Pin.setObjectName(u"label_Pin")

        self.gridLayout.addWidget(self.label_Pin, 0, 3, 1, 1)

        self.label_DeviceType = QLabel(self.formLayoutWidget)
        self.label_DeviceType.setObjectName(u"label_DeviceType")

        self.gridLayout.addWidget(self.label_DeviceType, 4, 3, 1, 1)

        self.comboBox_DeviceType = QComboBox(self.formLayoutWidget)
        self.comboBox_DeviceType.setObjectName(u"comboBox_DeviceType")

        self.gridLayout.addWidget(self.comboBox_DeviceType, 4, 5, 1, 1)

        self.checkBox_Active = QCheckBox(self.formLayoutWidget)
        self.checkBox_Active.setObjectName(u"checkBox_Active")

        self.gridLayout.addWidget(self.checkBox_Active, 6, 0, 1, 1)

        self.label_SerialNumber = QLabel(self.formLayoutWidget)
        self.label_SerialNumber.setObjectName(u"label_SerialNumber")

        self.gridLayout.addWidget(self.label_SerialNumber, 1, 0, 1, 1)

        self.comboBox_Manufacturer = QComboBox(self.formLayoutWidget)
        self.comboBox_Manufacturer.setObjectName(u"comboBox_Manufacturer")

        self.gridLayout.addWidget(self.comboBox_Manufacturer, 5, 2, 1, 1)

        self.label_Number = QLabel(self.formLayoutWidget)
        self.label_Number.setObjectName(u"label_Number")

        self.gridLayout.addWidget(self.label_Number, 0, 0, 1, 1)

        self.comboBox_DeviceName = QComboBox(self.formLayoutWidget)
        self.comboBox_DeviceName.setObjectName(u"comboBox_DeviceName")

        self.gridLayout.addWidget(self.comboBox_DeviceName, 4, 2, 1, 1)

        self.lineEdit_SerialNumber = QLineEdit(self.formLayoutWidget)
        self.lineEdit_SerialNumber.setObjectName(u"lineEdit_SerialNumber")

        self.gridLayout.addWidget(self.lineEdit_SerialNumber, 1, 2, 1, 1)

        self.comboBox_Employee = QComboBox(self.formLayoutWidget)
        self.comboBox_Employee.setObjectName(u"comboBox_Employee")

        self.gridLayout.addWidget(self.comboBox_Employee, 2, 2, 1, 1)

        self.comboBox_Inventory = QComboBox(self.formLayoutWidget)
        self.comboBox_Inventory.setObjectName(u"comboBox_Inventory")

        self.gridLayout.addWidget(self.comboBox_Inventory, 5, 5, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Add = QPushButton(self.formLayoutWidget)
        self.pushButton_Add.setObjectName(u"pushButton_Add")

        self.horizontalLayout.addWidget(self.pushButton_Add)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_EditFinish = QPushButton(self.formLayoutWidget)
        self.pushButton_EditFinish.setObjectName(u"pushButton_EditFinish")

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
            QCoreApplication.translate("MobileInputArea", u"Mobile", None)
        )
        # if QT_CONFIG(accessibility)
        MobileInputArea.setAccessibleName(
            QCoreApplication.translate("MobileInputArea", u"MobileInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        MobileInputArea.setTitle(
            QCoreApplication.translate("MobileInputArea", u"Mobile", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("MobileInputArea", u"Mobile", None)
        )
        self.label_DeviceName.setText(
            QCoreApplication.translate("MobileInputArea", u"Devicename", None)
        )
        self.label_Department.setText(
            QCoreApplication.translate("MobileInputArea", u"Department", None)
        )
        self.label_Inventory.setText(
            QCoreApplication.translate("MobileInputArea", u"Inventory", None)
        )
        self.label_Employee.setText(
            QCoreApplication.translate("MobileInputArea", u"Employee", None)
        )
        self.label_Manufacturer.setText(
            QCoreApplication.translate("MobileInputArea", u"Manufacturer", None)
        )
        self.checkBox_Replace.setText(
            QCoreApplication.translate("MobileInputArea", u"Replace", None)
        )
        self.label_Place.setText(
            QCoreApplication.translate("MobileInputArea", u"Place", None)
        )
        self.label_CardNumber.setText(
            QCoreApplication.translate("MobileInputArea", u"Card Number", None)
        )
        self.label_Pin.setText(
            QCoreApplication.translate("MobileInputArea", u"Pin", None)
        )
        self.label_DeviceType.setText(
            QCoreApplication.translate("MobileInputArea", u"Devicetype", None)
        )
        self.checkBox_Active.setText(
            QCoreApplication.translate("MobileInputArea", u"Active", None)
        )
        self.label_SerialNumber.setText(
            QCoreApplication.translate("MobileInputArea", u"Serial Number", None)
        )
        self.label_Number.setText(
            QCoreApplication.translate("MobileInputArea", u"Number", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("MobileInputArea", u"+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("MobileInputArea", u"Edit", None)
        )

    # retranslateUi
