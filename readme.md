# MySQL to PostgreSQL Data Migration Tool Using Docker
This project is a Python-based exercise tool for migrating data from a MySQL database to a PostgreSQL database which are hosted on Docker.
The source is from "**itversity**" YouTube course. This repo is a modified version to enhance the end-to-end automation process.

## Features
- Reads table structures and data from MySQL
- Creates corresponding tables in PostgreSQL
- Migrates data from MySQL to PostgreSQL
- Supports batch inserts for efficient data loading

## Prerequisites
- Docker and Docker Compose
- Python 3.x

## Setup
1. Clone the repository
2. Create a .env file in the root directory with the following variables:
```
MYSQL_ROOT_PASSWORD=your_root_password
MYSQL_DATABASE=your_database_name
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_db
```