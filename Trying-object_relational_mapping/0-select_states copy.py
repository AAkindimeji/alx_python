#!/usr/bin/python3
"""
A script that connects to a SQL database without hardcoding sensitive information.
"""

import MySQLdb
import os
import sys

def list_states():
    """
    Connects to a MySQL database and lists all states.
    """
    db_host = os.environ.get('DB_HOST')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')

    if None in [db_host, db_user, db_pass, db_name]:
        print("Please set the environment variables: DB_HOST, DB_USER, DB_PASS, DB_NAME")
        sys.exit(1)

    db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_pass, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    list_states()
