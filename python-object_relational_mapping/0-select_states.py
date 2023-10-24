#!/usr/bin/python3
import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    sys.exit(1)

username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

# Connect to the MySQL server
db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)

# Create a cursor object
cursor = db.cursor()

# Execute the SQL query to select states and order by states.id
query = "SELECT * FROM states ORDER BY states.id"
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Display the results
for row in results:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()
