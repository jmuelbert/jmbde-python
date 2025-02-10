#!/usr/bin/env python3
"""
End-to-End-Test für die Hauptanwendung von JMBDE.

Dieser Test prüft den kompletten Workflow:
- Eingabe von Daten
- Übermittlung der Daten
- Überprüfung, ob das EmployeeModel aktualisiert wurde
"""

import pytest
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from jmbde.core.database import Database
from jmbde.gui.main_app import MainApp  # Ensure this is the correct import
from jmbde.models.employee import EmployeeModel


@pytest.fixture(scope="session")
def qt_app():
    """Fixture to create a QGuiApplication for the entire test session."""
    if not QGuiApplication.instance():
        app = QGuiApplication([])  # Create a QGuiApplication for QML
    else:
        app = QGuiApplication.instance()  # Use existing instance
    yield app
    app.quit()  # Ensure the application quits after tests


@pytest.fixture
def database():
    """Erstellt eine temporäre Dummy-Datenbank."""
    return Database()  # Falls du eine spezielle Test-Datenbank hast, hier anpassen


@pytest.fixture
def main_app(database, qt_app):
    """Erstellt eine Instanz der Hauptanwendung."""
    engine = QQmlApplicationEngine()

    # Initialize MainApp with the database
    main_app = MainApp(database)
    engine.rootContext().setContextProperty(
        "mainApp", main_app
    )  # Expose MainApp to QML
    engine.load("qrc:/qml/main.qml")  # Load your QML file

    # Ensure the QML file loaded successfully
    assert engine.rootObjects(), "Failed to load QML file."

    return main_app


def test_full_workflow(main_app, qtbot):
    """
    Testet das Hinzufügen eines Mitarbeiters über die GUI und überprüft,
    ob das EmployeeModel korrekt aktualisiert wird.
    """
    # Step 1: Simulierte Benutzereingabe
    name = "Test Employee"
    position = "Developer"
    email = "test@example.com"
    phone = "123456789"
    department = "IT"

    success = main_app.add_employee(name, position, email, phone, department)

    # Überprüfung, ob der Eintrag erfolgreich war
    assert success, "Mitarbeiter konnte nicht hinzugefügt werden."

    # Step 2: Überprüfung, ob das Model die Daten enthält
    model: EmployeeModel = main_app._model  # Zugriff auf das EmployeeModel
    row_count = model.rowCount()
    assert (
        row_count > 0
    ), "Das EmployeeModel enthält keine Einträge nach dem Hinzufügen."

    # Step 3: Überprüfung des letzten hinzugefügten Mitarbeiters
    last_index = model.index(row_count - 1, 0)
    assert last_index.isValid(), "Der letzte Eintrag im Model ist ungültig."

    assert (
        model.data(last_index, Qt.DisplayRole) == name
    ), "Der Name im Model ist nicht korrekt."
