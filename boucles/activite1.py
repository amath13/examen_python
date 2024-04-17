# Écrire un programme qui choisit un nombre aléatoire entre 1 et 100 et demande à l'utilisateur de le deviner. 
# L'utilisateur a droit à un nombre limité de tentatives. Après chaque tentative, 
# le programme indique si le nombre mystère est plus grand ou plus petit que la saisie de l'utilisateur.

import random

# Générer un nombre aléatoire entre 1 et 100
nombre_mystere = random.randint(1, 100)

# Nombre maximum de tentatives
max_tentatives = 5

# Boucle pour les tentatives
for tentative in range(max_tentatives):
    # Demander à l'utilisateur de deviner le nombre
    guess_str = int(input("Devinez le nombre (entre 1 et 100) : "))


    # Vérifier si la saisie est un nombre valide entre 1 et 100
    if int(guess_str) < 1 or int(guess_str) > 100:
        print("Veuillez saisir un nombre valide entre 1 et 100.")
    
    devine = int(guess_str)

    # Vérifier si la devinette est correcte
    if devine == nombre_mystere:
        print("Félicitations ! Vous avez deviné le nombre mystère.")
    elif devine < nombre_mystere:
        print("Le nombre mystère est plus grand.")
    else:
        print("Le nombre mystère est plus petit.")

# Si l'utilisateur n'a pas deviné le nombre après le nombre maximal de tentatives
if devine != nombre_mystere:
    print("Dommage ! Le nombre mystère était :", nombre_mystere)
