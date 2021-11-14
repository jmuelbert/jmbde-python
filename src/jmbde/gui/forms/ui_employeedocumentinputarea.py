################################################################################
## Form generated from reading UI file 'employeedocumentinputarea.ui'
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
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class Ui_EmployeeDocumentInputArea:
    def setupUi(self, EmployeeDocumentInputArea):
        if not EmployeeDocumentInputArea.objectName():
            EmployeeDocumentInputArea.setObjectName("EmployeeDocumentInputArea")
        EmployeeDocumentInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(EmployeeDocumentInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(EmployeeDocumentInputArea)
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
        self.employeeIdLabel = QLabel(self.GroupBox)
        self.employeeIdLabel.setObjectName("employeeIdLabel")
        self.employeeIdLabel.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.employeeIdLabel)

        self.documentIdLabel = QLabel(self.GroupBox)
        self.documentIdLabel.setObjectName("documentIdLabel")
        self.documentIdLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.documentIdLabel)

        self.documentIdcomboBox = QComboBox(self.GroupBox)
        self.documentIdcomboBox.setObjectName("documentIdcomboBox")
        self.documentIdcomboBox.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.documentIdcomboBox)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.employeeIdcomboBox = QComboBox(self.GroupBox)
        self.employeeIdcomboBox.setObjectName("employeeIdcomboBox")
        self.employeeIdcomboBox.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.employeeIdcomboBox)

        self.lastUpdatelineEdit = QLineEdit(self.GroupBox)
        self.lastUpdatelineEdit.setObjectName("lastUpdatelineEdit")
        self.lastUpdatelineEdit.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lastUpdatelineEdit)

        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addPushButton = QPushButton(self.GroupBox)
        self.addPushButton.setObjectName("addPushButton")
        self.addPushButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.GroupBox)
        self.editFinishPushButton.setObjectName("editFinishPushButton")
        self.editFinishPushButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.editFinishPushButton)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.gridLayout_3.addWidget(self.GroupBox, 0, 0, 1, 1)

        # if QT_CONFIG(shortcut)
        self.employeeIdLabel.setBuddy(self.employeeIdcomboBox)
        self.documentIdLabel.setBuddy(self.documentIdcomboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdatelineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.employeeIdcomboBox, self.documentIdcomboBox)
        QWidget.setTabOrder(self.documentIdcomboBox, self.lastUpdatelineEdit)
        QWidget.setTabOrder(self.lastUpdatelineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(EmployeeDocumentInputArea)

        QMetaObject.connectSlotsByName(EmployeeDocumentInputArea)

    # setupUi

    def retranslateUi(self, EmployeeDocumentInputArea):
        EmployeeDocumentInputArea.setWindowTitle(
            QCoreApplication.translate(
                "EmployeeDocumentInputArea", "Mitarbeiter*in Dokument", None
            )
        )
        # if QT_CONFIG(accessibility)
        EmployeeDocumentInputArea.setAccessibleName(
            QCoreApplication.translate(
                "EmployeeDocumentInputArea", "EmployeeDocumentInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        EmployeeDocumentInputArea.setTitle(
            QCoreApplication.translate(
                "EmployeeDocumentInputArea", "Mitarbeiter*in Dokument", None
            )
        )
        self.label_Header.setText(
            QCoreApplication.translate(
                "EmployeeDocumentInputArea", "Mitarbeiter*in Dokument", None
            )
        )
        self.employeeIdLabel.setText(
            QCoreApplication.translate(
                "EmployeeDocumentInputArea", "Mitarbeiter*in", None
            )
        )
        self.documentIdLabel.setText(
            QCoreApplication.translate("EmployeeDocumentInputArea", "Dokument", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "EmployeeDocumentInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.addPushButton.setText(
            QCoreApplication.translate("EmployeeDocumentInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("EmployeeDocumentInputArea", "Bearbeiten", None)
        )

    # retranslateUi
