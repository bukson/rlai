import os

from board import Board
from player import *
import numpy as np
from cpu import *


class Game:

    def __init__(self, first_player=P1):
        self.board = Board()
        self.player = first_player
        self.cpu = MinMaxCpu(self.board, opposite(self.player))

    def get_human_move(self):
        while True:
            x, y = map(int, input('What is your move  x y ?\n').split())
            if (x, y) not in self.board.get_possible_moves():
                continue
            self.board.mark_field(x, y, self.player)
            return

    def get_cpu_move(self):
        x, y = self.cpu.get_move()
        self.board.mark_field(x, y, opposite(self.player))

    def play(self):
        player = self.player
        while True:
            self.board.draw()
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
            player = opposite(player)


class CpuGame:

    def __init__(self, cpu1, cpu2):
        self.score = {0: 0, 1: 0, 2: 0}
        self.players = {P1: cpu1, P2: cpu2}

    def play(self):
        board = Board()
        player = P1
        self.players[P1].start_game()
        self.players[P2].start_game()
        while True:
            x,y = self.players[player].get_move(board)
            board.mark_field(x, y, player)
            winner = board.get_winner()
            if winner is not None:
                self.score[winner.number] += 1
                if winner == Empty:
                    self.players[player].reward(0.5, board)
                    self.players[opposite(player)].reward(0.5, board)
                else:
                    self.players[winner].reward(1, board)
                    self.players[opposite(winner)].reward(-1, board)
                return
            self.players[opposite(player)].reward(0,board)
            player = opposite(player)

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
    game = CpuGame(QLearningCPU(P1, decay=1.0), QLearningCPU(P2, decay=1.0))
    # game = CpuGame(RandomCpu(P1), QLearningCPU(P2, decay=0.9, epsilon=1.0))

    r = 10
    for b in range(r):
        print (b / r, '%')
        for i in range(1000):
            game.play()
        game.print_score()
        print('cpu1.q:', len(game.cpu1.q))
        print('cpu2.q:', len(game.cpu2.q))
        game.reset_score()
        # game.cpu1.q = copy.deepcopy(game.cpu2.q)
    cpu2 = copy.deepcopy(game.cpu2)
    cpu1 = copy.deepcopy(game.cpu1)

    cpu2.epsilon = 0
    cpu2.min_epsilon = 0
    print('Random vs Qlearn')
    game = CpuGame(RandomCpu(P1), copy.deepcopy(cpu2))
    for i in range(20000):
        game.play()
    game.print_score()
    game.reset_score()

    # cpu2.epsilon = 0
    # cpu2.transfer_experience(cpu1.q)
    # print('Random vs Qlearn transfered')
    # game = CpuGame(RandomCpu(P1), copy.deepcopy(cpu2))
    # for i in range(20000):
    #     game.play()
    # game.print_score()
    # game.reset_score()

    print('Minmax vs Qlearn')

    # game = CpuGame(MinMaxCpu(P1), copy.deepcopy(cpu2))
    # for i in range(200):
    #     game.play()
    # game.print_score()
    # game.reset_score()

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
