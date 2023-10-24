#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all states from the
`hbtn_0e_0_usa` database.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Check if the script is run as the main program.

    # Connect to the MySQL database.
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    # Create a cursor to execute SQL queries.
    cursor = db.cursor()

    # Execute the SQL query to select all states from the 'states' table.
    cursor.execute("SELECT * FROM states")

    # Fetch all the results.
    states = cursor.fetchall()

    # Display the results.
    for state in states:
        print(state)

    # Close the cursor and the database connection.
    cursor.close()
    db.close()
