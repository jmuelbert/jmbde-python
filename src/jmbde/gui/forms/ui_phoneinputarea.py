# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'phoneinputarea.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_PhoneInputArea(object):
    def setupUi(self, PhoneInputArea):
        if not PhoneInputArea.objectName():
            PhoneInputArea.setObjectName(u"PhoneInputArea")
        PhoneInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(PhoneInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayoutWidget = QWidget(PhoneInputArea)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerLabel = QLabel(self.formLayoutWidget)
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
        self.deviceNameLabel = QLabel(self.formLayoutWidget)
        self.deviceNameLabel.setObjectName(u"deviceNameLabel")
        self.deviceNameLabel.setEnabled(False)
        self.deviceNameLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.deviceNameLabel, 6, 0, 1, 1)

        self.placeLabel = QLabel(self.formLayoutWidget)
        self.placeLabel.setObjectName(u"placeLabel")
        self.placeLabel.setEnabled(False)
        self.placeLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.placeLabel, 4, 2, 1, 1)

        self.pinLineEdit = QLineEdit(self.formLayoutWidget)
        self.pinLineEdit.setObjectName(u"pinLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pinLineEdit.sizePolicy().hasHeightForWidth())
        self.pinLineEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pinLineEdit, 1, 3, 1, 1)

        self.pinLabel = QLabel(self.formLayoutWidget)
        self.pinLabel.setObjectName(u"pinLabel")

        self.gridLayout.addWidget(self.pinLabel, 1, 2, 1, 1)

        self.serialNumberLineEdit = QLineEdit(self.formLayoutWidget)
        self.serialNumberLineEdit.setObjectName(u"serialNumberLineEdit")

        self.gridLayout.addWidget(self.serialNumberLineEdit, 2, 1, 1, 1)

        self.numberLineEdit = QLineEdit(self.formLayoutWidget)
        self.numberLineEdit.setObjectName(u"numberLineEdit")
        sizePolicy.setHeightForWidth(self.numberLineEdit.sizePolicy().hasHeightForWidth())
        self.numberLineEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.numberLineEdit, 1, 1, 1, 1)

        self.manufacturerLabel = QLabel(self.formLayoutWidget)
        self.manufacturerLabel.setObjectName(u"manufacturerLabel")
        self.manufacturerLabel.setEnabled(False)

        self.gridLayout.addWidget(self.manufacturerLabel, 8, 0, 1, 1)

        self.deviceNameComboBox = QComboBox(self.formLayoutWidget)
        self.deviceNameComboBox.setObjectName(u"deviceNameComboBox")
        self.deviceNameComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceNameComboBox, 6, 1, 1, 1)

        self.deviceTypeComboBox = QComboBox(self.formLayoutWidget)
        self.deviceTypeComboBox.setObjectName(u"deviceTypeComboBox")
        self.deviceTypeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceTypeComboBox, 6, 3, 1, 1)

        self.numberLabel = QLabel(self.formLayoutWidget)
        self.numberLabel.setObjectName(u"numberLabel")

        self.gridLayout.addWidget(self.numberLabel, 1, 0, 1, 1)

        self.inventoryLabel = QLabel(self.formLayoutWidget)
        self.inventoryLabel.setObjectName(u"inventoryLabel")
        self.inventoryLabel.setEnabled(False)

        self.gridLayout.addWidget(self.inventoryLabel, 8, 2, 1, 1)

        self.deviceTypeLabel = QLabel(self.formLayoutWidget)
        self.deviceTypeLabel.setObjectName(u"deviceTypeLabel")
        self.deviceTypeLabel.setEnabled(False)
        self.deviceTypeLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.deviceTypeLabel, 6, 2, 1, 1)

        self.departmentComboBox = QComboBox(self.formLayoutWidget)
        self.departmentComboBox.setObjectName(u"departmentComboBox")
        self.departmentComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.departmentComboBox, 4, 1, 1, 1)

        self.placeComboBox = QComboBox(self.formLayoutWidget)
        self.placeComboBox.setObjectName(u"placeComboBox")
        self.placeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.placeComboBox, 4, 3, 1, 1)

        self.employeeLabel = QLabel(self.formLayoutWidget)
        self.employeeLabel.setObjectName(u"employeeLabel")
        self.employeeLabel.setEnabled(False)
        self.employeeLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.employeeLabel, 3, 0, 1, 1)

        self.inventoryComboBox = QComboBox(self.formLayoutWidget)
        self.inventoryComboBox.setObjectName(u"inventoryComboBox")
        self.inventoryComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.inventoryComboBox, 8, 3, 1, 1)

        self.serialNumberLabel = QLabel(self.formLayoutWidget)
        self.serialNumberLabel.setObjectName(u"serialNumberLabel")

        self.gridLayout.addWidget(self.serialNumberLabel, 2, 0, 1, 1)

        self.activeCheckBox = QCheckBox(self.formLayoutWidget)
        self.activeCheckBox.setObjectName(u"activeCheckBox")

        self.gridLayout.addWidget(self.activeCheckBox, 9, 1, 1, 1)

        self.departmentLabel = QLabel(self.formLayoutWidget)
        self.departmentLabel.setObjectName(u"departmentLabel")
        self.departmentLabel.setEnabled(False)

        self.gridLayout.addWidget(self.departmentLabel, 4, 0, 1, 1)

        self.manufacturerComboBox = QComboBox(self.formLayoutWidget)
        self.manufacturerComboBox.setObjectName(u"manufacturerComboBox")
        self.manufacturerComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.manufacturerComboBox, 8, 1, 1, 1)

        self.employeeComboBox = QComboBox(self.formLayoutWidget)
        self.employeeComboBox.setObjectName(u"employeeComboBox")
        self.employeeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.employeeComboBox, 3, 1, 1, 1)

        self.lastUpdateLabel = QLabel(self.formLayoutWidget)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 10, 0, 1, 1)

        self.replaceCheckBox = QCheckBox(self.formLayoutWidget)
        self.replaceCheckBox.setObjectName(u"replaceCheckBox")

        self.gridLayout.addWidget(self.replaceCheckBox, 9, 2, 1, 2)

        self.lastUpdateLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 10, 1, 1, 3)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addPushButton = QPushButton(self.formLayoutWidget)
        self.addPushButton.setObjectName(u"addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.formLayoutWidget)
        self.editFinishPushButton.setObjectName(u"editFinishPushButton")

        self.horizontalLayout.addWidget(self.editFinishPushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.formLayoutWidget)

#if QT_CONFIG(shortcut)
        self.deviceNameLabel.setBuddy(self.deviceNameComboBox)
        self.placeLabel.setBuddy(self.placeComboBox)
        self.pinLabel.setBuddy(self.pinLineEdit)
        self.manufacturerLabel.setBuddy(self.manufacturerComboBox)
        self.numberLabel.setBuddy(self.numberLineEdit)
        self.inventoryLabel.setBuddy(self.inventoryComboBox)
        self.deviceTypeLabel.setBuddy(self.deviceTypeComboBox)
        self.employeeLabel.setBuddy(self.employeeComboBox)
        self.serialNumberLabel.setBuddy(self.serialNumberLineEdit)
        self.departmentLabel.setBuddy(self.departmentComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.numberLineEdit, self.pinLineEdit)
        QWidget.setTabOrder(self.pinLineEdit, self.serialNumberLineEdit)
        QWidget.setTabOrder(self.serialNumberLineEdit, self.employeeComboBox)
        QWidget.setTabOrder(self.employeeComboBox, self.departmentComboBox)
        QWidget.setTabOrder(self.departmentComboBox, self.placeComboBox)
        QWidget.setTabOrder(self.placeComboBox, self.deviceNameComboBox)
        QWidget.setTabOrder(self.deviceNameComboBox, self.deviceTypeComboBox)
        QWidget.setTabOrder(self.deviceTypeComboBox, self.manufacturerComboBox)
        QWidget.setTabOrder(self.manufacturerComboBox, self.inventoryComboBox)
        QWidget.setTabOrder(self.inventoryComboBox, self.activeCheckBox)
        QWidget.setTabOrder(self.activeCheckBox, self.replaceCheckBox)
        QWidget.setTabOrder(self.replaceCheckBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(PhoneInputArea)

        QMetaObject.connectSlotsByName(PhoneInputArea)
    # setupUi

    def retranslateUi(self, PhoneInputArea):
        PhoneInputArea.setWindowTitle(QCoreApplication.translate("PhoneInputArea", u"Telefon", None))
#if QT_CONFIG(accessibility)
        PhoneInputArea.setAccessibleName(QCoreApplication.translate("PhoneInputArea", u"PhoneInputDialog", None))
#endif // QT_CONFIG(accessibility)
        PhoneInputArea.setTitle(QCoreApplication.translate("PhoneInputArea", u"Telefon", None))
        self.headerLabel.setText(QCoreApplication.translate("PhoneInputArea", u"Telefon", None))
        self.deviceNameLabel.setText(QCoreApplication.translate("PhoneInputArea", u"Ger\u00e4tename", None))
        self.placeLabel.setText(QCoreApplication.translate("PhoneInputArea", u"Platz", None))
        self.pinLabel.setText(QCoreApplication.translate("PhoneInputArea", u"Pin", None))
        self.manufacturerLabel.setText(QCoreApplication.translate("PhoneInputArea", u"Hersteller", None))
        self.numberLabel.setText(QCoreApplication.translate("PhoneInputArea", u"Nummer", None))
        self.inventoryLabel.setText(QCoreApplication.translate("PhoneInputArea", u"Inventar", None))
        self.deviceTypeLabel.setText(QCoreApplication.translate("PhoneInputArea", u"Ger\u00e4tetyp", None))
        self.employeeLabel.setText(QCoreApplication.translate("PhoneInputArea", u"Mitarbeiter*in", None))
        self.serialNumberLabel.setText(QCoreApplication.translate("PhoneInputArea", u"Seriennummer", None))
        self.activeCheckBox.setText(QCoreApplication.translate("PhoneInputArea", u"Aktiv", None))
        self.departmentLabel.setText(QCoreApplication.translate("PhoneInputArea", u"Abteilung", None))
        self.lastUpdateLabel.setText(QCoreApplication.translate("PhoneInputArea", u"Letzte \u00c4nderuung", None))
        self.replaceCheckBox.setText(QCoreApplication.translate("PhoneInputArea", u"ersetzen", None))
        self.addPushButton.setText(QCoreApplication.translate("PhoneInputArea", u"+", None))
        self.editFinishPushButton.setText(QCoreApplication.translate("PhoneInputArea", u"Bearbeiten", None))
    # retranslateUi

