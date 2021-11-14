################################################################################
## Form generated from reading UI file 'manufacturerinputarea.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QDate
from PySide6.QtCore import QDateTime
from PySide6.QtCore import QLocale
from PySide6.QtCore import QMetaObject
from PySide6.QtCore import QObject
from PySide6.QtCore import QPoint
from PySide6.QtCore import QRect
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtCore import QTime
from PySide6.QtCore import QUrl
from PySide6.QtGui import QBrush
from PySide6.QtGui import QColor
from PySide6.QtGui import QConicalGradient
from PySide6.QtGui import QCursor
from PySide6.QtGui import QFont
from PySide6.QtGui import QFontDatabase
from PySide6.QtGui import QGradient
from PySide6.QtGui import QIcon
from PySide6.QtGui import QImage
from PySide6.QtGui import QKeySequence
from PySide6.QtGui import QLinearGradient
from PySide6.QtGui import QPainter
from PySide6.QtGui import QPalette
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QRadialGradient
from PySide6.QtGui import QTransform
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QGroupBox
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class Ui_ManufacturerInputArea:
    def setupUi(self, ManufacturerInputArea):
        if not ManufacturerInputArea.objectName():
            ManufacturerInputArea.setObjectName("ManufacturerInputArea")
        ManufacturerInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(ManufacturerInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(ManufacturerInputArea)
        self.GroupBox.setObjectName("GroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.GroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QLabel(self.GroupBox)
        self.headerLabel.setObjectName("headerLabel")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.headerLabel)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.phoneNumberLineEdit = QLineEdit(self.GroupBox)
        self.phoneNumberLineEdit.setObjectName("phoneNumberLineEdit")

        self.gridLayout.addWidget(self.phoneNumberLineEdit, 7, 1, 1, 3)

        self.nameLineEdit = QLineEdit(self.GroupBox)
        self.nameLineEdit.setObjectName("nameLineEdit")

        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 3)

        self.cityLineEdit = QLineEdit(self.GroupBox)
        self.cityLineEdit.setObjectName("cityLineEdit")
        self.cityLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.cityLineEdit, 3, 3, 1, 1)

        self.zipCodeLabel = QLabel(self.GroupBox)
        self.zipCodeLabel.setObjectName("zipCodeLabel")
        self.zipCodeLabel.setEnabled(False)

        self.gridLayout.addWidget(self.zipCodeLabel, 3, 0, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 10, 1, 1, 3)

        self.zipCodeComboBox = QComboBox(self.GroupBox)
        self.zipCodeComboBox.setObjectName("zipCodeComboBox")
        self.zipCodeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.zipCodeComboBox, 3, 1, 1, 1)

        self.hotlineNumberLabel = QLabel(self.GroupBox)
        self.hotlineNumberLabel.setObjectName("hotlineNumberLabel")

        self.gridLayout.addWidget(self.hotlineNumberLabel, 8, 0, 1, 1)

        self.nameLabel = QLabel(self.GroupBox)
        self.nameLabel.setObjectName("nameLabel")

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.mailAddressLabel = QLabel(self.GroupBox)
        self.mailAddressLabel.setObjectName("mailAddressLabel")

        self.gridLayout.addWidget(self.mailAddressLabel, 6, 0, 1, 1)

        self.faxNumberLabel = QLabel(self.GroupBox)
        self.faxNumberLabel.setObjectName("faxNumberLabel")

        self.gridLayout.addWidget(self.faxNumberLabel, 9, 0, 1, 1)

        self.addressLineEdit = QLineEdit(self.GroupBox)
        self.addressLineEdit.setObjectName("addressLineEdit")

        self.gridLayout.addWidget(self.addressLineEdit, 4, 1, 1, 3)

        self.cityLabel = QLabel(self.GroupBox)
        self.cityLabel.setObjectName("cityLabel")
        self.cityLabel.setEnabled(False)

        self.gridLayout.addWidget(self.cityLabel, 3, 2, 1, 1)

        self.name2LineEdit = QLineEdit(self.GroupBox)
        self.name2LineEdit.setObjectName("name2LineEdit")

        self.gridLayout.addWidget(self.name2LineEdit, 1, 1, 1, 3)

        self.supporterLineEdit = QLineEdit(self.GroupBox)
        self.supporterLineEdit.setObjectName("supporterLineEdit")

        self.gridLayout.addWidget(self.supporterLineEdit, 2, 1, 1, 3)

        self.name2Label = QLabel(self.GroupBox)
        self.name2Label.setObjectName("name2Label")

        self.gridLayout.addWidget(self.name2Label, 1, 0, 1, 1)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 10, 0, 1, 1)

        self.supporterLabel = QLabel(self.GroupBox)
        self.supporterLabel.setObjectName("supporterLabel")

        self.gridLayout.addWidget(self.supporterLabel, 2, 0, 1, 1)

        self.addressLabel = QLabel(self.GroupBox)
        self.addressLabel.setObjectName("addressLabel")

        self.gridLayout.addWidget(self.addressLabel, 4, 0, 1, 1)

        self.mailAddressLineEdit = QLineEdit(self.GroupBox)
        self.mailAddressLineEdit.setObjectName("mailAddressLineEdit")

        self.gridLayout.addWidget(self.mailAddressLineEdit, 6, 1, 1, 3)

        self.phoneNumberLabel = QLabel(self.GroupBox)
        self.phoneNumberLabel.setObjectName("phoneNumberLabel")

        self.gridLayout.addWidget(self.phoneNumberLabel, 7, 0, 1, 1)

        self.hotlineNumberLineEdit = QLineEdit(self.GroupBox)
        self.hotlineNumberLineEdit.setObjectName("hotlineNumberLineEdit")

        self.gridLayout.addWidget(self.hotlineNumberLineEdit, 8, 1, 1, 3)

        self.faxNumberLineEdit = QLineEdit(self.GroupBox)
        self.faxNumberLineEdit.setObjectName("faxNumberLineEdit")

        self.gridLayout.addWidget(self.faxNumberLineEdit, 9, 1, 1, 3)

        self.address2Label = QLabel(self.GroupBox)
        self.address2Label.setObjectName("address2Label")

        self.gridLayout.addWidget(self.address2Label, 5, 0, 1, 1)

        self.address2LineEdit = QLineEdit(self.GroupBox)
        self.address2LineEdit.setObjectName("address2LineEdit")

        self.gridLayout.addWidget(self.address2LineEdit, 5, 1, 1, 3)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addPushButton = QPushButton(self.GroupBox)
        self.addPushButton.setObjectName("addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.GroupBox)
        self.editFinishPushButton.setObjectName("editFinishPushButton")

        self.horizontalLayout.addWidget(self.editFinishPushButton)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.gridLayout_3.addWidget(self.GroupBox, 0, 0, 1, 1)

        # if QT_CONFIG(shortcut)
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
        # endif // QT_CONFIG(shortcut)
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
        ManufacturerInputArea.setWindowTitle(
            QCoreApplication.translate("ManufacturerInputArea", "Hersteller", None)
        )
        # if QT_CONFIG(accessibility)
        ManufacturerInputArea.setAccessibleName(
            QCoreApplication.translate(
                "ManufacturerInputArea", "ManufacturerInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        ManufacturerInputArea.setTitle(
            QCoreApplication.translate("ManufacturerInputArea", "Hersteller", None)
        )
        self.headerLabel.setText(
            QCoreApplication.translate("ManufacturerInputArea", "Hersteller", None)
        )
        self.zipCodeLabel.setText(
            QCoreApplication.translate("ManufacturerInputArea", "PLZ", None)
        )
        self.hotlineNumberLabel.setText(
            QCoreApplication.translate("ManufacturerInputArea", "Hotline", None)
        )
        self.nameLabel.setText(
            QCoreApplication.translate("ManufacturerInputArea", "Name", None)
        )
        self.mailAddressLabel.setText(
            QCoreApplication.translate("ManufacturerInputArea", "Mail", None)
        )
        self.faxNumberLabel.setText(
            QCoreApplication.translate("ManufacturerInputArea", "Fax", None)
        )
        self.cityLabel.setText(
            QCoreApplication.translate("ManufacturerInputArea", "Ort", None)
        )
        self.name2Label.setText(
            QCoreApplication.translate("ManufacturerInputArea", "Name2", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "ManufacturerInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.supporterLabel.setText(
            QCoreApplication.translate("ManufacturerInputArea", "Supporter", None)
        )
        self.addressLabel.setText(
            QCoreApplication.translate("ManufacturerInputArea", "Stra\u00dfe", None)
        )
        self.phoneNumberLabel.setText(
            QCoreApplication.translate("ManufacturerInputArea", "Telefon", None)
        )
        self.address2Label.setText(
            QCoreApplication.translate("ManufacturerInputArea", "Stra\u00dfe 2", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("ManufacturerInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("ManufacturerInputArea", "Bearbeiten", None)
        )

    # retranslateUi
