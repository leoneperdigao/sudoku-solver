import unittest
import numpy as np

from sudoku_solver import Sudoku


class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.sudoku = np.array([
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ])
        self.sudoku_obj = Sudoku(self.sudoku)

    def test_get_board(self):
        self.assertTrue(np.array_equal(self.sudoku_obj.get_board(), self.sudoku))

    def test_is_completed(self):
        self.assertFalse(self.sudoku_obj.is_completed())
        for i in range(9):
            self.sudoku_obj.set_value((i, 0), i + 1)
        self.assertTrue(self.sudoku_obj.is_completed())

    def test_is_valid(self):
        self.assertTrue(self.sudoku_obj.is_valid())
        self.sudoku_obj.set_value((0, 0), 1)
        self.assertTrue(self.sudoku_obj.is_valid())
        self.sudoku_obj.set_value((0, 1), 1)
        self.assertFalse(self.sudoku_obj.is_valid())

    def test_set_value(self):
        self.assertTrue(self.sudoku_obj.set_value((0, 0), 1))
        self.assertFalse(self.sudoku_obj.set_value((0, 0), 2))
        self.assertFalse(self.sudoku_obj.set_value((10, 10), 2))
        self.assertFalse(self.sudoku_obj.set_value((0, 1), 10))

    def test_get_possible_values(self):
        self.assertEqual(self.sudoku_obj.get_possible_values(), self.sudoku_obj.__set_initial_possible_values())
        self.sudoku_obj.set_value((0, 0), 1)
        self.assertNotEqual(self.sudoku_obj.get_possible_values(), self.sudoku_obj.__set_initial_possible_values())

    def test_valid_line(self):
        self.assertTrue(Sudoku.__is_valid_line([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertFalse(Sudoku.__is_valid_line([1, 2, 3, 4, 5, 6, 7, 8, 8]))
        self.assertFalse(Sudoku.__is_valid_line([1, 2, 3, 4, 5, 6, 7, 8]))
