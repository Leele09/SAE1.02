from matplotlib.pyplot import *
from time import *
from copy import copy
from random import randint


def complexite_par_pas(liste_tri,N,pas,Q_echantillon):
    '''
    Fonction qui va renvoyer un dictionnaire renseignant la complexité (temps d'execution en seconde) de chaque tri
    pour chaque cas (pire,moyen et meilleur) en fonction d'une liste de taille variable

    :param liste_tri: liste contenant les fonctions de tri à analyser
    :param N: nombre de valeur max de la liste à trier
    :param pas: taille de la liste variant augmentant de pas à chaque nouvelle génération de liste
    :param Q_echantillon: nombre de répétition de tri dans le cas moyen pour une liste de taille N donné
    :return:
    '''

    # Dico contenant les temps d'execution de chaque tri pour chaque cas:  dico = {"pire_cas:{tri_shaker:[],tri_selec:[] ... } , moyen_cas...}
    dico = {i: {u.__name__: [[],[]] for u in liste_tri} for i in ["pire_cas","moyen_cas","meilleur_cas"]}
    # Dico qui va contenir temporairement la somme des temps d'execution pour chaque tri dans le cas moyen
    dico_moyenne = {i: 0 for i in liste_tri}

    # On remplit cas par cas les valeurs du dictionnaire
    for c, v in dico.items():
        if c == "pire_cas":     # Pire des cas (clé)
            print("Pire cas ...")
            # On crée des tables décroissantes de taille N passée et avec un incrément de pas passé en argument
            for taille in range(0, N+1, pas):
                tab_pire = [i for i in range(taille, -1, -1)]
                # On ajoute à la valeur (v) pour chaque tri un tuple contenant la taille de la liste trié et le temps d'exec du tri
                for tri in liste_tri:
                    c = copy(tab_pire) # Copie de la liste de base au début de chaque tri pour éviter sa modification en fin de tri
                    start = time()
                    tri(c)
                    end = time()
                    v[tri.__name__][0].append(taille)
                    v[tri.__name__][1].append(end-start)
            print("OK")

        elif c == "moyen_cas":      # Moyen cas
            print("Moyen cas ...")
            for taille in range(0, N+ 1, pas):
                # On répète Q fois le tri d'une liste de taille N aléatoire
                for echantillon in range(Q_echantillon):
                    tab_moyen = [randint(0, 20) for k in range(taille + 1)] # Génération de liste aléatoire contenant taille valeur
                    # On implémente dans dico_moyenne la somme des temps d'executions pour chaque tri
                    for tri in liste_tri:
                        c = copy(tab_moyen)
                        start = time()
                        tri(c)
                        end = time()
                        dico_moyenne[tri] += end-start


                # On fait la moyenne des temps d'execution en divisant par Q_echantillon chaque somme de tri
                for c,v1 in dico_moyenne.items():
                    if v1 == 0:
                        v[c.__name__][0].append(taille)
                        v[c.__name__][1].append(0)
                    else:
                        v[c.__name__][0].append(taille)
                        v[c.__name__][1].append(v1/Q_echantillon)
                    dico_moyenne[c] = 0
            print("OK")

        elif c == "meilleur_cas":     # Meilleur cas (meme principe que pour le pire cas mais avec des listes croissantes)
            print("Meilleur cas ...")
            for taille in range(0, N+1, pas):
                tab_meilleur = [i for i in range(taille+1)]
                for tri in liste_tri:
                    start = time()
                    tri(tab_meilleur)
                    end = time()
                    v[tri.__name__][0].append(taille)
                    v[tri.__name__][1].append(end-start)
            print("OK")

    return dico



def dico_to_graphic(dico):
    '''
    Procédure qui transforme un dictionnaire passé en argument sous forme de graphique(courbe)
    '''

    # Création d'un graphique pour chaque cas
    for c , v in dico.items():
        # Pour chaque tri
        for k,j in v.items():
            # On donne les temps d'execution(ordonnée) en fonction des tailes(abscisse)
            plot(j[0],j[1],label = k )

        title(f"Comparaison de tri: {c}")
        xlabel("N")
        ylabel("Temps d'execution")
        legend(loc="upper left")
        show()

    return
