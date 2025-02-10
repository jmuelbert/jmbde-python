#!/usr/bin/env python3
"""
Unit-Test für die Database-Klasse, der mittels Monkeypatch einen Fehler in der Transaction simuliert.
"""

from datetime import datetime

import pytest

from jmbde.core.database import Database
from jmbde.models.employee import EmployeeModel
from jmbde.utils.exceptions import DatabaseError


def test_add_employee_failure(monkeypatch, tmp_path):
    """
    Simuliert einen Fehler in der Transaktion und prüft, ob ein DatabaseError ausgelöst wird.
    """
    db_path = tmp_path / "test.db"
    db = Database(db_path)

    # Definiere einen Fake-Context-Manager, der sofort beim Betreten einen Fehler wirft
    class FakeCursor:
        def __enter__(self):
            raise Exception("Simulierter Fehler in der Transaction")

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

    def fake_transaction():
        return FakeCursor()

    # Überschreibe die transaction-Methode der Datenbank-Instanz
    monkeypatch.setattr(db, "transaction", fake_transaction)

    # Erstelle einen Employee-Datensatz
    employee = EmployeeModel(
        name="Charlie",
        position="Manager",
        email="charlie@example.com",
        phone="555-6789",
        department="HR",
        hire_date=datetime.now(),
    )

    with pytest.raises(DatabaseError):
        db.add_employee(employee)
