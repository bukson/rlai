from typing import List

import numpy as np
from player import *


class Board:

    def __init__(self, board: np.array = None):
        if board is not None:
            self.board = board
        else:
            self.board = np.array(3 * [3 * [Empty.number]])

    def get_winner(self) -> Player:
        for i in range(3):
            if self.board[i][0] == P1.number and \
                self.board[i][1] == P1.number and \
                self.board[i][2] == P1.number:
                    return P1

            if self.board[i][0] == P2.number and \
                    self.board[i][1] == P2.number and \
                    self.board[i][2] == P2.number:
                return P2

            if self.board[0][i] == P1.number and \
                    self.board[1][i] == P1.number and \
                    self.board[2][i] == P1.number:
                return P1

            if self.board[0][i] == P2.number and \
                    self.board[1][i] == P2.number and \
                    self.board[2][i] == P2.number:
                return P2

            # if np.array_equal(self.board[i, :], 3 * [P1.number]):
            #     return P1
            # if np.array_equal(self.board[i, :], 3 * [P2.number]):
            #     return P2
            # if np.array_equal(self.board[:, i], 3 * [P1.number]):
            #     return P1
            # if np.array_equal(self.board[:, i], 3 * [P2.number]):
            #     return P2

        # if np.array_equal(np.diag(self.board), 3 * [P1.number]):
        #     return P1
        # if np.array_equal(np.diag(self.board, 1), 3 * [P2.number]):
        #     return P2

        if self.board[0,0] == P1.number and \
            self.board[1,1] == P1.number and\
            self.board[2,2] == P1.number:
            return P1
        if self.board[0,0] == P2.number and \
            self.board[1,1] == P2.number and\
            self.board[2,2] == P2.number:
            return P2

        if self.board[0,2] == P1.number and \
            self.board[1,1] == P1.number and\
            self.board[2,0] == P1.number:
            return P1
        if self.board[0,2] == P2.number and \
            self.board[1,1] == P2.number and\
            self.board[2,0] == P2.number:
            return P2

        # if np.array_equal(np.rot90(self.board).diagonal(), 3 * [P1.number]):
        #     return P1
        # if np.array_equal(np.rot90(self.board).diagonal(), 3 * [P2.number]):
        #     return P2

        if not 0 in self.board[:, 0] and not 0 in self.board[:, 1] and not 0  in self.board[:, 2]:
            return Empty

        return None

    def get_possible_moves(self) -> List[tuple]:
        r1, r2 = np.where(self.board == 0)
        return list(map(lambda x: tuple(x),np.column_stack((r2, r1))))

    def mark_field(self, x: int, y: int, player: Player):
        self.board[y][x] = player.number

    def __hash__(self):
        return int(''.join(map(str, self.board.flatten())))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
