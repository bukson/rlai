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

    def test_assert_valid_move(self):
        board = Board()
        board.mark_field(1, 1, P1)
        self.assertTrue(board.assert_valid_move(0, 0))
        self.assertFalse(board.assert_valid_move(1, 1))
        self.assertFalse(board.assert_valid_move(3, 3))
        self.assertFalse(board.assert_valid_move(-1, -1))
