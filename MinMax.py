def MIN_MAX(PLATEAU, PIECES, Piece, MaximisingPlayer, depth):
    for k in range(3):
        print()

    if depth == 0:
        return heuristique()

    if MaximisingPlayer:    #tour de l'IA
        Meilleur_coup = [0,0]
        Valeur_heuristique = -inf
        Meilleure_piece_a_donner = 0
        for i in range(3):
            for j in range(3):
                if PLATEAU[i][j] == 0:
                    copie_tableau = copy(PLATEAU)
                    copie_pieces = copy(PIECES)
                    copie_tableau[i][j] = Piece
                    if recherche_victoire_simple(copie_tableau):
                        return 10, [i,j]
                    else:
                        for piece_adverse in copie_pieces:
                            sous_copie_pieces = copy(copie_pieces)
                            sous_copie_pieces.remove(piece_adverse)
                            Valeur = MIN_MAX(copie_tableau, sous_copie_pieces, piece_adverse, False, depth-1)[0]
                            if Valeur_heuristique < Valeur:
                                Valeur_heuristique = Valeur
                                Meilleur_coup = [i,j]
                                Meilleure_piece_a_donner = piece_adverse
        return Valeur_heuristique, Meilleur_coup, Meilleure_piece_a_donner

    else:                     # tour de l'adversaire simulé en avance
        Meilleur_coup = [0,0]
        Valeur_heuristique = +inf
        Meilleure_piece_a_donner = 0
        for i in range(3):
            for j in range(3):
                if PLATEAU[i][j] == 0:
                    copie_tableau = copy(PLATEAU)
                    copie_pieces = copy(PIECES)
                    copie_tableau[i][j] = Piece
                    if recherche_victoire_simple(copie_tableau):
                        return -1, [i,j]
                    else:
                        for piece_adverse in copie_pieces:
                            sous_copie_pieces = copy(copie_pieces)
                            copie_pieces.remove(piece_adverse)
                            Valeur = MIN_MAX(copie_tableau, sous_copie_pieces, piece_adverse, True, depth-1)[0]
                            if Valeur_heuristique > Valeur:
                                Valeur_heuristique = Valeur
                                Meilleur_coup = [i,j]
                                Meilleure_piece_a_donner = piece_adverse
            return Valeur_heuristique, Meilleur_coup, Meilleure_piece_a_donner



            # un coup amenant à une victoire vaut 1pts, une défaite -1pts
            # égalité = 0




def MIN_MAX_V2(PLATEAU, PIECES, Piece, MaximisingPlayer, depth):
    """
    PLATEAU --> board
    PIECES --> pieces remaining
    Piece --> piece given that has to be placed
    MaximisingPlayer --> True or False depending of who is hypothticaly playing
    depth --> actual depth of the algorithm
    first call = MIN_MAX_V2( real_board, real_remaining_pieces, Piece_given_to_the_IA, True, depth)
    """
    ###########################################
    #i place the piece everywhere on the board, then i give every pieces remaining with this condition to search which one is the best to give, finally i test every case to search where is the best place to put the piece i was given, then i return the heuristic value of the node the best place to put th piece i was given, and the best piece to give
    ###########################################

    if depth == 0:
        return 0    # to make it simple for the moment

    if MaximisingPlayer:    # tour de l'IA
        Meilleur_coup = []          # best place to play for the moment
        Valeur_heuristique = -inf   # initializing the heuristic
        Meilleure_piece_a_donner = ()   # best piece to give
        for i in range(4):              # for all places of the board
            for j in range(4):
                Somme = 0               # initializing the sum_heuristic of the move : 'place the piece at [i,j]'
                heuristique_piece = -inf    # initializing the heuristic of the piece to give according to the actual move [i,j]
                meilleure_piece_ij = ()     # initializing the best piece to give according to the actual move

                if PLATEAU[i][j] == 0:      # only if the place is empty
                    copie_tableau = Copie_Plateau(PLATEAU)      # copy the board in order to not change the previous hypothetical board
                    copie_pieces = copy(PIECES)                 # same with the pieces remaining
                    copie_tableau[i][j] = Piece                 # place the piece given on the new copy of the board

                    if recherche_victoire_simple(i, j, copie_tableau):      # fonction to search if the game is finished
                        return 1, [i,j]               # if so, then return 1 and the place to win
                    else:
                        for piece_adverse in copie_pieces:      # or give every pieces remaining to the opponent and test which one is the best to give
                            sous_copie_pieces = copy(copie_pieces)  # then make a copy of the actual remaining pieces
                            sous_copie_pieces.remove(piece_adverse)     # and remove the piece choosen
                            if depth == 1:           # very precised case because the MinMax return just a int type if depth==1 and a tuple otherwise
                                Valeur = MIN_MAX_V2(copie_tableau, sous_copie_pieces, piece_adverse, False, depth-1)# int type return which is equal to 0 for the moment to simplify
                            else:
                                Valeur = MIN_MAX_V2(copie_tableau, sous_copie_pieces, piece_adverse, False, depth-1)[0]# int corresponding to the sum at the node
                            Somme += Valeur         # add the value of the under node to the sum of the actual move
                            if heuristique_piece < Valeur:       # test if the value is the best within every other that are linked to other pieces given
                                meilleure_piece_ij = piece_adverse     # if the value founded is better than the previous, stock the piece given
                                heuristique_piece = Valeur             # and its value to test it with others
                    if Valeur_heuristique < Somme:                     # test the value of the node of the move with others
                        Valeur_heuristique = Somme                     # if the move is better then stock
                        Meilleur_coup = [i,j]                          # the place [i,j]
                        Meilleure_piece_a_donner = meilleure_piece_ij    # and the piece to give

        return Valeur_heuristique, Meilleur_coup, Meilleure_piece_a_donner

    else:                     # tour de l'adversaire simulé en avance
        Meilleur_coup = []
        Valeur_heuristique = +inf
        Meilleure_piece_a_donner = ()
        for i in range(4):
            for j in range(4):
                Somme = 0
                heuristique_piece = +inf
                meilleure_piece_ij = ()
                if PLATEAU[i][j] == 0:
                    copie_tableau = Copie_Plateau(PLATEAU)
                    copie_pieces = copy(PIECES)
                    copie_tableau[i][j] = Piece
                    if recherche_victoire_simple(i, j, copie_tableau):
                        return -1, [i,j]
                    else:
                        for piece_adverse in copie_pieces:
                            sous_copie_pieces = copy(copie_pieces)
                            sous_copie_pieces.remove(piece_adverse)
                            if depth == 1:
                                Valeur = MIN_MAX_V2(copie_tableau, sous_copie_pieces, piece_adverse, True, depth-1)
                            else:
                                Valeur = MIN_MAX_V2(copie_tableau, sous_copie_pieces, piece_adverse, True, depth-1)[0]
                            Somme += Valeur
                            if heuristique_piece > Valeur:
                                meilleure_piece_ij = piece_adverse
                                heuristique_piece = Valeur
                    if Valeur_heuristique > Somme:
                        Valeur_heuristique = Somme
                        Meilleur_coup = [i,j]
                        Meilleure_piece_a_donner = piece_adverse
        return Valeur_heuristique, Meilleur_coup, Meilleure_piece_a_donner


