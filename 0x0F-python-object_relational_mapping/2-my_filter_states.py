#!/usr/bin/python3

import MySQLdb
import sys
from sys import argv

def matching_args(username, password, db_name, state_name):

    db = MySQLdb.connect(
            user=username,
            passwd=password,
            database=db_name,
            host='localhost',
            port=3306
            )

    cursor = db.cursor()



if __name__ == '__main__':
    if sys.argv != 5:
        exit(1)
    else:
        mysql_username = sys.argv[1]
        mysql_passwrd = sys.argv[2]
        mysql_db = sys.argv[3]
        mysql_state = sys.argv[4]

    matching_args(mysql_username, mysql_passwrd, mysql_db, mysql_state)
