# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employeedocumentinputarea.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_EmployeeDocumentInputArea(object):
    def setupUi(self, EmployeeDocumentInputArea):
        if not EmployeeDocumentInputArea.objectName():
            EmployeeDocumentInputArea.setObjectName(u"EmployeeDocumentInputArea")
        EmployeeDocumentInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(EmployeeDocumentInputArea)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.GroupBox = QWidget(EmployeeDocumentInputArea)
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
        self.employeeIdLabel = QLabel(self.GroupBox)
        self.employeeIdLabel.setObjectName(u"employeeIdLabel")
        self.employeeIdLabel.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.employeeIdLabel)

        self.documentIdLabel = QLabel(self.GroupBox)
        self.documentIdLabel.setObjectName(u"documentIdLabel")
        self.documentIdLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.documentIdLabel)

        self.documentIdcomboBox = QComboBox(self.GroupBox)
        self.documentIdcomboBox.setObjectName(u"documentIdcomboBox")
        self.documentIdcomboBox.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.documentIdcomboBox)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.employeeIdcomboBox = QComboBox(self.GroupBox)
        self.employeeIdcomboBox.setObjectName(u"employeeIdcomboBox")
        self.employeeIdcomboBox.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.employeeIdcomboBox)

        self.lastUpdatelineEdit = QLineEdit(self.GroupBox)
        self.lastUpdatelineEdit.setObjectName(u"lastUpdatelineEdit")
        self.lastUpdatelineEdit.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lastUpdatelineEdit)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addPushButton = QPushButton(self.GroupBox)
        self.addPushButton.setObjectName(u"addPushButton")
        self.addPushButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.GroupBox)
        self.editFinishPushButton.setObjectName(u"editFinishPushButton")
        self.editFinishPushButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.editFinishPushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout_3.addWidget(self.GroupBox, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.employeeIdLabel.setBuddy(self.employeeIdcomboBox)
        self.documentIdLabel.setBuddy(self.documentIdcomboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdatelineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.employeeIdcomboBox, self.documentIdcomboBox)
        QWidget.setTabOrder(self.documentIdcomboBox, self.lastUpdatelineEdit)
        QWidget.setTabOrder(self.lastUpdatelineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(EmployeeDocumentInputArea)

        QMetaObject.connectSlotsByName(EmployeeDocumentInputArea)
    # setupUi

    def retranslateUi(self, EmployeeDocumentInputArea):
        EmployeeDocumentInputArea.setWindowTitle(QCoreApplication.translate("EmployeeDocumentInputArea", u"Mitarbeiter*in Dokument", None))
#if QT_CONFIG(accessibility)
        EmployeeDocumentInputArea.setAccessibleName(QCoreApplication.translate("EmployeeDocumentInputArea", u"EmployeeDocumentInputDialog", None))
#endif // QT_CONFIG(accessibility)
        EmployeeDocumentInputArea.setTitle(QCoreApplication.translate("EmployeeDocumentInputArea", u"Mitarbeiter*in Dokument", None))
        self.label_Header.setText(QCoreApplication.translate("EmployeeDocumentInputArea", u"Mitarbeiter*in Dokument", None))
        self.employeeIdLabel.setText(QCoreApplication.translate("EmployeeDocumentInputArea", u"Mitarbeiter*in", None))
        self.documentIdLabel.setText(QCoreApplication.translate("EmployeeDocumentInputArea", u"Dokument", None))
        self.lastUpdateLabel.setText(QCoreApplication.translate("EmployeeDocumentInputArea", u"Letzte \u00c4nderung", None))
        self.addPushButton.setText(QCoreApplication.translate("EmployeeDocumentInputArea", u"+", None))
        self.editFinishPushButton.setText(QCoreApplication.translate("EmployeeDocumentInputArea", u"Bearbeiten", None))
    # retranslateUi

