import logging
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Optional, Union

from jmbde.core.config import Config
from jmbde.models.device import DeviceModel
from jmbde.models.employee import EmployeeModel
from jmbde.utils.exceptions import DatabaseError

logger = logging.getLogger(__name__)


class Database:
    def __init__(self, db_path: Union[str, Path] = Config.DATABASE_PATH):
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
        try:
            yield self.connection.cursor()
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            logger.error(f"Transaction failed: {e}")
            raise DatabaseError(f"Transaction failed: {e}") from e

    def _create_tables(self) -> None:
        try:
            with self.transaction() as cursor:
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
                        active BOOLEAN DEFAULT TRUE
                    )
                """
                )
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
                        FOREIGN KEY (employee_id) REFERENCES employees (id) ON DELETE SET NULL
                    )
                """
                )
                logger.info("Database tables created successfully")
        except Exception as e:
            logger.error(f"Failed to create tables: {e}")
            raise DatabaseError(f"Table creation failed: {e}") from e

    def add_employee(self, employee: EmployeeModel) -> int:
        try:
            with self.transaction() as cursor:
                cursor.execute(
                    """
                    INSERT INTO employees (name, position, email, phone, department, hire_date, active)
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

    def add_device(self, device: DeviceModel) -> int:
        try:
            with self.transaction() as cursor:
                cursor.execute(
                    """
                    INSERT INTO devices (employee_id, device_name, device_type, serial_number, purchase_date, warranty_expires, status)
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
