# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventoryinputarea.ui'
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
    QCheckBox,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Ui_InventoryInputArea(object):
    def setupUi(self, InventoryInputArea):
        if not InventoryInputArea.objectName():
            InventoryInputArea.setObjectName(u"InventoryInputArea")
        InventoryInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(InventoryInputArea)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.GroupBox = QWidget(InventoryInputArea)
        self.GroupBox.setObjectName(u"GroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.GroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerLabel = QLabel(self.GroupBox)
        self.headerLabel.setObjectName(u"headerLabel")
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
        self.formLayout.setObjectName(u"formLayout")
        self.label_Number = QLabel(self.GroupBox)
        self.label_Number.setObjectName(u"label_Number")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_Number)

        self.numberLineEdit = QLineEdit(self.GroupBox)
        self.numberLineEdit.setObjectName(u"numberLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.numberLineEdit)

        self.descriptionLabel = QLabel(self.GroupBox)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.descriptionLabel)

        self.descriptionTextEdit = QTextEdit(self.GroupBox)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.descriptionTextEdit)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lastUpdateLineEdit)

        self.activCheckBox = QCheckBox(self.GroupBox)
        self.activCheckBox.setObjectName(u"activCheckBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.activCheckBox)

        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addPushButton = QPushButton(self.GroupBox)
        self.addPushButton.setObjectName(u"addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.GroupBox)
        self.editFinishPushButton.setObjectName(u"editFinishPushButton")

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
            QCoreApplication.translate("InventoryInputArea", u"Inventar", None)
        )
        # if QT_CONFIG(accessibility)
        InventoryInputArea.setAccessibleName(
            QCoreApplication.translate(
                "InventoryInputArea", u"InventoryInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        InventoryInputArea.setTitle(
            QCoreApplication.translate("InventoryInputArea", u"Inventar", None)
        )
        self.headerLabel.setText(
            QCoreApplication.translate("InventoryInputArea", u"Inventar", None)
        )
        self.label_Number.setText(
            QCoreApplication.translate("InventoryInputArea", u"Nummer", None)
        )
        self.descriptionLabel.setText(
            QCoreApplication.translate("InventoryInputArea", u"Text", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "InventoryInputArea", u"Letzte \u00c4nderung", None
            )
        )
        self.activCheckBox.setText(
            QCoreApplication.translate("InventoryInputArea", u"Aktiv", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("InventoryInputArea", u"+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("InventoryInputArea", u"Bearbeiten", None)
        )

    # retranslateUi