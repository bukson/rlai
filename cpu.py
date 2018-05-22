import copy
from collections import defaultdict
from typing import Tuple

import numpy as np

from board import Board
from player import *
import random


class Cpu:

    def __init__(self, p=P2):
        self.player = p

    def reward(self, value: int, board):
        pass

    def get_possible_moves(self, board: Tuple):
        pm = []
        for y in range(3):
            for x in range(3):
                if board[x + 3 * y] == 0:
                    pm.append((x, y))
        return pm

    def start_game(self):
        pass


class RandomCpu(Cpu):

    def get_move(self, board):
        return random.choice(board.get_possible_moves())


class MinMaxCpu(Cpu):

    def get_move(self, board):
        if not any(board.board):
            return random.randint(0, 2), random.randint(0, 2)
        moves = []
        for move in self.get_possible_moves(board.board):
            x, y = move
            board.mark_field(x, y, self.player)
            moves.append((self.min_max(board, opposite(self.player)), (x, y)))
            board.mark_field(x, y, Empty)
        random.shuffle(moves)
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
            moves.append(MinMaxCpu.min_max(board, opposite(p), depth + 1))
            board.mark_field(x, y, Empty)
        if p == P1:
            return max(moves)
        else:
            return min(moves)


class QLearningCPU(Cpu):

    def __init__(self, p=P2, epsilon=0.2, alpha=0.3, gamma=0.9, decay=0.9, min_epsilon=0.1):
        super().__init__(p)
        self.q = {}  # state,action: reward
        self.epsilon = epsilon  # e-greedy chance of random exploration
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor for future reward
        self.decay = decay
        self.last_board = None
        self.last_move = None
        self.default_reward = 1.0
        self.min_epsion = min_epsilon

    def start_game(self):
        self.last_board = (0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.last_move = None

    def getQ(self, state, action) -> float:
        if self.q.get((state, action)) is None:
            self.q[(state, action)] = self.default_reward
        return self.q[(state, action)]

    def get_move(self, board):
        self.last_board = tuple(board.board)
        actions = self.get_possible_moves(self.last_board)

        if random.random() < self.epsilon:  # explore!
            self.last_move = random.choice(actions)
            return self.last_move

        qs = [self.getQ(self.last_board, a) for a in actions]
        max_q = max(qs)

        if qs.count(max_q) > 1:
            # more than 1 best option; choose among them randomly
            best_options = [i for i in range(len(actions)) if qs[i] == max_q]
            i = random.choice(best_options)
        else:
            i = qs.index(max_q)

        self.last_move = actions[i]
        return actions[i]

    def reward(self, value: int, board):
        if self.last_move:
            self.learn(self.last_board, self.last_move, value, tuple(board.board))

    def learn(self, state: Tuple, action: Tuple[int, int], reward: int, result_state: Tuple):
        state_reward = self.getQ(state, action)
        possible_actions = self.get_possible_moves(state)
        maxqnew = max([self.getQ(result_state, action) for action in possible_actions])
        new_reward = state_reward + self.alpha * ((reward + self.gamma * maxqnew) - state_reward)
        self.q[(tuple(state), action)] = new_reward
        # q = self.q
        # pass
