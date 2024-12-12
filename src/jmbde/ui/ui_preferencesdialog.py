# -*- coding: utf-8 -*-
################################################################################
# Form generated from reading UI file 'preferencesdialog.ui'
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


class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        if not PreferencesDialog.objectName():
            PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.resize(422, 277)
        PreferencesDialog.setMaximumSize(QSize(422, 277))
        self.verticalLayout = QVBoxLayout(PreferencesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBoxDatabaseType = QComboBox(PreferencesDialog)
        self.comboBoxDatabaseType.setObjectName("comboBoxDatabaseType")
        self.comboBoxDatabaseType.setEnabled(True)

        self.gridLayout.addWidget(self.comboBoxDatabaseType, 1, 2, 1, 1)

        self.lineEditPassword = QLineEdit(PreferencesDialog)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditPassword.setEnabled(True)

        self.gridLayout.addWidget(self.lineEditPassword, 5, 2, 1, 1)

        self.pushButtonDBForceFileDialog = QPushButton(PreferencesDialog)
        self.pushButtonDBForceFileDialog.setObjectName("pushButtonDBForceFileDialog")
        self.pushButtonDBForceFileDialog.setEnabled(True)

        self.gridLayout.addWidget(self.pushButtonDBForceFileDialog, 2, 3, 1, 1)

        self.labelPassword = QLabel(PreferencesDialog)
        self.labelPassword.setObjectName("labelPassword")

        self.gridLayout.addWidget(self.labelPassword, 5, 0, 1, 1)

        self.lineEditDatabaseConnection = QLineEdit(PreferencesDialog)
        self.lineEditDatabaseConnection.setObjectName("lineEditDatabaseConnection")
        self.lineEditDatabaseConnection.setEnabled(False)

        self.gridLayout.addWidget(self.lineEditDatabaseConnection, 2, 2, 1, 1)

        self.labelUserName = QLabel(PreferencesDialog)
        self.labelUserName.setObjectName("labelUserName")

        self.gridLayout.addWidget(self.labelUserName, 4, 0, 1, 1)

        self.labelDatabaseType = QLabel(PreferencesDialog)
        self.labelDatabaseType.setObjectName("labelDatabaseType")

        self.gridLayout.addWidget(self.labelDatabaseType, 1, 0, 1, 1)

        self.lineEditUserName = QLineEdit(PreferencesDialog)
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.lineEditUserName.setEnabled(True)

        self.gridLayout.addWidget(self.lineEditUserName, 4, 2, 1, 1)

        self.labelDatabaseConnection = QLabel(PreferencesDialog)
        self.labelDatabaseConnection.setObjectName("labelDatabaseConnection")

        self.gridLayout.addWidget(self.labelDatabaseConnection, 2, 0, 1, 1)

        self.lineEditHostName = QLineEdit(PreferencesDialog)
        self.lineEditHostName.setObjectName("lineEditHostName")
        self.lineEditHostName.setEnabled(True)

        self.gridLayout.addWidget(self.lineEditHostName, 3, 2, 1, 1)

        self.labelHostName = QLabel(PreferencesDialog)
        self.labelHostName.setObjectName("labelHostName")

        self.gridLayout.addWidget(self.labelHostName, 3, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setObjectName("buttonBox")
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
            QCoreApplication.translate("PreferencesDialog", "Dialog", None)
        )
        self.pushButtonDBForceFileDialog.setText(
            QCoreApplication.translate("PreferencesDialog", "...", None)
        )
        self.labelPassword.setText(
            QCoreApplication.translate("PreferencesDialog", "Password", None)
        )
        self.labelUserName.setText(
            QCoreApplication.translate("PreferencesDialog", "Username", None)
        )
        self.labelDatabaseType.setText(
            QCoreApplication.translate("PreferencesDialog", "Database Type", None)
        )
        self.labelDatabaseConnection.setText(
            QCoreApplication.translate("PreferencesDialog", "Database Connc.", None)
        )
        self.labelHostName.setText(
            QCoreApplication.translate("PreferencesDialog", "Hostname", None)
        )

    # retranslateUi
