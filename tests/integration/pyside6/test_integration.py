# tests/integration/pyside6/test_integration.py

import sys
from datetime import datetime
from pathlib import Path

import pytest
from PySide6.QtCore import QObject, Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from jmbde.core.db_handler import DBHandler
from jmbde.gui.main_app import MainApp
from jmbde.models.employee import EmployeeData, EmployeeModel

# Test QML for ListView
TEST_QML = """
import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "JMBDE Test"

    ListView {
        id: employeeListView
        objectName: "employeeListView"
        anchors.fill: parent
        model: employeeModel

        delegate: ItemDelegate {
            width: ListView.view.width
            height: 50

            Column {
                Text { text: "Name: " + (model.name || "") }
                Text { text: "Position: " + (model.position || "") }
            }
        }
    }
}
"""


@pytest.fixture(scope="session")
def qapp():
    """Provide QGuiApplication instance."""
    app = QGuiApplication.instance()
    if app is None:
        app = QGuiApplication(sys.argv)
    return app


@pytest.fixture
def db_handler(tmp_path):
    """Provide database handler."""
    handler = DBHandler(tmp_path / "test.db")
    yield handler
    handler.cleanup()


@pytest.fixture
def employee_model(db_handler):
    """Provide employee model."""
    model = EmployeeModel(database=db_handler.db)
    return model


@pytest.fixture
def qml_engine(qapp):
    """Provide QML engine instance."""
    engine = QQmlApplicationEngine()
    yield engine
    engine.deleteLater()


@pytest.fixture
def test_employee_data():
    """Provide test employee data."""
    return {
        "name": "Test Employee",
        "position": "Developer",
        "email": "test@example.com",
        "phone": "123-456",
        "department": "IT",
        "hire_date": datetime.now(),
        "active": True,
    }


def test_qml_interface_loading(qapp, qml_engine, employee_model, db_handler, qtbot):
    """Test QML interface loading."""
    # Set context properties
    qml_engine.rootContext().setContextProperty("employeeModel", employee_model)

    # Load QML
    qml_engine.loadData(TEST_QML.encode())

    # Wait for loading
    qtbot.wait(100)

    # Verify loading
    root_objects = qml_engine.rootObjects()
    assert root_objects, "Failed to load QML interface"

    # Find ListView
    root = root_objects[0]
    list_view = root.findChild(QObject, "employeeListView")
    assert list_view is not None, "Failed to find ListView"


def test_model_data_binding(
    qapp, qml_engine, employee_model, db_handler, test_employee_data, qtbot
):
    """Test data binding between model and QML."""
    # Set context properties
    qml_engine.rootContext().setContextProperty("employeeModel", employee_model)

    # Load QML
    qml_engine.loadData(TEST_QML.encode())
    qtbot.wait(100)

    # Get ListView
    root = qml_engine.rootObjects()[0]
    list_view = root.findChild(QObject, "employeeListView")
    assert list_view is not None, "Failed to find ListView"

    # Initial count
    initial_count = list_view.property("count")

    # Add employee
    employee = EmployeeData(**test_employee_data)
    db_handler.add_employee(employee)
    employee_model.refresh()

    # Wait for model update
    qtbot.wait(100)

    # Verify count increased
    updated_count = list_view.property("count")
    assert updated_count == initial_count + 1, "ListView not updated with new employee"


def test_model_filtering(
    qapp, qml_engine, employee_model, db_handler, test_employee_data, qtbot
):
    """Test model filtering in QML."""
    # Set context properties
    qml_engine.rootContext().setContextProperty("employeeModel", employee_model)

    # Load QML
    qml_engine.loadData(TEST_QML.encode())
    qtbot.wait(100)

    # Get ListView
    root = qml_engine.rootObjects()[0]
    list_view = root.findChild(QObject, "employeeListView")

    # Add test employee
    employee = EmployeeData(**test_employee_data)
    db_handler.add_employee(employee)
    employee_model.refresh()
    qtbot.wait(100)

    # Test filtering
    employee_model.filterText = "Test Employee"
    qtbot.wait(100)
    assert list_view.property("count") == 1

    # Clear filter
    employee_model.filterText = ""
    qtbot.wait(100)
    assert list_view.property("count") > 0


def test_mainapp_integration(qapp, qml_engine, db_handler, qtbot):
    """Test MainApp integration with QML."""
    # Create MainApp instance
    main_app = MainApp(db_handler=db_handler)
    model = EmployeeModel(database=db_handler.db)

    # Set context properties
    qml_engine.rootContext().setContextProperty("mainApp", main_app)
    qml_engine.rootContext().setContextProperty("employeeModel", model)

    # Load QML
    qml_engine.loadData(TEST_QML.encode())
    qtbot.wait(100)

    # Verify loading
    assert qml_engine.rootObjects(), "Failed to load QML"

    # Test adding employee
    success = main_app.add_employee(
        name="Integration Test",
        position="Tester",
        email="test@integration.com",
        phone="999-999",
        department="QA",
    )

    assert success, "Failed to add employee through MainApp"

    # Verify model updated
    qtbot.wait(100)
    root = qml_engine.rootObjects()[0]
    list_view = root.findChild(QObject, "employeeListView")
    assert list_view.property("count") > 0, "Model not updated after adding employee"


if __name__ == "__main__":
    pytest.main([__file__])
