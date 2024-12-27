################################################################################
# Form generated from reading UI file 'aboutdialog.ui'
##
# Created by: Qt User Interface Compiler version 5.15.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *


class Ui_AboutDialog:
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(444, 508)
        self.verticalLayout_3 = QVBoxLayout(AboutDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.logoLayout = QHBoxLayout()
        self.logoLayout.setObjectName("logoLayout")
        self.horizontalSpacer = QSpacerItem(
            0,
            20,
            QSizePolicy.Expanding,
            QSizePolicy.Minimum,
        )

        self.logoLayout.addItem(self.horizontalSpacer)

        self.logo = QLabel(AboutDialog)
        self.logo.setObjectName("logo")
        self.logo.setMinimumSize(QSize(400, 200))
        self.logo.setPixmap(QPixmap(":/images/about-tiled-logo.png"))
        self.logo.setAlignment(Qt.AlignCenter)

        self.logoLayout.addWidget(self.logo)

        self.horizontalSpacer_2 = QSpacerItem(
            0,
            20,
            QSizePolicy.Expanding,
            QSizePolicy.Minimum,
        )

        self.logoLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3.addLayout(self.logoLayout)

        self.textBrowser = QTextBrowser(AboutDialog)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.textBrowser)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.buttonLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_3 = QSpacerItem(
            40,
            20,
            QSizePolicy.Expanding,
            QSizePolicy.Minimum,
        )

        self.buttonLayout.addItem(self.horizontalSpacer_3)

        self.donateButton = QPushButton(AboutDialog)
        self.donateButton.setObjectName("donateButton")

        self.buttonLayout.addWidget(self.donateButton)

        self.pushButton = QPushButton(AboutDialog)
        self.pushButton.setObjectName("pushButton")

        self.buttonLayout.addWidget(self.pushButton)

        self.verticalLayout_3.addLayout(self.buttonLayout)

        self.retranslateUi(AboutDialog)
        self.pushButton.clicked.connect(AboutDialog.close)

        self.pushButton.setDefault(True)

        QMetaObject.connectSlotsByName(AboutDialog)

    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(
            QCoreApplication.translate("AboutDialog", "About jmbde", None),
        )
        self.logo.setText("")
        self.donateButton.setText(
            QCoreApplication.translate("AboutDialog", "Donate", None),
        )
        self.pushButton.setText(QCoreApplication.translate("AboutDialog", "OK", None))

    # retranslateUi
