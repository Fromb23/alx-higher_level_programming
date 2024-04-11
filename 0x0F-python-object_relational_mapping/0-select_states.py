#!/usr/bin/python3

import MySQLdb

connection = MySQLdb.connect(
        user='root',
        password='root@2024',
        database='hbtn_0e_0_usa',
        host='localhost',
        port=3306
        )

# Cursor object
cursor = connection.cursor()

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
