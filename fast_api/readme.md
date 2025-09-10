

tutorial

https://blog.stackademic.com/using-fastapi-with-sqlalchemy-5cd370473fe5


### Create env project

python venv -m env

### Get in to envirement

source env/bin/active

### Run server

fastapi dev main.py


### Seed fake data

python api/seed.py

### Display docs

http://localhost:8000/redoc


### Generate migration

alembic revision --autogenerate -m "create items table"

Update database

alembic upgrade head


### Generate requirements

pip freeze > requirements.txt

// install all
pip install -r requirements.txt