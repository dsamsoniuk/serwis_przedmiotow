
from models.models import Item
from models.ItemTableModel import ItemTableModel
from database import get_db
from module import ApiItemsModule
from PySide6.QtWidgets import QHeaderView

class pageItems():
    
    def __init__(self, MainWindow):
        self.mainWindow = MainWindow
        
    def loadTableData(self):
        session = next(get_db())
        items = session.query(Item).all()
        self.tableModel = ItemTableModel(items, session)
        self.mainWindow.tableView.setModel(self.tableModel)

        # stretch full size content table
        header = self.mainWindow.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

    def updateDataFromServer(self):
        session = next(get_db())

        session.query(Item).delete()
        session.commit()

        try:
            api = ApiItemsModule()
            response = api.makeRequest("/items")

            for data in response.json():
                newItem = Item(**data)
                session.add(newItem)
                session.commit()
                self.mainWindow.label_6.setText("Dane zaktualizowane lokanie")
        except Exception as e:
            self.mainWindow.logger.error(repr(e))
            self.mainWindow.label_6.setText("Nie udalo sie zaktualizowac danych")
            print(e)
        self.loadTableData()

    def saveModelData(self):
        self.tableModel.save_changes()
        self.mainWindow.logger.info("Zapis danych lokalnie - udany")

        for item in self.tableModel._rows:
            try:
                api = ApiItemsModule()
                api.makeRequest("/items", "patch", {
                    "id": item.id,
                    "name": item.name,
                    "description": item.description,
                    "price": item.price,
                    "tax": item.tax
                })
                self.mainWindow.label_6.setText("Dane zapisane")
            except Exception as e:
                self.mainWindow.logger.error(repr(e))
                self.mainWindow.logger.error("Zapis danych na serwerze - nie udany")
                self.mainWindow.label_6.setText("Nie udalo sie zapisac danych na serwerze")
                print(e)
        
        self.mainWindow.logger.info("Zapis danych na serwerze - udany")
