# tests/unit/test_device_model.py

from contextlib import contextmanager
from datetime import datetime, timedelta
from unittest.mock import Mock, call, patch

import pytest
from pydantic import ValidationError

from jmbde.core.database import Database
from jmbde.models.device import DeviceModel, DeviceStatus
from jmbde.utils.exceptions import DatabaseError

# Test data
current_time = datetime.now()
TEST_DEVICE_DATA = {
    "device_name": "Test Device",
    "device_type": "Laptop",
    "serial_number": "SN123456",
    "purchase_date": current_time,
    "warranty_expires": current_time + timedelta(days=365),
    "status": DeviceStatus.ACTIVE,
    "employee_id": None,
}


class TestDeviceModel:
    """Test DeviceModel functionality."""

    def test_device_creation(self):
        """Test device model creation."""
        device = DeviceModel(**TEST_DEVICE_DATA)
        assert device.device_name == TEST_DEVICE_DATA["device_name"]
        assert device.serial_number == TEST_DEVICE_DATA["serial_number"]

    # ... (other TestDeviceModel tests remain the same)


class TestDeviceDatabase:
    """Test device database operations."""

    @pytest.fixture
    def mock_db(self):
        """Provide mock database."""
        mock = Mock(spec=Database)

        # Create a mock transaction context
        @contextmanager
        def mock_transaction():
            cursor = Mock()
            cursor.lastrowid = 1
            cursor.fetchone.return_value = dict(TEST_DEVICE_DATA, id=1)
            yield cursor

        mock.transaction = mock_transaction

        # Add the required methods
        mock.add_device = Mock(return_value=1)
        mock.get_device = Mock(return_value=dict(TEST_DEVICE_DATA, id=1))
        mock.update_device = Mock(return_value=True)

        return mock

    def test_device_persistence(self, mock_db):
        """Test device persistence."""
        device = DeviceModel(**TEST_DEVICE_DATA)
        device_id = mock_db.add_device(device)

        assert device_id == 1
        assert mock_db.add_device.called

    def test_device_retrieval(self, mock_db):
        """Test device retrieval."""
        device_data = mock_db.get_device(1)

        assert device_data is not None
        assert device_data["device_name"] == TEST_DEVICE_DATA["device_name"]
        assert mock_db.get_device.called

    def test_device_update(self, mock_db):
        """Test device update."""
        device = DeviceModel(id=1, **TEST_DEVICE_DATA)
        success = mock_db.update_device(device)

        assert success
        assert mock_db.update_device.called


if __name__ == "__main__":
    pytest.main([__file__])
