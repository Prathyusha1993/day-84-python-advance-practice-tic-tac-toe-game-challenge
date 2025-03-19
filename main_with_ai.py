import random

board = []
for _ in range(3):
    board.append([' ']*3)
def draw_board():
    for row in board:
        print(' | '.join(row))
        print('-'*9)

def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def ai_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)


is_game_over = False
player = 'X'
ai = 'O'
while not is_game_over:
    draw_board()

    if player == 'X':
        try:
            row, col = map(int, input(f'Player {player} provide your input as row and columns(1-3) (eg: 1,2):').split())
            row -= 1
            col -= 1
        except ValueError:
            print('Invalid input, please enter twonumber between 1 and 3')
            continue
    else:
        row,col = ai_move()
        print(f'AI plays at ({row+1} {col+1})')


    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
        board[row][col] = player

        if check_winner(player):
            draw_board()
            print(f'player {player} Wins!')
            is_game_over = True
        elif is_draw():
            draw_board()
            print('Its a draw')
            is_game_over=True
        else:
            player = 'O' if player == 'X' else 'X'
    else:
        print('Invalid move! Try again.')
