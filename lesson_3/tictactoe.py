

def display_board(board):
    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')
    print('')


board = {1 : 'X',
         2 : ' ',
         3 : ' ',
         4 : 'O',
         5 : ' ',
         6 : ' ',
         7 : ' ',
         8 : ' ',
         9 : ' '}

def initialize_board():
    return {square: ' ' for square in range(1,10)}

def prompt(message):
    print(f'===> {message}')

def player_chooses_square(board):
    prompt('Choose a square (1-9):')
    square = input()
    board[int(square)] = 'X'

board = initialize_board()
player_chooses_square(board)
display_board(board)