# Écrivez un programme qui crée un bytearray à partir d'une liste d'entiers, 
# puis modifie un de ses éléments.

# Créer une liste d'entiers
liste_entiers = [10, 20, 30, 40, 50]

# Créer un bytearray à partir de la liste d'entiers
byte_array = bytearray(liste_entiers)

# Afficher le bytearray d'origine
print("Bytearray d'origine :", byte_array)

# Modifier un élément du bytearray
index_modification = 2
valeur_modification = 35
byte_array[index_modification] = valeur_modification

# Afficher le bytearray après la modification
print("Bytearray après modification :", byte_array)
