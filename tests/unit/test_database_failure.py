# tests/unit/test_database_failure.py

import sqlite3
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

import pytest

from jmbde.core.database import Database
from jmbde.models.employee import EmployeeData
from jmbde.utils.exceptions import DatabaseError

# Test data
TEST_EMPLOYEE_DATA = {
    "name": "Test Employee",
    "position": "Developer",
    "email": "test@example.com",
    "phone": "123-456",
    "department": "IT",
    "hire_date": datetime.now(),
    "active": True,
}


class MockCursor:
    """Mock cursor for testing."""

    def __init__(self):
        self.execute_calls = []
        self.lastrowid = 1
        self.fetchall_return = []
        self.fetchone_return = None
        self.should_raise_on_execute = False
        self._closed = False
        self._in_transaction = False

    def execute(self, query, params=()):
        if self.should_raise_on_execute:
            raise sqlite3.Error("Execute failed")
        if self._in_transaction:
            raise sqlite3.OperationalError("Nested transaction not allowed")
        self.execute_calls.append((query, params))

    def fetchall(self):
        return self.fetchall_return

    def fetchone(self):
        return self.fetchone_return

    def close(self):
        self._closed = True


class MockConnection:
    """Mock connection for testing."""

    def __init__(self):
        self._cursor = MockCursor()
        self.commit_called = False
        self.rollback_called = False
        self.closed = False
        self.should_raise_on_commit = False
        self.should_raise_on_rollback = False
        self.should_raise_on_cursor = False
        self.row_factory = None
        self._in_transaction = False

    def cursor(self):
        if self.should_raise_on_cursor:
            raise sqlite3.OperationalError("database is locked")
        if not hasattr(self, "_cursor"):
            raise sqlite3.Error("No connection")
        self._cursor._in_transaction = self._in_transaction
        return self._cursor

    def commit(self):
        if self.should_raise_on_commit:
            raise sqlite3.Error("Commit failed")
        self.commit_called = True
        self._in_transaction = False

    def rollback(self):
        if self.should_raise_on_rollback:
            raise sqlite3.Error("Rollback failed")
        self.rollback_called = True
        self._in_transaction = False

    def close(self):
        self.closed = True
        delattr(self, "_cursor")


@pytest.fixture
def mock_sqlite():
    """Provide mock sqlite3 module."""
    with patch("sqlite3.connect") as mock_connect:
        conn = MockConnection()
        mock_connect.return_value = conn
        yield mock_connect, conn


def test_transaction_without_connection():
    """Test transaction attempt without connection."""
    db = Database(Path("test.db"))
    delattr(db, "connection")  # Remove connection attribute

    with pytest.raises(DatabaseError) as exc_info:
        with db.transaction() as cursor:
            pass
    assert "No database connection available" in str(exc_info.value)


def test_transaction_rollback_failure(mock_sqlite):
    """Test transaction rollback failure."""
    mock_connect, conn = mock_sqlite

    # Create database instance
    db = Database(Path("test.db"))

    # Set up rollback to fail
    conn.should_raise_on_rollback = True

    with pytest.raises(DatabaseError) as exc_info:
        with db.transaction() as cursor:
            raise Exception("Force rollback")
    assert "Rollback failed" in str(exc_info.value)
    assert conn.rollback_called


def test_nested_transaction_handling(mock_sqlite):
    """Test nested transaction handling."""
    mock_connect, conn = mock_sqlite

    # Create database instance
    db = Database(Path("test.db"))

    # Set up nested transaction detection
    conn._in_transaction = True

    with pytest.raises(DatabaseError) as exc_info:
        with db.transaction() as cursor:
            with db.transaction() as nested_cursor:
                pass
    assert "Nested transaction not allowed" in str(exc_info.value)


# ... (keep other existing test functions)


def test_connection_state_handling(mock_sqlite):
    """Test connection state handling."""
    mock_connect, conn = mock_sqlite

    db = Database(Path("test.db"))

    # Test normal transaction
    with db.transaction() as cursor:
        assert not conn._in_transaction, "Transaction flag should be False initially"
        cursor.execute("SELECT 1")
    assert not conn._in_transaction, "Transaction flag should be False after commit"

    # Test failed transaction
    try:
        with db.transaction() as cursor:
            cursor.execute("SELECT 1")
            raise Exception("Force rollback")
    except DatabaseError:
        pass
    assert not conn._in_transaction, "Transaction flag should be False after rollback"


def test_cursor_cleanup(mock_sqlite):
    """Test cursor cleanup."""
    mock_connect, conn = mock_sqlite

    db = Database(Path("test.db"))

    with db.transaction() as cursor:
        pass
    assert conn._cursor._closed, "Cursor should be closed after transaction"


def test_transaction_isolation(mock_sqlite):
    """Test transaction isolation."""
    mock_connect, conn = mock_sqlite

    db = Database(Path("test.db"))

    # First transaction
    with db.transaction() as cursor1:
        cursor1.execute("SELECT 1")
        assert not conn._in_transaction, "Transaction should not be marked as nested"

        # Try nested transaction
        with pytest.raises(DatabaseError):
            with db.transaction() as cursor2:
                cursor2.execute("SELECT 2")


if __name__ == "__main__":
    pytest.main([__file__])
