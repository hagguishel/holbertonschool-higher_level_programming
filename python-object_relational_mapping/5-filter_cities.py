#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Prints corresponding values
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    state_name = sys.argv[4]

    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC",
        (state_name,),
    )

    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))
    cur.close()
    db.close()
