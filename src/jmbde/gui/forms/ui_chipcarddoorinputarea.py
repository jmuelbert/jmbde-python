################################################################################
## Form generated from reading UI file 'chipcarddoorinputarea.ui'
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
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QFormLayout
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QGroupBox
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QSpacerItem
from PySide6.QtWidgets import QSpinBox
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class Ui_ChipCardDoorInputArea:
    def setupUi(self, ChipCardDoorInputArea):
        if not ChipCardDoorInputArea.objectName():
            ChipCardDoorInputArea.setObjectName("ChipCardDoorInputArea")
        ChipCardDoorInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(ChipCardDoorInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(ChipCardDoorInputArea)
        self.GroupBox.setObjectName("GroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.GroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Header = QLabel(self.GroupBox)
        self.label_Header.setObjectName("label_Header")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_Header.setFont(font)
        self.label_Header.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Header)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.placeLabel = QLabel(self.GroupBox)
        self.placeLabel.setObjectName("placeLabel")
        self.placeLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.placeLabel)

        self.placeComboBox = QComboBox(self.GroupBox)
        self.placeComboBox.setObjectName("placeComboBox")
        self.placeComboBox.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.placeComboBox)

        self.departmentLabel = QLabel(self.GroupBox)
        self.departmentLabel.setObjectName("departmentLabel")
        self.departmentLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.departmentLabel)

        self.departmentComboBox = QComboBox(self.GroupBox)
        self.departmentComboBox.setObjectName("departmentComboBox")
        self.departmentComboBox.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.departmentComboBox)

        self.numberLabel = QLabel(self.GroupBox)
        self.numberLabel.setObjectName("numberLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.numberLabel)

        self.numberSpinBox = QSpinBox(self.GroupBox)
        self.numberSpinBox.setObjectName("numberSpinBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.numberSpinBox)

        self.employeeLabel = QLabel(self.GroupBox)
        self.employeeLabel.setObjectName("employeeLabel")
        self.employeeLabel.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.employeeLabel)

        self.employeeComboBox = QComboBox(self.GroupBox)
        self.employeeComboBox.setObjectName("employeeComboBox")
        self.employeeComboBox.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.employeeComboBox)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lastUpdateLineEdit)

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
        self.placeLabel.setBuddy(self.placeComboBox)
        self.departmentLabel.setBuddy(self.departmentComboBox)
        self.numberLabel.setBuddy(self.numberSpinBox)
        self.employeeLabel.setBuddy(self.employeeComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.numberSpinBox, self.placeComboBox)
        QWidget.setTabOrder(self.placeComboBox, self.departmentComboBox)
        QWidget.setTabOrder(self.departmentComboBox, self.employeeComboBox)
        QWidget.setTabOrder(self.employeeComboBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(ChipCardDoorInputArea)

        QMetaObject.connectSlotsByName(ChipCardDoorInputArea)

    # setupUi

    def retranslateUi(self, ChipCardDoorInputArea):
        ChipCardDoorInputArea.setWindowTitle(
            QCoreApplication.translate(
                "ChipCardDoorInputArea", "Schl\u00fcsselchip T\u00fcr", None
            )
        )
        # if QT_CONFIG(accessibility)
        ChipCardDoorInputArea.setAccessibleName(
            QCoreApplication.translate(
                "ChipCardDoorInputArea", "ChipCardDoorInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        ChipCardDoorInputArea.setTitle(
            QCoreApplication.translate(
                "ChipCardDoorInputArea", "Schl\u00fcsselchip T\u00fcr", None
            )
        )
        self.label_Header.setText(
            QCoreApplication.translate(
                "ChipCardDoorInputArea", "Schl\u00fcsselchip T\u00fcr", None
            )
        )
        self.placeLabel.setText(
            QCoreApplication.translate("ChipCardDoorInputArea", "Ort", None)
        )
        self.departmentLabel.setText(
            QCoreApplication.translate("ChipCardDoorInputArea", "Abteilung", None)
        )
        self.numberLabel.setText(
            QCoreApplication.translate("ChipCardDoorInputArea", "Nummer", None)
        )
        self.employeeLabel.setText(
            QCoreApplication.translate("ChipCardDoorInputArea", "Mitarbeiter*in", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "ChipCardDoorInputArea", "Letze \u00c4nderung", None
            )
        )
        self.addPushButton.setText(
            QCoreApplication.translate("ChipCardDoorInputArea", "+", None)
        )
        # if QT_CONFIG(accessibility)
        self.editFinishPushButton.setAccessibleName(
            QCoreApplication.translate(
                "ChipCardDoorInputArea", "ChipCardDoorDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        self.editFinishPushButton.setText(
            QCoreApplication.translate("ChipCardDoorInputArea", "Bearbeiten", None)
        )

    # retranslateUi
