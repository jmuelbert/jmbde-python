# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'printerinputarea.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_PrinterInputArea(object):
    def setupUi(self, PrinterInputArea):
        if not PrinterInputArea.objectName():
            PrinterInputArea.setObjectName(u"PrinterInputArea")
        PrinterInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(PrinterInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayoutWidget = QWidget(PrinterInputArea)
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
        self.label_Header.setFont(font)
        self.label_Header.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Header)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.resourcesTextEdit = QTextEdit(self.formLayoutWidget)
        self.resourcesTextEdit.setObjectName(u"resourcesTextEdit")
        self.resourcesTextEdit.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.resourcesTextEdit, 3, 2, 1, 1)

        self.deviceTypeComboBox = QComboBox(self.formLayoutWidget)
        self.deviceTypeComboBox.setObjectName(u"deviceTypeComboBox")
        self.deviceTypeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceTypeComboBox, 7, 4, 1, 1)

        self.activeCheckBox = QCheckBox(self.formLayoutWidget)
        self.activeCheckBox.setObjectName(u"activeCheckBox")

        self.gridLayout.addWidget(self.activeCheckBox, 9, 0, 1, 1)

        self.manufacturerLabel = QLabel(self.formLayoutWidget)
        self.manufacturerLabel.setObjectName(u"manufacturerLabel")

        self.gridLayout.addWidget(self.manufacturerLabel, 8, 0, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 10, 2, 1, 3)

        self.papersizeComboBox = QComboBox(self.formLayoutWidget)
        self.papersizeComboBox.setObjectName(u"papersizeComboBox")
        self.papersizeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.papersizeComboBox, 3, 4, 1, 1)

        self.employeeComboBox = QComboBox(self.formLayoutWidget)
        self.employeeComboBox.setObjectName(u"employeeComboBox")
        self.employeeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.employeeComboBox, 5, 2, 1, 1)

        self.computerLabel = QLabel(self.formLayoutWidget)
        self.computerLabel.setObjectName(u"computerLabel")

        self.gridLayout.addWidget(self.computerLabel, 5, 3, 1, 1)

        self.resourcesLabel = QLabel(self.formLayoutWidget)
        self.resourcesLabel.setObjectName(u"resourcesLabel")

        self.gridLayout.addWidget(self.resourcesLabel, 3, 0, 1, 1)

        self.replaceCheckBox = QCheckBox(self.formLayoutWidget)
        self.replaceCheckBox.setObjectName(u"replaceCheckBox")

        self.gridLayout.addWidget(self.replaceCheckBox, 9, 3, 1, 1)

        self.inventoryComboBox = QComboBox(self.formLayoutWidget)
        self.inventoryComboBox.setObjectName(u"inventoryComboBox")
        self.inventoryComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.inventoryComboBox, 8, 4, 1, 1)

        self.colorCheckBox = QCheckBox(self.formLayoutWidget)
        self.colorCheckBox.setObjectName(u"colorCheckBox")

        self.gridLayout.addWidget(self.colorCheckBox, 4, 0, 1, 1)

        self.networkLabel = QLabel(self.formLayoutWidget)
        self.networkLabel.setObjectName(u"networkLabel")

        self.gridLayout.addWidget(self.networkLabel, 1, 0, 1, 1)

        self.serialNumberLineEdit = QLineEdit(self.formLayoutWidget)
        self.serialNumberLineEdit.setObjectName(u"serialNumberLineEdit")

        self.gridLayout.addWidget(self.serialNumberLineEdit, 0, 4, 1, 1)

        self.departmentLabel = QLabel(self.formLayoutWidget)
        self.departmentLabel.setObjectName(u"departmentLabel")

        self.gridLayout.addWidget(self.departmentLabel, 6, 0, 1, 1)

        self.lastUpdateLabel = QLabel(self.formLayoutWidget)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")

        self.gridLayout.addWidget(self.lastUpdateLabel, 10, 0, 1, 1)

        self.networkLineEdit = QLineEdit(self.formLayoutWidget)
        self.networkLineEdit.setObjectName(u"networkLineEdit")

        self.gridLayout.addWidget(self.networkLineEdit, 1, 2, 1, 1)

        self.deviceNameLabel = QLabel(self.formLayoutWidget)
        self.deviceNameLabel.setObjectName(u"deviceNameLabel")

        self.gridLayout.addWidget(self.deviceNameLabel, 7, 0, 1, 1)

        self.inventoryLabel = QLabel(self.formLayoutWidget)
        self.inventoryLabel.setObjectName(u"inventoryLabel")

        self.gridLayout.addWidget(self.inventoryLabel, 8, 3, 1, 1)

        self.employeeLabel = QLabel(self.formLayoutWidget)
        self.employeeLabel.setObjectName(u"employeeLabel")

        self.gridLayout.addWidget(self.employeeLabel, 5, 0, 1, 1)

        self.paperSizeLabel = QLabel(self.formLayoutWidget)
        self.paperSizeLabel.setObjectName(u"paperSizeLabel")

        self.gridLayout.addWidget(self.paperSizeLabel, 3, 3, 1, 1)

        self.manufacturerComboBox = QComboBox(self.formLayoutWidget)
        self.manufacturerComboBox.setObjectName(u"manufacturerComboBox")
        self.manufacturerComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.manufacturerComboBox, 8, 2, 1, 1)

        self.placeLabel = QLabel(self.formLayoutWidget)
        self.placeLabel.setObjectName(u"placeLabel")

        self.gridLayout.addWidget(self.placeLabel, 6, 3, 1, 1)

        self.deviceNameComboBox = QComboBox(self.formLayoutWidget)
        self.deviceNameComboBox.setObjectName(u"deviceNameComboBox")
        self.deviceNameComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceNameComboBox, 7, 2, 1, 1)

        self.computerComboBox = QComboBox(self.formLayoutWidget)
        self.computerComboBox.setObjectName(u"computerComboBox")
        self.computerComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.computerComboBox, 5, 4, 1, 1)

        self.serialNumberLabel = QLabel(self.formLayoutWidget)
        self.serialNumberLabel.setObjectName(u"serialNumberLabel")

        self.gridLayout.addWidget(self.serialNumberLabel, 0, 3, 1, 1)

        self.departmentComboBox = QComboBox(self.formLayoutWidget)
        self.departmentComboBox.setObjectName(u"departmentComboBox")
        self.departmentComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.departmentComboBox, 6, 2, 1, 1)

        self.placeComboBox = QComboBox(self.formLayoutWidget)
        self.placeComboBox.setObjectName(u"placeComboBox")
        self.placeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.placeComboBox, 6, 4, 1, 1)

        self.deviceTypeLabel = QLabel(self.formLayoutWidget)
        self.deviceTypeLabel.setObjectName(u"deviceTypeLabel")

        self.gridLayout.addWidget(self.deviceTypeLabel, 7, 3, 1, 1)

        self.networkNameLabel = QLabel(self.formLayoutWidget)
        self.networkNameLabel.setObjectName(u"networkNameLabel")

        self.gridLayout.addWidget(self.networkNameLabel, 0, 0, 1, 1)

        self.networkNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.networkNameLineEdit.setObjectName(u"networkNameLineEdit")

        self.gridLayout.addWidget(self.networkNameLineEdit, 0, 2, 1, 1)

        self.ipAddressLabel = QLabel(self.formLayoutWidget)
        self.ipAddressLabel.setObjectName(u"ipAddressLabel")

        self.gridLayout.addWidget(self.ipAddressLabel, 1, 3, 1, 1)

        self.ipAddressLineEdit = QLineEdit(self.formLayoutWidget)
        self.ipAddressLineEdit.setObjectName(u"ipAddressLineEdit")

        self.gridLayout.addWidget(self.ipAddressLineEdit, 1, 4, 1, 1)


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
        self.label_Header.setBuddy(self.label_Header)
        self.manufacturerLabel.setBuddy(self.manufacturerComboBox)
        self.computerLabel.setBuddy(self.computerComboBox)
        self.resourcesLabel.setBuddy(self.resourcesTextEdit)
        self.networkLabel.setBuddy(self.networkLineEdit)
        self.departmentLabel.setBuddy(self.departmentComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        self.deviceNameLabel.setBuddy(self.deviceNameComboBox)
        self.inventoryLabel.setBuddy(self.inventoryComboBox)
        self.employeeLabel.setBuddy(self.employeeComboBox)
        self.paperSizeLabel.setBuddy(self.papersizeComboBox)
        self.placeLabel.setBuddy(self.placeComboBox)
        self.serialNumberLabel.setBuddy(self.serialNumberLineEdit)
        self.deviceTypeLabel.setBuddy(self.deviceTypeComboBox)
        self.networkNameLabel.setBuddy(self.networkNameLineEdit)
        self.ipAddressLabel.setBuddy(self.ipAddressLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.networkNameLineEdit, self.serialNumberLineEdit)
        QWidget.setTabOrder(self.serialNumberLineEdit, self.networkLineEdit)
        QWidget.setTabOrder(self.networkLineEdit, self.ipAddressLineEdit)
        QWidget.setTabOrder(self.ipAddressLineEdit, self.resourcesTextEdit)
        QWidget.setTabOrder(self.resourcesTextEdit, self.papersizeComboBox)
        QWidget.setTabOrder(self.papersizeComboBox, self.colorCheckBox)
        QWidget.setTabOrder(self.colorCheckBox, self.employeeComboBox)
        QWidget.setTabOrder(self.employeeComboBox, self.computerComboBox)
        QWidget.setTabOrder(self.computerComboBox, self.departmentComboBox)
        QWidget.setTabOrder(self.departmentComboBox, self.placeComboBox)
        QWidget.setTabOrder(self.placeComboBox, self.deviceNameComboBox)
        QWidget.setTabOrder(self.deviceNameComboBox, self.deviceTypeComboBox)
        QWidget.setTabOrder(self.deviceTypeComboBox, self.manufacturerComboBox)
        QWidget.setTabOrder(self.manufacturerComboBox, self.inventoryComboBox)
        QWidget.setTabOrder(self.inventoryComboBox, self.activeCheckBox)
        QWidget.setTabOrder(self.activeCheckBox, self.replaceCheckBox)
        QWidget.setTabOrder(self.replaceCheckBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.editFinishPushButton)

        self.retranslateUi(PrinterInputArea)

        QMetaObject.connectSlotsByName(PrinterInputArea)
    # setupUi

    def retranslateUi(self, PrinterInputArea):
        PrinterInputArea.setWindowTitle(QCoreApplication.translate("PrinterInputArea", u"Drucker", None))
#if QT_CONFIG(accessibility)
        PrinterInputArea.setAccessibleName(QCoreApplication.translate("PrinterInputArea", u"PrinterInputDialog", None))
#endif // QT_CONFIG(accessibility)
        PrinterInputArea.setTitle(QCoreApplication.translate("PrinterInputArea", u"Drucker", None))
        self.label_Header.setText(QCoreApplication.translate("PrinterInputArea", u"Drucker", None))
        self.activeCheckBox.setText(QCoreApplication.translate("PrinterInputArea", u"Aktiv", None))
        self.manufacturerLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Hersteller", None))
        self.computerLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Computer", None))
        self.resourcesLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Verbrauchsmaterial", None))
        self.replaceCheckBox.setText(QCoreApplication.translate("PrinterInputArea", u"ersetzen", None))
        self.colorCheckBox.setText(QCoreApplication.translate("PrinterInputArea", u"Farbe", None))
        self.networkLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Netzwerk", None))
        self.departmentLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Abteilung", None))
        self.lastUpdateLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Lezte \u00c4nderung", None))
        self.deviceNameLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Ger\u00e4tename", None))
        self.inventoryLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Inventar", None))
        self.employeeLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Mitarbeiter*in", None))
        self.paperSizeLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Papiergr\u00f6\u00dfe", None))
        self.placeLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Platz", None))
        self.serialNumberLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Seriennummer", None))
        self.deviceTypeLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Ger\u00e4tetyp", None))
        self.networkNameLabel.setText(QCoreApplication.translate("PrinterInputArea", u"Netzwerk Name", None))
        self.ipAddressLabel.setText(QCoreApplication.translate("PrinterInputArea", u"IP Adresse", None))
        self.addPushButton.setText(QCoreApplication.translate("PrinterInputArea", u"+", None))
        self.editFinishPushButton.setText(QCoreApplication.translate("PrinterInputArea", u"Bearbeiten", None))
    # retranslateUi

