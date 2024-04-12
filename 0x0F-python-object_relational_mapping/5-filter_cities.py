#!/usr/bin/python3
"""Script to list cities of a given state from a MySQL database."""

import MySQLdb
import sys


def list_cities_of_states(username, password, db_name, state_name):
    """List cities of a given state."""

    db = MySQLdb.connect(
            user=username,
            passwd=password,
            db=db_name,
            host='localhost',
            port=3306
            )

    cursor = db.cursor()

    sql_query = ("SELECT cities.name FROM cities "
                 "JOIN states ON cities.state_id = states.id "
                 "WHERE states.name = %s ORDER BY cities.id ASC")

    cursor.execute(sql_query, (state_name,))

    rows = cursor.fetchall()

    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 5:
        exit(1)
    else:
        _username = sys.argv[1]
        _passwd = sys.argv[2]
        _db_name = sys.argv[3]
        _state_name = sys.argv[4]

    list_cities_of_states(_username, _passwd, _db_name, _state_name)
