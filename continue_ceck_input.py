def player_choice(board):
    
    position = 0
    
    while True:
        try:
            position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position)
            position = int(input('Choose a position: (1-9) '))
        except ValueError:
            print('Wrong input! enter number of the cell between 1-9: ')
            continue
        
        return position