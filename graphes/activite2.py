def dfs(graphe, sommet, visite=[]):
    
######################################################################################"######
# Implémentez le parcours en profondeur (DFS) sur un graphe représenté par un dictionnaire. #
##############################################################################################

    """Parcours en profondeur (DFS) sur un graphe représenté par un dictionnaire.
    Args:
        graphe (dict): Le graphe représenté par un dictionnaire.
        sommet (str): Le sommet à partir duquel commencer le parcours.
        visite (list): Liste des sommets visités (par défaut, une liste vide).

    Returns:
        list: Liste des sommets visités dans l'ordre DFS.
    """
    # Marquer le sommet actuel comme visité
    visite.append(sommet)
    # Parcourir les sommets voisins non visités du sommet actuel
    for voisin in graphe[sommet]:
        if voisin not in visite:
            # Appel récursif de dfs pour visiter le voisin
            dfs(graphe, voisin, visite)
    return visite

def exemple_utilisateur():
    # Définition du graphe sous forme de dictionnaire
    graphe = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Sommet de départ pour le parcours DFS
    sommet_depart = 'A'

    # Appel de la fonction dfs pour effectuer le parcours DFS
    sommets_visites = dfs(graphe, sommet_depart)

    # Affichage des sommets visités dans l'ordre DFS
    print("Parcours en profondeur (DFS) à partir du sommet", sommet_depart, ":", sommets_visites)

# Appel de la fonction pour exécuter l'exemple utilisateur
exemple_utilisateur()