import sys
from datetime import datetime
from pathlib import Path

import pytest
from PySide6.QtCore import QObject, Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from jmbde.core.db_handler import DBHandler
from jmbde.gui.main_app import MainApp
from jmbde.models.employee import EmployeeModel

TEST_QML = """
import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "JMBDE Test"

    ListView {
        id: employeeList
        objectName: "employeeList"
        anchors.fill: parent
        model: employeeModel
        delegate: ItemDelegate {
            width: ListView.view.width
            height: 50
            text: model.name || ""
        }
    }
}
"""

TEST_EMPLOYEE = {
    "name": "Test Employee",
    "position": "Developer",
    "email": "test@example.com",
    "phone": "123-456",
    "department": "IT",
}


@pytest.fixture
def db_handler(tmp_path):
    """Provide database handler."""
    handler = DBHandler(tmp_path / "test.db")
    yield handler
    handler.cleanup()


@pytest.fixture
def employee_model(db_handler):
    """Provide employee model."""
    return EmployeeModel(database=db_handler.db)


def test_mainapp_integration(qapp, qml_engine, db_handler, employee_model, qtbot):
    """Test MainApp integration."""
    main_app = MainApp(db_handler=db_handler)

    qml_engine.rootContext().setContextProperty("mainApp", main_app)
    qml_engine.rootContext().setContextProperty("employeeModel", employee_model)
    qml_engine.loadData(TEST_QML.encode())
    qtbot.wait(100)

    root = qml_engine.rootObjects()[0]
    list_view = root.findChild(QObject, "employeeList")
    assert list_view is not None, "Failed to find ListView"

    initial_count = list_view.property("count")

    with qtbot.waitSignal(main_app.employeeAdded, timeout=1000):
        success = main_app.add_employee(**TEST_EMPLOYEE)
    assert success, "Failed to add employee"

    employee_model.refresh()
    qtbot.wait(100)

    new_count = list_view.property("count")
    assert new_count == initial_count + 1, "Model not updated after adding employee"

    # Proper cleanup
    main_app.cleanup()
    qml_engine.clearComponentCache()
    qml_engine.deleteLater()
    qml_engine = None  # Ensure complete deletion

    # Ensure the Qt application quits properly
    qapp.quit()
    del qapp  # Ensure QApplication is removed
