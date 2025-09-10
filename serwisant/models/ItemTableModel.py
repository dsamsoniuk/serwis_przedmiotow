
from PySide6.QtCore import Qt, QAbstractTableModel, QAbstractItemModel
from models.TableModel import TableModel 

class ItemTableModel(TableModel, QAbstractTableModel):

    _headers = ["id", "name", "price"]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        item = self._rows[index.row()]
        col = index.column()
        if role in (Qt.DisplayRole, Qt.EditRole):
            if col == 0: return item.id
            if col == 1: return item.name
            if col == 2: return item.price
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid() or role != Qt.EditRole:
            return False

        item = self._rows[index.row()]
        col = index.column()
        if col == 1:
            item.name = str(value)
        elif col == 2:
            try:
                item.price = int(value)
            except ValueError:
                return False
        else:
            return False
        self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])
        return True
