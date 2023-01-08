# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'functioninputarea.ui'
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


class Ui_FunctionInputArea(object):
    def setupUi(self, FunctionInputArea):
        if not FunctionInputArea.objectName():
            FunctionInputArea.setObjectName("FunctionInputArea")
        FunctionInputArea.resize(730, 600)
        self.gridLayout_3 = QGridLayout(FunctionInputArea)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupBox = QWidget(FunctionInputArea)
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

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.priorityHorizontalSlider = QSlider(self.GroupBox)
        self.priorityHorizontalSlider.setObjectName("priorityHorizontalSlider")
        self.priorityHorizontalSlider.setMaximum(100)
        self.priorityHorizontalSlider.setOrientation(Qt.Horizontal)
        self.priorityHorizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.priorityHorizontalSlider.setTickInterval(5)

        self.gridLayout.addWidget(self.priorityHorizontalSlider, 1, 2, 1, 1)

        self.lastUpdateLabel = QLabel(self.GroupBox)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 2, 0, 1, 1)

        self.nameLabel = QLabel(self.GroupBox)
        self.nameLabel.setObjectName("nameLabel")

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.priorityLabel = QLabel(self.GroupBox)
        self.priorityLabel.setObjectName("priorityLabel")

        self.gridLayout.addWidget(self.priorityLabel, 1, 0, 1, 1)

        self.prioritySpinBox = QSpinBox(self.GroupBox)
        self.prioritySpinBox.setObjectName("prioritySpinBox")

        self.gridLayout.addWidget(self.prioritySpinBox, 1, 1, 1, 1)

        self.nameLineEdit = QLineEdit(self.GroupBox)
        self.nameLineEdit.setObjectName("nameLineEdit")

        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 3)

        self.lastUpdateLineEdit = QLineEdit(self.GroupBox)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 2, 1, 1, 3)

        self.verticalLayout_3.addLayout(self.gridLayout)

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
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.priorityLabel.setBuddy(self.priorityHorizontalSlider)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameLineEdit, self.prioritySpinBox)
        QWidget.setTabOrder(self.prioritySpinBox, self.priorityHorizontalSlider)
        QWidget.setTabOrder(self.priorityHorizontalSlider, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(FunctionInputArea)

        QMetaObject.connectSlotsByName(FunctionInputArea)

    # setupUi

    def retranslateUi(self, FunctionInputArea):
        FunctionInputArea.setWindowTitle(
            QCoreApplication.translate("FunctionInputArea", "Funktion", None)
        )
        # if QT_CONFIG(accessibility)
        FunctionInputArea.setAccessibleName(
            QCoreApplication.translate("FunctionInputArea", "FunctionInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        FunctionInputArea.setTitle(
            QCoreApplication.translate("FunctionInputArea", "Funktion", None)
        )
        self.headerLabel.setText(
            QCoreApplication.translate("FunctionInputArea", "Funktion", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "FunctionInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.nameLabel.setText(
            QCoreApplication.translate("FunctionInputArea", "Name", None)
        )
        self.priorityLabel.setText(
            QCoreApplication.translate("FunctionInputArea", "Priorit\u00e4t", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("FunctionInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("FunctionInputArea", "Bearbeiten", None)
        )

    # retranslateUi
