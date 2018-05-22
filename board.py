from typing import List

import numpy as np
from player import *


class Board:

    def __init__(self, board: List = None):
        if board is not None:
            self.board = board
        else:
            self.board = [0 for _ in range(9)]

    def get_winner(self) -> Player:
        for i in range(3):
            if self.board[3*i] == self.board[3*i + 1] == self.board[3*i + 2] != Empty.number:
                return players[self.board[3*i]]

            if self.board[i] == self.board[i + 3] == self.board[i + 6] != Empty.number:
                return players[self.board[i]]

        if self.board[0] == self.board[4] == self.board[8] != Empty.number:
            return players[self.board[0]]

        if self.board[2] == self.board[4] == self.board[6] != Empty.number:
            return players[self.board[2]]

        if 0 not in self.board:
            return Empty

        return None

    def get_possible_moves(self) -> List[tuple]:
        pm = []
        for y in range(3):
            for x in range(3):
                if self.board[x + 3*y] == 0:
                    pm.append((x, y))
        return pm

    def mark_field(self, x: int, y: int, player: Player):
        self.board[x + 3 * y] = player.number

    @staticmethod
    def from_state(state: str):
        return list(map(int, state))

    def draw(self):
        print()
        for x in range(3):
            for y in range(3):
                print(players[self.board[x + 3*y]].mark + ' ', end='')
            print()
        print()

