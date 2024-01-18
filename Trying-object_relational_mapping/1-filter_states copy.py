#!/usr/bin/python3
import MySQLdb
import os

def main():
    # Retrieve database credentials from environment variables
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', 3306)
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')

    # Validate if all required information is available
    if not all([db_host, db_port, db_user, db_pass, db_name]):
        print("Error: Missing database configuration environment variables.")
        return

    # Ensure db_port is an integer
    try:
        db_port = int(db_port)
    except ValueError:
        print("Error: DB_PORT environment variable must be an integer.")
        return

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host=db_host, port=db_port, user=db_user, passwd=db_pass, db=db_name)

        # Create a cursor object
        cur = db.cursor()

        # Execute the SQL query
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        # Fetch and print the results
        for row in cur.fetchall():
            print(row)

        # Close all connections
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Database connection error: {e}")
        return

if __name__ == "__main__":
    main()
