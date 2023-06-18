# 0 draw
# 1 X
# 2 O
# -1 not finished, empty spots

import numpy as np

'''
board = [[0, 0, 1],
        [0, 1, 2],
        [2, 1, 0]]
'''

board = [[2, 1, 1],
        [2, 1, 1],
        [1, 1, 2]]

count = 0
aux = 0

# -1

for row in board:

    last = row[0]

    for element in row:

        # killea si 0
        if not element:

            print('board con 0')
            #return '-1'
            break
        
        # killea si soluciona por row
        if element != last:

            break
        
        # coincidentes por row
        else:

            count += 1

    # win si 3 en row
    if count == 3:

        print('gana por row')
        #return '1'
        #return '2'
        break
    
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
        
        # coincidentes por row
        else:

            count += 1

    # win si 3 en row
    if count == 3:

        print('gana por col')
        #return '1'
        #return '2'
        break
    
    # limpia cuenta por row
    count = 0

# diagonales

if board[1][1] == board[0][0] and board[1][1] == board[2][2] or board[1][1] == board[0][2] and board[1][1] == board[2][0]:

    print('gana por diagonal')