#All rights reserved to Damir & Darien Golami

#Indexing         0      1      2      3     4      5      6     7
chessboard =  [['[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]'],# 0, rank 8
               ['[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]'],# 1, rank 7
               ['[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]'],# 2, rank 6
               ['[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]'],# 3, rank 5
               ['[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]'],# 4, rank 4
               ['[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]'],# 5, rank 3
               ['[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]'],# 6, rank 2
               ['[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]'] # 7, rank 1
               ]# a      b      c      d     e      f      g      h
                
chessboard_original = [['[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]'],
                       ['[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]'],
                       ['[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]'],
                       ['[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]'],
                       ['[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]'],
                       ['[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]'],
                       ['[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]'],
                       ['[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]','[▆▆]','[▁▁]'] 
                       ]
white_pieces = ['[♔]', '[♕]', '[♖]', '[♗]', '[♘]', '[♙]']
black_pieces = ['[♚]', '[♛]', '[♜]', '[♝]', '[♞]', '[♟]']
all_pieces = ['[♔]', '[♕]', '[♖]', '[♗]', '[♘]', '[♙]', '[♚]', '[♛]', '[♜]', '[♝]', '[♞]', '[♟]']
ranks = [8, 7, 6, 5, 4, 3, 2, 1]
files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#Chessboard graphic
for i in range(0,4):
    print(('░░' + '██')*4)
    print(('██' + '░░')*4)
print('\n')

#Function to display the chessboard and algebraic notation
def printBoard():
    for i in range(0, 8):
            print(ranks[i], ' ' + chessboard[i][0] + chessboard[i][1] + chessboard[i][2] + chessboard[i][3] + chessboard[i][4] + chessboard[i][5] + chessboard[i][6] + chessboard[i][7])
    print('    a ', ' b ', ' c ', ' d ', ' e ', ' f ', ' g ' ,' h ')

#Function to put all pawns and pieces in the starting position
def setBoard():
    #Black and White pawns
    for i in range(0, 8):
        chessboard[1][i] = '[♟]'
        chessboard[6][i] = '[♙]'
    
    #Black pieces
    chessboard[0][0] = '[♜]'
    chessboard[0][1] = '[♞]'
    chessboard[0][2] = '[♝]'
    chessboard[0][3] = '[♛]'
    chessboard[0][4] = '[♚]'
    chessboard[0][5] = '[♝]'
    chessboard[0][6] = '[♞]'
    chessboard[0][7] = '[♜]'

    #White pieces
    chessboard[7][0] = '[♖]'
    chessboard[7][1] = '[♘]'
    chessboard[7][2] = '[♗]'
    chessboard[7][3] = '[♕]'
    chessboard[7][4] = '[♔]'
    chessboard[7][5] = '[♗]'
    chessboard[7][6] = '[♘]'
    chessboard[7][7] = '[♖]'
    
#Function to evaluate the position
def evaluate():
    WK = 0
    BK = 0
    WQ = 0
    BQ = 0
    WR = 0
    BR = 0
    WB = 0
    BB = 0
    WN = 0
    BN = 0
    WP = 0
    BP = 0
    
    for i in range(0, 8):
        for j in range(0, 8):
            if chessboard[i][j] == '[♔]':
                WK += 1
            elif chessboard[i][j] == '[♚]':
                BK += 1
            elif chessboard[i][j] == '[♕]':
                WQ += 1
            elif chessboard[i][j] == '[♛]':
                BQ += 1
            elif chessboard[i][j] == '[♖]':
                WR += 1
            elif chessboard[i][j] == '[♜]':
                BR += 1
            elif chessboard[i][j] == '[♗]':
                WB += 1
            elif chessboard[i][j] == '[♝]':
                BB += 1
            elif chessboard[i][j] == '[♘]':
                WN += 1
            elif chessboard[i][j] == '[♞]':
                BN += 1
            elif chessboard[i][j] == '[♙]':
                WP += 1
            elif chessboard[i][j] == '[♟]':
                BP += 1

    material_score = (200 * (WK - BK)) + (9 * (WQ - BQ)) + (5 * (WR - BR)) + (3 * (WB - BB)) + (3 * (WN - BN)) + (1 * (WP - BP))
    
    if material_score >= 0:
        print('Evaluation: +' + str(abs(material_score)), 'for White')
    else:
         print('Evaluation: -' + str(abs(material_score)), 'for Black')
    
#Function to move a piece
def movePiece():
    
    #Function to convert algebraic move notation to indexing syntax
    #a1 -> chessboard[7][0]
    #a2 -> chessboard[6][0]
    #a3 -> chessboard[5][0]
    #e4 -> chessboard[4][4]
    #h6 -> chessboard[2][7]
    #h7 -> chessboard[1][7]
    #h8 -> chessboard[0][7]
    def chessToIndex(move, original):
        file = move[0]
        if file not in files:
            print("That file doesn't exist!")
            movePiece()
            
        rank = move[-1]
        if int(rank) not in ranks:
            print("That rank doesn't exist!")
            movePiece()
            
        vert_index = ranks.index(int(rank))
        horiz_index = files.index(file)
        if original == True:
            return chessboard_original[vert_index][horiz_index], vert_index, horiz_index
        else:
            return chessboard[vert_index][horiz_index], vert_index, horiz_index
        
    #Input current square of piece to be moved, must be [a-h][1-8]
    #Algebraic notation will be converted to 2-dimensional list indexing
    current_square_alg = input('Enter the square of the piece you want to move: ')
    if len(current_square_alg) != 2:
        print('That is not a valid input!')
        printBoard()
        movePiece()
    current_square = chessToIndex(current_square_alg, False)
    print('Selected piece: ', current_square, '\n')
    
    #Input destination square of piece to be moved, must be [a-h][1-8]
    #Algebraic notation will be converted to indexing
    dest_square_alg = input('Enter the square you want to move to: ')
    dest_square = chessToIndex(dest_square_alg, False)
    print('Destination piece: ', dest_square, '\n')
    
    #Nested function to check if moves are legal
    def checkLegality():
        
        legal = False
        
        if current_square[0] in black_pieces:
            legal = True
            
        #If the current square is the same as destination
        if current_square == dest_square:
            legal = False
            print("You can't move to the same square you are currently on.")
            movePiece()

        #If an empty square is selected
        if (current_square[0] not in black_pieces) and (current_square[0] not in white_pieces):
            legal = False
            print("Selected square is empty.")
            movePiece()

        #If the destination square is a friendly piece
        if (dest_square[0] in white_pieces) and (current_square[0] in white_pieces):
            legal = False
            print("You can't capture your own pieces.")
            movePiece()

        #Checking if pieces are blocked
        if current_square[0] != '[♘]':

            #If moving diagonally
            if abs(current_square[1] - dest_square[1]) == abs(current_square[2] - dest_square[2]):

                #If moving northeast
                if (current_square[1] > dest_square[1]) and (current_square[2] < dest_square[2]):
                    for i in range(1, abs(current_square[1] - dest_square[1])):
                        if chessboard[current_square[1] - i][current_square[2] + i] in all_pieces:
                            print('Illegal move!')
                            legal = False
                            printBoard()
                            movePiece()
                            
                        else:
                            legal = True
                    print(current_square[0], 'moved northeast to', dest_square_alg)

                            
                #If moving northwest
                if (current_square[1] > dest_square[1]) and (current_square[2] > dest_square[2]):
                    for i in range(1, abs(current_square[1] - dest_square[1])):
                        if chessboard[current_square[1] - i][current_square[2] - i] in all_pieces:
                            print('Illegal move!')
                            legal = False
                            printBoard()
                            movePiece()
                            
                        else:
                            legal = True
                    print(current_square[0], 'moved northwest to', dest_square_alg)


                #If moving southeast
                if (current_square[1] < dest_square[1]) and (current_square[2] < dest_square[2]):
                    for i in range(1, abs(current_square[1] - dest_square[1])):
                        if chessboard[current_square[1] + i][current_square[2] + i] in all_pieces:
                            print('Illegal move!')
                            legal = False
                            printBoard()
                            movePiece()
                            
                        else:
                            legal = True
                    print(current_square[0], 'moved southeast to', dest_square_alg)


                #If moving southwest
                if (current_square[1] < dest_square[1]) and (current_square[2] > dest_square[2]):
                    for i in range(1, abs(current_square[1] - dest_square[1])):
                        if chessboard[current_square[1] + i][current_square[2] - i] in all_pieces:
                            print('Illegal move!')
                            legal = False
                            printBoard()
                            movePiece()
                            
                        else:
                            legal = True
                    print(current_square[0], 'moved southwest to', dest_square_alg)

                        
            #If moving orthogonally
            elif (current_square[1] == dest_square[1]) or (current_square[2] == dest_square[2]):

                #If moving horizontally left
                if (current_square[1] == dest_square[1]) and (current_square[2] > dest_square[2]):
                    for i in range(1, (abs(current_square[2] - dest_square[2]))):
                        if chessboard[current_square[1]][current_square[2] - i] in all_pieces:
                            print('Illegal move!')
                            legal = False
                            printBoard()
                            movePiece()
                            
                        else:
                            legal = True
                    print(current_square[0], 'moved west to', dest_square_alg)
                    
                #If moving horizontally right
                if (current_square[1] == dest_square[1]) and (current_square[2] < dest_square[2]):
                    for i in range(1, abs(current_square[2] - dest_square[2])):
                        if chessboard[current_square[1]][current_square[2] + i] in all_pieces:
                            print('Illegal move!')
                            legal = False
                            printBoard()
                            movePiece()
                            
                        else:
                            legal = True
                    print(current_square[0], 'moved east to', dest_square_alg)
            
                #If moving vertically up
                #If index 2 is the same for both, and current square index 1 greater than destination
                if (current_square[2] == dest_square[2]) and (current_square[1] > dest_square[1]):
                    for i in range(1, abs(current_square[1] - dest_square[1])):
                        if chessboard[current_square[1] - i][current_square[2]] in all_pieces:
                            print('Illegal move!')
                            legal = False
                            printBoard()
                            movePiece()
                            
                        else:
                            legal = True
                    print(current_square[0], 'moved north to', dest_square_alg)
            

                #If moving vertically down
                if (current_square[2] == dest_square[2]) and (current_square[1] < dest_square[1]):
                    for i in range(1, abs(current_square[1] - dest_square[1])):
                        if chessboard[current_square[1] + i][current_square[2]] in all_pieces:
                            print('Illegal move!')
                            legal = False
                            printBoard()
                            movePiece()
                            
                        else:
                            legal = True
                    print(current_square[0], 'moved south to', dest_square_alg)
            

        #For white pawns
        if current_square[0] == '[♙]':

            #Pawns can move 1 space forward, if not blocked
            if (current_square[1] - dest_square[1] == 1) and (dest_square[0] not in all_pieces) and (current_square[2] == dest_square [2]):
                legal = True

            #Pawns can move 2 spaces forward on their first move, if not blocked
            elif (current_square[1] == 6) and (current_square[1] - dest_square[1] == 2) and (chessboard[(dest_square[1] + 1)][dest_square[2]] not in all_pieces):
                legal = True

            #Pawns capture diagonally forward
            elif (current_square[1] - dest_square[1] == 1) and ((current_square[2] - dest_square[2] == -1) or (current_square[2] - dest_square[2] == 1)) and (dest_square[0] in black_pieces):
                legal = True
                
            #All other pawn moves are illegal
            else:
                legal = False
                print('Illegal pawn move!')
                printBoard()
                movePiece()
                

        #For white bishops
        elif current_square[0] == '[♗]':

            #Bishops move diagonally, if not blocked
            #If absolute value of the difference between the current and destination squares indexes is the same...
            if abs(current_square[1] - dest_square[1]) == abs(current_square[2] - dest_square[2]):
                legal = True

        #For white knights
        elif current_square[0] == '[♘]':

            #Knights move 2 squares horizontally and 1 vertically, or vice versa
            #Knights can jump over other pieces
            if (abs(current_square[1] - dest_square[1]) + abs(current_square[2] - dest_square[2]) == 3) and (current_square[1] != dest_square[1]) and (current_square[2] != dest_square[2]):
                print('Knight jumped to', dest_square_alg)
                legal = True


        #For white rooks
        elif current_square[0] == '[♖]':

            #Rooks move horizontally or vertically, if not blocked
            if (current_square[1] == dest_square[1]) or (current_square[2] == dest_square[2]):
                legal = True
            

        #For white queen       
        elif current_square[0] == '[♕]':

            #Queens move diagonally or orthogonally
            #If moving diagonally
            if abs(current_square[1] - dest_square[1]) == abs(current_square[2] - dest_square[2]):
                legal = True

            #If moving orthogonally
            elif (current_square[1] == dest_square[1]) or (current_square[2] == dest_square[2]):
                legal = True
                

        #For white king
        if current_square[0] == '[♔]':
            
            if (abs(current_square[1] - dest_square[1]) > 1) or (abs(current_square[2] - dest_square[2]) > 1):
                legal = False
                
            else:
                legal = True

        #After all checks if the move being made is not legal
        if legal == False:
            print('Illegal move!')
            printBoard()
            movePiece()

                
    #Function to promote a pawn that reaches the last rank
    def promotePawn():
        promotion = input('What piece would you like to promote to? Input N, Q, R, or B: ')

        #Promote to knight
        if promotion.lower() == 'n':
            chessboard[dest_square[1]][dest_square[2]] = '[♘]'
            chessboard[current_square[1]][current_square[2]] = chessboard_original[current_square[1]][current_square[2]]

        #Promote to queen
        elif promotion.lower() == 'q':
            chessboard[dest_square[1]][dest_square[2]] = '[♕]'
            chessboard[current_square[1]][current_square[2]] = chessboard_original[current_square[1]][current_square[2]]

        #Promote to rook
        elif promotion.lower() == 'r':
            chessboard[dest_square[1]][dest_square[2]] = '[♖]'
            chessboard[current_square[1]][current_square[2]] = chessboard_original[current_square[1]][current_square[2]]

        #Promote to bishop
        elif promotion.lower() == 'b':
            chessboard[dest_square[1]][dest_square[2]] = '[♗]'
            chessboard[current_square[1]][current_square[2]] = chessboard_original[current_square[1]][current_square[2]]

        #Easter egg, trying to promote to a king brings the Armageddon
        elif promotion.lower() == 'k':
            print('LO'*999 + 'L', "It's all over for you now boyo!!!!!!!!!!!!!!!!!!!!!!!")
            chessboard[dest_square[1]][dest_square[2]] = '[♕]'
            chessboard[current_square[1]][current_square[2]] = chessboard_original[current_square[1]][current_square[2]]
            for i in range(0,8):
                chessboard[6][i] = '[♕]'
                chessboard[5][i] = '[♕]'
            
        else:
            print('Please enter a valid promotion symbol.')

    
    #Check if the move being made is legal
    #If legal, make the move. Else, prompt to move again
    checkLegality()

    #For legal moves, change the destination square to the piece on the current square
    chessboard[dest_square[1]][dest_square[2]] = current_square[0]

    #Change the current square to be a proper empty square
    chessboard[current_square[1]][current_square[2]] = chessboard_original[current_square[1]][current_square[2]]

    #If the piece legally moving is a pawn and it makes it to the last rank, promote
    if (dest_square[1] == 0) and (current_square[0] == '[♙]'):
        promotePawn()
        
    printBoard()
    evaluate()
    movePiece()


            

#Initially set the board up, show the board, and prompt to move a piece
setBoard()
printBoard()
movePiece()
