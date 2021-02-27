"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    empty_counter = 0

    # if the number of empty's is odd, it's o's turn
    for row in board:
        for cell in row:
            if cell is None:
                empty_counter += 1
    return X if empty_counter % 2 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()

    # find coordinates of all emty cells and add them to a set
    for row_idx, row in enumerate(board):
        for col_idx, cell in enumerate(row):
            if cell == EMPTY:
                actions_set.add((row_idx, col_idx))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # get the current turn
    turn = player(board)
    resulting_board = deepcopy(board)

    # add the current players move to the board
    if resulting_board[action[0]][action[1]] is None:
        resulting_board[action[0]][action[1]] = turn
        return resulting_board
    else:
        raise IndexError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for row in board:
        row_set = set(row)
        # since sets don't allow duplicates, len 1 means all items are the same
        if len(row_set) == 1 and row[0] is not None:
            return row[0]

    # check columns
    columns = list(zip(*board))
    for column in columns:
        column_set = set(column)
        if len(column_set) == 1 and column[0] is not None:
            return column[0]

    # check diagonals
    first_diagonal = []
    for i in range(3):
        first_diagonal.append(board[i][i])

    if len(set(first_diagonal)) == 1 and first_diagonal[0] is not None:
        return first_diagonal[0]
    
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] is not None:
            return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check for a winner or no moves left
    return any([winner(board), not actions(board)])


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # use values dict for mapping
    win_value = {'X': 1, 'O': -1, None: 0}
    return win_value[winner(board)]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_move = None
    if player(board) == X:
        current_max = -2
        for action in actions(board):
            v = min_value(result(board, action))
            if v > current_max:
                current_max = v
                best_move = action
    if player(board) == O:
        current_min = 2
        for action in actions(board):
            v = max_value(result(board, action))
            if v < current_min:
                current_min = v
                best_move = action
    return best_move
            

def max_value(board):
    v = -2
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = 2
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v