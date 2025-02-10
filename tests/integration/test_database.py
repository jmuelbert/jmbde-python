#!/usr/bin/env python3
"""
Integrationstests für die Datenbank-Komponente.
Diese Tests erstellen eine temporäre Datenbank, fügen einen Employee-Datensatz hinzu
und prüfen anschließend, ob die Daten korrekt in der Datenbank gespeichert wurden.
"""

import sqlite3
from datetime import datetime

import pytest

from jmbde.core.database import Database
from jmbde.models.employee import EmployeeModel


def test_database_creation(tmp_path):
    """
    Testet, ob die Datenbank erfolgreich initialisiert wird und die Datei erstellt wurde.
    """
    db_path = tmp_path / "test.db"
    db = Database(db_path)
    # Die Datenbank-Datei sollte existieren.
    assert db.db_path.exists()


def test_add_employee_integration(tmp_path):
    """
    Testet, ob ein Employee-Datensatz korrekt in die Datenbank eingefügt wird.
    """
    db_path = tmp_path / "test.db"
    db = Database(db_path)

    # Erstelle einen Employee mit gültigen Daten
    employee = EmployeeModel(
        name="John Doe",
        position="Developer",
        email="john.doe@example.com",
        phone="123-456",
        department="IT",
        hire_date=datetime.now(),
        active=True,
    )

    emp_id = db.add_employee(employee)
    assert emp_id > 0

    # Direktes Abfragen der Datenbank, um den eingefügten Datensatz zu validieren
    with db.connection as conn:
        cursor = conn.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
        row = cursor.fetchone()
        assert row is not None
        assert row["name"] == "John Doe"
