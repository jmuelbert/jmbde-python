# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'computerinputarea.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Ui_ComputerInputArea(object):
    def setupUi(self, ComputerInputArea):
        if not ComputerInputArea.objectName():
            ComputerInputArea.setObjectName("ComputerInputArea")
        ComputerInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(ComputerInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayoutWidget = QWidget(ComputerInputArea)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Header = QLabel(self.formLayoutWidget)
        self.label_Header.setObjectName("label_Header")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_Header.setFont(font)
        self.label_Header.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Header)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.serialNumberLabel = QLabel(self.formLayoutWidget)
        self.serialNumberLabel.setObjectName("serialNumberLabel")

        self.gridLayout.addWidget(self.serialNumberLabel, 0, 3, 1, 1)

        self.printerLabel = QLabel(self.formLayoutWidget)
        self.printerLabel.setObjectName("printerLabel")
        self.printerLabel.setEnabled(False)

        self.gridLayout.addWidget(self.printerLabel, 5, 3, 1, 1)

        self.deviceTypeLabel = QLabel(self.formLayoutWidget)
        self.deviceTypeLabel.setObjectName("deviceTypeLabel")
        self.deviceTypeLabel.setEnabled(False)

        self.gridLayout.addWidget(self.deviceTypeLabel, 8, 3, 1, 1)

        self.departmentComboBox = QComboBox(self.formLayoutWidget)
        self.departmentComboBox.setObjectName("departmentComboBox")
        self.departmentComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.departmentComboBox, 7, 2, 1, 1)

        self.networkLabel = QLabel(self.formLayoutWidget)
        self.networkLabel.setObjectName("networkLabel")

        self.gridLayout.addWidget(self.networkLabel, 2, 0, 1, 1)

        self.inventoryLabel = QLabel(self.formLayoutWidget)
        self.inventoryLabel.setObjectName("inventoryLabel")
        self.inventoryLabel.setEnabled(False)

        self.gridLayout.addWidget(self.inventoryLabel, 9, 3, 1, 1)

        self.deviceNameComboBox = QComboBox(self.formLayoutWidget)
        self.deviceNameComboBox.setObjectName("deviceNameComboBox")
        self.deviceNameComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceNameComboBox, 8, 2, 1, 1)

        self.placeLabel = QLabel(self.formLayoutWidget)
        self.placeLabel.setObjectName("placeLabel")
        self.placeLabel.setEnabled(False)

        self.gridLayout.addWidget(self.placeLabel, 7, 3, 1, 1)

        self.placeComboBox = QComboBox(self.formLayoutWidget)
        self.placeComboBox.setObjectName("placeComboBox")
        self.placeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.placeComboBox, 7, 4, 1, 1)

        self.serviceTagLineEdit = QLineEdit(self.formLayoutWidget)
        self.serviceTagLineEdit.setObjectName("serviceTagLineEdit")

        self.gridLayout.addWidget(self.serviceTagLineEdit, 1, 4, 1, 1)

        self.manufacturerComboBox = QComboBox(self.formLayoutWidget)
        self.manufacturerComboBox.setObjectName("manufacturerComboBox")
        self.manufacturerComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.manufacturerComboBox, 9, 2, 1, 1)

        self.printerComboBox = QComboBox(self.formLayoutWidget)
        self.printerComboBox.setObjectName("printerComboBox")
        self.printerComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.printerComboBox, 5, 4, 1, 1)

        self.lastUpdateLabel = QLabel(self.formLayoutWidget)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 11, 0, 1, 1)

        self.processorComboBox = QComboBox(self.formLayoutWidget)
        self.processorComboBox.setObjectName("processorComboBox")
        self.processorComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.processorComboBox, 4, 2, 1, 1)

        self.processorLabel = QLabel(self.formLayoutWidget)
        self.processorLabel.setObjectName("processorLabel")
        self.processorLabel.setEnabled(False)

        self.gridLayout.addWidget(self.processorLabel, 4, 0, 1, 1)

        self.inventoryComboBox = QComboBox(self.formLayoutWidget)
        self.inventoryComboBox.setObjectName("inventoryComboBox")
        self.inventoryComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.inventoryComboBox, 9, 4, 1, 1)

        self.serviceNumberLineEdit = QLineEdit(self.formLayoutWidget)
        self.serviceNumberLineEdit.setObjectName("serviceNumberLineEdit")

        self.gridLayout.addWidget(self.serviceNumberLineEdit, 1, 2, 1, 1)

        self.networkLineEdit = QLineEdit(self.formLayoutWidget)
        self.networkLineEdit.setObjectName("networkLineEdit")

        self.gridLayout.addWidget(self.networkLineEdit, 2, 2, 1, 1)

        self.serviceNumberLabel = QLabel(self.formLayoutWidget)
        self.serviceNumberLabel.setObjectName("serviceNumberLabel")

        self.gridLayout.addWidget(self.serviceNumberLabel, 1, 0, 1, 1)

        self.serviceTagLabel = QLabel(self.formLayoutWidget)
        self.serviceTagLabel.setObjectName("serviceTagLabel")

        self.gridLayout.addWidget(self.serviceTagLabel, 1, 3, 1, 1)

        self.manufacturerLabel = QLabel(self.formLayoutWidget)
        self.manufacturerLabel.setObjectName("manufacturerLabel")
        self.manufacturerLabel.setEnabled(False)

        self.gridLayout.addWidget(self.manufacturerLabel, 9, 0, 1, 1)

        self.activeCheckBox = QCheckBox(self.formLayoutWidget)
        self.activeCheckBox.setObjectName("activeCheckBox")

        self.gridLayout.addWidget(self.activeCheckBox, 10, 0, 1, 1)

        self.deviceNameLabel = QLabel(self.formLayoutWidget)
        self.deviceNameLabel.setObjectName("deviceNameLabel")
        self.deviceNameLabel.setEnabled(False)

        self.gridLayout.addWidget(self.deviceNameLabel, 8, 0, 1, 1)

        self.deviceTypeComboBox = QComboBox(self.formLayoutWidget)
        self.deviceTypeComboBox.setObjectName("deviceTypeComboBox")
        self.deviceTypeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceTypeComboBox, 8, 4, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 11, 2, 1, 1)

        self.replaceCheckBox = QCheckBox(self.formLayoutWidget)
        self.replaceCheckBox.setObjectName("replaceCheckBox")

        self.gridLayout.addWidget(self.replaceCheckBox, 10, 3, 1, 1)

        self.serialNumberLineEdit = QLineEdit(self.formLayoutWidget)
        self.serialNumberLineEdit.setObjectName("serialNumberLineEdit")

        self.gridLayout.addWidget(self.serialNumberLineEdit, 0, 4, 1, 1)

        self.departmentLabel = QLabel(self.formLayoutWidget)
        self.departmentLabel.setObjectName("departmentLabel")
        self.departmentLabel.setEnabled(False)

        self.gridLayout.addWidget(self.departmentLabel, 7, 0, 1, 1)

        self.memorySpinBox = QSpinBox(self.formLayoutWidget)
        self.memorySpinBox.setObjectName("memorySpinBox")

        self.gridLayout.addWidget(self.memorySpinBox, 3, 4, 1, 1)

        self.memoryLabel = QLabel(self.formLayoutWidget)
        self.memoryLabel.setObjectName("memoryLabel")

        self.gridLayout.addWidget(self.memoryLabel, 3, 3, 1, 1)

        self.netWorkNameLabel = QLabel(self.formLayoutWidget)
        self.netWorkNameLabel.setObjectName("netWorkNameLabel")

        self.gridLayout.addWidget(self.netWorkNameLabel, 0, 0, 1, 1)

        self.netWorkNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.netWorkNameLineEdit.setObjectName("netWorkNameLineEdit")

        self.gridLayout.addWidget(self.netWorkNameLineEdit, 0, 2, 1, 1)

        self.ipAddressLabel = QLabel(self.formLayoutWidget)
        self.ipAddressLabel.setObjectName("ipAddressLabel")

        self.gridLayout.addWidget(self.ipAddressLabel, 2, 3, 1, 1)

        self.ipAddressLineEdit = QLineEdit(self.formLayoutWidget)
        self.ipAddressLineEdit.setObjectName("ipAddressLineEdit")

        self.gridLayout.addWidget(self.ipAddressLineEdit, 2, 4, 1, 1)

        self.operationSystemLabel = QLabel(self.formLayoutWidget)
        self.operationSystemLabel.setObjectName("operationSystemLabel")
        self.operationSystemLabel.setEnabled(False)

        self.gridLayout.addWidget(self.operationSystemLabel, 3, 0, 1, 1)

        self.operationSystemComboBox = QComboBox(self.formLayoutWidget)
        self.operationSystemComboBox.setObjectName("operationSystemComboBox")
        self.operationSystemComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.operationSystemComboBox, 3, 2, 1, 1)

        self.softwareLabel = QLabel(self.formLayoutWidget)
        self.softwareLabel.setObjectName("softwareLabel")
        self.softwareLabel.setEnabled(False)

        self.gridLayout.addWidget(self.softwareLabel, 4, 3, 1, 1)

        self.softwareComboBox = QComboBox(self.formLayoutWidget)
        self.softwareComboBox.setObjectName("softwareComboBox")
        self.softwareComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.softwareComboBox, 4, 4, 1, 1)

        self.employeeLabel = QLabel(self.formLayoutWidget)
        self.employeeLabel.setObjectName("employeeLabel")
        self.employeeLabel.setEnabled(False)

        self.gridLayout.addWidget(self.employeeLabel, 5, 0, 1, 1)

        self.employeeComboBox = QComboBox(self.formLayoutWidget)
        self.employeeComboBox.setObjectName("employeeComboBox")
        self.employeeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.employeeComboBox, 5, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addPushButton = QPushButton(self.formLayoutWidget)
        self.addPushButton.setObjectName("addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.formLayoutWidget)
        self.editFinishPushButton.setObjectName("editFinishPushButton")

        self.horizontalLayout.addWidget(self.editFinishPushButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addWidget(self.formLayoutWidget)

        # if QT_CONFIG(shortcut)
        self.serialNumberLabel.setBuddy(self.serialNumberLineEdit)
        self.printerLabel.setBuddy(self.printerComboBox)
        self.deviceTypeLabel.setBuddy(self.deviceTypeComboBox)
        self.networkLabel.setBuddy(self.networkLineEdit)
        self.inventoryLabel.setBuddy(self.inventoryComboBox)
        self.placeLabel.setBuddy(self.placeComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        self.processorLabel.setBuddy(self.processorComboBox)
        self.serviceNumberLabel.setBuddy(self.serviceNumberLineEdit)
        self.serviceTagLabel.setBuddy(self.serviceTagLineEdit)
        self.manufacturerLabel.setBuddy(self.manufacturerComboBox)
        self.deviceNameLabel.setBuddy(self.deviceNameComboBox)
        self.departmentLabel.setBuddy(self.departmentComboBox)
        self.memoryLabel.setBuddy(self.memorySpinBox)
        self.netWorkNameLabel.setBuddy(self.netWorkNameLineEdit)
        self.ipAddressLabel.setBuddy(self.ipAddressLineEdit)
        self.operationSystemLabel.setBuddy(self.operationSystemComboBox)
        self.softwareLabel.setBuddy(self.softwareComboBox)
        self.employeeLabel.setBuddy(self.employeeComboBox)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.netWorkNameLineEdit, self.serialNumberLineEdit)
        QWidget.setTabOrder(self.serialNumberLineEdit, self.serviceNumberLineEdit)
        QWidget.setTabOrder(self.serviceNumberLineEdit, self.serviceTagLineEdit)
        QWidget.setTabOrder(self.serviceTagLineEdit, self.networkLineEdit)
        QWidget.setTabOrder(self.networkLineEdit, self.ipAddressLineEdit)
        QWidget.setTabOrder(self.ipAddressLineEdit, self.operationSystemComboBox)
        QWidget.setTabOrder(self.operationSystemComboBox, self.memorySpinBox)
        QWidget.setTabOrder(self.memorySpinBox, self.processorComboBox)
        QWidget.setTabOrder(self.processorComboBox, self.softwareComboBox)
        QWidget.setTabOrder(self.softwareComboBox, self.employeeComboBox)
        QWidget.setTabOrder(self.employeeComboBox, self.printerComboBox)
        QWidget.setTabOrder(self.printerComboBox, self.departmentComboBox)
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

        self.retranslateUi(ComputerInputArea)

        QMetaObject.connectSlotsByName(ComputerInputArea)

    # setupUi

    def retranslateUi(self, ComputerInputArea):
        ComputerInputArea.setWindowTitle(
            QCoreApplication.translate("ComputerInputArea", "GroupBox", None)
        )
        # if QT_CONFIG(accessibility)
        ComputerInputArea.setAccessibleName(
            QCoreApplication.translate("ComputerInputArea", "ComputerInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        ComputerInputArea.setTitle(
            QCoreApplication.translate("ComputerInputArea", "Computer", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("ComputerInputArea", "Computer", None)
        )
        self.serialNumberLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Serial Number", None)
        )
        self.printerLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Drucker", None)
        )
        self.deviceTypeLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Ger\u00e4tetyp", None)
        )
        self.networkLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Netzwerk", None)
        )
        self.inventoryLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Inventarnummer", None)
        )
        self.placeLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Platz", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "ComputerInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.processorLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Prozessor", None)
        )
        self.serviceNumberLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Service Nummer", None)
        )
        self.serviceTagLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Service Tag", None)
        )
        self.manufacturerLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Hersteller", None)
        )
        self.activeCheckBox.setText(
            QCoreApplication.translate("ComputerInputArea", "Aktiv", None)
        )
        self.deviceNameLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Ger\u00e4tename", None)
        )
        self.replaceCheckBox.setText(
            QCoreApplication.translate("ComputerInputArea", "zu ersetzen", None)
        )
        self.departmentLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Abteilung", None)
        )
        self.memoryLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Speicher", None)
        )
        self.netWorkNameLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Name", None)
        )
        self.ipAddressLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "IP Addresse", None)
        )
        self.operationSystemLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Betriebssystem", None)
        )
        self.softwareLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Software", None)
        )
        self.employeeLabel.setText(
            QCoreApplication.translate("ComputerInputArea", "Mitarbeiter*in", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("ComputerInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("ComputerInputArea", "Bearbeiten", None)
        )

    # retranslateUi
