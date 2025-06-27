#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Prints all states starting with N and sorted by id
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = db.cursor()
<<<<<<< HEAD
    cur.execute("SELECT * FROM states "
                "WHERE BINARY name LIKE 'N%' "
                "ORDER BY id ASC"
                )
=======
    cur.execute(
        "SELECT * FROM states " "WHERE BINARY name LIKE 'N%' " "ORDER BY id ASC"
    )
>>>>>>> a51c919 (test)

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
