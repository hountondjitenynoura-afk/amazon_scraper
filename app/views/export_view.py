
import csv


def exporter_csv(produits):
    with open("exports/produits.csv", "w", newline="", encoding="utf-8-sig") as fichier:
        colonnes = ["nom", "prix", "note", "nombre_avis", "url"]

        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()
        writer.writerows(produits)

    print("Les produits ont ete enregistres dans le fichier CSV.")
