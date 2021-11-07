/********************************************************************************
** Form generated from reading UI file 'service.ui'
**
** Created by: Qt User Interface Compiler version 6.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef SERVICE_H
#define SERVICE_H

#include <QtCore/QVariant>
#include <QtWidgets/QAbstractButton>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_ServiceDiscovery
{
public:
    QVBoxLayout *verticalLayout;
    QListWidget *list;
    QLabel *status;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *ServiceDiscovery)
    {
        if (ServiceDiscovery->objectName().isEmpty())
            ServiceDiscovery->setObjectName(QString::fromUtf8("ServiceDiscovery"));
        ServiceDiscovery->resize(539, 486);
        verticalLayout = new QVBoxLayout(ServiceDiscovery);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        list = new QListWidget(ServiceDiscovery);
        list->setObjectName(QString::fromUtf8("list"));

        verticalLayout->addWidget(list);

        status = new QLabel(ServiceDiscovery);
        status->setObjectName(QString::fromUtf8("status"));

        verticalLayout->addWidget(status);

        buttonBox = new QDialogButtonBox(ServiceDiscovery);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setStandardButtons(QDialogButtonBox::Close);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(ServiceDiscovery);
        QObject::connect(buttonBox, &QDialogButtonBox::accepted, ServiceDiscovery, qOverload<>(&QDialog::accept));
        QObject::connect(buttonBox, &QDialogButtonBox::rejected, ServiceDiscovery, qOverload<>(&QDialog::reject));

        QMetaObject::connectSlotsByName(ServiceDiscovery);
    } // setupUi

    void retranslateUi(QDialog *ServiceDiscovery)
    {
        ServiceDiscovery->setWindowTitle(QCoreApplication::translate("ServiceDiscovery", "Available Services", nullptr));
        status->setText(QCoreApplication::translate("ServiceDiscovery", "Querying...", nullptr));
    } // retranslateUi

};

namespace Ui {
    class ServiceDiscovery: public Ui_ServiceDiscovery {};
} // namespace Ui

QT_END_NAMESPACE

#endif // SERVICE_H
