def QUARTO():
    class Jeu:
        PLATEAU = [[0,0,0,0] for k in range(4)]
        Pièces = pieces()
        RESULTAT = False
        Premier_coup = True
        compteur = 0
    while not(Jeu.RESULTAT) and not( nombre_de_places(Jeu.PLATEAU) == 0):                           #tant que personne n'a gagné
        Jeu.RESULTAT = True
        etat_du_jeu(Jeu.PLATEAU, Jeu.Pièces)
        n = int( input( "quelle est la place de la pièce que vous voulez donner? ") )
        while n > len(Jeu.Pièces) or n < 0 :
            n = int( input( "quelle est la place de la pièce que vous voulez jouer? ") )
        IA = recherche_gagne(Jeu.Pièces[n], Jeu.PLATEAU)                   #recherche où placer la pèce pour gagner le jeu
        if IA != False:
            Jeu.PLATEAU[IA[0]][IA[1]] = Jeu.Pièces[n]
            for k in range(4):
                print(Jeu.PLATEAU[k])
            return ("l'IA place la pièce", Jeu.Pièces[n], "à la place", IA, "QUARTO!!")

        pièce_jouée = Jeu.Pièces[n]
        Jeu.Pièces.pop(n)
        Jeu.compteur +=1
        print('TOUR', Jeu.compteur)
        if Jeu.Premier_coup:                                         #cas pour le premiers coup
            i, j = randint(0, 3),randint(0, 3)
            Jeu.PLATEAU[i][j] = pièce_jouée
            print( "l'ordinateur place sa pièce à la place",[i, j] )
            pièce_à_donner = Jeu.Pièces[ randint(0, len(Jeu.Pièces)-1) ]
            print("l'ordinateur vous donne la pièce", pièce_à_donner)
            i, j = demande_au_joueur( Jeu.PLATEAU )
            Jeu.PLATEAU[i][j] = pièce_à_donner
            Jeu.Pièces.remove( pièce_à_donner )
            Jeu.RESULTAT = False
            if Jeu.compteur == 2:
                Jeu.Premier_coup = False

        else:
            table = copy(Jeu.PLATEAU)
            pieces_copies = copy(Jeu.Pièces)
            Calcul = MIN_MAX_V2(table, pieces_copies, pièce_jouée, True, 2) #Somme,Valeur_heuristique,Meilleur_coup,Meilleure_piece_a_donner
            print(Calcul)
            place = Calcul[1]
            pièce_à_donner = Calcul[2]
            print( "l'ordinateur place la pièce", pièce_jouée, "à la place", place)
            a, b = place[0], place[1]
            Jeu.PLATEAU[a][b] = pièce_jouée                                 #place la pièce
            etat_du_jeu(Jeu.PLATEAU, Jeu.Pièces)
            print("l'ordinateur vous donne la pièce", pièce_à_donner)
            i, j = demande_au_joueur(Jeu.PLATEAU)
            Jeu.PLATEAU[i][j] = pièce_à_donner
            Jeu.Pièces.remove( pièce_à_donner )
            Jeu.RESULTAT = recherche_victoire_simple(i, j, Jeu.PLATEAU)                              #renvoie False si le joueur n'a pas gagné et réitère la boucle, True sinon ferme la boucle while
    print(Jeu.RESULTAT, nombre_de_places(Jeu.PLATEAU) == 0 )
    return ("BRAVO VOUS AVEZ GAGNE!!")                                              #sort de la boucle while uniquement si le joueur gagne