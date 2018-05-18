from enum import IntEnum

import numpy as np


class Field(IntEnum):
    Empty = 0
    P1 = 1
    P2 = 2


class Board:

    def __init__(self, board: np.array=None):
        if board is not None:
            self.board = board
        else:
            self.board = np.array(3 * [3 * [Field.Empty]])

    def get_winner(self) -> Field:
        for i in range(3):
            if np.array_equal(self.board[i, :], 3 * [Field.P1]):
                return Field.P1
            if np.array_equal(self.board[i, :], 3 * [Field.P2]):
                return Field.P2
            if np.array_equal(self.board[:, i], 3 * [Field.P1]):
                return Field.P1
            if np.array_equal(self.board[:, i], 3 * [Field.P2]):
                return Field.P2

        if np.array_equal(np.diag(self.board), 3 * [Field.P1]):
            return Field.P1
        if np.array_equal(np.diag(self.board,1), 3 * [Field.P2]):
            return Field.P2

        if np.array_equal(np.rot90(self.board).diagonal(), 3 * [Field.P1]):
            return Field.P1
        if np.array_equal(np.rot90(self.board).diagonal(), 3 * [Field.P2]):
            return Field.P2

        return Field.Empty
