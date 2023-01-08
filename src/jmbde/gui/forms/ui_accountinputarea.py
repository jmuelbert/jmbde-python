# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accountinputarea.ui'
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
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListView,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_AccountInputArea(object):
    def setupUi(self, AccountInputArea):
        if not AccountInputArea.objectName():
            AccountInputArea.setObjectName("AccountInputArea")
        AccountInputArea.resize(730, 609)
        self.verticalLayout_3 = QVBoxLayout(AccountInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayoutWidget = QWidget(AccountInputArea)
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
        self.systemListView = QListView(self.formLayoutWidget)
        self.systemListView.setObjectName("systemListView")
        self.systemListView.setEnabled(False)

        self.gridLayout.addWidget(self.systemListView, 0, 1, 1, 1)

        self.userNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.userNameLineEdit.setObjectName("userNameLineEdit")

        self.gridLayout.addWidget(self.userNameLineEdit, 1, 1, 1, 1)

        self.systemLabel = QLabel(self.formLayoutWidget)
        self.systemLabel.setObjectName("systemLabel")
        self.systemLabel.setEnabled(False)

        self.gridLayout.addWidget(self.systemLabel, 0, 0, 1, 1)

        self.passwordLineEdit = QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName("passwordLineEdit")

        self.gridLayout.addWidget(self.passwordLineEdit, 2, 1, 1, 1)

        self.userNameLabel = QLabel(self.formLayoutWidget)
        self.userNameLabel.setObjectName("userNameLabel")

        self.gridLayout.addWidget(self.userNameLabel, 1, 0, 1, 1)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")

        self.gridLayout.addWidget(self.passwordLabel, 2, 0, 1, 1)

        self.lastUpdateLabel = QLabel(self.formLayoutWidget)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 3, 0, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 3, 1, 1, 1)

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
        self.systemLabel.setBuddy(self.systemListView)
        self.userNameLabel.setBuddy(self.userNameLineEdit)
        self.passwordLabel.setBuddy(self.passwordLineEdit)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)

        self.retranslateUi(AccountInputArea)

        QMetaObject.connectSlotsByName(AccountInputArea)

    # setupUi

    def retranslateUi(self, AccountInputArea):
        AccountInputArea.setWindowTitle(
            QCoreApplication.translate("AccountInputArea", "Employee", None)
        )
        # if QT_CONFIG(accessibility)
        AccountInputArea.setAccessibleName(
            QCoreApplication.translate("AccountInputArea", "AccountInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        AccountInputArea.setTitle(
            QCoreApplication.translate("AccountInputArea", "Zugang", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("AccountInputArea", "Zug\u00e4nge", None)
        )
        self.systemLabel.setText(
            QCoreApplication.translate("AccountInputArea", "System", None)
        )
        self.userNameLabel.setText(
            QCoreApplication.translate("AccountInputArea", "Anmeldename", None)
        )
        self.passwordLabel.setText(
            QCoreApplication.translate("AccountInputArea", "Passwort", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate("AccountInputArea", "Letzte \u00c4nderung", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("AccountInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("AccountInputArea", "Bearbeiten", None)
        )

    # retranslateUi
