import pytest
from tic_tac_toe import check_win

class TestTicTacToeCheckWin:
    def setup_method(self):
        # Reset the squares list before each test
        global squares
        squares = [None] * 9

    def test_player_wins_horizontal(self):
        player = 'X'
        squares[0] = squares[1] = squares[2] = player
        assert check_win(player) is True

    def test_player_wins_vertical(self):
        player = 'O'
        squares[1] = squares[4] = squares[7] = player
        assert check_win(player) is True

    def test_player_wins_diagonal(self):
        player = 'X'
        squares[0] = squares[4] = squares[8] = player
        assert check_win(player) is True

    def test_no_win_condition(self):
        player = 'O'
        squares[0] = squares[4] = squares[8] = player
        squares[2] = squares[6] = 'X'
        assert check_win(player) is False

    def test_empty_board(self):
        player = 'X'
        assert check_win(player) is False

    def test_win_condition_not_met(self):
        player = 'O'
        squares[0] = squares[1] = player
        squares[2] = 'X'
        assert check_win(player) is False

    def test_win_condition_for_other_player(self):
        player1 = 'X'
        player2 = 'O'
        squares[0] = squares[1] = squares[2] = player2
        assert check_win(player1) is False

    def test_win_condition_with_mixed_players(self):
        player = 'X'
        squares[0] = squares[1] = player
        squares[2] = 'O'
        assert check_win(player) is False

    def test_win_condition_with_invalid_player(self):
        player = 'A'
        squares[0] = squares[1] = squares[2] = player
        assert check_win(player) is False
