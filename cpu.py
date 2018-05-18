import numpy as np

from player import *


class RandomCpu:

    def __init__(self, board, p=P2):
        self.board = board
        self.player = p

    def get_move(self):
        x = np.random.randint(0, 3)
        y = np.random.randint(0, 3)
        if not self.board.assert_valid_move(x, y):
            return self.get_move()
        else:
            return x, y


class MinMaxCpu:
    def __init__(self, board, p=P2):
        self.board = board
        self.player = p

    def get_move(self):
        moves = []
        for x in range(3):
            for y in range(3):
                if self.board.assert_valid_move(x, y):
                    self.board.mark_field(x, y, self.player)
                    moves.append((self.min_max(self.board, oppositve(self.player)),(x,y)))
                    self.board.mark_field(x, y, Empty)
        if self.player == P1:
            return max(moves)[1]
        else:
            return min(moves)[1]

    @staticmethod
    def min_max(board, p: Player, depth=0) -> int:
        if board.get_winner() == P1:
            return 10 - depth
        if board.get_winner() == Empty:
            return 0
        if board.get_winner() == P2:
            return -10 + depth
        moves = []
        for x in range(3):
            for y in range(3):
                if board.assert_valid_move(x, y):
                    board.mark_field(x, y, p)
                    moves.append((MinMaxCpu.min_max(board, oppositve(p), depth + 1),(x,y)))
                    board.mark_field(x, y, Empty)
        if p == P1:
            return max(moves)[0]
        else:
            return min(moves)[0]
