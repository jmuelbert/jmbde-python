from datetime import datetime
from unittest.mock import Mock, patch

import pytest
from PySide6.QtCore import QObject
from PySide6.QtWidgets import (  # Verwendung von QApplication statt QGuiApplication
    QApplication,
)

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


@pytest.fixture(scope="session")
def qapp():
    """Provide QApplication instance."""
    app = QApplication.instance() or QApplication([])
    yield app  # Kein explizites Quit, pytest-qt verwaltet dies


@pytest.fixture
def db_handler(tmp_path):
    """Provide database handler."""
    handler = DBHandler(tmp_path / "test.db")
    yield handler
    handler.cleanup()


@pytest.fixture
def main_app(db_handler):
    """Provide MainApp instance."""
    app = MainApp(db_handler=db_handler)
    yield app
    app.cleanup()


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
            main_app.employeeAdded.disconnect(handle_added)

    def test_cleanup(self, main_app):
        """Test cleanup functionality."""
        main_app._operation_in_progress = True
        main_app.cleanup()
        assert not main_app._operation_in_progress


class TestMainAppError:
    """Test MainApp error handling."""

    def test_add_employee_database_failure(self):
        """Test handling of database failures."""
        mock_db_handler = Mock(spec=DBHandler)
        mock_db_handler.add_employee = Mock(
            side_effect=DatabaseError("Test database error")
        )

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
            app.errorOccurred.disconnect(handle_error)


class TestMainAppIntegration:
    """Integration tests for MainApp."""

    def test_full_workflow(self, main_app, db_handler, qapp):
        """Test complete workflow."""
        signals_received = []

        def handle_added(emp_id, name):
            signals_received.append(("added", emp_id, name))

        main_app.employeeAdded.connect(handle_added)

        try:
            success = main_app.add_employee(**VALID_EMPLOYEE_DATA)
            assert success, "Should successfully add employee"
            assert len(signals_received) == 1, "Should emit employeeAdded signal"

            employees = db_handler.get_all_employees()
            assert any(
                emp.name == VALID_EMPLOYEE_DATA["name"]
                and emp.email == VALID_EMPLOYEE_DATA["email"]
                for emp in employees
            ), "Employee not found in database"
        finally:
            main_app.employeeAdded.disconnect(handle_added)


def test_concurrent_operations(main_app):
    """Test handling of concurrent operations."""
    signals_received = []

    def handle_error(msg):
        signals_received.append(("error", msg))

    main_app.errorOccurred.connect(handle_error)

    try:
        main_app._operation_in_progress = True
        success = main_app.add_employee(**VALID_EMPLOYEE_DATA)
        assert not success, "Should fail when operation in progress"
        assert len(signals_received) == 1, "Should emit error signal"
        assert "operation already in progress" in signals_received[0][1].lower()
    finally:
        main_app.errorOccurred.disconnect(handle_error)


def test_main_app_signals(main_app, qapp):
    """Test MainApp signals."""
    signals_received = []

    def handle_error(msg):
        signals_received.append(("error", msg))

    main_app.errorOccurred.connect(handle_error)

    try:
        main_app._operation_in_progress = True
        success = main_app.add_employee(**VALID_EMPLOYEE_DATA)
        assert not success, "Should fail when operation in progress"
        assert len(signals_received) == 1, "Should emit error signal"
        assert signals_received[0][0] == "error"
    finally:
        main_app.errorOccurred.disconnect(handle_error)


if __name__ == "__main__":
    pytest.main([__file__])
