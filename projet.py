# Fichier main SAE1.02


# Importation des modules
from Tri.tri import *
from Comparaison.tableau import *
from Comparaison.graphique import *


if __name__ == '__main__':
    # Liste des tries à analyser
    lst_tri1 = [tri_rapide,tri_shaker ,tri_selection ,tri_fusion ]
    lst_tri2 = [tri_gnome, tri_shaker, tri_bulle, tri_insertion , tri_rapide,tri_fusion,tri_selection ]

    # Affichage de la complexité des tries sous forme de tableau (Dataframe)
    print("Data Frame:")
    dico1= complexite_par_puissance10(lst_tri1,4,5)
    dico_to_dataframe(dico1)

    # Affichage de la complexité des tries sous forme de graphique
    print("Graphique:")
    dico2 = complexite_par_pas(lst_tri2, 3000, 300, 4)
    dico_to_graphic(dico2)
