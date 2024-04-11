#!/usr/bin/python3
"""
List all states from the db using MySQLdb
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    if len(argv) != 4:
        exit(1)

    user, password, database = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
            user=user,
            password=password,
            database=database,
            host='localhost',
            port=3306
            )

    # Cursor object
    cursor = db.cursor()

    # Execute sql queries
    cursor.execute('SELECT MIN(id) as id, name FROM states GROUP BY name')

    # Fetch the results
    results = cursor.fetchall()

    results = sorted(results)
    for row in results:
        print(row)

    # Close Connection
    cursor.close()
    connection.close()
