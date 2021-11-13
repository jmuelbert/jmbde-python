/********************************************************************************
** Form generated from reading UI file 'dialog.ui'
**
** Created by: Qt User Interface Compiler version 6.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef DIALOG_H
#define DIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QGridLayout *gridLayout;
    QLineEdit *input;
    QPushButton *send;
    QPlainTextEdit *output;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->resize(400, 300);
        gridLayout = new QGridLayout(Dialog);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        input = new QLineEdit(Dialog);
        input->setObjectName(QString::fromUtf8("input"));

        gridLayout->addWidget(input, 1, 0, 1, 1);

        send = new QPushButton(Dialog);
        send->setObjectName(QString::fromUtf8("send"));

        gridLayout->addWidget(send, 1, 1, 1, 1);

        output = new QPlainTextEdit(Dialog);
        output->setObjectName(QString::fromUtf8("output"));
        output->setReadOnly(true);
        output->setPlainText(QString::fromUtf8("Initializing WebChannel..."));
        output->setBackgroundVisible(false);

        gridLayout->addWidget(output, 0, 0, 1, 2);


        retranslateUi(Dialog);

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QCoreApplication::translate("Dialog", "Dialog", nullptr));
        input->setPlaceholderText(QCoreApplication::translate("Dialog", "Message Contents", nullptr));
        send->setText(QCoreApplication::translate("Dialog", "Send", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // DIALOG_H
