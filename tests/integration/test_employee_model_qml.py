import logging
import sys
from datetime import datetime
from pathlib import Path

import pytest
from PySide6.QtCore import QModelIndex, Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from jmbde.core.db_handler import DBHandler
from jmbde.models.employee import EmployeeData, EmployeeModel

# Test data
TEST_EMPLOYEES = [
    {
        "name": "Alice Smith",
        "position": "Developer",
        "email": "alice@example.com",
        "phone": "123-456",
        "department": "IT",
        "hire_date": datetime.now(),
        "active": True,
    },
    {
        "name": "Bob Johnson",
        "position": "Designer",
        "email": "bob@example.com",
        "phone": "789-012",
        "department": "Design",
        "hire_date": datetime.now(),
        "active": True,
    },
]


@pytest.fixture(scope="session")
def qapp():
    """Provide QGuiApplication instance."""
    app = QGuiApplication.instance()
    if app is None:
        app = QGuiApplication(sys.argv)
    return app


@pytest.fixture
def db_handler(tmp_path):
    """Provide database handler with test data."""
    handler = DBHandler(tmp_path / "test.db")

    # Initialize test data
    for emp_data in TEST_EMPLOYEES:
        employee = EmployeeData(**emp_data)
        handler.add_employee(employee)

    yield handler
    handler.cleanup()


@pytest.fixture
def employee_model(db_handler):
    """Provide employee model."""
    model = EmployeeModel(database=db_handler.db)
    model.refresh()  # Explicitly refresh the model
    return model


def test_model_initialization(employee_model):
    """Test model initialization."""
    assert employee_model.rowCount() == len(TEST_EMPLOYEES)


def test_model_data_access(employee_model):
    """Test data access from model."""
    index = employee_model.index(0, 0)
    name = employee_model.data(
        index, employee_model.ROLES[Qt.UserRole + 2]
    )  # Name role
    assert (
        name == TEST_EMPLOYEES[0]["name"]
    ), f"Expected {TEST_EMPLOYEES[0]['name']}, got {name}"


def test_model_filtering(employee_model):
    """Test model filtering."""
    # Test name filter
    employee_model.filterText = "Alice"
    assert employee_model.rowCount() == 1

    # Clear filter
    employee_model.filterText = ""
    assert employee_model.rowCount() == len(TEST_EMPLOYEES)
