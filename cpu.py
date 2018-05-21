import copy
from typing import Tuple

import numpy as np

from board import Board
from player import *
import random


class Cpu:

    def __init__(self, p=P2):
        self.player = p
        self.board = None

    def reward(self, value: int):
        pass


class RandomCpu(Cpu):

    def get_move(self):
        return random.choice(self.board.get_possible_moves())


class MinMaxCpu(Cpu):

    def get_move(self):
        if np.array_equal(self.board.board, np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])):
            return random.randint(0, 2), random.randint(0, 2)
        moves = []
        for move in self.board.get_possible_moves():
            x, y = move
            self.board.mark_field(x, y, self.player)
            moves.append((self.min_max(self.board, oppositve(self.player)), (x, y)))
            self.board.mark_field(x, y, Empty)
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
            moves.append(MinMaxCpu.min_max(board, oppositve(p), depth + 1))
            board.mark_field(x, y, Empty)
        if p == P1:
            return max(moves)
        else:
            return min(moves)


class QLearningCPU(Cpu):

    def __init__(self, p=P2, epsilon=0.2, alpha=0.3, gamma=0.9, decay=0.9):
        super().__init__(p)
        self.q = {}  # (state, action) keys: Q values
        self.epsilon = epsilon  # e-greedy chance of random exploration
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor for future reward
        self.decay = decay
        self.last_board = None
        self.last_move = None
        self.default_reward = 1.0

    def next_state(self, action: Tuple[int, int], board=None) -> int:
        if board is None:
            board = self.board
        next_board = copy.deepcopy(board)
        next_board.mark_field(*action, self.player)
        return self.get_state(next_board)

    def get_state(self, board):
        return board.state() + str(self.player.number)

    def getQ(self, state: int):
        return self.q.get(state, self.default_reward)

    def get_move(self):
        return self.__get_move(self.board)

    def __get_move(self, board):
        actions = board.get_possible_moves()

        if random.random() < self.epsilon:  # explore!
            self.last_board = copy.deepcopy(board)
            self.last_move = random.choice(actions)
            return self.last_move

        qs = [self.getQ(self.next_state(a)) for a in actions]
        max_q = max(qs)

        if qs.count(max_q) > 1:
            # more than 1 best option; choose among them randomly
            best_options = [i for i in range(len(actions)) if qs[i] == max_q]
            i = random.choice(best_options)
        else:
            i = qs.index(max_q)

        self.last_board = copy.deepcopy(board)
        self.last_move = actions[i]
        return actions[i]

    def reward(self, value: int):
        if self.last_move:
            self.learn(self.last_board, self.last_move, value)
            # if self.epsilon > 0.002:
            self.epsilon = self.epsilon * self.decay
            # self.default_reward = self.default_reward * self.decay

    def learn(self, state: Board, action: Tuple[int, int], reward: int):
        prev = self.getQ(self.get_state(state))
        possible_actions = state.get_possible_moves()
        maxqnew = max([self.getQ(self.next_state(a, state)) for a in possible_actions])
        self.q[self.next_state(action, state)] = prev + self.alpha * ((reward + self.gamma * maxqnew) - prev)
        q = self.q
        pass

    @staticmethod
    def _transfer_state(state: str) -> str:
        new_state = []
        for s in state:
            if s == '1':
                new_state.append('2')
            elif s == '2':
                new_state.append('1')
            else:
                new_state.append('0')
        return ''.join(new_state)

    def transfer_experience(self, transfer_q):
        new_q = {}
        for state,reward in self.q.items():
            new_q[state] = reward
            new_q[self._transfer_state(state)] = reward
        for state,reward in transfer_q.items():
            new_q[state] = reward
            new_q[self._transfer_state(state)] = reward
        self.q = new_q
