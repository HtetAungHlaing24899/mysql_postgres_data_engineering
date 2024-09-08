from util import get_connection

def build_insert_query(table_name, column_names):
    column_values = tuple(map(lambda column: column.replace(column, '%s'), column_names))
    query = (f'''
        INSERT INTO {table_name} {column_names} VALUES {column_values}
    ''')
    return query

def insert_data(connection, cursor, query, data, batch_size = 100):
    recs = []
    count = 1
    for rec in data:
        recs.append(rec)
        if count % batch_size == 0:
            cursor.executemany(query, recs)
            connection.commit()
            recs = []
        count = count + 1
    cursor.executemany(query, recs)
    connection.commit()