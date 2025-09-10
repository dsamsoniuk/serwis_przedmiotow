from dotenv import load_dotenv
load_dotenv()

import sys
from PySide6 import QtWidgets
from gui_main_qt6_ui import Ui_MainWindow 
from service.loggerModule import loggerModule
from pages.pageItems import pageItems
from pages.pageLogin import pageLogin
from PySide6 import QtCore

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        
        super().__init__()
        self.setupUi(self)

        lm           = loggerModule()
        self.logger  = lm.getLogger()
        self.settings = QtCore.QSettings("MyApp", "Runner")

        # Pages
        self.actionmain_page.triggered.connect(self.show_page1)
        self.actionzwykla_tabela.triggered.connect(self.show_page1)
        self.actionmodel_tabela.triggered.connect(self.show_page1)

        mainWindow = self
        self.pageLogin  = pageLogin(mainWindow)
        self.pageItem   = pageItems(mainWindow)
        self.pageItem.loadTableData()

        # Actions
        self.pushButton.clicked.connect(self.saveModelData)
        self.pushButton_2.clicked.connect(self.updateDataFromServer)
        self.pushButton_3.clicked.connect(self.saveLoginData)

    def saveLoginData(self):
        if self.pageLogin.saveLoginData():
            self.unlock_pages()

    def unlock_pages(self):
        self.actionmodel_tabela.triggered.connect(self.show_page2)

    def saveModelData(self):
        self.pageItem.saveModelData()
    def updateDataFromServer(self):
        self.pageItem.updateDataFromServer()

    def show_page1(self):
        self.stackedWidget.setCurrentIndex(0)  

    def show_page2(self):
        self.stackedWidget.setCurrentIndex(1) 

def main():
    
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
