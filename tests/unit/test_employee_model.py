#!/usr/bin/env python3
"""
Unit-Tests für das Employee Model.
Diese Tests prüfen, ob EmployeeModel bei gültigen Daten korrekt erzeugt wird
und ob ungültige Daten (z.B. ein falsches Email-Format) eine ValidationError auslösen.
"""

from datetime import datetime

import pytest
from pydantic import ValidationError

from jmbde.models.employee import EmployeeModel


def test_employee_valid():
    """
    Testet, ob ein EmployeeModel mit gültigen Daten erstellt werden kann.
    """
    employee = EmployeeModel(
        name="Alice",
        position="Engineer",
        email="alice@example.com",
        phone="555-1234",
        department="R&D",
        hire_date=datetime.now(),
    )
    assert employee.name == "Alice"
    assert employee.email == "alice@example.com"


def test_employee_invalid_email():
    """
    Testet, ob ein falsches Email-Format zu einer ValidationError führt.
    """
    with pytest.raises(ValidationError):
        EmployeeModel(
            name="Bob",
            position="Tester",
            email="invalid-email",  # ungültiges Format
            phone="555-1234",
            department="QA",
            hire_date=datetime.now(),
        )
