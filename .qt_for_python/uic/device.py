/********************************************************************************
** Form generated from reading UI file 'device.ui'
**
** Created by: Qt User Interface Compiler version 6.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef DEVICE_H
#define DEVICE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_DeviceDiscovery
{
public:
    QVBoxLayout *verticalLayout;
    QListWidget *list;
    QGroupBox *groupBox;
    QHBoxLayout *horizontalLayout_2;
    QCheckBox *power;
    QCheckBox *discoverable;
    QHBoxLayout *horizontalLayout;
    QPushButton *scan;
    QPushButton *clear;
    QPushButton *quit;

    void setupUi(QDialog *DeviceDiscovery)
    {
        if (DeviceDiscovery->objectName().isEmpty())
            DeviceDiscovery->setObjectName(QString::fromUtf8("DeviceDiscovery"));
        DeviceDiscovery->resize(400, 411);
        verticalLayout = new QVBoxLayout(DeviceDiscovery);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        list = new QListWidget(DeviceDiscovery);
        list->setObjectName(QString::fromUtf8("list"));

        verticalLayout->addWidget(list);

        groupBox = new QGroupBox(DeviceDiscovery);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        horizontalLayout_2 = new QHBoxLayout(groupBox);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        power = new QCheckBox(groupBox);
        power->setObjectName(QString::fromUtf8("power"));
        power->setChecked(true);

        horizontalLayout_2->addWidget(power);

        discoverable = new QCheckBox(groupBox);
        discoverable->setObjectName(QString::fromUtf8("discoverable"));
        discoverable->setChecked(true);

        horizontalLayout_2->addWidget(discoverable);


        verticalLayout->addWidget(groupBox);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        scan = new QPushButton(DeviceDiscovery);
        scan->setObjectName(QString::fromUtf8("scan"));

        horizontalLayout->addWidget(scan);

        clear = new QPushButton(DeviceDiscovery);
        clear->setObjectName(QString::fromUtf8("clear"));

        horizontalLayout->addWidget(clear);

        quit = new QPushButton(DeviceDiscovery);
        quit->setObjectName(QString::fromUtf8("quit"));

        horizontalLayout->addWidget(quit);


        verticalLayout->addLayout(horizontalLayout);


        retranslateUi(DeviceDiscovery);
        QObject::connect(quit, &QPushButton::clicked, DeviceDiscovery, qOverload<>(&QDialog::accept));
        QObject::connect(clear, &QPushButton::clicked, list, qOverload<>(&QListWidget::clear));

        QMetaObject::connectSlotsByName(DeviceDiscovery);
    } // setupUi

    void retranslateUi(QDialog *DeviceDiscovery)
    {
        DeviceDiscovery->setWindowTitle(QCoreApplication::translate("DeviceDiscovery", "Bluetooth Scanner", nullptr));
        groupBox->setTitle(QCoreApplication::translate("DeviceDiscovery", "Local Device", nullptr));
        power->setText(QCoreApplication::translate("DeviceDiscovery", "Bluetooth Powered On", nullptr));
        discoverable->setText(QCoreApplication::translate("DeviceDiscovery", "Discoverable", nullptr));
        scan->setText(QCoreApplication::translate("DeviceDiscovery", "Scan", nullptr));
        clear->setText(QCoreApplication::translate("DeviceDiscovery", "Clear", nullptr));
        quit->setText(QCoreApplication::translate("DeviceDiscovery", "Quit", nullptr));
    } // retranslateUi

};

namespace Ui {
    class DeviceDiscovery: public Ui_DeviceDiscovery {};
} // namespace Ui

QT_END_NAMESPACE

#endif // DEVICE_H
