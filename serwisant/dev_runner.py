# dev_runner.py
import sys
from watchfiles import run_process
from PySide6 import QtWidgets
from app import main 

# Tryb developer
# Uruchom projekt w trybie watch
# python dev_runner.py


def run():
    main()
    # app = QtWidgets.QApplication(sys.argv)
    # window = MainApp()
    # window.show()
    # sys.exit(app.exec())

if __name__ == "__main__":
    run_process('.', target=run)