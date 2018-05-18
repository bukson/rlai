from unittest import *

from board import Board
from cpu import *

class TestCpu(TestCase):

    def test_min_max(self):
        # 0 X 0
        # 0 _ X
        # _ _ _
        board = Board(np.array([[1, 2, 1], [1, 0, 2], [0, 0, 0]]))
        best_move = MinMaxCpu.min_max(board, P1)
        self.assertTrue(best_move > 0)
        best_move = MinMaxCpu.min_max(board, P2)
        self.assertEqual(best_move, 0)

    def test_get_move(self):
        # 0 X _
        # 0 _ X
        # _ _ _
        board = Board(np.array([[1, 2, 0], [1, 0, 2], [0, 0, 0]]))
        best_move = MinMaxCpu(board, P1).get_move()
        self.assertEqual(best_move, (0,2))

    def test_get_move2(self):
        # 0 0 _
        # _ _ _
        # X _ _
        board = Board(np.array([[1, 1, 0], [0, 0, 0], [2, 0, 0]]))
        best_move = MinMaxCpu(board, P2).get_move()
        self.assertEqual(best_move, (2,0))
