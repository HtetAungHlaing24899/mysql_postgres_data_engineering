import pandas as pd
from config import DB_DETAILS
from mysql import connector as mc
from mysql.connector import errorcode as ec
import psycopg2 as pg

#load db details from config
def load_db_details(env):
    return DB_DETAILS[env]

#get mysql connection
def get_mysql_connection(db_user, db_password, db_host, db_port, db_name):
    try:
        conn = mc.connect(user=db_user, 
                                 password=db_password, 
                                 host=db_host, 
                                 port=db_port, 
                                 database=db_name)
        
    except mc.Error as e:
        if e.errno == ec.ER_ACCESS_DENIED_ERROR:
            print('Invalid Credentials')
        else:
            print(e)
    return conn

#get postgres connection
def get_postgres_connection(db_user, db_password, db_host, db_port, db_name):
    try:
        conn = pg.connect(user=db_user, 
                           password=db_password, 
                           host=db_host, 
                           port=db_port, 
                           database=db_name)
    except pg.Error as e:
        print(e)
    return conn

#get connection for any db type
def get_connection(db_type, db_user, db_password, db_host, db_port, db_name):
    conn = None
    if db_type == 'mysql':
        conn = get_mysql_connection(db_user=db_user, 
                                    db_password=db_password, 
                                    db_host=db_host, 
                                    db_port=db_port, 
                                    db_name=db_name)
    elif db_type == 'postgresql':
        conn = get_postgres_connection(db_user=db_user, 
                                       db_password=db_password, 
                                       db_host=db_host, 
                                       db_port=db_port, 
                                       db_name=db_name)
    return conn

#get table list
def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    return tables.query('to_be_loaded == "yes"')