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