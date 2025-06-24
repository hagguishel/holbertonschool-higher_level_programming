# 📊 SQL - Introduction & Manipulation de Données

Ce projet a pour objectif de te familiariser avec la manipulation de bases de données relationnelles en SQL (MySQL 8.0), à travers la création, la gestion d’utilisateurs, l’usage des jointures, des sous-requêtes et la modélisation de données avec des contraintes.

---

## 📚 Ressources recommandées

Avant de commencer, tu peux consulter ces ressources (certaines sont obligatoires) :

- [Créer un utilisateur MySQL et gérer ses permissions](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [Documentation officielle sur GRANT en MySQL](https://www.mysqltutorial.org/mysql-grant.aspx)
- [Les contraintes SQL (PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, etc.)](https://www.mysqltutorial.org/mysql-constraints.aspx)
- **SQL Style Guide** – normes d’écriture pour requêtes SQL
- **UML & Design relationnel**
  - Normalisation
  - Modélisation entité-relation (ER)
- Techniques SQL :
  - Jointures (`INNER`, `LEFT`, `RIGHT`, `FULL OUTER`)
  - Jointures multiples
  - Mots-clés `DISTINCT`, `UNION`, `MINUS`
  - Sous-requêtes

---

## 🎯 Objectifs pédagogiques

À la fin de ce projet, tu seras capable d'expliquer (sans Google !) :

### Général
- Comment créer un nouvel utilisateur MySQL
- Comment gérer les droits (GRANT/REVOKE) sur une base ou une table
- À quoi sert une **clé primaire** (`PRIMARY KEY`)
- À quoi sert une **clé étrangère** (`FOREIGN KEY`)
- Comment utiliser les contraintes `NOT NULL` et `UNIQUE`
- Comment faire une **jointure** entre plusieurs tables
- Ce qu’est une **sous-requête**
- La différence entre **JOIN** et **UNION**

---

## 🧾 Contraintes du projet

- ✅ Tous les fichiers sont exécutés sur Ubuntu 20.04 LTS avec MySQL 8.0.25
- ✅ Éditeurs autorisés : `vi`, `vim`, `emacs`
- ✅ Chaque fichier SQL commence par un commentaire décrivant la tâche
- ✅ Chaque requête SQL est précédée d’un commentaire décrivant ce qu’elle fait
- ✅ Les mots-clés SQL doivent être en **MAJUSCULE** (`SELECT`, `WHERE`, etc.)
- ✅ Tous les fichiers se terminent par une ligne vide
- ✅ Un fichier `README.md` est obligatoire à la racine du projet

---

## 🛠 Exemples de commandes utiles

### Lancer un script SQL :
```bash
cat 0-list_databases.sql | mysql -uroot -p
