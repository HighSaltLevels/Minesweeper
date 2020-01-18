import random
import sys
from exceptions import InvalidGameBoardException

class GameBoard(object):

    def __init__(self, rows, cols, mines):
        if mines >= (rows*cols):
            raise InvalidGameBoardException('Too many mines. You must have 1 less mine than the total number of spaces')
        self.rows = int(rows)
        self.cols = int(cols)
        self.size = rows*cols
        self.num_spaces = self.size - 1
        self.mines = mines
        self.game_board = None
        self.clear_board()

    def generate_board(self):
        mine_positions = random.sample(range(0, self.rows*self.cols), self.mines)
        for mine_position in mine_positions:
            self.game_board[mine_position] = 'mine'

        for space in range(self.size):
            if not self.game_board[space]:
                self.game_board[space] = self.get_num_mines(space)

    def get_num_mines(self, space):
        num_mines = 0
        adjacent_space_values = self.get_adjacent_space_values(space)
        for adjacent_space_value in adjacent_space_values:
            if adjacent_space_value == 'mine':
                num_mines += 1

        return str(num_mines * -1) # Use negative numbers to represent unknown number spaces

    def get_adjacent_space_values(self, space):
        adjacent_space_values = []
        adjacent_space_values.append(self.get_top_left_value(space))
        adjacent_space_values.append(self.get_top_value(space))
        adjacent_space_values.append(self.get_top_right_value(space))
        adjacent_space_values.append(self.get_right_value(space))
        adjacent_space_values.append(self.get_bottom_right_value(space))
        adjacent_space_values.append(self.get_bottom_value(space))
        adjacent_space_values.append(self.get_bottom_left_value(space))
        adjacent_space_values.append(self.get_left_value(space))

        return [value for value in adjacent_space_values if value]

    def set_value(self, space, value):
        self.game_board[space] = value

    def get_value(self, space):
        return self.game_board[space]

    def get_top_left_value(self, space):
        if self.is_left_border(space):
            return None

        value_pos = space - self.cols - 1
        if value_pos < 0:
            return None

        return self.game_board[value_pos]

    def get_top_value(self, space):
        value_pos = space - self.cols
        if value_pos < 0:
            return None

        return self.game_board[value_pos]

    def get_top_right_value(self, space):
        if self.is_right_border(space):
            return None

        value_pos = space - self.cols + 1
        if value_pos < 0:
            return None

        return self.game_board[value_pos]        

    def get_right_value(self, space):
        if self.is_right_border(space):
            return None

        value_pos = space + 1
        if value_pos > self.num_spaces:
            return None

        return self.game_board[value_pos]

    def get_bottom_right_value(self, space):
        if self.is_right_border(space):
            return None

        value_pos = space + self.cols + 1
        if value_pos > self.num_spaces:
            return None

        return self.game_board[value_pos]

    def get_bottom_value(self, space):
        value_pos = space + self.cols
        if value_pos > self.num_spaces:
            return None

        return self.game_board[value_pos]

    def get_bottom_left_value(self, space):
        if self.is_left_border(space):
            return None

        value_pos = space + self.cols - 1
        if value_pos > self.num_spaces:
            return None

        return self.game_board[value_pos]

    def get_left_value(self, space):
        if self.is_left_border(space):
            return None
        value_pos = space - 1
        if value_pos < 0:
            return None

        return self.game_board[value_pos]

    def is_left_border(self, space):
        return not space % self.cols

    def is_right_border(self, space):
        return (space % self.cols) == (self.cols - 1)

    def is_top_border(self, space):
        return (space - self.cols) < 0

    def is_bottom_border(self, space):
        return (space + self.cols) > self.num_spaces

    def is_mine(self, space):
        return self.game_board[space] == 'mine'

    def is_blank(self, space):
        return self.is_revealed_blank(space) or self.is_unrevealed_space(space)

    def is_revealed_blank(self, space):
        return self.game_board[space] == ' '

    def is_unrevealed_blank(self, space):
        return self.game_board[space] == '0'

    def is_revealed(self, space):
        try:
            value = int(self.game_board[space])
            return value > 0
        except ValueError:
            return False

    def is_unrevealed(self, space):
        try:
            value = int(self.game_board[space])
            return value < 0
        except ValueError:
            return False

    def all_revealed(self):
        victory = True
        for space in range(self.size):
            if self.is_unrevealed(space):
                return False

        return True

    def clear_board(self):
        self.game_board = [None for _ in range(self.size)]
