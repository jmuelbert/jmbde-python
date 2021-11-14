################################################################################
## Form generated from reading UI file 'titleinputarea.ui'
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
from PySide6.QtWidgets import QDateEdit
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


class Ui_TitleInputArea:
    def setupUi(self, TitleInputArea):
        if not TitleInputArea.objectName():
            TitleInputArea.setObjectName("TitleInputArea")
        TitleInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(TitleInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayoutWidget = QWidget(TitleInputArea)
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

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fromLabel = QLabel(self.formLayoutWidget)
        self.fromLabel.setObjectName("fromLabel")

        self.gridLayout.addWidget(self.fromLabel, 1, 0, 1, 1)

        self.fromDateEdit = QDateEdit(self.formLayoutWidget)
        self.fromDateEdit.setObjectName("fromDateEdit")

        self.gridLayout.addWidget(self.fromDateEdit, 1, 2, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 2, 1, 1, 2)

        self.lastUpdateLabel = QLabel(self.formLayoutWidget)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 2, 0, 1, 1)

        self.titleLabel = QLabel(self.formLayoutWidget)
        self.titleLabel.setObjectName("titleLabel")

        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.titleLineEdit = QLineEdit(self.formLayoutWidget)
        self.titleLineEdit.setObjectName("titleLineEdit")

        self.gridLayout.addWidget(self.titleLineEdit, 0, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

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
        self.fromLabel.setBuddy(self.fromDateEdit)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        self.titleLabel.setBuddy(self.titleLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.titleLineEdit, self.fromDateEdit)
        QWidget.setTabOrder(self.fromDateEdit, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(TitleInputArea)

        QMetaObject.connectSlotsByName(TitleInputArea)

    # setupUi

    def retranslateUi(self, TitleInputArea):
        TitleInputArea.setWindowTitle(
            QCoreApplication.translate("TitleInputArea", "Titel", None)
        )
        # if QT_CONFIG(accessibility)
        TitleInputArea.setAccessibleName(
            QCoreApplication.translate("TitleInputArea", "TitleInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        TitleInputArea.setTitle(
            QCoreApplication.translate("TitleInputArea", "Titel", None)
        )
        self.headerLabel.setText(
            QCoreApplication.translate("TitleInputArea", "Titel", None)
        )
        self.fromLabel.setText(QCoreApplication.translate("TitleInputArea", "ab", None))
        self.lastUpdateLabel.setText(
            QCoreApplication.translate("TitleInputArea", "Letzte \u00c4nderung", None)
        )
        self.titleLabel.setText(
            QCoreApplication.translate("TitleInputArea", "Titel", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("TitleInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("TitleInputArea", "Bearbeiten", None)
        )

    # retranslateUi
