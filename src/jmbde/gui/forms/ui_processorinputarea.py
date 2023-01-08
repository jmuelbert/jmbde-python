# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'processorinputarea.ui'
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
    QDoubleSpinBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Ui_ProcessorInputArea(object):
    def setupUi(self, ProcessorInputArea):
        if not ProcessorInputArea.objectName():
            ProcessorInputArea.setObjectName("ProcessorInputArea")
        ProcessorInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(ProcessorInputArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayoutWidget = QWidget(ProcessorInputArea)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Header = QLabel(self.formLayoutWidget)
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
        self.clockRateLabel = QLabel(self.formLayoutWidget)
        self.clockRateLabel.setObjectName("clockRateLabel")

        self.gridLayout.addWidget(self.clockRateLabel, 2, 0, 1, 1)

        self.nameLabel = QLabel(self.formLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")

        self.gridLayout.addWidget(self.nameLabel, 1, 0, 1, 1)

        self.coresSpinBox = QSpinBox(self.formLayoutWidget)
        self.coresSpinBox.setObjectName("coresSpinBox")

        self.gridLayout.addWidget(self.coresSpinBox, 3, 2, 1, 1)

        self.clockRateLabel_2 = QLabel(self.formLayoutWidget)
        self.clockRateLabel_2.setObjectName("clockRateLabel_2")

        self.gridLayout.addWidget(self.clockRateLabel_2, 2, 3, 1, 1)

        self.coresLabel = QLabel(self.formLayoutWidget)
        self.coresLabel.setObjectName("coresLabel")

        self.gridLayout.addWidget(self.coresLabel, 3, 0, 1, 1)

        self.nameLineEdit = QLineEdit(self.formLayoutWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")

        self.gridLayout.addWidget(self.nameLineEdit, 1, 2, 1, 1)

        self.clockRateDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.clockRateDoubleSpinBox.setObjectName("clockRateDoubleSpinBox")

        self.gridLayout.addWidget(self.clockRateDoubleSpinBox, 2, 2, 1, 1)

        self.lastUpdateLabel = QLabel(self.formLayoutWidget)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")

        self.gridLayout.addWidget(self.lastUpdateLabel, 4, 0, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastUpdateLineEdit.setObjectName("lastUpdateLineEdit")

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 4, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

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
        self.clockRateLabel.setBuddy(self.clockRateDoubleSpinBox)
        self.nameLabel.setBuddy(self.nameLineEdit)
        self.coresLabel.setBuddy(self.coresSpinBox)
        self.lastUpdateLabel.setBuddy(self.lastUpdateLineEdit)
        # endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameLineEdit, self.clockRateDoubleSpinBox)
        QWidget.setTabOrder(self.clockRateDoubleSpinBox, self.coresSpinBox)
        QWidget.setTabOrder(self.coresSpinBox, self.lastUpdateLineEdit)
        QWidget.setTabOrder(self.lastUpdateLineEdit, self.addPushButton)
        QWidget.setTabOrder(self.addPushButton, self.editFinishPushButton)

        self.retranslateUi(ProcessorInputArea)

        QMetaObject.connectSlotsByName(ProcessorInputArea)

    # setupUi

    def retranslateUi(self, ProcessorInputArea):
        ProcessorInputArea.setWindowTitle(
            QCoreApplication.translate("ProcessorInputArea", "Prozessor", None)
        )
        # if QT_CONFIG(accessibility)
        ProcessorInputArea.setAccessibleName(
            QCoreApplication.translate(
                "ProcessorInputArea", "ProcessorInputDialog", None
            )
        )
        # endif // QT_CONFIG(accessibility)
        ProcessorInputArea.setTitle(
            QCoreApplication.translate("ProcessorInputArea", "Prozessor", None)
        )
        self.label_Header.setText(
            QCoreApplication.translate("ProcessorInputArea", "Prozessor", None)
        )
        self.clockRateLabel.setText(
            QCoreApplication.translate("ProcessorInputArea", "Taktrate", None)
        )
        self.nameLabel.setText(
            QCoreApplication.translate("ProcessorInputArea", "Name", None)
        )
        self.clockRateLabel_2.setText(
            QCoreApplication.translate("ProcessorInputArea", "Ghz", None)
        )
        self.coresLabel.setText(
            QCoreApplication.translate("ProcessorInputArea", "Kerne", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate(
                "ProcessorInputArea", "Letzte \u00c4nderung", None
            )
        )
        self.addPushButton.setText(
            QCoreApplication.translate("ProcessorInputArea", "+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("ProcessorInputArea", "Bearbeiten", None)
        )

    # retranslateUi
