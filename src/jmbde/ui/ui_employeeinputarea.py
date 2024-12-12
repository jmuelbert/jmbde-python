# -*- coding: utf-8 -*-
################################################################################
# Form generated from reading UI file 'employeeinputarea.ui'
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


class Ui_EmployeeInputArea(object):
    def setupUi(self, EmployeeInputArea):
        if not EmployeeInputArea.objectName():
            EmployeeInputArea.setObjectName("EmployeeInputArea")
        EmployeeInputArea.resize(730, 609)
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
        self.comboBox_Printer = QComboBox(self.formLayoutWidget)
        self.comboBox_Printer.setObjectName("comboBox_Printer")

        self.gridLayout.addWidget(self.comboBox_Printer, 8, 3, 1, 1)

        self.label_EndDate = QLabel(self.formLayoutWidget)
        self.label_EndDate.setObjectName("label_EndDate")

        self.gridLayout.addWidget(self.label_EndDate, 6, 2, 1, 1)

        self.label_HomeMobile = QLabel(self.formLayoutWidget)
        self.label_HomeMobile.setObjectName("label_HomeMobile")

        self.gridLayout.addWidget(self.label_HomeMobile, 4, 2, 1, 1)

        self.label_FirstName = QLabel(self.formLayoutWidget)
        self.label_FirstName.setObjectName("label_FirstName")

        self.gridLayout.addWidget(self.label_FirstName, 1, 0, 1, 1)

        self.label_BusinessMail = QLabel(self.formLayoutWidget)
        self.label_BusinessMail.setObjectName("label_BusinessMail")

        self.gridLayout.addWidget(self.label_BusinessMail, 5, 0, 1, 1)

        self.label_LastName = QLabel(self.formLayoutWidget)
        self.label_LastName.setObjectName("label_LastName")

        self.gridLayout.addWidget(self.label_LastName, 1, 2, 1, 1)

        self.dateEdit_StartDate = QDateEdit(self.formLayoutWidget)
        self.dateEdit_StartDate.setObjectName("dateEdit_StartDate")

        self.gridLayout.addWidget(self.dateEdit_StartDate, 6, 1, 1, 1)

        self.comboBox_EmployeeDocument = QComboBox(self.formLayoutWidget)
        self.comboBox_EmployeeDocument.setObjectName("comboBox_EmployeeDocument")

        self.gridLayout.addWidget(self.comboBox_EmployeeDocument, 10, 3, 1, 1)

        self.label_Address = QLabel(self.formLayoutWidget)
        self.label_Address.setObjectName("label_Address")

        self.gridLayout.addWidget(self.label_Address, 2, 4, 1, 1)

        self.comboBox_Function = QComboBox(self.formLayoutWidget)
        self.comboBox_Function.setObjectName("comboBox_Function")

        self.gridLayout.addWidget(self.comboBox_Function, 9, 3, 1, 1)

        self.label_Computer = QLabel(self.formLayoutWidget)
        self.label_Computer.setObjectName("label_Computer")

        self.gridLayout.addWidget(self.label_Computer, 8, 0, 1, 1)

        self.label_ZipCode = QLabel(self.formLayoutWidget)
        self.label_ZipCode.setObjectName("label_ZipCode")

        self.gridLayout.addWidget(self.label_ZipCode, 2, 0, 1, 1)

        self.lineEdit_HomeMail = QLineEdit(self.formLayoutWidget)
        self.lineEdit_HomeMail.setObjectName("lineEdit_HomeMail")

        self.gridLayout.addWidget(self.lineEdit_HomeMail, 4, 1, 1, 1)

        self.label_EmployeeAccount = QLabel(self.formLayoutWidget)
        self.label_EmployeeAccount.setObjectName("label_EmployeeAccount")

        self.gridLayout.addWidget(self.label_EmployeeAccount, 10, 0, 1, 1)

        self.label_Notes = QLabel(self.formLayoutWidget)
        self.label_Notes.setObjectName("label_Notes")

        self.gridLayout.addWidget(self.label_Notes, 11, 0, 1, 1)

        self.comboBox_Mobile = QComboBox(self.formLayoutWidget)
        self.comboBox_Mobile.setObjectName("comboBox_Mobile")

        self.gridLayout.addWidget(self.comboBox_Mobile, 7, 3, 1, 1)

        self.checkBox_DataCare = QCheckBox(self.formLayoutWidget)
        self.checkBox_DataCare.setObjectName("checkBox_DataCare")

        self.gridLayout.addWidget(self.checkBox_DataCare, 5, 5, 1, 1)

        self.comboBox_Department = QComboBox(self.formLayoutWidget)
        self.comboBox_Department.setObjectName("comboBox_Department")

        self.gridLayout.addWidget(self.comboBox_Department, 9, 1, 1, 1)

        self.comboBox_Gender = QComboBox(self.formLayoutWidget)
        self.comboBox_Gender.setObjectName("comboBox_Gender")

        self.gridLayout.addWidget(self.comboBox_Gender, 0, 3, 1, 1)

        self.comboBox_ChipCard = QComboBox(self.formLayoutWidget)
        self.comboBox_ChipCard.setObjectName("comboBox_ChipCard")

        self.gridLayout.addWidget(self.comboBox_ChipCard, 8, 5, 1, 1)

        self.label_PersNumber = QLabel(self.formLayoutWidget)
        self.label_PersNumber.setObjectName("label_PersNumber")

        self.gridLayout.addWidget(self.label_PersNumber, 1, 4, 1, 1)

        self.lineEdit_City = QLineEdit(self.formLayoutWidget)
        self.lineEdit_City.setObjectName("lineEdit_City")

        self.gridLayout.addWidget(self.lineEdit_City, 2, 3, 1, 1)

        self.comboBox_Fax = QComboBox(self.formLayoutWidget)
        self.comboBox_Fax.setObjectName("comboBox_Fax")

        self.gridLayout.addWidget(self.comboBox_Fax, 7, 5, 1, 1)

        self.label_HomePhone = QLabel(self.formLayoutWidget)
        self.label_HomePhone.setObjectName("label_HomePhone")

        self.gridLayout.addWidget(self.label_HomePhone, 4, 4, 1, 1)

        self.label_Birthday = QLabel(self.formLayoutWidget)
        self.label_Birthday.setObjectName("label_Birthday")

        self.gridLayout.addWidget(self.label_Birthday, 3, 0, 1, 1)

        self.label_Function = QLabel(self.formLayoutWidget)
        self.label_Function.setObjectName("label_Function")

        self.gridLayout.addWidget(self.label_Function, 9, 2, 1, 1)

        self.lineEdit_Firstname = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Firstname.setObjectName("lineEdit_Firstname")

        self.gridLayout.addWidget(self.lineEdit_Firstname, 1, 1, 1, 1)

        self.label_Phone = QLabel(self.formLayoutWidget)
        self.label_Phone.setObjectName("label_Phone")

        self.gridLayout.addWidget(self.label_Phone, 7, 0, 1, 1)

        self.lineEdit_HomeMobile = QLineEdit(self.formLayoutWidget)
        self.lineEdit_HomeMobile.setObjectName("lineEdit_HomeMobile")

        self.gridLayout.addWidget(self.lineEdit_HomeMobile, 4, 3, 1, 1)

        self.label_Title = QLabel(self.formLayoutWidget)
        self.label_Title.setObjectName("label_Title")

        self.gridLayout.addWidget(self.label_Title, 0, 0, 1, 1)

        self.label_Lastupdate_Date = QLabel(self.formLayoutWidget)
        self.label_Lastupdate_Date.setObjectName("label_Lastupdate_Date")

        self.gridLayout.addWidget(self.label_Lastupdate_Date, 10, 5, 1, 1)

        self.doubleSpinBox_PersNR = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_PersNR.setObjectName("doubleSpinBox_PersNR")
        self.doubleSpinBox_PersNR.setDecimals(0)
        self.doubleSpinBox_PersNR.setMaximum(1000.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_PersNR, 1, 5, 1, 1)

        self.label_Gender = QLabel(self.formLayoutWidget)
        self.label_Gender.setObjectName("label_Gender")

        self.gridLayout.addWidget(self.label_Gender, 0, 2, 1, 1)

        self.lineEdit_Address = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Address.setObjectName("lineEdit_Address")

        self.gridLayout.addWidget(self.lineEdit_Address, 2, 5, 1, 1)

        self.comboBox_EmployeeAccount = QComboBox(self.formLayoutWidget)
        self.comboBox_EmployeeAccount.setObjectName("comboBox_EmployeeAccount")

        self.gridLayout.addWidget(self.comboBox_EmployeeAccount, 10, 1, 1, 1)

        self.label_Fax = QLabel(self.formLayoutWidget)
        self.label_Fax.setObjectName("label_Fax")

        self.gridLayout.addWidget(self.label_Fax, 7, 4, 1, 1)

        self.label_ChipCard = QLabel(self.formLayoutWidget)
        self.label_ChipCard.setObjectName("label_ChipCard")

        self.gridLayout.addWidget(self.label_ChipCard, 8, 4, 1, 1)

        self.label_Printer = QLabel(self.formLayoutWidget)
        self.label_Printer.setObjectName("label_Printer")

        self.gridLayout.addWidget(self.label_Printer, 8, 2, 1, 1)

        self.checkBox_Active = QCheckBox(self.formLayoutWidget)
        self.checkBox_Active.setObjectName("checkBox_Active")

        self.gridLayout.addWidget(self.checkBox_Active, 5, 4, 1, 1)

        self.lineEditZipCode = QLineEdit(self.formLayoutWidget)
        self.lineEditZipCode.setObjectName("lineEditZipCode")

        self.gridLayout.addWidget(self.lineEditZipCode, 2, 1, 1, 1)

        self.lineEdit_HomePhone = QLineEdit(self.formLayoutWidget)
        self.lineEdit_HomePhone.setObjectName("lineEdit_HomePhone")

        self.gridLayout.addWidget(self.lineEdit_HomePhone, 4, 5, 1, 1)

        self.label_Mobile = QLabel(self.formLayoutWidget)
        self.label_Mobile.setObjectName("label_Mobile")

        self.gridLayout.addWidget(self.label_Mobile, 7, 2, 1, 1)

        self.comboBox_Title = QComboBox(self.formLayoutWidget)
        self.comboBox_Title.setObjectName("comboBox_Title")

        self.gridLayout.addWidget(self.comboBox_Title, 0, 1, 1, 1)

        self.comboBox_Phone = QComboBox(self.formLayoutWidget)
        self.comboBox_Phone.setObjectName("comboBox_Phone")

        self.gridLayout.addWidget(self.comboBox_Phone, 7, 1, 1, 1)

        self.lineEdit_BusinessMail = QLineEdit(self.formLayoutWidget)
        self.lineEdit_BusinessMail.setObjectName("lineEdit_BusinessMail")

        self.gridLayout.addWidget(self.lineEdit_BusinessMail, 5, 1, 1, 1)

        self.label_EmployeeDocument = QLabel(self.formLayoutWidget)
        self.label_EmployeeDocument.setObjectName("label_EmployeeDocument")

        self.gridLayout.addWidget(self.label_EmployeeDocument, 10, 2, 1, 1)

        self.dateEdit_Birthday = QDateEdit(self.formLayoutWidget)
        self.dateEdit_Birthday.setObjectName("dateEdit_Birthday")

        self.gridLayout.addWidget(self.dateEdit_Birthday, 3, 1, 1, 1)

        self.textEdit_Notes = QTextEdit(self.formLayoutWidget)
        self.textEdit_Notes.setObjectName("textEdit_Notes")

        self.gridLayout.addWidget(self.textEdit_Notes, 11, 1, 1, 2)

        self.label_StartDate = QLabel(self.formLayoutWidget)
        self.label_StartDate.setObjectName("label_StartDate")

        self.gridLayout.addWidget(self.label_StartDate, 6, 0, 1, 1)

        self.label_Department = QLabel(self.formLayoutWidget)
        self.label_Department.setObjectName("label_Department")

        self.gridLayout.addWidget(self.label_Department, 9, 0, 1, 1)

        self.lineEdit_Lastname = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Lastname.setObjectName("lineEdit_Lastname")

        self.gridLayout.addWidget(self.lineEdit_Lastname, 1, 3, 1, 1)

        self.label_Lastupdate = QLabel(self.formLayoutWidget)
        self.label_Lastupdate.setObjectName("label_Lastupdate")

        self.gridLayout.addWidget(self.label_Lastupdate, 10, 4, 1, 1)

        self.label_HomeMail = QLabel(self.formLayoutWidget)
        self.label_HomeMail.setObjectName("label_HomeMail")

        self.gridLayout.addWidget(self.label_HomeMail, 4, 0, 1, 1)

        self.comboBox_Computer = QComboBox(self.formLayoutWidget)
        self.comboBox_Computer.setObjectName("comboBox_Computer")

        self.gridLayout.addWidget(self.comboBox_Computer, 8, 1, 1, 1)

        self.label_City = QLabel(self.formLayoutWidget)
        self.label_City.setObjectName("label_City")

        self.gridLayout.addWidget(self.label_City, 2, 2, 1, 1)

        self.dateEdit_EndDate = QDateEdit(self.formLayoutWidget)
        self.dateEdit_EndDate.setObjectName("dateEdit_EndDate")

        self.gridLayout.addWidget(self.dateEdit_EndDate, 6, 3, 1, 1)

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
        self.label_EndDate.setBuddy(self.dateEdit_EndDate)
        self.label_HomeMobile.setBuddy(self.lineEdit_HomeMobile)
        self.label_FirstName.setBuddy(self.lineEdit_Firstname)
        self.label_BusinessMail.setBuddy(self.lineEdit_BusinessMail)
        self.label_LastName.setBuddy(self.lineEdit_Lastname)
        self.label_Address.setBuddy(self.lineEdit_Address)
        self.label_Computer.setBuddy(self.comboBox_Computer)
        self.label_ZipCode.setBuddy(self.lineEditZipCode)
        self.label_EmployeeAccount.setBuddy(self.comboBox_EmployeeAccount)
        self.label_Notes.setBuddy(self.textEdit_Notes)
        self.label_PersNumber.setBuddy(self.doubleSpinBox_PersNR)
        self.label_HomePhone.setBuddy(self.lineEdit_HomePhone)
        self.label_Birthday.setBuddy(self.dateEdit_Birthday)
        self.label_Function.setBuddy(self.comboBox_Function)
        self.label_Phone.setBuddy(self.comboBox_Phone)
        self.label_Title.setBuddy(self.comboBox_Title)
        self.label_Gender.setBuddy(self.comboBox_Gender)
        self.label_Fax.setBuddy(self.comboBox_Fax)
        self.label_ChipCard.setBuddy(self.comboBox_ChipCard)
        self.label_Printer.setBuddy(self.comboBox_Printer)
        self.label_Mobile.setBuddy(self.comboBox_Mobile)
        self.label_EmployeeDocument.setBuddy(self.comboBox_EmployeeDocument)
        self.label_StartDate.setBuddy(self.dateEdit_StartDate)
        self.label_Department.setBuddy(self.comboBox_Department)
        self.label_HomeMail.setBuddy(self.lineEdit_HomeMail)
        self.label_City.setBuddy(self.lineEdit_City)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.comboBox_Title, self.comboBox_Gender)
        QWidget.setTabOrder(self.comboBox_Gender, self.lineEdit_Firstname)
        QWidget.setTabOrder(self.lineEdit_Firstname, self.lineEdit_Lastname)
        QWidget.setTabOrder(self.lineEdit_Lastname, self.doubleSpinBox_PersNR)
        QWidget.setTabOrder(self.doubleSpinBox_PersNR, self.lineEditZipCode)
        QWidget.setTabOrder(self.lineEditZipCode, self.lineEdit_City)
        QWidget.setTabOrder(self.lineEdit_City, self.lineEdit_Address)
        QWidget.setTabOrder(self.lineEdit_Address, self.dateEdit_Birthday)
        QWidget.setTabOrder(self.dateEdit_Birthday, self.lineEdit_HomeMail)
        QWidget.setTabOrder(self.lineEdit_HomeMail, self.lineEdit_HomeMobile)
        QWidget.setTabOrder(self.lineEdit_HomeMobile, self.lineEdit_HomePhone)
        QWidget.setTabOrder(self.lineEdit_HomePhone, self.lineEdit_BusinessMail)
        QWidget.setTabOrder(self.lineEdit_BusinessMail, self.checkBox_Active)
        QWidget.setTabOrder(self.checkBox_Active, self.checkBox_DataCare)
        QWidget.setTabOrder(self.checkBox_DataCare, self.dateEdit_StartDate)
        QWidget.setTabOrder(self.dateEdit_StartDate, self.dateEdit_EndDate)
        QWidget.setTabOrder(self.dateEdit_EndDate, self.comboBox_Phone)
        QWidget.setTabOrder(self.comboBox_Phone, self.comboBox_Mobile)
        QWidget.setTabOrder(self.comboBox_Mobile, self.comboBox_Fax)
        QWidget.setTabOrder(self.comboBox_Fax, self.comboBox_Computer)
        QWidget.setTabOrder(self.comboBox_Computer, self.comboBox_Printer)
        QWidget.setTabOrder(self.comboBox_Printer, self.comboBox_ChipCard)
        QWidget.setTabOrder(self.comboBox_ChipCard, self.comboBox_Department)
        QWidget.setTabOrder(self.comboBox_Department, self.comboBox_Function)
        QWidget.setTabOrder(self.comboBox_Function, self.comboBox_EmployeeAccount)
        QWidget.setTabOrder(
            self.comboBox_EmployeeAccount, self.comboBox_EmployeeDocument
        )
        QWidget.setTabOrder(self.comboBox_EmployeeDocument, self.textEdit_Notes)

        self.retranslateUi(EmployeeInputArea)

        QMetaObject.connectSlotsByName(EmployeeInputArea)

    # setupUi

    def retranslateUi(self, EmployeeInputArea):
        EmployeeInputArea.setWindowTitle(
            QCoreApplication.translate("EmployeeInputArea", "Employee", None)
        )
        # if QT_CONFIG(accessibility)
        EmployeeInputArea.setAccessibleName(
            QCoreApplication.translate("EmployeeInputArea", "EmployeeInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        EmployeeInputArea.setTitle(
            QCoreApplication.translate("EmployeeInputArea", "Employee", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("EmployeeInputArea", "Employee", None)
        )
        self.label_EndDate.setText(
            QCoreApplication.translate("EmployeeInputArea", "End Date", None)
        )
        self.label_HomeMobile.setText(
            QCoreApplication.translate("EmployeeInputArea", "Home Mobile", None)
        )
        self.label_FirstName.setText(
            QCoreApplication.translate("EmployeeInputArea", "Firstname", None)
        )
        self.label_BusinessMail.setText(
            QCoreApplication.translate("EmployeeInputArea", "Businessmail", None)
        )
        self.label_LastName.setText(
            QCoreApplication.translate("EmployeeInputArea", "Lastname", None)
        )
        self.label_Address.setText(
            QCoreApplication.translate("EmployeeInputArea", "Address", None)
        )
        self.label_Computer.setText(
            QCoreApplication.translate("EmployeeInputArea", "Computer", None)
        )
        self.label_ZipCode.setText(
            QCoreApplication.translate("EmployeeInputArea", "Zipcode", None)
        )
        self.label_EmployeeAccount.setText(
            QCoreApplication.translate("EmployeeInputArea", "Employee Account", None)
        )
        self.label_Notes.setText(
            QCoreApplication.translate("EmployeeInputArea", "Notes", None)
        )
        self.checkBox_DataCare.setText(
            QCoreApplication.translate("EmployeeInputArea", "Datacare", None)
        )
        self.label_PersNumber.setText(
            QCoreApplication.translate("EmployeeInputArea", "Pers.Number", None)
        )
        self.label_HomePhone.setText(
            QCoreApplication.translate("EmployeeInputArea", "Home Phone", None)
        )
        self.label_Birthday.setText(
            QCoreApplication.translate("EmployeeInputArea", "Birthday", None)
        )
        self.label_Function.setText(
            QCoreApplication.translate("EmployeeInputArea", "Function", None)
        )
        self.label_Phone.setText(
            QCoreApplication.translate("EmployeeInputArea", "Phone", None)
        )
        self.label_Title.setText(
            QCoreApplication.translate("EmployeeInputArea", "Title", None)
        )
        self.label_Lastupdate_Date.setText(
            QCoreApplication.translate("EmployeeInputArea", "Date", None)
        )
        self.label_Gender.setText(
            QCoreApplication.translate("EmployeeInputArea", "Gender", None)
        )
        self.label_Fax.setText(
            QCoreApplication.translate("EmployeeInputArea", "Fax", None)
        )
        self.label_ChipCard.setText(
            QCoreApplication.translate("EmployeeInputArea", "ChipCard", None)
        )
        self.label_Printer.setText(
            QCoreApplication.translate("EmployeeInputArea", "Printer", None)
        )
        self.checkBox_Active.setText(
            QCoreApplication.translate("EmployeeInputArea", "Active", None)
        )
        self.label_Mobile.setText(
            QCoreApplication.translate("EmployeeInputArea", "Mobile", None)
        )
        self.label_EmployeeDocument.setText(
            QCoreApplication.translate("EmployeeInputArea", "Employee Document", None)
        )
        self.label_StartDate.setText(
            QCoreApplication.translate("EmployeeInputArea", "Start Date", None)
        )
        self.label_Department.setText(
            QCoreApplication.translate("EmployeeInputArea", "Department", None)
        )
        self.label_Lastupdate.setText(
            QCoreApplication.translate("EmployeeInputArea", "Last Update", None)
        )
        self.label_HomeMail.setText(
            QCoreApplication.translate("EmployeeInputArea", "Home Mail", None)
        )
        self.label_City.setText(
            QCoreApplication.translate("EmployeeInputArea", "City", None)
        )
        self.pushButton_Add.setText(
            QCoreApplication.translate("EmployeeInputArea", "+", None)
        )
        self.pushButton_EditFinish.setText(
            QCoreApplication.translate("EmployeeInputArea", "Edit", None)
        )

    # retranslateUi
