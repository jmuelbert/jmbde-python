from unittest.mock import Mock

import pytest
from main import EmployeeModel


@pytest.fixture
def mock_database():
    """Mocked database object."""
    mock = Mock()
    mock.get_employees.return_value = [
        (1, "Alice", "Manager"),
        (2, "Bob", "Developer"),
    ]
    return mock


@pytest.fixture
def model(mock_database):
    """Fixture for the EmployeeModel."""
    return EmployeeModel(mock_database)


def test_row_count(model):
    """Test row count of EmployeeModel."""
    assert model.rowCount() == 2


def test_data(model):
    """Test data retrieval from EmployeeModel."""
    index = model.index(0, 0)
    assert model.data(index, model.NAME_ROLE) == "Alice"
    assert model.data(index, model.POSITION_ROLE) == "Manager"
