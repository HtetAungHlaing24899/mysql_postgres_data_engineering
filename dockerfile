FROM python:3.9

WORKDIR /app/mysql_postgres_data_engineering
COPY requirements.txt /app/mysql_postgres_data_engineering

RUN pip install -r requirements.txt

CMD ["python", "scripts/app.py", "dev"]