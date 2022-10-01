# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'softwareinputarea.ui'
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

class Ui_SoftwareInputArea(object):
    def setupUi(self, SoftwareInputArea):
        if not SoftwareInputArea.objectName():
            SoftwareInputArea.setObjectName(u"SoftwareInputArea")
        SoftwareInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(SoftwareInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollAreaWidgetContents = QWidget(SoftwareInputArea)
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerLabel = QLabel(self.scrollAreaWidgetContents)
        self.headerLabel.setObjectName(u"headerLabel")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.headerLabel)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.versionLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.versionLineEdit.setObjectName(u"versionLineEdit")

        self.gridLayout.addWidget(self.versionLineEdit, 1, 1, 1, 1)

        self.nameLabel = QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setObjectName(u"nameLabel")

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.revisionLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.revisionLineEdit.setObjectName(u"revisionLineEdit")

        self.gridLayout.addWidget(self.revisionLineEdit, 2, 1, 1, 1)

        self.versionLabel = QLabel(self.scrollAreaWidgetContents)
        self.versionLabel.setObjectName(u"versionLabel")

        self.gridLayout.addWidget(self.versionLabel, 1, 0, 1, 1)

        self.nameLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)

        self.fixLabel = QLabel(self.scrollAreaWidgetContents)
        self.fixLabel.setObjectName(u"fixLabel")

        self.gridLayout.addWidget(self.fixLabel, 3, 0, 1, 1)

        self.fixLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.fixLineEdit.setObjectName(u"fixLineEdit")

        self.gridLayout.addWidget(self.fixLineEdit, 3, 1, 1, 1)

        self.revisionLabel = QLabel(self.scrollAreaWidgetContents)
        self.revisionLabel.setObjectName(u"revisionLabel")

        self.gridLayout.addWidget(self.revisionLabel, 2, 0, 1, 1)

        self.lastUpdateLabel = QLabel(self.scrollAreaWidgetContents)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 4, 0, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 4, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.addPushButton.setObjectName(u"addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.editFinishPushButton.setObjectName(u"editFinishPushButton")

        self.horizontalLayout.addWidget(self.editFinishPushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.scrollAreaWidgetContents)

#if QT_CONFIG(shortcut)
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.versionLabel.setBuddy(self.versionLineEdit)
        self.fixLabel.setBuddy(self.fixLineEdit)
        self.revisionLabel.setBuddy(self.revisionLineEdit)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameLineEdit, self.versionLineEdit)
        QWidget.setTabOrder(self.versionLineEdit, self.revisionLineEdit)
        QWidget.setTabOrder(self.revisionLineEdit, self.fixLineEdit)
        QWidget.setTabOrder(self.fixLineEdit, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(SoftwareInputArea)

        QMetaObject.connectSlotsByName(SoftwareInputArea)
    # setupUi

    def retranslateUi(self, SoftwareInputArea):
        SoftwareInputArea.setWindowTitle(QCoreApplication.translate("SoftwareInputArea", u"Software", None))
#if QT_CONFIG(accessibility)
        SoftwareInputArea.setAccessibleName(QCoreApplication.translate("SoftwareInputArea", u"SoftwareInputDialog", None))
#endif // QT_CONFIG(accessibility)
        SoftwareInputArea.setTitle(QCoreApplication.translate("SoftwareInputArea", u"Software", None))
        self.headerLabel.setText(QCoreApplication.translate("SoftwareInputArea", u"Software", None))
        self.nameLabel.setText(QCoreApplication.translate("SoftwareInputArea", u"Name", None))
        self.versionLabel.setText(QCoreApplication.translate("SoftwareInputArea", u"Version", None))
        self.fixLabel.setText(QCoreApplication.translate("SoftwareInputArea", u"Fix", None))
        self.revisionLabel.setText(QCoreApplication.translate("SoftwareInputArea", u"Revision", None))
        self.lastUpdateLabel.setText(QCoreApplication.translate("SoftwareInputArea", u"Letzte \u00c4nderung", None))
        self.addPushButton.setText(QCoreApplication.translate("SoftwareInputArea", u"+", None))
        self.editFinishPushButton.setText(QCoreApplication.translate("SoftwareInputArea", u"Bearbeiten", None))
    # retranslateUi

