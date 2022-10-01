# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'placeinputarea.ui'
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

class Ui_PlaceInputArea(object):
    def setupUi(self, PlaceInputArea):
        if not PlaceInputArea.objectName():
            PlaceInputArea.setObjectName(u"PlaceInputArea")
        PlaceInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(PlaceInputArea)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.GroupBox = QWidget(PlaceInputArea)
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
        self.nameLabel = QLabel(self.GroupBox)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.GroupBox)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.roomLabel = QLabel(self.GroupBox)
        self.roomLabel.setObjectName(u"roomLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.roomLabel)

        self.deskLabel = QLabel(self.GroupBox)
        self.deskLabel.setObjectName(u"deskLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.deskLabel)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lastUpdateLineEdit)

        self.roomLineEdit = QLineEdit(self.GroupBox)
        self.roomLineEdit.setObjectName(u"roomLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.roomLineEdit)

        self.deskLineEdit = QLineEdit(self.GroupBox)
        self.deskLineEdit.setObjectName(u"deskLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.deskLineEdit)


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
        self.roomLabel.setBuddy(self.roomLineEdit)
        self.deskLabel.setBuddy(self.deskLineEdit)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameLineEdit, self.roomLineEdit)
        QWidget.setTabOrder(self.roomLineEdit, self.deskLineEdit)
        QWidget.setTabOrder(self.deskLineEdit, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(PlaceInputArea)

        QMetaObject.connectSlotsByName(PlaceInputArea)
    # setupUi

    def retranslateUi(self, PlaceInputArea):
        PlaceInputArea.setWindowTitle(QCoreApplication.translate("PlaceInputArea", u"Platz", None))
#if QT_CONFIG(accessibility)
        PlaceInputArea.setAccessibleName(QCoreApplication.translate("PlaceInputArea", u"PlaceInputDialog", None))
#endif // QT_CONFIG(accessibility)
        PlaceInputArea.setTitle(QCoreApplication.translate("PlaceInputArea", u"Platz", None))
        self.headerLabel.setText(QCoreApplication.translate("PlaceInputArea", u"Platz", None))
        self.nameLabel.setText(QCoreApplication.translate("PlaceInputArea", u"Name", None))
        self.roomLabel.setText(QCoreApplication.translate("PlaceInputArea", u"Raum", None))
        self.deskLabel.setText(QCoreApplication.translate("PlaceInputArea", u"Tisch", None))
        self.lastUpdateLabel.setText(QCoreApplication.translate("PlaceInputArea", u"Letzte \u00c4nderung", None))
        self.addPushButton.setText(QCoreApplication.translate("PlaceInputArea", u"+", None))
        self.editFinishPushButton.setText(QCoreApplication.translate("PlaceInputArea", u"Bearbeiten", None))
    # retranslateUi

