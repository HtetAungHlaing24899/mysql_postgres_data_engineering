from dotenv import load_dotenv
import os

load_dotenv()

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
        'DB_TYPE': 'mysql',
        'DB_HOST': 'localhost',
        'DB_PORT': 3306,
        'DB_USER': os.getenv('MYSQL_USER'),
        'DB_PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'DB_NAME': os.getenv('MYSQL_DATABASE')
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgresql',
            'DB_HOST': 'localhost',
            'DB_PORT': 5432,
            'DB_USER': os.getenv('POSTGRES_USER'),
            'DB_PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'DB_NAME': os.getenv('POSTGRES_DB')
        },
    }
}