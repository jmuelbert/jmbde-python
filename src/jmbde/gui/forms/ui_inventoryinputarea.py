################################################################################
## Form generated from reading UI file 'inventoryinputarea.ui'
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
from PySide6.QtWidgets import QFormLayout
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


class Ui_InventoryInputArea:
    def setupUi(self, InventoryInputArea):
        if not InventoryInputArea.objectName():
            InventoryInputArea.setObjectName("InventoryInputArea")
        InventoryInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(InventoryInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(InventoryInputArea)
        self.GroupBox.setObjectName("GroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.GroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QLabel(self.GroupBox)
        self.headerLabel.setObjectName("headerLabel")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.headerLabel)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_Number = QLabel(self.GroupBox)
        self.label_Number.setObjectName("label_Number")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_Number)

        self.numberLineEdit = QLineEdit(self.GroupBox)
        self.numberLineEdit.setObjectName("numberLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.numberLineEdit)

        self.descriptionLabel = QLabel(self.GroupBox)
        self.descriptionLabel.setObjectName("descriptionLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.descriptionLabel)

        self.descriptionTextEdit = QTextEdit(self.GroupBox)
        self.descriptionTextEdit.setObjectName("descriptionTextEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.descriptionTextEdit)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lastUpdateLineEdit)

        self.activCheckBox = QCheckBox(self.GroupBox)
        self.activCheckBox.setObjectName("activCheckBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.activCheckBox)

        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addPushButton = QPushButton(self.GroupBox)
        self.addPushButton.setObjectName("addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.GroupBox)
        self.editFinishPushButton.setObjectName("editFinishPushButton")

        self.horizontalLayout.addWidget(self.editFinishPushButton)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.gridLayout_3.addWidget(self.GroupBox, 0, 0, 1, 1)

        # if QT_CONFIG(shortcut)
        self.label_Number.setBuddy(self.numberLineEdit)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.numberLineEdit, self.descriptionTextEdit)
        QWidget.setTabOrder(self.descriptionTextEdit, self.activCheckBox)
        QWidget.setTabOrder(self.activCheckBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(InventoryInputArea)

        QMetaObject.connectSlotsByName(InventoryInputArea)

    # setupUi

    def retranslateUi(self, InventoryInputArea):
        InventoryInputArea.setWindowTitle(
            QCoreApplication.translate("InventoryInputArea", "Inventar", None)
        )
        # if QT_CONFIG(accessibility)
        InventoryInputArea.setAccessibleName(
            QCoreApplication.translate(
                "InventoryInputArea", "InventoryInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        InventoryInputArea.setTitle(
            QCoreApplication.translate("InventoryInputArea", "Inventar", None)
        )
        self.headerLabel.setText(
            QCoreApplication.translate("InventoryInputArea", "Inventar", None)
        )
        self.label_Number.setText(
            QCoreApplication.translate("InventoryInputArea", "Nummer", None)
        )
        self.descriptionLabel.setText(
            QCoreApplication.translate("InventoryInputArea", "Text", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "InventoryInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.activCheckBox.setText(
            QCoreApplication.translate("InventoryInputArea", "Aktiv", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("InventoryInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("InventoryInputArea", "Bearbeiten", None)
        )

    # retranslateUi
