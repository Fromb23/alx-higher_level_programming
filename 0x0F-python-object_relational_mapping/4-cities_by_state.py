#!/usr/bin/python3
"""
This script connects to a MySQL database and
retrieves all rows from the 'cities' table,ordering
the results by 'id' in ascending order.
"""
import MySQLdb
import sys


def list_by_state(username, password, db_name):
    """
    Connects to the database and retrieves all cities,
    ordered by 'id' in ascending order.
    """
    db = MySQLdb.connect(
            user=username,
            passwd=password,
            host='localhost',
            port=3306,
            db=db_name,
            )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC;")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        list_by_state(username, password, db_name)
