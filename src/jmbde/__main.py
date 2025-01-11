#!/usr/bin/env python3

"""JMBDE - Business Data Management Application

This is the main entry point for the JMBDE application, a comprehensive tool
for managing business data and employee information.

Copyright (C) 2018-2024 Jürgen Mülbert

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

import logging
from pathlib import Path
import sys
from typing import Optional

import click
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine

from jmbde.core.database import Database, DatabaseError
from jmbde.core.settings import Settings
from jmbde.gui.employee_model import EmployeeModel
from jmbde.gui.main_app import MainApp
from jmbde.utils.exceptions import ApplicationError
from jmbde.utils.logger import setup_logging

# Initialize logging
logger = logging.getLogger(__name__)


class JMBDEApplication:
    """Main application class for JMBDE."""

    def __init__(self) -> None:
        """Initialize the JMBDE application."""
        self.app: Optional[QGuiApplication] = None
        self.engine: Optional[QQmlApplicationEngine] = None
        self.database: Optional[Database] = None
        self.employee_model: Optional[EmployeeModel] = None
        self.main_app: Optional[MainApp] = None
        self.settings: Optional[Settings] = None

    def initialize_logging(self) -> None:
        """Set up application logging."""
        try:
            log_dir = Path.home() / ".jmbde" / "logs"
            log_dir.mkdir(parents=True, exist_ok=True)
            setup_logging(log_dir / "jmbde.log")
            logger.info("Logging initialized successfully")
        except Exception as e:
            print(f"Failed to initialize logging: {e}", file=sys.stderr)
            sys.exit(1)

    def setup_application(self) -> None:
        """Initialize Qt application and settings."""
        try:
            # Set application metadata
            QCoreApplication.setOrganizationName("JM")
            QCoreApplication.setOrganizationDomain("jmuelbert.de")
            QCoreApplication.setApplicationName("JMBDE")

            # Initialize Qt application
            self.app = QGuiApplication(sys.argv)
            self.app.setWindowIcon(QIcon(":/images/jmbde-logo.png"))

            # Load settings
            self.settings = Settings()
            self.settings.load()

            logger.info("Application setup completed successfully")
        except Exception as e:
            logger.critical(f"Failed to setup application: {e}")
            raise ApplicationError("Application initialization failed") from e

    def initialize_database(self) -> None:
        """Initialize the database connection."""
        try:
            self.database = Database()
            # self.database.initialize()
            logger.info("Database initialized successfully")
        except DatabaseError as e:
            logger.error(f"Database initialization failed: {e}")
            raise ApplicationError("Failed to initialize database") from e

    def setup_models(self) -> None:
        """Initialize data models."""
        try:
            self.employee_model = EmployeeModel(self.database)
            self.main_app = MainApp(self.database, self.employee_model)
            logger.info("Models initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize models: {e}")
            raise ApplicationError("Model initialization failed") from e

    def setup_qml_engine(self) -> None:
        """Initialize QML engine and load main interface."""
        try:
            self.engine = QQmlApplicationEngine()

            # Register context properties
            context = self.engine.rootContext()
            context.setContextProperty("employeeModel", self.employee_model)
            context.setContextProperty("mainApp", self.main_app)
            context.setContextProperty("settings", self.settings)

            # Load main QML file
            qml_path = Path(__file__).parent / "qml" / "main.qml"
            self.engine.load(str(qml_path.resolve()))

            if not self.engine.rootObjects():
                raise ApplicationError("Failed to load QML interface")

            logger.info("QML engine initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize QML engine: {e}")
            raise ApplicationError("QML initialization failed") from e

    def cleanup(self) -> None:
        """Perform cleanup operations before exit."""
        try:
            if self.database:
                self.database.close()
            if self.settings:
                self.settings.save()
            logger.info("Application cleanup completed successfully")
        except Exception as e:
            logger.error(f"Cleanup failed: {e}")


@click.command()
@click.version_option()
@click.option("--debug", is_flag=True, help="Enable debug mode")
@click.option("--config", type=click.Path(), help="Path to configuration file")
def main(debug: bool, config: Optional[str]) -> None:
    """JMBDE - Business Data Management Application.

    A comprehensive tool for managing business data and employee information.
    """
    jmbde = JMBDEApplication()

    try:
        # Initialize application
        jmbde.initialize_logging()

        if debug:
            logging.getLogger().setLevel(logging.DEBUG)
            logger.debug("Debug mode enabled")

        logger.info("Starting JMBDE application")

        # Setup application components
        jmbde.setup_application()
        jmbde.initialize_database()
        jmbde.setup_models()
        jmbde.setup_qml_engine()

        # Run application
        exit_code = jmbde.app.exec()

        # Cleanup and exit
        jmbde.cleanup()
        sys.exit(exit_code)

    except ApplicationError as e:
        logger.critical(f"Application failed to start: {e}")
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        logger.critical(f"Unexpected error: {e}", exc_info=True)
        click.echo(
            "Fatal Error: An unexpected error occurred. Check logs for details.",
            err=True,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
