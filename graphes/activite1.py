# Écrivez un programme pour représenter un graphe en utilisant un dictionnaire en Python.

# Définition du graphe sous forme de dictionnaire
graphe = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}

# Affichage du graphe
print("Représentation du graphe :")
for sommet, voisins in graphe.items():
    print(sommet, "->", voisins)

