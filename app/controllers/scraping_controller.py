
from app.scraper.amazon_scraper import rechercher_produits
from app.models.produit import Produit
from app.models.depot import Depot
from app.views.export_view import exporter_csv


def lancer_scraping(recherche):
    produits_recuperes = rechercher_produits(recherche)

    depot = Depot()
    depot.vider_table()
    produits_csv = []

    for p in produits_recuperes:
        produit = Produit(
            p["nom"],
            p["prix"],
            p["note"],
            p["nombre_avis"],
            p["url"]
        )

        depot.ajouter_produit(produit)
        produits_csv.append(p)

    depot.fermer()
    exporter_csv(produits_csv)

    return produits_csv
