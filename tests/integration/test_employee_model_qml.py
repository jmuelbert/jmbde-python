#!/usr/bin/env python3
"""
Integration test for the EmployeeModel in a QML interface.
The test loads minimal QML code that uses the EmployeeModel as a context property
and checks if the number of ListView items (count) matches the rowCount() method of the model.
"""

import sys

import pytest
from PySide6.QtCore import QObject, QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


# Dummy database simulating the behavior of the real database.
class DummyDatabase:
    def __init__(self):
        self.employees = [
            {
                "id": 1,
                "name": "Alice",
                "position": "Developer",
                "email": "alice@example.com",
                "phone": "111-222",
                "department": "IT",
                "hire_date": "2020-01-01",
                "active": True,
            },
            {
                "id": 2,
                "name": "Bob",
                "position": "Tester",
                "email": "bob@example.com",
                "phone": "333-444",
                "department": "QA",
                "hire_date": "2020-02-01",
                "active": True,
            },
            {
                "id": 3,
                "name": "Charlie",
                "position": "Manager",
                "email": "charlie@example.com",
                "phone": "555-666",
                "department": "IT",
                "hire_date": "2020-03-01",
                "active": False,
            },
        ]

    def get_employees(self, active_only=True, department=None):
        employees = self.employees
        if active_only:
            employees = [emp for emp in employees if emp.get("active", True)]
        if department:
            employees = [
                emp for emp in employees if emp.get("department") == department
            ]
        return employees

    def update_employee(self, employee_id, data):
        return True

    def add_employee(self, employee_data):
        new_id = len(self.employees) + 1
        employee_data["id"] = new_id
        self.employees.append(employee_data)
        return new_id

    def delete_employee(self, employee_id):
        for emp in self.employees:
            if emp["id"] == employee_id:
                self.employees.remove(emp)
                return True
        return False


# Ensure a QGuiApplication exists.
@pytest.fixture(scope="session", autouse=True)
def app_qml():
    app = QGuiApplication.instance()
    if not app:
        app = QGuiApplication(sys.argv)  # Create a QGuiApplication if none exists
    return app


@pytest.fixture
def dummy_db():
    return DummyDatabase()


@pytest.fixture
def employee_model(dummy_db):
    from jmbde.gui.employee_model import EmployeeModel

    model = EmployeeModel(dummy_db)
    model.refresh()  # Load initial data (only active employees)
    return model


def test_employee_model_in_qml(app_qml, employee_model, qtbot):
    """
    Loads minimal QML code that displays a ListView with the EmployeeModel,
    and checks if the number of entries in the ListView matches the rowCount of the model.
    """
    engine = QQmlApplicationEngine()

    # Set the EmployeeModel as a ContextProperty for QML access.
    engine.rootContext().setContextProperty("employeeModel", employee_model)

    # Minimal QML code that includes a ListView.
    qml_code = b"""
import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 300; height: 300
    ListView {
        id: listView
        anchors.fill: parent
        model: employeeModel
    }
}
"""
    # Load the QML code and handle potential errors.
    engine.loadData(qml_code)
    if engine.rootObjects().isEmpty():
        raise RuntimeError("Failed to load QML code.")

    # Wait briefly to allow the QML engine to load the code.
    qtbot.wait(500)

    root_objects = engine.rootObjects()
    assert len(root_objects) > 0, "The QML interface did not load."

    # Find the ListView object in the QML hierarchy.
    listView = root_objects[0].findChild(QObject, "listView")
    assert listView is not None, "ListView was not found in the QML interface."

    # Get the count of items in the ListView.
    qml_count = listView.property("count")
    expected_count = employee_model.rowCount()  # Should be 2 (active employees)

    assert (
        qml_count == expected_count
    ), f"Expected {expected_count} entries in the ListView, but found: {qml_count}"

    # Additional test: Add a new employee and check if the ListView updates.
    new_employee = {
        "name": "David",
        "position": "Designer",
        "email": "david@example.com",
        "phone": "777-888",
        "department": "Design",
        "hire_date": "2021-01-01",
        "active": True,
    }
    dummy_db.add_employee(new_employee)  # Add a new active employee
    employee_model.refresh()  # Refresh the model to reflect the new data

    # Wait briefly to allow the QML engine to update the ListView.
    qtbot.wait(500)

    # Get the updated count of items in the ListView.
    updated_qml_count = listView.property("count")
    updated_expected_count = (
        employee_model.rowCount()
    )  # Should now be 3 (active employees)

    assert (
        updated_qml_count == updated_expected_count
    ), f"Expected {updated_expected_count} entries in the ListView after adding a new employee, but found: {updated_qml_count}"
