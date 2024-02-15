#!/usr/bin/python3
"""Script to display values from the states table based on user input"""

import sys
import MySQLdb


def main():
    """Main function to connect to MySQL and fecth data"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        (state_name,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
