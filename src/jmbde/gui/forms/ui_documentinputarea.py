# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'documentinputarea.ui'
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


class Ui_DocumentInputArea(object):
    def setupUi(self, DocumentInputArea):
        if not DocumentInputArea.objectName():
            DocumentInputArea.setObjectName("DocumentInputArea")
        DocumentInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(DocumentInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(DocumentInputArea)
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

        self.documentLabel = QLabel(self.GroupBox)
        self.documentLabel.setObjectName("documentLabel")
        self.documentLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.documentLabel)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lastUpdateLineEdit)

        self.documentAddPushButton = QPushButton(self.GroupBox)
        self.documentAddPushButton.setObjectName("documentAddPushButton")
        self.documentAddPushButton.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.documentAddPushButton)

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
        self.documentLabel.setBuddy(self.documentAddPushButton)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameLineEdit, self.documentAddPushButton)
        QWidget.setTabOrder(self.documentAddPushButton, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(DocumentInputArea)

        QMetaObject.connectSlotsByName(DocumentInputArea)

    # setupUi

    def retranslateUi(self, DocumentInputArea):
        DocumentInputArea.setWindowTitle(
            QCoreApplication.translate("DocumentInputArea", "Dokument", None)
        )
        # if QT_CONFIG(accessibility)
        DocumentInputArea.setAccessibleName(
            QCoreApplication.translate("DocumentInputArea", "DocumentInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        DocumentInputArea.setTitle(
            QCoreApplication.translate("DocumentInputArea", "Dokument", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("DocumentInputArea", "Dokument", None)
        )
        self.nameLabel.setText(
            QCoreApplication.translate("DocumentInputArea", "Name", None)
        )
        self.documentLabel.setText(
            QCoreApplication.translate("DocumentInputArea", "Dokument", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "DocumentInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.documentAddPushButton.setText(
            QCoreApplication.translate(
                "DocumentInputArea", "Dokument ausw\u00e4hlen", None
            )
        )
        self.addPushButton.setText(
            QCoreApplication.translate("DocumentInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("DocumentInputArea", "Bearbeiten", None)
        )

    # retranslateUi
