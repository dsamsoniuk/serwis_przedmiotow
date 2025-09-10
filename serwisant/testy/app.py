import sys
from PyQt6 import QtWidgets
from main_ui import Ui_MainWindow   # import wygenerowanego pliku
# from PyQt6 import *

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    numer = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Połączenie przycisku z funkcją
        self.pushButton.clicked.connect(self.change_text)
        self.numer = 3
    def change_text(self):
        # Zmiana tekstu etykiety
        tekst = "---" + str(self.numer)
        self.label.setText(tekst)
        self.numer = self.numer + 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())