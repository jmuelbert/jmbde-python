from database import Database
import pytest


@pytest.fixture
def db():
    """Fixture for a fresh database instance."""
    return Database(":memory:")


def test_create_tables(db):
    """Test if tables are created successfully."""
    cursor = db.connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]
    assert "employees" in tables
    assert "devices" in tables


def test_add_employee(db):
    """Test adding an employee."""
    emp_id = db.add_employee("John Doe", "Developer")
    assert emp_id > 0


def test_get_employees(db):
    """Test retrieving employees."""
    db.add_employee("Alice", "Manager")
    db.add_employee("Bob", "Developer")
    employees = db.get_employees()
    assert len(employees) == 2


def test_update_employee(db):
    """Test updating an employee."""
    emp_id = db.add_employee("Charlie", "Designer")
    db.update_employee(emp_id, "Charlie Updated", "Lead Designer")
    employees = db.get_employees()
    assert employees[0][1] == "Charlie Updated"
    assert employees[0][2] == "Lead Designer"


def test_delete_employee(db):
    """Test deleting an employee."""
    emp_id = db.add_employee("Dave", "Tester")
    db.delete_employee(emp_id)
    employees = db.get_employees()
    assert len(employees) == 0
