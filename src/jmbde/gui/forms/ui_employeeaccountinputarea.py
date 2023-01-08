# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employeeaccountinputarea.ui'
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


class Ui_EmployeeAccountInputArea(object):
    def setupUi(self, EmployeeAccountInputArea):
        if not EmployeeAccountInputArea.objectName():
            EmployeeAccountInputArea.setObjectName("EmployeeAccountInputArea")
        EmployeeAccountInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(EmployeeAccountInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(EmployeeAccountInputArea)
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

        self.employeeComboBox = QComboBox(self.GroupBox)
        self.employeeComboBox.setObjectName("employeeComboBox")
        self.employeeComboBox.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.employeeComboBox)

        self.accountLabel = QLabel(self.GroupBox)
        self.accountLabel.setObjectName("accountLabel")
        self.accountLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.accountLabel)

        self.accountComboBox = QComboBox(self.GroupBox)
        self.accountComboBox.setObjectName("accountComboBox")
        self.accountComboBox.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.accountComboBox)

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
        self.employeeIdLabel.setBuddy(self.employeeComboBox)
        self.accountLabel.setBuddy(self.accountComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.employeeComboBox, self.accountComboBox)
        QWidget.setTabOrder(self.accountComboBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(EmployeeAccountInputArea)

        QMetaObject.connectSlotsByName(EmployeeAccountInputArea)

    # setupUi

    def retranslateUi(self, EmployeeAccountInputArea):
        EmployeeAccountInputArea.setWindowTitle(
            QCoreApplication.translate(
                "EmployeeAccountInputArea", "Mitarbeiter*in Zugang", None
            )
        )
        # if QT_CONFIG(accessibility)
        EmployeeAccountInputArea.setAccessibleName(
            QCoreApplication.translate(
                "EmployeeAccountInputArea", "EmployeeAccountInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        EmployeeAccountInputArea.setTitle(
            QCoreApplication.translate(
                "EmployeeAccountInputArea", "Mitarbeiter*in Zugang", None
            )
        )
        self.label_Header.setText(
            QCoreApplication.translate(
                "EmployeeAccountInputArea", "Mitarbeiter*in Zugang", None
            )
        )
        self.employeeIdLabel.setText(
            QCoreApplication.translate(
                "EmployeeAccountInputArea", "Mitarbeiter*in", None
            )
        )
        self.accountLabel.setText(
            QCoreApplication.translate("EmployeeAccountInputArea", "Zugang", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "EmployeeAccountInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.addPushButton.setText(
            QCoreApplication.translate("EmployeeAccountInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("EmployeeAccountInputArea", "Bearbeiten", None)
        )

    # retranslateUi
