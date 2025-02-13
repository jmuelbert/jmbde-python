from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr

from jmbde.core.database import Database
from jmbde.models.employee import EmployeeData
from jmbde.utils.exceptions import DatabaseError


class DBHandler:
    def __init__(self, db_path):
        """Initialize database handler."""
        self.db = Database(db_path)

    def get_all_employees(self) -> List[EmployeeData]:
        """Retrieve all employees from the database.

        Returns:
            List[EmployeeData]: List of all employees

        Raises:
            DatabaseError: If retrieving employees fails
        """
        try:
            with self.db.transaction() as cursor:
                cursor.execute(
                    """
                    SELECT id, name, position, email, phone,
                           department, hire_date, active
                    FROM employees
                """
                )
                rows = cursor.fetchall()
                return [
                    EmployeeData.model_validate(
                        {
                            "id": row["id"],
                            "name": row["name"],
                            "position": row["position"],
                            "email": row["email"],
                            "phone": row["phone"],
                            "department": row["department"],
                            "hire_date": row["hire_date"],
                            "active": bool(row["active"]),
                        }
                    )
                    for row in rows
                ]
        except Exception as e:
            raise DatabaseError(f"Failed to retrieve employees: {e}") from e

    def add_employee(self, employee: EmployeeData) -> int:
        """Add an employee to the database.

        Args:
            employee: Employee data to add

        Returns:
            int: ID of the newly added employee

        Raises:
            DatabaseError: If adding employee fails
        """
        try:
            return self.db.add_employee(employee)
        except Exception as e:
            raise DatabaseError(f"Failed to add employee: {e}") from e

    def update_employee(self, employee: EmployeeData) -> bool:
        """Update an employee in the database.

        Args:
            employee: Employee data to update

        Returns:
            bool: True if update was successful

        Raises:
            DatabaseError: If updating employee fails
        """
        try:
            with self.db.transaction() as cursor:
                cursor.execute(
                    """
                    UPDATE employees
                    SET name=?, position=?, email=?, phone=?,
                        department=?, hire_date=?, active=?
                    WHERE id=?
                """,
                    (
                        employee.name,
                        employee.position,
                        employee.email,
                        employee.phone,
                        employee.department,
                        employee.hire_date,
                        employee.active,
                        employee.id,
                    ),
                )
                return cursor.rowcount > 0
        except Exception as e:
            raise DatabaseError(f"Failed to update employee: {e}") from e

    def delete_employee(self, employee_id: int) -> bool:
        """Delete an employee from the database.

        Args:
            employee_id: ID of employee to delete

        Returns:
            bool: True if deletion was successful

        Raises:
            DatabaseError: If deleting employee fails
        """
        try:
            with self.db.transaction() as cursor:
                cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
                return cursor.rowcount > 0
        except Exception as e:
            raise DatabaseError(f"Failed to delete employee: {e}") from e

    def get_employee_by_id(self, employee_id: int) -> Optional[EmployeeData]:
        """Retrieve an employee by ID.

        Args:
            employee_id: ID of employee to retrieve

        Returns:
            Optional[EmployeeData]: Employee data if found, None otherwise

        Raises:
            DatabaseError: If retrieving employee fails
        """
        try:
            with self.db.transaction() as cursor:
                cursor.execute(
                    """
                    SELECT id, name, position, email, phone,
                           department, hire_date, active
                    FROM employees
                    WHERE id = ?
                """,
                    (employee_id,),
                )
                row = cursor.fetchone()
                if row:
                    return EmployeeData.model_validate(
                        {
                            "id": row["id"],
                            "name": row["name"],
                            "position": row["position"],
                            "email": row["email"],
                            "phone": row["phone"],
                            "department": row["department"],
                            "hire_date": row["hire_date"],
                            "active": bool(row["active"]),
                        }
                    )
                return None
        except Exception as e:
            raise DatabaseError(f"Failed to retrieve employee: {e}") from e

    def cleanup(self):
        """Clean up database resources."""
        if hasattr(self, "db") and self.db:
            self.db.close()
