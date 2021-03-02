class Piece():
    def __init__(self, size, form, color, hollow):
        self.size = size
        self.form = form
        self.color = color
        self.hollow = hollow
        return None
    def __show__(self):
        return self.size, self.form, self.color, self.hollow
    def __showcar__(self):
# size: 1 is high,      0 is small
# form: 1 is circle     0 is square
# color: 1 is white     0 is black
# hollow: 1 is hollowed 0 is full
        dic = [ {'1':'high', '0':'small'}, {'1':'circle', '0':'square'}, {'1':'white', '0':'black'}, {'1':'hollowed', '0':'full'} ]
        caracteristics = []
        car = self.__show__()
        for index in range(4):
            if car[index]:
                caracteristics.append( dic[index]['1'])
            else:
                caracteristics.append( dic[index]['0'])
        return caracteristics

def QUARTO():
    # initializing all parameters
    board = [[0,0,0,0] for k in range(4)]
    pieces_set = pieces()
    condition = False
    first_places = True
    compteur = 0

    #tant que personne n'a gagné
    while not condition and not( nombre_de_places(board) == 0):
        condition = True
        etat_du_jeu(board, pieces_set)

        n = int( input( "quelle est la place de la pièce que vous voulez donner? ") )
        while n > len(pieces_set) or n < 0 :
            n = int( input( "quelle est la place de la pièce que vous voulez jouer? ") )

        # search if there is a direct move to win, place (i,j) if so
        IA = recherche_gagne(pieces_set[n], board)
        if IA != False:
            board[IA[0]][IA[1]] = pieces_set[n]
            for k in range(4):
                print(board[k])
            return ("l'IA place la pièce", pieces_set[n], "à la place", IA, "QUARTO!!")

        piece_to_play = pieces_set[n]
        pieces_set.pop(n)
        compteur +=1

        print('TOUR', compteur)
        #first 2 moves are selected randomly
        if first_places:
            i, j = randint(0, 3),randint(0, 3)
            while board[i][j] != 0:
                i, j = randint(0, 3),randint(0, 3)

            board[i][j] = piece_to_play
            print( "l'ordinateur place sa pièce à la place",[i, j] )

            piece_to_give = pieces_set[ randint(0, len(pieces_set)-1) ]
            print("l'ordinateur vous donne la pièce", piece_to_give)

            i, j = demande_au_joueur( board )
            board[i][j] = piece_to_give
            pieces_set.remove( piece_to_give )

            if compteur == 2:
                first_places = False

        else:
            table = copy(board)
            pieces_set_copies = copy(pieces_set)
            calcul = MIN_MAX_V2(table, pieces_set_copies, piece_to_play, True, 2) #Somme,Valeur_heuristique,Meilleur_coup,Meilleure_piece_a_donner
            print(calcul)
            place = calcul[1]
            piece_to_give = calcul[2]
            print( "l'ordinateur place la pièce", piece_to_play, "à la place", place)
            a, b = place[0], place[1]
            board[a][b] = piece_to_play                                 #place la pièce
            etat_du_jeu(board, pieces_set)
            print("l'ordinateur vous donne la pièce", piece_to_give)
            i, j = demande_au_joueur(board)
            board[i][j] = piece_to_give
            pieces_set.remove( piece_to_give )
            condition = recherche_victoire_simple(i, j, board)                              #renvoie False si le joueur n'a pas gagné et réitère la boucle, True sinon ferme la boucle while
    print(condition, nombre_de_places(board) == 0 )
    return ("BRAVO VOUS AVEZ GAGNE!!")                                              #sort de la boucle while uniquement si le joueur gagne