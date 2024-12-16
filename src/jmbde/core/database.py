class Database:
    """Database class to manage CRUD operations for employees and devices.
    """

    def __init__(self, db_path=Config.DATABASE_PATH):
        self.connection = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL
            );
            """,
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS devices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_id INTEGER,
                device_name TEXT NOT NULL,
                device_type TEXT NOT NULL,
                FOREIGN KEY (employee_id) REFERENCES employees (id)
            );
            """,
        )
        self.connection.commit()
        logger.info("Database tables created successfully.")

    def add_employee(self, name, position):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO employees (name, position) VALUES (?, ?)", (name, position),
        )
        self.connection.commit()
        logger.debug(f"Employee added: {name}, {position}")
        return cursor.lastrowid

    def get_employees(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, position FROM employees")
        result = cursor.fetchall()
        logger.debug(f"Retrieved employees: {result}")
        return result

    def update_employee(self, emp_id, name, position):
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE employees SET name = ?, position = ? WHERE id = ?",
            (name, position, emp_id),
        )
        self.connection.commit()
        logger.debug(f"Updated employee {emp_id}: {name}, {position}")

    def delete_employee(self, emp_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
        self.connection.commit()
        logger.debug(f"Deleted employee with ID: {emp_id}")
