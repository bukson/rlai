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
        cpu1 = self.cpu1(board, P1)
        cpu2 = self.cpu2(board, P2)
        while True:
            winner = board.get_winner()
            if winner is not None:
                self.score[winner.number] += 1
                return
            if player == P1:
                x, y = cpu1.get_move()
                board.mark_field(x, y, P1)
            if player == P2:
                x, y = cpu2.get_move()
                board.mark_field(x, y, P2)
            player = oppositve(player)

    def print_score(self):
        print(self.score)


if __name__ == '__main__':
    # game = Game(P1)
    # game.play()
    game = CpuGame(RandomCpu, MinMaxCpu)
    for i in range(10):
        game.play()
    game.print_score()

    game = CpuGame(MinMaxCpu, RandomCpu)
    for i in range(10):
        game.play()
    game.print_score()

    game = CpuGame(MinMaxCpu, MinMaxCpu)
    for i in range(10):
        game.play()
    game.print_score()
