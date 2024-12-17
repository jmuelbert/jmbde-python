#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Employee Model Module for JMBDE

This module provides a Qt model for exposing employee data to QML interfaces,
implementing the necessary methods for data access and modification.

Copyright (C) 2018-2024 Jürgen Mülbert
License: GPL-3.0
"""

import logging
from typing import Any, Dict, List, Optional

from PySide6.QtCore import (
    QAbstractListModel,
    QByteArray,
    QModelIndex,
    Qt,
    Property,
    Signal,
    Slot
)

from jmbde.core.database import Database, DatabaseError
from jmbde.utils.exceptions import ModelError

# Initialize logger
logger = logging.getLogger(__name__)

class EmployeeModel(QAbstractListModel):
    """
    Qt Model for Employee data management.

    Provides a list model implementation for exposing employee data
    to QML interfaces with support for filtering, sorting, and CRUD operations.
    """

    # Define custom roles for data access
    ROLES = {
        Qt.UserRole + 1: QByteArray(b'id'),
        Qt.UserRole + 2: QByteArray(b'name'),
        Qt.UserRole + 3: QByteArray(b'position'),
        Qt.UserRole + 4: QByteArray(b'email'),
        Qt.UserRole + 5: QByteArray(b'phone'),
        Qt.UserRole + 6: QByteArray(b'department'),
        Qt.UserRole + 7: QByteArray(b'hire_date'),
        Qt.UserRole + 8: QByteArray(b'active')
    }

    # Qt Signals
    dataChanged = Signal()
    filterChanged = Signal()
    errorOccurred = Signal(str)

    def __init__(self, database: Database, parent: Optional[Any] = None) -> None:
        """
        Initialize the Employee Model.

        Args:
            database: Database instance for data access
            parent: Optional parent QObject
        """
        super().__init__(parent)
        self._database = database
        self._data: List[Dict[str, Any]] = []
        self._filter_text: str = ""
        self._department_filter: Optional[str] = None
        self._show_inactive: bool = False

        self.refresh()
        logger.info("EmployeeModel initialized")

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Get the number of rows in the model.

        Args:
            parent: Parent model index (unused in list models)

        Returns:
            Number of employees in the filtered dataset
        """
        return len(self._data)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> Any:
        """
        Get data for the specified index and role.

        Args:
            index: Model index to get data for
            role: Data role to retrieve

        Returns:
            Requested data or None if invalid
        """
        if not index.isValid() or not (0 <= index.row() < len(self._data)):
            return None

        employee = self._data[index.row()]
        role_name = self.ROLES.get(role, b'').decode()

        try:
            return employee.get(role_name)
        except Exception as e:
            logger.error(f"Error accessing employee data: {e}")
            return None

    def roleNames(self) -> Dict[int, QByteArray]:
        """
        Get the role names for QML binding.

        Returns:
            Dictionary mapping role IDs to role names
        """
        return self.ROLES

    @Slot()
    def refresh(self) -> None:
        """Reload employee data from the database with current filters."""
        try:
            self.beginResetModel()
            self._data = self._load_filtered_data()
            self.endResetModel()
            self.dataChanged.emit()
            logger.debug(f"Model refreshed with {len(self._data)} employees")
        except Exception as e:
            logger.error(f"Failed to refresh model: {e}")
            self.errorOccurred.emit(str(e))

    def _load_filtered_data(self) -> List[Dict[str, Any]]:
        """
        Load employee data applying current filters.

        Returns:
            Filtered list of employee records
        """
        try:
            employees = self._database.get_employees(
                active_only=not self._show_inactive,
                department=self._department_filter
            )

            # Apply text filter if set
            if self._filter_text:
                filter_lower = self._filter_text.lower()
                employees = [
                    emp for emp in employees
                    if filter_lower in emp['name'].lower() or
                       filter_lower in emp['position'].lower() or
                       filter_lower in emp.get('email', '').lower()
                ]

            return employees
        except DatabaseError as e:
            logger.error(f"Database error loading employees: {e}")
            raise ModelError(f"Failed to load employee data: {e}") from e

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
            self.filterChanged.emit()

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
            self.filterChanged.emit()

    @Property(bool)
    def showInactive(self) -> bool:
        """Get inactive employees display setting."""
        return self._show_inactive

    @showInactive.setter
    def showInactive(self, value: bool) -> None:
        """Set inactive employees display setting and refresh model."""
        if value != self._show_inactive:
            self._show_inactive = value
            self.refresh()
            self.filterChanged.emit()

    @Slot(int, str, str, str, str)
    def updateEmployee(self, index: int, name: str, position: str,
                      email: str, phone: str) -> bool:
        """
        Update employee data at specified index.

        Args:
            index: Row index to update
            name: New employee name
            position: New position
            email: New email
            phone: New phone number

        Returns:
            bool: True if update was successful
        """
        try:
            if 0 <= index < len(self._data):
                employee_id = self._data[index]['id']
                success = self._database.update_employee(
                    employee_id,
                    {
                        'name': name,
                        'position': position,
                        'email': email,
                        'phone': phone
                    }
                )
                if success:
                    self.refresh()
                    logger.info(f"Updated employee {employee_id}")
                return success
            return False
        except Exception as e:
            logger.error(f"Failed to update employee: {e}")
            self.errorOccurred.emit(str(e))
            return False

    @Slot(str, str, str, str, str)
    def addEmployee(self, name: str, position: str, email: str,
                   phone: str, department: str) -> bool:
        """
        Add a new employee.

        Args:
            name: Employee name
            position: Position
            email: Email address
            phone: Phone number
            department: Department name

        Returns:
            bool: True if addition was successful
        """
        try:
            from datetime import datetime
            employee_id = self._database.add_employee({
                'name': name,
                'position': position,
                'email': email,
                'phone': phone,
                'department': department,
                'hire_date': datetime.now(),
                'active': True
            })
            if employee_id:
                self.refresh()
                logger.info(f"Added new employee: {name}")
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to add employee: {e}")
            self.errorOccurred.emit(str(e))
            return False

    @Slot(int)
    def removeEmployee(self, index: int) -> bool:
        """
        Remove employee at specified index.

        Args:
            index: Row index to remove

        Returns:
            bool: True if removal was successful
        """
        try:
            if 0 <= index < len(self._data):
                employee_id = self._data[index]['id']
                success = self._database.delete_employee(employee_id)
                if success:
                    self.refresh()
                    logger.info(f"Removed employee {employee_id}")
                return success
            return False
        except Exception as e:
            logger.error(f"Failed to remove employee: {e}")
            self.errorOccurred.emit(str(e))
            return False

    @Slot(result=list)
    def getDepartments(self) -> List[str]:
        """
        Get list of unique departments.

        Returns:
            List of department names
        """
        try:
            departments = set(emp['department'] for emp in self._data
                            if emp.get('department'))
            return sorted(departments)
        except Exception as e:
            logger.error(f"Failed to get departments: {e}")
            return []
