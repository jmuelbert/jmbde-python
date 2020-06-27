# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'chipcardinputarea.ui'
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


class Ui_ChipCardInputArea(object):
    def setupUi(self, ChipCardInputArea):
        if not ChipCardInputArea.objectName():
            ChipCardInputArea.setObjectName(u"ChipCardInputArea")
        ChipCardInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(ChipCardInputArea)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.GroupBox = QWidget(ChipCardInputArea)
        self.GroupBox.setObjectName(u"GroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.GroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_Number = QLabel(self.GroupBox)
        self.label_Number.setObjectName(u"label_Number")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_Number)

        self.lineEdit = QLineEdit(self.GroupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_Version = QLabel(self.GroupBox)
        self.label_Version.setObjectName(u"label_Version")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_Version)

        self.comboBox_Door = QComboBox(self.GroupBox)
        self.comboBox_Door.setObjectName(u"comboBox_Door")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_Door)

        self.label_Revision = QLabel(self.GroupBox)
        self.label_Revision.setObjectName(u"label_Revision")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_Revision)

        self.comboBox_Profile = QComboBox(self.GroupBox)
        self.comboBox_Profile.setObjectName(u"comboBox_Profile")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_Profile)

        self.label_Fix = QLabel(self.GroupBox)
        self.label_Fix.setObjectName(u"label_Fix")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_Fix)

        self.comboBox_Employee = QComboBox(self.GroupBox)
        self.comboBox_Employee.setObjectName(u"comboBox_Employee")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox_Employee)

        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

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

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.gridLayout_3.addWidget(self.GroupBox, 0, 0, 1, 1)

        QWidget.setTabOrder(self.pushButton_Add, self.pushButton_EditFinish)

        self.retranslateUi(ChipCardInputArea)

        QMetaObject.connectSlotsByName(ChipCardInputArea)

    # setupUi

    def retranslateUi(self, ChipCardInputArea):
        ChipCardInputArea.setWindowTitle(
            QCoreApplication.translate("ChipCardInputArea", u"Chip Card", None)
        )
        # if QT_CONFIG(accessibility)
        ChipCardInputArea.setAccessibleName(
            QCoreApplication.translate(
                "ChipCardInputArea", u"ChipCardInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        ChipCardInputArea.setTitle(
            QCoreApplication.translate("ChipCardInputArea", u"Chip Card", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("ChipCardInputArea", u"ChipCard", None)
        )
        self.label_Number.setText(
            QCoreApplication.translate("ChipCardInputArea", u"Number", None)
        )
        self.label_Version.setText(
            QCoreApplication.translate("ChipCardInputArea", u"Door", None)
        )
        self.label_Revision.setText(
            QCoreApplication.translate("ChipCardInputArea", u"Profile", None)
        )
        self.label_Fix.setText(
            QCoreApplication.translate("ChipCardInputArea", u"Employee", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("ChipCardInputArea", u"+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("ChipCardInputArea", u"Edit", None)
        )

    # retranslateUi
