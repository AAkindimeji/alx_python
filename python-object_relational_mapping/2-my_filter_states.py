#!/usr/bin/python3
import MySQLdb

# Global variables for database connection
host = "127.0.0.1"
port = 3306
username = "learnakins"
password = "Akins@1234"
database = "hbtn_0e_0_usa"

def search_states():
    # Connect to the MySQL database
    connection = MySQLdb.connect(host=host, port=port, user=username, passwd=password, db=database)

    # Create a cursor object
    cur = connection.cursor()

    # Prepare the SQL query to select all states
    query = "SELECT * FROM states ORDER BY id ASC"
    
    # Execute the SQL query
    cur.execute(query)

    # Fetch and print the results
    for row in cur.fetchall():
        print(row)

    # Close all connections
    cur.close()
    connection.close()

def main():
    search_states()

if __name__ == "__main__":
    main()
