import os

from board import Board
from player import *
import numpy as np
from cpu import *


class Game:

    def __init__(self, first_player=P1):
        self.board = Board()
        self.player = first_player
        self.cpu = MinMaxCpu(self.board, oppositve(self.player))

    def draw(self):
        print()
        for x in range(3):
            for y in range(3):
                print(players[self.board.board[x][y]].mark + ' ', end='')
            print()
        print()

    def get_human_move(self):
        while True:
            x, y = map(int, input('What is your move  x y ?\n').split())
            if (x, y) not in self.board.get_possible_moves():
                continue
            self.board.mark_field(x, y, self.player)
            return

    def get_cpu_move(self):
        x, y = self.cpu.get_move()
        self.board.mark_field(x, y, oppositve(self.player))

    def play(self):
        player = self.player
        while True:
            self.draw()
            winner = self.board.get_winner()
            if winner is not None:
                if winner == Empty:
                    print('Draw')
                else:
                    print(f'Player {winner.number} won')
                return
            if player == P1:
                self.get_human_move()
            else:
                self.get_cpu_move()
            player = oppositve(player)


class CpuGame:

    def __init__(self, cpu1, cpu2):
        self.score = {0: 0, 1: 0, 2: 0}
        self.cpu1 = cpu1
        self.cpu2 = cpu2

    def play(self):
        board = Board()
        player = P1
        self.cpu1.board = board
        self.cpu2.board = board
        while True:
            winner = board.get_winner()
            if winner is not None:
                self.score[winner.number] += 1
                if winner == P1:
                    self.cpu1.reward(10)
                    self.cpu2.reward(-10)
                elif winner == P2:
                    self.cpu1.reward(-10)
                    self.cpu2.reward(10)
                else:
                    self.cpu1.reward(0)
                    self.cpu2.reward(0)
                return
            if player == P1:
                x, y = self.cpu1.get_move()
                board.mark_field(x, y, P1)
            if player == P2:
                x, y = self.cpu2.get_move()
                board.mark_field(x, y, P2)
            player = oppositve(player)

    def print_score(self):
        print(self.score)

    def reset_score(self):
        for i in range(3):
            self.score[i] = 0


if __name__ == '__main__':
    # game = Game(P1)
    # game.play()
    # print('Random vs Qlearn')
    # game = CpuGame(RandomCpu(P1), QLearningCPU(P2, decay=0.99))
    print('Qlearn vs Qlearn')
    # game = CpuGame(QLearningCPU(P1, decay=1.0, epsilon=0.1), QLearningCPU(P2, decay=1.0, epsilon=0.1))
    game = CpuGame(QLearningCPU(P1, decay=0.9999, epsilon=0.2), QLearningCPU(P2, decay=0.9999, epsilon=0.2))

    for _ in range(90):
        for i in range(1000):
            game.play()
            game.cpu2.transfer_experience(game.cpu1.q)
        game.print_score()
        game.reset_score()
        game.cpu1.q = copy.deepcopy(game.cpu2.q)
    cpu2 = copy.deepcopy(game.cpu2)
    cpu1 = copy.deepcopy(game.cpu2)

    cpu2.epsilon = 0
    print('Random vs Qlearn')
    game = CpuGame(RandomCpu(P1), copy.deepcopy(cpu2))
    for i in range(20000):
        game.play()
    game.print_score()
    game.reset_score()

    cpu2.epsilon = 0
    cpu2.transfer_experience(cpu1.q)
    print('Random vs Qlearn transfered')
    game = CpuGame(RandomCpu(P1), copy.deepcopy(cpu2))
    for i in range(20000):
        game.play()
    game.print_score()
    game.reset_score()

    print('Minmax vs Qlearn')

    game = CpuGame(MinMaxCpu(P1), copy.deepcopy(cpu2))
    for i in range(200):
        game.play()
    game.print_score()
    game.reset_score()

    #
    # game = CpuGame(MinMaxCpu(P1), cpu2)
    # for i in range(20):
    #     game.play()
    # game.print_score()
    #
    # cpu2.epsilon = 0
    # print('Random vs Qlearm')
    # game = CpuGame(RandomCpu(P1), cpu2)
    # for i in range(50000):
    #     game.play()
    # game.print_score()

    # print('Random vs Qlearn')
    # cpu2.epsilon = 0.0
    # game = CpuGame(RandomCpu(P1), cpu2)
    # for i in range(50000):
    #     game.play()
    # game.print_score()

    # print('Minmax vs Qlearn')
    # game = CpuGame(MinMaxCpu(P1), cpu2)
    # for i in range(30):
    #     game.play()
    # game.print_score()

    # game = CpuGame(MinMaxCpu, MinMaxCpu)
    # for i in range(10):
    #     game.play()
    # game.print_score()
