from datetime import datetime
from unittest.mock import Mock, patch

import pytest
from PySide6.QtCore import QObject
from PySide6.QtGui import QGuiApplication

from jmbde.core.db_handler import DBHandler
from jmbde.gui.main_app import MainApp
from jmbde.models.employee import EmployeeData
from jmbde.utils.exceptions import DatabaseError

# Test data
VALID_EMPLOYEE_DATA = {
    "name": "Test Employee",
    "position": "Developer",
    "email": "test@example.com",
    "phone": "123-456",
    "department": "IT",
}


class MockDBHandler:
    """Mock database handler for testing."""

    def __init__(self, should_fail=False):
        self.should_fail = should_fail
        self.cleanup_called = False

    def add_employee(self, employee):
        if self.should_fail:
            raise DatabaseError("Mock database error")
        return 1

    def cleanup(self):
        self.cleanup_called = True


@pytest.fixture
def mock_db_handler():
    """Provide mock database handler."""
    return MockDBHandler()


@pytest.fixture
def main_app(mock_db_handler):
    """Provide MainApp instance with mock database."""
    app = MainApp(db_handler=mock_db_handler)
    return app


class TestMainApp:
    """Test MainApp functionality."""

    def test_add_employee_success(self, main_app, qapp):
        """Test successful employee addition."""
        signals_received = []

        def handle_added(emp_id, name):
            signals_received.append(("added", emp_id, name))

        main_app.employeeAdded.connect(handle_added)

        try:
            success = main_app.add_employee(**VALID_EMPLOYEE_DATA)

            assert success, "Should succeed with valid data"
            assert len(signals_received) == 1, "Should emit employeeAdded signal"
            assert signals_received[0][0] == "added"
        finally:
            try:
                main_app.employeeAdded.disconnect(handle_added)
            except TypeError:
                pass

    def test_cleanup(self, mock_db_handler):
        """Test cleanup functionality."""
        app = MainApp(db_handler=mock_db_handler)
        app._operation_in_progress = True

        # Perform cleanup
        app.cleanup()

        # Verify cleanup
        assert not app._operation_in_progress, "Operation in progress flag not reset"
        assert mock_db_handler.cleanup_called, "Database cleanup not called"


class TestMainAppError:
    """Test MainApp error handling."""

    def test_add_employee_database_failure(self):
        """Test handling of database failures."""
        mock_db_handler = MockDBHandler(should_fail=True)
        app = MainApp(db_handler=mock_db_handler)

        signals_received = []

        def handle_error(msg):
            signals_received.append(("error", msg))

        app.errorOccurred.connect(handle_error)

        try:
            success = app.add_employee(**VALID_EMPLOYEE_DATA)

            assert not success, "Should fail on database error"
            assert len(signals_received) == 1, "Should emit error signal"
            assert "database error" in signals_received[0][1].lower()
        finally:
            try:
                app.errorOccurred.disconnect(handle_error)
            except TypeError:
                pass


def test_concurrent_operations(main_app):
    """Test handling of concurrent operations."""
    signals_received = []

    def handle_error(msg):
        signals_received.append(("error", msg))

    main_app.errorOccurred.connect(handle_error)

    try:
        # Set operation in progress
        main_app._operation_in_progress = True

        # Try concurrent operation
        success = main_app.add_employee(**VALID_EMPLOYEE_DATA)

        assert not success, "Should fail when operation in progress"
        assert len(signals_received) == 1, "Should emit error signal"
        assert "operation already in progress" in signals_received[0][1].lower()
    finally:
        try:
            main_app.errorOccurred.disconnect(handle_error)
        except TypeError:
            pass


if __name__ == "__main__":
    pytest.main([__file__])
