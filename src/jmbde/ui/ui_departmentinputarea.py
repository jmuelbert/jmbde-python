# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'departmentinputarea.ui'
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


class Ui_DepartmentInputArea(object):
    def setupUi(self, DepartmentInputArea):
        if not DepartmentInputArea.objectName():
            DepartmentInputArea.setObjectName(u"DepartmentInputArea")
        DepartmentInputArea.resize(730, 600)
        self.verticalLayout_2 = QVBoxLayout(DepartmentInputArea)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayoutWidget = QWidget(DepartmentInputArea)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_Printer = QLabel(self.formLayoutWidget)
        self.label_Printer.setObjectName(u"label_Printer")

        self.gridLayout.addWidget(self.label_Printer, 4, 0, 1, 1)

        self.label_Pri_Test = QLabel(self.formLayoutWidget)
        self.label_Pri_Test.setObjectName(u"label_Pri_Test")

        self.gridLayout.addWidget(self.label_Pri_Test, 3, 0, 1, 1)

        self.lcdNumber_Priority = QLCDNumber(self.formLayoutWidget)
        self.lcdNumber_Priority.setObjectName(u"lcdNumber_Priority")

        self.gridLayout.addWidget(self.lcdNumber_Priority, 3, 4, 1, 1)

        self.label_Priority = QLabel(self.formLayoutWidget)
        self.label_Priority.setObjectName(u"label_Priority")

        self.gridLayout.addWidget(self.label_Priority, 2, 0, 1, 1)

        self.lineEdit_Name = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.gridLayout.addWidget(self.lineEdit_Name, 1, 3, 1, 1)

        self.dial_Priority = QDial(self.formLayoutWidget)
        self.dial_Priority.setObjectName(u"dial_Priority")

        self.gridLayout.addWidget(self.dial_Priority, 3, 5, 1, 1)

        self.comboBox_Printer = QComboBox(self.formLayoutWidget)
        self.comboBox_Printer.setObjectName(u"comboBox_Printer")

        self.gridLayout.addWidget(self.comboBox_Printer, 4, 3, 1, 1)

        self.spinBox_Priority = QSpinBox(self.formLayoutWidget)
        self.spinBox_Priority.setObjectName(u"spinBox_Priority")

        self.gridLayout.addWidget(self.spinBox_Priority, 2, 3, 1, 1)

        self.label_Name = QLabel(self.formLayoutWidget)
        self.label_Name.setObjectName(u"label_Name")

        self.gridLayout.addWidget(self.label_Name, 1, 0, 1, 1)

        self.horizontalSlider_Priority = QSlider(self.formLayoutWidget)
        self.horizontalSlider_Priority.setObjectName(u"horizontalSlider_Priority")
        self.horizontalSlider_Priority.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_Priority, 3, 3, 1, 1)

        self.label_Fax = QLabel(self.formLayoutWidget)
        self.label_Fax.setObjectName(u"label_Fax")

        self.gridLayout.addWidget(self.label_Fax, 5, 0, 1, 1)

        self.comboBox_Fax = QComboBox(self.formLayoutWidget)
        self.comboBox_Fax.setObjectName(u"comboBox_Fax")

        self.gridLayout.addWidget(self.comboBox_Fax, 5, 3, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

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

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addWidget(self.formLayoutWidget)

        # if QT_CONFIG(shortcut)
        self.label_Printer.setBuddy(self.comboBox_Printer)
        self.label_Pri_Test.setBuddy(self.horizontalSlider_Priority)
        self.label_Priority.setBuddy(self.spinBox_Priority)
        self.label_Name.setBuddy(self.lineEdit_Name)
        self.label_Fax.setBuddy(self.comboBox_Fax)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_Name, self.spinBox_Priority)
        QWidget.setTabOrder(self.spinBox_Priority, self.horizontalSlider_Priority)
        QWidget.setTabOrder(self.horizontalSlider_Priority, self.comboBox_Printer)
        QWidget.setTabOrder(self.comboBox_Printer, self.comboBox_Fax)
        QWidget.setTabOrder(self.comboBox_Fax, self.pushButton_Add)
        QWidget.setTabOrder(self.pushButton_Add, self.pushButton_EditFinish)
        QWidget.setTabOrder(self.pushButton_EditFinish, self.dial_Priority)

        self.retranslateUi(DepartmentInputArea)

        QMetaObject.connectSlotsByName(DepartmentInputArea)

    # setupUi

    def retranslateUi(self, DepartmentInputArea):
        DepartmentInputArea.setWindowTitle(
            QCoreApplication.translate("DepartmentInputArea", u"Department", None)
        )
        # if QT_CONFIG(accessibility)
        DepartmentInputArea.setAccessibleName(
            QCoreApplication.translate(
                "DepartmentInputArea", u"DepartmentInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        DepartmentInputArea.setTitle(
            QCoreApplication.translate("DepartmentInputArea", u"Department", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("DepartmentInputArea", u"Department", None)
        )
        self.label_Printer.setText(
            QCoreApplication.translate("DepartmentInputArea", u"Printer", None)
        )
        self.label_Pri_Test.setText(
            QCoreApplication.translate("DepartmentInputArea", u"Pri-Test", None)
        )
        self.label_Priority.setText(
            QCoreApplication.translate("DepartmentInputArea", u"Priority", None)
        )
        self.label_Name.setText(
            QCoreApplication.translate("DepartmentInputArea", u"Name", None)
        )
        self.label_Fax.setText(
            QCoreApplication.translate("DepartmentInputArea", u"Fax", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("DepartmentInputArea", u"+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("DepartmentInputArea", u"Edit", None)
        )

    # retranslateUi
