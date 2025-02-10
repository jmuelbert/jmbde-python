from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr  # Import EmailStr


class EmployeeModel(BaseModel):
    """Data model for Employee records."""

    id: Optional[int] = None  # Optional field with default value None
    name: str
    position: str
    email: EmailStr  # Use EmailStr for email validation
    phone: str
    department: str
    hire_date: datetime
    active: bool = True  # Default value is True


# Example usage
try:
    employee = EmployeeModel(
        name="John Doe",
        position="Software Engineer",
        email="john.doe@example.com",  # Valid email
        phone="123-456-7890",
        department="Engineering",
        hire_date=datetime.now(),
    )
    print(employee)
except ValueError as e:
    print(f"Error: {e}")

# Example of invalid email
try:
    invalid_employee = EmployeeModel(
        name="Jane Doe",
        position="Software Engineer",
        email="invalid-email",  # Invalid email
        phone="123-456-7890",
        department="Engineering",
        hire_date=datetime.now(),
    )
except ValueError as e:
    print(f"Error: {e}")  # This will raise a validation error
