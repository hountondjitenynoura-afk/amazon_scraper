
def afficher_produits(produits):
    if len(produits) == 0:
        print("Aucun produit trouve.")
        return

    for produit in produits:
        print("----------------------------")
        print("Nom :", produit["nom"])
        print("Prix :", produit["prix"])
        print("Note :", produit["note"])
        print("Nombre d'avis :", produit["nombre_avis"])
        print("Lien :", produit["url"])
