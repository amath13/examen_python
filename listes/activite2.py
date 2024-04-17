# Écrivez un programme Python qui effectue une rotation à droite des éléments d'une liste. 
# La rotation doit être définie par l'utilisateur.

def rotation_droite(liste, n):
    n = n % len(liste)  # Pour gérer les rotations supérieures à la longueur de la liste
    return liste[-n:] + liste[:-n]

# Demander à l'utilisateur d'entrer les éléments de la liste
elements = input("Entrez les éléments de la liste (séparés par une virgule) : ").split(',')

# Demander à l'utilisateur le nombre de rotations à droite
rotation = int(input("Entrez le nombre de rotations à droite : "))

# Convertir les éléments en liste d'entiers
elements = [int(element) for element in elements]

# Effectuer la rotation à droite
list_rotation = rotation_droite(elements, rotation)

# Afficher la liste après la rotation
print("Liste après la rotation à droite :", list_rotation)
