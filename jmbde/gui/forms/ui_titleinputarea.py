# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'titleinputarea.ui'
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
    QDateEdit,
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


class Ui_TitleInputArea(object):
    def setupUi(self, TitleInputArea):
        if not TitleInputArea.objectName():
            TitleInputArea.setObjectName(u"TitleInputArea")
        TitleInputArea.resize(730, 600)
        self.verticalLayout_3 = QVBoxLayout(TitleInputArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayoutWidget = QWidget(TitleInputArea)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerLabel = QLabel(self.formLayoutWidget)
        self.headerLabel.setObjectName(u"headerLabel")
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
        self.gridLayout.setObjectName(u"gridLayout")
        self.fromLabel = QLabel(self.formLayoutWidget)
        self.fromLabel.setObjectName(u"fromLabel")

        self.gridLayout.addWidget(self.fromLabel, 1, 0, 1, 1)

        self.fromDateEdit = QDateEdit(self.formLayoutWidget)
        self.fromDateEdit.setObjectName(u"fromDateEdit")

        self.gridLayout.addWidget(self.fromDateEdit, 1, 2, 1, 1)

        self.lastUpdateLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastUpdateLineEdit.setObjectName(u"lastUpdateLineEdit")
        self.lastUpdateLineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLineEdit, 2, 1, 1, 2)

        self.lastUpdateLabel = QLabel(self.formLayoutWidget)
        self.lastUpdateLabel.setObjectName(u"lastUpdateLabel")
        self.lastUpdateLabel.setEnabled(False)

        self.gridLayout.addWidget(self.lastUpdateLabel, 2, 0, 1, 1)

        self.titleLabel = QLabel(self.formLayoutWidget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.titleLineEdit = QLineEdit(self.formLayoutWidget)
        self.titleLineEdit.setObjectName(u"titleLineEdit")

        self.gridLayout.addWidget(self.titleLineEdit, 0, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addPushButton = QPushButton(self.formLayoutWidget)
        self.addPushButton.setObjectName(u"addPushButton")

        self.horizontalLayout.addWidget(self.addPushButton)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editFinishPushButton = QPushButton(self.formLayoutWidget)
        self.editFinishPushButton.setObjectName(u"editFinishPushButton")

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
            QCoreApplication.translate("TitleInputArea", u"Titel", None)
        )
        # if QT_CONFIG(accessibility)
        TitleInputArea.setAccessibleName(
            QCoreApplication.translate("TitleInputArea", u"TitleInputDialog", None)
        )
        # endif // QT_CONFIG(accessibility)
        TitleInputArea.setTitle(
            QCoreApplication.translate("TitleInputArea", u"Titel", None)
        )
        self.headerLabel.setText(
            QCoreApplication.translate("TitleInputArea", u"Titel", None)
        )
        self.fromLabel.setText(
            QCoreApplication.translate("TitleInputArea", u"ab", None)
        )
        self.lastUpdateLabel.setText(
            QCoreApplication.translate("TitleInputArea", u"Letzte \u00c4nderung", None)
        )
        self.titleLabel.setText(
            QCoreApplication.translate("TitleInputArea", u"Titel", None)
        )
        self.addPushButton.setText(
            QCoreApplication.translate("TitleInputArea", u"+", None)
        )
        self.editFinishPushButton.setText(
            QCoreApplication.translate("TitleInputArea", u"Bearbeiten", None)
        )

    # retranslateUi
