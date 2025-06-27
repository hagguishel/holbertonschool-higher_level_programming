#!/usr/bin/python3
"""exo 1"""
import MySQLdb

"""
Connecte à une base MySQL et affiche les lignes de la table 'states',
triées par id croissant, sous la forme : <id>: <name>.
"""
if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(f"{row[0]}: {row[1]}")
    cur.close()
    conn.close()
