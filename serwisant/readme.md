


### Skroty

source env/bin/activate // wejdz do srodowiska

make install // instalacja

make run // uruchom raz projekt
make dev // uruchom watch projekt

### Enter to env

source env/bin/activate

### Run project

python app.py

#### watcher

python dev_runner.py

### Run Qt designer

designer

// or

pyqt6-tools designer

### Generate template from .ui file

pyuic6 gui_main_window.ui -o gui_main_window.py

### Build onefile for linux

pyinstaller --onefile app.py

// dir dist/

### Generate requirements

pip freeze > requirements.txt


### Alembic 

alembic revision --autogenerate -m "create items table"

Update database

alembic upgrade head