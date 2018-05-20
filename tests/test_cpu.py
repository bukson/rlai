from unittest import *

from board import Board
from cpu import *
from profiling import SimpleProfiler
import numpy as np

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
        cpu = MinMaxCpu(P1)
        cpu.board = board
        best_move = cpu.get_move()
        self.assertEqual(best_move, (0,2))

    def test_get_move2(self):
        # 0 0 _
        # _ _ _
        # X _ _
        board = Board(np.array([[1, 1, 0], [0, 0, 0], [2, 0, 0]]))
        cpu = MinMaxCpu(P2)
        cpu.board = board
        best_move = cpu.get_move()
        self.assertEqual(best_move, (2,0))

    def test_get_move3(self):
        board = Board()
        cpu = MinMaxCpu(P1)
        cpu.board = board
        cpu.get_move()

    def test_transfer_state(self):
        state = '1201201201'
        new_state = QLearningCPU._transfer_state(state)
        self.assertEqual(new_state, '2102102102')

    def test_transfer_experience(self):
        state1 = '1201201201'
        state2 = '1122211122'
        cpu1 = QLearningCPU(P1)
        cpu2 = QLearningCPU(P2)
        cpu1.q[state1] = 0.3
        cpu2.q[state2] = 0.0
        cpu2.transfer_experience(cpu1.q)
        self.assertTrue('2102102102' in cpu2.q)
