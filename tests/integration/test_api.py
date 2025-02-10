import pytest
from fastapi.testclient import TestClient

from jmbde.api.server import app  # Ensure correct import path

client = TestClient(app)


def test_api_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to JMBDE API"}


def test_api_add_employee():
    response = client.post(
        "/employees",
        json={
            "name": "John Doe",
            "position": "Developer",
            "email": "john@example.com",
            "phone": "123456789",
            "department": "IT",
            "hire_date": "2024-01-01",
            "active": True,
        },
    )
    assert response.status_code == 201
