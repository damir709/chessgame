#All rights reserved to Damir Golami
#This is the Python 3 source code for a hobby project of mine where you play a game of chess against a CPU player.
#Newer version is underway with object-oriented programming.


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
print('Chess by Damir Golami!', '\n')

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

#Function to check if a CPU's move is legal                    
def checkCpuLegality(cpu_current_square, cpu_dest_square):
    #For black pieces        
    legal = False

     #For black pawns
    if cpu_current_square[0] == '[♟]':

        #Pawns can move 1 space forward, if not blocked
        if (cpu_current_square[1] - cpu_dest_square[1] == -1) and (cpu_dest_square[0] not in all_pieces) and (cpu_current_square[2] == cpu_dest_square[2]):
            legal = True

        #Pawns can move 2 spaces forward on their first move, if not blocked
        elif (cpu_current_square[1] == 1) and (cpu_current_square[1] - cpu_dest_square[1] == -2) and (chessboard[(cpu_current_square[1] + 1)][cpu_dest_square[2]] not in all_pieces) and (chessboard[(cpu_current_square[1] + 2)][cpu_dest_square[2]] not in all_pieces) and (cpu_current_square[2] == cpu_dest_square[2]):
            legal = True

        #Pawns capture diagonally forward
        elif (cpu_current_square[1] - cpu_dest_square[1] == -1) and ((cpu_current_square[2] - cpu_dest_square[2] == -1) or (cpu_current_square[2] - cpu_dest_square[2] == 1)) and cpu_dest_square[0] in white_pieces:
            legal = True
            
        #All other pawn moves are illegal
        else:
            legal = False
            

    #For black bishops
    elif cpu_current_square[0] == '[♝]':

        #Bishops move diagonally, if not blocked
        #If moving diagonally
        if abs(cpu_current_square[1] - cpu_dest_square[1]) == abs(cpu_current_square[2] - cpu_dest_square[2]):

            #If moving northeast
            if (cpu_current_square[1] - cpu_dest_square[1] == 1) and (cpu_current_square[2] - cpu_dest_square[2] == -1):
                legal = True
                
            if (cpu_current_square[1] > cpu_dest_square[1]) and (cpu_current_square[2] < cpu_dest_square[2]):
                for i in range(1, abs(cpu_current_square[1] - cpu_dest_square[1])):
                    if chessboard[cpu_current_square[1] - i][cpu_current_square[2] + i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True

                        
            #If moving northwest
            if (cpu_current_square[1] - cpu_dest_square[1] == 1) and (cpu_current_square[2] - cpu_dest_square[2] == 1):
                legal = True
                
            if (cpu_current_square[1] > cpu_dest_square[1]) and (cpu_current_square[2] > cpu_dest_square[2]):
                for i in range(1, abs(cpu_current_square[1] - cpu_dest_square[1])):
                    if chessboard[cpu_current_square[1] - i][cpu_current_square[2] - i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True

                    
            #If moving southeast
            if (cpu_current_square[1] - cpu_dest_square[1] == -1) and (cpu_current_square[2] - cpu_dest_square[2] == -1):
                legal = True
                
            if (cpu_current_square[1] < cpu_dest_square[1]) and (cpu_current_square[2] < cpu_dest_square[2]):
                for i in range(1, abs(cpu_current_square[1] - cpu_dest_square[1])):
                    if chessboard[cpu_current_square[1] + i][cpu_current_square[2] + i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True


            #If moving southwest
            if (cpu_current_square[1] - cpu_dest_square[1] == -1) and (cpu_current_square[2] - cpu_dest_square[2] == 1):
                legal = True
                
            if (cpu_current_square[1] < cpu_dest_square[1]) and (cpu_current_square[2] > cpu_dest_square[2]):
                for i in range(1, abs(cpu_current_square[1] - cpu_dest_square[1])):
                    if chessboard[cpu_current_square[1] + i][cpu_current_square[2] - i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True


    #For black knights
    elif cpu_current_square[0] == '[♞]':

        #Knights move 2 squares horizontally and 1 vertically, or vice versa
        #Knights can jump over other pieces
        if (abs(cpu_current_square[1] - cpu_dest_square[1]) + abs(cpu_current_square[2] - cpu_dest_square[2]) == 3) and (cpu_current_square[1] != cpu_dest_square[1]) and (cpu_current_square[2] != cpu_dest_square[2]):
            legal = True


    #For black rooks
    elif cpu_current_square[0] == '[♜]':

        #Rooks move orthogonally, if not blocked
        if (cpu_current_square[1] == cpu_dest_square[1]) or (cpu_current_square[2] == cpu_dest_square[2]):
          
            #If moving horizontally left
            if (cpu_current_square[1] == cpu_dest_square[1]) and (cpu_current_square[1] - cpu_dest_square[1] == 1):
                legal = True
                
            if (cpu_current_square[1] == cpu_dest_square[1]) and (cpu_current_square[2] > cpu_dest_square[2]):
                for i in range(1, (abs(cpu_current_square[2] - cpu_dest_square[2]))):
                    if chessboard[cpu_current_square[1]][cpu_current_square[2] - i] in all_pieces:
                        legal = False
                        break
                        
                    else:
                        legal = True
                
            #If moving horizontally right
            if (cpu_current_square[1] == cpu_dest_square[1]) and (cpu_current_square[1] - cpu_dest_square[1] == -1):
                legal = True
                
            if (cpu_current_square[1] == cpu_dest_square[1]) and (cpu_current_square[2] < cpu_dest_square[2]):
                for i in range(1, abs(cpu_current_square[2] - cpu_dest_square[2])):
                    if chessboard[cpu_current_square[1]][cpu_current_square[2] + i] in all_pieces:
                        legal = False
                        break
                        
                    else:
                        legal = True
        
            #If moving vertically up
            if (cpu_current_square[2] == cpu_dest_square[2]) and (cpu_current_square[1] - cpu_dest_square[1] == 1):
                legal = True
            
            if (cpu_current_square[2] == cpu_dest_square[2]) and (cpu_current_square[1] > cpu_dest_square[1]):
                for i in range(1, abs(cpu_current_square[1] - cpu_dest_square[1])):
                    if chessboard[cpu_current_square[1] - i][cpu_current_square[2]] in all_pieces:
                        legal = False
                        break
                        
                    else:
                        legal = True

            #If moving vertically down
            if (cpu_current_square[2] == cpu_dest_square[2]) and (cpu_current_square[1] - cpu_dest_square[1] == -1):
                legal = True
                
            if (cpu_current_square[2] == cpu_dest_square[2]) and (cpu_current_square[1] < cpu_dest_square[1]):
                for i in range(1, abs(cpu_current_square[1] - cpu_dest_square[1])):
                    if chessboard[cpu_current_square[1] + i][cpu_current_square[2]] in all_pieces:
                        legal = False
                        break
                       
                    else:
                        legal = True
    
    
    #For black queen       
    elif cpu_current_square[0] == '[♛]':

        #Queens move diagonally or orthogonally
        #If moving diagonally
        if abs(cpu_current_square[1] - cpu_dest_square[1]) == abs(cpu_current_square[2] - cpu_dest_square[2]):

            #If moving northeast
            if (cpu_current_square[1] - cpu_dest_square[1] == 1) and (cpu_current_square[2] - cpu_dest_square[2] == -1):
                legal = True
                
            if (cpu_current_square[1] > cpu_dest_square[1]) and (cpu_current_square[2] < cpu_dest_square[2]):
                for i in range(1, abs(cpu_current_square[1] - cpu_dest_square[1])):
                    if chessboard[cpu_current_square[1] - i][cpu_current_square[2] + i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True

                        
            #If moving northwest
            if (cpu_current_square[1] - cpu_dest_square[1] == 1) and (cpu_current_square[2] - cpu_dest_square[2] == 1):
                legal = True
                
            if (cpu_current_square[1] > cpu_dest_square[1]) and (cpu_current_square[2] > cpu_dest_square[2]):
                for i in range(1, abs(cpu_current_square[1] - cpu_dest_square[1])):
                    if chessboard[cpu_current_square[1] - i][cpu_current_square[2] - i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True

                    
            #If moving southeast
            if (cpu_current_square[1] - cpu_dest_square[1] == -1) and (cpu_current_square[2] - cpu_dest_square[2] == -1):
                legal = True
                
            if (cpu_current_square[1] < cpu_dest_square[1]) and (cpu_current_square[2] < cpu_dest_square[2]):
                for i in range(1, abs(cpu_current_square[1] - cpu_dest_square[1])):
                    if chessboard[cpu_current_square[1] + i][cpu_current_square[2] + i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True


            #If moving southwest
            if (cpu_current_square[1] - cpu_dest_square[1] == -1) and (cpu_current_square[2] - cpu_dest_square[2] == 1):
                legal = True
                
            if (cpu_current_square[1] < cpu_dest_square[1]) and (cpu_current_square[2] > cpu_dest_square[2]):
                for i in range(1, abs(cpu_current_square[1] - cpu_dest_square[1])):
                    if chessboard[cpu_current_square[1] + i][cpu_current_square[2] - i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True

        #If moving orthogonally
        elif (cpu_current_square[1] == cpu_dest_square[1]) or (cpu_current_square[2] == cpu_dest_square[2]):
          
            #If moving horizontally left
            if (cpu_current_square[1] == cpu_dest_square[1]) and (cpu_current_square[1] - cpu_dest_square[1] == 1):
                legal = True
                
            if (cpu_current_square[1] == cpu_dest_square[1]) and (cpu_current_square[2] > cpu_dest_square[2]):
                for i in range(1, (abs(cpu_current_square[2] - cpu_dest_square[2]))):
                    if chessboard[cpu_current_square[1]][cpu_current_square[2] - i] in all_pieces:
                        legal = False
                        break
                        
                    else:
                        legal = True
                
            #If moving horizontally right
            if (cpu_current_square[1] == cpu_dest_square[1]) and (cpu_current_square[1] - cpu_dest_square[1] == -1):
                legal = True
                
            if (cpu_current_square[1] == cpu_dest_square[1]) and (cpu_current_square[2] < cpu_dest_square[2]):
                for i in range(1, abs(cpu_current_square[2] - cpu_dest_square[2])):
                    if chessboard[cpu_current_square[1]][cpu_current_square[2] + i] in all_pieces:
                        legal = False
                        break
                        
                    else:
                        legal = True
        
            #If moving vertically up
            if (cpu_current_square[2] == cpu_dest_square[2]) and (cpu_current_square[1] - cpu_dest_square[1] == 1):
                legal = True
            
            if (cpu_current_square[2] == cpu_dest_square[2]) and (cpu_current_square[1] > cpu_dest_square[1]):
                for i in range(1, abs(cpu_current_square[1] - cpu_dest_square[1])):
                    if chessboard[cpu_current_square[1] - i][cpu_current_square[2]] in all_pieces:
                        legal = False
                        break
                        
                    else:
                        legal = True

            #If moving vertically down
            if (cpu_current_square[2] == cpu_dest_square[2]) and (cpu_current_square[1] - cpu_dest_square[1] == -1):
                legal = True
                
            if (cpu_current_square[2] == cpu_dest_square[2]) and (cpu_current_square[1] < cpu_dest_square[1]):
                for i in range(1, abs(cpu_current_square[1] - cpu_dest_square[1])):
                    if chessboard[cpu_current_square[1] + i][cpu_current_square[2]] in all_pieces:
                        legal = False
                        break
                       
                    else:
                        legal = True
            

    #For black king
    elif cpu_current_square[0] == '[♚]':
        
        #If the king tries to move more than 2 squares in any direction
        if (abs(cpu_current_square[1] - cpu_dest_square[1]) > 1) or (abs(cpu_current_square[2] - cpu_dest_square[2]) > 1):
            legal = False
            
        else:
            legal = True

    
    #If the current square is the same as destination
    if cpu_current_square == cpu_dest_square:
            legal = False

    #If the destination square is a friendly piece
    if (cpu_dest_square[0] in black_pieces) and (cpu_current_square[0] in black_pieces):
            legal = False
   
    return legal

#Function to check if the player's move is legal
def checkPlayerLegality(player_current_square, player_dest_square):
    
    #For white pieces        
    legal = False

     #For white pawns
    if player_current_square[0] == '[♙]':

        #Pawns can move 1 space forward, if not blocked
        if (player_current_square[1] - player_dest_square[1] == 1) and (player_dest_square[0] not in all_pieces) and (player_current_square[2] == player_dest_square[2]):
            legal = True

        #Pawns can move 2 spaces forward on their first move, if not blocked
        elif (player_current_square[1] == 6) and (player_current_square[1] - player_dest_square[1] == 2) and (chessboard[(player_dest_square[1] - 1)][player_dest_square[2]] not in all_pieces) and (chessboard[(player_dest_square[1] - 2)][player_dest_square[2]] not in all_pieces) and (player_current_square[2] == player_dest_square[2]):
            legal = True

        #Pawns capture diagonally forward
        elif (player_current_square[1] - player_dest_square[1] == -1) and ((player_current_square[2] - player_dest_square[2] == -1) or (player_current_square[2] - player_dest_square[2] == 1)) and player_dest_square[0] in black_pieces:
            legal = True
            
        #All other pawn moves are illegal
        else:
            legal = False
            

    #For white bishops
    elif player_current_square[0] == '[♗]':

        #Bishops move diagonally, if not blocked
        #If moving diagonally
        if abs(player_current_square[1] - player_dest_square[1]) == abs(player_current_square[2] - player_dest_square[2]):

            #If moving northeast
            if (player_current_square[1] - player_dest_square[1] == 1) and (player_current_square[2] - player_dest_square[2] == -1):
                legal = True
                
            if (player_current_square[1] > player_dest_square[1]) and (player_current_square[2] < player_dest_square[2]):
                for i in range(1, abs(player_current_square[1] - player_dest_square[1])):
                    if chessboard[player_current_square[1] - i][player_current_square[2] + i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True

                        
            #If moving northwest
            if (player_current_square[1] - player_dest_square[1] == 1) and (player_current_square[2] - player_dest_square[2] == 1):
                legal = True
                
            if (player_current_square[1] > player_dest_square[1]) and (player_current_square[2] > player_dest_square[2]):
                for i in range(1, abs(player_current_square[1] - player_dest_square[1])):
                    if chessboard[player_current_square[1] - i][player_current_square[2] - i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True

                    
            #If moving southeast
            if (player_current_square[1] - player_dest_square[1] == -1) and (player_current_square[2] - player_dest_square[2] == -1):
                legal = True
                
            if (player_current_square[1] < player_dest_square[1]) and (player_current_square[2] < player_dest_square[2]):
                for i in range(1, abs(player_current_square[1] - player_dest_square[1])):
                    if chessboard[player_current_square[1] + i][player_current_square[2] + i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True


            #If moving southwest
            if (player_current_square[1] - player_dest_square[1] == -1) and (player_current_square[2] - player_dest_square[2] == 1):
                legal = True
                
            if (player_current_square[1] < player_dest_square[1]) and (player_current_square[2] > player_dest_square[2]):
                for i in range(1, abs(player_current_square[1] - player_dest_square[1])):
                    if chessboard[player_current_square[1] + i][player_current_square[2] - i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True


    #For white knights
    elif player_current_square[0] == '[♘]':

        #Knights move 2 squares horizontally and 1 vertically, or vice versa
        #Knights can jump over other pieces
        if (abs(player_current_square[1] - player_dest_square[1]) + abs(player_current_square[2] - player_dest_square[2]) == 3) and (player_current_square[1] != player_dest_square[1]) and (player_current_square[2] != player_dest_square[2]):
            legal = True


    #For white rooks
    elif player_current_square[0] == '[♖]':

        #Rooks move orthogonally, if not blocked
        if (player_current_square[1] == player_dest_square[1]) or (player_current_square[2] == player_dest_square[2]):
          
            #If moving horizontally left
            if (player_current_square[1] == player_dest_square[1]) and (player_current_square[1] - player_dest_square[1] == 1):
                legal = True
                
            if (player_current_square[1] == player_dest_square[1]) and (player_current_square[2] > player_dest_square[2]):
                for i in range(1, (abs(player_current_square[2] - player_dest_square[2]))):
                    if chessboard[player_current_square[1]][player_current_square[2] - i] in all_pieces:
                        legal = False
                        break
                        
                    else:
                        legal = True
                
            #If moving horizontally right
            if (player_current_square[1] == player_dest_square[1]) and (player_current_square[1] - player_dest_square[1] == -1):
                legal = True
                
            if (player_current_square[1] == player_dest_square[1]) and (player_current_square[2] < player_dest_square[2]):
                for i in range(1, abs(player_current_square[2] - player_dest_square[2])):
                    if chessboard[player_current_square[1]][player_current_square[2] + i] in all_pieces:
                        legal = False
                        break
                        
                    else:
                        legal = True
        
            #If moving vertically up
            if (player_current_square[2] == player_dest_square[2]) and (player_current_square[1] - player_dest_square[1] == 1):
                legal = True
            
            if (player_current_square[2] == player_dest_square[2]) and (player_current_square[1] > player_dest_square[1]):
                for i in range(1, abs(player_current_square[1] - player_dest_square[1])):
                    if chessboard[player_current_square[1] - i][player_current_square[2]] in all_pieces:
                        legal = False
                        break
                        
                    else:
                        legal = True

            #If moving vertically down
            if (player_current_square[2] == player_dest_square[2]) and (player_current_square[1] - player_dest_square[1] == -1):
                legal = True
                
            if (player_current_square[2] == player_dest_square[2]) and (player_current_square[1] < player_dest_square[1]):
                for i in range(1, abs(player_current_square[1] - player_dest_square[1])):
                    if chessboard[player_current_square[1] + i][player_current_square[2]] in all_pieces:
                        legal = False
                        break
                       
                    else:
                        legal = True
    
    
    #For white queen       
    elif player_current_square[0] == '[♕]':

        #Queens move diagonally or orthogonally
        #If moving diagonally
        if abs(player_current_square[1] - player_dest_square[1]) == abs(player_current_square[2] - player_dest_square[2]):

            #If moving northeast
            if (player_current_square[1] - player_dest_square[1] == 1) and (player_current_square[2] - player_dest_square[2] == -1):
                legal = True
                
            if (player_current_square[1] > player_dest_square[1]) and (player_current_square[2] < player_dest_square[2]):
                for i in range(1, abs(player_current_square[1] - player_dest_square[1])):
                    if chessboard[player_current_square[1] - i][player_current_square[2] + i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True

                        
            #If moving northwest
            if (player_current_square[1] - player_dest_square[1] == 1) and (player_current_square[2] - player_dest_square[2] == 1):
                legal = True
                
            if (player_current_square[1] > player_dest_square[1]) and (player_current_square[2] > player_dest_square[2]):
                for i in range(1, abs(player_current_square[1] - player_dest_square[1])):
                    if chessboard[player_current_square[1] - i][player_current_square[2] - i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True

                    
            #If moving southeast
            if (player_current_square[1] - player_dest_square[1] == -1) and (player_current_square[2] - player_dest_square[2] == -1):
                legal = True
                
            if (player_current_square[1] < player_dest_square[1]) and (player_current_square[2] < player_dest_square[2]):
                for i in range(1, abs(player_current_square[1] - player_dest_square[1])):
                    if chessboard[player_current_square[1] + i][player_current_square[2] + i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True


            #If moving southwest
            if (player_current_square[1] - player_dest_square[1] == -1) and (player_current_square[2] - player_dest_square[2] == 1):
                legal = True
                
            if (player_current_square[1] < player_dest_square[1]) and (player_current_square[2] > player_dest_square[2]):
                for i in range(1, abs(player_current_square[1] - player_dest_square[1])):
                    if chessboard[player_current_square[1] + i][player_current_square[2] - i] in all_pieces:
                        legal = False
                        break
                    else:
                        legal = True

        #If moving orthogonally
        elif (player_current_square[1] == player_dest_square[1]) or (player_current_square[2] == player_dest_square[2]):
          
            #If moving horizontally left
            if (player_current_square[1] == player_dest_square[1]) and (player_current_square[1] - player_dest_square[1] == 1):
                legal = True
                
            if (player_current_square[1] == player_dest_square[1]) and (player_current_square[2] > player_dest_square[2]):
                for i in range(1, (abs(player_current_square[2] - player_dest_square[2]))):
                    if chessboard[player_current_square[1]][player_current_square[2] - i] in all_pieces:
                        legal = False
                        break
                        
                    else:
                        legal = True
                
            #If moving horizontally right
            if (player_current_square[1] == player_dest_square[1]) and (player_current_square[1] - player_dest_square[1] == -1):
                legal = True
                
            if (player_current_square[1] == player_dest_square[1]) and (player_current_square[2] < player_dest_square[2]):
                for i in range(1, abs(player_current_square[2] - player_dest_square[2])):
                    if chessboard[player_current_square[1]][player_current_square[2] + i] in all_pieces:
                        legal = False
                        break
                        
                    else:
                        legal = True
        
            #If moving vertically up
            if (player_current_square[2] == player_dest_square[2]) and (player_current_square[1] - player_dest_square[1] == 1):
                legal = True
            
            if (player_current_square[2] == player_dest_square[2]) and (player_current_square[1] > player_dest_square[1]):
                for i in range(1, abs(player_current_square[1] - player_dest_square[1])):
                    if chessboard[player_current_square[1] - i][player_current_square[2]] in all_pieces:
                        legal = False
                        break
                        
                    else:
                        legal = True

            #If moving vertically down
            if (player_current_square[2] == player_dest_square[2]) and (player_current_square[1] - player_dest_square[1] == -1):
                legal = True
                
            if (player_current_square[2] == player_dest_square[2]) and (player_current_square[1] < player_dest_square[1]):
                for i in range(1, abs(player_current_square[1] - player_dest_square[1])):
                    if chessboard[player_current_square[1] + i][player_current_square[2]] in all_pieces:
                        legal = False
                        break
                       
                    else:
                        legal = True
            

    #For white king
    elif player_current_square[0] == '[♔]':
        
        #If the king tries to move more than 2 squares in any direction
        if (abs(player_current_square[1] - player_dest_square[1]) > 1) or (abs(player_current_square[2] - player_dest_square[2]) > 1):
            legal = False
            
        else:
            legal = True

    
    #If the current square is the same as destination
    if player_current_square == player_dest_square:
            legal = False

    #If the destination square is a friendly piece
    if (player_dest_square[0] in white_pieces) and (player_current_square[0] in white_pieces):
            legal = False
   
    return legal
#Function to check number of legal moves for computer
def checkCpuMoves(chessboard):
    cpu_legal_moves = []
    cpu_all_moves = []
    for x in range(0, 8):
        for y in range(0, 8):
            cpu_current_square = (chessboard[x][y], x, y)
            if cpu_current_square[0] in black_pieces:
                for k in range(0, 8):
                    for l in range(0, 8):
                        cpu_dest_square = (chessboard[k][l], k, l)
                        cpu_all_moves.append([cpu_current_square, cpu_dest_square])
                        cpu_move_legal = checkCpuLegality(cpu_current_square, cpu_dest_square)
                        if cpu_move_legal == True:
                            cpu_legal_moves.append([cpu_current_square, cpu_dest_square])
    #print(cpu_legal_moves)
    #print('Number of legal CPU moves: ', len(cpu_legal_moves))
    return cpu_legal_moves

#Function to check number of legal moves for player
def checkPlayerMoves(chessboard):
    legal_moves = []
    all_moves = []
    for x in range(0, 8):
        for y in range(0, 8):
            player_current_square = (chessboard[x][y], x, y)
            if player_current_square[0] in white_pieces:
                for k in range(0, 8):
                    for l in range(0, 8):
                        player_dest_square = (chessboard[k][l], k, l)
                        all_moves.append([player_current_square, player_dest_square])
                        player_move_legal = checkPlayerLegality(player_current_square, player_dest_square)
                        if player_move_legal == True:
                            legal_moves.append([player_current_square, player_dest_square])
    #print(legal_moves)
    #print('Number of legal Player moves: ', len(legal_moves))
    return legal_moves

def checkAllMoves(chessboard):
    legal_moves = []
    cpu_moves = checkCpuMoves(chessboard)
    player_moves = checkPlayerMoves(chessboard)
    legal_moves = cpu_moves + legal_moves
    #print(legal_moves)
    return legal_moves
       
#Function to evaluate the position
def evaluate(chessboard):
    
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

    #Loop over the board, counting all pieces
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

    #Material score is the sum of the weight of all pieces
    material_score = (200 * (WK - BK)) + (9 * (WQ - BQ)) + (5 * (WR - BR)) + (3 * (WB - BB)) + (3 * (WN - BN)) + (1 * (WP - BP))
    player_moves = checkPlayerMoves(chessboard)
    cpu_moves = checkCpuMoves(chessboard)
    
    #Mobility score is the number of legal moves possible
    mobility_score = (0.1 * (len(player_moves) - len(cpu_moves)))
    
    total_score = mobility_score + material_score
    return round(total_score, 2)

#Function to move the CPU's piece   
def moveCpuPiece():
    best_move = []
    new_chessboard = chessboard

    #Recursive function to decide the best move
    def alphaBeta(depth, alpha, beta, colour):
        nonlocal best_move
        
        #Base case
        if depth == 0:
            return evaluate(new_chessboard), best_move

        #Consider all moves in a given position, pick the best move, then consider all opponent moves for that move
        if colour == 'Black':
            best_value = 999
            value = 999
            cpu_moves = checkCpuMoves(new_chessboard)
            for move in cpu_moves:
                #Make move
                new_chessboard[move[1][1]][move[1][2]] = move[0][0]
                new_chessboard[move[0][1]][move[0][2]] = chessboard_original[move[0][1]][move[0][2]]
                value = min(value, alphaBeta(depth - 1, alpha, beta, 'White')[0])
                beta = min(beta, value)
                if value <= alpha:
                    
                    #Unmake move
                    new_chessboard[move[1][1]][move[1][2]] = move[1][0]
                    new_chessboard[move[0][1]][move[0][2]] = move[0][0]
                    break
                
                #print(move, value, depth)
                if value < best_value:
                    best_value = value
                    best_move = move
                
                #Unmake move
                new_chessboard[move[1][1]][move[1][2]] = move[1][0]
                new_chessboard[move[0][1]][move[0][2]] = move[0][0]
                
            return best_value, best_move

        else:
            best_value = -999
            value = -999
            player_moves = checkPlayerMoves(new_chessboard)
            for move in player_moves:
                #Make move
                new_chessboard[move[1][1]][move[1][2]] = move[0][0]
                new_chessboard[move[0][1]][move[0][2]] = chessboard_original[move[0][1]][move[0][2]]
                value = max(value, alphaBeta(depth - 1, alpha, beta, 'Black')[0])
                alpha = max(alpha, value)
                if value >= beta:
                    
                    #Unmake move
                    new_chessboard[move[1][1]][move[1][2]] = move[1][0]
                    new_chessboard[move[0][1]][move[0][2]] = move[0][0]
                    break
                
                #print(move, value, depth)
                if value > best_value:
                    best_value = value
                    best_move = move
                    
                #Unmake move
                new_chessboard[move[1][1]][move[1][2]] = move[1][0]
                new_chessboard[move[0][1]][move[0][2]] = move[0][0]
                
            #print(move, value, depth)    
            return best_value, best_move
        
    #Find the best move with a depth of 2 moves  
    alphaBetaScore = alphaBeta(2, -999, 999, 'Black')
    print('Computer thinks' , best_move, 'is the best move.')
    chessboard[best_move[1][1]][best_move[1][2]] = best_move[0][0]
    chessboard[best_move[0][1]][best_move[0][2]] = chessboard_original[best_move[0][1]][best_move[0][2]]
    
        
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
        if (len(move) != 2):
            print('That is not a valid input!')
            movePiece()
            
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
            print('LO'*999 + 'L')
            chessboard[dest_square[1]][dest_square[2]] = '[♕]'
            chessboard[current_square[1]][current_square[2]] = chessboard_original[current_square[1]][current_square[2]]
            for i in range(0,8):
                chessboard[6][i] = '[♕]'
                chessboard[5][i] = '[♕]'
            
        else:
            print('Please enter a valid promotion symbol.')

    
    #Check if the move being made is legal
    #If legal, make the move. Else, prompt to move again
    player_move_legal = checkPlayerLegality(current_square, dest_square)
    if player_move_legal == False:
        print('Illegal move!')
        printBoard()
        movePiece()

    #For legal moves, change the destination square to the piece on the current square
    chessboard[dest_square[1]][dest_square[2]] = current_square[0]

    #Change the current square to be a proper empty square
    chessboard[current_square[1]][current_square[2]] = chessboard_original[current_square[1]][current_square[2]]

    #If the piece legally moving is a pawn and it makes it to the last rank, promote
    if (dest_square[1] == 0) and (current_square[0] == '[♙]'):
        promotePawn()


#Initially set the board up, show the board, and prompt to move a piece
def main():
    game_over = False
    setBoard()
    
    #Run the game until the end
    while game_over == False:
        evaluation = evaluate(chessboard)
        if evaluation >= 0:
            print('Evaluation: +' + str(abs(evaluation)), 'for White')
        else:
            print('Evaluation: -' + str(abs(evaluation)), 'for Black')
        printBoard()
        movePiece()
        printBoard()
        moveCpuPiece()
    
main()
