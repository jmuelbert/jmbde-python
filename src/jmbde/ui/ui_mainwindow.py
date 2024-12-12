# -*- coding: utf-8 -*-
################################################################################
# Form generated from reading UI file 'mainwindow.ui'
##
# Created by: Qt User Interface Compiler version 5.15.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 250))
        MainWindow.setBaseSize(QSize(500, 250))
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        icon = QIcon()
        icon.addFile(
            ":/icons/tango-icon/ApplicationPreferences.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.actionPreferences.setIcon(icon)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(
            ":/icons/tango-icon/22x22/document-new.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.actionNew.setIcon(icon1)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setEnabled(True)
        icon2 = QIcon()
        icon2.addFile(
            ":/icons/tango-icon/22x22/document-open.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.actionOpen.setIcon(icon2)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionImport.setEnabled(False)
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExport.setEnabled(False)
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        icon3 = QIcon()
        icon3.addFile(
            ":/icons/tango/32x32/document-print.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionPrint.setIcon(icon3)
        self.actionPrint_Preview = QAction(MainWindow)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        icon4 = QIcon()
        icon4.addFile(
            ":/icons/tango-icon/32x32/document-print-preview.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.actionPrint_Preview.setIcon(icon4)
        self.actionPrint_Preview.setIconVisibleInMenu(True)
        self.action_Export_Pdf = QAction(MainWindow)
        self.action_Export_Pdf.setObjectName("action_Export_Pdf")
        icon5 = QIcon()
        icon5.addFile(
            ":/icons/tango/32x32/document-print-preview.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.action_Export_Pdf.setIcon(icon5)
        self.action_Export_Pdf.setVisible(False)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        icon6 = QIcon()
        icon6.addFile(
            ":/icons/tango-icon/icons/tango-icon/16x16/help-browser.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.actionHelp.setIcon(icon6)
        self.actionEditAdd = QAction(MainWindow)
        self.actionEditAdd.setObjectName("actionEditAdd")
        icon7 = QIcon()
        icon7.addFile(
            ":/icons/tango/white/FileNew.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionEditAdd.setIcon(icon7)
        self.actionEditEdit = QAction(MainWindow)
        self.actionEditEdit.setObjectName("actionEditEdit")
        icon8 = QIcon()
        icon8.addFile(
            ":/icons/tango/white/TaskEdit.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionEditEdit.setIcon(icon8)
        self.actionEditDelete = QAction(MainWindow)
        self.actionEditDelete.setObjectName("actionEditDelete")
        icon9 = QIcon()
        icon9.addFile(
            ":/icons/tango/white/TaskDelete.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionEditDelete.setIcon(icon9)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.centralWidget.sizePolicy().hasHeightForWidth()
        )
        self.centralWidget.setSizePolicy(sizePolicy1)
        self.centralWidget.setMinimumSize(QSize(300, 0))
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QSplitter(self.centralWidget)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.treeView = QTreeView(self.splitter)
        self.treeView.setObjectName("treeView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy2)
        self.treeView.setMinimumSize(QSize(140, 200))
        self.treeView.setMaximumSize(QSize(140, 16777215))
        self.treeView.setBaseSize(QSize(150, 0))
        self.treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeView.setProperty("showDropIndicator", False)
        self.treeView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.splitter.addWidget(self.treeView)
        self.treeView.header().setVisible(False)
        self.listView = QListView(self.splitter)
        self.listView.setObjectName("listView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy3)
        self.listView.setMinimumSize(QSize(200, 0))
        self.listView.setMaximumSize(QSize(200, 16777215))
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.setProperty("showDropIndicator", False)
        self.listView.setDefaultDropAction(Qt.IgnoreAction)
        self.splitter.addWidget(self.listView)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 404, 465))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.scrollArea)

        self.verticalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionPrint_Preview)
        self.menuFile.addAction(self.action_Export_Pdf)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionEditAdd)
        self.menuEdit.addAction(self.actionEditEdit)
        self.menuEdit.addAction(self.actionEditDelete)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionEditAdd)
        self.mainToolBar.addAction(self.actionEditEdit)
        self.mainToolBar.addAction(self.actionEditDelete)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionPrint)
        self.mainToolBar.addAction(self.action_Export_Pdf)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow", "JMBDE Version 0.2.0 (c) J\u00fcrgen M\u00fclbert", None
            )
        )
        self.actionPreferences.setText(
            QCoreApplication.translate("MainWindow", "Preferences", None)
        )
        self.actionAbout.setText(
            QCoreApplication.translate("MainWindow", "About", None)
        )
        self.actionNew.setText(QCoreApplication.translate("MainWindow", "New", None))
        # if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+N", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", "Quit", None))
        self.actionOpen.setText(
            QCoreApplication.translate("MainWindow", "Open...", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+O", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionImport.setText(
            QCoreApplication.translate("MainWindow", "Import...", None)
        )
        self.actionExport.setText(
            QCoreApplication.translate("MainWindow", "Export...", None)
        )
        self.actionPrint.setText(
            QCoreApplication.translate("MainWindow", "Print...", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionPrint.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+P", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionPrint_Preview.setText(
            QCoreApplication.translate("MainWindow", "Print Preview...", None)
        )
        self.action_Export_Pdf.setText(
            QCoreApplication.translate("MainWindow", "&Export Pdf", None)
        )
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", "Help", None))
        self.actionEditAdd.setText(
            QCoreApplication.translate("MainWindow", "Add", None)
        )
        self.actionEditEdit.setText(
            QCoreApplication.translate("MainWindow", "Edit", None)
        )
        self.actionEditDelete.setText(
            QCoreApplication.translate("MainWindow", "Delete", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))

    # retranslateUi
