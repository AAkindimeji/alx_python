import MySQLdb
import sys

# Global variables for the MySQL connection
host = "127.0.0.1"
port = 3306
mysql_username = "learnakins"
mysql_password = "Akins@1234"
database_name = "hbtn_0e_0_usa"  # Updated database name

def list_cities(state_name):
    """
    Lists all cities of a given state from the 'hbtn_0e_0_usa' database
    """
    # Connect to the MySQL database using global connection variables
    connection = MySQLdb.connect(host=host, port=port, user=mysql_username, passwd=mysql_password, db=database_name)
    cur = connection.cursor()

    # Using parameterized query to avoid SQL injection
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))

    query_results = cur.fetchall()
    for city in query_results:
        print(city[0])

    cur.close()
    connection.close()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        state_name = sys.argv[1]
        list_cities(state_name)
    else:
        print("Usage: script.py state_name")
