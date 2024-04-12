#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def list_all_cities(username, password, database):
    """
    Lists all cities from the database hbtn_0e_4_usa
    """

    db = MySQLdb.connect(
            usrname=username,
            passwd=password,
            db_name=database,
            host='localhost',
            port=3306
            )

    cursor = db.cursor()

    sql_query = "SELECT * FROM cities ORDER BY id ASC"

    cursor.execute(sql_query)

    rows = sorted(cursor.fetchall())

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    if sys.argv != 4:
        exit(1)
    else:
        _username = sys.argv[1]
        _passwd = sys.argv[2]
        _db = sys.argv[3]

    list_all_cities(_username, _passwd, _db)
