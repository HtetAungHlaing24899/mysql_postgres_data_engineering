import sys
from config import DB_DETAILS
from util import get_tables

def main():
    #getting arguments from command line and get db_details based on the argument
    env = sys.argv[1]
    db_details = DB_DETAILS[env]

    #getting table list from the csv
    tables = get_tables('../table_list.txt')
    for table in tables['table_name']:
        print(table)


if __name__ == '__main__':
    main()