# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'departmentinputarea.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_DepartmentInputArea(object):
    def setupUi(self, DepartmentInputArea):
        if not DepartmentInputArea.objectName():
            DepartmentInputArea.setObjectName(u"DepartmentInputArea")
        DepartmentInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(DepartmentInputArea)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.GroupBox = QWidget(DepartmentInputArea)
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

        self.priorityLabel = QLabel(self.GroupBox)
        self.priorityLabel.setObjectName(u"priorityLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.priorityLabel)

        self.printerLabel = QLabel(self.GroupBox)
        self.printerLabel.setObjectName(u"printerLabel")
        self.printerLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.printerLabel)

        self.printerComboBox = QComboBox(self.GroupBox)
        self.printerComboBox.setObjectName(u"printerComboBox")
        self.printerComboBox.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.printerComboBox)

        self.faxLabel = QLabel(self.GroupBox)
        self.faxLabel.setObjectName(u"faxLabel")
        self.faxLabel.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.faxLabel)

        self.faxComboBox = QComboBox(self.GroupBox)
        self.faxComboBox.setObjectName(u"faxComboBox")
        self.faxComboBox.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.faxComboBox)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lastUpdateLineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.prioritySpinBox = QSpinBox(self.GroupBox)
        self.prioritySpinBox.setObjectName(u"prioritySpinBox")

        self.horizontalLayout_2.addWidget(self.prioritySpinBox)

        self.priorityHorizontalSlider = QSlider(self.GroupBox)
        self.priorityHorizontalSlider.setObjectName(u"priorityHorizontalSlider")
        self.priorityHorizontalSlider.setMinimum(1)
        self.priorityHorizontalSlider.setMaximum(100)
        self.priorityHorizontalSlider.setValue(1)
        self.priorityHorizontalSlider.setSliderPosition(1)
        self.priorityHorizontalSlider.setOrientation(Qt.Horizontal)
        self.priorityHorizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.priorityHorizontalSlider.setTickInterval(5)

        self.horizontalLayout_2.addWidget(self.priorityHorizontalSlider)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)


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
        self.priorityLabel.setBuddy(self.priorityHorizontalSlider)
        self.printerLabel.setBuddy(self.printerComboBox)
        self.faxLabel.setBuddy(self.faxComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameLineEdit, self.prioritySpinBox)
        QWidget.setTabOrder(self.prioritySpinBox, self.priorityHorizontalSlider)
        QWidget.setTabOrder(self.priorityHorizontalSlider, self.printerComboBox)
        QWidget.setTabOrder(self.printerComboBox, self.faxComboBox)
        QWidget.setTabOrder(self.faxComboBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(DepartmentInputArea)

        QMetaObject.connectSlotsByName(DepartmentInputArea)
    # setupUi

    def retranslateUi(self, DepartmentInputArea):
        DepartmentInputArea.setWindowTitle(QCoreApplication.translate("DepartmentInputArea", u"Abteilung", None))
#if QT_CONFIG(accessibility)
        DepartmentInputArea.setAccessibleName(QCoreApplication.translate("DepartmentInputArea", u"DepartmentInputDialog", None))
#endif // QT_CONFIG(accessibility)
        DepartmentInputArea.setTitle(QCoreApplication.translate("DepartmentInputArea", u"Abteilung", None))
        self.label_Header.setText(QCoreApplication.translate("DepartmentInputArea", u"Abteilung", None))
        self.nameLabel.setText(QCoreApplication.translate("DepartmentInputArea", u"Name", None))
        self.priorityLabel.setText(QCoreApplication.translate("DepartmentInputArea", u"Priorit\u00e4t", None))
        self.printerLabel.setText(QCoreApplication.translate("DepartmentInputArea", u"Drucker", None))
        self.faxLabel.setText(QCoreApplication.translate("DepartmentInputArea", u"Fax", None))
        self.lastUpdateLabel.setText(QCoreApplication.translate("DepartmentInputArea", u"Letzte \u00c4nderung", None))
        self.addPushButton.setText(QCoreApplication.translate("DepartmentInputArea", u"+", None))
        self.editFinishPushButton.setText(QCoreApplication.translate("DepartmentInputArea", u"Bearbeiten", None))
    # retranslateUi

