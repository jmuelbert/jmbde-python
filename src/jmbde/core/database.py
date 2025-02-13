import logging
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Generator, Optional, Union

from jmbde.core.config import Config
from jmbde.utils.exceptions import DatabaseError

logger = logging.getLogger(__name__)


class Database:
    """Database handler for JMBDE."""

    def __init__(self, db_path: Union[str, Path] = Config.DATABASE_PATH):
        """Initialize database connection."""
        try:
            self.db_path = Path(db_path)
            self.db_path.parent.mkdir(parents=True, exist_ok=True)

            self.connection = sqlite3.connect(
                str(self.db_path),
                detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
                isolation_level="IMMEDIATE",
            )
            self.connection.row_factory = sqlite3.Row

            self._create_tables()
            logger.info(f"Database initialized successfully at {self.db_path}")

        except sqlite3.Error as e:
            logger.error(f"Failed to initialize database: {e}")
            raise DatabaseError(f"Database initialization failed: {e}")
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            raise DatabaseError(f"Database initialization failed: {e}")

    @contextmanager
    def transaction(self):
        """Provide transaction context."""
        cursor = None
        try:
            cursor = self.connection.cursor()
            yield cursor
            self.connection.commit()
        except sqlite3.Error as e:
            if self.connection:
                try:
                    self.connection.rollback()
                except sqlite3.Error as rollback_error:
                    logger.error(f"Failed to rollback transaction: {rollback_error}")
                    raise DatabaseError(
                        f"Failed to rollback transaction: {rollback_error}"
                    )
            raise DatabaseError(f"Transaction failed: {e}")
        except Exception as e:
            if self.connection:
                self.connection.rollback()
            raise DatabaseError(f"Transaction failed: {e}")
        finally:
            if cursor:
                cursor.close()

    def close(self) -> None:
        """Close database connection."""
        if hasattr(self, "connection") and self.connection:
            try:
                self.connection.close()
            except sqlite3.Error as e:
                logger.error(f"Failed to close database connection: {e}")
                raise DatabaseError(f"Failed to close database connection: {e}")

    def _create_tables(self) -> None:
        """Create database tables."""
        try:
            with self.transaction() as cursor:
                # Create employees table
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        position TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        phone TEXT NOT NULL,
                        department TEXT NOT NULL,
                        hire_date TIMESTAMP NOT NULL,
                        active BOOLEAN DEFAULT TRUE
                    )
                """
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
                        FOREIGN KEY (employee_id) REFERENCES employees (id)
                            ON DELETE SET NULL
                    )
                """
                )
                logger.info("Database tables created successfully")
        except sqlite3.Error as e:
            logger.error(f"Failed to create tables: {e}")
            raise DatabaseError(f"Table creation failed: {e}")

    def add_employee(self, employee: "EmployeeData") -> int:
        """Add an employee to the database."""
        try:
            with self.transaction() as cursor:
                cursor.execute(
                    """
                    INSERT INTO employees
                    (name, position, email, phone, department, hire_date, active)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
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
                return cursor.lastrowid
        except Exception as e:
            logger.error(f"Failed to add employee: {e}")
            raise DatabaseError(f"Failed to add employee: {e}") from e

    def get_employee(self, employee_id: int) -> Optional[dict[str, Any]]:
        """Retrieve an employee by ID."""
        try:
            with self.transaction() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM employees WHERE id = ?
                """,
                    (employee_id,),
                )
                row = cursor.fetchone()
                return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get employee: {e}")
            raise DatabaseError(f"Failed to get employee: {e}") from e

    def get_all_employees(self) -> list[dict[str, Any]]:
        """Retrieve all employees."""
        try:
            with self.transaction() as cursor:
                cursor.execute("SELECT * FROM employees")
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get employees: {e}")
            raise DatabaseError(f"Failed to get employees: {e}") from e

    def add_device(self, device: "DeviceModel") -> int:
        """Add a device to the database.

        Args:
            device: Device model instance

        Returns:
            int: ID of the newly added device

        Raises:
            DatabaseError: If adding device fails
        """
        try:
            with self.transaction() as cursor:
                cursor.execute(
                    """
                        INSERT INTO devices
                        (employee_id, device_name, device_type, serial_number,
                         purchase_date, warranty_expires, status)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        device.employee_id,
                        device.device_name,
                        device.device_type,
                        device.serial_number,
                        device.purchase_date,
                        device.warranty_expires,
                        device.status.value,
                    ),
                )
                return cursor.lastrowid
        except Exception as e:
            logger.error(f"Failed to add device: {e}")
            raise DatabaseError(f"Failed to add device: {e}") from e

    def get_device(self, device_id: int) -> Optional[dict[str, Any]]:
        """Retrieve a device by ID.

        Args:
            device_id: ID of the device to retrieve

        Returns:
            Optional[dict]: Device data if found, None otherwise

        Raises:
            DatabaseError: If retrieving device fails
        """
        try:
            with self.transaction() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM devices WHERE id = ?
                    """,
                    (device_id,),
                )
                row = cursor.fetchone()
                return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get device: {e}")
            raise DatabaseError(f"Failed to get device: {e}") from e

    def update_device(self, device: "DeviceModel") -> bool:
        """Update a device in the database.

        Args:
            device: Device model instance with updated data

        Returns:
            bool: True if update successful, False otherwise

        Raises:
            DatabaseError: If updating device fails
        """
        try:
            with self.transaction() as cursor:
                cursor.execute(
                    """
                    UPDATE devices
                    SET employee_id = ?,
                        device_name = ?,
                        device_type = ?,
                        serial_number = ?,
                        purchase_date = ?,
                        warranty_expires = ?,
                        status = ?
                    WHERE id = ?
                    """,
                    (
                        device.employee_id,
                        device.device_name,
                        device.device_type,
                        device.serial_number,
                        device.purchase_date,
                        device.warranty_expires,
                        device.status.value,
                        device.id,
                    ),
                )
                return cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Failed to update device: {e}")
            raise DatabaseError(f"Failed to update device: {e}") from e

    def get_all_devices(self) -> list[dict[str, Any]]:
        """Retrieve all devices.

        Returns:
            list[dict]: List of all devices

        Raises:
            DatabaseError: If retrieving devices fails
        """
        try:
            with self.transaction() as cursor:
                cursor.execute("SELECT * FROM devices")
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get devices: {e}")
            raise DatabaseError(f"Failed to get devices: {e}") from e

    def delete_device(self, device_id: int) -> bool:
        """Delete a device from the database.

        Args:
            device_id: ID of the device to delete

        Returns:
            bool: True if deletion successful, False otherwise

        Raises:
            DatabaseError: If deleting device fails
        """
        try:
            with self.transaction() as cursor:
                cursor.execute("DELETE FROM devices WHERE id = ?", (device_id,))
                return cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Failed to delete device: {e}")
            raise DatabaseError(f"Failed to delete device: {e}") from e
