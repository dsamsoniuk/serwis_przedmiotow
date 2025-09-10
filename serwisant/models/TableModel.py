
from PySide6.QtCore import Qt, QAbstractTableModel, QAbstractItemModel

class TableModel():
    def __init__(self, objects, session):
        super().__init__()
        self._rows = objects
        self._session = session
        # self._headers = ["id", "name", "age"]

    def rowCount(self, parent=None):
        return len(self._rows)

    def columnCount(self, parent=None):
        return len(self._headers)

    # def data(self, index, role=Qt.DisplayRole):
    #     if not index.isValid():
    #         return None
    #     user = self._users[index.row()]
    #     col = index.column()
    #     if role in (Qt.DisplayRole, Qt.EditRole):
    #         if col == 0: return user.id
    #         if col == 1: return user.name
    #         if col == 2: return user.age
    #     return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        if index.column() == 0:  # id nie edytujemy
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    # def setData(self, index, value, role=Qt.EditRole):
    #     if not index.isValid() or role != Qt.EditRole:
    #         return False

    #     user = self._users[index.row()]
    #     col = index.column()
    #     if col == 1:
    #         user.name = str(value)
    #     elif col == 2:
    #         try:
    #             user.age = int(value)
    #         except ValueError:
    #             return False
    #     else:
    #         return False
    #     self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])
    #     return True

    def save_changes(self):
        self._session.commit()
