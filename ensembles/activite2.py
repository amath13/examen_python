def difference_symetrique(e1, e2):
    # Calculer la différence symétrique entre les deux ensembles à l'aide de l'opérateur ^
    difference = e1 ^ e2
    return difference
# Définir deux ensembles d'exemple
e1 = {1, 2, 3, 4, 5,7}
e2 = {4, 5, 6, 7, 8,9}
# Appeler la fonction pour calculer la différence symétrique entre les ensembles
RESULT = difference_symetrique(e1,e2)
print("Différence symétrique entre les 2 ensembles :", RESULT)
