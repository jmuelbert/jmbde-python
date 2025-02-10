from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class DeviceStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"


class DeviceModel(BaseModel):
    """Data model for Device records."""

    id: Optional[int] = None  # Set default value to None
    employee_id: Optional[int] = None  # Set default value to None
    device_name: str
    device_type: str
    serial_number: str
    purchase_date: datetime
    warranty_expires: Optional[datetime] = None  # Set default value to None
    status: DeviceStatus  # Use the Enum for status
