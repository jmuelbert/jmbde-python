import unittest
from unittest.mock import MagicMock, patch

from jmbde.core.database import (
    Database,  # Replace 'your_module' with the actual module name
)
from jmbde.models.device import DeviceModel
from jmbde.models.employee import EmployeeModel
from jmbde.utils.exceptions import DatabaseError


class TestDatabase(unittest.TestCase):

    @patch("sqlite3.connect")
    def setUp(self, mock_connect):
        # Mock the database connection and cursor
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        mock_connect.return_value = self.mock_connection
        self.mock_connection.cursor.return_value = self.mock_cursor

        # Initialize the Database instance
        self.db = Database(db_path=":memory:")  # Use in-memory database for testing

    def test_add_employee_success(self):
        # Create a mock employee
        employee = EmployeeModel(
            name="John Doe",
            position="Developer",
            email="john.doe@example.com",
            phone="1234567890",
            department="Engineering",
            hire_date="2023-01-01",
            active=True,
        )

        # Mock the cursor's lastrowid
        self.mock_cursor.lastrowid = 1

        # Call the method
        employee_id = self.db.add_employee(employee)

        # Assert that the cursor executed the correct SQL
        self.mock_cursor.execute.assert_called_once_with(
            """
            INSERT INTO employees (name, position, email, phone, department, hire_date, active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                employee.name,
                employee.position,
                employee.email,
                employee.phone,
                employee.department,
                employee.hire_date,
                employee.active,
            ),
        )
        # Assert that the returned employee ID is correct
        self.assertEqual(employee_id, 1)

    def test_add_employee_failure(self):
        # Create a mock employee
        employee = EmployeeModel(
            name="Jane Doe",
            position="Manager",
            email="jane.doe@example.com",
            phone="0987654321",
            department="HR",
            hire_date="2023-01-01",
            active=True,
        )

        # Simulate a database error
        self.mock_cursor.execute.side_effect = Exception("Database error")

        # Call the method and assert that it raises a DatabaseError
        with self.assertRaises(DatabaseError):
            self.db.add_employee(employee)

    def test_add_device_success(self):
        # Create a mock device
        device = DeviceModel(
            employee_id=1,
            device_name="Laptop",
            device_type="Computer",
            serial_number="ABC123",
            purchase_date="2023-01-01",
            warranty_expires="2024-01-01",
            status="active",
        )

        # Mock the cursor's lastrowid
        self.mock_cursor.lastrowid = 1

        # Call the method
        device_id = self.db.add_device(device)

        # Assert that the cursor executed the correct SQL
        self.mock_cursor.execute.assert_called_once_with(
            """
            INSERT INTO devices (employee_id, device_name, device_type, serial_number, purchase_date, warranty_expires, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                device.employee_id,
                device.device_name,
                device.device_type,
                device.serial_number,
                device.purchase_date,
                device.warranty_expires,
                device.status,
            ),
        )
        # Assert that the returned device ID is correct
        self.assertEqual(device_id, 1)

    def test_add_device_failure(self):
        # Create a mock device
        device = DeviceModel(
            employee_id=1,
            device_name="Tablet",
            device_type="Computer",
            serial_number="XYZ789",
            purchase_date="2023-01-01",
            warranty_expires="2024-01-01",
            status="active",
        )

        # Simulate a database error
        self.mock_cursor.execute.side_effect = Exception("Database error")

        # Call the method and assert that it raises a DatabaseError
        with self.assertRaises(DatabaseError):
            self.db.add_device(device)


if __name__ == "__main__":
    unittest.main()
