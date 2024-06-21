#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves
all cities from a specified state,ordering the
results by 'cities.id' in ascending order.
"""
import MySQLdb
import sys


def sort_cities(username, password, db_name, state_name):
    """
    Connects to the database and retrieves cities for a given state.
    """
    db = MySQLdb.connect(
            user=username,
            passwd=password,
            host='localhost',
            port=3306,
            db=db_name
            )
    cursor = db.cursor()

    cursor.execute("""SELECT cities.* FROM cities JOIN states
                    ON cities.state_id = states.id WHERE states.name = %s
                    ORDER BY cities.id ASC;""", (state_name,))

    rows = cursor.fetchall()

    for i in range(len(rows)):
        if i != len(rows) - 1:
            print(rows[i][2], end=', ')
        else:
            print(rows[i][2])

    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        sort_cities(username, password, db_name, state_name)
