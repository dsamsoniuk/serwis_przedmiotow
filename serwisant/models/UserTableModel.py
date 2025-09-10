
from PySide6.QtCore import Qt, QAbstractTableModel, QAbstractItemModel
from models.TableModel import TableModel 

class UserTableModel(TableModel, QAbstractTableModel):

    _headers = ["id", "name", "age"]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        user = self._rows[index.row()]
        col = index.column()
        if role in (Qt.DisplayRole, Qt.EditRole):
            if col == 0: return user.id
            if col == 1: return user.name
            if col == 2: return user.age
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid() or role != Qt.EditRole:
            return False

        user = self._rows[index.row()]
        col = index.column()
        if col == 1:
            user.name = str(value)
        elif col == 2:
            try:
                user.age = int(value)
            except ValueError:
                return False
        else:
            return False
        self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])
        return True
