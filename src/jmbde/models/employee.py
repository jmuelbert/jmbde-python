import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr
from PySide6.QtCore import Property, QAbstractListModel, QModelIndex, Qt, Signal

from jmbde.utils.exceptions import DatabaseError

logger = logging.getLogger(__name__)


class EmployeeData(BaseModel):
    """Pydantic model for employee data validation."""

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
        validate_assignment=True,
    )

    id: Optional[int] = None
    name: str
    position: str
    email: EmailStr
    phone: str
    department: str
    hire_date: datetime
    active: bool = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary."""
        return self.model_dump()


class EmployeeModel(QAbstractListModel):
    """Qt Model for Employee data management."""

    ROLES = {
        Qt.UserRole + 1: b"id",
        Qt.UserRole + 2: b"name",
        Qt.UserRole + 3: b"position",
        Qt.UserRole + 4: b"email",
        Qt.UserRole + 5: b"phone",
        Qt.UserRole + 6: b"department",
        Qt.UserRole + 7: b"hire_date",
        Qt.UserRole + 8: b"active",
    }

    dataChanged = Signal()
    errorOccurred = Signal(str)

    def __init__(self, database=None, parent=None):
        """Initialize the model.

        Args:
            database: Database instance
            parent: Parent QObject
        """
        super().__init__(parent)
        self._database = database
        self._employees: List[Dict[str, Any]] = []
        self._filter_text: str = ""
        self._department_filter: Optional[str] = None

        if database:
            self.refresh()

    def refresh(self) -> None:
        """Refresh model data from database."""
        try:
            self.beginResetModel()
            if self._database:
                # Get all employees and apply filters
                all_employees = self._database.get_all_employees()
                self._employees = [
                    emp for emp in all_employees if self._matches_filters(emp)
                ]
            self.endResetModel()
            self.dataChanged.emit()
        except Exception as e:
            logger.error(f"Failed to refresh model: {e}")
            self.errorOccurred.emit(str(e))

    def _matches_filters(self, employee: Dict[str, Any]) -> bool:
        """Check if employee matches current filters.

        Args:
            employee: Employee data dictionary

        Returns:
            bool: True if employee matches filters
        """
        if not employee.get("active", True):
            return False

        if (
            self._department_filter
            and employee.get("department") != self._department_filter
        ):
            return False

        if self._filter_text:
            filter_lower = self._filter_text.lower()
            searchable_fields = [
                str(employee.get("name", "")),
                str(employee.get("position", "")),
                str(employee.get("email", "")),
            ]
            return any(filter_lower in field.lower() for field in searchable_fields)

        return True

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """Get number of rows in model."""
        return len(self._employees)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> Any:
        """Get data for specified index and role."""
        if not index.isValid() or not (0 <= index.row() < len(self._employees)):
            return None

        employee = self._employees[index.row()]

        if role == Qt.DisplayRole:
            return employee.get("name", "")

        try:
            role_name = self.ROLES.get(role, b"").decode()
            return employee.get(role_name)
        except Exception as e:
            logger.error(f"Error accessing employee data: {e}")
            return None

    def roleNames(self) -> Dict[int, bytes]:
        """Get role names for QML."""
        return self.ROLES

    @Property(str)
    def filterText(self) -> str:
        """Get current filter text."""
        return self._filter_text

    @filterText.setter
    def filterText(self, value: str) -> None:
        """Set filter text and refresh model."""
        if value != self._filter_text:
            self._filter_text = value
            self.refresh()

    @Property(str)
    def departmentFilter(self) -> Optional[str]:
        """Get current department filter."""
        return self._department_filter

    @departmentFilter.setter
    def departmentFilter(self, value: Optional[str]) -> None:
        """Set department filter and refresh model."""
        if value != self._department_filter:
            self._department_filter = value
            self.refresh()

    def addEmployee(
        self, name: str, position: str, email: str, phone: str, department: str
    ) -> bool:
        """Add new employee to the model.

        Args:
            name: Employee name
            position: Job position
            email: Email address
            phone: Phone number
            department: Department name

        Returns:
            bool: True if successful
        """
        try:
            employee = EmployeeData(
                name=name,
                position=position,
                email=email,
                phone=phone,
                department=department,
                hire_date=datetime.now(),
                active=True,
            )

            if self._database:
                self._database.add_employee(employee)
                self.refresh()
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to add employee: {e}")
            self.errorOccurred.emit(str(e))
            return False

    def removeEmployee(self, index: int) -> bool:
        """Remove employee at specified index.

        Args:
            index: Row index to remove

        Returns:
            bool: True if successful
        """
        try:
            if 0 <= index < len(self._employees):
                employee_id = self._employees[index].get("id")
                if employee_id and self._database:
                    self._database.delete_employee(employee_id)
                    self.refresh()
                    return True
            return False
        except Exception as e:
            logger.error(f"Failed to remove employee: {e}")
            self.errorOccurred.emit(str(e))
            return False
