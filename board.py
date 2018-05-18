import numpy as np
from player import *


class Board:

    def __init__(self, board: np.array=None):
        if board is not None:
            self.board = board
        else:
            self.board = np.array(3 * [3 * [Empty.number]])

    def get_winner(self) -> Player:
        for i in range(3):
            if np.array_equal(self.board[i, :], 3 * [P1.number]):
                return P1
            if np.array_equal(self.board[i, :], 3 * [P2.number]):
                return P2
            if np.array_equal(self.board[:, i], 3 * [P1.number]):
                return P1
            if np.array_equal(self.board[:, i], 3 * [P2.number]):
                return P2

        if np.array_equal(np.diag(self.board), 3 * [P1.number]):
            return P1
        if np.array_equal(np.diag(self.board, 1), 3 * [P2.number]):
            return P2

        if np.array_equal(np.rot90(self.board).diagonal(), 3 * [P1.number]):
            return P1
        if np.array_equal(np.rot90(self.board).diagonal(), 3 * [P2.number]):
            return P2

        if not np.isin(0, self.board):
            return Empty

        return None

    def assert_valid_move(self, x, y):
        if x > 2 or y > 2 or  x < 0 or y < 0:
            return False
        if self.board[y][x] != 0:
            return False
        return True

    def mark_field(self, x, y, player):
        self.board[y][x] = player.number
