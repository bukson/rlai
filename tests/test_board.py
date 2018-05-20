from unittest import *

from board import Board
from player import *
import numpy as np


class TestBoard(TestCase):

    def test_init(self):
        board = Board()
        for i in range(3):
            for j in range(3):
                self.assertTrue(board.board[i][j] == 0)

    def test_get_winner(self):
        board = Board()
        self.assertEqual(board.get_winner(), None)

        board = Board(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
        self.assertEqual(board.get_winner(), P1)

        board = Board(np.array([[2, 0, 0], [2, 0, 0], [2, 0, 0]]))
        self.assertEqual(board.get_winner(), P2)

        board = Board(np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]]))
        self.assertEqual(board.get_winner(), P2)

        board = Board(np.array([[0, 0, 2], [0, 2, 0], [2, 0, 0]]))
        self.assertEqual(board.get_winner(), P2)

        board = Board(np.array([[2, 1, 2], [2, 1, 1], [1, 2, 2]]))
        self.assertEqual(board.get_winner(), Empty)

    def test_mark_field(self):
        board = Board()
        board.mark_field(1, 1, P1)
        self.assertEqual(board.board[1][1], 1)

    def test_get_possible_moves(self):
        # 0 X _
        # _ X O
        # X _ X
        board = Board(np.array([[1,2,0], [0,2,1], [2,0,2]]))
        moves = board.get_possible_moves()
        self.assertIn((2,0), moves)

    def test_hash(self):
        b1 = Board(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
        b2 = Board(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
        self.assertEqual(b1.__hash__(), b2.__hash__())
        d = {b1: 3}
        self.assertTrue(b1 in d)