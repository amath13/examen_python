# Étant donné un dictionnaire contenant le nom des étudiants et leurs notes moyennes, 
# écrivez un programme qui génère un nouveau dictionnaire 
# avec les noms des étudiants qui ont une note moyenne supérieure ou égale à 15.

def eleves_sup_ou_egal_15(notes):
    """
    Retourne un nouveau dictionnaire contenant les élèves ayant une note moyenne supérieure ou égale à 15.
    """
    eleves_sup_15 = {}
    for eleve, note in notes.items():
        if note >= 15:
            eleves_sup_15[eleve] = note
    return eleves_sup_15

# Important :  
# la méthode .items() est utilisée sur un dictionnaire pour obtenir une vue d'ensemble 
# des paires clé-valeur contenues dans ce dictionnaire.

# Dictionnaire des étudiants et de leurs notes moyennes
notes_etudiants = {
    "Amadou": 17,
    "Ismail": 12,
    "Amath": 15,
    "KewKew": 19,
    "Ibrahima": 14,
    "Abu": 18
}

# Générer un nouveau dictionnaire avec les étudiants ayant une note moyenne supérieure ou égale à 15
eleves_sup_15 = eleves_sup_ou_egal_15(notes_etudiants)

# Afficher le nouveau dictionnaire
print("Élèves avec une note moyenne supérieure ou égale à 15 :")
for eleve, note in eleves_sup_15.items():
    print(eleve, ":", note)

