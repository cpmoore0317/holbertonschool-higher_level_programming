#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all states from the
`hbtn_0e_0_usa` database.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
