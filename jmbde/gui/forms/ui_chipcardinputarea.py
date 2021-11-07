# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chipcardinputarea.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


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
        self.numberLabel = QLabel(self.GroupBox)
        self.numberLabel.setObjectName(u"numberLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.numberLabel)

        self.numberLineEdit = QLineEdit(self.GroupBox)
        self.numberLineEdit.setObjectName(u"numberLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.numberLineEdit)

        self.doorLabel = QLabel(self.GroupBox)
        self.doorLabel.setObjectName(u"doorLabel")
        self.doorLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.doorLabel)

        self.doorComboBox = QComboBox(self.GroupBox)
        self.doorComboBox.setObjectName(u"doorComboBox")
        self.doorComboBox.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.doorComboBox)

        self.profileLabel = QLabel(self.GroupBox)
        self.profileLabel.setObjectName(u"profileLabel")
        self.profileLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.profileLabel)

        self.profileComboBox = QComboBox(self.GroupBox)
        self.profileComboBox.setObjectName(u"profileComboBox")
        self.profileComboBox.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.profileComboBox)

        self.employeeLabel = QLabel(self.GroupBox)
        self.employeeLabel.setObjectName(u"employeeLabel")
        self.employeeLabel.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.employeeLabel)

        self.employeeComboBox = QComboBox(self.GroupBox)
        self.employeeComboBox.setObjectName(u"employeeComboBox")
        self.employeeComboBox.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.employeeComboBox)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lastUpdateLineEdit)

        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addPushButton = QPushButton(self.GroupBox)
        self.addPushButton.setObjectName(u"addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.GroupBox)
        self.editFinishPushButton.setObjectName(u"editFinishPushButton")

        self.horizontalLayout.addWidget(self.editFinishPushButton)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.gridLayout_3.addWidget(self.GroupBox, 0, 0, 1, 1)

        # if QT_CONFIG(shortcut)
        self.numberLabel.setBuddy(self.numberLineEdit)
        self.doorLabel.setBuddy(self.doorComboBox)
        self.profileLabel.setBuddy(self.profileComboBox)
        self.employeeLabel.setBuddy(self.employeeComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.numberLineEdit, self.doorComboBox)
        QWidget.setTabOrder(self.doorComboBox, self.profileComboBox)
        QWidget.setTabOrder(self.profileComboBox, self.employeeComboBox)
        QWidget.setTabOrder(self.employeeComboBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(ChipCardInputArea)

        QMetaObject.connectSlotsByName(ChipCardInputArea)

    # setupUi

    def retranslateUi(self, ChipCardInputArea):
        ChipCardInputArea.setWindowTitle(
            QCoreApplication.translate("ChipCardInputArea", u"Schl\u00fcsselchip", None)
        )
        # if QT_CONFIG(accessibility)
        ChipCardInputArea.setAccessibleName(
            QCoreApplication.translate(
                "ChipCardInputArea", u"ChipCardInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        ChipCardInputArea.setTitle(
            QCoreApplication.translate("ChipCardInputArea", u"Schl\u00fcsselchip", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("ChipCardInputArea", u"Schl\u00fcsselchip", None)
        )
        self.numberLabel.setText(
            QCoreApplication.translate("ChipCardInputArea", u"Nummer", None)
        )
        self.doorLabel.setText(
            QCoreApplication.translate("ChipCardInputArea", u"T\u00fcr", None)
        )
        self.profileLabel.setText(
            QCoreApplication.translate("ChipCardInputArea", u"Profil", None)
        )
        self.employeeLabel.setText(
            QCoreApplication.translate("ChipCardInputArea", u"Mitarbeiter*in", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "ChipCardInputArea", u"Letzte \u00c4nderung", None
            )
        )
        self.addPushButton.setText(
            QCoreApplication.translate("ChipCardInputArea", u"+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("ChipCardInputArea", u"Bearbeiten", None)
        )

    # retranslateUi
