# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'faxinputarea.ui'
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
    QVBoxLayout,
    QWidget,
)


class Ui_FaxInputArea(object):
    def setupUi(self, FaxInputArea):
        if not FaxInputArea.objectName():
            FaxInputArea.setObjectName(u"FaxInputArea")
        FaxInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(FaxInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayoutWidget = QWidget(FaxInputArea)
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

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.employeeComboBox = QComboBox(self.formLayoutWidget)
        self.employeeComboBox.setObjectName(u"employeeComboBox")
        self.employeeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.employeeComboBox, 2, 2, 1, 1)

        self.departmentLabel = QLabel(self.formLayoutWidget)
        self.departmentLabel.setObjectName(u"departmentLabel")
        self.departmentLabel.setEnabled(False)

        self.gridLayout.addWidget(self.departmentLabel, 3, 0, 1, 1)

        self.inventoryLabel = QLabel(self.formLayoutWidget)
        self.inventoryLabel.setObjectName(u"inventoryLabel")
        self.inventoryLabel.setEnabled(False)

        self.gridLayout.addWidget(self.inventoryLabel, 5, 3, 1, 1)

        self.inventoryComboBox = QComboBox(self.formLayoutWidget)
        self.inventoryComboBox.setObjectName(u"inventoryComboBox")
        self.inventoryComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.inventoryComboBox, 5, 5, 1, 1)

        self.manufacturerComboBox = QComboBox(self.formLayoutWidget)
        self.manufacturerComboBox.setObjectName(u"manufacturerComboBox")
        self.manufacturerComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.manufacturerComboBox, 5, 2, 1, 1)

        self.deviceTypeComboBox = QComboBox(self.formLayoutWidget)
        self.deviceTypeComboBox.setObjectName(u"deviceTypeComboBox")
        self.deviceTypeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceTypeComboBox, 4, 5, 1, 1)

        self.serialNumberLabel = QLabel(self.formLayoutWidget)
        self.serialNumberLabel.setObjectName(u"serialNumberLabel")

        self.gridLayout.addWidget(self.serialNumberLabel, 1, 0, 1, 1)

        self.placeLabel = QLabel(self.formLayoutWidget)
        self.placeLabel.setObjectName(u"placeLabel")
        self.placeLabel.setEnabled(False)

        self.gridLayout.addWidget(self.placeLabel, 3, 3, 1, 1)

        self.employeeLabel = QLabel(self.formLayoutWidget)
        self.employeeLabel.setObjectName(u"employeeLabel")
        self.employeeLabel.setEnabled(False)

        self.gridLayout.addWidget(self.employeeLabel, 2, 0, 1, 1)

        self.placeComboBox = QComboBox(self.formLayoutWidget)
        self.placeComboBox.setObjectName(u"placeComboBox")
        self.placeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.placeComboBox, 3, 5, 1, 1)

        self.deviceNameComboBox = QComboBox(self.formLayoutWidget)
        self.deviceNameComboBox.setObjectName(u"deviceNameComboBox")
        self.deviceNameComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceNameComboBox, 4, 2, 1, 1)

        self.pinLabel = QLabel(self.formLayoutWidget)
        self.pinLabel.setObjectName(u"pinLabel")

        self.gridLayout.addWidget(self.pinLabel, 0, 3, 1, 1)

        self.replaceCheckBox = QCheckBox(self.formLayoutWidget)
        self.replaceCheckBox.setObjectName(u"replaceCheckBox")

        self.gridLayout.addWidget(self.replaceCheckBox, 6, 3, 1, 1)

        self.deviceTypeLabel = QLabel(self.formLayoutWidget)
        self.deviceTypeLabel.setObjectName(u"deviceTypeLabel")
        self.deviceTypeLabel.setEnabled(False)

        self.gridLayout.addWidget(self.deviceTypeLabel, 4, 3, 1, 1)

        self.deviceNameLabel = QLabel(self.formLayoutWidget)
        self.deviceNameLabel.setObjectName(u"deviceNameLabel")
        self.deviceNameLabel.setEnabled(False)

        self.gridLayout.addWidget(self.deviceNameLabel, 4, 0, 1, 1)

        self.serialNumberLineEdit = QLineEdit(self.formLayoutWidget)
        self.serialNumberLineEdit.setObjectName(u"serialNumberLineEdit")

        self.gridLayout.addWidget(self.serialNumberLineEdit, 1, 2, 1, 1)

        self.departmentComboBox = QComboBox(self.formLayoutWidget)
        self.departmentComboBox.setObjectName(u"departmentComboBox")
        self.departmentComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.departmentComboBox, 3, 2, 1, 1)

        self.manufacturerLabel = QLabel(self.formLayoutWidget)
        self.manufacturerLabel.setObjectName(u"manufacturerLabel")
        self.manufacturerLabel.setEnabled(False)

        self.gridLayout.addWidget(self.manufacturerLabel, 5, 0, 1, 1)

        self.pinLineEdit = QLineEdit(self.formLayoutWidget)
        self.pinLineEdit.setObjectName(u"pinLineEdit")
        self.pinLineEdit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.pinLineEdit, 0, 5, 1, 1)

        self.activeCheckBox = QCheckBox(self.formLayoutWidget)
        self.activeCheckBox.setObjectName(u"activeCheckBox")

        self.gridLayout.addWidget(self.activeCheckBox, 6, 2, 1, 1)

        self.numberLabel = QLabel(self.formLayoutWidget)
        self.numberLabel.setObjectName(u"numberLabel")

        self.gridLayout.addWidget(self.numberLabel, 0, 0, 1, 1)

        self.numberLineEdit = QLineEdit(self.formLayoutWidget)
        self.numberLineEdit.setObjectName(u"numberLineEdit")

        self.gridLayout.addWidget(self.numberLineEdit, 0, 2, 1, 1)

        self.lastUpdateLabel = QLabel(self.formLayoutWidget)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 7, 0, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 7, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addPushButton = QPushButton(self.formLayoutWidget)
        self.addPushButton.setObjectName(u"addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.formLayoutWidget)
        self.editFinishPushButton.setObjectName(u"editFinishPushButton")

        self.horizontalLayout.addWidget(self.editFinishPushButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addWidget(self.formLayoutWidget)

        # if QT_CONFIG(shortcut)
        self.departmentLabel.setBuddy(self.departmentComboBox)
        self.inventoryLabel.setBuddy(self.inventoryComboBox)
        self.serialNumberLabel.setBuddy(self.serialNumberLineEdit)
        self.placeLabel.setBuddy(self.placeComboBox)
        self.employeeLabel.setBuddy(self.employeeComboBox)
        self.pinLabel.setBuddy(self.pinLineEdit)
        self.deviceTypeLabel.setBuddy(self.deviceTypeComboBox)
        self.deviceNameLabel.setBuddy(self.deviceNameComboBox)
        self.manufacturerLabel.setBuddy(self.manufacturerComboBox)
        self.numberLabel.setBuddy(self.numberLineEdit)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
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

        self.retranslateUi(FaxInputArea)

        QMetaObject.connectSlotsByName(FaxInputArea)

    # setupUi

    def retranslateUi(self, FaxInputArea):
        FaxInputArea.setWindowTitle(
            QCoreApplication.translate("FaxInputArea", u"Fax", None)
        )
        # if QT_CONFIG(accessibility)
        FaxInputArea.setAccessibleName(
            QCoreApplication.translate("FaxInputArea", u"FaxInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        FaxInputArea.setTitle(QCoreApplication.translate("FaxInputArea", u"Fax", None))
        self.label_Header.setText(
            QCoreApplication.translate("FaxInputArea", u"Fax", None)
        )
        self.departmentLabel.setText(
            QCoreApplication.translate("FaxInputArea", u"Abteilung", None)
        )
        self.inventoryLabel.setText(
            QCoreApplication.translate("FaxInputArea", u"Inventar Nummer", None)
        )
        self.serialNumberLabel.setText(
            QCoreApplication.translate("FaxInputArea", u"Seriennummer", None)
        )
        self.placeLabel.setText(
            QCoreApplication.translate("FaxInputArea", u"Platz", None)
        )
        self.employeeLabel.setText(
            QCoreApplication.translate("FaxInputArea", u"Mitarbeiter*in", None)
        )
        self.pinLabel.setText(QCoreApplication.translate("FaxInputArea", u"Pin", None))
        self.replaceCheckBox.setText(
            QCoreApplication.translate("FaxInputArea", u"ersetzen", None)
        )
        self.deviceTypeLabel.setText(
            QCoreApplication.translate("FaxInputArea", u"Ger\u00e4tetyp", None)
        )
        self.deviceNameLabel.setText(
            QCoreApplication.translate("FaxInputArea", u"Ger\u00e4tename", None)
        )
        self.manufacturerLabel.setText(
            QCoreApplication.translate("FaxInputArea", u"Hersteller", None)
        )
        self.activeCheckBox.setText(
            QCoreApplication.translate("FaxInputArea", u"Aktiv", None)
        )
        self.numberLabel.setText(
            QCoreApplication.translate("FaxInputArea", u"Nummer", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate("FaxInputArea", u"Letzte \u00c4nderung", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("FaxInputArea", u"+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("FaxInputArea", u"Bearbeiten", None)
        )

    # retranslateUi