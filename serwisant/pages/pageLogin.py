# from service.Db import Db
# from PySide6 import QtWidgets
from models.models import Item
from models.ItemTableModel import ItemTableModel
from database import get_db
from module import ApiItemsModule
# from service.loggerModule import loggerModule
from PySide6 import QtCore

class pageLogin():
    
    def __init__(self, MainWindow):
        self.mainWindow = MainWindow
        self.settings = QtCore.QSettings("MyApp", "Runner")

        if self.settings.value("login") != None:
            self.mainWindow.label_5.setText("zalogowany jako " + str(self.settings.value("login")))
            self.mainWindow.unlock_pages()
        else:
            self.mainWindow.label_5.setText("Nie zalogowany !")

    def saveLoginData(self):

        login       = self.mainWindow.lineEdit.text()
        password    = self.mainWindow.lineEdit_2.text()

        self.settings.setValue('login', login)
        self.settings.setValue('password', password)
        # print("zalogowales sie")

        self.mainWindow.label_5.setText("zalogowany jako " + str(self.settings.value("login")))
        return True