# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manufacturerinputarea.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ManufacturerInputArea(object):
    def setupUi(self, ManufacturerInputArea):
        if not ManufacturerInputArea.objectName():
            ManufacturerInputArea.setObjectName(u"ManufacturerInputArea")
        ManufacturerInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(ManufacturerInputArea)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.GroupBox = QWidget(ManufacturerInputArea)
        self.GroupBox.setObjectName(u"GroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.GroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerLabel = QLabel(self.GroupBox)
        self.headerLabel.setObjectName(u"headerLabel")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.headerLabel)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.phoneNumberLineEdit = QLineEdit(self.GroupBox)
        self.phoneNumberLineEdit.setObjectName(u"phoneNumberLineEdit")

        self.gridLayout.addWidget(self.phoneNumberLineEdit, 7, 1, 1, 3)

        self.nameLineEdit = QLineEdit(self.GroupBox)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 3)

        self.cityLineEdit = QLineEdit(self.GroupBox)
        self.cityLineEdit.setObjectName(u"cityLineEdit")
        self.cityLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.cityLineEdit, 3, 3, 1, 1)

        self.zipCodeLabel = QLabel(self.GroupBox)
        self.zipCodeLabel.setObjectName(u"zipCodeLabel")
        self.zipCodeLabel.setEnabled(False)

        self.gridLayout.addWidget(self.zipCodeLabel, 3, 0, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 10, 1, 1, 3)

        self.zipCodeComboBox = QComboBox(self.GroupBox)
        self.zipCodeComboBox.setObjectName(u"zipCodeComboBox")
        self.zipCodeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.zipCodeComboBox, 3, 1, 1, 1)

        self.hotlineNumberLabel = QLabel(self.GroupBox)
        self.hotlineNumberLabel.setObjectName(u"hotlineNumberLabel")

        self.gridLayout.addWidget(self.hotlineNumberLabel, 8, 0, 1, 1)

        self.nameLabel = QLabel(self.GroupBox)
        self.nameLabel.setObjectName(u"nameLabel")

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.mailAddressLabel = QLabel(self.GroupBox)
        self.mailAddressLabel.setObjectName(u"mailAddressLabel")

        self.gridLayout.addWidget(self.mailAddressLabel, 6, 0, 1, 1)

        self.faxNumberLabel = QLabel(self.GroupBox)
        self.faxNumberLabel.setObjectName(u"faxNumberLabel")

        self.gridLayout.addWidget(self.faxNumberLabel, 9, 0, 1, 1)

        self.addressLineEdit = QLineEdit(self.GroupBox)
        self.addressLineEdit.setObjectName(u"addressLineEdit")

        self.gridLayout.addWidget(self.addressLineEdit, 4, 1, 1, 3)

        self.cityLabel = QLabel(self.GroupBox)
        self.cityLabel.setObjectName(u"cityLabel")
        self.cityLabel.setEnabled(False)

        self.gridLayout.addWidget(self.cityLabel, 3, 2, 1, 1)

        self.name2LineEdit = QLineEdit(self.GroupBox)
        self.name2LineEdit.setObjectName(u"name2LineEdit")

        self.gridLayout.addWidget(self.name2LineEdit, 1, 1, 1, 3)

        self.supporterLineEdit = QLineEdit(self.GroupBox)
        self.supporterLineEdit.setObjectName(u"supporterLineEdit")

        self.gridLayout.addWidget(self.supporterLineEdit, 2, 1, 1, 3)

        self.name2Label = QLabel(self.GroupBox)
        self.name2Label.setObjectName(u"name2Label")

        self.gridLayout.addWidget(self.name2Label, 1, 0, 1, 1)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 10, 0, 1, 1)

        self.supporterLabel = QLabel(self.GroupBox)
        self.supporterLabel.setObjectName(u"supporterLabel")

        self.gridLayout.addWidget(self.supporterLabel, 2, 0, 1, 1)

        self.addressLabel = QLabel(self.GroupBox)
        self.addressLabel.setObjectName(u"addressLabel")

        self.gridLayout.addWidget(self.addressLabel, 4, 0, 1, 1)

        self.mailAddressLineEdit = QLineEdit(self.GroupBox)
        self.mailAddressLineEdit.setObjectName(u"mailAddressLineEdit")

        self.gridLayout.addWidget(self.mailAddressLineEdit, 6, 1, 1, 3)

        self.phoneNumberLabel = QLabel(self.GroupBox)
        self.phoneNumberLabel.setObjectName(u"phoneNumberLabel")

        self.gridLayout.addWidget(self.phoneNumberLabel, 7, 0, 1, 1)

        self.hotlineNumberLineEdit = QLineEdit(self.GroupBox)
        self.hotlineNumberLineEdit.setObjectName(u"hotlineNumberLineEdit")

        self.gridLayout.addWidget(self.hotlineNumberLineEdit, 8, 1, 1, 3)

        self.faxNumberLineEdit = QLineEdit(self.GroupBox)
        self.faxNumberLineEdit.setObjectName(u"faxNumberLineEdit")

        self.gridLayout.addWidget(self.faxNumberLineEdit, 9, 1, 1, 3)

        self.address2Label = QLabel(self.GroupBox)
        self.address2Label.setObjectName(u"address2Label")

        self.gridLayout.addWidget(self.address2Label, 5, 0, 1, 1)

        self.address2LineEdit = QLineEdit(self.GroupBox)
        self.address2LineEdit.setObjectName(u"address2LineEdit")

        self.gridLayout.addWidget(self.address2LineEdit, 5, 1, 1, 3)


        self.verticalLayout_3.addLayout(self.gridLayout)

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
        self.zipCodeLabel.setBuddy(self.zipCodeComboBox)
        self.hotlineNumberLabel.setBuddy(self.hotlineNumberLineEdit)
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.mailAddressLabel.setBuddy(self.mailAddressLineEdit)
        self.faxNumberLabel.setBuddy(self.faxNumberLineEdit)
        self.cityLabel.setBuddy(self.cityLineEdit)
        self.name2Label.setBuddy(self.name2LineEdit)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        self.supporterLabel.setBuddy(self.supporterLineEdit)
        self.addressLabel.setBuddy(self.addressLineEdit)
        self.phoneNumberLabel.setBuddy(self.phoneNumberLineEdit)
        self.address2Label.setBuddy(self.address2LineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameLineEdit, self.name2LineEdit)
        QWidget.setTabOrder(self.name2LineEdit, self.supporterLineEdit)
        QWidget.setTabOrder(self.supporterLineEdit, self.zipCodeComboBox)
        QWidget.setTabOrder(self.zipCodeComboBox, self.cityLineEdit)
        QWidget.setTabOrder(self.cityLineEdit, self.addressLineEdit)
        QWidget.setTabOrder(self.addressLineEdit, self.address2LineEdit)
        QWidget.setTabOrder(self.address2LineEdit, self.mailAddressLineEdit)
        QWidget.setTabOrder(self.mailAddressLineEdit, self.phoneNumberLineEdit)
        QWidget.setTabOrder(self.phoneNumberLineEdit, self.hotlineNumberLineEdit)
        QWidget.setTabOrder(self.hotlineNumberLineEdit, self.faxNumberLineEdit)
        QWidget.setTabOrder(self.faxNumberLineEdit, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(ManufacturerInputArea)

        QMetaObject.connectSlotsByName(ManufacturerInputArea)
    # setupUi

    def retranslateUi(self, ManufacturerInputArea):
        ManufacturerInputArea.setWindowTitle(QCoreApplication.translate("ManufacturerInputArea", u"Hersteller", None))
#if QT_CONFIG(accessibility)
        ManufacturerInputArea.setAccessibleName(QCoreApplication.translate("ManufacturerInputArea", u"ManufacturerInputDialog", None))
#endif // QT_CONFIG(accessibility)
        ManufacturerInputArea.setTitle(QCoreApplication.translate("ManufacturerInputArea", u"Hersteller", None))
        self.headerLabel.setText(QCoreApplication.translate("ManufacturerInputArea", u"Hersteller", None))
        self.zipCodeLabel.setText(QCoreApplication.translate("ManufacturerInputArea", u"PLZ", None))
        self.hotlineNumberLabel.setText(QCoreApplication.translate("ManufacturerInputArea", u"Hotline", None))
        self.nameLabel.setText(QCoreApplication.translate("ManufacturerInputArea", u"Name", None))
        self.mailAddressLabel.setText(QCoreApplication.translate("ManufacturerInputArea", u"Mail", None))
        self.faxNumberLabel.setText(QCoreApplication.translate("ManufacturerInputArea", u"Fax", None))
        self.cityLabel.setText(QCoreApplication.translate("ManufacturerInputArea", u"Ort", None))
        self.name2Label.setText(QCoreApplication.translate("ManufacturerInputArea", u"Name2", None))
        self.lastUpdateLabel.setText(QCoreApplication.translate("ManufacturerInputArea", u"Letzte \u00c4nderung", None))
        self.supporterLabel.setText(QCoreApplication.translate("ManufacturerInputArea", u"Supporter", None))
        self.addressLabel.setText(QCoreApplication.translate("ManufacturerInputArea", u"Stra\u00dfe", None))
        self.phoneNumberLabel.setText(QCoreApplication.translate("ManufacturerInputArea", u"Telefon", None))
        self.address2Label.setText(QCoreApplication.translate("ManufacturerInputArea", u"Stra\u00dfe 2", None))
        self.addPushButton.setText(QCoreApplication.translate("ManufacturerInputArea", u"+", None))
        self.editFinishPushButton.setText(QCoreApplication.translate("ManufacturerInputArea", u"Bearbeiten", None))
    # retranslateUi

