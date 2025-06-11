#!/usr/bin/python3
# 👉 Indique au système d'exécuter ce script avec Python 3
import requests
import csv

# 👉 URL de l'API à contacter : elle renvoie une liste de faux articles (posts) au format JSON
url = "https://jsonplaceholder.typicode.com/posts"


# 🔹 Fonction pour afficher les titres de tous les posts reçus depuis l'API
def fetch_and_print_posts():

    reponse = requests.get(url)
    # 👉 Envoie une requête HTTP GET à l'URL et stocke la réponse dans la variable "reponse"
    if reponse.status_code == 200:
        print("Status code: 200")
        post = reponse.json()
        # 👉 Convertit la réponse JSON en objet Python (liste de dictionnaires)
        for item in post:
            print(item["title"])

    else:
        print("Erreur : la requête a échoué")


# 🔹 Fonction pour enregistrer les posts dans un fichier CSV
def fetch_and_save_posts():
    reponse = requests.get(url)
    if reponse.status_code == 200:
        print("Status code: 200")
        data = reponse.json()
        csv_data = []
        for post in data:
            dico_simplifier = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"],
            }
            # 👉 On crée un dictionnaire avec seulement les clés "id", "title" et "body"
            csv_data.append(dico_simplifier)

        with open("posts.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            # 👉 Crée un "écrivain CSV" qui sait gérer des dictionnaires avec ces 3 clés
            writer.writeheader()
            # 👉Écrit la première ligne (les noms de colonnes : id,title,body)
            writer.writerows(csv_data)
            # 👉 Écrit chaque dictionnaire de la liste comme une ligne du tableau
