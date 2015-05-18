"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
Online version: http://www.codeskulptor.org/#user40_z4gNwFVH3S_26.py
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    def basic_move_tile(self, from_row, from_col, to_row, to_col):
        """
        A general method to move a tile from one place to aother.
        This method can't move a tile to the first row.
        """
        assert self._grid[to_row][to_col] == 0, 'Input not equal to 0'
        approach_string = ''
        for idx in xrange(to_row-from_row):
            approach_string += 'u'
        if to_col > from_col:
            for idx in xrange(to_col-from_col):
                approach_string += 'l'
            if from_row == 0:
                approach_string += 'dru'
                from_row += 1
            else:
                approach_string += 'ur'
            from_col += 1
        else:
            for idx in xrange(from_col-to_col):
                approach_string += 'r'
            if from_row == 0:
                approach_string += 'dlu'
                from_row += 1
            else:
                approach_string += 'ul'
            from_col -= 1
        self.update_puzzle(approach_string)

        return_string = ''
        for idx in xrange(to_col-from_col):
            return_string += 'rdlur'
        for idx in xrange(from_col-to_col):
            return_string += 'ldrul'
        for idx in xrange(to_row-from_row):
            return_string += 'lddru'
        return_string += 'ld'
        self.update_puzzle(return_string)
        return approach_string + return_string


    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        if self._grid[target_row][target_col] != 0:
            return False
        for idx, block in enumerate(self._grid[target_row][target_col+1:], start=1):
            if block != target_row * self._width + target_col + idx:
                return False
        for r_idx, row in enumerate(self._grid[target_row+1:], start=target_row+1):
            for c_idx, block in enumerate(row):
                if block != r_idx * self._width + c_idx:
                    return False 
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # assert self.lower_row_invariant(target_row, target_col), 'Input not correct'
        correct_tile = self.current_position(target_row, target_col)
        move_string = self.basic_move_tile(correct_tile[0], correct_tile[1], target_row, target_col)
        # assert self.lower_row_invariant(target_row, target_col-1), 'Return wrong string '+move_string
        return move_string

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # assert self.lower_row_invariant(target_row, 0), 'Input not correct'

        self.update_puzzle('ur')
        if self._grid[target_row][0] == target_row * self._width:
            move_string = 'u' + 'r' * (self._width - 1)
            self.update_puzzle( 'r' * (self._width - 2))
            return move_string

        correct_tile = self.current_position(target_row, 0)
        move_string = self.basic_move_tile(correct_tile[0], correct_tile[1], target_row-1, 1)

        magic_solve_string = 'ruldrdlurdluurddlu' + 'r' * (self._width-1)
        self.update_puzzle(magic_solve_string)

        # assert self.lower_row_invariant(target_row-1, self._width-1), 'Return wrong string'
        return 'ur' + move_string + magic_solve_string

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self._grid[0][target_col] != 0:
            return False
        for idx, block in enumerate(self._grid[0][target_col+1:], start=1):
            if block != target_col + idx:
                return False
        for idx, block in enumerate(self._grid[1][target_col:]):
            if block != self._width + target_col + idx:
                return False
        for r_idx, row in enumerate(self._grid[2:], start=2):
            for c_idx, block in enumerate(row):
                if block != r_idx * self._width + c_idx:
                    return False
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self._grid[1][target_col] != 0:
            return False
        for idx, block in enumerate(self._grid[1][target_col+1:], start=1):
            if block != self._width + target_col + idx:
                return False
        for r_idx, row in enumerate(self._grid[2:], start=2):
            for c_idx, block in enumerate(row):
                if block != r_idx * self._width + c_idx:
                    return False 
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row0_invariant(target_col), 'Input not correct'
        self.update_puzzle('ld')
        if self._grid[0][target_col] == target_col:
            assert self.row1_invariant(target_col-1)
            return 'ld'
        move_string = ''
        correct_tile = self.current_position(0, target_col)
        for idx in xrange(target_col-correct_tile[1]-1):
            move_string += 'l'
        if correct_tile[0] == 0:
            move_string += 'uld'
        for idx in xrange(target_col-correct_tile[1]-2):
            move_string += 'urrdl'
        self.update_puzzle(move_string)
        magic_solve_string = 'urdlurrdluldrruld'
        self.update_puzzle(magic_solve_string)
        assert self.row1_invariant(target_col-1), '\n'+str(self)
        return 'ld' + move_string + magic_solve_string

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # assert self.row1_invariant(target_col), 'Input not correct'
        if self._grid[0][target_col] == self._width + target_col:
            self.update_puzzle('u')
            assert self.row0_invariant(target_col)
            return 'u'
        correct_tile = self.current_position(1, target_col)
        move_string = self.basic_move_tile(correct_tile[0], correct_tile[1], 1, target_col)
        self.update_puzzle('ur')
        # assert self.row0_invariant(target_col), 'Return wrong string'
        return move_string + 'ur'

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

# Start interactive simulation
if __name__ == '__main__':
    poc_fifteen_gui.FifteenGUI(Puzzle(5, 5))


