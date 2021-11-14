################################################################################
## Form generated from reading UI file 'companyinputarea.ui'
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
from PySide6.QtWidgets import QCheckBox
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QFormLayout
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


class Ui_CompanyInputArea:
    def setupUi(self, CompanyInputArea):
        if not CompanyInputArea.objectName():
            CompanyInputArea.setObjectName("CompanyInputArea")
        CompanyInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(CompanyInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(CompanyInputArea)
        self.GroupBox.setObjectName("GroupBox")
        self.GroupBox.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.GroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Header = QLabel(self.GroupBox)
        self.label_Header.setObjectName("label_Header")
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
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QLabel(self.GroupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLabel.setEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.GroupBox)
        self.nameLineEdit.setObjectName("nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.name2Label = QLabel(self.GroupBox)
        self.name2Label.setObjectName("name2Label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.name2Label)

        self.name2LineEdit = QLineEdit(self.GroupBox)
        self.name2LineEdit.setObjectName("name2LineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name2LineEdit)

        self.streetLabel = QLabel(self.GroupBox)
        self.streetLabel.setObjectName("streetLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.streetLabel)

        self.streetLineEdit = QLineEdit(self.GroupBox)
        self.streetLineEdit.setObjectName("streetLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.streetLineEdit)

        self.zipCodeLabel = QLabel(self.GroupBox)
        self.zipCodeLabel.setObjectName("zipCodeLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.zipCodeLabel)

        self.zipCodeLineEdit = QLineEdit(self.GroupBox)
        self.zipCodeLineEdit.setObjectName("zipCodeLineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.zipCodeLineEdit)

        self.cityLabel = QLabel(self.GroupBox)
        self.cityLabel.setObjectName("cityLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.cityLabel)

        self.cityLineEdit = QLineEdit(self.GroupBox)
        self.cityLineEdit.setObjectName("cityLineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cityLineEdit)

        self.phoneNumberLabel = QLabel(self.GroupBox)
        self.phoneNumberLabel.setObjectName("phoneNumberLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.phoneNumberLabel)

        self.phoneNumberLineEdit = QLineEdit(self.GroupBox)
        self.phoneNumberLineEdit.setObjectName("phoneNumberLineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.phoneNumberLineEdit)

        self.mobileNumberLabel = QLabel(self.GroupBox)
        self.mobileNumberLabel.setObjectName("mobileNumberLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.mobileNumberLabel)

        self.mobileNumberLineEdit = QLineEdit(self.GroupBox)
        self.mobileNumberLineEdit.setObjectName("mobileNumberLineEdit")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.mobileNumberLineEdit)

        self.faxNumberLabel = QLabel(self.GroupBox)
        self.faxNumberLabel.setObjectName("faxNumberLabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.faxNumberLabel)

        self.faxNumberLineEdit = QLineEdit(self.GroupBox)
        self.faxNumberLineEdit.setObjectName("faxNumberLineEdit")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.faxNumberLineEdit)

        self.mailAddressLabel = QLabel(self.GroupBox)
        self.mailAddressLabel.setObjectName("mailAddressLabel")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.mailAddressLabel)

        self.mailAddressLineEdit = QLineEdit(self.GroupBox)
        self.mailAddressLineEdit.setObjectName("mailAddressLineEdit")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.mailAddressLineEdit)

        self.activeLabel = QLabel(self.GroupBox)
        self.activeLabel.setObjectName("activeLabel")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.activeLabel)

        self.activeCheckBox = QCheckBox(self.GroupBox)
        self.activeCheckBox.setObjectName("activeCheckBox")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.activeCheckBox)

        self.employeeIdLabel = QLabel(self.GroupBox)
        self.employeeIdLabel.setObjectName("employeeIdLabel")
        self.employeeIdLabel.setEnabled(False)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.employeeIdLabel)

        self.employeeIdComboBox = QComboBox(self.GroupBox)
        self.employeeIdComboBox.setObjectName("employeeIdComboBox")
        self.employeeIdComboBox.setEnabled(False)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.employeeIdComboBox)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.lastUpdateLineEdit)

        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addPushButton = QPushButton(self.GroupBox)
        self.addPushButton.setObjectName("addPushButton")
        self.addPushButton.setEnabled(True)

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.GroupBox)
        self.editFinishPushButton.setObjectName("editFinishPushButton")
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
            QCoreApplication.translate("CompanyInputArea", "Firma", None)
        )
        # if QT_CONFIG(accessibility)
        CompanyInputArea.setAccessibleName(
            QCoreApplication.translate("CompanyInputArea", "CompanyInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        CompanyInputArea.setTitle(
            QCoreApplication.translate("CompanyInputArea", "Firma", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("CompanyInputArea", "Firma", None)
        )
        self.nameLabel.setText(
            QCoreApplication.translate("CompanyInputArea", "Name", None)
        )
        self.name2Label.setText(
            QCoreApplication.translate("CompanyInputArea", "Name2", None)
        )
        self.streetLabel.setText(
            QCoreApplication.translate("CompanyInputArea", "Stra\u00dfe", None)
        )
        self.zipCodeLabel.setText(
            QCoreApplication.translate("CompanyInputArea", "PLZ", None)
        )
        self.cityLabel.setText(
            QCoreApplication.translate("CompanyInputArea", "Ort", None)
        )
        self.phoneNumberLabel.setText(
            QCoreApplication.translate("CompanyInputArea", "Telefon", None)
        )
        self.mobileNumberLabel.setText(
            QCoreApplication.translate("CompanyInputArea", "Mobil Nummer", None)
        )
        self.faxNumberLabel.setText(
            QCoreApplication.translate("CompanyInputArea", "Fax", None)
        )
        self.mailAddressLabel.setText(
            QCoreApplication.translate("CompanyInputArea", "E Mail", None)
        )
        self.activeLabel.setText(
            QCoreApplication.translate("CompanyInputArea", "Aktiv", None)
        )
        self.employeeIdLabel.setText(
            QCoreApplication.translate("CompanyInputArea", "Mitarbeiter*in", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate("CompanyInputArea", "Letzte \u00c4nderung", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("CompanyInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("CompanyInputArea", "Bearbeiten", None)
        )

    # retranslateUi
