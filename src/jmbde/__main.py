#!/usr/bin/python3
#
#   jmbde a BDE Tool for datacontext
#   Copyright (C) 2018-2020  Jürgen Mülbert
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
"""JMBDe app."""

import click


@click.command()
@click.version_option()
def main():
    app = QGuiApplication(sys.argv)

    # Initialize database and model
    database = Database()
    employee_model = EmployeeModel(database)

    # Initialize main application logic
    main_app = MainApp(database, employee_model)

    # QML Application Engine
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("employeeModel", employee_model)
    engine.rootContext().setContextProperty("mainApp", main_app)
    engine.load("main.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
