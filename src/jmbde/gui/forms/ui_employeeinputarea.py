# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employeeinputarea.ui'
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
    QDateEdit,
    QDoubleSpinBox,
    QGraphicsView,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Ui_EmployeeInputArea(object):
    def setupUi(self, EmployeeInputArea):
        if not EmployeeInputArea.objectName():
            EmployeeInputArea.setObjectName("EmployeeInputArea")
        EmployeeInputArea.resize(730, 637)
        self.verticalLayout_3 = QVBoxLayout(EmployeeInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayoutWidget = QWidget(EmployeeInputArea)
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
        self.phoneLabel = QLabel(self.formLayoutWidget)
        self.phoneLabel.setObjectName("phoneLabel")
        self.phoneLabel.setEnabled(False)

        self.gridLayout.addWidget(self.phoneLabel, 8, 0, 1, 1)

        self.zipCityIdComboBox = QComboBox(self.formLayoutWidget)
        self.zipCityIdComboBox.setObjectName("zipCityIdComboBox")
        self.zipCityIdComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.zipCityIdComboBox, 3, 1, 1, 1)

        self.employeeDocumentLabel = QLabel(self.formLayoutWidget)
        self.employeeDocumentLabel.setObjectName("employeeDocumentLabel")
        self.employeeDocumentLabel.setEnabled(False)

        self.gridLayout.addWidget(self.employeeDocumentLabel, 11, 2, 1, 1)

        self.functionComboBox = QComboBox(self.formLayoutWidget)
        self.functionComboBox.setObjectName("functionComboBox")
        self.functionComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.functionComboBox, 10, 3, 1, 1)

        self.departmentLabel = QLabel(self.formLayoutWidget)
        self.departmentLabel.setObjectName("departmentLabel")
        self.departmentLabel.setEnabled(False)

        self.gridLayout.addWidget(self.departmentLabel, 10, 0, 1, 1)

        self.phoneComboBox = QComboBox(self.formLayoutWidget)
        self.phoneComboBox.setObjectName("phoneComboBox")
        self.phoneComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.phoneComboBox, 8, 1, 1, 1)

        self.endDateLabel = QLabel(self.formLayoutWidget)
        self.endDateLabel.setObjectName("endDateLabel")

        self.gridLayout.addWidget(self.endDateLabel, 7, 4, 1, 1)

        self.homeMobileLineEdit = QLineEdit(self.formLayoutWidget)
        self.homeMobileLineEdit.setObjectName("homeMobileLineEdit")

        self.gridLayout.addWidget(self.homeMobileLineEdit, 5, 3, 1, 1)

        self.faxLabel = QLabel(self.formLayoutWidget)
        self.faxLabel.setObjectName("faxLabel")
        self.faxLabel.setEnabled(False)

        self.gridLayout.addWidget(self.faxLabel, 8, 4, 1, 1)

        self.homePhonelabel = QLabel(self.formLayoutWidget)
        self.homePhonelabel.setObjectName("homePhonelabel")

        self.gridLayout.addWidget(self.homePhonelabel, 5, 4, 1, 1)

        self.homePhoneLineEdit = QLineEdit(self.formLayoutWidget)
        self.homePhoneLineEdit.setObjectName("homePhoneLineEdit")

        self.gridLayout.addWidget(self.homePhoneLineEdit, 5, 5, 1, 1)

        self.chipCardComboBox = QComboBox(self.formLayoutWidget)
        self.chipCardComboBox.setObjectName("chipCardComboBox")
        self.chipCardComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.chipCardComboBox, 9, 5, 1, 1)

        self.lastNameLabel = QLabel(self.formLayoutWidget)
        self.lastNameLabel.setObjectName("lastNameLabel")

        self.gridLayout.addWidget(self.lastNameLabel, 1, 3, 1, 1)

        self.hireDateDateEdit = QDateEdit(self.formLayoutWidget)
        self.hireDateDateEdit.setObjectName("hireDateDateEdit")

        self.gridLayout.addWidget(self.hireDateDateEdit, 7, 3, 1, 1)

        self.businessMailLabel = QLabel(self.formLayoutWidget)
        self.businessMailLabel.setObjectName("businessMailLabel")

        self.gridLayout.addWidget(self.businessMailLabel, 7, 0, 1, 1)

        self.titleComboBox = QComboBox(self.formLayoutWidget)
        self.titleComboBox.setObjectName("titleComboBox")
        self.titleComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.titleComboBox, 0, 1, 1, 1)

        self.departmentComboBox = QComboBox(self.formLayoutWidget)
        self.departmentComboBox.setObjectName("departmentComboBox")
        self.departmentComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.departmentComboBox, 10, 1, 1, 1)

        self.notesLabel = QLabel(self.formLayoutWidget)
        self.notesLabel.setObjectName("notesLabel")

        self.gridLayout.addWidget(self.notesLabel, 12, 0, 1, 1)

        self.hireDateLabel = QLabel(self.formLayoutWidget)
        self.hireDateLabel.setObjectName("hireDateLabel")

        self.gridLayout.addWidget(self.hireDateLabel, 7, 2, 1, 1)

        self.computerComboBox = QComboBox(self.formLayoutWidget)
        self.computerComboBox.setObjectName("computerComboBox")
        self.computerComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.computerComboBox, 9, 1, 1, 1)

        self.printerComboBox = QComboBox(self.formLayoutWidget)
        self.printerComboBox.setObjectName("printerComboBox")
        self.printerComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.printerComboBox, 9, 3, 1, 1)

        self.firstNameLabel = QLabel(self.formLayoutWidget)
        self.firstNameLabel.setObjectName("firstNameLabel")

        self.gridLayout.addWidget(self.firstNameLabel, 1, 0, 1, 1)

        self.homeMailLineEdit = QLineEdit(self.formLayoutWidget)
        self.homeMailLineEdit.setObjectName("homeMailLineEdit")

        self.gridLayout.addWidget(self.homeMailLineEdit, 5, 1, 1, 1)

        self.businessMailLineEdit = QLineEdit(self.formLayoutWidget)
        self.businessMailLineEdit.setObjectName("businessMailLineEdit")

        self.gridLayout.addWidget(self.businessMailLineEdit, 7, 1, 1, 1)

        self.zipCityIdLabel = QLabel(self.formLayoutWidget)
        self.zipCityIdLabel.setObjectName("zipCityIdLabel")
        self.zipCityIdLabel.setEnabled(False)

        self.gridLayout.addWidget(self.zipCityIdLabel, 3, 0, 1, 1)

        self.computerLabel = QLabel(self.formLayoutWidget)
        self.computerLabel.setObjectName("computerLabel")
        self.computerLabel.setEnabled(False)

        self.gridLayout.addWidget(self.computerLabel, 9, 0, 1, 1)

        self.homeMobilelabel = QLabel(self.formLayoutWidget)
        self.homeMobilelabel.setObjectName("homeMobilelabel")

        self.gridLayout.addWidget(self.homeMobilelabel, 5, 2, 1, 1)

        self.activeCheckBox = QCheckBox(self.formLayoutWidget)
        self.activeCheckBox.setObjectName("activeCheckBox")

        self.gridLayout.addWidget(self.activeCheckBox, 6, 4, 1, 1)

        self.chipCardLabel = QLabel(self.formLayoutWidget)
        self.chipCardLabel.setObjectName("chipCardLabel")
        self.chipCardLabel.setEnabled(False)

        self.gridLayout.addWidget(self.chipCardLabel, 9, 4, 1, 1)

        self.genderComboBox = QComboBox(self.formLayoutWidget)
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.genderComboBox, 0, 3, 1, 1)

        self.endDateDateEdit = QDateEdit(self.formLayoutWidget)
        self.endDateDateEdit.setObjectName("endDateDateEdit")

        self.gridLayout.addWidget(self.endDateDateEdit, 7, 5, 1, 1)

        self.mobileLabel = QLabel(self.formLayoutWidget)
        self.mobileLabel.setObjectName("mobileLabel")
        self.mobileLabel.setEnabled(False)

        self.gridLayout.addWidget(self.mobileLabel, 8, 2, 1, 1)

        self.faxComboBox = QComboBox(self.formLayoutWidget)
        self.faxComboBox.setObjectName("faxComboBox")
        self.faxComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.faxComboBox, 8, 5, 1, 1)

        self.notesTextEdit = QTextEdit(self.formLayoutWidget)
        self.notesTextEdit.setObjectName("notesTextEdit")

        self.gridLayout.addWidget(self.notesTextEdit, 12, 1, 1, 2)

        self.functionLabel = QLabel(self.formLayoutWidget)
        self.functionLabel.setObjectName("functionLabel")
        self.functionLabel.setEnabled(False)

        self.gridLayout.addWidget(self.functionLabel, 10, 2, 1, 1)

        self.cityLabel = QLabel(self.formLayoutWidget)
        self.cityLabel.setObjectName("cityLabel")
        self.cityLabel.setEnabled(False)

        self.gridLayout.addWidget(self.cityLabel, 3, 2, 1, 1)

        self.employeeNumberDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.employeeNumberDoubleSpinBox.setObjectName("employeeNumberDoubleSpinBox")
        self.employeeNumberDoubleSpinBox.setDecimals(0)
        self.employeeNumberDoubleSpinBox.setMaximum(1000.000000000000000)

        self.gridLayout.addWidget(self.employeeNumberDoubleSpinBox, 0, 5, 1, 1)

        self.dataCareCheckBox = QCheckBox(self.formLayoutWidget)
        self.dataCareCheckBox.setObjectName("dataCareCheckBox")

        self.gridLayout.addWidget(self.dataCareCheckBox, 6, 5, 1, 1)

        self.photoLabel = QLabel(self.formLayoutWidget)
        self.photoLabel.setObjectName("photoLabel")
        self.photoLabel.setEnabled(False)

        self.gridLayout.addWidget(self.photoLabel, 12, 3, 1, 1)

        self.titleLabel = QLabel(self.formLayoutWidget)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setEnabled(False)

        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.printerLabel = QLabel(self.formLayoutWidget)
        self.printerLabel.setObjectName("printerLabel")
        self.printerLabel.setEnabled(False)

        self.gridLayout.addWidget(self.printerLabel, 9, 2, 1, 1)

        self.mobileComboBox = QComboBox(self.formLayoutWidget)
        self.mobileComboBox.setObjectName("mobileComboBox")
        self.mobileComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.mobileComboBox, 8, 3, 1, 1)

        self.employeeDocumentComboBox = QComboBox(self.formLayoutWidget)
        self.employeeDocumentComboBox.setObjectName("employeeDocumentComboBox")
        self.employeeDocumentComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.employeeDocumentComboBox, 11, 3, 1, 1)

        self.homeMailLabel = QLabel(self.formLayoutWidget)
        self.homeMailLabel.setObjectName("homeMailLabel")

        self.gridLayout.addWidget(self.homeMailLabel, 5, 0, 1, 1)

        self.photoGraphicsView = QGraphicsView(self.formLayoutWidget)
        self.photoGraphicsView.setObjectName("photoGraphicsView")
        self.photoGraphicsView.setEnabled(False)

        self.gridLayout.addWidget(self.photoGraphicsView, 12, 4, 1, 1)

        self.genderLabel = QLabel(self.formLayoutWidget)
        self.genderLabel.setObjectName("genderLabel")
        self.genderLabel.setEnabled(False)

        self.gridLayout.addWidget(self.genderLabel, 0, 2, 1, 1)

        self.employeeNumberLabel = QLabel(self.formLayoutWidget)
        self.employeeNumberLabel.setObjectName("employeeNumberLabel")

        self.gridLayout.addWidget(self.employeeNumberLabel, 0, 4, 1, 1)

        self.lastUpdateLabel = QLabel(self.formLayoutWidget)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 13, 0, 1, 1)

        self.employeeAccountLabel = QLabel(self.formLayoutWidget)
        self.employeeAccountLabel.setObjectName("employeeAccountLabel")
        self.employeeAccountLabel.setEnabled(False)

        self.gridLayout.addWidget(self.employeeAccountLabel, 10, 4, 1, 1)

        self.employeeAccountComboBox = QComboBox(self.formLayoutWidget)
        self.employeeAccountComboBox.setObjectName("employeeAccountComboBox")
        self.employeeAccountComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.employeeAccountComboBox, 10, 5, 1, 1)

        self.firstNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")

        self.gridLayout.addWidget(self.firstNameLineEdit, 1, 1, 1, 2)

        self.lastNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")

        self.gridLayout.addWidget(self.lastNameLineEdit, 1, 4, 1, 2)

        self.birthdayDateEdit = QDateEdit(self.formLayoutWidget)
        self.birthdayDateEdit.setObjectName("birthdayDateEdit")

        self.gridLayout.addWidget(self.birthdayDateEdit, 4, 5, 1, 1)

        self.birthdayLabel = QLabel(self.formLayoutWidget)
        self.birthdayLabel.setObjectName("birthdayLabel")

        self.gridLayout.addWidget(self.birthdayLabel, 4, 4, 1, 1)

        self.streetLabel = QLabel(self.formLayoutWidget)
        self.streetLabel.setObjectName("streetLabel")

        self.gridLayout.addWidget(self.streetLabel, 4, 0, 1, 1)

        self.addressLineEdit = QLineEdit(self.formLayoutWidget)
        self.addressLineEdit.setObjectName("addressLineEdit")

        self.gridLayout.addWidget(self.addressLineEdit, 4, 1, 1, 3)

        self.cityLineEdit = QLineEdit(self.formLayoutWidget)
        self.cityLineEdit.setObjectName("cityLineEdit")
        self.cityLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.cityLineEdit, 3, 3, 1, 3)

        self.lastUpdateLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 13, 1, 1, 5)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addPushButton = QPushButton(self.formLayoutWidget)
        self.addPushButton.setObjectName("addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.formLayoutWidget)
        self.editFinishPushButton.setObjectName("editFinishPushButton")

        self.horizontalLayout.addWidget(self.editFinishPushButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addWidget(self.formLayoutWidget)

        # if QT_CONFIG(shortcut)
        self.phoneLabel.setBuddy(self.phoneComboBox)
        self.employeeDocumentLabel.setBuddy(self.employeeDocumentComboBox)
        self.departmentLabel.setBuddy(self.departmentComboBox)
        self.endDateLabel.setBuddy(self.endDateDateEdit)
        self.faxLabel.setBuddy(self.faxComboBox)
        self.homePhonelabel.setBuddy(self.homePhoneLineEdit)
        self.lastNameLabel.setBuddy(self.lastNameLineEdit)
        self.businessMailLabel.setBuddy(self.businessMailLineEdit)
        self.notesLabel.setBuddy(self.notesTextEdit)
        self.hireDateLabel.setBuddy(self.hireDateDateEdit)
        self.firstNameLabel.setBuddy(self.firstNameLineEdit)
        self.zipCityIdLabel.setBuddy(self.zipCityIdComboBox)
        self.computerLabel.setBuddy(self.computerComboBox)
        self.homeMobilelabel.setBuddy(self.homeMobileLineEdit)
        self.chipCardLabel.setBuddy(self.chipCardComboBox)
        self.mobileLabel.setBuddy(self.mobileComboBox)
        self.functionLabel.setBuddy(self.functionComboBox)
        self.cityLabel.setBuddy(self.cityLineEdit)
        self.titleLabel.setBuddy(self.titleComboBox)
        self.printerLabel.setBuddy(self.printerComboBox)
        self.homeMailLabel.setBuddy(self.homeMailLineEdit)
        self.genderLabel.setBuddy(self.genderComboBox)
        self.employeeNumberLabel.setBuddy(self.employeeNumberDoubleSpinBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        self.employeeAccountLabel.setBuddy(self.employeeAccountComboBox)
        self.birthdayLabel.setBuddy(self.birthdayDateEdit)
        self.streetLabel.setBuddy(self.addressLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.titleComboBox, self.genderComboBox)
        QWidget.setTabOrder(self.genderComboBox, self.employeeNumberDoubleSpinBox)
        QWidget.setTabOrder(self.employeeNumberDoubleSpinBox, self.firstNameLineEdit)
        QWidget.setTabOrder(self.firstNameLineEdit, self.lastNameLineEdit)
        QWidget.setTabOrder(self.lastNameLineEdit, self.zipCityIdComboBox)
        QWidget.setTabOrder(self.zipCityIdComboBox, self.cityLineEdit)
        QWidget.setTabOrder(self.cityLineEdit, self.addressLineEdit)
        QWidget.setTabOrder(self.addressLineEdit, self.birthdayDateEdit)
        QWidget.setTabOrder(self.birthdayDateEdit, self.homeMailLineEdit)
        QWidget.setTabOrder(self.homeMailLineEdit, self.homeMobileLineEdit)
        QWidget.setTabOrder(self.homeMobileLineEdit, self.homePhoneLineEdit)
        QWidget.setTabOrder(self.homePhoneLineEdit, self.activeCheckBox)
        QWidget.setTabOrder(self.activeCheckBox, self.dataCareCheckBox)
        QWidget.setTabOrder(self.dataCareCheckBox, self.businessMailLineEdit)
        QWidget.setTabOrder(self.businessMailLineEdit, self.hireDateDateEdit)
        QWidget.setTabOrder(self.hireDateDateEdit, self.endDateDateEdit)
        QWidget.setTabOrder(self.endDateDateEdit, self.phoneComboBox)
        QWidget.setTabOrder(self.phoneComboBox, self.mobileComboBox)
        QWidget.setTabOrder(self.mobileComboBox, self.faxComboBox)
        QWidget.setTabOrder(self.faxComboBox, self.computerComboBox)
        QWidget.setTabOrder(self.computerComboBox, self.printerComboBox)
        QWidget.setTabOrder(self.printerComboBox, self.chipCardComboBox)
        QWidget.setTabOrder(self.chipCardComboBox, self.departmentComboBox)
        QWidget.setTabOrder(self.departmentComboBox, self.functionComboBox)
        QWidget.setTabOrder(self.functionComboBox, self.employeeAccountComboBox)
        QWidget.setTabOrder(self.employeeAccountComboBox, self.employeeDocumentComboBox)
        QWidget.setTabOrder(self.employeeDocumentComboBox, self.notesTextEdit)
        QWidget.setTabOrder(self.notesTextEdit, self.photoGraphicsView)
        QWidget.setTabOrder(self.photoGraphicsView, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(EmployeeInputArea)

        QMetaObject.connectSlotsByName(EmployeeInputArea)

    # setupUi

    def retranslateUi(self, EmployeeInputArea):
        EmployeeInputArea.setWindowTitle(
            QCoreApplication.translate("EmployeeInputArea", "Mitarbeiter*innen", None)
        )
        # if QT_CONFIG(accessibility)
        EmployeeInputArea.setAccessibleName(
            QCoreApplication.translate("EmployeeInputArea", "EmployeeInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        EmployeeInputArea.setTitle(
            QCoreApplication.translate("EmployeeInputArea", "Mitarbeiter*in", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("EmployeeInputArea", "Mitarbeiter*in", None)
        )
        self.phoneLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Telefon", None)
        )
        self.employeeDocumentLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Dokumente", None)
        )
        self.departmentLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Abteilung", None)
        )
        self.endDateLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Enddatum", None)
        )
        self.faxLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Fax", None)
        )
        self.homePhonelabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "private Telefonnr.", None)
        )
        self.lastNameLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Nachname", None)
        )
        self.businessMailLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Mail", None)
        )
        self.notesLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Notizen", None)
        )
        self.hireDateLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Einstellungsdatun", None)
        )
        self.firstNameLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Vorname", None)
        )
        self.zipCityIdLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "PLZ", None)
        )
        self.computerLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Computer", None)
        )
        self.homeMobilelabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "private Mobilnummer", None)
        )
        self.activeCheckBox.setText(
            QCoreApplication.translate("EmployeeInputArea", "Aktiv", None)
        )
        self.chipCardLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "ChipCard", None)
        )
        self.mobileLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Mobilnummer", None)
        )
        self.functionLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Funktion", None)
        )
        self.cityLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Stadt", None)
        )
        self.dataCareCheckBox.setText(
            QCoreApplication.translate("EmployeeInputArea", "Datenschutz", None)
        )
        self.photoLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Foto", None)
        )
        self.titleLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Titel", None)
        )
        self.printerLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Drucker", None)
        )
        self.homeMailLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "private Mail", None)
        )
        self.genderLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Gender", None)
        )
        self.employeeNumberLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Pers.Number", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "EmployeeInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.employeeAccountLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Zug\u00e4nge", None)
        )
        self.birthdayLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Geburtstag", None)
        )
        self.streetLabel.setText(
            QCoreApplication.translate("EmployeeInputArea", "Stra\u00dfe", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("EmployeeInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("EmployeeInputArea", "Bearbeiten", None)
        )

    # retranslateUi
