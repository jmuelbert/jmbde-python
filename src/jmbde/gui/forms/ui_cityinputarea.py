################################################################################
## Form generated from reading UI file 'cityinputarea.ui'
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


class Ui_CityInputArea:
    def setupUi(self, CityInputArea):
        if not CityInputArea.objectName():
            CityInputArea.setObjectName("CityInputArea")
        CityInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(CityInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.GroupBox = QWidget(CityInputArea)
        self.GroupBox.setObjectName("GroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.GroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cityNameLabel = QLabel(self.GroupBox)
        self.cityNameLabel.setObjectName("cityNameLabel")

        self.gridLayout.addWidget(self.cityNameLabel, 1, 0, 1, 1)

        self.cityNameLineEdit = QLineEdit(self.GroupBox)
        self.cityNameLineEdit.setObjectName("cityNameLineEdit")

        self.gridLayout.addWidget(self.cityNameLineEdit, 1, 1, 1, 1)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 2, 0, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 2, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

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

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addWidget(self.GroupBox)

        # if QT_CONFIG(shortcut)
        self.cityNameLabel.setBuddy(self.cityNameLineEdit)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.cityNameLineEdit, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(CityInputArea)

        QMetaObject.connectSlotsByName(CityInputArea)

    # setupUi

    def retranslateUi(self, CityInputArea):
        CityInputArea.setWindowTitle(
            QCoreApplication.translate("CityInputArea", "Ort", None)
        )
        # if QT_CONFIG(accessibility)
        CityInputArea.setAccessibleName(
            QCoreApplication.translate("CityInputArea", "CityInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        CityInputArea.setTitle(QCoreApplication.translate("CityInputArea", "Ort", None))
        self.label_Header.setText(
            QCoreApplication.translate("CityInputArea", "Ort", None)
        )
        self.cityNameLabel.setText(
            QCoreApplication.translate("CityInputArea", "Ort/Name", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate("CityInputArea", "Letzte \u00c4nderung", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("CityInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("CityInputArea", "Bearbeiten", None)
        )

    # retranslateUi
