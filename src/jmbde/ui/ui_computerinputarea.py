# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'computerinputarea.ui'
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


class Ui_ComputerInputArea(object):
    def setupUi(self, ComputerInputArea):
        if not ComputerInputArea.objectName():
            ComputerInputArea.setObjectName(u"ComputerInputArea")
        ComputerInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(ComputerInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayoutWidget = QWidget(ComputerInputArea)
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
        self.label_ServiceNumber = QLabel(self.formLayoutWidget)
        self.label_ServiceNumber.setObjectName(u"label_ServiceNumber")

        self.gridLayout.addWidget(self.label_ServiceNumber, 1, 0, 1, 1)

        self.checkBox_Active = QCheckBox(self.formLayoutWidget)
        self.checkBox_Active.setObjectName(u"checkBox_Active")

        self.gridLayout.addWidget(self.checkBox_Active, 9, 0, 1, 1)

        self.checkBox_Replace = QCheckBox(self.formLayoutWidget)
        self.checkBox_Replace.setObjectName(u"checkBox_Replace")

        self.gridLayout.addWidget(self.checkBox_Replace, 9, 3, 1, 1)

        self.label_OperationSystem = QLabel(self.formLayoutWidget)
        self.label_OperationSystem.setObjectName(u"label_OperationSystem")

        self.gridLayout.addWidget(self.label_OperationSystem, 3, 3, 1, 1)

        self.comboBox_OperationSystem = QComboBox(self.formLayoutWidget)
        self.comboBox_OperationSystem.setObjectName(u"comboBox_OperationSystem")

        self.gridLayout.addWidget(self.comboBox_OperationSystem, 3, 4, 1, 1)

        self.label_Place = QLabel(self.formLayoutWidget)
        self.label_Place.setObjectName(u"label_Place")

        self.gridLayout.addWidget(self.label_Place, 6, 3, 1, 1)

        self.label_Employee = QLabel(self.formLayoutWidget)
        self.label_Employee.setObjectName(u"label_Employee")

        self.gridLayout.addWidget(self.label_Employee, 5, 0, 1, 1)

        self.comboBox_Inventory = QComboBox(self.formLayoutWidget)
        self.comboBox_Inventory.setObjectName(u"comboBox_Inventory")

        self.gridLayout.addWidget(self.comboBox_Inventory, 8, 4, 1, 1)

        self.comboBox_Processor = QComboBox(self.formLayoutWidget)
        self.comboBox_Processor.setObjectName(u"comboBox_Processor")

        self.gridLayout.addWidget(self.comboBox_Processor, 3, 2, 1, 1)

        self.label_Processor = QLabel(self.formLayoutWidget)
        self.label_Processor.setObjectName(u"label_Processor")

        self.gridLayout.addWidget(self.label_Processor, 3, 0, 1, 1)

        self.label_Inventory = QLabel(self.formLayoutWidget)
        self.label_Inventory.setObjectName(u"label_Inventory")

        self.gridLayout.addWidget(self.label_Inventory, 8, 3, 1, 1)

        self.comboBox_Department = QComboBox(self.formLayoutWidget)
        self.comboBox_Department.setObjectName(u"comboBox_Department")

        self.gridLayout.addWidget(self.comboBox_Department, 6, 2, 1, 1)

        self.label_Manufacturer = QLabel(self.formLayoutWidget)
        self.label_Manufacturer.setObjectName(u"label_Manufacturer")

        self.gridLayout.addWidget(self.label_Manufacturer, 8, 0, 1, 1)

        self.comboBox_DeviceType = QComboBox(self.formLayoutWidget)
        self.comboBox_DeviceType.setObjectName(u"comboBox_DeviceType")

        self.gridLayout.addWidget(self.comboBox_DeviceType, 7, 4, 1, 1)

        self.comboBox_DeviceName = QComboBox(self.formLayoutWidget)
        self.comboBox_DeviceName.setObjectName(u"comboBox_DeviceName")

        self.gridLayout.addWidget(self.comboBox_DeviceName, 7, 2, 1, 1)

        self.comboBox_Place = QComboBox(self.formLayoutWidget)
        self.comboBox_Place.setObjectName(u"comboBox_Place")

        self.gridLayout.addWidget(self.comboBox_Place, 6, 4, 1, 1)

        self.comboBox_Employee = QComboBox(self.formLayoutWidget)
        self.comboBox_Employee.setObjectName(u"comboBox_Employee")

        self.gridLayout.addWidget(self.comboBox_Employee, 5, 2, 1, 1)

        self.label_Name = QLabel(self.formLayoutWidget)
        self.label_Name.setObjectName(u"label_Name")

        self.gridLayout.addWidget(self.label_Name, 0, 0, 1, 1)

        self.lineEdit_IPAddress = QLineEdit(self.formLayoutWidget)
        self.lineEdit_IPAddress.setObjectName(u"lineEdit_IPAddress")

        self.gridLayout.addWidget(self.lineEdit_IPAddress, 2, 4, 1, 1)

        self.comboBox_Manufacturer = QComboBox(self.formLayoutWidget)
        self.comboBox_Manufacturer.setObjectName(u"comboBox_Manufacturer")

        self.gridLayout.addWidget(self.comboBox_Manufacturer, 8, 2, 1, 1)

        self.label_IPAddress = QLabel(self.formLayoutWidget)
        self.label_IPAddress.setObjectName(u"label_IPAddress")

        self.gridLayout.addWidget(self.label_IPAddress, 2, 3, 1, 1)

        self.label_SerialNumber = QLabel(self.formLayoutWidget)
        self.label_SerialNumber.setObjectName(u"label_SerialNumber")

        self.gridLayout.addWidget(self.label_SerialNumber, 0, 3, 1, 1)

        self.label_Network = QLabel(self.formLayoutWidget)
        self.label_Network.setObjectName(u"label_Network")

        self.gridLayout.addWidget(self.label_Network, 2, 0, 1, 1)

        self.label_Devicename = QLabel(self.formLayoutWidget)
        self.label_Devicename.setObjectName(u"label_Devicename")

        self.gridLayout.addWidget(self.label_Devicename, 7, 0, 1, 1)

        self.label_DeviceType = QLabel(self.formLayoutWidget)
        self.label_DeviceType.setObjectName(u"label_DeviceType")

        self.gridLayout.addWidget(self.label_DeviceType, 7, 3, 1, 1)

        self.lineEdit_Network = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Network.setObjectName(u"lineEdit_Network")

        self.gridLayout.addWidget(self.lineEdit_Network, 2, 2, 1, 1)

        self.label_Department = QLabel(self.formLayoutWidget)
        self.label_Department.setObjectName(u"label_Department")

        self.gridLayout.addWidget(self.label_Department, 6, 0, 1, 1)

        self.lineEdit_ServiceNumber = QLineEdit(self.formLayoutWidget)
        self.lineEdit_ServiceNumber.setObjectName(u"lineEdit_ServiceNumber")

        self.gridLayout.addWidget(self.lineEdit_ServiceNumber, 1, 2, 1, 1)

        self.label_ServiceTag = QLabel(self.formLayoutWidget)
        self.label_ServiceTag.setObjectName(u"label_ServiceTag")

        self.gridLayout.addWidget(self.label_ServiceTag, 1, 3, 1, 1)

        self.lineEdit_ServiceTag = QLineEdit(self.formLayoutWidget)
        self.lineEdit_ServiceTag.setObjectName(u"lineEdit_ServiceTag")

        self.gridLayout.addWidget(self.lineEdit_ServiceTag, 1, 4, 1, 1)

        self.lineEdit_SerialNumber = QLineEdit(self.formLayoutWidget)
        self.lineEdit_SerialNumber.setObjectName(u"lineEdit_SerialNumber")

        self.gridLayout.addWidget(self.lineEdit_SerialNumber, 0, 4, 1, 1)

        self.lineEdit_ComputerName = QLineEdit(self.formLayoutWidget)
        self.lineEdit_ComputerName.setObjectName(u"lineEdit_ComputerName")

        self.gridLayout.addWidget(self.lineEdit_ComputerName, 0, 2, 1, 1)

        self.label_Software = QLabel(self.formLayoutWidget)
        self.label_Software.setObjectName(u"label_Software")

        self.gridLayout.addWidget(self.label_Software, 4, 0, 1, 1)

        self.comboBox_Software = QComboBox(self.formLayoutWidget)
        self.comboBox_Software.setObjectName(u"comboBox_Software")

        self.gridLayout.addWidget(self.comboBox_Software, 4, 2, 1, 1)

        self.label_Printer = QLabel(self.formLayoutWidget)
        self.label_Printer.setObjectName(u"label_Printer")

        self.gridLayout.addWidget(self.label_Printer, 4, 3, 1, 1)

        self.comboBox_Printer = QComboBox(self.formLayoutWidget)
        self.comboBox_Printer.setObjectName(u"comboBox_Printer")

        self.gridLayout.addWidget(self.comboBox_Printer, 4, 4, 1, 1)

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
        self.label_ServiceNumber.setBuddy(self.lineEdit_ServiceNumber)
        self.label_OperationSystem.setBuddy(self.comboBox_OperationSystem)
        self.label_Place.setBuddy(self.comboBox_Place)
        self.label_Employee.setBuddy(self.comboBox_Employee)
        self.label_Processor.setBuddy(self.comboBox_Processor)
        self.label_Inventory.setBuddy(self.comboBox_Inventory)
        self.label_Manufacturer.setBuddy(self.comboBox_Manufacturer)
        self.label_Name.setBuddy(self.lineEdit_ComputerName)
        self.label_IPAddress.setBuddy(self.lineEdit_IPAddress)
        self.label_SerialNumber.setBuddy(self.lineEdit_SerialNumber)
        self.label_Network.setBuddy(self.lineEdit_Network)
        self.label_Devicename.setBuddy(self.comboBox_DeviceName)
        self.label_DeviceType.setBuddy(self.comboBox_DeviceType)
        self.label_Department.setBuddy(self.comboBox_Department)
        self.label_ServiceTag.setBuddy(self.lineEdit_ServiceTag)
        self.label_Software.setBuddy(self.comboBox_Software)
        self.label_Printer.setBuddy(self.comboBox_Printer)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_ComputerName, self.lineEdit_SerialNumber)
        QWidget.setTabOrder(self.lineEdit_SerialNumber, self.lineEdit_ServiceNumber)
        QWidget.setTabOrder(self.lineEdit_ServiceNumber, self.lineEdit_ServiceTag)
        QWidget.setTabOrder(self.lineEdit_ServiceTag, self.lineEdit_Network)
        QWidget.setTabOrder(self.lineEdit_Network, self.lineEdit_IPAddress)
        QWidget.setTabOrder(self.lineEdit_IPAddress, self.comboBox_Processor)
        QWidget.setTabOrder(self.comboBox_Processor, self.comboBox_OperationSystem)
        QWidget.setTabOrder(self.comboBox_OperationSystem, self.comboBox_Software)
        QWidget.setTabOrder(self.comboBox_Software, self.comboBox_Printer)
        QWidget.setTabOrder(self.comboBox_Printer, self.comboBox_Employee)
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

        self.retranslateUi(ComputerInputArea)

        QMetaObject.connectSlotsByName(ComputerInputArea)

    # setupUi

    def retranslateUi(self, ComputerInputArea):
        ComputerInputArea.setWindowTitle(
            QCoreApplication.translate("ComputerInputArea", u"GroupBox", None)
        )
        # if QT_CONFIG(accessibility)
        ComputerInputArea.setAccessibleName(
            QCoreApplication.translate(
                "ComputerInputArea", u"ComputerInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        ComputerInputArea.setTitle(
            QCoreApplication.translate("ComputerInputArea", u"Computer", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("ComputerInputArea", u"Computer", None)
        )
        self.label_ServiceNumber.setText(
            QCoreApplication.translate("ComputerInputArea", u"Service Number", None)
        )
        self.checkBox_Active.setText(
            QCoreApplication.translate("ComputerInputArea", u"Active", None)
        )
        self.checkBox_Replace.setText(
            QCoreApplication.translate("ComputerInputArea", u"Replace", None)
        )
        self.label_OperationSystem.setText(
            QCoreApplication.translate("ComputerInputArea", u"Operation System", None)
        )
        self.label_Place.setText(
            QCoreApplication.translate("ComputerInputArea", u"Place", None)
        )
        self.label_Employee.setText(
            QCoreApplication.translate("ComputerInputArea", u"Employee", None)
        )
        self.label_Processor.setText(
            QCoreApplication.translate("ComputerInputArea", u"Processor", None)
        )
        self.label_Inventory.setText(
            QCoreApplication.translate("ComputerInputArea", u"Inventory", None)
        )
        self.label_Manufacturer.setText(
            QCoreApplication.translate("ComputerInputArea", u"Manufacturer", None)
        )
        self.label_Name.setText(
            QCoreApplication.translate("ComputerInputArea", u"Name", None)
        )
        self.label_IPAddress.setText(
            QCoreApplication.translate("ComputerInputArea", u"IP Address", None)
        )
        self.label_SerialNumber.setText(
            QCoreApplication.translate("ComputerInputArea", u"Serial Number", None)
        )
        self.label_Network.setText(
            QCoreApplication.translate("ComputerInputArea", u"Network", None)
        )
        self.label_Devicename.setText(
            QCoreApplication.translate("ComputerInputArea", u"Devicename", None)
        )
        self.label_DeviceType.setText(
            QCoreApplication.translate("ComputerInputArea", u"Devicetype", None)
        )
        self.label_Department.setText(
            QCoreApplication.translate("ComputerInputArea", u"Department", None)
        )
        self.label_ServiceTag.setText(
            QCoreApplication.translate("ComputerInputArea", u"Service Tag", None)
        )
        self.label_Software.setText(
            QCoreApplication.translate("ComputerInputArea", u"Software", None)
        )
        self.label_Printer.setText(
            QCoreApplication.translate("ComputerInputArea", u"Printer", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("ComputerInputArea", u"+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("ComputerInputArea", u"Edit", None)
        )

    # retranslateUi
