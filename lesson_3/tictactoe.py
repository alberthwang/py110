import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_NEEDED_TO_WIN = 5
WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # cols
        [1, 5, 9], [3, 5, 7]             # diags
    ]


def display_board(board):
   # os.system('cls')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}")
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

def join_or(sequence, delimiter = ', ', joiner = 'or'):
    # print(squares)
    # joined_word = ''
    # if len(squares) == 1:
    #     return squares
    # elif len(squares) == 2:
    #     return str(squares[0]) + joiner + str(squares[1])
    # else:
    #     for i in range(0, len(squares) - 1):
    #         joined_word += str(squares[i]) + seperator

    #     joined_word += joiner + str(squares[len(squares)-1])
    # return joined_word 
    match len(sequence):
        case 0:
            return ''
        case 1:
            return str(sequence[0])
        case 2:
            return f'{sequence[0]} {joiner} {sequence[1]}'
        
    leading_items = delimiter.join(str(item) for item in sequence[0:-1])
    return f"{leading_items}{delimiter}{joiner} {sequence[-1]}"



def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if(board[sq1] == HUMAN_MARKER
           and board[sq2] == HUMAN_MARKER
           and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif(board[sq1] == COMPUTER_MARKER
             and board[sq2] == COMPUTER_MARKER
             and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
        
    return None

def someone_won(board):
    return bool(detect_winner(board))

def find_at_risk_square(board, line, marker):
    markers_in_line = [board[square] for square in line]
    
    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
            
    return None


def player_chooses_square(board):
    # valid spots would be in this list, if list at index = empty space
    # empty_squares = [key 
    #                  for key, value in board.items() 
    #                  if value == INITIAL_MARKER]

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
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
    
    square = None
    #offnsiv move
    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(board, line, COMPUTER_MARKER)
            if square:
                break
    
    #defensive move
    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(board, line, HUMAN_MARKER)
            if square:
                break
    
    if not square and board[5] is not INITIAL_MARKER:
        square = 5
        
    if not square:
        square = random.choice(empty_squares(board))
        
    board[int(square)] = COMPUTER_MARKER


def play_tic_tac_toe():
    player_wins, computer_wins = 0, 0
    while True:    

        while player_wins < GAMES_NEEDED_TO_WIN and computer_wins < GAMES_NEEDED_TO_WIN:
            print(player_wins, computer_wins)
            board = initialize_board()

            while True:
                display_board(board)

                player_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break

                computer_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break
                
                display_board(board)
            if someone_won(board):
                prompt(f"{detect_winner(board)} won!")
                if detect_winner(board) == 'Player':
                    player_wins += 1
                else:
                    computer_wins += 1
                    
            elif board_full(board):
                prompt("It's a tie!")
                
            # if player_wins == 5 or computer_wins == 5:
            #     break
                
        prompt("Play again? (y or n)")
        answer = input().lower()
        
        if answer[0] != 'y':
            break
        else:
            player_wins, computer_wins = 0, 0

    prompt("Thanks for playing Tic Tac Toe!")

play_tic_tac_toe()