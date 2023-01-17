import unittest
import numpy as np

from sudoku_solver import SudokuSolver


class TestSudokuSolver(unittest.TestCase):
    def test_get_solution(self):
        sample_sudoku = np.array([
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
        solver = SudokuSolver(sample_sudoku)
        solver.try_find_solution()
        correct_solution = np.array([
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7]
        ])
        self.assertTrue(solver.try_find_solution())
        self.assertTrue(np.array_equal(solver.get_solution(), correct_solution))

    def test_solve_easy_sudoku(self):
        # easy sudoku
        easy_sudoku = np.array([
            [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]
        ])
        solver = SudokuSolver(easy_sudoku)
        expected_sudoku = np.array([
            [3, 1, 6, 5, 7, 8, 4, 9, 2],
            [5, 2, 9, 1, 3, 4, 7, 6, 8],
            [4, 8, 7, 6, 2, 9, 5, 3, 1],
            [2, 6, 3, 4, 1, 5, 9, 8, 7],
            [9, 7, 4, 8, 6, 3, 1, 2, 5],
            [8, 5, 1, 7, 9, 2, 6, 4, 3],
            [1, 3, 8, 9, 4, 7, 2, 5, 6],
            [6, 9, 2, 3, 5, 1, 8, 7, 4],
            [7, 4, 5, 2, 8, 6, 3, 1, 9]
        ])
        self.assertTrue(solver.try_find_solution())
        self.assertTrue(np.array_equal(solver.get_solution(), expected_sudoku))

    def test_solve_medium_sudoku(self):
        # medium sudoku
        medium_sudoku = np.array([
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0]
        ])
        solver = SudokuSolver(medium_sudoku)
        expected_sudoku = np.array([
            [8, 1, 2, 7, 5, 3, 6, 4, 9],
            [9, 4, 3, 6, 8, 2, 1, 7, 5],
            [6, 7, 5, 4, 9, 1, 2, 8, 3],
            [1, 5, 4, 2, 3, 7, 8, 9, 6],
            [3, 6, 9, 8, 4, 5, 7, 2, 1],
            [2, 8, 7, 1, 6, 9, 5, 3, 4],
            [5, 2, 1, 9, 7, 4, 3, 6, 8],
            [4, 3, 8, 5, 2, 6, 9, 1, 7],
            [7, 9, 6, 3, 1, 8, 4, 5, 2]
        ])
        self.assertTrue(solver.try_find_solution())
        self.assertTrue(np.array_equal(solver.get_solution(), expected_sudoku))

    def test_solve_hard_sudoku(self):
        # hard sudoku
        hard_sudoku = np.array([
            [0, 0, 0, 6, 0, 0, 4, 0, 0],
            [7, 0, 0, 0, 0, 3, 6, 0, 0],
            [0, 0, 0, 0, 9, 1, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 1, 8, 0, 0, 0, 3],
            [0, 0, 0, 3, 0, 0, 0, 0, 0],
            [0, 4, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 5, 0, 0, 0, 0, 7, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0]
        ])
        solver = SudokuSolver(hard_sudoku)
        expected_sudoku = np.array([
            [1, 3, 8, 6, 2, 5, 4, 9, 7],
            [7, 2, 9, 8, 4, 3, 6, 1, 5],
            [5, 6, 4, 7, 9, 1, 3, 8, 2],
            [8, 1, 3, 4, 5, 2, 7, 6, 9],
            [6, 5, 7, 1, 8, 9, 2, 4, 3],
            [4, 9, 2, 3, 7, 6, 8, 5, 1],
            [9, 4, 6, 2, 1, 7, 5, 3, 8],
            [2, 8, 5, 9, 3, 4, 1, 7, 6],
            [3, 7, 1, 5, 6, 8, 9, 2, 4],
        ])
        self.assertTrue(solver.try_find_solution())
        self.assertTrue(np.array_equal(solver.get_solution(), expected_sudoku))

    def test_solve_invalid_sudoku(self):
        # invalid sudoku (same number in same row)
        invalid_sudoku = np.array([
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 8, 9, 1, 2, 3, 4, 5]
        ])
        solver = SudokuSolver(invalid_sudoku)
        self.assertFalse(solver.try_find_solution())
        self.assertTrue(np.array_equal(solver.get_solution(), np.full((9, 9), -1)))

    def test_solve_unsolvable_sudoku(self):
        # unsolvable sudoku (impossible to place a number in a cell)
        unsolvable_sudoku = np.array(
            [[0, 8, 0, 4, 3, 0, 0, 0, 0],
             [0, 0, 5, 0, 0, 9, 0, 0, 0],
             [6, 0, 0, 0, 8, 0, 0, 7, 0],
             [0, 0, 0, 0, 9, 0, 0, 0, 3],
             [0, 0, 0, 8, 0, 7, 0, 0, 0],
             [9, 0, 0, 0, 0, 0, 0, 5, 4],
             [0, 6, 0, 0, 0, 0, 0, 0, 5],
             [0, 0, 8, 0, 0, 0, 4, 0, 0],
             [0, 4, 0, 0, 0, 6, 0, 1, 0]]
        )
        solver = SudokuSolver(unsolvable_sudoku)
        self.assertFalse(solver.try_find_solution())
        self.assertTrue(np.array_equal(solver.get_solution(), np.full((9, 9), -1)))



