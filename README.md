# Projet Amazon Scraper

## 1. Présentation du projet

Ce projet permet de rechercher des produits sur Amazon.fr et de récupérer certaines informations sur ces produits à l'aide de Python et Selenium.

Les informations récupérées sont :
- Le nom du produit
- Le prix
- La note
- Le nombre d'avis
- Le lien du produit

## 2. Technologies utilisées

- Python
- Selenium
- SQLite
- CSV

## 3. Organisation du projet

- `main.py` : fichier principal du programme
- `app/controllers/` : gestion du déroulement du scraping
- `app/models/` : gestion des produits et de la base de données
- `app/scraper/` : ouverture du navigateur et récupération des données
- `app/views/` : affichage des résultats et export CSV
- `data/amazon.db` : base de données SQLite
- `exports/produits.csv` : fichier CSV contenant les produits récupérés
- `requirements.txt` : liste des dépendances Python

## 4. Installation

Installer les dépendances avec la commande suivante :

```bash
python -m pip install -r requirements.txt
```

## 5. Exécution

Depuis le dossier principal du projet, exécuter :

```bash
python main.py
```

Saisir ensuite le nom du produit à rechercher.

## 6. Stockage des données

Les produits récupérés sont enregistrés dans deux formats :

- Une base de données SQLite : `data/amazon.db`
- Un fichier CSV : `exports/produits.csv`

À chaque nouvelle recherche, les produits précédemment enregistrés dans la base de données et dans le fichier CSV sont remplacés par les nouveaux résultats.

## 7. Architecture

Le projet suit une organisation inspirée du modèle MVC (Modèle-Vue-Contrôleur), avec une séparation entre la gestion des données, le traitement du scraping et l'affichage des résultats.