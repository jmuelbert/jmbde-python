class EmployeeModel(QAbstractListModel):
    """A QAbstractListModel implementation to expose employee data to QML.
    """

    ID_ROLE = Qt.UserRole + 1
    NAME_ROLE = Qt.UserRole + 2
    POSITION_ROLE = Qt.UserRole + 3

    def __init__(self, database, parent=None):
        super().__init__(parent)
        self._database = database
        self._data = self._database.get_employees()

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role):
        if not index.isValid() or index.row() >= len(self._data):
            return None
        row = self._data[index.row()]
        if role == self.ID_ROLE:
            return row[0]
        if role == self.NAME_ROLE:
            return row[1]
        if role == self.POSITION_ROLE:
            return row[2]
        return None

    def roleNames(self):
        return {
            self.ID_ROLE: b"id",
            self.NAME_ROLE: b"name",
            self.POSITION_ROLE: b"position",
        }

    @Slot()
    def refresh(self):
        self.beginResetModel()
        self._data = self._database.get_employees()
        self.endResetModel()
