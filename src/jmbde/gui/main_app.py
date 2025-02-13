import logging
from datetime import datetime

from pydantic import ValidationError
from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QGuiApplication

from jmbde.models.employee import EmployeeData
from jmbde.utils.exceptions import DatabaseError

logger = logging.getLogger(__name__)


class MainApp(QObject):
    """Main application logic handler."""

    errorOccurred = Signal(str)
    employeeAdded = Signal(int, str)

    def __init__(self, db_handler, parent=None):
        """Initialize MainApp."""
        super().__init__(parent)
        self._db_handler = db_handler
        self._operation_in_progress = False

    def add_employee(
        self, name: str, position: str, email: str, phone: str, department: str
    ) -> bool:
        """Add new employee."""
        if self._operation_in_progress:
            error_msg = "Operation already in progress"
            logger.warning(error_msg)
            self.errorOccurred.emit(error_msg)
            return False

        self._operation_in_progress = True
        try:
            # Validate input
            if not name.strip():
                raise ValueError("Name cannot be empty")

            employee = EmployeeData(
                name=name,
                position=position,
                email=email,
                phone=phone,
                department=department,
                hire_date=datetime.now(),
                active=True,
            )

            # Add to database
            employee_id = self._db_handler.add_employee(employee)
            if employee_id:
                self.employeeAdded.emit(employee_id, name)
                return True
            return False

        except (ValueError, ValidationError) as e:
            error_msg = str(e)
            logger.error(f"Validation error: {error_msg}")
            self.errorOccurred.emit(error_msg)
            raise
        except DatabaseError as e:
            error_msg = str(e)
            logger.error(f"Database error: {error_msg}")
            self.errorOccurred.emit(error_msg)
            return False
        except Exception as e:
            error_msg = f"Unexpected error: {e}"
            logger.error(error_msg)
            self.errorOccurred.emit(error_msg)
            return False
        finally:
            self._operation_in_progress = False

    def cleanup(self) -> None:
        """Clean up resources and connections."""
        logger.info("Cleaning up MainApp resources")
        try:
            self._operation_in_progress = False

            if hasattr(self, "_db_handler") and self._db_handler:
                self._db_handler.cleanup()
                self._db_handler = None  # Remove reference

            # Disconnect signals
            self.errorOccurred.disconnect()
            self.employeeAdded.disconnect()

            # Ensure QApplication is properly cleaned up
            app = QGuiApplication.instance()
            if app is not None:
                app.quit()

            # Ensure QObject is deleted
            self.deleteLater()

        except Exception as e:
            logger.error(f"Error during cleanup: {e}")
