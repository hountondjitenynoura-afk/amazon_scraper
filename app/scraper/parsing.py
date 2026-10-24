
def extraire_produits(navigateur):
    articles = navigateur.find_elements(
        "css selector",
        "[data-component-type='s-search-result']"
    )

    produits = []

    for article in articles:
        try:
            nom = article.find_element(
                "css selector", "h2"
            ).text

            lien = article.find_element(
                "css selector", "a[href*='/dp/']"
            ).get_attribute("href")

            try:
                prix_element = article.find_element(
                    "css selector", ".a-price"
                )

                prix = prix_element.find_element(
                    "css selector", ".a-offscreen"
                ).get_attribute("textContent").strip()

            except Exception:
                prix = ""

            try:
                note = article.find_element(
                    "css selector", ".a-icon-alt"
                ).get_attribute("innerText")
            except Exception:
                note = ""

            try:
                nombre_avis = article.find_element(
                    "css selector",
                    "a[href*='#customerReviews']"
                ).text
            except Exception:
                nombre_avis = ""

            produit = {
                "nom": nom,
                "prix": prix,
                "note": note,
                "nombre_avis": nombre_avis,
                "url": lien
            }

            produits.append(produit)

        except Exception:
            continue

    return produits
