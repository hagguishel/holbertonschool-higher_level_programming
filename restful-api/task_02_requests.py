import requests
import csv


def fetch_and_print_posts():
    """
    Récupère les posts depuis JSONPlaceholder et affiche leurs titres.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Affiche le code de réponse HTTP
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Convertit la réponse JSON en liste de dictionnaires
        posts = response.json()

        # Affiche le titre de chaque post
        for post in posts:
            print(post["title"])
    else:
        # En cas d'erreur, affiche un message
        print("Erreur lors de la récupération des posts.")


def fetch_and_save_posts():
    """
    Récupère les posts depuis JSONPlaceholder et les enregistre dans un CSV.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        # Convertit la réponse JSON en liste de dictionnaires
        posts = response.json()

        # Garde uniquement les champs 'id', 'title' et 'body'
        simplified_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Ouvre le fichier CSV en écriture
        with open("posts.csv", mode="w", encoding="utf-8", newline="") as fichier:
            champs = ["id", "title", "body"]

            # Initialise le writer CSV avec les bons champs
            writer = csv.DictWriter(fichier, fieldnames=champs)

            # Écrit l'en-tête du fichier CSV
            writer.writeheader()

            # Écrit toutes les lignes de posts
            writer.writerows(simplified_posts)
    else:
        # En cas d'erreur, affiche un message
        print("Erreur lors de la récupération des posts.")
