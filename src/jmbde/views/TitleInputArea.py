# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'titleinputarea.ui'
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


class Ui_TitleInputArea(object):
    def setupUi(self, TitleInputArea):
        if not TitleInputArea.objectName():
            TitleInputArea.setObjectName(u"TitleInputArea")
        TitleInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(TitleInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayoutWidget = QWidget(TitleInputArea)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Header = QLabel(self.formLayoutWidget)
        self.label_Header.setObjectName(u"label_Header")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Header.setFont(font)
        self.label_Header.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Header)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_From = QLabel(self.formLayoutWidget)
        self.label_From.setObjectName(u"label_From")

        self.gridLayout.addWidget(self.label_From, 1, 0, 1, 1)

        self.label_To = QLabel(self.formLayoutWidget)
        self.label_To.setObjectName(u"label_To")

        self.gridLayout.addWidget(self.label_To, 2, 0, 1, 1)

        self.lineEdit_Title = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Title.setObjectName(u"lineEdit_Title")

        self.gridLayout.addWidget(self.lineEdit_Title, 0, 2, 1, 1)

        self.dateEdit_From = QDateEdit(self.formLayoutWidget)
        self.dateEdit_From.setObjectName(u"dateEdit_From")

        self.gridLayout.addWidget(self.dateEdit_From, 1, 2, 1, 1)

        self.label_Title = QLabel(self.formLayoutWidget)
        self.label_Title.setObjectName(u"label_Title")

        self.gridLayout.addWidget(self.label_Title, 0, 0, 1, 1)

        self.dateEdit_To = QDateEdit(self.formLayoutWidget)
        self.dateEdit_To.setObjectName(u"dateEdit_To")

        self.gridLayout.addWidget(self.dateEdit_To, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Add = QPushButton(self.formLayoutWidget)
        self.pushButton_Add.setObjectName(u"pushButton_Add")

        self.horizontalLayout.addWidget(self.pushButton_Add)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_EditFinish = QPushButton(self.formLayoutWidget)
        self.pushButton_EditFinish.setObjectName(u"pushButton_EditFinish")

        self.horizontalLayout.addWidget(self.pushButton_EditFinish)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.formLayoutWidget)

#if QT_CONFIG(shortcut)
        self.label_From.setBuddy(self.dateEdit_From)
        self.label_To.setBuddy(self.dateEdit_To)
        self.label_Title.setBuddy(self.lineEdit_Title)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_Title, self.dateEdit_From)
        QWidget.setTabOrder(self.dateEdit_From, self.dateEdit_To)
        QWidget.setTabOrder(self.dateEdit_To, self.pushButton_Add)
        QWidget.setTabOrder(self.pushButton_Add, self.pushButton_EditFinish)

        self.retranslateUi(TitleInputArea)

        QMetaObject.connectSlotsByName(TitleInputArea)
    # setupUi

    def retranslateUi(self, TitleInputArea):
        TitleInputArea.setWindowTitle(QCoreApplication.translate("TitleInputArea", u"Title", None))
#if QT_CONFIG(accessibility)
        TitleInputArea.setAccessibleName(QCoreApplication.translate("TitleInputArea", u"TitleInputDialog", None))
#endif // QT_CONFIG(accessibility)
        TitleInputArea.setTitle(QCoreApplication.translate("TitleInputArea", u"Title", None))
        self.label_Header.setText(QCoreApplication.translate("TitleInputArea", u"Title", None))
        self.label_From.setText(QCoreApplication.translate("TitleInputArea", u"From", None))
        self.label_To.setText(QCoreApplication.translate("TitleInputArea", u"To", None))
        self.label_Title.setText(QCoreApplication.translate("TitleInputArea", u"Title", None))
        self.pushButton_Add.setText(QCoreApplication.translate("TitleInputArea", u"+", None))
        self.pushButton_EditFinish.setText(QCoreApplication.translate("TitleInputArea", u"Edit", None))
    # retranslateUi

