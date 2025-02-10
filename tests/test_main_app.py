# test_main_app.py
import unittest
from unittest.mock import MagicMock, patch

from jmbde.gui.main_app import MainApp


class TestMainApp(unittest.TestCase):
    @patch("jmbde.gui.main_app.EmployeeModel")
    @patch("jmbde.gui.main_app.logging")
    def setUp(self, mock_logging, mock_employee_model):
        self.mock_database = MagicMock()
        self.app = MainApp(database=self.mock_database)

    def test_add_employee_success(self):
        self.mock_database.add_employee.return_value = 1  # Simulate successful addition
        result = self.app.add_employee(
            "John Doe", "Developer", "john@example.com", "1234567890", "IT"
        )
        self.assertTrue(result)
        self.app.employeeAdded.emit.assert_called_with(1, "John Doe")

    def test_add_employee_invalid_email(self):
        result = self.app.add_employee(
            "John Doe", "Developer", "invalid-email", "1234567890", "IT"
        )
        self.assertFalse(result)
        self.app.errorOccurred.emit.assert_called_with("Invalid email format")

    def test_add_employee_operation_in_progress(self):
        self.app._operation_in_progress = True
        result = self.app.add_employee(
            "John Doe", "Developer", "john@example.com", "1234567890", "IT"
        )
        self.assertFalse(result)

    def test_cleanup(self):
        with patch("jmbde.gui.main_app.Settings") as mock_settings:
            self.app.cleanup()
            self.mock_database.cleanup.assert_called_once()
            mock_settings.return_value.save.assert_called_once()


if __name__ == "__main__":
    unittest.main()
