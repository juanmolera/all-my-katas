import numpy as np

def is_solved(board):

    count = 0
    aux = 0

    for row in board:

        last = row[0]

        for element in row:

            # break si no soluciona por esa row y pasa a la siguiente
            if element != last:

                break

            # coincidentes por row
            else:

                count += 1

        # win si 3 en row
        if count == 3:

            if row[-1] == 1:

                return 1 # X

            elif row[-1] == 2:

                return 2 # O
            
            else:
                
                pass


        # limpia cuenta por row
        count = 0

    # la traspongo y le corro el mismo alg anterior

    traspuesta = np.array(board).T.tolist()

    for row in traspuesta:

        last = row[0]

        for element in row:

            # killea si soluciona por row
            if element != last:

                break

            # coincidentes por col
            else:

                count += 1

        # win si 3 en col
        if count == 3:

            if row[-1] == 1:

                return 1 # X

            elif row[-1] == 2:

                return 2 # O
            
            else:
                
                pass

        # limpia cuenta por row
        count = 0

    # diagonales

    if board[1][1] == board[0][0] and board[1][1] == board[2][2] or board[1][1] == board[0][2] and board[1][1] == board[2][0]:

        if board[1][1] == 1:

            return 1 # X

        elif board[1][1] != 0:

            return 2 # O
        
        else:
            
            pass
            

    for row in board:

        for element in row:

            if not element:

                return -1 # not finished

    return 0 # draw