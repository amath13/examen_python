# Écrivez un programme qui trouve l'intersection de deux ensembles.

def intersection_ensembles(ensemble1, ensemble2):
    """
    Retourne l'intersection de deux ensembles.
    """
    return ensemble1.intersection(ensemble2)

# Deux ensembles d'exemple
ensemble1 = {1, 2, 3, 4, 0}
ensemble2 = {4, 9, 6, 7, 8}

# Trouver l'intersection des deux ensembles
intersection = intersection_ensembles(ensemble1, ensemble2)

# Afficher l'intersection
print("Intersection des ensembles :", intersection)
