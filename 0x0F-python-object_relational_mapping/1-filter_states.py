#!/usr/bin/python3
"""
This script connects to a MySQL database and
retrieves rows from the 'state' table
where the name starts with 'N',
ordering the results by 'id' in ascending order.
"""
import MySQLdb
import sys


def filter_state(username, password, db_name):
    """
    Connects to the database and retrieves states
    with names starting with 'N'.
    """
    db = MySQLdb.connect(
            user=username,
            passwd=password,
            port=3306,
            host='localhost',
            db=db_name
            )
    # creating a cursor obj
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")

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
        filter_state(username, password, db_name)
