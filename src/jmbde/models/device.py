from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator


class DeviceStatus(str, Enum):
    """Device status enumeration."""

    ACTIVE = "active"
    MAINTENANCE = "maintenance"
    RETIRED = "retired"


class DeviceModel(BaseModel):
    """Device data model."""

    model_config = ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        str_strip_whitespace=True,
        extra="forbid",
    )

    id: Optional[int] = Field(default=None, description="Device ID")
    employee_id: Optional[int] = Field(
        default=None, description="Associated employee ID"
    )
    device_name: str = Field(..., min_length=1, description="Name of the device")
    device_type: str = Field(..., min_length=1, description="Type of device")
    serial_number: str = Field(
        ...,
        min_length=1,
        description="Unique serial number",
        pattern=r"^[A-Za-z0-9-]+$",
    )
    purchase_date: datetime = Field(..., description="Date of purchase")
    warranty_expires: datetime = Field(..., description="Warranty expiration date")
    status: DeviceStatus = Field(
        default=DeviceStatus.ACTIVE, description="Current device status"
    )

    @model_validator(mode="after")
    def validate_dates(self) -> "DeviceModel":
        """Validate warranty expiration is after purchase date."""
        if self.warranty_expires < self.purchase_date:
            raise ValueError("Warranty expiration must be after purchase date")
        return self

    def to_dict(self) -> dict:
        """Convert model to dictionary."""
        return self.model_dump()

    @classmethod
    def from_dict(cls, data: dict) -> "DeviceModel":
        """Create instance from dictionary."""
        return cls.model_validate(data)
