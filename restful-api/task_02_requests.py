#!/usr/bin/python3
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():

    reponse = requests.get(url)
    if reponse.status_code == 200:
        print("Status code: 200")
        post = reponse.json()
        for item in post:
            print(item["title"])

    else:
        print("Erreur : la requête a échoué")


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
            csv_data.append(dico_simplifier)

        with open("posts.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(csv_data)
