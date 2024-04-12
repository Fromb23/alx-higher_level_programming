#!/usr/bin/python3

import MySQLdb
import sys
"""
    This script connects to a MySQL database and retrieves
    the minimum id and name of states matching a given name.
    It takes four command-line arguments in the following
    order: username, password, database name, state name.
"""


def fetch_state_info(username, password, database, state_name):
    """
    Fetches the minimum ID and name of states
    from a MySQL database for a given state name.

    Args:
        username (str): The username for MySQL database connection.
        password (str): The password for MySQL database connection.
        database (str): The name of the database to connect to.
        state_name (str): The name of the state to fetch information for.

    Returns:
        None

    Prints:
        The minimum ID and name of states matching the given state name.
    """
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
            )

    cursor = db.cursor()

    cursor.execute(("SELECT MIN(id), name FROM states "
                    "WHERE name = %s GROUP BY name"), (state_name,))

    rows = sorted(cursor.fetchall())

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 5:
        sys.exit(1)

    fetch_state_info(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
