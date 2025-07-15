from IPython.display import clear_output
import random 
test_board = ['#','-','-','-','-','-','-','-','-','-','-','-']
def display_board(b):
    clear_output()
    print(b[1]+'|'+b[2]+'|'+b[3])
    print(b[4]+'|'+b[5]+'|'+b[6])
    print(b[7]+'|'+b[8]+'|'+b[9])






def player_input():
    '''
    OUTPUT = (PLAYER 1 MARKER, PLAYER 2 MARKER)
    '''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    





def place_marker(board, marker, position):
    board[position] = marker





    
def win_mark(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark ) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or 
        (board[3] == mark and board[6] == mark and board[9] == mark ) or
        (board[1] == mark and board[5] == mark and board[9] == mark) or 
        (board[3] == mark and board[5] == mark and board[7] == mark))






def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    




def space_check(board, position):
    return board[position] == '-'






def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True






def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position (1-9):'))
    return position







def replay():
    choice = input("play again? Enter Yes or No")
    return choice == 'Yes'










# while loop to keep runing the game 
print('---------------___WELCOME TO TIC TAC TOE GAME___---------------')
while True:
    #play the game 
    # set every thing up (board , whos first , choose markers  )
    the_board = ['-']*10
    player1,player2 = player_input()

    turn = choose_first()
    print( turn + ' will go first ')

    play_game  =  input('ready to play? (Y,N):')
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    # game play
    while game_on:
        if turn == 'Player 1':
            # show the board
            display_board(the_board)
            #choose position 
            position = player_choice(the_board)
            #place the marker on the position 
            place_marker(the_board,player1,position)
            # check if they won 
            if win_mark(the_board,player1):
                display_board(the_board)
                print('PLAYER1 HAS WON !!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('THE GAME HAS TIE !')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            # show the board
            display_board(the_board)
            #choose position 
            position = player_choice(the_board)
            #place the marker on the position 
            place_marker(the_board,player2,position)
            # check if they won 
            if win_mark(the_board,player2):
                display_board(the_board)
                print('PLAYER1 HAS WON !!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('THE GAME HAS TIE !')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break
# break out of the while loop on replay()