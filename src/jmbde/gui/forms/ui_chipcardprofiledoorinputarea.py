# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chipcardprofiledoorinputarea.ui'
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
    QComboBox,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListView,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_ChipCardProfileDoorInputArea(object):
    def setupUi(self, ChipCardProfileDoorInputArea):
        if not ChipCardProfileDoorInputArea.objectName():
            ChipCardProfileDoorInputArea.setObjectName("ChipCardProfileDoorInputArea")
        ChipCardProfileDoorInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(ChipCardProfileDoorInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(ChipCardProfileDoorInputArea)
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
        self.profileDoorLabel = QLabel(self.GroupBox)
        self.profileDoorLabel.setObjectName("profileDoorLabel")
        self.profileDoorLabel.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.profileDoorLabel)

        self.profileLabel = QLabel(self.GroupBox)
        self.profileLabel.setObjectName("profileLabel")
        self.profileLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.profileLabel)

        self.profileComboBox = QComboBox(self.GroupBox)
        self.profileComboBox.setObjectName("profileComboBox")
        self.profileComboBox.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.profileComboBox)

        self.doorLabel = QLabel(self.GroupBox)
        self.doorLabel.setObjectName("doorLabel")
        self.doorLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.doorLabel)

        self.doorComboBox = QComboBox(self.GroupBox)
        self.doorComboBox.setObjectName("doorComboBox")
        self.doorComboBox.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.doorComboBox)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.profileDoorListView = QListView(self.GroupBox)
        self.profileDoorListView.setObjectName("profileDoorListView")
        self.profileDoorListView.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.profileDoorListView)

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
        self.profileDoorLabel.setBuddy(self.profileDoorListView)
        self.profileLabel.setBuddy(self.profileComboBox)
        self.doorLabel.setBuddy(self.doorComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.profileDoorListView, self.profileComboBox)
        QWidget.setTabOrder(self.profileComboBox, self.doorComboBox)
        QWidget.setTabOrder(self.doorComboBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(ChipCardProfileDoorInputArea)

        QMetaObject.connectSlotsByName(ChipCardProfileDoorInputArea)

    # setupUi

    def retranslateUi(self, ChipCardProfileDoorInputArea):
        ChipCardProfileDoorInputArea.setWindowTitle(
            QCoreApplication.translate(
                "ChipCardProfileDoorInputArea",
                "Schl\u00fcsselchip Profil T\u00fcr",
                None,
            )
        )
        # if QT_CONFIG(accessibility)
        ChipCardProfileDoorInputArea.setAccessibleName(
            QCoreApplication.translate(
                "ChipCardProfileDoorInputArea", "ChipCardProfileInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        ChipCardProfileDoorInputArea.setTitle(
            QCoreApplication.translate(
                "ChipCardProfileDoorInputArea",
                "Schl\u00fcsselchip Profil T\u00fcr",
                None,
            )
        )
        self.label_Header.setText(
            QCoreApplication.translate(
                "ChipCardProfileDoorInputArea",
                "Schl\u00fcsselchip Profil T\u00fcr",
                None,
            )
        )
        self.profileDoorLabel.setText(
            QCoreApplication.translate(
                "ChipCardProfileDoorInputArea", "Profil T\u00fcr", None
            )
        )
        self.profileLabel.setText(
            QCoreApplication.translate("ChipCardProfileDoorInputArea", "Profil", None)
        )
        self.doorLabel.setText(
            QCoreApplication.translate("ChipCardProfileDoorInputArea", "T\u00fcr", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "ChipCardProfileDoorInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.addPushButton.setText(
            QCoreApplication.translate("ChipCardProfileDoorInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate(
                "ChipCardProfileDoorInputArea", "Bearbeiten", None
            )
        )

    # retranslateUi
