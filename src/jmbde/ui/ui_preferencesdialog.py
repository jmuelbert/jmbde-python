# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'preferencesdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import QCoreApplication
from PySide2.QtCore import QDate
from PySide2.QtCore import QDateTime
from PySide2.QtCore import QMetaObject
from PySide2.QtCore import QObject
from PySide2.QtCore import QPoint
from PySide2.QtCore import QRect
from PySide2.QtCore import QSize
from PySide2.QtCore import Qt
from PySide2.QtCore import QTime
from PySide2.QtCore import QUrl
from PySide2.QtGui import QBrush
from PySide2.QtGui import QColor
from PySide2.QtGui import QConicalGradient
from PySide2.QtGui import QCursor
from PySide2.QtGui import QFont
from PySide2.QtGui import QFontDatabase
from PySide2.QtGui import QIcon
from PySide2.QtGui import QKeySequence
from PySide2.QtGui import QLinearGradient
from PySide2.QtGui import QPainter
from PySide2.QtGui import QPalette
from PySide2.QtGui import QPixmap
from PySide2.QtGui import QRadialGradient
from PySide2.QtWidgets import *


class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        if not PreferencesDialog.objectName():
            PreferencesDialog.setObjectName(u"PreferencesDialog")
        PreferencesDialog.resize(422, 277)
        PreferencesDialog.setMaximumSize(QSize(422, 277))
        self.verticalLayout = QVBoxLayout(PreferencesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBoxDatabaseType = QComboBox(PreferencesDialog)
        self.comboBoxDatabaseType.setObjectName(u"comboBoxDatabaseType")
        self.comboBoxDatabaseType.setEnabled(True)

        self.gridLayout.addWidget(self.comboBoxDatabaseType, 1, 2, 1, 1)

        self.lineEditPassword = QLineEdit(PreferencesDialog)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setEnabled(True)

        self.gridLayout.addWidget(self.lineEditPassword, 5, 2, 1, 1)

        self.pushButtonDBForceFileDialog = QPushButton(PreferencesDialog)
        self.pushButtonDBForceFileDialog.setObjectName(u"pushButtonDBForceFileDialog")
        self.pushButtonDBForceFileDialog.setEnabled(True)

        self.gridLayout.addWidget(self.pushButtonDBForceFileDialog, 2, 3, 1, 1)

        self.labelPassword = QLabel(PreferencesDialog)
        self.labelPassword.setObjectName(u"labelPassword")

        self.gridLayout.addWidget(self.labelPassword, 5, 0, 1, 1)

        self.lineEditDatabaseConnection = QLineEdit(PreferencesDialog)
        self.lineEditDatabaseConnection.setObjectName(u"lineEditDatabaseConnection")
        self.lineEditDatabaseConnection.setEnabled(False)

        self.gridLayout.addWidget(self.lineEditDatabaseConnection, 2, 2, 1, 1)

        self.labelUserName = QLabel(PreferencesDialog)
        self.labelUserName.setObjectName(u"labelUserName")

        self.gridLayout.addWidget(self.labelUserName, 4, 0, 1, 1)

        self.labelDatabaseType = QLabel(PreferencesDialog)
        self.labelDatabaseType.setObjectName(u"labelDatabaseType")

        self.gridLayout.addWidget(self.labelDatabaseType, 1, 0, 1, 1)

        self.lineEditUserName = QLineEdit(PreferencesDialog)
        self.lineEditUserName.setObjectName(u"lineEditUserName")
        self.lineEditUserName.setEnabled(True)

        self.gridLayout.addWidget(self.lineEditUserName, 4, 2, 1, 1)

        self.labelDatabaseConnection = QLabel(PreferencesDialog)
        self.labelDatabaseConnection.setObjectName(u"labelDatabaseConnection")

        self.gridLayout.addWidget(self.labelDatabaseConnection, 2, 0, 1, 1)

        self.lineEditHostName = QLineEdit(PreferencesDialog)
        self.lineEditHostName.setObjectName(u"lineEditHostName")
        self.lineEditHostName.setEnabled(True)

        self.gridLayout.addWidget(self.lineEditHostName, 3, 2, 1, 1)

        self.labelHostName = QLabel(PreferencesDialog)
        self.labelHostName.setObjectName(u"labelHostName")

        self.gridLayout.addWidget(self.labelHostName, 3, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        # if QT_CONFIG(shortcut)
        self.labelPassword.setBuddy(self.lineEditPassword)
        self.labelUserName.setBuddy(self.lineEditUserName)
        self.labelDatabaseType.setBuddy(self.comboBoxDatabaseType)
        self.labelDatabaseConnection.setBuddy(self.lineEditDatabaseConnection)
        self.labelHostName.setBuddy(self.lineEditHostName)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.comboBoxDatabaseType, self.lineEditDatabaseConnection)
        QWidget.setTabOrder(
            self.lineEditDatabaseConnection, self.pushButtonDBForceFileDialog
        )
        QWidget.setTabOrder(self.pushButtonDBForceFileDialog, self.lineEditHostName)
        QWidget.setTabOrder(self.lineEditHostName, self.lineEditUserName)
        QWidget.setTabOrder(self.lineEditUserName, self.lineEditPassword)

        self.retranslateUi(PreferencesDialog)
        self.buttonBox.accepted.connect(PreferencesDialog.accept)
        self.buttonBox.rejected.connect(PreferencesDialog.reject)

        QMetaObject.connectSlotsByName(PreferencesDialog)

    # setupUi

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(
            QCoreApplication.translate("PreferencesDialog", u"Dialog", None)
        )
        self.pushButtonDBForceFileDialog.setText(
            QCoreApplication.translate("PreferencesDialog", u"...", None)
        )
        self.labelPassword.setText(
            QCoreApplication.translate("PreferencesDialog", u"Password", None)
        )
        self.labelUserName.setText(
            QCoreApplication.translate("PreferencesDialog", u"Username", None)
        )
        self.labelDatabaseType.setText(
            QCoreApplication.translate("PreferencesDialog", u"Database Type", None)
        )
        self.labelDatabaseConnection.setText(
            QCoreApplication.translate("PreferencesDialog", u"Database Connc.", None)
        )
        self.labelHostName.setText(
            QCoreApplication.translate("PreferencesDialog", u"Hostname", None)
        )

    # retranslateUi
