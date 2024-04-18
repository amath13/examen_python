# Vous disposez de la chaîne de caractères suivante : 
# "Python est un langage de programmation puissant et facile à apprendre."
# Extraction simple : Extraire le mot "Python" de la chaîne.

# Chaîne de caractères donnée
chaine = "Python est un langage de programmation puissant et facile à apprendre."

# Extraction du mot "Python"
mot_python = chaine.split()[0]

print('Affiche le mot python de la chaine : ' + mot_python)

# Extraction par indices négatifs : Extraire le mot "apprendre" en utilisant des indices négatifs.
# Extraction du mot "apprendre" avec des indices négatifs
mots = chaine.split()  # Divise la chaîne en mots
mot_apprendre = mots[-1]  # Utilise l'indice -1 pour extraire l'avant-dernier mot
mot_apprendre_sans_point = mot_apprendre.rstrip('.') #extraire le mot apprendre sans le point

print('Affiche le mot apprendre de la chaine : ' + mot_apprendre_sans_point)

# Slicing : Extraire la phrase "langage de programmation" en utilisant le slicing.
# Extraction de la phrase "langage de programmation" avec le slicing
extraire_phrase = chaine[14:39]

print('Affiche langage de programmation de la chaine : ' + extraire_phrase)

# Challenge : Inversez la chaîne de caractères entière.
inverse_chaine = chaine[::-1]

# Important :
# [::-1] = cette expression utilise le slicing pour inverser le mot 
# Le premier : indique le début du slicing.
# Le deuxième : indique la fin du slicing.
# Le 1 indique le pas, c'est-à-dire le nombre d'éléments à sauter entre chaque élément sélectionné. 
# Un pas de -1 signifie que nous parcourons la séquence de droite à gauche, ce qui inverse l'ordre.

print('Inverse la chaine : ' + inverse_chaine)
