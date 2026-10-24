
from app.controllers.scraping_controller import lancer_scraping
from app.views.console_view import afficher_produits


recherche = input("Quel produit voulez-vous rechercher sur Amazon ? ")

produits = lancer_scraping(recherche)

afficher_produits(produits)
