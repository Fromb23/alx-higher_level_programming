#!/usr/bin/python3
"""
This script lists states from a MySQL database whose names start with 'N'
"""

import MySQLdb
import sys
from sys import argv


def list_state_n(username, password, db_name):
    """
    List states from the MySQL database whose names start with 'N'
    """

    db = MySQLdb.connect(
            user=username,
            passwd=password,
            database=db_name,
            host='localhost',
            port=3306
            )

    cursor = db.cursor()

    sql_query = "SELECT MIN(id), name FROM states WHERE name LIKE 'N%' GROUP BY name"
    cursor.execute(sql_query)

    results = sorted(cursor.fetchall())

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(argv) != 4:
        exit(1)
    else:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

    list_state_n(mysql_username, mysql_password, database_name)
