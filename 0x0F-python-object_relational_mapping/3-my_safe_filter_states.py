#!/usr/bin/python3

import MySQLdb
import sys
"""
    This script connects to a MySQL database and retrieves
    the minimum id and name of states matching a given name.
    It takes four command-line arguments in the following
    order: username, password, database name, state name.
"""


if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    cursor = db.cursor()

    cursor.execute(("SELECT MIN(id), name FROM states "
                    "WHERE name = %s GROUP BY name", (sys.argv[4],)))

    rows = sorted(cursor.fetchall())

    for row in rows:
        print(row)

    cursor.close()
    db.close()
