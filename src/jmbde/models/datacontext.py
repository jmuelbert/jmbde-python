#
#   jmbde a BDE Tool for datacontext
#   Copyright (C) 201=-2020  Jürgen Mülbert
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
"""The datacontext module."""
from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QDir
from PySide6.QtCore import QFile
from PySide6.QtCore import QIODevice
from PySide6.QtCore import QStandardPaths
from PySide6.QtCore import QTextStream
from PySide6.QtCore import Slot
from PySide6.QtSql import QSqlDatabase
from PySide6.QtSql import QSqlQuery

from ..logger import Logger


class DataContext:
    """The DataContext Class.

    Provide the communication with the database
    """

    def __init__(self) -> None:
        """The class initializer."""
        self.database: QSqlDatabase = QSqlDatabase()
        self.dbType: str = "sqlite"
        self.database_name: str = ""
        self.database_hostname: str = ""
        self.database_port: int = 0
        self.database_user_name: str = ""
        self.database_password: str = ""
        self.log = Logger().create_log()
        self.log.info("jmbde: init datacontext")

    def init(self) -> bool:
        """Create the Connection to the Database.

        For the Moment just SQLite

        Returns:
            Return true is the database successful initialized.
        """
        self.database = QSqlDatabase.database()

        if self.dbType == "sqlite":
            if not self.database.isValid():
                self.database = QSqlDatabase.addDatabase("QSQLITE")
                if not self.database.isValid():
                    self.log.error("Cannot add database")
                    return False

            self.database_name = self.__get_sqlite_name()
            file = QFile(self.database_name)
            if file.exists():
                # When using the SQLite driver, open() will create the SQLite
                # database if it doesn't exist.
                self.log.info(f"Try open the existing db : {self.database_name}")
                self.database.setDatabaseName(self.database_name)
            else:
                self.database.setDatabaseName(self.database_name)
                self.log.info(f"Try create db : {self.database_name}")
                self.prepare_db()

            if not self.database.open():
                self.log.error("Cannot open database")
                QFile.remove(self.database_name)
                return False
        elif self.dbType == "psql":
            self.database = QSqlDatabase.addDatabase("QPSQL")
        elif self.dbType == "odbc":
            self.database = QSqlDatabase.addDatabase("QODBC")

        self.database.setHostName(self.database_hostname)
        self.database.setPort(self.database_port)
        self.database.setUserName(self.database_user_name)
        self.database.setPassword(self.database_password)

        if not self.database.isValid():
            self.log.error("Cannot add database")
            return False

        if not self.database.open():
            self.log.error("Cannot open database")
            return False

        return True

    def open_db(self) -> None:
        """Open the database."""
        pass

    def insert(self, table_name: str, insert_data: map) -> bool:
        """Insert data int a table.

        Args:
            table_name: the table for data insertion.
            insert_data: the new data to insert int the table.

        Returns:
            True is the insertion successful.
        """
        return True

    def update(
        self, table_name: str, column: str, new_value: str, op: str, id: str
    ) -> bool:
        """Update data in the table.

        Update the data in the table name.

        Args:
            table_name: The name of the table for update.
            column: the column of data for update.
            new_value: the newvalie for insert.
            op: the op.
            id: the id

        Returns:
            return true is the update successful.
        """
        return True

    def remove(self, table_name: str, remove_data: str) -> bool:
        """Remove data from a table.

        Args:
            table_name: The name of the table for remove data.
            remove_data: The data to remove.

        Returns:
            return true is the removing successful.
        """
        return True

    @Slot(bool)
    def check_existence(self, table_name: str, search_id: str, search: str) -> bool:
        """Check the existence in the database.

        Args:
            table_name: The name of the table for remove data.
            search_id: The id to search.
            search: The string to search.

        Returns:
            return true os the data into the database.
        """
        return True

    @Slot(map)
    def get(self, query_text: str) -> map:
        """Get data.

        Get the queryed data.

        Args:
            query_text: The query to select the data.

        Returns:
            A map with the data.
        """
        return map

    def __get_sqlite_name(self) -> str:
        """Create the name for the SqliteDB.

        Therefor combine the Qt Application Defs:
        QStandardPaths::AppDataLocation + QtCoreApplication.applicationName + .sqlite3

        * *on Mac is this*
            `~/Library/Application Support/io.jmuelbert.github/jmbde/jmbde.sqlite3`
        * *on Linux this*
            `~/.local/share/<APPNAME>/jmbde.sqlite3`
        * *on Windows is this*
            `C:/Users/<USER>/AppData/Local/<APPNAME>/jmbde.sqlite3`

        Returns:
            The connection string fot the sqlite database.
        """
        db_data_path = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)

        self.log.info(f"The Database: {db_data_path}")

        write_dir = QDir(db_data_path)
        if not write_dir.mkpath("."):
            self.log.error("Failed to create writable directory")

        if not write_dir.exists():
            write_dir.mkpath(db_data_path)

        # Ensure that we have a writable location on all devices.
        filename = "{}/{}.sqlite3".format(
            write_dir.absolutePath(), QCoreApplication.applicationName()
        )

        return filename

    def prepare_db(self) -> bool:
        """Create the Database from the DDL.

        The DDL is a script that provided as QResource

        Returns:
            True if creation successful.
        """
        if not self.database.isValid():
            self.log.warning("The Database is not valid, reopen")
            self.database = QSqlDatabase.database(self.database_name)

        self.database.open()

        query = QSqlQuery(self.database)

        file = QFile(":/data/script.sql")
        if not file.exists():
            self.log.error(
                "Kritischer Fehler beim erzeugen der Datenbank"
                " {} nicht gefunden".format(file.fileName())
            )
            return False

        if not file.open(QIODevice.ReadOnly):
            self.log.error(
                "Kritischer Fehler bei der Initialisierung der Datenbank."
                "Die Datei {} konnte nicht geöffnet werden".format(file.fileName())
            )

        ts = QTextStream(file)

        line: str = ""
        cleaned_line: str = ""
        string_list: list = []
        read_line: list = []

        self.log.info(f"File at end: {ts.atEnd()}")

        while not ts.atEnd():
            has_text: bool = False
            line = ""
            string_list.clear()
            while not has_text:
                read_line = ts.read_line()
                self.log.info(f"read Line: {read_line}")
                cleaned_line = read_line.strip()
                string_list = cleaned_line.split("--")
                cleaned_line = string_list[0]
                if not cleaned_line.startswith("--") and not cleaned_line.startswith(
                    "DROP"
                ):
                    line += cleaned_line
                if cleaned_line.endswith(";"):
                    break
                if cleaned_line.startswith("COMMIT"):
                    has_text = True
            if not line == "":
                self.log.info(f"Line: {line}")

                if not query.exec_(line):
                    self.log.error(f"Fehler beim Erzeugen der Tabelle {line}")
                    self.log.error(f"Datenbank meldet Fehler {query.lastError()}")
                    return False
            else:
                self.log.error("Fehler beim Lesen der Datei zur Datenbank Erzeugung: ")
                return False
        file.close()
        self.log.info("Datenbank erfolgreich erzeugt")
        return True
