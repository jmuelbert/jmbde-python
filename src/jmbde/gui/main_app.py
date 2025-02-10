#!/usr/bin/env python3

"""
Main Application Logic Module for JMBDE

This module provides the main application logic and business operations
for the JMBDE application, serving as a bridge between the UI and data layers.

Copyright (C) 2018-2024 Jürgen Mülbert
License: GPL-3.0
"""

import logging
from datetime import datetime
from typing import Any, Optional

from PySide6.QtCore import QObject, Signal, Slot

from jmbde.core.database import Database
from jmbde.core.settings import Settings
from jmbde.models.employee import EmployeeModel
from jmbde.utils.exceptions import ApplicationError
from jmbde.utils.validators import validate_email, validate_phone

# Initialize logger
logger = logging.getLogger(__name__)


class MainApp(QObject):
    """
    Main application logic handler for JMBDE.

    Provides business logic and operations coordination between
    the UI layer and data management components.
    """

    # Define signals for application events
    employeeAdded = Signal(int, str)  # id, name
    employeeUpdated = Signal(int)  # id
    employeeDeleted = Signal(int)  # id
    errorOccurred = Signal(str)  # error message
    operationSucceeded = Signal(str)  # success message

    def __init__(
        self,
        database: Database,
        settings: Optional[Settings] = None,
        parent: Optional[QObject] = None,
    ) -> None:
        """
        Initialize the main application handler.

        Args:
        ----
            database: Database instance for data operations
            settings: Optional settings manager
            parent: Optional parent QObject

        """
        super().__init__(parent)
        self._database = database
        self._settings = settings or Settings()
        self._operation_in_progress = False
        self._model = EmployeeModel(
            database
        )  # Ensure EmployeeModel is properly instantiated

        logger.info("MainApp initialized successfully")

    @Slot(str, str, str, str, str, result=bool)
    def add_employee(
        self,
        name: str,
        position: str,
        email: str,
        phone: str,
        department: str,
    ) -> bool:
        """
        Add a new employee to the system.

        Args:
        ----
            name: Employee name
            position: Job position
            email: Email address
            phone: Phone number
            department: Department name

        Returns:
        -------
            bool: True if operation was successful

        """
        if self._operation_in_progress:
            logger.warning("Operation already in progress")
            return False

        try:
            self._operation_in_progress = True

            # Validate inputs
            if not name or not position:
                raise ValueError("Name and position are required")

            if email and not validate_email(email):
                raise ValueError("Invalid email format")

            if phone and not validate_phone(phone):
                raise ValueError("Invalid phone format")

            # Create employee record
            employee_data = {
                "name": name.strip(),
                "position": position.strip(),
                "email": email.strip() if email else None,
                "phone": phone.strip() if phone else None,
                "department": department.strip() if department else None,
                "hire_date": datetime.now(),
                "active": True,
            }

            # Add to database
            employee_id = self._database.add_employee(employee_data)

            if not employee_id:
                raise ApplicationError("Failed to create employee record")

            # Refresh model and notify
            self._model.refresh()
            self.employeeAdded.emit(employee_id, name)
            self.operationSucceeded.emit(f"Employee {name} added successfully")

            logger.info(f"Added employee: {name} (ID: {employee_id})")
            return True

        except (ValueError, ApplicationError) as e:
            logger.error(f"Failed to add employee: {e}")
            self.errorOccurred.emit(str(e))
            return False

        finally:
            self._operation_in_progress = False

    def cleanup(self) -> None:
        """Perform cleanup operations before application exit."""
        try:
            if self._database:
                self._database.cleanup()
            if self._settings:
                self._settings.save()
            logger.info("MainApp cleanup completed successfully")
        except Exception as e:
            logger.error(f"Cleanup failed: {e}")
