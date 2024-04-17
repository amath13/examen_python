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

# Liste de mots
liste_mots = ["radar", "bonjour", "kayak", "été", "elle", "reconnaître"]

# Compter le nombre de mots palindromes
nb_palindromes = compter_palindromes(liste_mots)

print("Il y a", nb_palindromes, "palindrome(s) dans la liste.")
