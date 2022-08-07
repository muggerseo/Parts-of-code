from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('   |   |   ')
    print(' ' + board[7]+' | '+ board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4]+' | '+ board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1]+' | '+ board[2] + ' | ' + board[3])
    print('   |   |   ')

def player_input():
    
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    
    marker = ''
    
    while not (marker == 'X' or marker =='O'): #or while marker != 'X' and marker != 'O':
    
        marker = input('Player1: choose X or O: ').upper()
        
    if marker =='X':
        return('X','O')
    else:
        return('O','X')

def place_marker(board, marker, position):
    
    board[position] = marker
    
    if type(marker) is int and marker not in range [1,9]:
            print('enter number between 1-9')

def win_check(board,mark):
    
    #WIN TIC-TAC-TOE?
    
    #ALL ROWS, AND CHECK TOE SEE IF THEY ALL SHARE THE SAME MARKER?
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

import random

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    #board is full so True returned    
    return True

def player_choice(board):
    
    position = 0
    
    while True:
        try:
            position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position)
            position = int(input('Choose a position: (1-9) '))
        except ValueError:
            print('Wrong input! enter number of the cell between 1-9: ')
        
        return position

def replay():

        while True:
            try:
                #choice not in ('Yes','No'):
                choice = input("play again? Enter Yes or No ")
            except ValueError:
                print("Please print Yes or No exactly")
                
            if choice == 'Yes':
                print('New game!')
                return choice == 'Yes'
            elif choice == 'No':
                print('See ya!')
                break

print ('Welcome to the game')

while True:
    
    #play the game
    
    ##set everything up (board,whos first, markers X,O)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + "will go first")
    
    play_game = input('Ready to play? y or n? ')
                
    if play_game == 'y':
           game_on = True
    else:
        game_on = False
 

    
    while game_on:
        
        if turn == 'Player 1':
            
            #show the board
            display_board(the_board)
            #choose position
            position = player_choice(the_board)
            #place marker
            place_marker(the_board,player1_marker,position)
            
            #check for tie
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player one has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    game_on = False
                else:
                    turn = 'Player 2'
##################################################################
            
        else:
            #show the board
            display_board(the_board)
            #choose position
            position = player_choice(the_board)
            #place marker
            place_marker(the_board,player2_marker,position)
            
            #or check for tie
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player two has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    game_on = False
                else:
                    turn = 'Player 1'
            # no tie no win? next player turn 
    
    if not replay():
        break        