#!/usr/bin/python3
"""Script to list all cities from the database"""

import sys
import MySQLdb


def main():
    """Main function to connect to MySQL and fetch cities"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
