#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PySide2.QtCore import QTextStream, QDir, QFile, QIODevice, QStandardPaths, QCoreApplication
from PySide2.QtSql import QSqlDatabase, QSqlQuery

from ..logger import Logger


class DataContext():
    """The DataContext Class
       Provide the communication with the database
    """

    def __init__(self) -> None:
        """"The class initializer"""
        self.database = 0
        self.dbType = 'sqlite'
        self.database_name = 0
        self.log = Logger().create_log()
        self.log.info("jmbde: init datacontext")

    def createConnection(self) -> None:
        """Create the Connection to the Database.
           For the Moment just SQLite
        """"
        if self.dbType == 'sqlite':
            self.database = QSqlDatabase.database()
            if not self.database.isValid():
                self.database = QSqlDatabase.addDatabase("QSQLITE")
                if not self.database.isValid():
                    self.log.error("Cannot add database")
                    return False

            self.database_name = self.getSqliteName()
            file = QFile(self.database_name)
            if file.exists():
                # When using the SQLite driver, open() will create the SQLite
                # database if it doesn't exist.
                self.log.info("Try open the existing db : {0}".format(self.database_name))
                self.database.setDatabaseName(self.database_name)
                self.database.open()
            else:
                self.database.setDatabaseName(self.database_name)
                self.log.info("Try create db : {0}".format(self.database_name))
                self.prepareDB()

            if not self.database.open():
                self.log.error("Cannot open database")
                QFile.remove(self.database_name)

    def getSqliteName(self) -> str:
        """Create the name for the SqliteDB.
            Therefor combine the Qt Application Defs:
            QStandardPaths.DataLocation + QtCoreApplication.applicationName + .sqlite3
            on Mac is this:
            ~/Library/Application Support/io.jmuelbert.github/jmbde/jmbde.sqlite3
            on Linux this:
            ~/.local/share/<APPNAME>/jmbde.sqlite3
            on Windows is this:
            C:/Users/<USER>/AppData/Local/<APPNAME>/jmbde.sqlite3
        """
        dbDataPath = QStandardPaths.writableLocation(QStandardPaths.DataLocation)

        self.log.info("The Database: {}".format(dbDataPath))

        write_dir = QDir(dbDataPath)
        if not write_dir.mkpath("."):
            self.log.error("Failed to create writable directory")

        if not write_dir.exists():
            write_dir.mkpath(dbDataPath)

        # Ensure that we have a writable location on all devices.
        filename = "{0}/{1}.sqlite3".format(write_dir.absolutePath(), QCoreApplication.applicationName())

        return filename

    def prepareDB(self) -> bool:
        """Create the Database from the DDL
           The DDL is a script that provided as QResource

        Returns
            [bool] -- [True if creation succesful]
        """
        if not self.database.isValid():
            self.log.warning("The Database is not valid, reopen")
            self.database = QSqlDatabase.database(self.database_name)

        self.database.open()

        query = QSqlQuery(self.database)

        file = QFile(":/data/script.sql")
        if not file.exists():
            self.log.error("Kritischer Fehler beim erzeugen der Datenbank {} nicht gefunden".format(file.fileName()))
            return False

        if not file.open(QIODevice.ReadOnly):
            self.log.error("Kritischer Fehler bei der Initialisierung der Datenbank. Die Datei {} konnte nicht geöffnet werden".format(file.fileName()))

        ts = QTextStream(file)

        line = ""
        cleanedLine = ""
        stringList = []
        readLine = []

        self.log.info("File at end: {}".format(ts.atEnd()))

        while not ts.atEnd():
            hasText = False
            line = ""
            stringList.clear()
            while not hasText:
                readLine = ts.readLine()
                self.log.info("read Line: {}".format(readLine))
                cleanedLine = readLine.strip()
                stringList = cleanedLine.split("--")
                cleanedLine = stringList[0]
                if not cleanedLine.startswith("--") and not cleanedLine.startswith("DROP"):
                    line += cleanedLine
                if cleanedLine.endswith(";"):
                    break
                if cleanedLine.startswith("COMMIT"):
                    hasText = True
            if not line == "":
                self.log.info("Line: {}".format(line))

                if not query.exec_(line):
                    self.log.error("Fehler beim Erzeugen der Tabelle {}".format(line))
                    self.log.error("Datenbank meldet Fehler {}".format(query.lastError()))
                    return False
            else:
                self.log.error(
                    "Fehler beim Lesen der Datei zur Datenbank Erzeugung: ")
                return False
        file.close()
        self.log.info("Datenbank erfolgreich erzeugt")
        return True
