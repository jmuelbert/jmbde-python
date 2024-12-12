# -*- coding: utf-8 -*-
################################################################################
# Form generated from reading UI file 'functioninputarea.ui'
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


class Ui_FunctionInputArea(object):
    def setupUi(self, FunctionInputArea):
        if not FunctionInputArea.objectName():
            FunctionInputArea.setObjectName("FunctionInputArea")
        FunctionInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(FunctionInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayoutWidget = QWidget(FunctionInputArea)
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
        self.label_Priority = QLabel(self.formLayoutWidget)
        self.label_Priority.setObjectName("label_Priority")

        self.gridLayout.addWidget(self.label_Priority, 1, 0, 1, 1)

        self.lineEdit_Name = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Name.setObjectName("lineEdit_Name")

        self.gridLayout.addWidget(self.lineEdit_Name, 0, 3, 1, 1)

        self.label_Name = QLabel(self.formLayoutWidget)
        self.label_Name.setObjectName("label_Name")

        self.gridLayout.addWidget(self.label_Name, 0, 0, 1, 1)

        self.spinBox_Priotity = QSpinBox(self.formLayoutWidget)
        self.spinBox_Priotity.setObjectName("spinBox_Priotity")

        self.gridLayout.addWidget(self.spinBox_Priotity, 1, 3, 1, 1)

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
        self.label_Priority.setBuddy(self.spinBox_Priotity)
        self.label_Name.setBuddy(self.lineEdit_Name)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_Name, self.spinBox_Priotity)
        QWidget.setTabOrder(self.spinBox_Priotity, self.pushButton_Add)
        QWidget.setTabOrder(self.pushButton_Add, self.pushButton_EditFinish)

        self.retranslateUi(FunctionInputArea)

        QMetaObject.connectSlotsByName(FunctionInputArea)

    # setupUi

    def retranslateUi(self, FunctionInputArea):
        FunctionInputArea.setWindowTitle(
            QCoreApplication.translate("FunctionInputArea", "Function", None)
        )
        # if QT_CONFIG(accessibility)
        FunctionInputArea.setAccessibleName(
            QCoreApplication.translate("FunctionInputArea", "FunctionInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        FunctionInputArea.setTitle(
            QCoreApplication.translate("FunctionInputArea", "Function", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("FunctionInputArea", "Function", None)
        )
        self.label_Priority.setText(
            QCoreApplication.translate("FunctionInputArea", "Priority", None)
        )
        self.label_Name.setText(
            QCoreApplication.translate("FunctionInputArea", "Name", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("FunctionInputArea", "+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("FunctionInputArea", "Edit", None)
        )

    # retranslateUi
