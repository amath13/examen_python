######################################################################################################################
# Écrivez un programme Python qui prend enparamètre une liste de tuples et affiche le tuple avec le plus d'éléments. #
######################################################################################################################

def tuple_avec_plus_elements(liste_tuples):
    """ Args:
        liste_tuples (list): Une liste de tuples.

    Returns:
        tuple: Le tuple avec le plus d'éléments.
    """
    # Utilise la fonction max() avec la clé len pour trouver le tuple avec le plus d'éléments
    max_tuple = max(liste_tuples, key=len)
    return max_tuple

def main():
    # Liste de tuples à titre d'exemple
    liste_tuples = [(1, 2), (4, 5, 6), (7, 8, 9, 10), (11,)]
    # Appel de la fonction pour trouver le tuple avec le plus d'éléments
    max_tuple = tuple_avec_plus_elements(liste_tuples)
    # Affichage du résultat
    print("Le tuple avec le plus d'éléments est :", max_tuple)

# Appel de la fonction principale
main()

