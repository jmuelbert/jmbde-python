#!/usr/bin/env python3
"""
Integrationstest für die PySide6-GUI
Stellt sicher, dass die QML-Oberfläche geladen wird und dass
die MainApp-Instanz als ContextProperty zur Verfügung steht.
"""

import sys

import pytest
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from jmbde.core.database import Database
from jmbde.gui.employee_model import EmployeeModel
from jmbde.gui.main_app import MainApp


@pytest.fixture(scope="session")
def qml_app():
    """
    Stellt sicher, dass für alle Tests nur eine Instanz von QGuiApplication existiert.
    """
    app = QGuiApplication.instance()
    if not app:
        app = QGuiApplication(sys.argv)
    return app


def test_qml_interface_loading(qml_app, qtbot):
    """
    Testet, ob die QML-Oberfläche geladen wird und ob die MainApp-Instanz
    als ContextProperty verfügbar ist.
    """
    engine = QQmlApplicationEngine()

    # Initialisiere die Kernkomponenten
    database = Database()  # Consider using a test database or mock
    employee_model = EmployeeModel(database)
    main_app = MainApp(database, employee_model)

    # Setze MainApp als ContextProperty, damit QML darauf zugreifen kann
    engine.rootContext().setContextProperty("MainApp", main_app)

    # Lade die Haupt-QML-Datei. Stelle sicher, dass der qrc-Pfad korrekt ist.
    engine.load(QUrl("qrc:/qml/main.qml"))

    # Überprüfe, ob die QML-Oberfläche erfolgreich geladen wurde
    root_objects = engine.rootObjects()
    assert root_objects, "QML-Oberfläche konnte nicht geladen werden."

    # Optional: Überprüfe, ob die MainApp-Instanz im QML verfügbar ist
    main_app_instance = root_objects[0].findChild(QObject, "MainApp")
    assert main_app_instance is not None, "MainApp-Instanz ist nicht im QML verfügbar."

    # Cleanup if necessary
    # database.cleanup()  # Uncomment if your Database class has a cleanup method
