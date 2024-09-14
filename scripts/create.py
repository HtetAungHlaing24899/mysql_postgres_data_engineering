from util import get_connection

def build_create_query(table_name, column_names, column_types):
    columns_list = [f'{name} {type}' for name, type in zip(column_names, column_types)]
    create_column = ', '.join(columns_list)
    query = f'''
                CREATE TABLE IF NOT EXISTS {table_name} ({create_column})
            '''
    
    #print(f'create query : {query}')
    
    return query

def create_table(DB_DETAILS, table_name, column_names, column_types):
    TARGET_DB = DB_DETAILS['TARGET_DB']

    conn = get_connection(db_type=TARGET_DB['DB_TYPE'],
                          db_user=TARGET_DB['DB_USER'],
                          db_password=TARGET_DB['DB_PASSWORD'],
                          db_host=TARGET_DB['DB_HOST'],
                          db_port=TARGET_DB['DB_PORT'],
                          db_name=TARGET_DB['DB_NAME'])
    
    cur = conn.cursor()
    query = build_create_query(table_name, column_names, column_types)
    cur.execute(query)
    conn.commit()

    conn.close()