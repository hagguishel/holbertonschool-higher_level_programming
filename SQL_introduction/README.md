# 📘 Projet : Introduction à SQL et aux bases de données relationnelles

Ce projet est une introduction pratique aux bases de données relationnelles et au langage SQL, en particulier avec MySQL 8.0. Il vise à te rendre capable de manipuler des données, créer des structures de base et comprendre comment les systèmes de gestion de base de données fonctionnent.

---

## 🔍 Objectifs pédagogiques

À la fin de ce projet, tu devras être capable d'expliquer **sans Google** :

- ✅ Ce qu’est une **base de données**
- ✅ Ce qu’est une **base de données relationnelle**
- ✅ Ce que signifie **SQL** (Structured Query Language)
- ✅ Ce qu’est **MySQL**
- ✅ Comment **créer une base de données** dans MySQL
- ✅ Ce que signifient **DDL** (Data Definition Language) et **DML** (Data Manipulation Language)
- ✅ Comment **créer ou modifier** une table (`CREATE`, `ALTER`)
- ✅ Comment **lire** des données (`SELECT`)
- ✅ Comment **ajouter, mettre à jour ou supprimer** des données (`INSERT`, `UPDATE`, `DELETE`)
- ✅ Ce que sont les **sous-requêtes** (subqueries)
- ✅ Comment utiliser les **fonctions MySQL**
- ✅ La différence entre un **apostrophe `'`** et un **backtick `` ` ``

---

## 📚 Ressources utiles

- What is Database & SQL?
- Installer MySQL (MySQL Server)
- A Basic MySQL Tutorial
- Basic SQL statements: DDL and DML (pas besoin de lire “Privileges”)
- Basic queries: SQL and RA
- SQL technique: functions
- SQL technique: subqueries
- What makes the big difference between a backtick and an apostrophe?
- MySQL Cheat Sheet
- MySQL 8.0 SQL Statement Syntax

---

## 💻 Configuration requise

- Système : Ubuntu 20.04 LTS
- MySQL : version 8.0
- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous les fichiers SQL doivent :
  - Commencer par un **commentaire** décrivant la tâche
  - Contenir un **commentaire SQL** avant chaque requête
  - Avoir les **mots-clés SQL en majuscules** (`SELECT`, `WHERE`, etc.)
  - Se terminer par une **ligne vide**
  - Être testables avec la commande `wc`

---

## ⚙️ Installation de MySQL (Ubuntu 20.04)

```bash
sudo apt update
sudo apt install mysql-server
mysql --version
