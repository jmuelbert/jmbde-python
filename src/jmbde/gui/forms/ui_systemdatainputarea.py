################################################################################
## Form generated from reading UI file 'systemdatainputarea.ui'
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
from PySide6.QtWidgets import QFormLayout
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


class Ui_SystemDataInputArea:
    def setupUi(self, SystemDataInputArea):
        if not SystemDataInputArea.objectName():
            SystemDataInputArea.setObjectName("SystemDataInputArea")
        SystemDataInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(SystemDataInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(SystemDataInputArea)
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
        self.nameLabel = QLabel(self.GroupBox)
        self.nameLabel.setObjectName("nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.GroupBox)
        self.nameLineEdit.setObjectName("nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.localCheckBox = QCheckBox(self.GroupBox)
        self.localCheckBox.setObjectName("localCheckBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.localCheckBox)

        self.companyLabel = QLabel(self.GroupBox)
        self.companyLabel.setObjectName("companyLabel")
        self.companyLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.companyLabel)

        self.compamyComboBox = QComboBox(self.GroupBox)
        self.compamyComboBox.setObjectName("compamyComboBox")
        self.compamyComboBox.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.compamyComboBox)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lastUpdateLineEdit)

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
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.companyLabel.setBuddy(self.compamyComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameLineEdit, self.localCheckBox)
        QWidget.setTabOrder(self.localCheckBox, self.compamyComboBox)
        QWidget.setTabOrder(self.compamyComboBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(SystemDataInputArea)

        QMetaObject.connectSlotsByName(SystemDataInputArea)

    # setupUi

    def retranslateUi(self, SystemDataInputArea):
        SystemDataInputArea.setWindowTitle(
            QCoreApplication.translate("SystemDataInputArea", "System Daten", None)
        )
        # if QT_CONFIG(accessibility)
        SystemDataInputArea.setAccessibleName(
            QCoreApplication.translate(
                "SystemDataInputArea", "SystemDataInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        SystemDataInputArea.setTitle(
            QCoreApplication.translate("SystemDataInputArea", "System Daten", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("SystemDataInputArea", "System Daten", None)
        )
        self.nameLabel.setText(
            QCoreApplication.translate("SystemDataInputArea", "Name", None)
        )
        self.localCheckBox.setText(
            QCoreApplication.translate("SystemDataInputArea", "Lokal", None)
        )
        self.companyLabel.setText(
            QCoreApplication.translate("SystemDataInputArea", "Firma", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "SystemDataInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.addPushButton.setText(
            QCoreApplication.translate("SystemDataInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("SystemDataInputArea", "Bearbeiten", None)
        )

    # retranslateUi