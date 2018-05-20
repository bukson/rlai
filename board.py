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
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != Empty.number:
                return players[self.board[i][0]]

            if self.board[0][i] == self.board[1][i] == self.board[2][i] != Empty.number:
                return players[self.board[0][i]]

        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] != Empty.number:
            return players[self.board[0][0]]

        if self.board[2, 0] == self.board[1, 1] == self.board[0, 2] != Empty.number:
            return players[self.board[2][0]]

        if 0 not in self.board[:, 0] and 0 not in self.board[:, 1] and 0 not in self.board[:, 2]:
            return Empty

        return None

    def get_possible_moves(self) -> List[tuple]:
        pm = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    pm.append((j, i))
        return pm

    def mark_field(self, x: int, y: int, player: Player):
        self.board[y][x] = player.number

    def state(self):
        return ''.join(map(str, self.board.flatten()))

    @staticmethod
    def from_state(state: str):
        new_board = np.array(3 * [3 * [Empty.number]])
        for index, field in enumerate(state[:-1]):
            x = index % 3
            y = index // 3
            new_board[y, x] = int(field)
        return new_board

