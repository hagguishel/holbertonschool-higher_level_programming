#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )

    # Création du curseur
    cur = db.cursor()

    # Exécution de la requête SQL
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Récupération et affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture
    cur.close()
    db.close()
