# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'softwareinputarea.ui'
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


class Ui_SoftwareInputArea(object):
    def setupUi(self, SoftwareInputArea):
        if not SoftwareInputArea.objectName():
            SoftwareInputArea.setObjectName(u"SoftwareInputArea")
        SoftwareInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(SoftwareInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayoutWidget = QWidget(SoftwareInputArea)
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
        self.lineEdit_Version = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Version.setObjectName(u"lineEdit_Version")

        self.gridLayout.addWidget(self.lineEdit_Version, 1, 2, 1, 1)

        self.lineEdit_Name = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.gridLayout.addWidget(self.lineEdit_Name, 0, 2, 1, 1)

        self.label_Revision = QLabel(self.formLayoutWidget)
        self.label_Revision.setObjectName(u"label_Revision")

        self.gridLayout.addWidget(self.label_Revision, 2, 0, 1, 1)

        self.label_Version = QLabel(self.formLayoutWidget)
        self.label_Version.setObjectName(u"label_Version")

        self.gridLayout.addWidget(self.label_Version, 1, 0, 1, 1)

        self.lineEdit_Revision = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Revision.setObjectName(u"lineEdit_Revision")

        self.gridLayout.addWidget(self.lineEdit_Revision, 2, 2, 1, 1)

        self.label_Name = QLabel(self.formLayoutWidget)
        self.label_Name.setObjectName(u"label_Name")

        self.gridLayout.addWidget(self.label_Name, 0, 0, 1, 1)

        self.label_Fix = QLabel(self.formLayoutWidget)
        self.label_Fix.setObjectName(u"label_Fix")

        self.gridLayout.addWidget(self.label_Fix, 3, 0, 1, 1)

        self.lineEdit_Fix = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Fix.setObjectName(u"lineEdit_Fix")

        self.gridLayout.addWidget(self.lineEdit_Fix, 3, 2, 1, 1)

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
        self.label_Revision.setBuddy(self.lineEdit_Revision)
        self.label_Version.setBuddy(self.lineEdit_Version)
        self.label_Name.setBuddy(self.lineEdit_Name)
        self.label_Fix.setBuddy(self.lineEdit_Fix)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_Name, self.lineEdit_Version)
        QWidget.setTabOrder(self.lineEdit_Version, self.lineEdit_Revision)
        QWidget.setTabOrder(self.lineEdit_Revision, self.lineEdit_Fix)
        QWidget.setTabOrder(self.lineEdit_Fix, self.pushButton_Add)
        QWidget.setTabOrder(self.pushButton_Add, self.pushButton_EditFinish)

        self.retranslateUi(SoftwareInputArea)

        QMetaObject.connectSlotsByName(SoftwareInputArea)

    # setupUi

    def retranslateUi(self, SoftwareInputArea):
        SoftwareInputArea.setWindowTitle(
            QCoreApplication.translate("SoftwareInputArea", u"Software", None)
        )
        # if QT_CONFIG(accessibility)
        SoftwareInputArea.setAccessibleName(
            QCoreApplication.translate(
                "SoftwareInputArea", u"SoftwareInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        SoftwareInputArea.setTitle(
            QCoreApplication.translate("SoftwareInputArea", u"Software", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("SoftwareInputArea", u"Software", None)
        )
        self.label_Revision.setText(
            QCoreApplication.translate("SoftwareInputArea", u"Revision", None)
        )
        self.label_Version.setText(
            QCoreApplication.translate("SoftwareInputArea", u"Version", None)
        )
        self.label_Name.setText(
            QCoreApplication.translate("SoftwareInputArea", u"Name", None)
        )
        self.label_Fix.setText(
            QCoreApplication.translate("SoftwareInputArea", u"Fix", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("SoftwareInputArea", u"+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("SoftwareInputArea", u"Edit", None)
        )

    # retranslateUi
