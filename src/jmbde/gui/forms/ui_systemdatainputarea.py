# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'systemdatainputarea.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SystemDataInputArea(object):
    def setupUi(self, SystemDataInputArea):
        if not SystemDataInputArea.objectName():
            SystemDataInputArea.setObjectName(u"SystemDataInputArea")
        SystemDataInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(SystemDataInputArea)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.GroupBox = QWidget(SystemDataInputArea)
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
        self.nameLabel = QLabel(self.GroupBox)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.GroupBox)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.localCheckBox = QCheckBox(self.GroupBox)
        self.localCheckBox.setObjectName(u"localCheckBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.localCheckBox)

        self.companyLabel = QLabel(self.GroupBox)
        self.companyLabel.setObjectName(u"companyLabel")
        self.companyLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.companyLabel)

        self.compamyComboBox = QComboBox(self.GroupBox)
        self.compamyComboBox.setObjectName(u"compamyComboBox")
        self.compamyComboBox.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.compamyComboBox)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lastUpdateLineEdit)


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
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.companyLabel.setBuddy(self.compamyComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameLineEdit, self.localCheckBox)
        QWidget.setTabOrder(self.localCheckBox, self.compamyComboBox)
        QWidget.setTabOrder(self.compamyComboBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(SystemDataInputArea)

        QMetaObject.connectSlotsByName(SystemDataInputArea)
    # setupUi

    def retranslateUi(self, SystemDataInputArea):
        SystemDataInputArea.setWindowTitle(QCoreApplication.translate("SystemDataInputArea", u"System Daten", None))
#if QT_CONFIG(accessibility)
        SystemDataInputArea.setAccessibleName(QCoreApplication.translate("SystemDataInputArea", u"SystemDataInputDialog", None))
#endif // QT_CONFIG(accessibility)
        SystemDataInputArea.setTitle(QCoreApplication.translate("SystemDataInputArea", u"System Daten", None))
        self.label_Header.setText(QCoreApplication.translate("SystemDataInputArea", u"System Daten", None))
        self.nameLabel.setText(QCoreApplication.translate("SystemDataInputArea", u"Name", None))
        self.localCheckBox.setText(QCoreApplication.translate("SystemDataInputArea", u"Lokal", None))
        self.companyLabel.setText(QCoreApplication.translate("SystemDataInputArea", u"Firma", None))
        self.lastUpdateLabel.setText(QCoreApplication.translate("SystemDataInputArea", u"Letzte \u00c4nderung", None))
        self.addPushButton.setText(QCoreApplication.translate("SystemDataInputArea", u"+", None))
        self.editFinishPushButton.setText(QCoreApplication.translate("SystemDataInputArea", u"Bearbeiten", None))
    # retranslateUi

