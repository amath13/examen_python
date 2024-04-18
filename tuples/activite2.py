def inverse_tuples(liste_tuples):
    # Créer une liste vide pour stocker les tuples inversés
    tuples_inverse = []
    # Parcourir chaque tuple dans la liste
    for k in liste_tuples:
        # Inverser l'ordre des éléments dans le tuple et l'ajouter à la liste des tuples inversés
        tuples_inverse.append(tuple(reversed(k)))
    return tuples_inverse
# Exemple pour tester la fonction avec une liste de tuples 
liste_de_tuples = [(1, 2), (3, 4), (5, 6),(7,8)]
réponse = inverse_tuples(liste_de_tuples)
print("La liste de tuples inversés :", réponse)
