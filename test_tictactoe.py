import pytest

from tictactoe import *

EMPTY = None

def test_player_odd_empties_returns_x():
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    assert player(board) == 'X'


def test_player_even_empties_returns_o():
    board = [[EMPTY, "X", EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    assert player(board) == 'O'


def test_action_no_action_on_full_board():
    board = [["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]]
    
    assert not actions(board)


def test_action_if_empty_cell():
    board = [["X", "X", EMPTY],
            ["X", "X", "X"],
            ["X", EMPTY, "X"]]
    act = actions(board)
    assert (0,2) in act and (2,1) in act


def test_result_success():
    board = [["X", "X", EMPTY],
            ["X", "X", "X"],
            ["X", EMPTY, "X"]]
    action = (0, 2)
    resulting_board = [["X", "X", "O"],
                      ["X", "X", "X"],
                      ["X", EMPTY, "X"]]

    assert result(board, action) == resulting_board


def test_result_exception():
    board = [["X", "X", EMPTY],
            ["X", "X", "X"],
            ["X", EMPTY, "X"]]
    action = (0, 1)
    with pytest.raises(IndexError):
        result(board, action)


def test_winner_row():
    board = [[EMPTY, EMPTY, EMPTY],
            ['X', 'X', 'X'],
            [EMPTY, EMPTY, EMPTY]]
    assert winner(board) == 'X'


def test_winner_column():
    board = [[EMPTY, EMPTY, 'O'],
            [EMPTY, EMPTY, 'O'],
            [EMPTY, EMPTY, 'O']]
    assert winner(board) == 'O'


def test_winner_first_diagonal():
    board = [['X', EMPTY, EMPTY],
            [EMPTY, 'X', EMPTY],
            [EMPTY, EMPTY, 'X']]
    assert winner(board) == 'X'


def test_winner_second_diagonal():
    board = [[EMPTY, EMPTY, 'X'],
            [EMPTY, 'X', EMPTY],
            ['X', EMPTY, EMPTY]]
    assert winner(board) == 'X'


def test_terminal_with_winner():
    board = [['X', EMPTY, EMPTY],
            [EMPTY, 'X', EMPTY],
            [EMPTY, EMPTY, 'X']]
    assert terminal(board)


def test_terminal_on_full_board():
    board = [["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]]
    assert terminal(board)


def test_not_terminal_if_empty_spaces():
    board = [["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", EMPTY]]
    assert not terminal(board)


def test_utility_X_winner():
    board = [['X', EMPTY, EMPTY],
            [EMPTY, 'X', EMPTY],
            [EMPTY, EMPTY, 'X']]
    assert utility(board) == 1


def test_utility_O_winner():
    board = [['O', EMPTY, EMPTY],
            [EMPTY, 'O', EMPTY],
            [EMPTY, EMPTY, 'O']]
    assert utility(board) == -1


def test_utility_no_winner():
    board = [['X', EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, 'X']]
    assert utility(board) == 0


def test_minimax_O_chooses_right_move():
    board = [[EMPTY, "X", "O"],
            ["O", "X", "X"],
            ["X", EMPTY, "O"]]
    correct_move = (2, 1)
    assert minimax(board) == correct_move


def test_minimax_X_chooses_right_move():
    board = [["X", "O", "O"],
            ["O", "X", EMPTY],
            ["X", EMPTY, EMPTY]]
    correct_move = (2, 2)
    assert minimax(board) == correct_move


def test_minimax_no_moves_returns_none():
    board = [["X", "X", "O"],
            ["O", "X", "X"],
            ["X", "O", "O"]]
    correct_move = None
    assert minimax(board) == correct_move


def test_minimax_O_chooses_right_move_v2():
    board = [["X", EMPTY, "O"],
            [EMPTY, "X", EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    correct_move = (2, 2)
    assert minimax(board) == correct_move


def test_minimax_X_chooses_right_move_v2():
    board = [[EMPTY, "X", "O"],
            [EMPTY, "O", "X"],
            [EMPTY, EMPTY, EMPTY]]
    correct_move = (2, 0)
    assert minimax(board) == correct_move