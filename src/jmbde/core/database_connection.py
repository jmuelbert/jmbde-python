# database_connection.py
from jmbde.core.database import Database


class DatabaseConnection:
    def __init__(self, db_path=None):
        self.database = Database(db_path)

    def add_employee(self, employee):
        return self.database.add_employee(employee)

    def add_device(self, device):
        return self.database.add_device(device)

    # You can add more methods to interact with the database as needed
