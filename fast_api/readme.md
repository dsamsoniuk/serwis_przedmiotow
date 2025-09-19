

# Projekt FastApi + JWT


## Install

1. docker compose up
2. create venv venv/
3. make migration seed.py

```
docker exec -it bash // to container console
docker exec -it pip list
docker exec -it api_fastapi alembic --version // execute once command
docker exec -it api_fastapi alembic upgrade head // execute once command
docker exec -it api_fastapi python seed.py // execute once command
```

### Create env project

python -m venv  venv

### Get in to envirement

source env/bin/active

### Seed fake data

python seed.py

### Display docs and debug

```
http://localhost:80/redoc

// debugger port
http://localhost:8000
```

### Generate migration

UWAGA! alembic tylko uzywac przez konsole docker

```
alembic revision --autogenerate -m "create items table"

// Update database

alembic upgrade head

alembic history

alembic downgrade -1
```

### Generate requirements

```
pip freeze > requirements.txt

// install all
pip install -r requirements.txt
```

### Test 

```
pytest
```

### Helped

https://blog.stackademic.com/using-fastapi-with-sqlalchemy-5cd370473fe5
