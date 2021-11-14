################################################################################
## Form generated from reading UI file 'printerinputarea.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QDate
from PySide6.QtCore import QDateTime
from PySide6.QtCore import QLocale
from PySide6.QtCore import QMetaObject
from PySide6.QtCore import QObject
from PySide6.QtCore import QPoint
from PySide6.QtCore import QRect
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtCore import QTime
from PySide6.QtCore import QUrl
from PySide6.QtGui import QBrush
from PySide6.QtGui import QColor
from PySide6.QtGui import QConicalGradient
from PySide6.QtGui import QCursor
from PySide6.QtGui import QFont
from PySide6.QtGui import QFontDatabase
from PySide6.QtGui import QGradient
from PySide6.QtGui import QIcon
from PySide6.QtGui import QImage
from PySide6.QtGui import QKeySequence
from PySide6.QtGui import QLinearGradient
from PySide6.QtGui import QPainter
from PySide6.QtGui import QPalette
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QRadialGradient
from PySide6.QtGui import QTransform
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QCheckBox
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QGroupBox
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QTextEdit
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class Ui_PrinterInputArea:
    def setupUi(self, PrinterInputArea):
        if not PrinterInputArea.objectName():
            PrinterInputArea.setObjectName("PrinterInputArea")
        PrinterInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(PrinterInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayoutWidget = QWidget(PrinterInputArea)
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
        self.resourcesTextEdit = QTextEdit(self.formLayoutWidget)
        self.resourcesTextEdit.setObjectName("resourcesTextEdit")
        self.resourcesTextEdit.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.resourcesTextEdit, 3, 2, 1, 1)

        self.deviceTypeComboBox = QComboBox(self.formLayoutWidget)
        self.deviceTypeComboBox.setObjectName("deviceTypeComboBox")
        self.deviceTypeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceTypeComboBox, 7, 4, 1, 1)

        self.activeCheckBox = QCheckBox(self.formLayoutWidget)
        self.activeCheckBox.setObjectName("activeCheckBox")

        self.gridLayout.addWidget(self.activeCheckBox, 9, 0, 1, 1)

        self.manufacturerLabel = QLabel(self.formLayoutWidget)
        self.manufacturerLabel.setObjectName("manufacturerLabel")

        self.gridLayout.addWidget(self.manufacturerLabel, 8, 0, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 10, 2, 1, 3)

        self.papersizeComboBox = QComboBox(self.formLayoutWidget)
        self.papersizeComboBox.setObjectName("papersizeComboBox")
        self.papersizeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.papersizeComboBox, 3, 4, 1, 1)

        self.employeeComboBox = QComboBox(self.formLayoutWidget)
        self.employeeComboBox.setObjectName("employeeComboBox")
        self.employeeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.employeeComboBox, 5, 2, 1, 1)

        self.computerLabel = QLabel(self.formLayoutWidget)
        self.computerLabel.setObjectName("computerLabel")

        self.gridLayout.addWidget(self.computerLabel, 5, 3, 1, 1)

        self.resourcesLabel = QLabel(self.formLayoutWidget)
        self.resourcesLabel.setObjectName("resourcesLabel")

        self.gridLayout.addWidget(self.resourcesLabel, 3, 0, 1, 1)

        self.replaceCheckBox = QCheckBox(self.formLayoutWidget)
        self.replaceCheckBox.setObjectName("replaceCheckBox")

        self.gridLayout.addWidget(self.replaceCheckBox, 9, 3, 1, 1)

        self.inventoryComboBox = QComboBox(self.formLayoutWidget)
        self.inventoryComboBox.setObjectName("inventoryComboBox")
        self.inventoryComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.inventoryComboBox, 8, 4, 1, 1)

        self.colorCheckBox = QCheckBox(self.formLayoutWidget)
        self.colorCheckBox.setObjectName("colorCheckBox")

        self.gridLayout.addWidget(self.colorCheckBox, 4, 0, 1, 1)

        self.networkLabel = QLabel(self.formLayoutWidget)
        self.networkLabel.setObjectName("networkLabel")

        self.gridLayout.addWidget(self.networkLabel, 1, 0, 1, 1)

        self.serialNumberLineEdit = QLineEdit(self.formLayoutWidget)
        self.serialNumberLineEdit.setObjectName("serialNumberLineEdit")

        self.gridLayout.addWidget(self.serialNumberLineEdit, 0, 4, 1, 1)

        self.departmentLabel = QLabel(self.formLayoutWidget)
        self.departmentLabel.setObjectName("departmentLabel")

        self.gridLayout.addWidget(self.departmentLabel, 6, 0, 1, 1)

        self.lastUpdateLabel = QLabel(self.formLayoutWidget)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")

        self.gridLayout.addWidget(self.lastUpdateLabel, 10, 0, 1, 1)

        self.networkLineEdit = QLineEdit(self.formLayoutWidget)
        self.networkLineEdit.setObjectName("networkLineEdit")

        self.gridLayout.addWidget(self.networkLineEdit, 1, 2, 1, 1)

        self.deviceNameLabel = QLabel(self.formLayoutWidget)
        self.deviceNameLabel.setObjectName("deviceNameLabel")

        self.gridLayout.addWidget(self.deviceNameLabel, 7, 0, 1, 1)

        self.inventoryLabel = QLabel(self.formLayoutWidget)
        self.inventoryLabel.setObjectName("inventoryLabel")

        self.gridLayout.addWidget(self.inventoryLabel, 8, 3, 1, 1)

        self.employeeLabel = QLabel(self.formLayoutWidget)
        self.employeeLabel.setObjectName("employeeLabel")

        self.gridLayout.addWidget(self.employeeLabel, 5, 0, 1, 1)

        self.paperSizeLabel = QLabel(self.formLayoutWidget)
        self.paperSizeLabel.setObjectName("paperSizeLabel")

        self.gridLayout.addWidget(self.paperSizeLabel, 3, 3, 1, 1)

        self.manufacturerComboBox = QComboBox(self.formLayoutWidget)
        self.manufacturerComboBox.setObjectName("manufacturerComboBox")
        self.manufacturerComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.manufacturerComboBox, 8, 2, 1, 1)

        self.placeLabel = QLabel(self.formLayoutWidget)
        self.placeLabel.setObjectName("placeLabel")

        self.gridLayout.addWidget(self.placeLabel, 6, 3, 1, 1)

        self.deviceNameComboBox = QComboBox(self.formLayoutWidget)
        self.deviceNameComboBox.setObjectName("deviceNameComboBox")
        self.deviceNameComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceNameComboBox, 7, 2, 1, 1)

        self.computerComboBox = QComboBox(self.formLayoutWidget)
        self.computerComboBox.setObjectName("computerComboBox")
        self.computerComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.computerComboBox, 5, 4, 1, 1)

        self.serialNumberLabel = QLabel(self.formLayoutWidget)
        self.serialNumberLabel.setObjectName("serialNumberLabel")

        self.gridLayout.addWidget(self.serialNumberLabel, 0, 3, 1, 1)

        self.departmentComboBox = QComboBox(self.formLayoutWidget)
        self.departmentComboBox.setObjectName("departmentComboBox")
        self.departmentComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.departmentComboBox, 6, 2, 1, 1)

        self.placeComboBox = QComboBox(self.formLayoutWidget)
        self.placeComboBox.setObjectName("placeComboBox")
        self.placeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.placeComboBox, 6, 4, 1, 1)

        self.deviceTypeLabel = QLabel(self.formLayoutWidget)
        self.deviceTypeLabel.setObjectName("deviceTypeLabel")

        self.gridLayout.addWidget(self.deviceTypeLabel, 7, 3, 1, 1)

        self.networkNameLabel = QLabel(self.formLayoutWidget)
        self.networkNameLabel.setObjectName("networkNameLabel")

        self.gridLayout.addWidget(self.networkNameLabel, 0, 0, 1, 1)

        self.networkNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.networkNameLineEdit.setObjectName("networkNameLineEdit")

        self.gridLayout.addWidget(self.networkNameLineEdit, 0, 2, 1, 1)

        self.ipAddressLabel = QLabel(self.formLayoutWidget)
        self.ipAddressLabel.setObjectName("ipAddressLabel")

        self.gridLayout.addWidget(self.ipAddressLabel, 1, 3, 1, 1)

        self.ipAddressLineEdit = QLineEdit(self.formLayoutWidget)
        self.ipAddressLineEdit.setObjectName("ipAddressLineEdit")

        self.gridLayout.addWidget(self.ipAddressLineEdit, 1, 4, 1, 1)

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
        # endif // QT_CONFIG(shortcut)
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
        PrinterInputArea.setWindowTitle(
            QCoreApplication.translate("PrinterInputArea", "Drucker", None)
        )
        # if QT_CONFIG(accessibility)
        PrinterInputArea.setAccessibleName(
            QCoreApplication.translate("PrinterInputArea", "PrinterInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        PrinterInputArea.setTitle(
            QCoreApplication.translate("PrinterInputArea", "Drucker", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("PrinterInputArea", "Drucker", None)
        )
        self.activeCheckBox.setText(
            QCoreApplication.translate("PrinterInputArea", "Aktiv", None)
        )
        self.manufacturerLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Hersteller", None)
        )
        self.computerLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Computer", None)
        )
        self.resourcesLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Verbrauchsmaterial", None)
        )
        self.replaceCheckBox.setText(
            QCoreApplication.translate("PrinterInputArea", "ersetzen", None)
        )
        self.colorCheckBox.setText(
            QCoreApplication.translate("PrinterInputArea", "Farbe", None)
        )
        self.networkLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Netzwerk", None)
        )
        self.departmentLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Abteilung", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Lezte \u00c4nderung", None)
        )
        self.deviceNameLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Ger\u00e4tename", None)
        )
        self.inventoryLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Inventar", None)
        )
        self.employeeLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Mitarbeiter*in", None)
        )
        self.paperSizeLabel.setText(
            QCoreApplication.translate(
                "PrinterInputArea", "Papiergr\u00f6\u00dfe", None
            )
        )
        self.placeLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Platz", None)
        )
        self.serialNumberLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Seriennummer", None)
        )
        self.deviceTypeLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Ger\u00e4tetyp", None)
        )
        self.networkNameLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "Netzwerk Name", None)
        )
        self.ipAddressLabel.setText(
            QCoreApplication.translate("PrinterInputArea", "IP Adresse", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("PrinterInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("PrinterInputArea", "Bearbeiten", None)
        )

    # retranslateUi
