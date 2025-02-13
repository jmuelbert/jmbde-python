import sys
from pathlib import Path
from unittest.mock import MagicMock, Mock, call, patch

import pytest
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from jmbde.__main__ import main, parse_args
from jmbde.core.db_handler import DBHandler

# Test QML content
TEST_QML = """
import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "JMBDE Test"
}
"""


@pytest.fixture
def temp_db_path(tmp_path):
    """Provide temporary database path."""
    return tmp_path / "test.db"


@pytest.fixture
def mock_engine():
    """Mock QQmlApplicationEngine."""
    with patch("PySide6.QtQml.QQmlApplicationEngine", autospec=True) as MockEngine:
        engine = MockEngine.return_value
        engine.rootObjects = Mock(return_value=[Mock()])
        engine.quit = Mock()
        yield engine


@pytest.fixture
def mock_app():
    """Mock QGuiApplication."""
    with patch("PySide6.QtGui.QGuiApplication", autospec=True) as MockApp:
        app = MockApp.return_value
        app.exec = Mock(return_value=0)
        yield app


def test_parse_args():
    """Test argument parsing."""
    with patch("sys.argv", ["jmbde", "--db-path", "/test/path/db.sqlite"]):
        args = parse_args()
        assert args.db_path == "/test/path/db.sqlite"


def test_main_successful(temp_db_path, mock_app, mock_engine):
    """Test successful application startup."""
    with patch("sys.argv", ["jmbde", "--db-path", str(temp_db_path)]):
        with patch("sys.exit") as mock_exit:
            # Mock DBHandler and EmployeeModel
            with patch("jmbde.core.db_handler.DBHandler") as MockDBHandler:
                with patch("jmbde.models.employee.EmployeeModel") as MockEmployeeModel:
                    # Configure mock engine
                    mock_engine.rootObjects.return_value = [Mock()]

                    # Run main
                    main()

                    # Verify expected calls
                    mock_exit.assert_called_once_with(0)
                    mock_engine.load.assert_called_once_with(QUrl("qrc:/qml/main.qml"))
                    assert mock_engine.rootContext.called
                    MockDBHandler.assert_called_once_with(temp_db_path)
                    MockEmployeeModel.assert_called_once()


def test_main_qml_loading_failure(temp_db_path, mock_app, mock_engine):
    """Test handling of QML loading failure."""
    with patch("sys.argv", ["jmbde", "--db-path", str(temp_db_path)]):
        with patch("sys.exit") as mock_exit:
            # Mock DBHandler and EmployeeModel
            with patch("jmbde.core.db_handler.DBHandler") as MockDBHandler:
                with patch("jmbde.models.employee.EmployeeModel") as MockEmployeeModel:
                    # Configure mock engine for loading failure
                    mock_engine.rootObjects.return_value = []

                    # Run main
                    main()

                    # Verify expected calls
                    mock_exit.assert_called_once_with(-1)
                    mock_engine.load.assert_called_once_with(QUrl("qrc:/qml/main.qml"))


def test_main_database_error(tmp_path, mock_app, mock_engine):
    """Test handling of database initialization error."""
    invalid_path = tmp_path / "nonexistent" / "db.sqlite"
    with patch("sys.argv", ["jmbde", "--db-path", str(invalid_path)]):
        with patch("sys.exit") as mock_exit:
            main()
            mock_exit.assert_called_once_with(1)


class TestMainIntegration:
    """Integration tests for main application."""

    def test_application_setup(self, temp_db_path, qapp, qtbot):
        """Test full application setup without running event loop."""
        db_handler = DBHandler(temp_db_path)
        engine = QQmlApplicationEngine()

        try:
            # Set up QML context
            engine.rootContext().setContextProperty("dbHandler", db_handler)

            # Load test QML
            engine.loadData(TEST_QML.encode())

            # Wait for QML loading
            qtbot.wait(100)

            # Verify components
            assert engine.rootObjects(), "QML should load successfully"

        finally:
            db_handler.cleanup()
            engine.deleteLater()

    @pytest.mark.parametrize("db_exists", [True, False])
    def test_database_initialization(self, tmp_path, db_exists):
        """Test database initialization with and without existing database."""
        db_path = tmp_path / "test.db"

        if db_exists:
            db_path.parent.mkdir(parents=True, exist_ok=True)
            db_path.touch()

        db_handler = None
        try:
            db_handler = DBHandler(db_path)
            assert db_path.exists(), "Database file should exist"

        finally:
            if db_handler:
                db_handler.cleanup()


if __name__ == "__main__":
    pytest.main([__file__])
