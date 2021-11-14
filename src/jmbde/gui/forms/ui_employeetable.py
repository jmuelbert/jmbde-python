################################################################################
## Form generated from reading UI file 'employeetable.ui'
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
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QTableView
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class Ui_EmployeeTable:
    def setupUi(self, EmployeeTable):
        if not EmployeeTable.objectName():
            EmployeeTable.setObjectName("EmployeeTable")
        EmployeeTable.resize(765, 596)
        self.verticalLayoutWidget = QWidget(EmployeeTable)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 751, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.tableView = QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setVisible(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(EmployeeTable)

        QMetaObject.connectSlotsByName(EmployeeTable)

    # setupUi

    def retranslateUi(self, EmployeeTable):
        EmployeeTable.setWindowTitle(
            QCoreApplication.translate("EmployeeTable", "Form", None)
        )

    # retranslateUi
