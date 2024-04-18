####################################################################################################################
# Vous gérez une base de données de produits pour un magasin en ligne, stockée sous forme de dictionnaire.         #
# Chaque clé du dictionnaire est l'identifiant du produit (un nombre entier), et chaque valeur est un autre        #
# dictionnaire contenant des informations sur le produit, y compris le prix et la quantité en stock. Votre         #
# tâche est de générer une liste de produits en rupture de stock (quantité en stock égale à 0) triée par prix,     #
# du plus cher au moins cher. Si deux produits ont le même prix, triez-les par leur identifiant en ordre croissant.#
####################################################################################################################


def produits_en_rupture_de_stock(base_de_donnees):
    """Fonction pour générer une liste de produits en rupture de stock triée par prix.
    Args:
        base_de_donnees (dict): Base de données des produits.
    Returns:
        list: Liste des produits en rupture de stock triée par prix.
    """
    # Filtrer les produits en rupture de stock
    produits_rupture_stock = {id_produit: infos_produit for id_produit, infos_produit in base_de_donnees.items() if infos_produit["quantite"] == 0}
    
    # Trier les produits en rupture de stock par prix, du plus cher au moins cher
    produits_tries = sorted(produits_rupture_stock.items(), key=lambda x: (-x[1]["prix"], x[0]))

    return produits_tries

def exemple_utilisateur():
    # Exemple de base de données de produits
    base_de_donnees = {
        1: {"nom": "Produit A", "prix": 10.99, "quantite": 0},
        2: {"nom": "Produit B", "prix": 5.99, "quantite": 0},
        3: {"nom": "Produit C", "prix": 15.99, "quantite": 0},
        4: {"nom": "Produit D", "prix": 8.99, "quantite": 0},
        5: {"nom": "Produit E", "prix": 15.99, "quantite": 0}
    }

    # Appel de la fonction pour générer la liste des produits en rupture de stock triée par prix
    liste_produits_rupture_stock = produits_en_rupture_de_stock(base_de_donnees)

    # Affichage des résultats
    print("Liste des produits en rupture de stock triée par prix (du plus cher au moins cher):")
    for id_produit, infos_produit in liste_produits_rupture_stock:
        print(f"Produit {id_produit}: {infos_produit['nom']} - Prix: {infos_produit['prix']}$ - Quantité en stock: {infos_produit['quantite']}")

# Appel de la fonction pour exécuter l'exemple utilisateur
exemple_utilisateur()
