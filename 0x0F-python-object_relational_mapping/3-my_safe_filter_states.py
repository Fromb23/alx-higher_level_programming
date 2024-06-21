#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
"""
import MySQLdb
import sys


def find_state_by_name_safe(username, password, db_name, state_name):
    """
    Connects to MySQL and retrieves states matching state_name.
    """
    # Establishing a connection to the database
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=db_name
            )

    # Creating a cursor object
    cursor = db.cursor()

    # Formulating the query using parameterized queries to avoid SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Executing the query with the provided state name
    cursor.execute(query, (state_name,))

    # Fetching all the results
    rows = cursor.fetchall()

    # Printing the results
    for row in rows:
        print(row)

    # Closing the cursor and database connection
    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        find_state_by_name_safe(username, password, db_name, state_name)
