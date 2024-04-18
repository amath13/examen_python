###################################################################################################
# Écrire un programme python qui affiche une pyramide d'étoiles (*). L'utilisateur doit indiquer  #
# la hauteur de la pyramide, et le programme génère la pyramide correspondante.                   #
# ##################################################################################################

def afficher_pyramide(hauteur):
    """Fonction pour afficher une pyramide d'étoiles.
    Args:
        hauteur (int): La hauteur de la pyramide.
    """
    for i in range(1, hauteur + 1):  # Boucle sur les lignes de la pyramide
        # Affichage des espaces pour centrer la ligne
        print(" " * (hauteur - i), end="")
        # Affichage des étoiles pour former la ligne de la pyramide
        print("*" * (2 * i - 1))

def main():
    # Demande à l'utilisateur de saisir la hauteur de la pyramide
    hauteur = int(input("Entrez la hauteur de la pyramide : "))
    # Appel de la fonction pour afficher la pyramide
    afficher_pyramide(hauteur)

# Appel de la fonction principale
main()