################################################################################
## Form generated from reading UI file 'softwareinputarea.ui'
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


class Ui_SoftwareInputArea:
    def setupUi(self, SoftwareInputArea):
        if not SoftwareInputArea.objectName():
            SoftwareInputArea.setObjectName("SoftwareInputArea")
        SoftwareInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(SoftwareInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollAreaWidgetContents = QWidget(SoftwareInputArea)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QLabel(self.scrollAreaWidgetContents)
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
        self.versionLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.versionLineEdit.setObjectName("versionLineEdit")

        self.gridLayout.addWidget(self.versionLineEdit, 1, 1, 1, 1)

        self.nameLabel = QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setObjectName("nameLabel")

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.revisionLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.revisionLineEdit.setObjectName("revisionLineEdit")

        self.gridLayout.addWidget(self.revisionLineEdit, 2, 1, 1, 1)

        self.versionLabel = QLabel(self.scrollAreaWidgetContents)
        self.versionLabel.setObjectName("versionLabel")

        self.gridLayout.addWidget(self.versionLabel, 1, 0, 1, 1)

        self.nameLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.nameLineEdit.setObjectName("nameLineEdit")

        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)

        self.fixLabel = QLabel(self.scrollAreaWidgetContents)
        self.fixLabel.setObjectName("fixLabel")

        self.gridLayout.addWidget(self.fixLabel, 3, 0, 1, 1)

        self.fixLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.fixLineEdit.setObjectName("fixLineEdit")

        self.gridLayout.addWidget(self.fixLineEdit, 3, 1, 1, 1)

        self.revisionLabel = QLabel(self.scrollAreaWidgetContents)
        self.revisionLabel.setObjectName("revisionLabel")

        self.gridLayout.addWidget(self.revisionLabel, 2, 0, 1, 1)

        self.lastUpdateLabel = QLabel(self.scrollAreaWidgetContents)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 4, 0, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 4, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.addPushButton.setObjectName("addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.editFinishPushButton.setObjectName("editFinishPushButton")

        self.horizontalLayout.addWidget(self.editFinishPushButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addWidget(self.scrollAreaWidgetContents)

        # if QT_CONFIG(shortcut)
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.versionLabel.setBuddy(self.versionLineEdit)
        self.fixLabel.setBuddy(self.fixLineEdit)
        self.revisionLabel.setBuddy(self.revisionLineEdit)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameLineEdit, self.versionLineEdit)
        QWidget.setTabOrder(self.versionLineEdit, self.revisionLineEdit)
        QWidget.setTabOrder(self.revisionLineEdit, self.fixLineEdit)
        QWidget.setTabOrder(self.fixLineEdit, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(SoftwareInputArea)

        QMetaObject.connectSlotsByName(SoftwareInputArea)

    # setupUi

    def retranslateUi(self, SoftwareInputArea):
        SoftwareInputArea.setWindowTitle(
            QCoreApplication.translate("SoftwareInputArea", "Software", None)
        )
        # if QT_CONFIG(accessibility)
        SoftwareInputArea.setAccessibleName(
            QCoreApplication.translate("SoftwareInputArea", "SoftwareInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        SoftwareInputArea.setTitle(
            QCoreApplication.translate("SoftwareInputArea", "Software", None)
        )
        self.headerLabel.setText(
            QCoreApplication.translate("SoftwareInputArea", "Software", None)
        )
        self.nameLabel.setText(
            QCoreApplication.translate("SoftwareInputArea", "Name", None)
        )
        self.versionLabel.setText(
            QCoreApplication.translate("SoftwareInputArea", "Version", None)
        )
        self.fixLabel.setText(
            QCoreApplication.translate("SoftwareInputArea", "Fix", None)
        )
        self.revisionLabel.setText(
            QCoreApplication.translate("SoftwareInputArea", "Revision", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "SoftwareInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.addPushButton.setText(
            QCoreApplication.translate("SoftwareInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("SoftwareInputArea", "Bearbeiten", None)
        )

    # retranslateUi
