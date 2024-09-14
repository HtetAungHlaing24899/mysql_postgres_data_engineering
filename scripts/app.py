import sys
from config import DB_DETAILS, TYPE_MAPPING
from util import get_tables
from util import load_db_details
from read import read_table, read_column_types
from write import load_table
from create import create_table

def main():
    #getting arguments from command line and get db_details based on the argument
    env = sys.argv[1]
    db_details = load_db_details(env)

    #reading data from db
    tables = get_tables('../table_list.txt')
    for table_name in tables['table_name']:
        print(f'reading data for {table_name}')

        #reading data from mysql
        data, columns = read_table(db_details, table_name)

        #reading column types from mysql to create a new table in postgres
        column_names, column_types = read_column_types(db_details, table_name)

        #replacing column types with postgres types using dict
        for i in range(len(column_types)):
            column_types[i] = TYPE_MAPPING[column_types[i]]

        #create table in postgres
        print(f'creat table {table_name} in postgres server')
        create_table(db_details, table_name, column_names, column_types)
        print(f'completed creating table')

        #load data into postgres
        print(f'loading data for {table_name}')
        load_table(db_details, data, column_names, table_name)


if __name__ == '__main__':
    main()