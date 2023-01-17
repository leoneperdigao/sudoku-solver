import numpy as np


class Sudoku:
    def __init__(self, sudoku: np.array, related_cells, possible_values=None):
        self.__board = np.copy(sudoku)
        self.__related_cells = related_cells
        self.__possible_values = self.__set_initial_possible_values() if possible_values is None else possible_values

    def get_board(self):
        return self.__board

    def get_related_cells(self):
        return self.__related_cells

    def get_possible_values(self):
        return self.__possible_values

    def get_unfinished_possible_values(self):
        return set(k for k, v in self.__possible_values.items())

    def get_unfinished_cells(self, coord_set):
        return [coord for coord in coord_set if coord in self.__possible_values]

    def is_completed(self):
        return len(self.__possible_values) < 1

    def is_valid(self):
        """
        This method checks if the Sudoku puzzle is valid
        It checks if the possible values still contain at least one value for each cell
        Then it checks if the rows and columns are valid using the __is_row_valid() method
        Finally, it checks if the 3x3 squares are valid using the __is_row_valid() method as well
        Returns:
            bool: True if the puzzle is valid, False otherwise
        """
        # possible values must be at least one
        for _, values in self.__possible_values.items():
            if len(values) == 0:
                return False

        # validate rows/cols
        for i in range(0, 9):
            row = self.__board[i, :]
            column = self.__board[:, i]

            if not self.__is_row_valid(row) or not self.__is_row_valid(column):
                return False

        # validate squares
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                square = self.__board[0 + r:3 + r, 0 + c:3 + c]
                if not self.__is_row_valid(square.flatten()):
                    return False

        return True

    def set_value(self, coords, value):
        """
        This method sets the value of a cell in the Sudoku puzzle.
        It checks if the given coordinates are in the possible values
        and if the value is in the possible values of the given cell
        If it is, it sets the cell's value to the given value and remove the cell from the possible values
        Then it updates all related cells, removing the value from their possible values if the cell is not set yet
        If any of the related cells have no possible values, the method returns False
        If any of the related cells have only one possible value, the method recursively calls itself
        with the value and the related cell's coordinates.
        Args:
            coords (tuple): the x,y coordinates of the cell
            value (int): the value to be set in the cell
        Returns:
            bool: True if the value was successfully set, False otherwise
        """
        if coords not in self.__possible_values or value not in self.__possible_values[coords]:
            return False

        self.__board[coords[1]][coords[0]] = value
        del self.__possible_values[coords]

        # update related cells
        for related in self.__related_cells[coords]:
            if related not in self.__possible_values:
                if self.__board[related[1]][related[0]] == value:
                    return False
                continue

            related_values = self.__possible_values[related]
            related_values.discard(value)

            if len(related_values) == 0:
                return False
            if len(related_values) == 1:
                (last_value,) = related_values
                if not self.set_value(related, last_value):
                    return False

        return True

    def __set_initial_possible_values(self):
        """
        This method initializes the possible values for each cell in the Sudoku puzzle.
        It uses the numpy 'where' function to get the empty cells coordinates in the board.
        Then it creates a dictionary where the keys are the coordinates of the empty cells
        and the values are the set of all possible values from 1 to 9.
        Returns:
            dict: dictionary containing the possible values for each empty cell
        """
        possibilities = dict()
        empty_cells = np.where(self.__board == 0)
        coords = list(zip(empty_cells[1], empty_cells[0]))
        for coord in coords:
            possibilities[coord] = set(range(1, 10))
        return possibilities

    @staticmethod
    def __is_row_valid(row):
        return len(row) == 9 and sum(row) == sum(set(row))
