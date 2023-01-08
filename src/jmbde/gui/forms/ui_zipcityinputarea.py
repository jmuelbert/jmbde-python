# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zipcityinputarea.ui'
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
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_ZipCityInputArea(object):
    def setupUi(self, ZipCityInputArea):
        if not ZipCityInputArea.objectName():
            ZipCityInputArea.setObjectName("ZipCityInputArea")
        ZipCityInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(ZipCityInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(ZipCityInputArea)
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
        self.zipCodeLabel = QLabel(self.GroupBox)
        self.zipCodeLabel.setObjectName("zipCodeLabel")
        self.zipCodeLabel.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.zipCodeLabel)

        self.zipCodeComboBox = QComboBox(self.GroupBox)
        self.zipCodeComboBox.setObjectName("zipCodeComboBox")
        self.zipCodeComboBox.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.zipCodeComboBox)

        self.cityLabel = QLabel(self.GroupBox)
        self.cityLabel.setObjectName("cityLabel")
        self.cityLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cityLabel)

        self.cityComboBox = QComboBox(self.GroupBox)
        self.cityComboBox.setObjectName("cityComboBox")
        self.cityComboBox.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cityComboBox)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lastUpdateLineEdit)

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
        self.zipCodeLabel.setBuddy(self.zipCodeComboBox)
        self.cityLabel.setBuddy(self.cityComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.zipCodeComboBox, self.cityComboBox)
        QWidget.setTabOrder(self.cityComboBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(ZipCityInputArea)

        QMetaObject.connectSlotsByName(ZipCityInputArea)

    # setupUi

    def retranslateUi(self, ZipCityInputArea):
        ZipCityInputArea.setWindowTitle(
            QCoreApplication.translate("ZipCityInputArea", "PLZ Ort", None)
        )
        # if QT_CONFIG(accessibility)
        ZipCityInputArea.setAccessibleName(
            QCoreApplication.translate("ZipCityInputArea", "ZipCityInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        ZipCityInputArea.setTitle(
            QCoreApplication.translate("ZipCityInputArea", "PLZ Ort", None)
        )
        self.headerLabel.setText(
            QCoreApplication.translate("ZipCityInputArea", "PLZ Ort", None)
        )
        self.zipCodeLabel.setText(
            QCoreApplication.translate("ZipCityInputArea", "PLZ", None)
        )
        self.cityLabel.setText(
            QCoreApplication.translate("ZipCityInputArea", "Ort", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate("ZipCityInputArea", "Letzte \u00c4nderung", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("ZipCityInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("ZipCityInputArea", "Bearbeiten", None)
        )

    # retranslateUi
