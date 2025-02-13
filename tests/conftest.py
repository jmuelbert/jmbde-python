import sys

import pytest
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


@pytest.fixture(scope="session")
def qapp():
    """Provide a single QGuiApplication instance for all tests."""
    app = QGuiApplication.instance()
    if app is None:
        app = QGuiApplication(sys.argv)

    yield app  # Provide to tests

    # Ensure proper cleanup
    app.quit()
    del app


@pytest.fixture
def qml_engine(qapp):
    """Provide QML engine instance."""
    engine = QQmlApplicationEngine()
    yield engine

    # Ensure proper cleanup
    engine.clearComponentCache()
    engine.deleteLater()
    engine = None  # Ensure engine is completely destroyed
