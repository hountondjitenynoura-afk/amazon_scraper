
import sqlite3

connexion = sqlite3.connect("data/amazon.db")
curseur = connexion.cursor()

curseur.execute("SELECT COUNT(*) FROM produits")
nombre = curseur.fetchone()[0]

print("Nombre de produits dans la base :", nombre)

curseur.execute("SELECT nom, prix FROM produits LIMIT 5")
produits = curseur.fetchall()

for produit in produits:
    print("Nom :", produit[0])
    print("Prix :", produit[1])
    print("----------------------")

connexion.close()
