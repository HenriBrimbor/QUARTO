from math import *
from random import *
from copy import copy

def pieces():
    pieces = []
    for size in range(2):
        for form in range(2):
            for color in range(2):
                for hollow in range(2):
                    pieces.append( Piece(size, form, color, hollow) )
    return pieces

def Copie_Plateau(Plateau):
    return [copy(Plateau[0]), copy(Plateau[1]), copy(Plateau[2]), copy(Plateau[3])]

def recherche_gagne(piece, board):
    """
    foncton qui recherche où placer la piece pour gagner en 1 coup
    """
    caracteristics = ['size', 'form', 'color', 'hollow']
    for i in range(4):
        for j in range(4):
            P2 = Copie_Plateau(board)
            if P2[i][j] == 0:
                P2[i][j] = piece
                for car in range(4):
                    S = 0
                    for o in range(4):
                        if P2[o][o] != 0: #évite l'erreur 'int' object is not subscriptable
                            if P2[o][o].__show__()[car]:
                                S += 1
                        if S == 4 or S == 0:
                            return (i,j)
                    S = 0
                    for o in range(4):  #reparcours la matrice en diagonnale
                        if P2[o][3-o]!=0:
                            if P2[k][3-o].__show__()[car]:
                                S += 1
                        if S == 4 or S == 0:
                            return (i,j)
                    S = 0
                    for p in range(4): #reparcours la matrice en ligne
                        if P2[p][j] != 0:
                            if P2[p][j].__show__()[car]:
                                S += 1
                    if S == 4 or S == 0:
                        return (i,j)
                    S = 0
                    for m in range(4):  #reparcours la matrice en colonnes
                        if P2[i][m] != 0:
                            if P2[i][m].__show__()[car]:
                                S += 1
                    if S == 4 or S == 0:
                        return (i,j)
    return False

def recherche_inverse(pieces,plateau):
    """
    fonction qui renvoie toutes les pièces possibles à donner quand la pièce obtenue est déja placée
    donc toutes les pièces qui ne font pas gagner l'adversaire
    """
    P=[]
    for piece in range(len(pieces)):
        if recherche_gagne(pieces[piece],plateau) == False:
            P.append(pieces[piece])
    if len(P) !=0:
        return P
    else:
        return pieces[randint(0,len(pieces)-1)]

def plateau_plein(plateau):
    """
    fonction qui vérifie si le plateau est plein
    """
    for i in range(4):
        for j in range(4):
            if plateau[i][j]==0:
                return False
    return True

def etat_du_jeu(plateau, pièces):
        for k in range(10):
            print(" ")
        for k in range(4):
            print(plateau[k])
        for k in range(len(pièces)):
            print(pièces[k].__showcar__(),k)

def demande_au_joueur( plateau ):
        i = int(input("sur quelle ligne voulez vous placer cette pièce?"))
        j = int(input("sur quelle colonne voulez vous placer cette pièce?"))
        while i>3 or j>3 or plateau[i][j] != 0:
            i = int(input("sur quelle ligne voulez vous placer cette pièce?"))
            j = int(input("sur quelle colonne voulez vous placer cette pièce?"))
        return i, j

def recherche_victoire(plateau):
    """
    fonction qui recherche si l'adversaire a gagné après avoir posé sa pièce
    """
    pièce=[['petit','grand'],['carré','rond'],['noir','blanc'],['creux','pleins']]
    for i in range(4):
        for j in range(4):
            for l in range(4):
                for r in range(2):
                    S = []
                    for o in range(4):              #reparcours la matrice en diagonnale
                        if plateau[o][o] != 0:             #évite l'erreur 'int' object is not subscriptable
                            if plateau[o][o][l] == pièce[l][r] :
                                S.append(1)
                    if S == [1,1,1,1]:
                        return True
                    S = []
                    for k in range(4):              #reparcours la matrice en diagonnale
                        if plateau[k][3-k]!=0:
                            if plateau[k][3-k][l]==pièce[l][r]:
                                S.append(1)
                        if S == [1,1,1,1]:
                            return True
                    S = []
                    for p in range(4):               #reparcours la matrice en ligne
                        if plateau[p][j] != 0:
                            if plateau[p][j][l] == pièce[l][r]:
                                S.append(1)
                        if S == [1,1,1,1]:
                            return True
                    S = []
                    for m in range(4):               #reparcours la matrice en colonnes
                        if plateau[i][m]!=0:
                            if plateau[i][m][l]==pièce[l][r]:
                                S.append(1)
                        if S == [1,1,1,1]:
                            return True
    return False

def nombre_de_places(plateau):
    """
    fonction qui calcule combien il reste de places de libre sur le plateau
    """
    compteur=0
    for i in range(4):
        for j in range(4):
            if plateau[i][j]==0:
                compteur+=1
    return compteur

def recherche_victoire_simple(a, b, Plateau):
    """
    même fonction que recherche victoire mais simplifiée en ne recherchant que la ligne, la colonne et les diagonnales potentielles
    cette fonction simplifiée fera tourner le minmax plus rapidement
    'a' l'indice de ligne
    'b' l'indice de colonne
    """
    pièce=[['petit','grand'],['carré','rond'],['noir','blanc'],['creux','pleins']]
    diag_1 = [(0,0), (1,1), (2,2), (3,3)]
    diag_2 = [(0,3), (1,2), (2,1), (3,0)]
    for caractere in range(4):
        S = 0
        for j in range(4):
            if Plateau[a][j] != 0:
                if Plateau[a][j][caractere] == pièce[caractere][0]:
                    S += 1
                else:
                    S -= 1
            if S == 4 or S == -4:
                return True

    for caractere in range(4):
        S = 0
        for i in range(4):
            if Plateau[i][b] != 0:
                if Plateau[i][b][caractere] == pièce[caractere][0]:
                    S += 1
                else:
                    S -= 1
            if S == 4 or S == -4:
                return True

    if (a, b) in diag_1:
        for caractere in range(4):
            S = 0
            for k in range(4):
                if Plateau[k][k] != 0:
                    if Plateau[k][k][caractere] == pièce[caractere][0]:
                        S += 1
                    else:
                        S -= 1
                if S == 4 or S == -4:
                    return True
    elif (a, b) in diag_2:
        for caractere in range(4):
            S = 0
            for k in range(4):
                if Plateau[k][3-k] != 0:
                    if Plateau[k][3-k][caractere] == pièce[caractere][0]:
                        S += 1
                    else:
                        S -= 1
            if S == 4 or S == -4:
                return True
    return False











