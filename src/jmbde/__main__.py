#!/usr/bin/env python3

"""
Main entry point for the JMBDE GUI application.
"""

import logging
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from jmbde.core.database_connection import DatabaseConnection  # Updated import
from jmbde.gui.main_app import MainApp
from jmbde.models.employee import EmployeeModel

logger = logging.getLogger(__name__)


def main():
    """Initialize and start the JMBDE GUI application."""
    logging.basicConfig(level=logging.INFO)
    logger.info("Starting JMBDE GUI application...")

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Initialize core components
    db = DatabaseConnection()
    model = EmployeeModel(db)
    main_app = MainApp(engine, model)

    engine.load("qrc:/qml/main.qml")
    if not engine.rootObjects():
        logger.error("Failed to load main QML file.")
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
