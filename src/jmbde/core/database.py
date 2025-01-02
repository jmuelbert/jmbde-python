#!/usr/bin/env python3

"""Database Management Module for JMBDE

This module provides database operations for the JMBDE application,
handling employee and device data using SQLite.

Copyright (C) 2018-2024 Jürgen Mülbert
License: GPL-3.0
"""

import logging
import sqlite3
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Any, Optional, Union

from pydantic import BaseModel

from jmbde.core.config import Config
from jmbde.utils.exceptions import DatabaseError

# Initialize logger
logger = logging.getLogger(__name__)


class EmployeeModel(BaseModel):
    """Data model for Employee records."""

    id: Optional[int]
    name: str
    position: str
    email: str
    phone: str
    department: str
    hire_date: datetime
    active: bool = True


class DeviceModel(BaseModel):
    """Data model for Device records."""

    id: Optional[int]
    employee_id: Optional[int]
    device_name: str
    device_type: str
    serial_number: str
    purchase_date: datetime
    warranty_expires: Optional[datetime]
    status: str = "active"


class Database:
    """Database management class for JMBDE application.

    Handles all database operations including CRUD operations
    for employees and devices using SQLite.
    """

    def __init__(self, db_path: Union[str, Path] = Config.DATABASE_PATH):
        """Initialize database connection and setup.

        Args:
            db_path: Path to SQLite database file

        Raises:
            DatabaseError: If database initialization fails

        """
        try:
            self.db_path = Path(db_path)
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            self.connection = sqlite3.connect(
                str(self.db_path),
                detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
            )
            self.connection.row_factory = sqlite3.Row
            self._create_tables()
            logger.info(f"Database initialized successfully at {self.db_path}")
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            raise DatabaseError(f"Database initialization failed: {e}") from e

    @contextmanager
    def transaction(self):
        """Context manager for database transactions.

        Ensures proper commit/rollback handling.
        """
        try:
            yield self.connection.cursor()
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            logger.error(f"Transaction failed: {e}")
            raise DatabaseError(f"Transaction failed: {e}") from e

    def _create_tables(self) -> None:
        """Create database tables if they don't exist.

        Creates tables for employees and devices with proper schema.
        """
        try:
            with self.transaction() as cursor:
                # Create employees table
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        position TEXT NOT NULL,
                        email TEXT UNIQUE,
                        phone TEXT,
                        department TEXT,
                        hire_date TIMESTAMP,
                        active BOOLEAN DEFAULT TRUE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """,
                )

                # Create devices table
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS devices (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        employee_id INTEGER,
                        device_name TEXT NOT NULL,
                        device_type TEXT NOT NULL,
                        serial_number TEXT UNIQUE,
                        purchase_date TIMESTAMP,
                        warranty_expires TIMESTAMP,
                        status TEXT DEFAULT 'active',
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (employee_id) REFERENCES employees (id)
                            ON DELETE SET NULL
                    )
                """,
                )

                # Create indices
                cursor.execute(
                    "CREATE INDEX IF NOT EXISTS idx_employee_name ON employees(name)",
                )
                cursor.execute(
                    "CREATE INDEX IF NOT EXISTS idx_device_serial ON devices(serial_number)",
                )

                logger.info("Database tables and indices created successfully")
        except Exception as e:
            logger.error(f"Failed to create tables: {e}")
            raise DatabaseError(f"Table creation failed: {e}") from e

    def add_employee(self, employee: EmployeeModel) -> int:
        """Add a new employee to the database.

        Args:
            employee: EmployeeModel instance containing employee data

        Returns:
            int: ID of the newly created employee record

        Raises:
            DatabaseError: If employee creation fails

        """
        try:
            with self.transaction() as cursor:
                cursor.execute(
                    """
                    INSERT INTO employees (
                        name, position, email, phone, department,
                        hire_date, active
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
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
                employee_id = cursor.lastrowid
                logger.info(f"Added employee: {employee.name} (ID: {employee_id})")
                return employee_id
        except Exception as e:
            logger.error(f"Failed to add employee {employee.name}: {e}")
            raise DatabaseError(f"Failed to add employee: {e}") from e

    def get_employee(self, employee_id: int) -> Optional[dict[str, Any]]:
        """Retrieve employee data by ID.

        Args:
            employee_id: ID of the employee to retrieve

        Returns:
            Optional[Dict]: Employee data or None if not found

        """
        try:
            with self.transaction() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM employees WHERE id = ?
                """,
                    (employee_id,),
                )
                result = cursor.fetchone()
                return dict(result) if result else None
        except Exception as e:
            logger.error(f"Failed to retrieve employee {employee_id}: {e}")
            raise DatabaseError(f"Employee retrieval failed: {e}") from e

    def get_employees(
        self,
        active_only: bool = True,
        department: Optional[str] = None,
    ) -> list[dict[str, Any]]:
        """Retrieve all employees matching the specified criteria.

        Args:
            active_only: If True, return only active employees
            department: Filter by department name

        Returns:
            List[Dict]: List of employee records

        """
        try:
            query = "SELECT * FROM employees WHERE 1=1"
            params = []

            if active_only:
                query += " AND active = ?"
                params.append(True)

            if department:
                query += " AND department = ?"
                params.append(department)

            query += " ORDER BY name"

            with self.transaction() as cursor:
                cursor.execute(query, params)
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to retrieve employees: {e}")
            raise DatabaseError(f"Employee retrieval failed: {e}") from e

    def update_employee(self, employee_id: int, data: dict[str, Any]) -> bool:
        """Update employee information.

        Args:
            employee_id: ID of the employee to update
            data: Dictionary containing fields to update

        Returns:
            bool: True if update was successful

        Raises:
            DatabaseError: If update fails

        """
        try:
            valid_fields = {
                "name",
                "position",
                "email",
                "phone",
                "department",
                "active",
            }
            update_fields = {
                k: v for k, v in data.items() if k in valid_fields and v is not None
            }

            if not update_fields:
                return False

            query = """
                UPDATE employees
                SET {}
                WHERE id = ?
            """.format(
                ", ".join(f"{field} = ?" for field in update_fields),
            )

            with self.transaction() as cursor:
                cursor.execute(query, [*update_fields.values(), employee_id])
                success = cursor.rowcount > 0
                if success:
                    logger.info(f"Updated employee {employee_id}")
                return success
        except Exception as e:
            logger.error(f"Failed to update employee {employee_id}: {e}")
            raise DatabaseError(f"Employee update failed: {e}") from e

    def delete_employee(self, employee_id: int) -> bool:
        """Delete an employee record.

        Args:
            employee_id: ID of the employee to delete

        Returns:
            bool: True if deletion was successful

        Raises:
            DatabaseError: If deletion fails

        """
        try:
            with self.transaction() as cursor:
                cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
                success = cursor.rowcount > 0
                if success:
                    logger.info(f"Deleted employee {employee_id}")
                return success
        except Exception as e:
            logger.error(f"Failed to delete employee {employee_id}: {e}")
            raise DatabaseError(f"Employee deletion failed: {e}") from e

    def cleanup(self) -> None:
        """Perform database cleanup operations.

        Closes connections and performs any necessary cleanup.
        """
        try:
            if hasattr(self, "connection") and self.connection:
                self.connection.close()
                logger.info("Database connection closed successfully")
        except Exception as e:
            logger.error(f"Database cleanup failed: {e}")
            raise DatabaseError(f"Database cleanup failed: {e}") from e

    def __enter__(self):
        """Context manager enter."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.cleanup()
