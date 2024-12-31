FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD uvicorn fastapiapp.main:app --port=8000 --host=0.0.0.0