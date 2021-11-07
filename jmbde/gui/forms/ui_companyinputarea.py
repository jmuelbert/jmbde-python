# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'companyinputarea.ui'
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
    QCheckBox,
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


class Ui_CompanyInputArea(object):
    def setupUi(self, CompanyInputArea):
        if not CompanyInputArea.objectName():
            CompanyInputArea.setObjectName(u"CompanyInputArea")
        CompanyInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(CompanyInputArea)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.GroupBox = QWidget(CompanyInputArea)
        self.GroupBox.setObjectName(u"GroupBox")
        self.GroupBox.setEnabled(True)
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
        self.nameLabel = QLabel(self.GroupBox)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.GroupBox)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.name2Label = QLabel(self.GroupBox)
        self.name2Label.setObjectName(u"name2Label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.name2Label)

        self.name2LineEdit = QLineEdit(self.GroupBox)
        self.name2LineEdit.setObjectName(u"name2LineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name2LineEdit)

        self.streetLabel = QLabel(self.GroupBox)
        self.streetLabel.setObjectName(u"streetLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.streetLabel)

        self.streetLineEdit = QLineEdit(self.GroupBox)
        self.streetLineEdit.setObjectName(u"streetLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.streetLineEdit)

        self.zipCodeLabel = QLabel(self.GroupBox)
        self.zipCodeLabel.setObjectName(u"zipCodeLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.zipCodeLabel)

        self.zipCodeLineEdit = QLineEdit(self.GroupBox)
        self.zipCodeLineEdit.setObjectName(u"zipCodeLineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.zipCodeLineEdit)

        self.cityLabel = QLabel(self.GroupBox)
        self.cityLabel.setObjectName(u"cityLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.cityLabel)

        self.cityLineEdit = QLineEdit(self.GroupBox)
        self.cityLineEdit.setObjectName(u"cityLineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cityLineEdit)

        self.phoneNumberLabel = QLabel(self.GroupBox)
        self.phoneNumberLabel.setObjectName(u"phoneNumberLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.phoneNumberLabel)

        self.phoneNumberLineEdit = QLineEdit(self.GroupBox)
        self.phoneNumberLineEdit.setObjectName(u"phoneNumberLineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.phoneNumberLineEdit)

        self.mobileNumberLabel = QLabel(self.GroupBox)
        self.mobileNumberLabel.setObjectName(u"mobileNumberLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.mobileNumberLabel)

        self.mobileNumberLineEdit = QLineEdit(self.GroupBox)
        self.mobileNumberLineEdit.setObjectName(u"mobileNumberLineEdit")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.mobileNumberLineEdit)

        self.faxNumberLabel = QLabel(self.GroupBox)
        self.faxNumberLabel.setObjectName(u"faxNumberLabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.faxNumberLabel)

        self.faxNumberLineEdit = QLineEdit(self.GroupBox)
        self.faxNumberLineEdit.setObjectName(u"faxNumberLineEdit")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.faxNumberLineEdit)

        self.mailAddressLabel = QLabel(self.GroupBox)
        self.mailAddressLabel.setObjectName(u"mailAddressLabel")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.mailAddressLabel)

        self.mailAddressLineEdit = QLineEdit(self.GroupBox)
        self.mailAddressLineEdit.setObjectName(u"mailAddressLineEdit")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.mailAddressLineEdit)

        self.activeLabel = QLabel(self.GroupBox)
        self.activeLabel.setObjectName(u"activeLabel")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.activeLabel)

        self.activeCheckBox = QCheckBox(self.GroupBox)
        self.activeCheckBox.setObjectName(u"activeCheckBox")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.activeCheckBox)

        self.employeeIdLabel = QLabel(self.GroupBox)
        self.employeeIdLabel.setObjectName(u"employeeIdLabel")
        self.employeeIdLabel.setEnabled(False)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.employeeIdLabel)

        self.employeeIdComboBox = QComboBox(self.GroupBox)
        self.employeeIdComboBox.setObjectName(u"employeeIdComboBox")
        self.employeeIdComboBox.setEnabled(False)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.employeeIdComboBox)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.lastUpdateLineEdit)

        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addPushButton = QPushButton(self.GroupBox)
        self.addPushButton.setObjectName(u"addPushButton")
        self.addPushButton.setEnabled(True)

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.GroupBox)
        self.editFinishPushButton.setObjectName(u"editFinishPushButton")
        self.editFinishPushButton.setEnabled(True)

        self.horizontalLayout.addWidget(self.editFinishPushButton)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.gridLayout_3.addWidget(self.GroupBox, 0, 0, 1, 1)

        # if QT_CONFIG(shortcut)
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.name2Label.setBuddy(self.name2LineEdit)
        self.streetLabel.setBuddy(self.streetLineEdit)
        self.zipCodeLabel.setBuddy(self.zipCodeLineEdit)
        self.cityLabel.setBuddy(self.cityLineEdit)
        self.phoneNumberLabel.setBuddy(self.phoneNumberLineEdit)
        self.mobileNumberLabel.setBuddy(self.mobileNumberLineEdit)
        self.faxNumberLabel.setBuddy(self.faxNumberLineEdit)
        self.mailAddressLabel.setBuddy(self.mailAddressLineEdit)
        self.activeLabel.setBuddy(self.activeCheckBox)
        self.employeeIdLabel.setBuddy(self.employeeIdComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameLineEdit, self.name2LineEdit)
        QWidget.setTabOrder(self.name2LineEdit, self.streetLineEdit)
        QWidget.setTabOrder(self.streetLineEdit, self.zipCodeLineEdit)
        QWidget.setTabOrder(self.zipCodeLineEdit, self.cityLineEdit)
        QWidget.setTabOrder(self.cityLineEdit, self.phoneNumberLineEdit)
        QWidget.setTabOrder(self.phoneNumberLineEdit, self.mobileNumberLineEdit)
        QWidget.setTabOrder(self.mobileNumberLineEdit, self.faxNumberLineEdit)
        QWidget.setTabOrder(self.faxNumberLineEdit, self.mailAddressLineEdit)
        QWidget.setTabOrder(self.mailAddressLineEdit, self.activeCheckBox)
        QWidget.setTabOrder(self.activeCheckBox, self.employeeIdComboBox)
        QWidget.setTabOrder(self.employeeIdComboBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(CompanyInputArea)

        QMetaObject.connectSlotsByName(CompanyInputArea)

    # setupUi

    def retranslateUi(self, CompanyInputArea):
        CompanyInputArea.setWindowTitle(
            QCoreApplication.translate("CompanyInputArea", u"Firma", None)
        )
        # if QT_CONFIG(accessibility)
        CompanyInputArea.setAccessibleName(
            QCoreApplication.translate("CompanyInputArea", u"CompanyInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        CompanyInputArea.setTitle(
            QCoreApplication.translate("CompanyInputArea", u"Firma", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("CompanyInputArea", u"Firma", None)
        )
        self.nameLabel.setText(
            QCoreApplication.translate("CompanyInputArea", u"Name", None)
        )
        self.name2Label.setText(
            QCoreApplication.translate("CompanyInputArea", u"Name2", None)
        )
        self.streetLabel.setText(
            QCoreApplication.translate("CompanyInputArea", u"Stra\u00dfe", None)
        )
        self.zipCodeLabel.setText(
            QCoreApplication.translate("CompanyInputArea", u"PLZ", None)
        )
        self.cityLabel.setText(
            QCoreApplication.translate("CompanyInputArea", u"Ort", None)
        )
        self.phoneNumberLabel.setText(
            QCoreApplication.translate("CompanyInputArea", u"Telefon", None)
        )
        self.mobileNumberLabel.setText(
            QCoreApplication.translate("CompanyInputArea", u"Mobil Nummer", None)
        )
        self.faxNumberLabel.setText(
            QCoreApplication.translate("CompanyInputArea", u"Fax", None)
        )
        self.mailAddressLabel.setText(
            QCoreApplication.translate("CompanyInputArea", u"E Mail", None)
        )
        self.activeLabel.setText(
            QCoreApplication.translate("CompanyInputArea", u"Aktiv", None)
        )
        self.employeeIdLabel.setText(
            QCoreApplication.translate("CompanyInputArea", u"Mitarbeiter*in", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "CompanyInputArea", u"Letzte \u00c4nderung", None
            )
        )
        self.addPushButton.setText(
            QCoreApplication.translate("CompanyInputArea", u"+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("CompanyInputArea", u"Bearbeiten", None)
        )

    # retranslateUi
