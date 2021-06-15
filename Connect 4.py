import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    top_row = board[ROW_COUNT - 1]
    if (col in np.arange(len(top_row))):
        return top_row[col] == 0
    else:
        return "choose something else"


def print_board(board):
    print(np.flip(board, 0))


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def winning_move(board, row, col, piece):
    pass


board = create_board()
game_over = False
turn = 0

while not game_over:

    # Ask for player 1 Input
    if turn % 2 == 0:
        col = int(input("player 1, make your selection (0-6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

    # Ask for player 2 Input
    else:
        col = int(input("player 2, make your selection (0-6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
    print_board(board)
    turn += 1
