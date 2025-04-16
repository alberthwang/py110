

def displayBoard(board):
    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |   {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |   {board[6]}')
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
displayBoard(board)