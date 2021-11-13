/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QListView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QTreeView>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionPreferences;
    QAction *actionAbout;
    QAction *actionNew;
    QAction *actionQuit;
    QAction *actionOpen;
    QAction *actionImport;
    QAction *actionExport;
    QAction *actionPrint;
    QAction *actionPrint_Preview;
    QAction *action_Export_Pdf;
    QAction *actionHelp;
    QAction *actionEditAdd;
    QAction *actionEditEdit;
    QAction *actionEditDelete;
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout;
    QSplitter *splitter;
    QTreeView *treeView;
    QListView *listView;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QMenuBar *menuBar;
    QMenu *menuFile;
    QMenu *menuEdit;
    QMenu *menuHelp;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->setWindowModality(Qt::NonModal);
        MainWindow->resize(881, 525);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        MainWindow->setMinimumSize(QSize(500, 250));
        MainWindow->setBaseSize(QSize(500, 250));
        actionPreferences = new QAction(MainWindow);
        actionPreferences->setObjectName(QString::fromUtf8("actionPreferences"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/tango-icon/ApplicationPreferences.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionPreferences->setIcon(icon);
        actionAbout = new QAction(MainWindow);
        actionAbout->setObjectName(QString::fromUtf8("actionAbout"));
        actionNew = new QAction(MainWindow);
        actionNew->setObjectName(QString::fromUtf8("actionNew"));
        actionNew->setEnabled(true);
        QIcon icon1;
        QString iconThemeName = QString::fromUtf8("tango-icon");
        if (QIcon::hasThemeIcon(iconThemeName)) {
            icon1 = QIcon::fromTheme(iconThemeName);
        } else {
            icon1.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-new.png"), QSize(), QIcon::Normal, QIcon::Off);
            icon1.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-new.png"), QSize(), QIcon::Normal, QIcon::On);
            icon1.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-new.png"), QSize(), QIcon::Disabled, QIcon::Off);
            icon1.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-new.png"), QSize(), QIcon::Disabled, QIcon::On);
            icon1.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-new.png"), QSize(), QIcon::Active, QIcon::Off);
            icon1.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-new.png"), QSize(), QIcon::Active, QIcon::On);
            icon1.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-new.png"), QSize(), QIcon::Selected, QIcon::Off);
            icon1.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-new.png"), QSize(), QIcon::Selected, QIcon::On);
        }
        actionNew->setIcon(icon1);
        actionQuit = new QAction(MainWindow);
        actionQuit->setObjectName(QString::fromUtf8("actionQuit"));
        actionOpen = new QAction(MainWindow);
        actionOpen->setObjectName(QString::fromUtf8("actionOpen"));
        actionOpen->setEnabled(true);
        QIcon icon2;
        iconThemeName = QString::fromUtf8("tango-icon");
        if (QIcon::hasThemeIcon(iconThemeName)) {
            icon2 = QIcon::fromTheme(iconThemeName);
        } else {
            icon2.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-open.png"), QSize(), QIcon::Normal, QIcon::Off);
            icon2.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-open.png"), QSize(), QIcon::Normal, QIcon::On);
            icon2.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-open.png"), QSize(), QIcon::Disabled, QIcon::Off);
            icon2.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-open.png"), QSize(), QIcon::Active, QIcon::Off);
            icon2.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-open.png"), QSize(), QIcon::Active, QIcon::On);
            icon2.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-open.png"), QSize(), QIcon::Selected, QIcon::Off);
            icon2.addFile(QString::fromUtf8(":/icons/tango-icon/22x22/document-open.png"), QSize(), QIcon::Selected, QIcon::On);
        }
        actionOpen->setIcon(icon2);
        actionImport = new QAction(MainWindow);
        actionImport->setObjectName(QString::fromUtf8("actionImport"));
        actionImport->setEnabled(false);
        actionExport = new QAction(MainWindow);
        actionExport->setObjectName(QString::fromUtf8("actionExport"));
        actionExport->setEnabled(false);
        actionPrint = new QAction(MainWindow);
        actionPrint->setObjectName(QString::fromUtf8("actionPrint"));
        QIcon icon3;
        iconThemeName = QString::fromUtf8("tango-icon");
        if (QIcon::hasThemeIcon(iconThemeName)) {
            icon3 = QIcon::fromTheme(iconThemeName);
        } else {
            icon3.addFile(QString::fromUtf8(":/icons/tango/32x32/document-print.png"), QSize(), QIcon::Normal, QIcon::Off);
            icon3.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print.png"), QSize(), QIcon::Normal, QIcon::On);
            icon3.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print.png"), QSize(), QIcon::Disabled, QIcon::Off);
            icon3.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print.png"), QSize(), QIcon::Active, QIcon::Off);
            icon3.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print.png"), QSize(), QIcon::Active, QIcon::On);
            icon3.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print.png"), QSize(), QIcon::Selected, QIcon::Off);
            icon3.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print.png"), QSize(), QIcon::Selected, QIcon::On);
        }
        actionPrint->setIcon(icon3);
        actionPrint_Preview = new QAction(MainWindow);
        actionPrint_Preview->setObjectName(QString::fromUtf8("actionPrint_Preview"));
        QIcon icon4;
        iconThemeName = QString::fromUtf8("tango-icon");
        if (QIcon::hasThemeIcon(iconThemeName)) {
            icon4 = QIcon::fromTheme(iconThemeName);
        } else {
            icon4.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print-preview.png"), QSize(), QIcon::Normal, QIcon::Off);
            icon4.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print-preview.png"), QSize(), QIcon::Normal, QIcon::On);
            icon4.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print-preview.png"), QSize(), QIcon::Disabled, QIcon::Off);
            icon4.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print-preview.png"), QSize(), QIcon::Active, QIcon::Off);
            icon4.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print-preview.png"), QSize(), QIcon::Active, QIcon::On);
            icon4.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print-preview.png"), QSize(), QIcon::Selected, QIcon::Off);
            icon4.addFile(QString::fromUtf8(":/icons/tango-icon/32x32/document-print-preview.png"), QSize(), QIcon::Selected, QIcon::On);
        }
        actionPrint_Preview->setIcon(icon4);
        actionPrint_Preview->setIconVisibleInMenu(true);
        action_Export_Pdf = new QAction(MainWindow);
        action_Export_Pdf->setObjectName(QString::fromUtf8("action_Export_Pdf"));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/icons/tango/32x32/document-print-preview.png"), QSize(), QIcon::Normal, QIcon::Off);
        icon5.addFile(QString::fromUtf8(":/icons/tango/32x32/document-print-preview.png"), QSize(), QIcon::Normal, QIcon::On);
        action_Export_Pdf->setIcon(icon5);
        action_Export_Pdf->setVisible(false);
        actionHelp = new QAction(MainWindow);
        actionHelp->setObjectName(QString::fromUtf8("actionHelp"));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/icons/tango-icon/icons/tango-icon/16x16/help-browser.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionHelp->setIcon(icon6);
        actionEditAdd = new QAction(MainWindow);
        actionEditAdd->setObjectName(QString::fromUtf8("actionEditAdd"));
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/icons/tango/white/FileNew.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionEditAdd->setIcon(icon7);
        actionEditEdit = new QAction(MainWindow);
        actionEditEdit->setObjectName(QString::fromUtf8("actionEditEdit"));
        QIcon icon8;
        icon8.addFile(QString::fromUtf8(":/icons/tango/white/TaskEdit.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionEditEdit->setIcon(icon8);
        actionEditDelete = new QAction(MainWindow);
        actionEditDelete->setObjectName(QString::fromUtf8("actionEditDelete"));
        QIcon icon9;
        icon9.addFile(QString::fromUtf8(":/icons/tango/white/TaskDelete.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionEditDelete->setIcon(icon9);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(2);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(centralWidget->sizePolicy().hasHeightForWidth());
        centralWidget->setSizePolicy(sizePolicy1);
        centralWidget->setMinimumSize(QSize(300, 0));
        verticalLayout = new QVBoxLayout(centralWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        splitter = new QSplitter(centralWidget);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setOrientation(Qt::Horizontal);
        treeView = new QTreeView(splitter);
        treeView->setObjectName(QString::fromUtf8("treeView"));
        QSizePolicy sizePolicy2(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(treeView->sizePolicy().hasHeightForWidth());
        treeView->setSizePolicy(sizePolicy2);
        treeView->setMinimumSize(QSize(140, 200));
        treeView->setMaximumSize(QSize(140, 16777215));
        treeView->setBaseSize(QSize(150, 0));
        treeView->setEditTriggers(QAbstractItemView::NoEditTriggers);
        treeView->setProperty("showDropIndicator", QVariant(false));
        treeView->setSelectionBehavior(QAbstractItemView::SelectItems);
        splitter->addWidget(treeView);
        treeView->header()->setVisible(false);
        listView = new QListView(splitter);
        listView->setObjectName(QString::fromUtf8("listView"));
        QSizePolicy sizePolicy3(QSizePolicy::Minimum, QSizePolicy::Expanding);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(listView->sizePolicy().hasHeightForWidth());
        listView->setSizePolicy(sizePolicy3);
        listView->setMinimumSize(QSize(200, 0));
        listView->setMaximumSize(QSize(200, 16777215));
        listView->setEditTriggers(QAbstractItemView::NoEditTriggers);
        listView->setProperty("showDropIndicator", QVariant(false));
        listView->setDefaultDropAction(Qt::IgnoreAction);
        listView->setAlternatingRowColors(true);
        splitter->addWidget(listView);
        scrollArea = new QScrollArea(splitter);
        scrollArea->setObjectName(QString::fromUtf8("scrollArea"));
        scrollArea->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOn);
        scrollArea->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOn);
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QString::fromUtf8("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 485, 388));
        scrollArea->setWidget(scrollAreaWidgetContents);
        splitter->addWidget(scrollArea);

        verticalLayout->addWidget(splitter);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 881, 24));
        menuFile = new QMenu(menuBar);
        menuFile->setObjectName(QString::fromUtf8("menuFile"));
        menuEdit = new QMenu(menuBar);
        menuEdit->setObjectName(QString::fromUtf8("menuEdit"));
        menuHelp = new QMenu(menuBar);
        menuHelp->setObjectName(QString::fromUtf8("menuHelp"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuFile->menuAction());
        menuBar->addAction(menuEdit->menuAction());
        menuBar->addAction(menuHelp->menuAction());
        menuFile->addAction(actionNew);
        menuFile->addAction(actionOpen);
        menuFile->addAction(actionImport);
        menuFile->addAction(actionExport);
        menuFile->addAction(actionPrint);
        menuFile->addAction(actionPrint_Preview);
        menuFile->addAction(action_Export_Pdf);
        menuFile->addAction(actionQuit);
        menuEdit->addAction(actionEditAdd);
        menuEdit->addAction(actionEditEdit);
        menuEdit->addAction(actionEditDelete);
        menuEdit->addAction(actionPreferences);
        menuHelp->addAction(actionAbout);
        menuHelp->addAction(actionHelp);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actionEditAdd);
        mainToolBar->addAction(actionEditEdit);
        mainToolBar->addAction(actionEditDelete);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actionPrint);
        mainToolBar->addAction(action_Export_Pdf);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "JMBDE Version 0.4.0 (c) J\303\274rgen M\303\274lbert", nullptr));
        actionPreferences->setText(QCoreApplication::translate("MainWindow", "Einstellungen...", nullptr));
        actionAbout->setText(QCoreApplication::translate("MainWindow", "\303\234ber...", nullptr));
        actionNew->setText(QCoreApplication::translate("MainWindow", "Neu", nullptr));
#if QT_CONFIG(shortcut)
        actionNew->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+N", nullptr));
#endif // QT_CONFIG(shortcut)
        actionQuit->setText(QCoreApplication::translate("MainWindow", "jmbde beenden", nullptr));
        actionOpen->setText(QCoreApplication::translate("MainWindow", "\303\226ffnen...", nullptr));
#if QT_CONFIG(shortcut)
        actionOpen->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+O", nullptr));
#endif // QT_CONFIG(shortcut)
        actionImport->setText(QCoreApplication::translate("MainWindow", "Importieren...", nullptr));
        actionExport->setText(QCoreApplication::translate("MainWindow", "Exportieren..", nullptr));
        actionPrint->setText(QCoreApplication::translate("MainWindow", "Drucken...", nullptr));
#if QT_CONFIG(shortcut)
        actionPrint->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+P", nullptr));
#endif // QT_CONFIG(shortcut)
        actionPrint_Preview->setText(QCoreApplication::translate("MainWindow", "Drucken Vorschau...", nullptr));
        action_Export_Pdf->setText(QCoreApplication::translate("MainWindow", "&Exportieren Pdf", nullptr));
        actionHelp->setText(QCoreApplication::translate("MainWindow", "Hilfe", nullptr));
        actionEditAdd->setText(QCoreApplication::translate("MainWindow", "Hinzuf\303\274gen", nullptr));
        actionEditEdit->setText(QCoreApplication::translate("MainWindow", "Bearbeiten", nullptr));
        actionEditDelete->setText(QCoreApplication::translate("MainWindow", "L\303\266schen", nullptr));
        menuFile->setTitle(QCoreApplication::translate("MainWindow", "Datei", nullptr));
        menuEdit->setTitle(QCoreApplication::translate("MainWindow", "Edit", nullptr));
        menuHelp->setTitle(QCoreApplication::translate("MainWindow", "Help", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAINWINDOW_H
