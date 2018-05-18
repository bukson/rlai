import numpy as np

from player import *
from random import shuffle


class Cpu:

    def __init__(self, board, p=P2):
        self.board = board
        self.player = p


class RandomCpu(Cpu):

    def get_move(self):
        possible_moves = self.board.get_possible_moves()
        np.random.shuffle(possible_moves)
        return possible_moves[0]


class MinMaxCpu(Cpu):

    def get_move(self):
        moves = []
        for move in self.board.get_possible_moves():
            x, y = move
            self.board.mark_field(x, y, self.player)
            moves.append((self.min_max(self.board, oppositve(self.player)), (x, y)))
            self.board.mark_field(x, y, Empty)
        shuffle(moves)
        if self.player == P1:
            return max(moves, key=lambda m: m[0])[1]
        else:
            return min(moves, key=lambda m: m[0])[1]

    @staticmethod
    def min_max(board, p: Player, depth=0) -> int:
        if board.get_winner() == P1:
            return 10 - depth
        if board.get_winner() == Empty:
            return 0
        if board.get_winner() == P2:
            return -10 + depth
        moves = []
        for move in board.get_possible_moves():
            x, y = move
            board.mark_field(x, y, p)
            moves.append((MinMaxCpu.min_max(board, oppositve(p), depth + 1), (x, y)))
            board.mark_field(x, y, Empty)
        if p == P1:
            return max(moves)[0]
        else:
            return min(moves)[0]


class QLearningCPU(Cpu):

    def __init__(self, board, p=P2):
        super().__init__(board, p)
        self.Q = {}
