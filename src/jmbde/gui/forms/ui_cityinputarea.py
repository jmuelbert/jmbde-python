# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cityinputarea.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_CityInputArea(object):
    def setupUi(self, CityInputArea):
        if not CityInputArea.objectName():
            CityInputArea.setObjectName(u"CityInputArea")
        CityInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(CityInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.GroupBox = QWidget(CityInputArea)
        self.GroupBox.setObjectName(u"GroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.GroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cityNameLabel = QLabel(self.GroupBox)
        self.cityNameLabel.setObjectName(u"cityNameLabel")

        self.gridLayout.addWidget(self.cityNameLabel, 1, 0, 1, 1)

        self.cityNameLineEdit = QLineEdit(self.GroupBox)
        self.cityNameLineEdit.setObjectName(u"cityNameLineEdit")

        self.gridLayout.addWidget(self.cityNameLineEdit, 1, 1, 1, 1)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 2, 0, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.GroupBox)

#if QT_CONFIG(shortcut)
        self.cityNameLabel.setBuddy(self.cityNameLineEdit)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.cityNameLineEdit, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(CityInputArea)

        QMetaObject.connectSlotsByName(CityInputArea)
    # setupUi

    def retranslateUi(self, CityInputArea):
        CityInputArea.setWindowTitle(QCoreApplication.translate("CityInputArea", u"Ort", None))
#if QT_CONFIG(accessibility)
        CityInputArea.setAccessibleName(QCoreApplication.translate("CityInputArea", u"CityInputDialog", None))
#endif // QT_CONFIG(accessibility)
        CityInputArea.setTitle(QCoreApplication.translate("CityInputArea", u"Ort", None))
        self.label_Header.setText(QCoreApplication.translate("CityInputArea", u"Ort", None))
        self.cityNameLabel.setText(QCoreApplication.translate("CityInputArea", u"Ort/Name", None))
        self.lastUpdateLabel.setText(QCoreApplication.translate("CityInputArea", u"Letzte \u00c4nderung", None))
        self.addPushButton.setText(QCoreApplication.translate("CityInputArea", u"+", None))
        self.editFinishPushButton.setText(QCoreApplication.translate("CityInputArea", u"Bearbeiten", None))
    # retranslateUi

