import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'


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
    return {square: INITIAL_MARKER for square in range(1,10)}

def prompt(message):
    print(f'===> {message}')

def player_chooses_square(board):
    # valid spots would be in this list, if list at index = empty space
    empty_squares = [key 
                     for key, value in board.items() 
                     if value == INITIAL_MARKER]

    while True:
        valid_choices = [str(num) for num in empty_squares]
        prompt(f"Choose a square ({', '.join(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break # break when choice is valid
        
        prompt("Sorry, that's not a valid choice.")
    
    board[int(square)] = HUMAN_MARKER

def computer_chooses_square():
    empty_squares = [key 
                    for key, value in board.items()
                    if value == INITIAL_MARKER]
    square = random.choice(empty_squares)
    board[square] = COMPUTER_MARKER

board = initialize_board()
player_chooses_square(board)
display_board(board)