import sys
from config import DB_DETAILS
from util import get_tables
from util import load_db_details
from read import read_table

def main():
    #getting arguments from command line and get db_details based on the argument
    env = sys.argv[1]
    db_details = load_db_details(env)

    #reading data from db
    tables = get_tables('../table_list.txt')
    for table_name in tables['table_name']:
        data, columns = read_table(db_details, table_name)
    
    for column in columns:
        print(column)


if __name__ == '__main__':
    main()