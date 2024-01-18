#!/usr/bin/python3
import MySQLdb
import sys

host = "127.0.0.1"
port = 3306
username = "learnakins"
password = "Akins@1234"
database = "hbtn_0e_0_usa"
# Connect to the MySQL database
connection = MySQLdb.connect(host="127.0.0.1", port=3306, user=username, passwd=password, db=database)

# Create a cursor object
cur = connection.cursor()

# Execute the SQL query
cur.execute("SELECT * FROM cities ORDER BY id ASC")

# Fetch and print the results
for row in cur.fetchall():
    print(row)

# Close all connections
cur.close()
connection.close()

def main():
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        (username, password, dbname)
    else:
        print("Usage: ./script.py <mysql username> <mysql password> <database name>")

    if __name__ == "__main__":
        main()
