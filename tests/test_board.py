from unittest import *

from board import Board
import numpy as np

class TestBoard(TestCase):

    def test_init(self):
        board = Board()
        for i in range(3):
            for j in range(3):
                self.assertTrue(board.board[i][j] == 0)

    def test_get_winner(self):
        board = Board()
        self.assertEqual(board.get_winner(), 0)

        board = Board(np.array([[1,0,0], [0,1,0], [0,0,1]]))
        self.assertEqual(board.get_winner(), 1)

        board = Board(np.array([[2, 0, 0], [2, 0, 0], [2, 0, 0]]))
        self.assertEqual(board.get_winner(), 2)

        board = Board(np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]]))
        self.assertEqual(board.get_winner(), 2)

        board = Board(np.array([[0, 0, 2], [0, 2, 0], [2, 0, 0]]))
        self.assertEqual(board.get_winner(), 2)
