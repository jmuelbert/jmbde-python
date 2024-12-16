################################################################################
# Form generated from reading UI file 'chipcardinputarea.ui'
##
# Created by: Qt User Interface Compiler version 5.15.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import (
    QCoreApplication,
    QMetaObject,
    Qt,
)
from PySide2.QtGui import (
    QFont,
)
from PySide2.QtWidgets import *


class Ui_ChipCardInputArea:
    def setupUi(self, ChipCardInputArea):
        if not ChipCardInputArea.objectName():
            ChipCardInputArea.setObjectName("ChipCardInputArea")
        ChipCardInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(ChipCardInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(ChipCardInputArea)
        self.GroupBox.setObjectName("GroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.GroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Header = QLabel(self.GroupBox)
        self.label_Header.setObjectName("label_Header")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Header.setFont(font)
        self.label_Header.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Header)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred,
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_Number = QLabel(self.GroupBox)
        self.label_Number.setObjectName("label_Number")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_Number)

        self.lineEdit = QLineEdit(self.GroupBox)
        self.lineEdit.setObjectName("lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_Version = QLabel(self.GroupBox)
        self.label_Version.setObjectName("label_Version")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_Version)

        self.comboBox_Door = QComboBox(self.GroupBox)
        self.comboBox_Door.setObjectName("comboBox_Door")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_Door)

        self.label_Revision = QLabel(self.GroupBox)
        self.label_Revision.setObjectName("label_Revision")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_Revision)

        self.comboBox_Profile = QComboBox(self.GroupBox)
        self.comboBox_Profile.setObjectName("comboBox_Profile")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_Profile)

        self.label_Fix = QLabel(self.GroupBox)
        self.label_Fix.setObjectName("label_Fix")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_Fix)

        self.comboBox_Employee = QComboBox(self.GroupBox)
        self.comboBox_Employee.setObjectName("comboBox_Employee")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox_Employee)

        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding,
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Add = QPushButton(self.GroupBox)
        self.pushButton_Add.setObjectName("pushButton_Add")

        self.horizontalLayout.addWidget(self.pushButton_Add)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum,
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_EditFinish = QPushButton(self.GroupBox)
        self.pushButton_EditFinish.setObjectName("pushButton_EditFinish")

        self.horizontalLayout.addWidget(self.pushButton_EditFinish)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.gridLayout_3.addWidget(self.GroupBox, 0, 0, 1, 1)

        QWidget.setTabOrder(self.pushButton_Add, self.pushButton_EditFinish)

        self.retranslateUi(ChipCardInputArea)

        QMetaObject.connectSlotsByName(ChipCardInputArea)

    # setupUi

    def retranslateUi(self, ChipCardInputArea):
        ChipCardInputArea.setWindowTitle(
            QCoreApplication.translate("ChipCardInputArea", "Chip Card", None),
        )
        # if QT_CONFIG(accessibility)
        ChipCardInputArea.setAccessibleName(
            QCoreApplication.translate("ChipCardInputArea", "ChipCardInputDialog", None),
        )
        # endif // QT_CONFIG(accessibility)
        ChipCardInputArea.setTitle(
            QCoreApplication.translate("ChipCardInputArea", "Chip Card", None),
        )
        self.label_Header.setText(
            QCoreApplication.translate("ChipCardInputArea", "ChipCard", None),
        )
        self.label_Number.setText(
            QCoreApplication.translate("ChipCardInputArea", "Number", None),
        )
        self.label_Version.setText(
            QCoreApplication.translate("ChipCardInputArea", "Door", None),
        )
        self.label_Revision.setText(
            QCoreApplication.translate("ChipCardInputArea", "Profile", None),
        )
        self.label_Fix.setText(
            QCoreApplication.translate("ChipCardInputArea", "Employee", None),
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("ChipCardInputArea", "+", None),
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("ChipCardInputArea", "Edit", None),
        )

    # retranslateUi
