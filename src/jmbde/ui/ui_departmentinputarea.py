# -*- coding: utf-8 -*-
################################################################################
# Form generated from reading UI file 'departmentinputarea.ui'
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


class Ui_DepartmentInputArea(object):
    def setupUi(self, DepartmentInputArea):
        if not DepartmentInputArea.objectName():
            DepartmentInputArea.setObjectName("DepartmentInputArea")
        DepartmentInputArea.resize(730, 600)
        self.verticalLayout_2 = QVBoxLayout(DepartmentInputArea)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayoutWidget = QWidget(DepartmentInputArea)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
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

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_Printer = QLabel(self.formLayoutWidget)
        self.label_Printer.setObjectName("label_Printer")

        self.gridLayout.addWidget(self.label_Printer, 4, 0, 1, 1)

        self.label_Pri_Test = QLabel(self.formLayoutWidget)
        self.label_Pri_Test.setObjectName("label_Pri_Test")

        self.gridLayout.addWidget(self.label_Pri_Test, 3, 0, 1, 1)

        self.lcdNumber_Priority = QLCDNumber(self.formLayoutWidget)
        self.lcdNumber_Priority.setObjectName("lcdNumber_Priority")

        self.gridLayout.addWidget(self.lcdNumber_Priority, 3, 4, 1, 1)

        self.label_Priority = QLabel(self.formLayoutWidget)
        self.label_Priority.setObjectName("label_Priority")

        self.gridLayout.addWidget(self.label_Priority, 2, 0, 1, 1)

        self.lineEdit_Name = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Name.setObjectName("lineEdit_Name")

        self.gridLayout.addWidget(self.lineEdit_Name, 1, 3, 1, 1)

        self.dial_Priority = QDial(self.formLayoutWidget)
        self.dial_Priority.setObjectName("dial_Priority")

        self.gridLayout.addWidget(self.dial_Priority, 3, 5, 1, 1)

        self.comboBox_Printer = QComboBox(self.formLayoutWidget)
        self.comboBox_Printer.setObjectName("comboBox_Printer")

        self.gridLayout.addWidget(self.comboBox_Printer, 4, 3, 1, 1)

        self.spinBox_Priority = QSpinBox(self.formLayoutWidget)
        self.spinBox_Priority.setObjectName("spinBox_Priority")

        self.gridLayout.addWidget(self.spinBox_Priority, 2, 3, 1, 1)

        self.label_Name = QLabel(self.formLayoutWidget)
        self.label_Name.setObjectName("label_Name")

        self.gridLayout.addWidget(self.label_Name, 1, 0, 1, 1)

        self.horizontalSlider_Priority = QSlider(self.formLayoutWidget)
        self.horizontalSlider_Priority.setObjectName("horizontalSlider_Priority")
        self.horizontalSlider_Priority.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_Priority, 3, 3, 1, 1)

        self.label_Fax = QLabel(self.formLayoutWidget)
        self.label_Fax.setObjectName("label_Fax")

        self.gridLayout.addWidget(self.label_Fax, 5, 0, 1, 1)

        self.comboBox_Fax = QComboBox(self.formLayoutWidget)
        self.comboBox_Fax.setObjectName("comboBox_Fax")

        self.gridLayout.addWidget(self.comboBox_Fax, 5, 3, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

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
            QCoreApplication.translate("DepartmentInputArea", "Department", None)
        )
        # if QT_CONFIG(accessibility)
        DepartmentInputArea.setAccessibleName(
            QCoreApplication.translate(
                "DepartmentInputArea", "DepartmentInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        DepartmentInputArea.setTitle(
            QCoreApplication.translate("DepartmentInputArea", "Department", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("DepartmentInputArea", "Department", None)
        )
        self.label_Printer.setText(
            QCoreApplication.translate("DepartmentInputArea", "Printer", None)
        )
        self.label_Pri_Test.setText(
            QCoreApplication.translate("DepartmentInputArea", "Pri-Test", None)
        )
        self.label_Priority.setText(
            QCoreApplication.translate("DepartmentInputArea", "Priority", None)
        )
        self.label_Name.setText(
            QCoreApplication.translate("DepartmentInputArea", "Name", None)
        )
        self.label_Fax.setText(
            QCoreApplication.translate("DepartmentInputArea", "Fax", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("DepartmentInputArea", "+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("DepartmentInputArea", "Edit", None)
        )

    # retranslateUi
