################################################################################
## Form generated from reading UI file 'phoneinputarea.ui'
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
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class Ui_PhoneInputArea:
    def setupUi(self, PhoneInputArea):
        if not PhoneInputArea.objectName():
            PhoneInputArea.setObjectName("PhoneInputArea")
        PhoneInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(PhoneInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayoutWidget = QWidget(PhoneInputArea)
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
        self.deviceNameLabel = QLabel(self.formLayoutWidget)
        self.deviceNameLabel.setObjectName("deviceNameLabel")
        self.deviceNameLabel.setEnabled(False)
        self.deviceNameLabel.setAlignment(
            Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft
        )

        self.gridLayout.addWidget(self.deviceNameLabel, 6, 0, 1, 1)

        self.placeLabel = QLabel(self.formLayoutWidget)
        self.placeLabel.setObjectName("placeLabel")
        self.placeLabel.setEnabled(False)
        self.placeLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

        self.gridLayout.addWidget(self.placeLabel, 4, 2, 1, 1)

        self.pinLineEdit = QLineEdit(self.formLayoutWidget)
        self.pinLineEdit.setObjectName("pinLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pinLineEdit.sizePolicy().hasHeightForWidth())
        self.pinLineEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pinLineEdit, 1, 3, 1, 1)

        self.pinLabel = QLabel(self.formLayoutWidget)
        self.pinLabel.setObjectName("pinLabel")

        self.gridLayout.addWidget(self.pinLabel, 1, 2, 1, 1)

        self.serialNumberLineEdit = QLineEdit(self.formLayoutWidget)
        self.serialNumberLineEdit.setObjectName("serialNumberLineEdit")

        self.gridLayout.addWidget(self.serialNumberLineEdit, 2, 1, 1, 1)

        self.numberLineEdit = QLineEdit(self.formLayoutWidget)
        self.numberLineEdit.setObjectName("numberLineEdit")
        sizePolicy.setHeightForWidth(
            self.numberLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.numberLineEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.numberLineEdit, 1, 1, 1, 1)

        self.manufacturerLabel = QLabel(self.formLayoutWidget)
        self.manufacturerLabel.setObjectName("manufacturerLabel")
        self.manufacturerLabel.setEnabled(False)

        self.gridLayout.addWidget(self.manufacturerLabel, 8, 0, 1, 1)

        self.deviceNameComboBox = QComboBox(self.formLayoutWidget)
        self.deviceNameComboBox.setObjectName("deviceNameComboBox")
        self.deviceNameComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceNameComboBox, 6, 1, 1, 1)

        self.deviceTypeComboBox = QComboBox(self.formLayoutWidget)
        self.deviceTypeComboBox.setObjectName("deviceTypeComboBox")
        self.deviceTypeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.deviceTypeComboBox, 6, 3, 1, 1)

        self.numberLabel = QLabel(self.formLayoutWidget)
        self.numberLabel.setObjectName("numberLabel")

        self.gridLayout.addWidget(self.numberLabel, 1, 0, 1, 1)

        self.inventoryLabel = QLabel(self.formLayoutWidget)
        self.inventoryLabel.setObjectName("inventoryLabel")
        self.inventoryLabel.setEnabled(False)

        self.gridLayout.addWidget(self.inventoryLabel, 8, 2, 1, 1)

        self.deviceTypeLabel = QLabel(self.formLayoutWidget)
        self.deviceTypeLabel.setObjectName("deviceTypeLabel")
        self.deviceTypeLabel.setEnabled(False)
        self.deviceTypeLabel.setAlignment(
            Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft
        )

        self.gridLayout.addWidget(self.deviceTypeLabel, 6, 2, 1, 1)

        self.departmentComboBox = QComboBox(self.formLayoutWidget)
        self.departmentComboBox.setObjectName("departmentComboBox")
        self.departmentComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.departmentComboBox, 4, 1, 1, 1)

        self.placeComboBox = QComboBox(self.formLayoutWidget)
        self.placeComboBox.setObjectName("placeComboBox")
        self.placeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.placeComboBox, 4, 3, 1, 1)

        self.employeeLabel = QLabel(self.formLayoutWidget)
        self.employeeLabel.setObjectName("employeeLabel")
        self.employeeLabel.setEnabled(False)
        self.employeeLabel.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

        self.gridLayout.addWidget(self.employeeLabel, 3, 0, 1, 1)

        self.inventoryComboBox = QComboBox(self.formLayoutWidget)
        self.inventoryComboBox.setObjectName("inventoryComboBox")
        self.inventoryComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.inventoryComboBox, 8, 3, 1, 1)

        self.serialNumberLabel = QLabel(self.formLayoutWidget)
        self.serialNumberLabel.setObjectName("serialNumberLabel")

        self.gridLayout.addWidget(self.serialNumberLabel, 2, 0, 1, 1)

        self.activeCheckBox = QCheckBox(self.formLayoutWidget)
        self.activeCheckBox.setObjectName("activeCheckBox")

        self.gridLayout.addWidget(self.activeCheckBox, 9, 1, 1, 1)

        self.departmentLabel = QLabel(self.formLayoutWidget)
        self.departmentLabel.setObjectName("departmentLabel")
        self.departmentLabel.setEnabled(False)

        self.gridLayout.addWidget(self.departmentLabel, 4, 0, 1, 1)

        self.manufacturerComboBox = QComboBox(self.formLayoutWidget)
        self.manufacturerComboBox.setObjectName("manufacturerComboBox")
        self.manufacturerComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.manufacturerComboBox, 8, 1, 1, 1)

        self.employeeComboBox = QComboBox(self.formLayoutWidget)
        self.employeeComboBox.setObjectName("employeeComboBox")
        self.employeeComboBox.setEnabled(False)

        self.gridLayout.addWidget(self.employeeComboBox, 3, 1, 1, 1)

        self.lastUpdateLabel = QLabel(self.formLayoutWidget)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 10, 0, 1, 1)

        self.replaceCheckBox = QCheckBox(self.formLayoutWidget)
        self.replaceCheckBox.setObjectName("replaceCheckBox")

        self.gridLayout.addWidget(self.replaceCheckBox, 9, 2, 1, 2)

        self.lastUpdateLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 10, 1, 1, 3)

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

        self.retranslateUi(PhoneInputArea)

        QMetaObject.connectSlotsByName(PhoneInputArea)

    # setupUi

    def retranslateUi(self, PhoneInputArea):
        PhoneInputArea.setWindowTitle(
            QCoreApplication.translate("PhoneInputArea", "Telefon", None)
        )
        # if QT_CONFIG(accessibility)
        PhoneInputArea.setAccessibleName(
            QCoreApplication.translate("PhoneInputArea", "PhoneInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        PhoneInputArea.setTitle(
            QCoreApplication.translate("PhoneInputArea", "Telefon", None)
        )
        self.headerLabel.setText(
            QCoreApplication.translate("PhoneInputArea", "Telefon", None)
        )
        self.deviceNameLabel.setText(
            QCoreApplication.translate("PhoneInputArea", "Ger\u00e4tename", None)
        )
        self.placeLabel.setText(
            QCoreApplication.translate("PhoneInputArea", "Platz", None)
        )
        self.pinLabel.setText(QCoreApplication.translate("PhoneInputArea", "Pin", None))
        self.manufacturerLabel.setText(
            QCoreApplication.translate("PhoneInputArea", "Hersteller", None)
        )
        self.numberLabel.setText(
            QCoreApplication.translate("PhoneInputArea", "Nummer", None)
        )
        self.inventoryLabel.setText(
            QCoreApplication.translate("PhoneInputArea", "Inventar", None)
        )
        self.deviceTypeLabel.setText(
            QCoreApplication.translate("PhoneInputArea", "Ger\u00e4tetyp", None)
        )
        self.employeeLabel.setText(
            QCoreApplication.translate("PhoneInputArea", "Mitarbeiter*in", None)
        )
        self.serialNumberLabel.setText(
            QCoreApplication.translate("PhoneInputArea", "Seriennummer", None)
        )
        self.activeCheckBox.setText(
            QCoreApplication.translate("PhoneInputArea", "Aktiv", None)
        )
        self.departmentLabel.setText(
            QCoreApplication.translate("PhoneInputArea", "Abteilung", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate("PhoneInputArea", "Letzte \u00c4nderuung", None)
        )
        self.replaceCheckBox.setText(
            QCoreApplication.translate("PhoneInputArea", "ersetzen", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("PhoneInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("PhoneInputArea", "Bearbeiten", None)
        )

    # retranslateUi
