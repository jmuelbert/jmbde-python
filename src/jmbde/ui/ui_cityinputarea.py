# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'cityinputarea.ui'
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


class Ui_CityInputArea(object):
    def setupUi(self, CityInputArea):
        if not CityInputArea.objectName():
            CityInputArea.setObjectName(u"CityInputArea")
        CityInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(CityInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.GroupBox = QWidget(CityInputArea)
        self.GroupBox.setObjectName(u"GroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.GroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Header = QLabel(self.GroupBox)
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
        self.lineEdit_CityName = QLineEdit(self.GroupBox)
        self.lineEdit_CityName.setObjectName(u"lineEdit_CityName")

        self.gridLayout.addWidget(self.lineEdit_CityName, 2, 1, 1, 1)

        self.label_ZipCode = QLabel(self.GroupBox)
        self.label_ZipCode.setObjectName(u"label_ZipCode")

        self.gridLayout.addWidget(self.label_ZipCode, 1, 0, 1, 1)

        self.comboBox_ZipCode = QComboBox(self.GroupBox)
        self.comboBox_ZipCode.setObjectName(u"comboBox_ZipCode")

        self.gridLayout.addWidget(self.comboBox_ZipCode, 1, 1, 1, 1)

        self.label_CityName = QLabel(self.GroupBox)
        self.label_CityName.setObjectName(u"label_CityName")

        self.gridLayout.addWidget(self.label_CityName, 2, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Add = QPushButton(self.GroupBox)
        self.pushButton_Add.setObjectName(u"pushButton_Add")

        self.horizontalLayout.addWidget(self.pushButton_Add)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_EditFinish = QPushButton(self.GroupBox)
        self.pushButton_EditFinish.setObjectName(u"pushButton_EditFinish")

        self.horizontalLayout.addWidget(self.pushButton_EditFinish)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addWidget(self.GroupBox)

        self.retranslateUi(CityInputArea)

        QMetaObject.connectSlotsByName(CityInputArea)

    # setupUi

    def retranslateUi(self, CityInputArea):
        CityInputArea.setWindowTitle(
            QCoreApplication.translate("CityInputArea", u"City", None)
        )
        # if QT_CONFIG(accessibility)
        CityInputArea.setAccessibleName(
            QCoreApplication.translate("CityInputArea", u"CityInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        CityInputArea.setTitle(
            QCoreApplication.translate("CityInputArea", u"City", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("CityInputArea", u"City", None)
        )
        self.label_ZipCode.setText(
            QCoreApplication.translate("CityInputArea", u"Zip Code", None)
        )
        self.label_CityName.setText(
            QCoreApplication.translate("CityInputArea", u"City Name", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("CityInputArea", u"+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("CityInputArea", u"Edit", None)
        )

    # retranslateUi
