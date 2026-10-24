
import sqlite3


class Depot:
    def __init__(self):
        self.connexion = sqlite3.connect("data/amazon.db")
        self.creer_table()

    def creer_table(self):
        curseur = self.connexion.cursor()

        curseur.execute("""
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                prix TEXT,
                note TEXT,
                nombre_avis TEXT,
                url TEXT
            )
        """)

        self.connexion.commit()

    def vider_table(self):
        curseur = self.connexion.cursor()
        curseur.execute("DELETE FROM produits")
        self.connexion.commit()

    def ajouter_produit(self, produit):
        curseur = self.connexion.cursor()

        curseur.execute("""
            INSERT INTO produits (nom, prix, note, nombre_avis, url)
            VALUES (?, ?, ?, ?, ?)
        """, (
            produit.nom,
            produit.prix,
            produit.note,
            produit.nombre_avis,
            produit.url
        ))

        self.connexion.commit()

    def fermer(self):
        self.connexion.close()
