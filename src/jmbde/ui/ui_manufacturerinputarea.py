# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'manufacturerinputarea.ui'
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


class Ui_ManufacturerInputArea(object):
    def setupUi(self, ManufacturerInputArea):
        if not ManufacturerInputArea.objectName():
            ManufacturerInputArea.setObjectName(u"ManufacturerInputArea")
        ManufacturerInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(ManufacturerInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayoutWidget = QWidget(ManufacturerInputArea)
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
        self.label_Phone = QLabel(self.formLayoutWidget)
        self.label_Phone.setObjectName(u"label_Phone")

        self.gridLayout.addWidget(self.label_Phone, 11, 2, 1, 1)

        self.comboBox_ZipCode = QComboBox(self.formLayoutWidget)
        self.comboBox_ZipCode.setObjectName(u"comboBox_ZipCode")

        self.gridLayout.addWidget(self.comboBox_ZipCode, 8, 4, 1, 1)

        self.label_MailAddress = QLabel(self.formLayoutWidget)
        self.label_MailAddress.setObjectName(u"label_MailAddress")

        self.gridLayout.addWidget(self.label_MailAddress, 9, 2, 1, 1)

        self.lineEdit_Phone = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Phone.setObjectName(u"lineEdit_Phone")

        self.gridLayout.addWidget(self.lineEdit_Phone, 11, 4, 1, 1)

        self.label_Name2 = QLabel(self.formLayoutWidget)
        self.label_Name2.setObjectName(u"label_Name2")

        self.gridLayout.addWidget(self.label_Name2, 3, 2, 1, 1)

        self.lineEdit_Fax = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Fax.setObjectName(u"lineEdit_Fax")

        self.gridLayout.addWidget(self.lineEdit_Fax, 12, 4, 1, 1)

        self.lineEdit_Name2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Name2.setObjectName(u"lineEdit_Name2")

        self.gridLayout.addWidget(self.lineEdit_Name2, 3, 4, 1, 1)

        self.label_ZipCode = QLabel(self.formLayoutWidget)
        self.label_ZipCode.setObjectName(u"label_ZipCode")

        self.gridLayout.addWidget(self.label_ZipCode, 8, 2, 1, 1)

        self.label_Fax = QLabel(self.formLayoutWidget)
        self.label_Fax.setObjectName(u"label_Fax")

        self.gridLayout.addWidget(self.label_Fax, 12, 2, 1, 1)

        self.label_Address2 = QLabel(self.formLayoutWidget)
        self.label_Address2.setObjectName(u"label_Address2")

        self.gridLayout.addWidget(self.label_Address2, 7, 2, 1, 1)

        self.lineEdit_Address = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Address.setObjectName(u"lineEdit_Address")

        self.gridLayout.addWidget(self.lineEdit_Address, 6, 4, 1, 1)

        self.lineEdit_Address2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Address2.setObjectName(u"lineEdit_Address2")

        self.gridLayout.addWidget(self.lineEdit_Address2, 7, 4, 1, 1)

        self.lineEdit_Supporter = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Supporter.setObjectName(u"lineEdit_Supporter")

        self.gridLayout.addWidget(self.lineEdit_Supporter, 4, 4, 1, 1)

        self.label_Address = QLabel(self.formLayoutWidget)
        self.label_Address.setObjectName(u"label_Address")

        self.gridLayout.addWidget(self.label_Address, 6, 2, 1, 1)

        self.lineEdit_MailAddress = QLineEdit(self.formLayoutWidget)
        self.lineEdit_MailAddress.setObjectName(u"lineEdit_MailAddress")

        self.gridLayout.addWidget(self.lineEdit_MailAddress, 9, 4, 1, 1)

        self.lineEdit_Name = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.gridLayout.addWidget(self.lineEdit_Name, 1, 4, 1, 1)

        self.label_Name = QLabel(self.formLayoutWidget)
        self.label_Name.setObjectName(u"label_Name")

        self.gridLayout.addWidget(self.label_Name, 1, 2, 1, 1)

        self.label_Supporter = QLabel(self.formLayoutWidget)
        self.label_Supporter.setObjectName(u"label_Supporter")

        self.gridLayout.addWidget(self.label_Supporter, 4, 2, 1, 1)

        self.label_Hotline = QLabel(self.formLayoutWidget)
        self.label_Hotline.setObjectName(u"label_Hotline")

        self.gridLayout.addWidget(self.label_Hotline, 10, 2, 1, 1)

        self.lineEdit_Hotline = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Hotline.setObjectName(u"lineEdit_Hotline")

        self.gridLayout.addWidget(self.lineEdit_Hotline, 10, 4, 1, 1)

        self.label_City = QLabel(self.formLayoutWidget)
        self.label_City.setObjectName(u"label_City")

        self.gridLayout.addWidget(self.label_City, 8, 5, 1, 1)

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
        self.label_Phone.setBuddy(self.lineEdit_Phone)
        self.label_MailAddress.setBuddy(self.lineEdit_MailAddress)
        self.label_Name2.setBuddy(self.lineEdit_Name2)
        self.label_ZipCode.setBuddy(self.comboBox_ZipCode)
        self.label_Fax.setBuddy(self.lineEdit_Fax)
        self.label_Address2.setBuddy(self.lineEdit_Address2)
        self.label_Address.setBuddy(self.lineEdit_Address)
        self.label_Name.setBuddy(self.lineEdit_Name)
        self.label_Supporter.setBuddy(self.lineEdit_Supporter)
        self.label_Hotline.setBuddy(self.lineEdit_Hotline)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_Name, self.lineEdit_Name2)
        QWidget.setTabOrder(self.lineEdit_Name2, self.lineEdit_Supporter)
        QWidget.setTabOrder(self.lineEdit_Supporter, self.lineEdit_Address)
        QWidget.setTabOrder(self.lineEdit_Address, self.lineEdit_Address2)
        QWidget.setTabOrder(self.lineEdit_Address2, self.comboBox_ZipCode)
        QWidget.setTabOrder(self.comboBox_ZipCode, self.lineEdit_MailAddress)
        QWidget.setTabOrder(self.lineEdit_MailAddress, self.lineEdit_Hotline)
        QWidget.setTabOrder(self.lineEdit_Hotline, self.lineEdit_Phone)
        QWidget.setTabOrder(self.lineEdit_Phone, self.lineEdit_Fax)
        QWidget.setTabOrder(self.lineEdit_Fax, self.pushButton_Add)
        QWidget.setTabOrder(self.pushButton_Add, self.pushButton_EditFinish)

        self.retranslateUi(ManufacturerInputArea)

        QMetaObject.connectSlotsByName(ManufacturerInputArea)

    # setupUi

    def retranslateUi(self, ManufacturerInputArea):
        ManufacturerInputArea.setWindowTitle(
            QCoreApplication.translate("ManufacturerInputArea", u"Manufacturer", None)
        )
        # if QT_CONFIG(accessibility)
        ManufacturerInputArea.setAccessibleName(
            QCoreApplication.translate(
                "ManufacturerInputArea", u"ManufacturerInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        ManufacturerInputArea.setTitle(
            QCoreApplication.translate("ManufacturerInputArea", u"Manufacturer", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"Manufacturer", None)
        )
        self.label_Phone.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"Phone Number", None)
        )
        self.label_MailAddress.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"Mail Address", None)
        )
        self.label_Name2.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"Name2", None)
        )
        self.label_ZipCode.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"Zip Code", None)
        )
        self.label_Fax.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"Fax Number", None)
        )
        self.label_Address2.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"Address2", None)
        )
        self.label_Address.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"Address", None)
        )
        self.label_Name.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"Name", None)
        )
        self.label_Supporter.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"Supporter", None)
        )
        self.label_Hotline.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"Hotline Number", None)
        )
        self.label_City.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"City", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("ManufacturerInputArea", u"Edit", None)
        )

    # retranslateUi
