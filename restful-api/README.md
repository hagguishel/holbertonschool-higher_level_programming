# Projet RESTful API - README (FR)

## ✨ Introduction

Dans le monde en constante évolution du développement logiciel, savoir communiquer et transférer des données entre systèmes est fondamental. Ce projet explore les bases et les pratiques modernes autour des **APIs RESTful**, qui sont devenues un pilier incontournable dans l'univers des services web.

L'architecture REST (Representational State Transfer) repose sur un ensemble de contraintes qui garantissent un système de communication scalable, sans état, et cacheable. En résumé : des services web accessibles, simples et puissants.

## 🔧 Objectifs Pédagogiques

### ✅ Notions abordées :

* **Les bases de HTTP/HTTPS** : comprendre comment les données circulent sur le Web, et en quoi HTTPS diffère d'HTTP.
* **Consommation d'API en ligne de commande** avec `curl`.
* **Consommation d'API en Python** avec la librairie `requests`, puis export en CSV.
* **Création d'une API simple** avec le module `http.server` de Python.
* **Création d'une API plus avancée** avec Flask.
* **Sécurité et authentification** des APIs (Basic Auth et JWT).
* **Standardisation et documentation d'API** avec OpenAPI (non inclus dans les tâches ici mais mentionné comme notion clé).

## 🤖 Schéma Conceptuel : API REST

```
+-------+           +-------+           +---------+           +---------+
|Client |  Request  | Web   |  Process  |  API    |  Fetch/   |Database |
|       |   ----->  |Server |  -------> | Server |  Modify   |         |
|       | <-----    |       | <-------  |        |           |         |
|       | Response  |       |  Return   |        |           |         |
+-------+           +-------+           +---------+           +---------+
```

* **Client** : navigateur, app mobile, outil CLI...
* **Web Server** : reçoit la requête HTTP(S), peut faire du routage.
* **API Server** : logique métier, gère les requêtes.
* **Base de données** : récupère ou modifie les données.

## 🗒️ Tâches

### 0. Bases de HTTP/HTTPS

* Différencier HTTP et HTTPS
  > **HTTPS est comme HTTP, mais sécurisé grâce au chiffrement des données via SSL/TLS.**
  > Ils utilisent des ports différents : **80 pour HTTP** et **443 pour HTTPS**.
  > ✅ *Résumé : HTTPS = HTTP + sécurité (via SSL/TLS).*
  > HTTP convient aux sites simples, HTTPS aux sites nécessitant une protection des données.
* Comprendre la structure d'une requête et réponse HTTP
* Identifier les méthodes (GET, POST...) et codes (200, 404, 500...)

### 1. Consommer une API en ligne de commande (avec `curl`)

* Récupérer des données JSON depuis `https://jsonplaceholder.typicode.com`
* Utiliser les options `-X`, `-d`, `-I`...

### 2. Consommer et traiter une API avec Python

* Utiliser `requests.get()` pour récupérer des posts
* Parser les réponses JSON et extraire les titres
* Exporter les données au format CSV avec `csv.DictWriter`

### 3. Créer une API simple avec `http.server`

* Répondre à des requêtes GET ("/", "/data", "/status")
* Renvoyer du JSON, gérer les headers
* Retourner une 404 pour les routes inconnues

### 4. Créer une API avec Flask

* Créer des routes ("/", "/data", "/status", "/users/<username>")
* Stocker les utilisateurs dans un dictionnaire en mémoire
* Gérer les POST pour créer de nouveaux utilisateurs ("/add\_user")

### 5. Authentification et Sécurité

* Authentification de base avec `Flask-HTTPAuth`
* Authentification par token (JWT) avec `Flask-JWT-Extended`
* Routes protégées : `@auth.login_required` et `@jwt_required()`
* Accès basé sur les rôles : route `admin-only`

## 📈 Importance

Dans un monde hyperconnecté, les APIs REST sont les artères qui relient les applications. Que ce soit pour afficher les publications Instagram dans une app tierce ou pour synchroniser un thermostat avec un smartphone, les APIs sont partout. Maîtriser leur usage, leur création et leur sécurité est aujourd'hui une compétence essentielle pour tout développeur.

## 📄 Structure du projet

* **GitHub repo** : `holbertonschool-higher_level_programming`
* **Dossier** : `restful-api`
* **Fichiers principaux** :

  * `task_02_requests.py`
  * `task_03_http_server.py`
  * `task_04_flask.py`
  * `task_05_basic_security.py`

---

Ce README a pour but de vous fournir une vue d'ensemble claire, cohérente et didactique du projet. N'oubliez pas : une bonne API, c'est comme un bon serveur à table, discret, efficace, et toujours à l'écoute !
