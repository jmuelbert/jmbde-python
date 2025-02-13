from datetime import datetime

import pytest
from pydantic import ValidationError
from PySide6.QtCore import QModelIndex, Qt

from jmbde.core.db_handler import DBHandler
from jmbde.models.employee import EmployeeData, EmployeeModel

# Test data
VALID_EMPLOYEE_DATA = {
    "name": "John Doe",
    "position": "Developer",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "department": "IT",
    "hire_date": datetime.now(),
    "active": True,
}


@pytest.fixture
def db_handler(tmp_path):
    """Provide database handler."""
    handler = DBHandler(tmp_path / "test.db")
    yield handler
    handler.cleanup()


@pytest.fixture
def employee_model(db_handler):
    """Provide employee model instance."""
    model = EmployeeModel(database=db_handler.db)
    return model


def test_employee_data_valid():
    """Test valid employee data creation."""
    employee = EmployeeData(**VALID_EMPLOYEE_DATA)
    assert employee.name == VALID_EMPLOYEE_DATA["name"]
    assert employee.email == VALID_EMPLOYEE_DATA["email"]
    assert employee.active == VALID_EMPLOYEE_DATA["active"]


def test_employee_data_invalid_email():
    """Test employee creation with invalid email."""
    invalid_data = VALID_EMPLOYEE_DATA.copy()
    invalid_data["email"] = "invalid-email"

    with pytest.raises(ValidationError) as exc_info:
        EmployeeData(**invalid_data)
    assert "email" in str(exc_info.value)


def test_employee_model_initialization(employee_model):
    """Test employee model initialization."""
    assert employee_model is not None
    assert employee_model.rowCount() == 0


def test_employee_model_add_employee(employee_model, db_handler):
    """Test adding employee to model."""
    # Create and add employee
    employee = EmployeeData(**VALID_EMPLOYEE_DATA)
    db_handler.add_employee(employee)

    # Refresh model and verify
    employee_model.refresh()
    assert employee_model.rowCount() == 1

    # Verify data
    index = employee_model.index(0, 0)
    assert employee_model.data(index, Qt.DisplayRole) == VALID_EMPLOYEE_DATA["name"]


def test_employee_model_filtering(employee_model, db_handler):
    """Test employee model filtering."""
    # Add test employees
    employees = [
        EmployeeData(
            name=f"Employee {i}",
            position="Developer",
            email=f"emp{i}@example.com",
            phone="123-456",
            department="IT",
            hire_date=datetime.now(),
            active=True,
        )
        for i in range(3)
    ]

    for emp in employees:
        db_handler.add_employee(emp)

    employee_model.refresh()
    assert employee_model.rowCount() == 3

    # Test name filter
    employee_model.filterText = "Employee 1"
    assert employee_model.rowCount() == 1

    # Test department filter
    employee_model.filterText = ""
    employee_model.departmentFilter = "IT"
    assert employee_model.rowCount() == 3


def test_employee_model_data_roles(employee_model, db_handler):
    """Test employee model data roles."""
    employee = EmployeeData(**VALID_EMPLOYEE_DATA)
    db_handler.add_employee(employee)
    employee_model.refresh()

    index = employee_model.index(0, 0)

    # Test different roles
    assert employee_model.data(index, Qt.DisplayRole) == VALID_EMPLOYEE_DATA["name"]
    role_names = employee_model.roleNames()
    assert any(b"name" in role for role in role_names.values())


def test_employee_model_invalid_index(employee_model):
    """Test handling of invalid model index."""
    invalid_index = employee_model.index(999, 0)
    assert employee_model.data(invalid_index, Qt.DisplayRole) is None


def test_employee_model_refresh(employee_model, db_handler):
    """Test model refresh functionality."""
    # Add employee
    employee = EmployeeData(**VALID_EMPLOYEE_DATA)
    db_handler.add_employee(employee)

    # Before refresh
    assert employee_model.rowCount() == 0

    # After refresh
    employee_model.refresh()
    assert employee_model.rowCount() == 1


@pytest.mark.parametrize(
    "filter_text,expected_count",
    [
        ("John", 1),
        ("Developer", 1),
        ("Nonexistent", 0),
        ("", 1),
    ],
)
def test_employee_model_filter_scenarios(
    employee_model, db_handler, filter_text, expected_count
):
    """Test various filtering scenarios."""
    # Add test data
    employee = EmployeeData(**VALID_EMPLOYEE_DATA)
    db_handler.add_employee(employee)
    employee_model.refresh()

    # Apply filter and verify
    employee_model.filterText = filter_text
    assert employee_model.rowCount() == expected_count


def test_employee_model_department_filter(employee_model, db_handler):
    """Test department filtering."""
    # Add employees in different departments
    departments = ["IT", "HR", "IT"]
    for i, dept in enumerate(departments):
        employee = EmployeeData(
            name=f"Employee {i}",
            position="Developer",
            email=f"emp{i}@example.com",
            phone="123-456",
            department=dept,
            hire_date=datetime.now(),
            active=True,
        )
        db_handler.add_employee(employee)

    employee_model.refresh()

    # Test IT department filter
    employee_model.departmentFilter = "IT"
    assert employee_model.rowCount() == 2

    # Test HR department filter
    employee_model.departmentFilter = "HR"
    assert employee_model.rowCount() == 1


if __name__ == "__main__":
    pytest.main([__file__])
