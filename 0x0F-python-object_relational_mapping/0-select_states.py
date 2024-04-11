#!/usr/bin/python3
"""
List all states from the db using MySQLdb
"""
import MySQLdb
import sys
from sys import argv


def list_states(username, password, database):
    """
    Fetches unique states along with their minimum IDs from the MySQL database.
    """

    user, password, database = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
            user=username,
            passwd=password,
            db=database,
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
    db.close()


if __name__ == '__main__':
    if len(argv) != 4:
        exit(1)
    else:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

    list_states(mysql_username, mysql_password, database_name)
