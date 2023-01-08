# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mobileinputarea.ui'
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


class Ui_MobileInputArea(object):
    def setupUi(self, MobileInputArea):
        if not MobileInputArea.objectName():
            MobileInputArea.setObjectName("MobileInputArea")
        MobileInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(MobileInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayoutWidget = QWidget(MobileInputArea)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QLabel(self.formLayoutWidget)
        self.headerLabel.setObjectName("headerLabel")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.headerLabel)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.departmentLabel = QLabel(self.formLayoutWidget)
        self.departmentLabel.setObjectName("departmentLabel")
        self.departmentLabel.setEnabled(False)

        self.gridLayout.addWidget(self.departmentLabel, 3, 0, 1, 1)

        self.placeLabel = QLabel(self.formLayoutWidget)
        self.placeLabel.setObjectName("placeLabel")
        self.placeLabel.setEnabled(False)

        self.gridLayout.addWidget(self.placeLabel, 3, 3, 1, 1)

        self.deviceNameComboBox = QComboBox(self.formLayoutWidget)
        self.deviceNameComboBox.setObjectName("deviceNameComboBox")
        self.deviceNameComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceNameComboBox, 4, 2, 1, 1)

        self.numberLineEdit = QLineEdit(self.formLayoutWidget)
        self.numberLineEdit.setObjectName("numberLineEdit")

        self.gridLayout.addWidget(self.numberLineEdit, 0, 2, 1, 1)

        self.manufacturerComboBox = QComboBox(self.formLayoutWidget)
        self.manufacturerComboBox.setObjectName("manufacturerComboBox")
        self.manufacturerComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.manufacturerComboBox, 5, 2, 1, 1)

        self.pinLabel = QLabel(self.formLayoutWidget)
        self.pinLabel.setObjectName("pinLabel")

        self.gridLayout.addWidget(self.pinLabel, 0, 3, 1, 1)

        self.numberLabel = QLabel(self.formLayoutWidget)
        self.numberLabel.setObjectName("numberLabel")

        self.gridLayout.addWidget(self.numberLabel, 0, 0, 1, 1)

        self.employeeComboBox = QComboBox(self.formLayoutWidget)
        self.employeeComboBox.setObjectName("employeeComboBox")
        self.employeeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.employeeComboBox, 2, 2, 1, 1)

        self.employeeLabel = QLabel(self.formLayoutWidget)
        self.employeeLabel.setObjectName("employeeLabel")
        self.employeeLabel.setEnabled(False)

        self.gridLayout.addWidget(self.employeeLabel, 2, 0, 1, 1)

        self.manufacturerLabel = QLabel(self.formLayoutWidget)
        self.manufacturerLabel.setObjectName("manufacturerLabel")
        self.manufacturerLabel.setEnabled(False)

        self.gridLayout.addWidget(self.manufacturerLabel, 5, 0, 1, 1)

        self.serialNumberLabel = QLabel(self.formLayoutWidget)
        self.serialNumberLabel.setObjectName("serialNumberLabel")

        self.gridLayout.addWidget(self.serialNumberLabel, 1, 0, 1, 1)

        self.deviceTypeLabel = QLabel(self.formLayoutWidget)
        self.deviceTypeLabel.setObjectName("deviceTypeLabel")
        self.deviceTypeLabel.setEnabled(False)

        self.gridLayout.addWidget(self.deviceTypeLabel, 4, 3, 1, 1)

        self.cardNumberLabel = QLabel(self.formLayoutWidget)
        self.cardNumberLabel.setObjectName("cardNumberLabel")

        self.gridLayout.addWidget(self.cardNumberLabel, 1, 3, 1, 1)

        self.serialNumberLineEdit = QLineEdit(self.formLayoutWidget)
        self.serialNumberLineEdit.setObjectName("serialNumberLineEdit")

        self.gridLayout.addWidget(self.serialNumberLineEdit, 1, 2, 1, 1)

        self.deviceNameLabel = QLabel(self.formLayoutWidget)
        self.deviceNameLabel.setObjectName("deviceNameLabel")
        self.deviceNameLabel.setEnabled(False)

        self.gridLayout.addWidget(self.deviceNameLabel, 4, 0, 1, 1)

        self.departmentComboBox = QComboBox(self.formLayoutWidget)
        self.departmentComboBox.setObjectName("departmentComboBox")
        self.departmentComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.departmentComboBox, 3, 2, 1, 1)

        self.replaceCheckBox = QCheckBox(self.formLayoutWidget)
        self.replaceCheckBox.setObjectName("replaceCheckBox")

        self.gridLayout.addWidget(self.replaceCheckBox, 6, 3, 1, 3)

        self.inventoryLabel = QLabel(self.formLayoutWidget)
        self.inventoryLabel.setObjectName("inventoryLabel")
        self.inventoryLabel.setEnabled(False)

        self.gridLayout.addWidget(self.inventoryLabel, 5, 3, 1, 1)

        self.activeCheckBox = QCheckBox(self.formLayoutWidget)
        self.activeCheckBox.setObjectName("activeCheckBox")

        self.gridLayout.addWidget(self.activeCheckBox, 6, 2, 1, 1)

        self.lastUpdateLabel = QLabel(self.formLayoutWidget)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 7, 0, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 7, 2, 1, 4)

        self.pinLineEdit = QLineEdit(self.formLayoutWidget)
        self.pinLineEdit.setObjectName("pinLineEdit")
        self.pinLineEdit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.pinLineEdit, 0, 4, 1, 2)

        self.cardNumberLineEdit = QLineEdit(self.formLayoutWidget)
        self.cardNumberLineEdit.setObjectName("cardNumberLineEdit")

        self.gridLayout.addWidget(self.cardNumberLineEdit, 1, 4, 1, 2)

        self.placeComboBox = QComboBox(self.formLayoutWidget)
        self.placeComboBox.setObjectName("placeComboBox")
        self.placeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.placeComboBox, 3, 4, 1, 2)

        self.deviceTypeComboBox = QComboBox(self.formLayoutWidget)
        self.deviceTypeComboBox.setObjectName("deviceTypeComboBox")
        self.deviceTypeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceTypeComboBox, 4, 4, 1, 2)

        self.inventoryComboBox = QComboBox(self.formLayoutWidget)
        self.inventoryComboBox.setObjectName("inventoryComboBox")
        self.inventoryComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.inventoryComboBox, 5, 4, 1, 2)

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
        self.departmentLabel.setBuddy(self.departmentComboBox)
        self.placeLabel.setBuddy(self.placeComboBox)
        self.pinLabel.setBuddy(self.pinLineEdit)
        self.numberLabel.setBuddy(self.numberLineEdit)
        self.employeeLabel.setBuddy(self.employeeComboBox)
        self.manufacturerLabel.setBuddy(self.manufacturerComboBox)
        self.serialNumberLabel.setBuddy(self.serialNumberLineEdit)
        self.deviceTypeLabel.setBuddy(self.deviceTypeComboBox)
        self.cardNumberLabel.setBuddy(self.cardNumberLineEdit)
        self.deviceNameLabel.setBuddy(self.deviceNameComboBox)
        self.inventoryLabel.setBuddy(self.inventoryComboBox)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.numberLineEdit, self.pinLineEdit)
        QWidget.setTabOrder(self.pinLineEdit, self.serialNumberLineEdit)
        QWidget.setTabOrder(self.serialNumberLineEdit, self.cardNumberLineEdit)
        QWidget.setTabOrder(self.cardNumberLineEdit, self.employeeComboBox)
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

        self.retranslateUi(MobileInputArea)

        QMetaObject.connectSlotsByName(MobileInputArea)

    # setupUi

    def retranslateUi(self, MobileInputArea):
        MobileInputArea.setWindowTitle(
            QCoreApplication.translate("MobileInputArea", "Mobil Telefon", None)
        )
        # if QT_CONFIG(accessibility)
        MobileInputArea.setAccessibleName(
            QCoreApplication.translate("MobileInputArea", "MobileInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        MobileInputArea.setTitle(
            QCoreApplication.translate("MobileInputArea", "Mobil Telefon", None)
        )
        self.headerLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Mobil Telefon", None)
        )
        self.departmentLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Abteilung", None)
        )
        self.placeLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Platz", None)
        )
        self.pinLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Pin", None)
        )
        self.numberLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Nummer", None)
        )
        self.employeeLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Mitarbeiter*in", None)
        )
        self.manufacturerLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Hersteller", None)
        )
        self.serialNumberLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Seriennummer", None)
        )
        self.deviceTypeLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Ger\u00e4tetyp", None)
        )
        self.cardNumberLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Karten Nummer", None)
        )
        self.deviceNameLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Ger\u00e4tename", None)
        )
        self.replaceCheckBox.setText(
            QCoreApplication.translate("MobileInputArea", "ersetzen", None)
        )
        self.inventoryLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Inventar", None)
        )
        self.activeCheckBox.setText(
            QCoreApplication.translate("MobileInputArea", "Aktiv", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate("MobileInputArea", "Letzte \u00c4nderung", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("MobileInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("MobileInputArea", "Bearbeiten", None)
        )

    # retranslateUi
