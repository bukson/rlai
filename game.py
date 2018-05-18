import os

from board import Board
from player import *
import numpy as np
from cpu import *

class Game:

    def __init__(self):
        self.board = Board()
        self.cpu = MinMaxCpu(self.board)

    def draw(self):
        print()
        for x in range(3):
            for y in range(3):
                print(players[self.board.board[x][y]].mark + ' ', end='')
            print()
        print()

    def get_human_move(self):
        x, y = map(int, input('What is your move  x y ?\n').split())
        if not self.board.assert_valid_move(x, y):
            self.get_human_move()
        else:
            self.board.mark_field(x, y, P1)

    def get_cpu_move(self):
        x,y = self.cpu.get_move()
        self.board.mark_field(x, y, P2)

    def play(self):
        player = P1
        while True:
            game.draw()
            winner = self.board.get_winner()
            if winner != None:
                if winner == Empty:
                    print('Draw')
                else:
                    print(f'Player {winner.number} won')
                return
            if player == P1:
                game.get_human_move()
            else:
                game.get_cpu_move()
            player = oppositve(player)

if __name__ == '__main__':
    game = Game()
    game.play()
