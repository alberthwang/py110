import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'


def display_board(board):
    os.system('cls')

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

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return False

def player_chooses_square(board):
    # valid spots would be in this list, if list at index = empty space
    # empty_squares = [key 
    #                  for key, value in board.items() 
    #                  if value == INITIAL_MARKER]

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({', '.join(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break # break when choice is valid
        
        prompt("Sorry, that's not a valid choice.")
    
    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    # empty_squares = [key 
    #                 for key, value in board.items()
    #                 if value == INITIAL_MARKER]
    if board_full(board): return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER


board = initialize_board()
display_board(board)

while True:
    player_chooses_square(board)
    computer_chooses_square(board)
    display_board(board)

    if someone_won(board) or board_full(board):
        break
    
