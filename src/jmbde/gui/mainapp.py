class MainApp:
    """Main application logic exposed to QML.
    """

    def __init__(self, database, model):
        super().__init__()
        self.database = database
        self.model = model

    @Slot(str, str)
    def add_employee(self, name, position):
        self.database.add_employee(name, position)
        self.model.refresh()
        logger.info(f"Employee added via MainApp: {name}, {position}")

    @Slot(int, str, str)
    def update_employee(self, emp_id, name, position):
        self.database.update_employee(emp_id, name, position)
        self.model.refresh()
        logger.info(
            f"Employee updated via MainApp: ID={emp_id}, Name={name}, Position={position}",
        )

    @Slot(int)
    def delete_employee(self, emp_id):
        self.database.delete_employee(emp_id)
        self.model.refresh()
        logger.info(f"Employee deleted via MainApp: ID={emp_id}")
