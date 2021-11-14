################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QDate
from PySide6.QtCore import QDateTime
from PySide6.QtCore import QLocale
from PySide6.QtCore import QMetaObject
from PySide6.QtCore import QObject
from PySide6.QtCore import QPoint
from PySide6.QtCore import QRect
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtCore import QTime
from PySide6.QtCore import QUrl
from PySide6.QtGui import QAction
from PySide6.QtGui import QBrush
from PySide6.QtGui import QColor
from PySide6.QtGui import QConicalGradient
from PySide6.QtGui import QCursor
from PySide6.QtGui import QFont
from PySide6.QtGui import QFontDatabase
from PySide6.QtGui import QGradient
from PySide6.QtGui import QIcon
from PySide6.QtGui import QImage
from PySide6.QtGui import QKeySequence
from PySide6.QtGui import QLinearGradient
from PySide6.QtGui import QPainter
from PySide6.QtGui import QPalette
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QRadialGradient
from PySide6.QtGui import QTransform
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QListView
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMenu
from PySide6.QtWidgets import QMenuBar
from PySide6.QtWidgets import QScrollArea
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QSplitter
from PySide6.QtWidgets import QStatusBar
from PySide6.QtWidgets import QToolBar
from PySide6.QtWidgets import QTreeView
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

import jmbde.gui.resources_rc


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(881, 525)
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
        iconThemeName = "tango-icon"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(
                ":/icons/tango-icon/22x22/document-new.png",
                QSize(),
                QIcon.Normal,
                QIcon.Off,
            )
            icon1.addFile(
                ":/icons/tango-icon/22x22/document-new.png",
                QSize(),
                QIcon.Normal,
                QIcon.On,
            )
            icon1.addFile(
                ":/icons/tango-icon/22x22/document-new.png",
                QSize(),
                QIcon.Disabled,
                QIcon.Off,
            )
            icon1.addFile(
                ":/icons/tango-icon/22x22/document-new.png",
                QSize(),
                QIcon.Disabled,
                QIcon.On,
            )
            icon1.addFile(
                ":/icons/tango-icon/22x22/document-new.png",
                QSize(),
                QIcon.Active,
                QIcon.Off,
            )
            icon1.addFile(
                ":/icons/tango-icon/22x22/document-new.png",
                QSize(),
                QIcon.Active,
                QIcon.On,
            )
            icon1.addFile(
                ":/icons/tango-icon/22x22/document-new.png",
                QSize(),
                QIcon.Selected,
                QIcon.Off,
            )
            icon1.addFile(
                ":/icons/tango-icon/22x22/document-new.png",
                QSize(),
                QIcon.Selected,
                QIcon.On,
            )

        self.actionNew.setIcon(icon1)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setEnabled(True)
        icon2 = QIcon()
        iconThemeName = "tango-icon"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(
                ":/icons/tango-icon/22x22/document-open.png",
                QSize(),
                QIcon.Normal,
                QIcon.Off,
            )
            icon2.addFile(
                ":/icons/tango-icon/22x22/document-open.png",
                QSize(),
                QIcon.Normal,
                QIcon.On,
            )
            icon2.addFile(
                ":/icons/tango-icon/22x22/document-open.png",
                QSize(),
                QIcon.Disabled,
                QIcon.Off,
            )
            icon2.addFile(
                ":/icons/tango-icon/22x22/document-open.png",
                QSize(),
                QIcon.Active,
                QIcon.Off,
            )
            icon2.addFile(
                ":/icons/tango-icon/22x22/document-open.png",
                QSize(),
                QIcon.Active,
                QIcon.On,
            )
            icon2.addFile(
                ":/icons/tango-icon/22x22/document-open.png",
                QSize(),
                QIcon.Selected,
                QIcon.Off,
            )
            icon2.addFile(
                ":/icons/tango-icon/22x22/document-open.png",
                QSize(),
                QIcon.Selected,
                QIcon.On,
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
        iconThemeName = "tango-icon"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(
                ":/icons/tango/32x32/document-print.png",
                QSize(),
                QIcon.Normal,
                QIcon.Off,
            )
            icon3.addFile(
                ":/icons/tango-icon/32x32/document-print.png",
                QSize(),
                QIcon.Normal,
                QIcon.On,
            )
            icon3.addFile(
                ":/icons/tango-icon/32x32/document-print.png",
                QSize(),
                QIcon.Disabled,
                QIcon.Off,
            )
            icon3.addFile(
                ":/icons/tango-icon/32x32/document-print.png",
                QSize(),
                QIcon.Active,
                QIcon.Off,
            )
            icon3.addFile(
                ":/icons/tango-icon/32x32/document-print.png",
                QSize(),
                QIcon.Active,
                QIcon.On,
            )
            icon3.addFile(
                ":/icons/tango-icon/32x32/document-print.png",
                QSize(),
                QIcon.Selected,
                QIcon.Off,
            )
            icon3.addFile(
                ":/icons/tango-icon/32x32/document-print.png",
                QSize(),
                QIcon.Selected,
                QIcon.On,
            )

        self.actionPrint.setIcon(icon3)
        self.actionPrint_Preview = QAction(MainWindow)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        icon4 = QIcon()
        iconThemeName = "tango-icon"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(
                ":/icons/tango-icon/32x32/document-print-preview.png",
                QSize(),
                QIcon.Normal,
                QIcon.Off,
            )
            icon4.addFile(
                ":/icons/tango-icon/32x32/document-print-preview.png",
                QSize(),
                QIcon.Normal,
                QIcon.On,
            )
            icon4.addFile(
                ":/icons/tango-icon/32x32/document-print-preview.png",
                QSize(),
                QIcon.Disabled,
                QIcon.Off,
            )
            icon4.addFile(
                ":/icons/tango-icon/32x32/document-print-preview.png",
                QSize(),
                QIcon.Active,
                QIcon.Off,
            )
            icon4.addFile(
                ":/icons/tango-icon/32x32/document-print-preview.png",
                QSize(),
                QIcon.Active,
                QIcon.On,
            )
            icon4.addFile(
                ":/icons/tango-icon/32x32/document-print-preview.png",
                QSize(),
                QIcon.Selected,
                QIcon.Off,
            )
            icon4.addFile(
                ":/icons/tango-icon/32x32/document-print-preview.png",
                QSize(),
                QIcon.Selected,
                QIcon.On,
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
        icon5.addFile(
            ":/icons/tango/32x32/document-print-preview.png",
            QSize(),
            QIcon.Normal,
            QIcon.On,
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
        self.listView.setAlternatingRowColors(True)
        self.splitter.addWidget(self.listView)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 485, 388))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.scrollArea)

        self.verticalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 881, 24))
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
                "MainWindow", "JMBDE Version 0.4.0 (c) J\u00fcrgen M\u00fclbert", None
            )
        )
        self.actionPreferences.setText(
            QCoreApplication.translate("MainWindow", "Einstellungen...", None)
        )
        self.actionAbout.setText(
            QCoreApplication.translate("MainWindow", "\u00dcber...", None)
        )
        self.actionNew.setText(QCoreApplication.translate("MainWindow", "Neu", None))
        # if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+N", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(
            QCoreApplication.translate("MainWindow", "jmbde beenden", None)
        )
        self.actionOpen.setText(
            QCoreApplication.translate("MainWindow", "\u00d6ffnen...", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+O", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionImport.setText(
            QCoreApplication.translate("MainWindow", "Importieren...", None)
        )
        self.actionExport.setText(
            QCoreApplication.translate("MainWindow", "Exportieren..", None)
        )
        self.actionPrint.setText(
            QCoreApplication.translate("MainWindow", "Drucken...", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionPrint.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+P", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionPrint_Preview.setText(
            QCoreApplication.translate("MainWindow", "Drucken Vorschau...", None)
        )
        self.action_Export_Pdf.setText(
            QCoreApplication.translate("MainWindow", "&Exportieren Pdf", None)
        )
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", "Hilfe", None))
        self.actionEditAdd.setText(
            QCoreApplication.translate("MainWindow", "Hinzuf\u00fcgen", None)
        )
        self.actionEditEdit.setText(
            QCoreApplication.translate("MainWindow", "Bearbeiten", None)
        )
        self.actionEditDelete.setText(
            QCoreApplication.translate("MainWindow", "L\u00f6schen", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "Datei", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))

    # retranslateUi
