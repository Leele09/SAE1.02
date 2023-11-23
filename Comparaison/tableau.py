import pandas as pd
from copy import copy
from time import *
from random import randint
from tabulate import tabulate

def complexite_par_puissance10(liste_tri,N_puissance_de_10,Q_echantillon):
    '''
    Fonction qui va renvoyer 3 dictionnaires pour chaque cas renseignant la complexité (temps d'execution en seconde) de chaque tri
    en fonction d'une liste de taille variable par puissance de 10


    :param liste_tri: liste des tries qu'on analyse
    :param N_puissance_de_10: puissance représentant la taille maximale de la liste
    :param Q_echantillon: nombre de répétition de tri dans le cas moyen pour une liste de taille N donné
    :return:
    '''

    # Création de la première clé du dico ayant pour valeur la liste des tries selectionnées en fonction du cas
    dico_pire = {"Pire cas":[i.__name__ for i in liste_tri]}
    dico_moyen = {"Moyen cas": [i.__name__ for i in liste_tri]}
    dico_meilleur = {"Meilleur cas": [i.__name__ for i in liste_tri]}

    # Génération des autres clées correspondant aux tailles des listes par puissance de 10
    for i in range(N_puissance_de_10+1):
        dico_pire[10**i] = []
        dico_moyen[10**i] = []
        dico_meilleur[10**i] = []

    # On stocke les dictionnaires dans une liste
    dico_cas = [dico_pire , dico_moyen , dico_meilleur]

    # On remplit les valeurs manquantes pour chaque dictionnaire
    for cas in dico_cas:

        if cas == dico_pire: # Pire cas (dico_pire)
            print("Pire cas ...")
            # Création des tables décroissantes de taille variable par puissance de 10
            for taille in range(0, N_puissance_de_10+1):
                tab_pire = [i for i in range(10**taille, 0, -1)]
                # Calcul du temps d'execution pour chaque trie rajouté à la clé correspondante
                for tri in liste_tri:
                    c = copy(tab_pire) # Copie temporaire de la liste
                    start = time()
                    tri(c)
                    end = time()
                    dico_pire[10**taille].append(end - start)

            print("OK")
        elif cas == dico_moyen: # Moyen cas
            print("Moyen cas ...")
            dico_moyenne = {i: 0 for i in liste_tri}
            for taille in range(N_puissance_de_10 + 1):
                #  On répète Q fois le tri d'une liste de taille N aléatoire
                for echantillon in range(Q_echantillon):
                    tab_moyen = [randint(0, 20) for i in range(10 ** taille)]
                    # On implémente dans dico_moyenne la somme des temps d'executions pour chaque tri
                    for tri in liste_tri:
                        c = copy(tab_moyen) # Copie temporaire
                        start = time()
                        tri(c)
                        end = time()
                        dico_moyenne[tri] += end - start

                # On fait la moyenne des temps d'execution en divisant par Q_echantillon chaque valeur
                for c, v in dico_moyenne.items():
                    if v == 0:
                        dico_moyen[10**taille].append(0)
                    else:
                        dico_moyen[10**taille].append(v / Q_echantillon)
                    dico_moyenne[c] = 0
            print("OK")

        elif cas == dico_meilleur:  # Meilleur cas (meme principe que pour le pire cas)
            print("Meilleur cas ...")
            for taille in range(N_puissance_de_10 + 1):
                tab_meilleur = [i for i in range(0, 10 ** taille)]
                for tri in liste_tri:
                    start = time()
                    tri(tab_meilleur)
                    end = time()
                    dico_meilleur[10**taille].append(end - start)
            print("OK")
    return dico_pire ,dico_moyen,dico_meilleur


def dico_to_dataframe(dico):
    '''
    Procédure qui affiche les dico sous forme de tableau
    '''

    # On transforme pour dictionnaire les clées et valeur en dataframe
    for cas in dico:
        print(tabulate(pd.DataFrame(cas),headers = 'keys', tablefmt='psql'))
    return
