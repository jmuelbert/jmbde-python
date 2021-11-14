################################################################################
## Form generated from reading UI file 'csvimportdialog.ui'
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
from PySide6.QtWidgets import QAbstractButton
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QDialogButtonBox
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QTableView
from PySide6.QtWidgets import QVBoxLayout


class Ui_CsvImportDialog:
    def setupUi(self, CsvImportDialog):
        if not CsvImportDialog.objectName():
            CsvImportDialog.setObjectName("CsvImportDialog")
        CsvImportDialog.resize(671, 318)
        CsvImportDialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(CsvImportDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QTableView(CsvImportDialog)
        self.tableView.setObjectName("tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.buttonBox = QDialogButtonBox(CsvImportDialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CsvImportDialog)
        self.buttonBox.accepted.connect(CsvImportDialog.accept)
        self.buttonBox.rejected.connect(CsvImportDialog.reject)

        QMetaObject.connectSlotsByName(CsvImportDialog)

    # setupUi

    def retranslateUi(self, CsvImportDialog):
        CsvImportDialog.setWindowTitle(
            QCoreApplication.translate("CsvImportDialog", "CSV Import", None)
        )

    # retranslateUi
