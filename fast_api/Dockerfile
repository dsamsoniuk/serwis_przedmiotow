# Use an official Python runtime as a parent image
FROM python:3.10


WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./api /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]

