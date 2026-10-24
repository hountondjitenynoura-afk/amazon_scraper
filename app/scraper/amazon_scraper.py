
from app.scraper.driver import ouvrir_navigateur
from app.scraper.parsing import extraire_produits
from selenium.common.exceptions import TimeoutException


def rechercher_produits(recherche):
    navigateur = ouvrir_navigateur()
    navigateur.set_page_load_timeout(40)

    url = "https://www.amazon.fr/s?k=" + recherche.replace(" ", "+")

    try:
        navigateur.get(url)
    except TimeoutException:
        print("La page met trop de temps a charger.")

    print("Titre de la page :", navigateur.title)
    print("Adresse :", navigateur.current_url)

    input("Chrome est ouvert. Observe la page, puis appuie sur Entree ici...")

    produits = extraire_produits(navigateur)

    print("Nombre de produits recuperes :", len(produits))

    navigateur.quit()
    return produits
