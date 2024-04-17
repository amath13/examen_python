def unique_elements(liste):
    # Initialiser un dictionnaire pour stocker les éléments de la liste comme clés
    # et leur nombre d'occurrences comme valeurs (K_elements)
    K_elements = {}
    # Parcourir la liste et compter les occurrences de chaque élément
    for element in liste:
        K_elements[element] = K_elements.get(element, 0) + 1
    # Créer une nouvelle liste contenant uniquement les éléments uniques
    liste_uniques = [element for element, K_elements in K_elements.items() 
                     if K_elements == 1]

    return liste_uniques

# Tester la fonction avec une liste d'exemple
liste = [1, 2, 3, 4, 1, 2, 5, 6, 3,9,9,1,2,3,13]
reponse = unique_elements(liste)
print("Liste d'éléments uniques :", reponse)
