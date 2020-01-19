import random
import sys
from exceptions import InvalidGameBoardException
from spaces import SpaceValue 

class GameBoard(object):

    def __init__(self, rows, cols, mines):
        if mines >= (rows*cols):
            raise InvalidGameBoardException('Too many mines. You must have 1 less mine than the total number of spaces')
        self._rows = int(rows)
        self._cols = int(cols)
        self._size = rows*cols
        self._num_spaces = self._size - 1
        self._mines = mines
        self.spaces = None

        self.clear_board()

    def clear_board(self):
        self.spaces = [SpaceValue('blank') for _ in range(self._size)]

    def generate_board(self):
        mine_positions = random.sample(range(self._size), self._mines)
        for mine_position in mine_positions:
            self.spaces[mine_position] = SpaceValue('mine')

        for space in range(self._size):
            if not self.spaces[space].is_mine():
                num_mines = self._get_num_mines(space)
                self.spaces[space] = SpaceValue(num_mines)

    def size(self):
        return self._size

    def rows(self):
        return self._rows

    def cols(self):
        return self._cols

    def all_revealed(self):
        for space in range(self._size):
            if not self.spaces[space].is_revealed() and not self.spaces[space].is_mine():
                return False

        return True

    def is_left_border(self, space):
        return not space % self._cols

    def is_right_border(self, space):
        return (space % self._cols) == (self._cols - 1)

    def is_top_border(self, space):
        return (space - self._cols) < 0

    def is_bottom_border(self, space):
        return (space + self._cols) > self._num_spaces

    def has_adjacent_revealed_blank(self, space):
        adjacent_space_values = self._get_adjacent_space_values(space)
        for adjacent_space_value in adjacent_space_values:
            if adjacent_space_value.is_revealed() and adjacent_space_value.is_blank():
                return True

        return False

    def _get_adjacent_space_values(self, space):
        adjacent_space_values = []
        adjacent_space_values.append(self._get_top_left_value(space))
        adjacent_space_values.append(self._get_top_value(space))
        adjacent_space_values.append(self._get_top_right_value(space))
        adjacent_space_values.append(self._get_right_value(space))
        adjacent_space_values.append(self._get_bottom_right_value(space))
        adjacent_space_values.append(self._get_bottom_value(space))
        adjacent_space_values.append(self._get_bottom_left_value(space))
        adjacent_space_values.append(self._get_left_value(space))

        return [value for value in adjacent_space_values if value]

    def _get_num_mines(self, space):
        num_mines = 0
        adjacent_space_values = self._get_adjacent_space_values(space)
        for adjacent_space_value in adjacent_space_values:
            if adjacent_space_value.is_mine():
                num_mines += 1

        # Use negative numbers to represent unknown number spaces
        return num_mines * -1 

    def _get_top_left_value(self, space):
        if self.is_left_border(space):
            return None

        value_pos = space - self._cols - 1
        if value_pos < 0:
            return None

        return self.spaces[value_pos]

    def _get_top_value(self, space):
        value_pos = space - self._cols
        if value_pos < 0:
            return None

        return self.spaces[value_pos]

    def _get_top_right_value(self, space):
        if self.is_right_border(space):
            return None

        value_pos = space - self._cols + 1
        if value_pos < 0:
            return None

        return self.spaces[value_pos]        

    def _get_right_value(self, space):
        if self.is_right_border(space):
            return None

        value_pos = space + 1
        if value_pos > self._num_spaces:
            return None

        return self.spaces[value_pos]

    def _get_bottom_right_value(self, space):
        if self.is_right_border(space):
            return None

        value_pos = space + self._cols + 1
        if value_pos > self._num_spaces:
            return None

        return self.spaces[value_pos]

    def _get_bottom_value(self, space):
        value_pos = space + self._cols
        if value_pos > self._num_spaces:
            return None

        return self.spaces[value_pos]

    def _get_bottom_left_value(self, space):
        if self.is_left_border(space):
            return None

        value_pos = space + self._cols - 1
        if value_pos > self._num_spaces:
            return None

        return self.spaces[value_pos]

    def _get_left_value(self, space):
        if self.is_left_border(space):
            return None
        value_pos = space - 1
        if value_pos < 0:
            return None

        return self.spaces[value_pos]

