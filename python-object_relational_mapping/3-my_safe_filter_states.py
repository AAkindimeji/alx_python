#!/usr/bin/python3
import MySQLdb

# Global variables for database connection
host = "127.0.0.1"
port = 3306
username = "learnakins"
password = "Akins@1234"
database = "hbtn_0e_0_usa"

def search_states(username, password, database, search_pattern):
    # Connect to the MySQL database
    connection = MySQLdb.connect(host=host, port=port, user=username, passwd=password, db=database)

    # Create a cursor object
    cur = connection.cursor()

    # Prepare the SQL query using parameterized format to prevent SQL injection
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    # Execute the SQL query with the search pattern parameter
    cur.execute(query, (search_pattern,))

    # Fetch and print the results
    for row in cur.fetchall():
        print(row)

    # Close all connections
    cur.close()
    connection.close()

def main():
    # Define the search pattern
    search_pattern = '%'  # This will find all states starting

    # Call the search_states function with the required parameters
    search_states(username, password, database, search_pattern)

if __name__ == "__main__":
    main()
