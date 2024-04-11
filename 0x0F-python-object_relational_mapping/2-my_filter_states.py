#!/usr/bin/python3
"""
    This script displays all values in the states table of a MySQL
    database where the name matches the provided argument
"""

import MySQLdb
import sys
from sys import argv


def matching_args(username, password, db_name, state_name):
    """
    Searches for states in the MySQL database based on the provided state name
    """

    db = MySQLdb.connect(
            user=username,
            passwd=password,
            database=db_name,
            host='localhost',
            port=3306
            )

    cursor = db.cursor()

    sql_query = ("SELECT MIN(id), name FROM states WHERE "
                 "name = '{}' GROUP BY name".format(state_name))

    cursor.execute(sql_query)

    results = sorted(cursor.fetchall())

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 5:
        exit(1)
    else:
        mysql_username = sys.argv[1]
        mysql_passwrd = sys.argv[2]
        mysql_db = sys.argv[3]
        mysql_state = sys.argv[4]

    matching_args(mysql_username, mysql_passwrd, mysql_db, mysql_state)
