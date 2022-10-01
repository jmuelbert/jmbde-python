# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chipcarddoorinputarea.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_ChipCardDoorInputArea(object):
    def setupUi(self, ChipCardDoorInputArea):
        if not ChipCardDoorInputArea.objectName():
            ChipCardDoorInputArea.setObjectName(u"ChipCardDoorInputArea")
        ChipCardDoorInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(ChipCardDoorInputArea)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.GroupBox = QWidget(ChipCardDoorInputArea)
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

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.placeLabel = QLabel(self.GroupBox)
        self.placeLabel.setObjectName(u"placeLabel")
        self.placeLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.placeLabel)

        self.placeComboBox = QComboBox(self.GroupBox)
        self.placeComboBox.setObjectName(u"placeComboBox")
        self.placeComboBox.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.placeComboBox)

        self.departmentLabel = QLabel(self.GroupBox)
        self.departmentLabel.setObjectName(u"departmentLabel")
        self.departmentLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.departmentLabel)

        self.departmentComboBox = QComboBox(self.GroupBox)
        self.departmentComboBox.setObjectName(u"departmentComboBox")
        self.departmentComboBox.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.departmentComboBox)

        self.numberLabel = QLabel(self.GroupBox)
        self.numberLabel.setObjectName(u"numberLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.numberLabel)

        self.numberSpinBox = QSpinBox(self.GroupBox)
        self.numberSpinBox.setObjectName(u"numberSpinBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.numberSpinBox)

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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addPushButton = QPushButton(self.GroupBox)
        self.addPushButton.setObjectName(u"addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.GroupBox)
        self.editFinishPushButton.setObjectName(u"editFinishPushButton")

        self.horizontalLayout.addWidget(self.editFinishPushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout_3.addWidget(self.GroupBox, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.placeLabel.setBuddy(self.placeComboBox)
        self.departmentLabel.setBuddy(self.departmentComboBox)
        self.numberLabel.setBuddy(self.numberSpinBox)
        self.employeeLabel.setBuddy(self.employeeComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.numberSpinBox, self.placeComboBox)
        QWidget.setTabOrder(self.placeComboBox, self.departmentComboBox)
        QWidget.setTabOrder(self.departmentComboBox, self.employeeComboBox)
        QWidget.setTabOrder(self.employeeComboBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(ChipCardDoorInputArea)

        QMetaObject.connectSlotsByName(ChipCardDoorInputArea)
    # setupUi

    def retranslateUi(self, ChipCardDoorInputArea):
        ChipCardDoorInputArea.setWindowTitle(QCoreApplication.translate("ChipCardDoorInputArea", u"Schl\u00fcsselchip T\u00fcr", None))
#if QT_CONFIG(accessibility)
        ChipCardDoorInputArea.setAccessibleName(QCoreApplication.translate("ChipCardDoorInputArea", u"ChipCardDoorInputDialog", None))
#endif // QT_CONFIG(accessibility)
        ChipCardDoorInputArea.setTitle(QCoreApplication.translate("ChipCardDoorInputArea", u"Schl\u00fcsselchip T\u00fcr", None))
        self.label_Header.setText(QCoreApplication.translate("ChipCardDoorInputArea", u"Schl\u00fcsselchip T\u00fcr", None))
        self.placeLabel.setText(QCoreApplication.translate("ChipCardDoorInputArea", u"Ort", None))
        self.departmentLabel.setText(QCoreApplication.translate("ChipCardDoorInputArea", u"Abteilung", None))
        self.numberLabel.setText(QCoreApplication.translate("ChipCardDoorInputArea", u"Nummer", None))
        self.employeeLabel.setText(QCoreApplication.translate("ChipCardDoorInputArea", u"Mitarbeiter*in", None))
        self.lastUpdateLabel.setText(QCoreApplication.translate("ChipCardDoorInputArea", u"Letze \u00c4nderung", None))
        self.addPushButton.setText(QCoreApplication.translate("ChipCardDoorInputArea", u"+", None))
#if QT_CONFIG(accessibility)
        self.editFinishPushButton.setAccessibleName(QCoreApplication.translate("ChipCardDoorInputArea", u"ChipCardDoorDialog", None))
#endif // QT_CONFIG(accessibility)
        self.editFinishPushButton.setText(QCoreApplication.translate("ChipCardDoorInputArea", u"Bearbeiten", None))
    # retranslateUi

