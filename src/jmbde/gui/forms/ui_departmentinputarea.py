# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'departmentinputarea.ui'
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
    QSlider,
    QSpacerItem,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Ui_DepartmentInputArea(object):
    def setupUi(self, DepartmentInputArea):
        if not DepartmentInputArea.objectName():
            DepartmentInputArea.setObjectName("DepartmentInputArea")
        DepartmentInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(DepartmentInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(DepartmentInputArea)
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

        self.priorityLabel = QLabel(self.GroupBox)
        self.priorityLabel.setObjectName("priorityLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.priorityLabel)

        self.printerLabel = QLabel(self.GroupBox)
        self.printerLabel.setObjectName("printerLabel")
        self.printerLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.printerLabel)

        self.printerComboBox = QComboBox(self.GroupBox)
        self.printerComboBox.setObjectName("printerComboBox")
        self.printerComboBox.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.printerComboBox)

        self.faxLabel = QLabel(self.GroupBox)
        self.faxLabel.setObjectName("faxLabel")
        self.faxLabel.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.faxLabel)

        self.faxComboBox = QComboBox(self.GroupBox)
        self.faxComboBox.setObjectName("faxComboBox")
        self.faxComboBox.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.faxComboBox)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lastUpdateLabel)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lastUpdateLineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prioritySpinBox = QSpinBox(self.GroupBox)
        self.prioritySpinBox.setObjectName("prioritySpinBox")

        self.horizontalLayout_2.addWidget(self.prioritySpinBox)

        self.priorityHorizontalSlider = QSlider(self.GroupBox)
        self.priorityHorizontalSlider.setObjectName("priorityHorizontalSlider")
        self.priorityHorizontalSlider.setMinimum(1)
        self.priorityHorizontalSlider.setMaximum(100)
        self.priorityHorizontalSlider.setValue(1)
        self.priorityHorizontalSlider.setSliderPosition(1)
        self.priorityHorizontalSlider.setOrientation(Qt.Horizontal)
        self.priorityHorizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.priorityHorizontalSlider.setTickInterval(5)

        self.horizontalLayout_2.addWidget(self.priorityHorizontalSlider)

        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

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
        self.priorityLabel.setBuddy(self.priorityHorizontalSlider)
        self.printerLabel.setBuddy(self.printerComboBox)
        self.faxLabel.setBuddy(self.faxComboBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameLineEdit, self.prioritySpinBox)
        QWidget.setTabOrder(self.prioritySpinBox, self.priorityHorizontalSlider)
        QWidget.setTabOrder(self.priorityHorizontalSlider, self.printerComboBox)
        QWidget.setTabOrder(self.printerComboBox, self.faxComboBox)
        QWidget.setTabOrder(self.faxComboBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(DepartmentInputArea)

        QMetaObject.connectSlotsByName(DepartmentInputArea)

    # setupUi

    def retranslateUi(self, DepartmentInputArea):
        DepartmentInputArea.setWindowTitle(
            QCoreApplication.translate("DepartmentInputArea", "Abteilung", None)
        )
        # if QT_CONFIG(accessibility)
        DepartmentInputArea.setAccessibleName(
            QCoreApplication.translate(
                "DepartmentInputArea", "DepartmentInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        DepartmentInputArea.setTitle(
            QCoreApplication.translate("DepartmentInputArea", "Abteilung", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("DepartmentInputArea", "Abteilung", None)
        )
        self.nameLabel.setText(
            QCoreApplication.translate("DepartmentInputArea", "Name", None)
        )
        self.priorityLabel.setText(
            QCoreApplication.translate("DepartmentInputArea", "Priorit\u00e4t", None)
        )
        self.printerLabel.setText(
            QCoreApplication.translate("DepartmentInputArea", "Drucker", None)
        )
        self.faxLabel.setText(
            QCoreApplication.translate("DepartmentInputArea", "Fax", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "DepartmentInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.addPushButton.setText(
            QCoreApplication.translate("DepartmentInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("DepartmentInputArea", "Bearbeiten", None)
        )

    # retranslateUi
