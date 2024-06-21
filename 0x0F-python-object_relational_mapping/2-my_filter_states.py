#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb


def filter_user_input(username, password, db_name, state_name):
    """
    Connects to the MySQL database and displays all
    values in the states table where name matches the argument.
    """

    # Establish a connect
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=db_name
            )

    # Creating a cursor obj
    cursor = db.cursor()

    # Executing a query with the provided state name
    cursor.execute("SELECT * FROM states WHERE name = BINARY '{:s}' \
                    ORDER BY id ASC;".format(state_name))

    # Fetching all the results
    rows = cursor.fetchall()

    # Printing the results
    for row in rows:
        print(row)

    # Closing the cursor and db connection
    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        filter_user_input(username, password, db_name, state_name)
