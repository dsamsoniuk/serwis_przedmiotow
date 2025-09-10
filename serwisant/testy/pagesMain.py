import sys
from PyQt6 import QtWidgets, uic

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pages.ui", self)   # wczytanie GUI z Qt Designer

        # Obsługa przycisków
        self.pushButton.clicked.connect(self.show_page1)
        self.pushButton_2.clicked.connect(self.show_page2)

    def show_page1(self):
        self.stackedWidget.setCurrentIndex(0)  # przełącz na stronę 0 ("Witaj")

    def show_page2(self):
        self.stackedWidget.setCurrentIndex(2)  # przełącz na stronę 1 ("Cześć")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())