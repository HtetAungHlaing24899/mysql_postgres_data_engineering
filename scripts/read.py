from util import get_connection

def connect_mysql(SOURCE_DB):
    conn = get_connection(db_type=SOURCE_DB['DB_TYPE'],
                          db_user=SOURCE_DB['DB_USER'],
                          db_password=SOURCE_DB['DB_PASSWORD'],
                          db_host=SOURCE_DB['DB_HOST'],
                          db_port=SOURCE_DB['DB_PORT'],
                          db_name=SOURCE_DB['DB_NAME'])
    
    return conn

def read_table(DB_DETAILS, table_name, limit=0):
    SOURCE_DB = DB_DETAILS['SOURCE_DB']
    conn = connect_mysql(SOURCE_DB)
    cur = conn.cursor()

    if limit == 0:
        query = f'SELECT * FROM {table_name}'
    else:
        query = f'SELECT * FROM {table_name} LIMIT {limit}'

    cur.execute(query)
    data = cur.fetchall()
    column_names = cur.column_names

    conn.close()
    return data, column_names

def read_column_types(DB_DETAILS, table_name):
    SOURCE_DB = DB_DETAILS['SOURCE_DB']
    conn = connect_mysql(SOURCE_DB)
    cur = conn.cursor()

    query = f'DESCRIBE {table_name}'
    cur.execute(query)
    columns = cur.fetchall()

    column_names = []
    column_types = []

    for column in columns:
        column_names.append(column[0])
        column_types.append(column[1])

    return column_names, column_types






