# Écrivez un programme qui compte combien de mots dans une liste sont des palindromes. 
# Un palindrome est un mot qui se lit de la même manière de gauche à droite et de droite à gauche.

def est_palindrome(mot):
    """
    Vérifie si un mot est un palindrome.
    """
    return mot == mot[::-1]

def compter_palindromes(liste_mots):
    """
    Compte le nombre de mots palindromes dans une liste de mots.
    """
    count = 0
    for mot in liste_mots:
        if est_palindrome(mot):
            count += 1
    return count

# Important : 
# ici j'ai crée 2 fonctions
# fct est_palindrome : elle sert à déterminer si un mot est palindrome 
# (un palindrome est un mot qui se lit dans les 2 sens)
# fct compter_plaindromes : intialiser à 0, elle incrémente +1 à chaque fois qu'elle trouve un palindrome dans la liste 

# Liste de mots
liste_mots = ["radar", "bonjour", "kayak", "été", "elle", "reconnaître"]

# Compter le nombre de mots palindromes
nb_palindromes = compter_palindromes(liste_mots)

print("Il y a", nb_palindromes, "palindrome(s) dans la liste.")
