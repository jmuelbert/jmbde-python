# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(444, 508)
        self.verticalLayout_3 = QVBoxLayout(AboutDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.logoLayout = QHBoxLayout()
        self.logoLayout.setObjectName(u"logoLayout")
        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.logoLayout.addItem(self.horizontalSpacer)

        self.logo = QLabel(AboutDialog)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(400, 200))
        self.logo.setPixmap(QPixmap(u":/images/about-tiled-logo.png"))
        self.logo.setAlignment(Qt.AlignCenter)

        self.logoLayout.addWidget(self.logo)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.logoLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.logoLayout)

        self.textBrowser = QTextBrowser(AboutDialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.textBrowser)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer_3)

        self.donateButton = QPushButton(AboutDialog)
        self.donateButton.setObjectName(u"donateButton")

        self.buttonLayout.addWidget(self.donateButton)

        self.pushButton = QPushButton(AboutDialog)
        self.pushButton.setObjectName(u"pushButton")

        self.buttonLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.buttonLayout)


        self.retranslateUi(AboutDialog)
        self.pushButton.clicked.connect(AboutDialog.close)

        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About jmbde", None))
        self.logo.setText("")
        self.donateButton.setText(QCoreApplication.translate("AboutDialog", u"Donate", None))
        self.pushButton.setText(QCoreApplication.translate("AboutDialog", u"OK", None))
    # retranslateUi

