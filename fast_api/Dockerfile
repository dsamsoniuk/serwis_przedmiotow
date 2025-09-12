# Use an official Python runtime as a parent image
FROM python:3.10


WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

EXPOSE 80

# CMD ["fastapi", "run", "app/main.py", "--port", "80"] # nie przeladuje zmian
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
