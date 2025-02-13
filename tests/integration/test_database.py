import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any

import pytest

from jmbde.core.database import Database
from jmbde.models.employee import EmployeeData
from jmbde.utils.exceptions import DatabaseError

# Test data
TEST_EMPLOYEE_DATA = {
    "name": "John Doe",
    "position": "Developer",
    "email": "john.doe@example.com",
    "phone": "123-456",
    "department": "IT",
    "hire_date": datetime.now(),
    "active": True,
}


@pytest.fixture
def test_db(tmp_path: Path) -> Database:
    """Create a temporary test database."""
    db = Database(tmp_path / "test.db")
    yield db
    if hasattr(db, "connection") and db.connection:
        db.connection.close()


def get_employee_by_id(db: Database, emp_id: int) -> dict[str, Any]:
    """Retrieve employee record by ID."""
    with db.transaction() as cursor:
        cursor.execute(
            """
            SELECT id, name, position, email, phone, department, 
                   hire_date, active
            FROM employees 
            WHERE id = ?
        """,
            (emp_id,),
        )
        row = cursor.fetchone()
        return dict(row) if row else None


def test_database_creation(test_db: Database) -> None:
    """Test database initialization and file creation."""
    assert test_db.db_path.exists(), "Database file was not created"

    # Verify tables exist
    with test_db.transaction() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = {row["name"] for row in cursor.fetchall()}
        assert "employees" in tables, "Employees table not created"
        assert "devices" in tables, "Devices table not created"


def test_add_employee_integration(test_db: Database) -> None:
    """Test employee record insertion and verification."""
    # Create and add employee
    employee = EmployeeData(**TEST_EMPLOYEE_DATA)
    emp_id = test_db.add_employee(employee)

    assert emp_id > 0, "Failed to add employee"

    # Verify database record
    record = get_employee_by_id(test_db, emp_id)
    assert record is not None, "Employee record not found"
    assert record["name"] == TEST_EMPLOYEE_DATA["name"], "Employee name mismatch"
    assert record["email"] == TEST_EMPLOYEE_DATA["email"], "Employee email mismatch"


def test_employee_update(test_db: Database) -> None:
    """Test updating employee record."""
    # Add initial employee
    employee = EmployeeData(**TEST_EMPLOYEE_DATA)
    emp_id = test_db.add_employee(employee)

    # Update employee name
    new_name = "Updated Name"
    with test_db.transaction() as cursor:
        cursor.execute("UPDATE employees SET name = ? WHERE id = ?", (new_name, emp_id))

    # Verify update
    record = get_employee_by_id(test_db, emp_id)
    assert record is not None, "Employee record not found"
    assert record["name"] == new_name, "Employee name not updated"


def test_get_all_employees(test_db: Database) -> None:
    """Test retrieving all employees."""
    # Add multiple employees
    employees = []
    for i in range(3):
        emp_data = TEST_EMPLOYEE_DATA.copy()
        emp_data["name"] = f"Employee {i}"
        emp_data["email"] = f"emp{i}@example.com"
        employee = EmployeeData(**emp_data)
        emp_id = test_db.add_employee(employee)
        employees.append(emp_id)

    # Retrieve all employees
    with test_db.transaction() as cursor:
        cursor.execute("SELECT * FROM employees")
        records = cursor.fetchall()

    assert len(records) >= len(employees), "Not all employees retrieved"


def test_employee_delete(test_db: Database) -> None:
    """Test deleting employee record."""
    # Add employee
    employee = EmployeeData(**TEST_EMPLOYEE_DATA)
    emp_id = test_db.add_employee(employee)

    # Delete employee
    with test_db.transaction() as cursor:
        cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))

    # Verify deletion
    record = get_employee_by_id(test_db, emp_id)
    assert record is None, "Employee record still exists"


if __name__ == "__main__":
    pytest.main([__file__])
