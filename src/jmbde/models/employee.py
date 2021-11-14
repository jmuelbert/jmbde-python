#
#   jmbde a BDE Tool for datacontext
#   Copyright (C) 2018-2020  Jürgen Mülbert
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
"""The Employee Data Model."""
from typing import Any
from typing import Dict

from PySide6.QtCore import QAbstractListModel
from PySide6.QtCore import QModelIndex
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal
from PySide6.QtCore import Slot


class EmployeeModel(QAbstractListModel):
    """The Model for the Employees.

    Args:
        QAbstractListModel ([type]): [description]

    Returns:
        [type]: [description]
    """

    NameRole = Qt.UserRole + 1
    AgeRole = Qt.UserRole + 2

    person_changed = Signal()

    def __init__(self, parent: Any = None) -> None:
        """The initializer for the Employee Model.

        Args:
            parent: The parent QObject. Defaults to None.
        """
        super().__init__(parent)
        self.persons = [{"name": "jon", "age": 20}, {"name": "jane", "age": 25}]

    def data(self, index: Any, role: Any = Qt.DisplayRole) -> Any:
        """The data generator for Employee.

        Args:
            index: The index to display
            role: The age or the name.

        Returns:
            Returns the name or the age of the person.
        """
        row = index.row()
        if role == EmployeeModel.NameRole:
            return self.persons[row]["name"]
        if role == EmployeeModel.AgeRole:
            return self.persons[row]["age"]

    def rowCount(self, parent: Any = QModelIndex) -> int:  # NoQa
        """Get back the row count.

        Args:
            parent: The actual QModelIndex

        Returns:
            the count of rows.
        """
        return len(self.persons)

    def roleNames(self) -> Dict:  # NoQa
        """Return the rolenames of the person.

        Returns:
            A Dict with the rolenames.
        """
        return {EmployeeModel.NameRole: b"name", EmployeeModel.AgeRole: b"age"}

    @Slot(str, int)
    def add_person(self, name: str, age: int) -> None:
        """Add a person.

        Args:
            name: the name of the person.
            age: the age of the version.
        """
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.persons.append({"name": name, "age": age})
        self.endInsertRows()

    @Slot(int, str, int)
    def edit_person(self, row: int, name: str, age: int) -> None:
        """Edit the person on the row.

        Args:
            row: the row of the person.
            name: name of the person.
            age: the age of the person.
        """
        ix = self.index(row, 0)
        self.persons[row] = {"name": name, "age": age}
        self.dataChanged.emit(ix, ix, self.roleNames())

    @Slot(int)
    def delete_person(self, row: int) -> None:
        """Delete the person on row.

        Args:
            row: the row of the person.
        """
        self.beginRemoveColumns(QModelIndex(), row, row)
        del self.persons[row]
        self.endRemoveRows()
