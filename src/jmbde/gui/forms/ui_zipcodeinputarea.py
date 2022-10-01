# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zipcodeinputarea.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ZipCodeInputArea(object):
    def setupUi(self, ZipCodeInputArea):
        if not ZipCodeInputArea.objectName():
            ZipCodeInputArea.setObjectName(u"ZipCodeInputArea")
        ZipCodeInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(ZipCodeInputArea)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.GroupBox = QWidget(ZipCodeInputArea)
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

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.codeLabel = QLabel(self.GroupBox)
        self.codeLabel.setObjectName(u"codeLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.codeLabel)

        self.codeLineEdit = QLineEdit(self.GroupBox)
        self.codeLineEdit.setObjectName(u"codeLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.codeLineEdit)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lastUpdateLineEdit)


        self.verticalLayout_3.addLayout(self.formLayout)

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
        self.codeLabel.setBuddy(self.codeLineEdit)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.codeLineEdit, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(ZipCodeInputArea)

        QMetaObject.connectSlotsByName(ZipCodeInputArea)
    # setupUi

    def retranslateUi(self, ZipCodeInputArea):
        ZipCodeInputArea.setWindowTitle(QCoreApplication.translate("ZipCodeInputArea", u"PLZ", None))
#if QT_CONFIG(accessibility)
        ZipCodeInputArea.setAccessibleName(QCoreApplication.translate("ZipCodeInputArea", u"ChipCardInputDialog", None))
#endif // QT_CONFIG(accessibility)
        ZipCodeInputArea.setTitle(QCoreApplication.translate("ZipCodeInputArea", u"PLZ", None))
        self.headerLabel.setText(QCoreApplication.translate("ZipCodeInputArea", u"PLZ", None))
        self.codeLabel.setText(QCoreApplication.translate("ZipCodeInputArea", u"PLZ", None))
        self.lastUpdateLabel.setText(QCoreApplication.translate("ZipCodeInputArea", u"Letzte \u00c4nderung", None))
        self.addPushButton.setText(QCoreApplication.translate("ZipCodeInputArea", u"+", None))
        self.editFinishPushButton.setText(QCoreApplication.translate("ZipCodeInputArea", u"Bearbeiten", None))
    # retranslateUi

