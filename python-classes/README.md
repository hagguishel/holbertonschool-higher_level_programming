# 📘 0x06. Python - Classes et Objets

## 🧠 Contexte

Ce projet introduit les bases de la **programmation orientée objet (POO)** en Python.

Le point **le plus important** à retenir est :
> 💡 **Expérimente par toi-même, joue avec les concepts, teste, modifie et recommence.**
C’est en pratiquant que tu comprendras vraiment comment les classes fonctionnent.

---

## 📚 Ressources à lire/visionner (dans l'ordre)

Tu dois lire ou regarder **toutes** les ressources suivantes :

- **Object Oriented Programming** (Lis jusqu'au paragraphe “Inheritance” inclus – ignore la suite)
- **Object-Oriented Programming**
  Concentre-toi sur ces sections :
  - Introduction générale
  - Tout est objet (First-class Everything)
  - Une classe minimale en Python
  - Attributs (⚠️ pas besoin d'apprendre les attributs de classe)
  - Méthodes
  - La méthode spéciale `__init__`
  - Abstraction des données, encapsulation, masquage des informations
  - Attributs publics, protégés et privés
- **Propriétés vs Getters/Setters**
- **Learn to Program 9 : Object Oriented Programming (vidéo)**
- **Python Classes and Objects**
- **Object Oriented Programming (vidéo)**

---

## 🎯 Objectifs pédagogiques

À la fin de ce projet, tu dois être capable d’expliquer les notions suivantes **sans avoir besoin de Google** :

### Concepts généraux

- Qu’est-ce que la programmation orientée objet ?
- Que signifie “tout est objet” en Python ?
- Qu’est-ce qu’une **classe** ?
- Qu’est-ce qu’un **objet** ou une **instance** ?
- Quelle est la différence entre une classe et une instance ?
- Qu’est-ce qu’un **attribut** ?
- Quelle est la différence entre les attributs **publics**, **protégés** et **privés** ?
- Que représente `self` dans une classe ?
- Qu’est-ce qu’une **méthode** ?
- À quoi sert la méthode spéciale `__init__()` ?

### Gestion des données

- Qu’est-ce que l’**abstraction**, l’**encapsulation** et le **masquage des données** ?
- Qu’est-ce qu’une **propriété** (`@property`) ?
- Quelle est la différence entre une **propriété** et un **attribut** simple ?
- Quelle est la façon “Pythonique” d’écrire des **getters et setters** ?

### Comportements dynamiques

- Comment créer dynamiquement de nouveaux attributs dans une instance existante ?
- Comment lier un attribut à une **classe** ou à une **instance** ?
- Qu’est-ce que l’attribut spécial `__dict__` d’une classe ou d’un objet ?
- Comment Python trouve les attributs dans un objet ?
- Comment utiliser la fonction intégrée `getattr()` ?

---

## 🛠️ Exigences du projet

- Interprétation avec **Python 3.8.5** sur **Ubuntu 20.04 LTS**
- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous les fichiers doivent être **exécutables**
- Chaque script doit commencer par la ligne : `#!/usr/bin/python3`
- Le code doit respecter le style **pycodestyle v2.7.\***
- **Chaque module, classe et méthode doit contenir une docstring complète**
  - Utiliser le style [Google Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- Vérification des docstrings avec :
  ```bash
  python3 -c 'print(__import__("mon_module").__doc__)'
  python3 -c 'print(__import__("mon_module").MaClasse.__doc__)'
  python3 -c 'print(__import__("mon_module").ma_fonction.__doc__)'
