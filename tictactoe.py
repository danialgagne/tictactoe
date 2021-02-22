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

    for row_idx, row in enumerate(board):
        for col_idx, cell in enumerate(row):
            if cell == EMPTY:
                actions_set.add((row_idx, col_idx))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    resulting_board = deepcopy(board)

    if resulting_board[action[0]][action[1]] is None:
        resulting_board[action[0]][action[1]] = turn
        return resulting_board
    else:
        raise IndexError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
