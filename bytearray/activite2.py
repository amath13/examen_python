############################################################################################################
# Écrivez un programme qui parcourt un bytearray, affiche chaque élément, puis ajoute 1 à chaque élément.  #
############################################################################################################

def parcourir_et_incrementer(bytearray_input):
    # Parcourt chaque indice du bytearray
    for i in range(len(bytearray_input)):
        # Affiche l'élément à l'indice i et sa valeur
        print("Élément à l'indice", i, ":", bytearray_input[i])
        # Incrémente l'élément à l'indice i de 1
        bytearray_input[i] += 1

# Exemple utilisateur

# Création d'un bytearray d'exemple avec des valeurs initiales
exemple_bytearray = bytearray([10, 20, 30, 40, 50])

# Affichage du bytearray initial
print("Bytearray initial :", exemple_bytearray)

# Appel de la fonction parcourir_et_incrementer avec le bytearray d'exemple en argument
parcourir_et_incrementer(exemple_bytearray)

# Affichage du bytearray après l'incrémentation
print("Bytearray après l'incrémentation :", exemple_bytearray)
