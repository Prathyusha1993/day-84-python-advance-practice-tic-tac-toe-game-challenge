from dataclasses import is_dataclass

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

is_game_over = False
current_player = 'X'
while not is_game_over:
    draw_board()
    row, col = map(int, input(f'Player {current_player} provide your input as row and columns(1-3) (eg: 1,2):').split())
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
        board[row][col] = current_player

        if check_winner(current_player):
            draw_board()
            print(f'player {current_player} Wins!')
            is_game_over = True
        elif is_draw():
            draw_board()
            print('Its a draw')
            is_game_over=True
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    else:
        print('Invalid move! Try again.')