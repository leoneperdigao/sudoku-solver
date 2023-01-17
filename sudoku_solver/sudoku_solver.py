import copy

import numpy as np

from .sudoku import Sudoku


class SudokuSolver:
    def __init__(self, sudoku, related_cells=None, possible_values=None):
        self.__related_cells = related_cells
        self.__is_valid = True

        if self.__related_cells is None:
            self.__init_related_cells_cache()

        self.__sudoku = Sudoku(sudoku, self.__related_cells, possible_values)

        if possible_values is None:
            self.__ac3_prune_possible_values()
            self.__is_valid = self.__sudoku.is_valid()

    def get_sudoku(self):
        return self.__sudoku

    def get_related_cells(self):
        return self.__related_cells

    def get_solution(self):
        """
        Returns the solution of the Sudoku puzzle if it is solved.
        Returns:
            list: 2D list representing the solution of the puzzle
        """
        if not self.get_sudoku().is_completed() or not self.__is_valid:
            return np.full((9, 9), -1)

        return self.get_sudoku().get_board()

    def try_find_solution(self):
        """
        Tries to solve the Sudoku puzzle.
        Returns:
            bool: True if the puzzle is solved successfully, False otherwise
        """
        if not self.__is_valid:
            return False

        if self.get_sudoku().is_completed() and self.__is_valid:
            return True

        return self.__search()

    def __ac3_prune_possible_values(self):
        """
        This method uses the AC-3 algorithm to prune the possible values for each cell in the Sudoku puzzle.
        The algorithm uses the concept of arc consistency, where it iteratively removes values that cannot be
        placed in a cell without breaking the constraints of the puzzle.
        """
        # make shallow 'copy' to keep obj reference
        sudoku = self.__sudoku
        queue = self.__sudoku.get_unfinished_possible_values()

        while len(queue) > 0:
            changed = False
            current = queue.pop()
            element_values = self.get_sudoku().get_possible_values()[current]
            all_related_cells = sudoku.get_related_cells()[current]

            for cell in all_related_cells:
                if current not in sudoku.get_possible_values():
                    continue
                value = sudoku.get_board()[cell[1], cell[0]]
                if value in element_values:
                    sudoku.get_possible_values()[current].remove(value)
                    if len(sudoku.get_possible_values()[current]) == 1:
                        (last_val,) = sudoku.get_possible_values()[current]
                        # last element
                        sudoku.get_board()[current[1], current[0]] = last_val
                        # remove impossible value
                        del sudoku.get_possible_values()[current]
                        changed = True

            if changed:
                queue.union(sudoku.get_unfinished_cells(all_related_cells))

    def __set_value(self, coord, value):
        """
        This method sets the value of a cell in the Sudoku puzzle.
        It creates a new solver instance with a copy of the current board, related cells and possible values.
        Then it uses the set_value() method of the Sudoku class to set the value of the cell.
        Args:
            coord (tuple): the x,y coordinates of the cell
            value (int): the value to be set in the cell
        Returns:
            object: the new solver instance
        """
        new_solver = SudokuSolver(
            self.get_sudoku().get_board(),
            self.get_related_cells(),
            copy.deepcopy(self.get_sudoku().get_possible_values())
        )
        new_solver.__is_valid = new_solver.get_sudoku().set_value(coord, value)
        return new_solver

    def __search(self):
        """
        This method is responsible for trying to solve a Sudoku puzzle.
        It uses a backtracking search strategy where it starts with the cell with the smallest domain and
        proceeds down in the branch where it sets the cell to a certain value and then recursively calls itself.
        If it reaches a point where there are no valid values for the cell, it backtracks to the previous
        call and tries the next value for the cell.
        Returns:
            bool: True if the puzzle is solved successfully, False otherwise
        """
        queue = [(k, v) for k, v in self.get_sudoku().get_possible_values().items()]
        queue.sort(key=lambda item: len(item[1]))
        while len(queue) > 0:
            coordinates, poss = queue.pop(0)
            for value in poss:
                new_solver = self.__set_value(coordinates, value)
                if new_solver.try_find_solution():
                    self.__sudoku = new_solver.get_sudoku()
                    return True
            break

        return False

    def __init_related_cells_cache(self):
        """
        Calculates the related cells for each cell in the puzzle and populates the related_cells cache.
        """
        self.__related_cells = dict()
        rows, cols = np.meshgrid(range(9), range(9), indexing='ij')
        for (r, c) in zip(rows.ravel(), cols.ravel()):
            coordinates = (c, r)
            self.__related_cells[coordinates] = SudokuSolver.__calculate_related_cells((c, r))

    @staticmethod
    def __calculate_related_cells(coordinates):
        """
        Returns a set of coordinates representing the cells that are related to the input cell.
        This includes cells in the same row, column, and square as the input cell.

        Parameters:
            coordinates (tuple): a tuple of integers representing the (x, y) coordinates of the cell in the puzzle

        Returns:
            set: a set of tuples representing the coordinates of related cells
        """
        related = set()

        related.update({(i, coordinates[1]) for i in range(9)})
        related.update({(coordinates[0], i) for i in range(9)})

        square_x = int((coordinates[0]) / 3) * 3
        square_y = int((coordinates[1]) / 3) * 3

        related.update({(square_x + x, square_y + y) for x in range(3) for y in range(3)})
        related.remove(coordinates)

        return related

