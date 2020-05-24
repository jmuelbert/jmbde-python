# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'processorinputarea.ui'
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


class Ui_ProcessorInputArea(object):
    def setupUi(self, ProcessorInputArea):
        if not ProcessorInputArea.objectName():
            ProcessorInputArea.setObjectName(u"ProcessorInputArea")
        ProcessorInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(ProcessorInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayoutWidget = QWidget(ProcessorInputArea)
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.doubleSpinBox_ClockRate = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_ClockRate.setObjectName(u"doubleSpinBox_ClockRate")

        self.gridLayout.addWidget(self.doubleSpinBox_ClockRate, 2, 2, 1, 1)

        self.lineEdit_Name = QLineEdit(self.formLayoutWidget)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.gridLayout.addWidget(self.lineEdit_Name, 1, 2, 1, 1)

        self.label_Name = QLabel(self.formLayoutWidget)
        self.label_Name.setObjectName(u"label_Name")

        self.gridLayout.addWidget(self.label_Name, 1, 0, 1, 1)

        self.label_ClockRate = QLabel(self.formLayoutWidget)
        self.label_ClockRate.setObjectName(u"label_ClockRate")

        self.gridLayout.addWidget(self.label_ClockRate, 2, 0, 1, 1)

        self.label_Frequeny = QLabel(self.formLayoutWidget)
        self.label_Frequeny.setObjectName(u"label_Frequeny")

        self.gridLayout.addWidget(self.label_Frequeny, 2, 3, 1, 1)

        self.label_Cores = QLabel(self.formLayoutWidget)
        self.label_Cores.setObjectName(u"label_Cores")

        self.gridLayout.addWidget(self.label_Cores, 3, 0, 1, 1)

        self.spinBox_Cores = QSpinBox(self.formLayoutWidget)
        self.spinBox_Cores.setObjectName(u"spinBox_Cores")

        self.gridLayout.addWidget(self.spinBox_Cores, 3, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

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
        self.label_Name.setBuddy(self.lineEdit_Name)
        self.label_ClockRate.setBuddy(self.doubleSpinBox_ClockRate)
        self.label_Cores.setBuddy(self.spinBox_Cores)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_Name, self.doubleSpinBox_ClockRate)
        QWidget.setTabOrder(self.doubleSpinBox_ClockRate, self.spinBox_Cores)
        QWidget.setTabOrder(self.spinBox_Cores, self.pushButton_Add)
        QWidget.setTabOrder(self.pushButton_Add, self.pushButton_EditFinish)

        self.retranslateUi(ProcessorInputArea)

        QMetaObject.connectSlotsByName(ProcessorInputArea)
    # setupUi

    def retranslateUi(self, ProcessorInputArea):
        ProcessorInputArea.setWindowTitle(QCoreApplication.translate("ProcessorInputArea", u"Processor", None))
#if QT_CONFIG(accessibility)
        ProcessorInputArea.setAccessibleName(QCoreApplication.translate("ProcessorInputArea", u"ProcessorInputDialog", None))
#endif // QT_CONFIG(accessibility)
        ProcessorInputArea.setTitle(QCoreApplication.translate("ProcessorInputArea", u"Processor", None))
        self.label_Header.setText(QCoreApplication.translate("ProcessorInputArea", u"Processor", None))
        self.label_Name.setText(QCoreApplication.translate("ProcessorInputArea", u"Name", None))
        self.label_ClockRate.setText(QCoreApplication.translate("ProcessorInputArea", u"Clock Rate", None))
        self.label_Frequeny.setText(QCoreApplication.translate("ProcessorInputArea", u"Ghz", None))
        self.label_Cores.setText(QCoreApplication.translate("ProcessorInputArea", u"Cores", None))
        self.pushButton_Add.setText(QCoreApplication.translate("ProcessorInputArea", u"+", None))
        self.pushButton_EditFinish.setText(QCoreApplication.translate("ProcessorInputArea", u"Edit", None))
    # retranslateUi

